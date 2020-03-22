# Import class
from CheckingAccount import CheckingAccount
# Define Main function
def main():
    CA = CheckingAccount('John','Carter','5124 Barsum St','112233','test@email.com') # Instanciate CA (CheckingAccount) object

    #CA.__balance # Will throw an error
    try:
        print(CA.__balance)
    except AttributeError:
        print("This attribute is private")
    except:
        print("Another error happened")
    
    print(f"Hi {CA.firstName} {CA.lastName}") # Print Name

    print(f"Your current balance is: ${CA.getBalance()}") # Print Balance

    CA.creditFunds(1526) # Add funds
    print(f"Your current balance is: ${CA.getBalance()}") # Print Balance

    CA.debitFunds(156) # Remove funds
    print(f"Your current balance is: ${CA.getBalance()}") # Print Balance

main()