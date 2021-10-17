from fizzbuzz import fizzbuzz


def test_1():
    assert fizzbuzz(list[0] == 1)


def test_3_5_15():
    assert fizzbuzz(list[3] == "Fizz")
    assert fizzbuzz(list[5] == "Buzz")
    assert fizzbuzz(list[15] == "FizzBuzz")


def test_3_5_15_multiplied():
    MULTIPLIER = 7
    assert fizzbuzz(list[3 * MULTIPLIER] == "Fizz")
    assert fizzbuzz(list[5 * MULTIPLIER] == "Buzz")
    assert fizzbuzz(list[15 * MULTIPLIER] == "FizzBuzz")
