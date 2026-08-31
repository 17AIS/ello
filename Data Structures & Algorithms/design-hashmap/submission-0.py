class MyHashMap:

    def __init__(self):
        self.keyv = []
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.keyv)):
            if self.keyv[i][0] == key:
                self.keyv[i][1] = value
                return
        self.keyv.append([key, value])
        

    def get(self, key: int) -> int:
        for k, v in self.keyv:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.keyv)):
            if self.keyv[i][0] == key:
                self.keyv.pop(i)
                break


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)