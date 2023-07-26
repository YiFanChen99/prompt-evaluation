""" Module to read json file """
import json

class JsonReader:
    """ 
        Reader for json format file.
        Reference's key name is "reference"
        Prediction's key name is "prediction"
    """
    def __init__(self, path) -> None:
        with open(path, "r", encoding="UTF-8") as file:
            raw_data = json.loads(file.read())
            if not isinstance(raw_data, list):
                raw_data = [raw_data]
        self.data = []
        for data in raw_data:
            if len(data) != 2:
                raise SyntaxError("Input format error")
            self.data.append([data["reference"], data["prediction"]])

    def get_list_data(self):
        """
            Get all of data in a list of list
            The first element in inner list is reference and the second one is prediction
            Ex: [[X, Y],...] where X is reference and Y is prediction
        """
        return self.data

    def get_indexed_data(self, index: int):
        """
            Get data with specified index
            The first element in returned list is reference and the second one is prediction
            Ex: [X, Y] where X is reference and Y is prediction
        """
        return self.data[index]

    def write_data(self, data: dict, path: str):
        """
            Write $data to $path in json format
        """
        with open(path, "w", encoding="UTF-8") as file:
            file.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    tmp = JsonReader("./Testcase/test.json")
