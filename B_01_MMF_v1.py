
# Functions go here...
def make_statement(question, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Check that user enter the full word
        or the 'n' letter/s of a word from a list of valid responses"""

    error = f"Please choose an option from {valid_ans_list}"

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(error)


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


def int_check(question):
    """Checks that users enter an integer"""

    while True:

        try:
            # Check the response to an integer and check that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print("Please enter an integer")


# Main routine goose here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# Program main heading
make_statement("Mini-Movie Fundraiser Program", "🍿")

# Ask user if they want to see the instr
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print()

# loop to get name, age and payment detail
while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank)
    print()
    name = not_blank("Name: ")

    # if name is exit coed , break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")
    print("Age: ", age)

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket price is $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif age < 65:
        ticket_price = ADULT_PRICE

    # Senior Citizen ticket ($6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Pyment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

        # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

        # add mane, ticket cost and surcharge to
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1



if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
