# Dunder/Magic Methods in Python

class LinkedList:
    def __init__(self):
        self.items = []

    # __repr__ gives an unambiguous string representation
    def __repr__(self):
        return f"LinkedList({self.items})"

    # __str__ gives a user-friendly string
    def __str__(self):
        return " -> ".join(map(str, self.items)) or "Empty list"

    # __len__ lets you use len(obj)
    def __len__(self):
        return len(self.items)

    # __contains__ lets you use `in`
    def __contains__(self, value):
        return value in self.items

    # __getitem__ enables indexing (obj[i])
    def __getitem__(self, index):
        return self.items[index]

    # __setitem__ allows assigning (obj[i] = value)
    def __setitem__(self, index, value):
        self.items[index] = value

    # __iter__ makes the object iterable (for loops)
    def __iter__(self):
        return iter(self.items)

    # __eq__ enables == comparison
    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.items == other.items
        return False

    # custom add method to demonstrate updates
    def add(self, value):
        self.items.append(value)


# Example usage
lst = LinkedList()
lst.add(10)
lst.add(20)
lst.add(30)

print(lst)                  # Output: 10 -> 20 -> 30
print(repr(lst))            # Output: LinkedList([10, 20, 30])
print(len(lst))             # Output: 3
print(20 in lst)            # Output: True
print(lst[1])               # Output: 20
lst[1] = 99
print(lst)                  # Output: 10 -> 99 -> 30
