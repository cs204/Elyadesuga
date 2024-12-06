from bank import value

def test_zero():
    assert value("здравствуйте") == 0
    assert value("Здравствуйте") == 0
    assert value("ЗДРАВСТВУЙТЕ") == 0

def test_twenty():
    assert value("здорово") == 20
    assert value("Зачем") == 20
    assert value("з") == 20

def test_hundred():
    assert value("привет") == 100
    assert value("добрый день") == 100
    assert value("123") == 100
