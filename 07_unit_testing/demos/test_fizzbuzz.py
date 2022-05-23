<<<<<<< HEAD
# In module test_fizzbuzz.py
from fizzbuzz import fizzbuzz
=======
from fizzbuzz import fizzbuzz


>>>>>>> 584a75b437188de8bab001c0b2aa7a529a044c24
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

<<<<<<< HEAD
def test_fizzbuzz_zero():
    result = fizzbuzz(0)
    assert result == 0

def test_fizzbuzz_fraction():
    result = fizzbuzz(1.8)
    assert result == 1.8
    
    
=======

def some_helper_function():
    print("Hello there!")
>>>>>>> 584a75b437188de8bab001c0b2aa7a529a044c24
