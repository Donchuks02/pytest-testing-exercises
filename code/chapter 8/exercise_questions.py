# Getting used to adding and editing configuration files now will help you understand just how simple and powerful they can be. These exercises focus on the primary configuration files.

# The following exercises are based around the /path/to/code/exercises/ch8 directory,
# which looks like this:
# exercises/ch8
# ├── pytest.ini
# └── tests
#   ├── a
# │   └── test_x.py
# └── b
#   └── test_x.py


# 1. Go to /path/to/code/exercises/ch8 and run pytest.
# • What is the root directory?   tests
# • What is the configuration file in use?   pytest.ini
# • You should also see an error message. What does it say?
# ___________ ERROR collecting tests/b/test_x.py __________
# import file mismatch:
# imported module 'test_x' has this __file__ attribute:
#   Desktop\Pytest-Testing-Exercises\code\chapter 8\tests\a\test_x.py                                           !
# which is not the same as the test file we want to collect:
#   Desktop\Pytest-Testing-Exercises\code\chapter 8\tests\b\test_x.py

# Pytest cant collect tets due to duplicate module name (test_x) in different directories (test/a) and (test/b).



# 2. In the pytest.ini file, set testpaths to tests/a.
# • Does that fix the error? NO, i got his error message :(pytest.ini:10: no section header defined )


# 3. Change the testpaths from tests/a to tests. Add __init__.py files to a and b.
# • Does that fix the error? NO, i got his error message :(pytest.ini:10: no section header defined )



# 4. Set addopts to -v and re-run pytest.
# • What was the behavior change?


# 5. Create a tests/pyproject.toml file.
# • Set addopts to "-v".
# • Run pytest from the exercises/ch8 directory and once from the exercises/ch8/tests directory.
# • Was the root directory and configuration file different?
# • If so, why?
