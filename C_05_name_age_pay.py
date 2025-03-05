# Functions go here...
def int_check(question):
    """Check thet user enter an integer between two values"""

    error = "Oops - please enter an intger between {low} and {high}."

    while True:

        try:
            # Check the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


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

# intialise variables / non-default optuons for string checker
payment_ans = ('cash', 'card')

# loop for testing purposes...

while True:
    print()

    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
       pass

# ask user for paymant method (cash / credit / ca / cr)
pay_method = string_check("Pyment method: ", payment_ans, 2)
print(f"{name} has bought a trcket ({pay_method})")

