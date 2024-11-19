"""
writing a test file and using different types of assert statements.

"""
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1


def test_list_contains():
    assert 1 in [1, 2, 3]

def test_list_length():
    assert len([1, 2, 3]) == 3

def test_dict_key():
    assert 'key' in {'key': 'value'}

def test_set():
    assert 1 in {1, 2, 3}

def test_greater_than():
    assert 5 > 3

def test_less_than():
    assert 3 < 5


def test_not_equal():
    assert 5 != 3

