from approvaltests import verify, Options
from app import hello_world

def test_hello_world():
    """
    Hello, Matt!
    """
    verify(hello_world(), options=Options().inline())