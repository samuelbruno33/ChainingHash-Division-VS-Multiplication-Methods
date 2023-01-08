import math
import random
import time

# import matplotlib.pyplot as plt   # Import della libreria per effettuare i grafici in Python

# plot_count = 0    # Var globale per contare ogni inserimento effettuato nella insert per disegnare sul grafico
                    # (Serve per plot - Div method)

count_collision_div = 0
count_collision_mul = 0


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
    def __init__(self, m):
        self.m = m  # Scelgo un numero primo che non sia una potenza di 2
        self.h = [None] * self.m

    # def insert_with_plot(self, key, value):
    #     start_time = time.process_time()
    #     global plot_count
    #     index = key % self.m
    #     a = self.countAll()
    #     if self.h[index] is None and a < self.m:
    #         newLinkedList = LinkedList()
    #         newLinkedList.insertAtFirst(key, value)
    #         self.h[index] = newLinkedList
    #         plot_count += 1
    #     else:
    #         if a < self.m:
    #             self.h[index].insertAtLast(key, value)
    #             plot_count += 1
    #             end_time = time.time() - start_time
    #             plt.plot(plot_count, end_time, marker="o", color='red')
    #         else:
    #             raise Exception('Lunghezza lista superata! La sua grandezza è di: {}'.format(self.m))

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

    def countCollisionsInsertDivision(self, key, value):
        """
        Un programma che esegue gli esperimenti contando quante collisioni
        si hanno eseguendo un numero variabile di inserimenti in una
        tabella hash in entrambi i casi(in pratica vedere che succede crescere del fattore di
        caricamento α = n/m)
        """
        global count_collision_div
        index = key % self.m
        a = self.countAll()
        if self.h[index] is None and a < self.m:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key, value)
            self.h[index] = newLinkedList
        else:
            if a < self.m:
                count_collision_div += 1
                self.h[index].insertAtLast(key, value)
            else:
                raise Exception('Lunghezza lista superata! La sua grandezza è di: {}'.format(self.m))


class HashTableMultiplication:
    def __init__(self, m):
        self.m = m  # Scelgo un numero che sia una potenza di 2
        self.h = [None] * self.m
        self.A = ((math.sqrt(5) - 1) / 2)  # Numero ottimo per la scelta di A, che deve essere 0 < A < 1

    def insert(self, key, value):
        index = math.floor(self.m * ((key * self.A) % 1))
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
        index = math.floor(self.m * ((key * self.A) % 1))
        if self.h[index] is not None:
            return self.h[index].find(key)

    def delete(self, key):
        index = math.floor(self.m * ((key * self.A) % 1))
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

    def countCollisionsInsertMultiplication(self, key, value):
        """
        Un programma che esegue gli esperimenti contando quante collisioni
        si hanno eseguendo un numero variabile di inserimenti in una
        tabella hash in entrambi i casi(in pratica vedere che succede crescere del fattore di
        caricamento α = n/m)
        """
        global count_collision_mul
        index = math.floor(self.m * ((key * self.A) % 1))
        a = self.countAll()
        if self.h[index] is None and a < self.m:
            newLinkedList = LinkedList()
            newLinkedList.insertAtFirst(key, value)
            self.h[index] = newLinkedList
        else:
            if a < self.m:
                count_collision_mul += 1
                self.h[index].insertAtLast(key, value)
            else:
                raise Exception('Lunghezza lista superata! La sua grandezza è di: {}'.format(self.m))


