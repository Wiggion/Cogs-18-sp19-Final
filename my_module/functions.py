import string
import random
import nltk

#Methods to play with lists and build up chatbot.


def intList(input_string):
    """
    Convert a string with only integers to integer list.
    
    Parameters
    ----------
    input_string : String
        String to convert to int list
    
    Returns
    -------
    output : list
        Integer list or converted list of input String.
    """
    output = [];
    temp_string = str(input_string);
    temp_string = temp_string.replace(' ', '');
    
    if temp_string.isdigit():
        temp_list = prepare_text(input_string);
        for item in temp_list:
            output.append(int(item));
        return output;
    else:
        return prepare_text(input_string);
        
def test_int(random_list):
    """
    Check if the input list is a list of integers.
    
    
    Parameters
    ----------
    random_list : list
        List to be checked for whether a list of integers.
    
    Returns
    -------
    output : boolean
        True or False whether current list is an integer list.
    """
    
    for item in random_list:
        if not isinstance(item, int):  
            
            return False;
        
        
    return True;

def length(random_list):
    """
    Get the length of the input list.
    
    Parameters
    ----------
    random_list : list
        List to get length of.
    
    Returns
    -------
    length : int
        The length of the input list.
    """
    length = len(random_list);
    
    return length;


def sort_list(random_list):
    """
    Sort the input list ascendingly.
    
    Parameters
    ----------
    random_list : list
        List to sort ascendingly.
    
    Returns
    -------
    random_list : list
        sorted list.
    """
    random_list.sort();
    
    return random_list;


def find_max(random_list):
    """
    Get the maximum value of input list.
    
    Parameters
    ----------
    random_list : list
        List to find maximum from
    
    Returns
    -------
    list_max : int
        The maximum of input list.
    """
    list_max = random_list[0];
    
    for number in random_list:
        if number > list_max:
            
            list_max = number;
            
    return list_max;


def find_min(random_list):
    """
    Get the minimum of input list.
    
    Parameters
    ----------
    random_list : list
        List to find minimum from.
    
    Returns
    -------
    list_min : int
        The minimum of inout list.
    """
    list_min = random_list[0];
    index = 0;
    
    for number in random_list:
        if number < list_min:
            
            list_min = number;
            index = random_list.index(list_min);
            
    return list_min;


def find_num(random_list, toFind):
    """
    Get the index of the integer first appearing inside the input list.
    
    Parameters
    ----------
    random_list : list
        List to find the index of the input integer from.
    
    toFind : int
        The integer to find index of from input list.
        
    Returns
    -------
    index : int
        The index of the integer to find inside input list.
    """
    if toFind not in random_list:
        return -1;
    
    else:
        index = random_list.index(toFind);
        
        return index;

    
def square_all(collection):
    """
    Square all numbers inside input list.
    
    Parameters
    ----------
    collection : list
        list to square every number inside it.
    
    Returns
    -------
    output_list : list
        List containing numbers square of input list.
    """
    output_list = [];
    
    for number in collection:
        
        output_list.append(number**2);
        
    return output_list;


def check_len(checkList, tocheckList):
    """
    Check whether two lists have different length.
    
    Parameters
    ----------
    random_list : list
        list to check length with another input list.
    tocheckList : list
        list to check length with another input list.
        
    Returns
    -------
    output : String
        String prompting the user whether two lists have same length.
    """
    if len(checkList) == len(tocheckList):
        
        return 'Two lists have same length.'
    
    else:
        
        return 'Two lists have different length.'

    
def summation(addingList, addedList):
    """
    Add two lists up. If two lists have different lengths, add them up
    from index 0
    
    Parameters
    ----------
    addingList : list
        List to add another input list to.
        
    addedList : list
        List to add to another input list.
        
    Returns
    -------
    output : list
        List added up by two input lists.
    """
    length = len(addingList);
    check_len = len(addedList);
    
    if length > check_len:
        for i in range(0, check_len):
            
            addingList[i] += addedList[i];
            
        return addingList;
    
    elif length < check_len:
        for i in range(0, length):
            
            addedList[i] += addingList[i];
            
        return addedList;
    
    #If two lists have same length, directly add two lists up.
    else:
        for i in range(0, length):
            
            addedList[i] += addingList[i];
            
        return addedList;


def multiplication(firstList, secondList):
    """
    Multiply numbers of two input lists.
    
    Parameters
    ----------
    firstList : list
        List to multiply by another input list.
    
    secondList : list
        List to multiply by another input list.
    
    Returns
    -------
    output : list
        List containing numbers gotten through multiplying two input 
        lists number.
    """
    length = len(firstList);
    check_len = len(secondList);
    
    if length > check_len:
        for i in range(0, check_len):
            
            firstList[i] = firstList[i] * secondList[i];
            
        return firstList;
    
    elif length < check_len:
        for i in range(0, length):
            
            secondList[i] = firstList[i] * secondList[i];
            
        return secondList;
    
    #If two lsits have same length, directly times two lists
    else:
        for i in range(0, length):
            
            secondList[i] = firstList[i] * secondList[i];
            
        return secondList;
    
    
def division(firstList, secondList):
    """
    Divide numbers of input list by numbers from another input list.
    
    Parameters
    ----------
    firsList : list
        List to divide by antoher input list.
        
    secondList : list
        List to divide another input list.
        
    Returns
    -------
    output : list
        List gotten by dividing two lists up.
    """
    length = len(firstList);
    check_len = len(secondList);
    
    if length > check_len:
        for i in range(0, check_len):
            
            firstList[i] = firstList[i] / secondList[i];
            
        return firstList;
    
    elif length < check_len:
        for i in range(0, length):
            
            secondList[i] = firstList[i] / secondList[i];
            
        return secondList;
    
    #If two lists have same length, directly divide.
    else:
        for i in range(0, length):
            
            secondList[i] = firstList[i] / secondList[i];
            
        return secondList;
    
    
