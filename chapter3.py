# **************************************
# The chapter 3 section
# **************************************
from terminaltables import AsciiTable

vowels = {'a', 'e', 'i', 'o', 'u'}
example = set('example')

union = vowels.union(example)
intersection = vowels.intersection(example)
print("union",union)
print("intersection",intersection)

beers = [
    {'name': 'Modelo Especial', 'price': 25.00, 'ap': 4.0},
    {'name': 'Indio', 'price': 20.00, 'ap': 4.2},
    {'name': 'Tecate Light', 'price': 30.00, 'ap': 3.5},
    {'name': 'Minerva', 'price': 35.00, 'ap': 8.0},
    {'name': 'Bud Light', 'price': 18.00, 'ap': 5.0}
]

beersDataTable = [
    ["Beer's name","Price","Alcohol Percentage"]
]

for i in range(len(beers)):
    data = beers[i]
    beersDataTable.append([data['name'],data['price'],data['ap']])

beersTable = AsciiTable(beersDataTable).table
print(beersTable)
