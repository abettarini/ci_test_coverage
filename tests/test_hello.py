from hello import toyou, add, subtract, multiply


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


## Run to see failed test
def test_hello_add():
   assert add(test_hello_add.x) == 20

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

def test_hello_multiply():
    assert multiply(2,3) == 6

def test_toyou():
    assert toyou(1) == "hi 1"