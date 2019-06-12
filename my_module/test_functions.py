import pytest

from functions import test_int, length, sort_list, find_max, find_min, find_num
from functions import square_all, check_len, summation, multiplication, division
from functions import subtraction, sum_atIndex, multiplication_atIndex
from functions import division_atIndex, subtraction_atIndex, concatenation
from functions import concatenation_int

#Test whether methods defined in functions.py work properly.

def main():
    assert test_int([1,2,3,4]) == True;
    assert test_int([1,2,'e',3]) == False;
    assert length([1,2,3]) == 3;
    assert sort_list([3,2,1]) == [1,2,3];
    assert find_max([1,2,3]) == 3;
    assert find_max([1,1,1]) == 1;
    assert find_min([1,2,3]) == 1;
    assert find_num([1,2,3], 2) == 1;
    assert square_all([1,2,3]) == [1,4,9];
    assert check_len([1,2,3], [2,3]) == 'Two lists have different length.'
    assert check_len([1,2,3], [1,2,3]) == 'Two lists have same length.'
    assert summation([1,2,3], [2,3]) == [3,5,3];
    assert multiplication([1,1,1], [2,2,2]) == [2.0,2.0,2.0];
    assert division([2,2,2], [1,1,1]) == [2,2,2];
    assert subtraction([2,2,2], [1,1,1]) == [1,1,1];
    assert sum_atIndex([1,1,1], 1, 0) == [2,1,1];
    assert multiplication_atIndex([1,1,1], 2, 0) == [2,1,1];
    assert division_atIndex([2,1,1], 2, 0) == [1.0,1,1];
    assert subtraction_atIndex([2,1,1], 1, 0) == [1,1,1];
    assert concatenation([1,2,3], [4,5,6]) == [1,2,3,4,5,6];
    assert concatenation_int([1,2,3], 4) == [1,2,3,4];
    