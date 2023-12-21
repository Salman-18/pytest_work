import pytest
import src.shapes as shapes 

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81),(6,36), (7,49), (2, 4), (20, 400), (17, 289), (13, 169), (12, 144), 100, 100000])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
