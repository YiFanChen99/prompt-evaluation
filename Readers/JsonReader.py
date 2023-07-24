import json

class JsonReader:
    def __init__(self, path) -> None:
        with open(path, "r") as f:
            rawData = json.loads(f.read())
            if type(rawData) is not list:
                rawData = [rawData]
        self.Data = []
        for data in rawData:
            if len(data) != 2:
                raise Exception("Input format error")
            self.Data.append([data["reference"], data["prediction"]])
    
    def GetListData(self):
        return self.Data
    
    def GetIndexedData(self, index: int):
        return self.Data[index]

if __name__ == "__main__":
    tmp = JsonReader("./Testcase/test.json")
