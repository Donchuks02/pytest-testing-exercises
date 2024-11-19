#  Exercises

# 1. Write a test without fixtures that validates that hello() writes the correct content to hellotxt.

# 2. Write a second test using fixtures that utilizes a temporary directory and monkeypatch.chdir().

# 3. Add a print statement to see where the temporary directory is located. Manually check the hello.txt file after a test run. pytest leaves the temporary directories around for a while after test runs to help with debugging.

# 4. Comment out the calls to hello() in both tests and re-run. Do they both
# fail? If not, why not?

def hello():
    with open("hello.txt", "w") as f:
        f.write("Hello World!\n")


if __name__ == "__main__":
    hello()




def test_validate_hello():
    hello()
    with open("hello.txt", "r") as file:
        content = file.read()
    assert content == "Hello World!\n"


def test_validate_hello(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    hello()

    file_path = tmp_path / "hello.txt"
    assert file_path.exists(), "The file hello.txt was not created."

    with open(file_path, "r") as file:
        content = file.read()
    assert content == "Hello World!\n"



