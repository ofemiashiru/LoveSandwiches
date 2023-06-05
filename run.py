# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures - while loop used to continually
    question user until the data entered is valid
    """
    while True:
        print('Please enter sales data from the last market')
        print('Data should be 6 numbers separated by commas')
        print('e.g. 5,10,15,20,25,30\n')

        # request user input
        data_str = input('Please enter data: ')
        # splits user entry into list by the commas
        sales_data = data_str.split(",")

        # checks that the data is valid using the validate_data() function
        if validate_data(sales_data):
            print('Data entered is valid!')
            break

    # if data is valid returns list of integers using list comprehension
    return [int(n) for n in sales_data]


def validate_data(values):
    """
    Try, converts all string values to ints
    """
    try:
        # converts user input to integers
        [int(n) for n in values]

        # checks that user has entered exactly 6 items
        if len(values) != 6:
            raise ValueError(
                f'You need exactly 6 items and you have entered {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True

# Refactored code
# def update_sales_worksheet(data):
#     """
#     Sends data entered by user to the Google Sheets document adding a new row
#     """
#     print('Updating sales worksheet...\n')

#     # worksheet() method helps access the individual worksheet in Sheets
#     sales_worksheet = SHEET.worksheet('sales')

#     # append_row() method adds a new row to the worksheet with our chosen data
#     sales_worksheet.append_row(data)

#     print('Sales worksheet updated successfully!\n')

# Refactored code
# def update_surplus_worksheet(data):
    """
    Sends the new surplus data to the surplus worksheet 
    """
    # print('Updating surplus worksheet...\n')

    # worksheet() method helps access the individual worksheet in Sheets
    # surplus_worksheet = SHEET.worksheet('surplus')

    # append_row() method adds a new row to the worksheet with our chosen data
    # surplus_worksheet.append_row(data)

    # print('Surplus worksheet updated successfully!\n')


def update_worksheet(data, worksheet):
    """
    Update the relevant worksheet with the new row of data
    """

    print(f'Updating {worksheet} worksheet...\n')

    # worksheet() method helps access the individual worksheet in Sheets
    new_worksheet = SHEET.worksheet(worksheet)

    # append_row() method adds a new row to the worksheet with our chosen data
    new_worksheet.append_row(data)

    print(f'{worksheet.capitalize()} worksheet updated successfully!\n')


def calculate_surplus(sales_row):
    """
    Calcualtes the surplus data
    """
    print('Calculating surplus...\n')

    stock = SHEET.worksheet('stock')
    stock = stock.get_all_values()
    # list comprehension to return values as int not str
    stock_row = [int(num) for num in stock[-1]]

    surplus_data = []
    # using zip to iterate through two collections
    for stock, sale in zip(stock_row, sales_row):
        surplus_data.append(stock - sale)
    
    return surplus_data


def main():
    """
    Runs all main functions -
    common practice to place all main function calls
    into one function called main()
    """
    sales_data = get_sales_data()
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus(sales_data)
    update_worksheet(new_surplus_data, "surplus")


print('Welcome to Love Sandwiches Database\n')
# calling our main initial functions
main()
