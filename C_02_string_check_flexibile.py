# Functions go here...
def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Check that user enter the full word
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


# Main Routine gose here
# payment_ans = ('cash', 'card')

while True:
    want_instructions = string_check("Do you want to see the instrucions? ")
    print(f"You choose {want_instructions}")
    print()

#pay_method = string_check("Payment method:", payment_ans 2)
# print(f"You choose {pay_method}")