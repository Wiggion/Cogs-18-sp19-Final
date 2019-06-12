"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

import string
import random
import nltk

# Imports
from functions import test_int, length, sort_list, find_max, find_min, find_num
from functions import square_all, check_len, summation, multiplication, division
from functions import subtraction, sum_atIndex, multiplication_atIndex
from functions import division_atIndex, subtraction_atIndex, concatenation
from functions import concatenation_int

import functions as fu

USAGE = ('Please Enter one of the commands and follow the instructions:\n'
         'curr : show current list\n'
         'L : get the length of the list\n'
         'S : sort the list\n'
         'max : find the max value of the list\n'
         'min : find the min value of the list\n'
         'num : find the index of the number in the list\n'
         'Sq : square all numbers inside the list\n'
         'check : check whether two lists have same length\n'
         'sum : add two lists up\n'
         'time : multiply two lists\n'
         'divide : divide two lists up\n'
         'minus : subtract two lists\n'
         'sumIndex : add an integer at certain index\n'
         'multiIndex : multiply an integer to list at certain index\n'
         'divideIndex : divide an integer from list at certain index\n'
         'minusIndex : minus an integer from list at certain index\n'
         'concat : concat two lists together\n'
         'concatKey : concat a key to list\n'
         'quit : quit\n');
        
GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings'];
GREETINGS_OUT = [('Hello, nice to meet you! Please enter an integer list'
                  ' in following format\n'
                  '1 2 3 4')];

LS_FMT_1 = 'Length of current list is: {}';
LS_FMT_2 = 'Sorted list is: {}';
LS_FMT_3 = 'Max value of current list is: {}, at: {}';
LS_FMT_4 = 'Min value of current list is: {}, at: {}';
LS_FMT_5 = 'The integer is at {}';
LS_FMT_6 = 'Squared list is {}';
LS_FMT_7 = 'Current list is {}';
LS_FMT_8 = 'Result list is {}';

Unknown = 'Sorry, I can only understand commands above.';
findnumPrompt = 'Please enter the integer you wish to find from current list';
intPrompt = 'Please enter an integer';
Prompt = ('Please enter another integer list in following format\n'
          '1 2 3 4')
indexPrompt = 'At which index?';
reEnter = 'Please retype the command and enter an integer list';
reType = 'Please retype the command and enter an integer';


