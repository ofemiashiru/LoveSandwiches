# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

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
    Get sales figures
    """

    print('Please enter sales data from the last market')
    print('Data should be 6 numbers separated by commas')
    print('e.g. 5,10,15,20,25,30\n')

    data_str = input('Enter data: ')
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Try, converts all string values to ints
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f'You need exactly 6 items and you have entered {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')

get_sales_data()
