from hellotest import hello

def test_default(): 
    assert hello() == "hello, world"

# def test_argument(): 
#     assert hello("david") == "hello, david"

''' Using loop'''

def test_argument(): 
    for name in ["earn", "luffy", "zoro"]:
        assert hello(name) == f"hello, {name}"