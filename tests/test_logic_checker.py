import pytest
from syllogism_checker.logic_checker import check_syllogism

def test_check_syllogism():
    valid_syllogism = "All men are mortal.\nSocrates is a man.\nTherefore, Socrates is mortal."
    invalid_syllogism = "All men are mortal\nSocrates is a man\nTherefore, Socrates is mortal"
    
    assert check_syllogism(valid_syllogism) == []
    assert "The first premise must end with a period." in check_syllogism(invalid_syllogism)
    assert "The second premise must end with a period." in check_syllogism(invalid_syllogism)
    assert "The conclusion must end with a period." in check_syllogism(invalid_syllogism)