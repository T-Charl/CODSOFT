import csv
import sys
import pandas
from  prettytable import PrettyTable


def main():
    user =input("""Welcome to Contact Book.
Would you like to create your personal contact book? Y/n? """)
    
    while True:
        if user.lower() == 'n':
            sys.exit("Thank You.\nPlease try again when you would like to make a contact book.")
        elif user.lower() == 'y':
            print("Let's get started")
            add_contact()
            if not to_continue():
                break
        else:
            user = input('Would you like to create your personal contact book? Y/n?')


def to_continue():
    user = input('Would you like to add another? Y/n').strip().lower()
    if user == 'y':
        return True
    return False


def create_contact_book():
    with open("Contact_book\contact_book.csv", 'w', newline='') as contact_book:
        headers = ['name',"surname", 'phone_number', 'email', 'address']
        writer =  csv.writer(contact_book)
        writer.writerow(headers) 

# create_contact_book()
        

def add_contact():
    name = input('Enter contact name: ').strip().title()
    surname = input('Enter contact surname: ').strip().title()
    phone = input('Enter contact phone number: ').strip().title()
    email = input('Enter contact email: ').strip().title()
    address = input('Enter contact address: ').strip().title()
    with open("/workspaces/CODSOFT/Contact_book/contact_book.csv", 'a') as contact_book:
        writer = csv.writer(contact_book)
        writer.writerow([name, surname, phone, email, address])

# add_contact()
        

def delete_contact():
    # contact_name = input().strip().title()

    
    delete = pandas.read_csv('/workspaces/CODSOFT/Contact_book/contact_book.csv',  index_col='name')
    for i in delete:
            if 'False' in i:
                delete = delete.drop(i[0])
            else:
                pass
    # delete = delete.drop(columns=['Unnamed: 0'])

# Save the DataFrame to a CSV file without including the index
    delete.to_csv('/workspaces/CODSOFT/Contact_book/contact_book.csv', index=True)
    # delete.to_csv('Contact_book\contact_book.csv')
# delete_contact()


def view_contacts():

    newTable = PrettyTable(['Name','Surname','Phone number','Email','Address'])
    with open("/workspaces/CODSOFT/Contact_book/contact_book.csv", 'r') as contact_book:
        reader = csv.DictReader(contact_book)
        for i in reader:
            name = i.get('name')
            surname = i.get('surname')
            phone_number = i.get('phone_number')
            email = i.get('email')
            address = i.get('address')
            newTable.add_row([name, surname, phone_number, email, address])
    print(newTable)
# view_contacts()


if __name__  == "__main__":
    main()