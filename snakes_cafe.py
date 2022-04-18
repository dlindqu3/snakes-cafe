print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']

print('Appetizers')
print('----------')
for item in appetizers: 
  print(item)

entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Litteral Garden']

print('Entrees')
print('-------')
for item in entrees: 
  print(item)

desserts = ['Ice Cream', 'Cake', 'Pie']

print('Desserts')
print('--------')
for item in desserts: 
  print(item)

drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print("""
Drinks
------
""")
for item in drinks: 
  print(item)

print("""
***********************************
** What would you like to order? **
***********************************
""")

items = {}

while True: 
  selection = input('> ')
  # print(selection, 'selected')
  if selection == 'quit': 
    break 
  elif selection and not items.get(selection): 
    items[selection] = 1
  elif selection and items[selection]: 
    items[selection] += 1
  print(f"** {items[selection]} order of {selection} have been added to your meal **")

