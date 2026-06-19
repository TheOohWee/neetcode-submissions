class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        # iterating thru to see if we have key -> upd value
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map[i][1] = value
                break
        else: 
            self.map.append([key, value])
        

    def get(self, key: int) -> int:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return self.map[i][1]
                break
        else:
            return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.remove(self.map[i])
                break