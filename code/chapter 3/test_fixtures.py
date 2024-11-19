#  Exercises

# 1. Create a test file called test_fixtures.py.
# 2. Write a few data fixtures—functions with the @pytest.fixture() decorator—that return some data (perhaps a list, dictionary, or tuple).
# 3. For each fixture, write at least one test function that uses it.
# 4. Write two tests that use the same fixture.
# 5. Run pytest --setup-show test_fixtures.py. Are all the fixtures run before every test?
# 6. Add scope='module' to the fixture from Exercise 4.
# 7. Re-run pytest --setup-show test_fixtures.py. What changed?
# 8. For the fixture from Exercise 6, change return <data> to yield <data>.
# 9. Add print statements before and after the yield.
# 10. Run pytest -s -v test_fixtures.py. Does the output make sense?
# 11. Run pytest --fixtures. Can you see your fixtures listed?
# 12. Add a docstring to one of your fixtures, if you didn’t include them already. Re-run pytest --fixtures to see the description show up.



import pytest

@pytest.fixture(scope='module')
def names_dict_func():
  names_dict = {
    "name1": "John",
    "name2": "Jane",
    "name3": "Bob"
  }
  print("printed before names_dict yield")
  yield names_dict
  print("printed after names_dict yield")



@pytest.fixture(scope='module')
def dept_dict_func():
  dept_dict = {
    "dept1": "Sales",
    "dept2": "IT",
    "dept3": "HR"
  }
  print('printed before dept_dict yield')
  yield dept_dict
  print('printed after dept_dict yield')



def test_names(names_dict_func):
  assert names_dict_func["name1"] == "John"
  assert names_dict_func["name2"] == "Jane"
  assert names_dict_func["name3"] == "Bob"

def test_departments(dept_dict_func):
  assert dept_dict_func["dept1"] == "Sales"
  assert dept_dict_func["dept2"] == "IT"
  assert dept_dict_func["dept3"] == "HR"


def test_name_and_department(names_dict_func, dept_dict_func):
  combinations = [
    (names_dict_func["name1"], dept_dict_func["dept1"]),
    (names_dict_func["name2"], dept_dict_func["dept2"]),
    (names_dict_func["name3"], dept_dict_func["dept3"]),
  ]
  for name, department in combinations:
    assert isinstance(name, str)
    assert isinstance(department, str)

def test_fixture_contents(names_dict_func, dept_dict_func):
  assert len(names_dict_func) == 3
  assert len(dept_dict_func) == 3