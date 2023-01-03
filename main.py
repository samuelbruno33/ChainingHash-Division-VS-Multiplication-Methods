import math
import random


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtFirst(self, key, value):
        self.head = Node(key, value, self.head)
        self.size += 1

    def insertAtLast(self, key, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(key, value)
        self.size += 1

    def remove(self, key):
        current = self.head
        previous = None
        if current.key == key:
            self.head = current.next
        else:
            while current.next:
                previous = current
                current = current.next
                if current.key == key:
                    previous.next = current.next
            self.size -= 1

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def printAll(self):
        current = self.head
        while current:
            print(current.key, current.value)
            current = current.next

    def countElements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


class HashTableDivision:
    def __init__(self):
        self.m = 5  # Scelgo un numero primo che non sia una potenza di 2
        self.h = [None] * self.m

    def insert(self, key, value):
        index = key % self.m
        a = self.countAll()
        if self.h[index] is None and a < self.m:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key, value)
            self.h[index] = newLinkedList
        else:
            if a < self.m:
                self.h[index].insertAtLast(key, value)
            else:
                raise Exception('Lunghezza lista superata! La sua grandezza è di: {}'.format(self.m))

    def get(self, key):
        index = key % self.m
        if self.h[index] is not None:
            return self.h[index].find(key)

    def delete(self, key):
        index = key % self.m
        if self.h[index] is not None:
            self.h[index].remove(key)

    def printAll(self):
        for i in self.h:
            if i is not None:
                i.printAll()

    def countAll(self):
        count = 0
        for i in self.h:
            if i is not None:
                ret = i.countElements()
                count += ret
        return count


class HashTableMultiplication:
    def __init__(self):
        self.m = 128  # Scelgo un numero che sia una potenza di 2
        self.h = [None] * self.m
        self.A = ((math.sqrt(5) - 1) / 2)  # Numero ottimo per la scelta di A, che deve essere 0 < A < 1

    def insert(self, key, value):
        index = self.m * math.floor((key * self.A) % 1)
        a = self.countAll()
        if self.h[index] is None and a < self.m:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key, value)
            self.h[index] = newLinkedList
        else:
            if a < self.m:
                self.h[index].insertAtLast(key, value)
            else:
                raise Exception('Lunghezza lista superata! La sua grandezza è di: {}'.format(self.m))

    def get(self, key):
        index = self.m * math.floor((key * self.A) % 1)
        if self.h[index] is not None:
            return self.h[index].find(key)

    def delete(self, key):
        index = self.m * math.floor((key * self.A) % 1)
        if self.h[index] is not None:
            self.h[index].remove(key)

    def printAll(self):
        for i in self.h:
            if i is not None:
                i.printAll()

    def countAll(self):
        count = 0
        for i in self.h:
            if i is not None:
                ret = i.countElements()
                count += ret
        return count


def main():
    div = HashTableDivision()
    div.insert(0,0)
    for x in range(div.m - 1):
        div.insert(random.randint(0,1000) , random.randint(0,1000))
    param_2 = div.get(0)
    print("Valore cercato: ", param_2)
    param_3 = div.get(1001)
    print("Valore cercato: ", param_3)
    div.delete(0)
    div.printAll()

    mul = HashTableMultiplication()
    mul.insert(0, 0)
    for x in range(mul.m - 1):
        mul.insert(random.randint(0, 1000), random.randint(0, 1000))
    param_2 = mul.get(0)
    print("Valore cercato: ", param_2)
    param_3 = mul.get(1001)
    print("Valore cercato: ", param_3)
    mul.delete(0)
    mul.printAll()


if __name__ == '__main__':
    main()
