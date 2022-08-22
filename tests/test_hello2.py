from hello import helloworld


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
# def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_helloworld():
    hw = helloworld(test_hello_helloworld.branch)
    assert hw == "Hello World!"