# In module test_fizzbuzz.py
from fizzbuzz import fizzbuzz
def test_fizzbuzz_three():
    result = fizzbuzz(3)
    assert result == 'fizz'

def test_fizzbuzz_five():
    result = fizzbuzz(5)
    assert result == 'buzz'

def test_fizzbuzz_fifteen():
    result = fizzbuzz(15)
    assert result == 'fizzbuzz'

def test_fizzbuzz_two():
    result = fizzbuzz(2)
    assert result == 2

def test_fizzbuzz_zero():
    result = fizzbuzz(0)
    assert result == 0

def test_fizzbuzz_fraction():
    result = fizzbuzz(1.8)
    assert result == 1.8
    
    
