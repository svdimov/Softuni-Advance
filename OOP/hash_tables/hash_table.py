from email.policy import default
from typing import NamedTuple, Any
class Deleted:
    pass


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    DELETED = Deleted

    def __init__(self,capacity = 4):
        self.capacity = capacity
        self._array: list = [None] * self.capacity
    @property
    def capacity(self):
        return self.__capacity


    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError('Capacity must be positive number')
        self.__capacity = value

    @property
    def keys(self):
        return {pair.key for pair in self.array}

    @property
    def values(self):
        return [pair.value for pair in self.array]


    @property
    def array(self):
        return {pair for pair in self._array if pair not in (None,self.DELETED)}

    def hash(self,key):
        # hash(key) % self.capacity
        return sum(ord(ch) for ch in str(key)) % self.capacity
    def get(self,key,default = None):
        try:
            return self[key]
        except KeyError:
            return default

    def add(self,key,value):
        self[key] = value

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                raise

    def __delitem__(self, key):

        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key == key:
                self._array[index] = self.DELETED
                break
        else:
            raise KeyError(key)


    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __len__(self):
        return len(self.array)

    def __setitem__(self, key, value):
        for index,pair in self._probe(key):
            if pair is self.DELETED:
                continue
            if pair is None or pair.key == key:
                self._array[index] = Pair(key,value)
                break
        else:
            self.resize()
            self[key] = value



    def __getitem__(self, key):

        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)




    def __iter__(self):
        yield from self.keys

    def __str__(self):
        result = []
        for k,v in self.array:
            result.append(f'{k!r}: {v!r}')
        return '{' + ' ,'.join(result) + '}'

    def _probe(self,key)->list[Pair]:
        index = self.hash(key)
        for _ in range(self.capacity):
            yield index,self._array[index]
            index = (index + 1) % self.capacity

    def resize(self):
        copy_t = HashTable(capacity=self.capacity * 2)
        for k,v in self.array:
            copy_t[k] = v
        self.capacity = copy_t.capacity
        self._array = copy_t._array





table = HashTable()


table["name"] = "Peter"
table["age"] = 25


print(table)
print(table.get("name"))
print(table["age"])
print(len(table))

