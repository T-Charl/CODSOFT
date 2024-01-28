import csv
import pandas


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
    with open("Contact_book\contact_book.csv", 'a') as contact_book:
        writer = csv.writer(contact_book)
        writer.writerow([name, surname, phone, email, address])

# add_contact()
        

def delete_contact():
    contact_name = input().strip().title()


    delete = pandas.read_csv('Contact_book\contact_book.csv',  index_col='name')
    delete = delete.drop(contact_name)
    # delete = delete.drop(columns=['Unnamed: 0'])

# Save the DataFrame to a CSV file without including the index
    delete.to_csv('Contact_book\contact_book.csv', index=True)
    # delete.to_csv('Contact_book\contact_book.csv')
delete_contact()