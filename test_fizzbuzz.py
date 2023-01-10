from fizzbuzz import fizzbuzz


def test_it_should_return_1_when_input_1():
    result = fizzbuzz(1)
    assert result == "1"


def test_it_should_return_2_when_input_2():
    result = fizzbuzz(2)
    assert result == "2"


def test_it_should_return_fizz_when_input_3():
    result = fizzbuzz(3)
    assert result == "Fizz"


def test_it_should_return_buzz_when_input_5():
    result = fizzbuzz(5)
    assert result == "Buzz"


def test_it_should_return_fizz_when_input_6():
    result = fizzbuzz(6)
    assert result == "Fizz"


def test_it_should_return_buzz_when_input_10():
    result = fizzbuzz(10)
    assert result == "Buzz"
