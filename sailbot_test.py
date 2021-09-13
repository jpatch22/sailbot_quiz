from sailbot_quiz import AngleCalc
import pytest

def test_bound_1():
    assert AngleCalc.boundTo180(425) == 65

def test_bound_2():
    assert AngleCalc.boundTo180(360) == 0

def test_bound_3():
    assert AngleCalc.boundTo180(270) == -90

def test_bound_4():
    assert AngleCalc.boundTo180(-450) == -90

def test_bound_5():
    assert AngleCalc.boundTo180(180) == -180

def test_bound_6():
    assert AngleCalc.boundTo180(-180) == -180

def test_bound_7():
    assert AngleCalc.boundTo180(179) == 179

def test_between_1():
    assert AngleCalc.isAngleBetween(-90, -180, 110) == True

def test_between_2():
    assert AngleCalc.isAngleBetween(-90, -180, 80) == False

def test_between_3():
    assert AngleCalc.isAngleBetween(45, 0, -45) == True

def test_between_4():
    assert AngleCalc.isAngleBetween(-45, -180, 45) == False

def test_between_5():
    assert AngleCalc.isAngleBetween(-75, -20, 80) == True

def test_between_5():
    assert AngleCalc.isAngleBetween(0, 0, 0) == True

def test_between_5():
    assert AngleCalc.isAngleBetween(0, -20, 0) == False
