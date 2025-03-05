# Functions go here...
def make_statement(question, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""


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


def instruction():
    make_statement("Instrucions", "ℹ️")

    print('''
    
For each ticket holder enter...
- Their name
- Their age     
- The payment method (cash / card)

The program will record the ticket sale and calculate the 
ticket code (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).
   
     ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def int_check(question, low=None, high=None):
    """Check the user enter an integer between two values"""

    error = "Oops - please enter an integer between {low} and {high}."

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



# Main routine gose here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# intialise variables / non-default optuons for string checker
payment_ans = ('cash', 'card')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print()

while tickets_sold <MAX_TICKETS:
    # ask user for their name (and check it's not blank)
    print()
    name = not_blank("Name: ")

    #if name is exit coad , break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for paymant method (cash / credit / ca / cr)
    pay_method = string_check("Pyment method: ", payment_ans, 2)
    print(f"{name} has bought a trcket ({pay_method})")

    tickets_sold +=1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
