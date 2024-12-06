class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Емкость должна быть неотрицательным целым числом")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Количество печений должно быть неотрицательным целым числом")
        if self._size + n > self._capacity:
            raise ValueError("Превышена емкость банки")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Количество печений должно быть неотрицательным целым числом")
        if self._size < n:
            raise ValueError("В банке недостаточно печений")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
