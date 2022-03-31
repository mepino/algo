class MyHashMap:
    def __init__(self):
        self.direct_index_list = [None for i in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.direct_index_list[key] = value
    
    def get(self, key: int) -> int:
        if self.direct_index_list[key] == None:
            return -1
        else:
            return self.direct_index_list[key]

    def remove(self, key: int) -> None:
        self.direct_index_list[key] = None