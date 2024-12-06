import pytest
from jar import Jar

def test_init():
    # Проверка значения по умолчанию
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Проверка пользовательской емкости
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Проверка на отрицательную емкость
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(3)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(1)
    assert jar.size == 3

    # Проверка на превышение емкости
    with pytest.raises(ValueError):
        jar.deposit(1)

    # Проверка на отрицательное количество
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0

    # Проверка на изъятие большего количества, чем есть
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Проверка на отрицательное количество
    with pytest.raises(ValueError):
        jar.withdraw(-1)