def main():
    div = HashTableDivision(127)
    mul = HashTableMultiplication(128)

    print("----- INSERT -----")
    start_div_time = time.process_time_ns()
    for x in range(div.m):
        div.insert(random.randint(0, 1000), random.randint(0, 1000))
    end_div_time = time.process_time_ns() - start_div_time
    print("Division: %s ns " % end_div_time)

    start_mul_time = time.process_time_ns()
    for y in range(mul.m):
        mul.insert(random.randint(0, 1000), random.randint(0, 1000))
    end_mul_time = time.process_time_ns() - start_mul_time
    print("Multiplication: %s ns " % end_mul_time)

    delta = end_div_time - end_mul_time
    print("Delta: %s ns " % delta)
    print("----------------------------\n")

    print("----- RICERCA CON SUCCESSO -----")
    start_div_time = time.process_time_ns()
    div.get(0)
    end_div_time = time.process_time_ns() - start_div_time
    print("Division: %s ns " % end_div_time)

    start_mul_time = time.process_time_ns()
    mul.get(0)
    end_mul_time = time.process_time_ns() - start_mul_time
    print("Multiplication: %s ns " % end_mul_time)

    delta = end_div_time - end_mul_time
    print("Delta: %s ns " % delta)
    print("----------------------------\n")

    print("----- RICERCA SENZA SUCCESSO -----")
    start_div_time = time.process_time_ns()
    div.get(1001)
    end_div_time = time.process_time_ns() - start_div_time
    print("Division: %s ns " % end_div_time)

    start_mul_time = time.process_time_ns()
    mul.get(1001)
    end_mul_time = time.process_time_ns() - start_mul_time
    print("Multiplication: %s ns " % end_mul_time)

    delta = end_div_time - end_mul_time
    print("Delta: %s ns " % delta)
    print("----------------------------\n")

    print("----- DELETE -----")
    start_div_time = time.process_time_ns()
    div.delete(0)
    end_div_time = time.process_time_ns() - start_div_time
    print("Division: %s ns " % end_div_time)

    start_mul_time = time.process_time_ns()
    mul.delete(0)
    end_mul_time = time.process_time_ns() - start_mul_time
    print("Multiplication: %s ns " % end_mul_time)

    delta = end_div_time - end_mul_time
    print("Delta: %s ns " % delta)
    print("----------------------------\n")

    i = 0
    arr = [10, 25, 50, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    global count_collision_div
    global count_collision_mul
    while i < 13:
        div2 = HashTableDivision(1000)
        mul2 = HashTableMultiplication(1000)

        for x in range(arr[i]):
            div2.countCollisionsInsertDivision(random.randint(0, 1000), random.randint(0, 1000))

        for x in range(arr[i]):
            mul2.countCollisionsInsertMultiplication(random.randint(0, 1000), random.randint(0, 1000))

        print("n:", arr[i])
        print("m: ", div2.m)
        alpha = (arr[i] / div2.m)
        print("Alpha: %s" % alpha)  # Calcolo alpha = n/m

        print("Numero di collisioni metodo della divisione: %s" % count_collision_div)
        a = ((count_collision_div / arr[i]) * 100)
        print("Percentuale di collisioni su n elementi: ", a, "%")

        print("Numero di collisioni metodo della moltiplicazione: %s" % count_collision_mul)
        b = ((count_collision_mul / arr[i]) * 100)
        print("Percentuale di collisioni su n elementi: ", b, "%")

        i += 1
        count_collision_mul = 0
        count_collision_div = 0
        

# def main2():  # Serve per disegnare i grafici attraverso la libreria plot di python
#     div = HashTableDivision()
#     mul = HashTableMultiplication()
#
#     plt.title("INSERT DIVISION METHOD")
#     plt.rcParams["figure.figsize"] = [7.50, 3.50]
#     plt.rcParams["figure.autolayout"] = True
#     plt.xlabel("Elementi")
#     plt.ylabel("Tempo Operazioni")
#     div.insert(0, 0)
#     for i in range(div.m - 1):
#         div.insert(random.randint(0, 1000), random.randint(0, 1000))
#     plt.show()
#
#     mul.insert(0, 0)
#     for x in range(mul.m - 1):
#         mul.insert(random.randint(0, 1000), random.randint(0, 1000))
#
#     div.get(0)
#     mul.get(0)
#
#     div.get(1001)
#     mul.get(1001)
#
#     div.delete(0)
#     mul.delete(0)


# if __name__ == '__main__':
#     main2()


if __name__ == '__main__':
    main()
