import calculator


def test__add():
    a = 1
    b = 2
    expected_value = 3
    actual_value = calculator.add(a, b)
    assert actual_value == expected_value


def test__subtract():
    a = 2
    b = 1
    expected_value = 1
    actual_value = calculator.subtract(a, b)
    assert actual_value == expected_value
