'''
ASHA MAURYA
03/08/2022
PROJECT 1 - TIP CALCULATOR
'''
# create an infinite loop to run indefinitely until when the program is stopped by a False return. The True/if statement creates an infinite loop. After the calculation finishes and the output is printed for the user, a multiple check if-else conditional statement is used to create the end of the infintie loop.

Tip_Calculator = True
while Tip_Calculator:

#Create a list of the user input user_input_dict
    user_input_user_input_dict = [ 
        'What was the total check? \n Example: Enter 100.21 for $100.21 ',
        'How many guests will be splitting the check? \n Example: Enter 10 for ten guests. ',
        'How much tip would you like to add? \n Example: Enter 10 for 10% ',
        'How much sales tax would you like to add? \n Example: Enter 10 for 10% '
            ]  

#Create a list of the user input question names
    user_input_names = [
                'subtotal_check',
                'number_guests_split',
                'how_much_tip',
                'how_much_tax']
             
# INPUTS
# Define a function which loops through the question list as a user input.  The function returns a new list populated with the user inputs. 
# A try block is used to test a block of code for errors. The except block handles the error. A ValueError and AssertionError are used. Assertion Error. Assertion is a used while writing a code where the user declares a condition to be true using assert statement prior to running the module. If the condition is True, the control simply moves to the next line of code. In case if it is False the program stops running and returns AssertionError Exception.
#If there is an error, the user is asked to answer again.
# https://www.geeksforgeeks.org/python-assertion-error/
# https://realpython.com/lessons/assertions-and-tryexcept/
    def get_user_input():             
            for i in range(len(user_input_user_input_dict)):
                user_input = input(user_input_user_input_dict[i])
                try:
                    user_input = float(user_input)
                    assert user_input >= 0 
                    user_inputs_saved.append (float(user_input)) 
                except AssertionError:
                    print('\n Your entry has a negative value, please try again.\n')
                    user_input = get_user_input()
                    break
                except ValueError:
                        print('\n Your entry was not valid, please try again.\n')
                        user_input = get_user_input()
                        break
            return user_inputs_saved    

    user_inputs_saved = []  
    get_user_input()
               
# Create new dictionary containing the user input name : value of user inputs
#https://www.adamsmith.haus/python/answers/how-to-create-a-dictionary-from-two-lists-in-python
    user_input_dict = dict(zip(user_input_names, user_inputs_saved))
      
# Calculate the total check   
    def total_check():
            return ((1+(((user_input_dict['how_much_tip'])+(user_input_dict['how_much_tax']))/100))*(user_input_dict['subtotal_check']))
    
# calculate the split  
    def split_check():
            return (total_check()/(user_input_dict['number_guests_split']))

# Print Total check and split amount per guest plus 
# Format as a currency string (https://stackabuse.com/format-number-as-currency-string-in-python/)
# Print different statements if party is larger than 1   
    print()
    
    if (user_input_dict['number_guests_split']) >= 2:
        print(f'Adding {(user_input_dict["how_much_tip"])}% tip and {(user_input_dict["how_much_tax"])}% tax for {int(user_input_dict["number_guests_split"])} guests, the total bill {"${:,.2f}".format(total_check())} and the amount each should contribute is {"${:,.2f}".format(split_check())}.')
    else:
        print(f'Adding {(user_input_dict["how_much_tip"])}% tip and {(user_input_dict["how_much_tax"])}% tax for {int(user_input_dict["number_guests_split"])} guest, is the amount to pay is {"${:,.2f}".format(split_check())}.')
        
    print()
# User is promoted if they would like to try again if they were not satisfied with the result

    try_again=str(input("Would you to try again? Enter Y or N "))
    if try_again == "n" or try_again == "N" or try_again == "no" or try_again == "No"or try_again == "NO":
        Tip_Calculator = False 