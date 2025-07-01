# test_hello.py
from hello import greet

def test_greet():
    assert greet() == "Hello from CI!"
