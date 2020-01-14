import requests
x = requests.get('https://raw.githubusercontent.com/JoePotentier/cmput-404-labs/master/lab1/printMyself.py?token=ACJZXVDB33YNYQ5SNB6F66C6E2B3I')
print(x.text)
