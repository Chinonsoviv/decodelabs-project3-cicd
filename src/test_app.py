from app import add, greet

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    print("add() test passed")

def test_greet():
    assert greet("DecodeLabs") == "Hello, DecodeLabs!"
    print("greet() test passed")

if __name__ == "__main__":
    test_add()
    test_greet()
    print("All tests passed!")
