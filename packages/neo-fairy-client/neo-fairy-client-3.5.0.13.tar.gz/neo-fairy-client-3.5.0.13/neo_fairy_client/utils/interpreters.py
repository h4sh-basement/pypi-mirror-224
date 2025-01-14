from typing import List
from math import log
import base64


class Interpreter:
    @staticmethod
    def bytes_to_int(bytes_: bytes):
        return int.from_bytes(bytes_, byteorder='little', signed=False)
    
    @staticmethod
    def int_to_bytes(int_: int, bytes_needed: int = None):
        if int_ == 0:
            return b''
        if int_ < 0:
            raise ValueError(f'Cannot handle minus numbers. Got {int_}')
        if not bytes_needed:
            bytes_needed = int(log(int_, 256)) + 1  # may be not accurate
        try:
            return int_.to_bytes(bytes_needed, 'little')
        except OverflowError:
            return int_.to_bytes(bytes_needed + 1, 'little')

    
class ClientInterpreter(Interpreter):
    @staticmethod
    def interpret_raw_result_as_iterator(result):
        return result['result']['stack'][0]['iterator']
    
    @staticmethod
    def base64_struct_to_bytestrings(base64_struct: dict) -> List[bytes]:
        processed_struct = []
        if type(base64_struct) is dict and 'type' in base64_struct and base64_struct['type'] == 'Struct':
            values = base64_struct['value']
            for value in values:
                if value['type'] == 'ByteString':
                    processed_struct.append(base64.b64decode(value['value']))
        return processed_struct
