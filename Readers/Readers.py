import logging
from Readers.JsonReader import *
class Readers:
    _Readers = {
        "json": JsonReader
    }

    @staticmethod
    def GetReaderList():
        return Readers._Readers.keys()
    
    @staticmethod
    def GetFormatReader(format):
        if format not in Readers._Readers.keys():
            logging.error("Asking a unImplemented or not supported metric")
            raise NotImplementedError
        return Readers._Readers[format]
