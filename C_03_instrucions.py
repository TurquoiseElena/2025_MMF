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

# Main routine gose here

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

print()
print("Program continues...")