def subtraction(firstList, secondList):
    """
    Subtract one input list from the other.
    
    Parameters
    ----------
    firstList : list
        List to subtract antoher input list from.
    
    secondList : list
        List to subtract from another input list.
    
    Returns
    -------
    output : list
        List gotten through by subtract an input list from another.
    """
    length = len(firstList);
    check_len = len(secondList);
    
    if length > check_len:
        for i in range(0, check_len):
            
            firstList[i] = firstList[i] - secondList[i];
            
        return firstList;
    
    elif length < check_len:
        for i in range(0, length):
            
            secondList[i] = firstList[i] - secondList[i];
            
        return secondList;
    
    #If two lists have same length, directly subtract
    else:
        for i in range(0, length):
            
            secondList[i] = firstList[i] - secondList[i];
            
        return secondList;
    
    
def sum_atIndex(random_list, toAdd, index):
    """
    Add a number at certain index of input list.
    
    Parameters
    ----------
    random_list : list
        List to add a number in.
    toAdd : int
        Integer to add to the number at index of input list.
    index : int
        Index of input list to add the number to.
    
    Returns
    -------
    random_list : list
        List added by an integer at certain index.
    """
    random_list[index] += toAdd;
    
    return random_list;


def multiplication_atIndex(random_list, toTime, index):
    """
    Multiply an integer by number at input indx of input list.
    
    Parameters
    ----------
    random_list : list
        List to multiply the integer at index from.
    toTime : int
        Integer to multiply integer of the list at index.
    index : int
        Index of number of input list to multiply the integer.
        
    Returns
    -------
    random_list : list
        List multiplied by an integer from input list.
    """
    random_list[index] = random_list[index] * toTime;
    
    return random_list;


def division_atIndex(random_list, toDivide, index):
    """
    Divide an integer from input list at index.
    
    Parameters
    ----------
    random_list : list
        List to divide the integer from.
    toDivide:
        The integer to divide.
    index: 
        The index at which to divide integer from the list.
    
    Returns
    -------
    random_list : list
        List gotten by diving an integer from input list at index.
    """
    random_list[index] = random_list[index] / toDivide;
    
    return random_list;


def subtraction_atIndex(random_list, toSubtract, index):
    """
    Subtract an integer from input list at index.
    
    Parameters
    ----------
    random_list : list
        List to subtract the integer from.
    toSubtract : int
        Integer to subtract from input list at index.
    index : int
        Index from which to subtract the integer.
        
    Returns
    -------
    random_list : list
        List gotten by subtracting an integer from input list.
    """
    random_list[index] = random_list[index] - toSubtract;
    
    return random_list;


def concatenation(firstList, secondList):
    """
    Concat two lists together.
    
    Parameters
    ----------
    firstList : list
        List to concat another list to.
        
    secondList : list
        List to concat to another list.
        
    Retuns
    ------
    output : list
        List containing two input lists.
    """
    return firstList + secondList;


def concatenation_int(random_list, key):
    """
    Concat an integer to input list.
    
    Parameters
    ----------
    random_list : list
        List to concat the integer to.
    
    key : int
        Integer to concat to input list.
    
    Returns
    -------
    random_list : list
        List concated by the integer.
    """
    random_list.append(key);
    return random_list;


def remove_punctuation(input_string):
    """
    Remove punctuations from input string.
    
    Parameters
    ----------
    input_string : String
        String to remove punctuations from.
        
    Returns
    -------
    output_string : String
        String without punctuations.
    """
    output_string = '';
    
    for item in input_string:
        if item not in string.punctuation:
            
            output_string = output_string + item;
            
    return output_string;


def prepare_text(input_string):
    """
    Convert String to list.
    
    Parameters
    ----------
    input_string : String
        String to convert to list.
        
    Returns
    -------
    out_list : list
        List converted from input String.
    """
    temp_string = input_string.lower();
    temp_string = remove_punctuation(temp_string);
    out_list = temp_string.split();
    
    return out_list;


def selector(input_list, check_list, return_list):
    """
    Select responce to input_list from return_list.
    
    Parameters
    ----------
    input_list : list
        List to check whether has items in check_list.
    check_list : list
        List to check whether containing items in input_list.
    return_list : list
        List to give responce from.
    Returns
    -------
    output : String
        Random String inside return_list.
    """
    output = None;
    
    for item in input_list:
        if item in check_list:
            
            output = random.choice(return_list);
            break;
            
    return output;


def list_to_string(input_list, separator):
    """
    Convert list to String.
    
    Parameters
    ----------
    input_list : list
        List to convert from.
    separator : String
        String that separates items inside lists.
    
    Returns
    -------
    output : String
        String converted from list.
    """
    output = input_list[0];
    i = 1;
    
    while i >= 1 and i < len(input_list):
        
        output = string_concatenator(output, input_list[i], separator);
        i+=1;
        
    return output;


def end_chat(input_list):
    """
    Break out from the while loop of chatbot.
    
    Parameters
    ----------
    input_list : list
        User's input list
    
    Returns
    -------
    True or false to break out the while loop.
    """
    if 'quit' in input_list:
        
        return True;
    
    else:
        
        return False;
    
