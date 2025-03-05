# Functions go here...
def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Check thet user enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option form {valid_ans_list}")


# Main routine goes here
payment_list = ['cash', 'credit']

want_instruction = string_check("Do you eant to see the instruction? ")
print(f"You chose {want_instruction}")
pay_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")
