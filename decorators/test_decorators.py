import pytest

from decorators import repeat, type_check


# Repeater

def test_repeater():
    var = 0
    n = 10

    @repeat(n)
    def modify_var():
        nonlocal var
        var += 1

    modify_var()

    assert var == n


def test_repeater_continue_on_errors():
    call_limit = 5

    @repeat(7, continue_on_errors=True)
    def func():
        nonlocal call_limit
        if call_limit > 0:
            call_limit -= 1
            print(call_limit)
        else:
            raise Exception("Wait some time ...")

    func()

    assert call_limit == 0


# Type Checker

@type_check(str, int)
def str_repeater(text, repeat_count, sep=""):
    return sep.join(text for _ in range(repeat_count))


def test_ok():
    assert str_repeater("a", 3) == "aaa"

    assert str_repeater("go", 3, sep=", ") == "go, go, go"


def test_arg_count_mismatch():
    with pytest.raises(TypeError):
        str_repeater("aaa")

    with pytest.raises(TypeError):
        str_repeater("aaa", 3, "-")


def test_arg_types_mismatch():
    with pytest.raises(TypeError):
        str_repeater("text", 3.14)

    with pytest.raises(TypeError):
        str_repeater(3.14, "text", sep="_")
