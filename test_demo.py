import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    add_result = demo.add(3,4)
    assert add_result == 7
    assert demo.add(7,5) == 12
    assert demo.add(14,26) == 40

def test_sub():
    # GIVEN two numbers
    # WHEN I invoke the method sub
    # THEN I get the difference between the firstone and the other number

    assert demo.sub(-14,25) == -39
    assert demo.sub(24, 38) == -14
    assert demo.sub(-45, -7) == -38
    


