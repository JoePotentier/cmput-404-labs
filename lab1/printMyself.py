import requests
x = requests.get('https://raw.githubusercontent.com/JoePotentier/cmput-404-labs/master/lab1/printMyself.py')
print(x.text)
