from example import add_two_args


def test_add_two_args():
    assert add_two_args(1, 1) == 2


def test_add_two_args_bad():
    assert add_two_args(5, 5) != 11