def have_a_chat():
    """Main function to run my chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        msg = fu.intList(msg);
        # Prepare the input message
        
        
        isintList = test_int(msg);
        
        # Check for an end msg 
        if fu.end_chat(msg):
            out_msg = 'Bye!'
            chat = False
            
        if not out_msg and isintList:
            firstintList = msg.copy()
            out_msg = USAGE
            
            
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(fu.selector(msg, GREETINGS_IN, GREETINGS_OUT));
            
            #Different input cases to handle output.
            
            #Get length 
            if msg == ['l']:
                
                outs.append(LS_FMT_1.format(length(firstintList)));
            
            #Sort list
            elif msg == ['s']:
                
                firstintList = sort_list(firstintList);
                outs.append(LS_FMT_2.format(firstintList));
                
            #Get maximum
            elif msg == ['max']:
                
                maximum = find_max(firstintList)
                outs.append(LS_FMT_3.format(maximum, 
                                            find_num(firstintList, maximum)));
            
            #Get minimum
            elif msg == ['min']:
                
                minimum = find_min(firstintList)
                outs.append(LS_FMT_4.format(minimum, 
                                            find_num(firstintList, minimum)));
                
            #Return index of certain integer
            elif msg == ['num']:
                
                print('OUTPUT:', findnumPrompt);
                user_input = input();
                
                try:
                    toFind = int(user_input);
                    index = find_num(firstintList, toFind);
                    outs.append(LS_FMT_5.format(index));
                    
                except ValueError:
                    outs.append(reType);
            
            #Square all integers in current list
            elif msg == ['sq']:
                
                temp_list = square_all(firstintList);
                outs.append(LS_FMT_6.format(temp_list));
            
            #Show current list
            elif msg == ['curr']:
                
                outs.append(LS_FMT_7.format(firstintList));
            
            #check whether two lists have different length
            elif msg == ['check']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                
                if test_int(intList):
                    
                    outs.append(check_len(firstintList, intList));
                    
                else:
                    
                    outs.append(reEnter);
            
            #sum two lists up
            elif msg == ['sum']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                
                #To avoid change to original list.
                temp_list = firstintList.copy();
                
                if test_int(intList):
                    
                    outs.append(LS_FMT_8.format(summation(temp_list, intList)));
                    
                else:
                    
                    outs.append(reEnter);
            #Multiply two lists
            elif msg == ['time']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                temp_list = firstintList.copy();
                
                if test_int(intList):
                    
                    outs.append(LS_FMT_8.format(multiplication(temp_list, intList)));
                    
                else:
                    
                    outs.append(reEnter);
            #Divide Two lists
            elif msg == ['divide']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                temp_list = firstintList.copy();
                
                if test_int(intList):
                    
                    outs.append(LS_FMT_8.format(division(temp_list, intList)));
                    
                else:
                    
                    outs.append(reEnter);
            #Subtract a list from another  
            elif msg == ['minus']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                temp_list = firstintList.copy();
                
                if test_int(intList):
                    
                    outs.append(LS_FMT_8.format(subtraction(temp_list, intList)));
                    
                else:
                    
                    outs.append(reEnter);
            
            #Add an integer at certain index
            elif msg == ['sumindex']:
                
                print('OUTPUT:', intPrompt);
                user_input = input();
                temp_list = firstintList.copy();
                
                try:
                    value = int(user_input);
                    print('OUTPUT:', indexPrompt);
                    index = input();
                    index = int(index);
                    output_list = sum_atIndex(temp_list, value, index);
                    outs.append(LS_FMT_8.format(output_list));
                    
                except ValueError:
                    
                    outs.append(reType);
                    
            #Minus an integer at certain index       
            elif msg == ['multiindex']:
                
                print('OUTPUT:', intPrompt);
                user_input = input();
                temp_list = firstintList.copy();
                
                try:
                    value = int(user_input);
                    print('OUTPUT:', indexPrompt);
                    index = input();
                    index = int(index);
                    output_list = multiplication_atIndex(temp_list, value, index);
                    outs.append(LS_FMT_8.format(output_list));
                    
                except ValueError:
                    
                    outs.append(reType);
            
            #Divide an integer at certain index
            elif msg == ['divideindex']:
                
                print('OUTPUT:', intPrompt);
                user_input = input();
                temp_list = firstintList.copy();
                
                try:
                    value = int(user_input);
                    print('OUTPUT:', indexPrompt);
                    index = input();
                    index = int(index);
                    output_list = division_atIndex(temp_list, value, index);
                    outs.append(LS_FMT_8.format(output_list));
                    
                except ValueError:
                    
                    outs.append(reType);
            
            #Subtract an integer at certain index
            elif msg == ['minusindex']:
                
                print('OUTPUT:', intPrompt);
                user_input = input();
                temp_list = firstintList.copy();
                
                try:
                    value = int(user_input);
                    print('OUTPUT:', indexPrompt);
                    index = input();
                    index = int(index);
                    output_list = subtraction_atIndex(temp_list, value, index);
                    outs.append(LS_FMT_8.format(output_list));
                    
                except ValueError:
                    outs.append(reType);
            
            #Concat two lists together
            elif msg == ['concat']:
                
                print('OUTPUT:', Prompt);
                user_input = input();
                intList = fu.intList(user_input);
                
                if test_int(intList):
                    
                    outs.append(LS_FMT_8.format(concatenation(firstintList, intList)));
                    
                else:
                    
                    outs.append(reEnter);
            
            #Concat an integer to end of current list
            elif msg == ['concatkey']:
                
                print('OUTPUT:', intPrompt);
                user_input = input();
                temp_list = firstintList.copy();
                
                try:
                    value = int(user_input);
                    output_list = concatenation_int(temp_list, value);
                    outs.append(LS_FMT_8.format(output_list));
                    
                except ValueError:
                    
                    outs.append(reType);
            
            #Unknown cases
            else:
                outs.append(USAGE + Unknown);

            
            options = list(filter(None, outs))
            if options:
                out_msg = options[0];
                
        #Print to output
        print('OUTPUT:', out_msg)