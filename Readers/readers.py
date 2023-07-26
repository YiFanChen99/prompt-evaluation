""" Module to log error information """
import logging
from Readers.json_reader import JsonReader
class Readers:
    """
        Class to get supported file readers information.
        Also provide mapping from format name to reader type
    """
    _Readers = {
        "json": JsonReader
    }

    @staticmethod
    def get_reader_list():
        """
            Get name of all supported reader 
        """
        return Readers._Readers.keys()

    @staticmethod
    def get_format_reader(file_format):
        """
            Returns reader correspond to given format name
        """
        aval_readers = Readers._Readers.keys()
        if file_format not in aval_readers:
            logging.error("Asking a unImplemented or not supported metric")
            raise NotImplementedError
        return Readers._Readers[file_format]
