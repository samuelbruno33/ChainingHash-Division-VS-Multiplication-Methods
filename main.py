class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class HashTable:

    def __init__(self):
        self.m = 1000
        self.h = [None] * self.m    #Object to store keys/value Objects

    def insert(self, key, value):
        """
        value will always be non-negative.
        """
        index = key % self.m
        if self.h[index] is None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def find(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur:
            return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


def main():
    # obj = HashTable()
    # obj.insert(key, value)
    # param_2 = obj.find(key)
    # obj.remove(key)
    print("--------------- Hellooooo ---------------\n")


if __name__ == '__main__':
    main()
