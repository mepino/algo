def hashfunc(x):
    m = 664579
    return x % m

class MyHashMap:
    def __init__(self):
        self.direct_index_list = [None for i in range(1000001)]

    def put(self, key: int, value: int) -> None:
        new_key = hashfunc(key)
        self.direct_index_list[new_key] = value
    
    def get(self, key: int) -> int:
        new_key = hashfunc(key)
        if self.direct_index_list[new_key] == None:
            return -1
        else:
            return self.direct_index_list[new_key]

    def remove(self, key: int) -> None:
        new_key = hashfunc(key)
        self.direct_index_list[new_key] = None

# class MyHashMap:
#     def __init__(self):
#         self.len_list = 1000001
#         self.direct_index_list = [None for i in range(self.len_list)]

#     def put(self, key: int, value: int) -> None:
#         new_key = hashfunc(key)
#         print(new_key)
        
#         for i in range(self.len_list - new_key):
#             new_key = hashfunc(key) + i
#             if self.direct_index_list[new_key] == None:
#                 self.direct_index_list[new_key] = value
#                 break
    
#     def get(self, key: int) -> int:
#         new_key = hashfunc(key)
        
#         for i in range(self.len_list - new_key):
#             new_key = hashfunc(key) + i
#             if self.direct_index_list[new_key] == None:
#                 return -1
#             elif self.direct_index_list[new_key] == 'Deleted':
#                 continue
#             else:
#                 return self.direct_index_list[new_key]

#     def remove(self, key: int) -> None:
#         new_key = hashfunc(key)
        
#         for i in range(self.len_list - new_key):
#             new_key = hashfunc(key) + i
#             if self.direct_index_list[new_key] == None:
#                 break
#             elif self.direct_index_list[new_key] == key:
#                 self.direct_index_list[new_key] = 'Deleted'
        
       
        
# class MyHashMap:
#     def __init__(self):
#         self.direct_index_list = [None for i in range(1000001)]

#     def put(self, key: int, value: int) -> None:
#         self.direct_index_list[key] = value
    
#     def get(self, key: int) -> int:
#         if self.direct_index_list[key] == None:
#             return -1
#         else:
#             return self.direct_index_list[key]

#     def remove(self, key: int) -> None:
#         self.direct_index_list[key] = None
        
