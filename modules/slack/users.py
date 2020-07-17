import os

# users = {'U014WTGDGFJ': 'Arakaki', 'U0140AQV9L6': 'Taishow', 'U014EL0EZ2Q': 'Yokotsuka'}
users = {}

users[os.getenv('TCI_USER1_ID')] = os.getenv('TCI_USER1_NAME')
users[os.getenv('TCI_USER2_ID')] = os.getenv('TCI_USER2_NAME')
users[os.getenv('TCI_USER3_ID')] = os.getenv('TCI_USER3_NAME')
