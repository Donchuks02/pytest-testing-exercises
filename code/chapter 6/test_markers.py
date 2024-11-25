import pytest


pytestmark = pytest.mark.all

# #########################  (Exercises)   ##########################

# 1. Modify pytest.ini to register three markers, odd, testclass, and all.
# 2. Mark all the odd test cases with odd.
# 3. Use a file level marker to add the all marker.
# 4. Mark the test class with the testclass marker.
# 5. Run all the tests using the all marker.
# 6. Run the odd tests.
# 7. Run the odd tests that are not marked with testclass.
# 8. Run the odd tests that are parametrized. (Hint: Use both marker and
# keyword flags.)



# ################# (pytest commmands to run from no.5 - 8) ###################
# 5. pytest -v -m all
# 6. pytest -v -m odd
# 7. pytest -v -m "odd and not testclass"
# 8. pytest -v -m odd -k "parametrize"


@pytest.mark.odd
def test_one():
    pass

@pytest.mark.odd
def test_two():
    pass

@pytest.mark.odd
def test_three():
    pass

@pytest.mark.testclass
class TestClass:
    def test_four(self):
        pass

    def test_five(self):
        pass


@pytest.mark.odd
@pytest.mark.parametrize("x", [6, 7])
def test_param(x):
    pass
