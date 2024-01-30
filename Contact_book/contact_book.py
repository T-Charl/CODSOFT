import csv
import sys
import pandas



def main():
    user =input("""Welcome to Contact Book.
Would you like to create your personal contact book? Y/n? """)
    
    while True:
        if user.lower() == 'n':
            sys.exit("Thank You.\nPlease try again when you would like to make a contact book.")
        elif user.lower() == 'y':
            print("Let's get started")
            add_contact()
        else:
            user = input('Would you like to create your personal contact book? Y/n?')




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
delete_contact()


def read_csv():
    with open('/workspaces/CODSOFT/Contact_book/contact_book.csv', 'r') as book:
        red = csv.reader(book)
        for i in red:
            if 'False' in i:
                delete_contact(i[0])
            else:
                print(i)

# read_csv()


if __name__  == "__main__":
    pass
    # main()