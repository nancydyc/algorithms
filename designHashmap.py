"""
Input:
["MyHashMap","put","put","get","get","put","get", "remove", "get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]

Output:

[null,null,null,1,-1,null,1,null,-1]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.dict[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.dict.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.dict:
            del self.dict[key]

