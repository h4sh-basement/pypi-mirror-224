import os.path

import io
import string
import base64
from time import sleep

import oss2
import pyarrow as pa
import logging
import enum
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED

from qcloud_cos import CosConfig, CosS3Client

logger = logging.getLogger(__name__)


class QueryDataType(enum.Enum):
    Memory = 0
    File = 1


class ObjectStorageType(enum.Enum):
    OSS = 0
    COS = 1


class QueryData(object):
    def __init__(self, data: list, data_type: QueryDataType, file_list: list = None,
                 object_storage_type: ObjectStorageType = None, oss_bucket: oss2.Bucket = None,
                 cos_client: CosS3Client = None):
        self.data = data
        self.data_type = data_type
        self.file_list = file_list
        self.object_storage_type = object_storage_type
        self.oss_bucket = oss_bucket
        self.cos_client = cos_client
        self.current_file_index = 0
        self.memory_read = False

    def read(self):
        if self.data_type == QueryDataType.Memory:
            if self.memory_read:
                return None
            self.memory_read = True
            return self.data
        elif self.data_type == QueryDataType.File:
            assert self.file_list is not None
            try:
                if self.current_file_index >= len(self.file_list):
                    return None
                file = self.file_list[self.current_file_index]
                file_info = file.split('/', 3)
                result = []
                if self.object_storage_type == ObjectStorageType.OSS:
                    stream = self.oss_bucket.get_object(file_info[3]).read()
                    with pa.ipc.RecordBatchStreamReader(stream) as reader:
                        self.current_file_index += 1
                        for index, row in reader.read_pandas().iterrows():
                            result.append(tuple(row.to_list()))
                        return result
                elif self.object_storage_type == ObjectStorageType.COS:
                    with self.cos_client.get_object(Bucket=file_info[2], Key=file_info[3])['Body'].get_raw_stream() as stream:
                        with pa.ipc.RecordBatchStreamReader(stream) as reader:
                            self.current_file_index += 1
                            for index, row in reader.read_pandas().iterrows():
                                result.append(tuple(row.to_list()))
                            return result
            except Exception as e:
                logger.error(f'Error while converting from arrow to result: {e}')
                raise Exception(f'Error while converting from arrow to result: {e}')


class Field(object):
    def __init__(self):
        self.name = None
        self.field_type = None
        self.precision = None
        self.scale = None
        self.length = None
        self.nullable = None

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.field_type = type

    def set_precision(self, precision):
        self.precision = precision

    def set_scale(self, scale):
        self.scale = scale

    def set_length(self, length):
        self.length = length

    def set_nullable(self, nullable):
        self.nullable = nullable


class QueryResult(object):
    def __init__(self, total_msg):
        self.data = None
        self.state = None
        self.total_row_count = 0
        self.total_msg = total_msg
        self.schema = []
        self._parse_result_data()

    def _parse_field(self, field: str, schema_field: Field):
        schema_field.set_name(field['name'])
        if field['type'].__contains__('charTypeInfo'):
            schema_field.set_type(field['type']['category'])
            schema_field.set_nullable(str(field['type']['nullable']) != 'False')
            schema_field.set_length(field['type']['charTypeInfo']['length'])
        elif field['type'].__contains__('decimalTypeInfo'):
            schema_field.set_type(field['type']['category'])
            schema_field.set_nullable(str(field['type']['nullable']) == 'true')
            schema_field.set_precision(field['type']['decimalTypeInfo']['precision'])
            schema_field.set_scale(field['type']['decimalTypeInfo']['scale'])
        else:
            schema_field.set_type(field['type']['category'])
            schema_field.set_nullable(str(field['type']['nullable']) == 'true')

    def get_result_state(self) -> string:
        return self.total_msg['status']['state']

    def get_arrow_result(self, arrow_buffer):
        try:
            buffer = base64.b64decode(arrow_buffer)
            with pa.ipc.RecordBatchStreamReader(io.BytesIO(buffer)) as reader:
                pandas_result = reader.read_all().to_pandas()
                result = []
                for index, row in pandas_result.iterrows():
                    result.append(tuple(row.tolist()))
                return result

        except Exception as e:
            logger.error(f'Error while converting from arrow to result: {e}')
            raise Exception(f'Error while converting from arrow to result: {e}')

    def get_result_schema(self):
        fields = self.total_msg['resultSet']['metadata']['fields']
        for field in fields:
            schema_field = Field()
            self._parse_field(field, schema_field)
            self.schema.append(schema_field)

    def get_object_storage_type(self) -> ObjectStorageType:
        object_storage_type = self.total_msg['resultSet']['location']['fileSystem']
        if object_storage_type == 'OSS':
            return ObjectStorageType.OSS
        elif object_storage_type == 'COS':
            return ObjectStorageType.COS

    def get_object_storage_file_list(self) -> list:
        object_storage_file_list = self.total_msg['resultSet']['location']['location']
        return object_storage_file_list

    def get_oss_bucket(self) -> oss2.Bucket:
        location_info = self.total_msg['resultSet']['location']
        id = location_info['stsAkId']
        secret = location_info['stsAkSecret']
        token = location_info['stsToken']
        endpoint = location_info['ossEndpoint']
        if len(location_info['location']) == 0:
            raise Exception('No file found in oss when get result from clickzetta')
        bucket_name = location_info['location'][0].split('/', 3)[2]
        auth = oss2.StsAuth(id, secret, token)
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        return bucket

    def get_cos_client(self) -> CosS3Client:
        location_info = self.total_msg['resultSet']['location']
        region = location_info['objectStorageRegion']
        id = location_info['stsAkId']
        secret = location_info['stsAkSecret']
        token = location_info['stsToken']
        cos_config = CosConfig(Region=region, SecretId=id, SecretKey=secret, Token=token)
        client = CosS3Client(cos_config)
        return client

    def _parse_result_data(self):
        self.state = self.total_msg['status']['state']
        if self.state != 'FAILED':
            if 'data' not in self.total_msg['resultSet']:
                if 'location' in self.total_msg['resultSet']:
                    self.get_result_schema()
                    file_list = self.get_object_storage_file_list()
                    object_storage_type = self.get_object_storage_type()
                    if object_storage_type == ObjectStorageType.OSS:
                        self.data = QueryData(data_type=QueryDataType.File, file_list=file_list, data=None,
                                              object_storage_type=object_storage_type, oss_bucket=self.get_oss_bucket())
                    elif object_storage_type == ObjectStorageType.COS:
                        self.data = QueryData(data_type=QueryDataType.File, file_list=file_list, data=None,
                                              object_storage_type=object_storage_type, cos_client=self.get_cos_client())

                else:
                    field = Field()
                    field.set_name('RESULT_MESSAGE')
                    field.set_type("STRING")
                    self.schema.append(field)
                    self.total_row_count = 1
                    result_data = [['OPERATION SUCCEED']]
                    self.data = QueryData(data=result_data, data_type=QueryDataType.Memory)
            else:
                if not (len(self.total_msg['resultSet']['data']['data'])):
                    self.total_row_count = 0
                    fields = self.total_msg['resultSet']['metadata']['fields']
                    for field in fields:
                        schema_field = Field()
                    self._parse_field(field, schema_field)
                    self.schema.append(schema_field)
                    self.data = QueryData(data=[], data_type=QueryDataType.Memory)
                    return
                result_data = self.total_msg['resultSet']['data']['data']
                self.get_result_schema()
                query_result = []
                for row in result_data:
                    partial_result = self.get_arrow_result(row)
                    query_result.extend(entity for entity in partial_result)
                self.data = QueryData(data=query_result, data_type=QueryDataType.Memory)

        else:
            raise Exception('SQL job execute failed.Error:' + self.total_msg['status']['message'].split('\n')[0])
