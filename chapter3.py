# **************************************
# The chapter 3 section
# **************************************
print("\n")
print("Third chapter")
print("\n")
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

# Exercise 3.1
# Given the following vowels 'a', 'e', 'i', 'o', 'u'
# Count each vowel inside the text file
# **Output:
# Vowel name    Count
#     a         170
# **Sum of all the vowels in paragraph 1
# **Sum of all the vowels in paragraph 2
# **Sum of vowels in paragraph 1 and 2
# **Print the results of the union between both paragraphs
# **Print the results of the intersection between both paragraphs
# **Print the results of the diference between both paragraphs
# **Print the most used word on each paragraph
# **Print the least used word on each paragraph
# If only one word is found, just add it to an
# array and print the lenngth of the array.

print("\n")
print("Excercice 3.1")
print("\n")

p1Count = {'vowelA': 0,'vowelE': 0,'vowelI': 0,'vowelO': 0, 'vowelU': 0}
p2Count = {'vowelA': 0,'vowelE': 0,'vowelI': 0,'vowelO': 0, 'vowelU': 0}
p1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra."
p2 = "Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst."

for i in range(len(p1)):
    if p1[i] == 'a':
        p1Count['vowelA'] += 1
    elif p1[i] == 'e':
        p1Count['vowelE'] += 1
    elif p1[i] == 'i':
        p1Count['vowelI'] += 1
    elif p1[i] == 'o':
        p1Count['vowelO'] += 1
    elif p1[i] == 'u':
        p1Count['vowelU'] += 1

for i in range(len(p2)):
    if p2[i] == 'a':
        p2Count['vowelA'] += 1
    elif p2[i] == 'e':
        p2Count['vowelE'] += 1
    elif p2[i] == 'i':
        p2Count['vowelI'] += 1
    elif p2[i] == 'o':
        p2Count['vowelO'] += 1
    elif p2[i] == 'u':
        p2Count['vowelU'] += 1

dataTable3 = [
    ["Paragraph","Vowel name","Count"],
    ["1","a",p1Count['vowelA']],
    ["1","e",p1Count['vowelE']],
    ["1","i",p1Count['vowelI']],
    ["1","o",p1Count['vowelO']],
    ["1","u",p1Count['vowelU']],
    ["---------","-----","-------"],
    ["2","a",p2Count['vowelA']],
    ["2","e",p2Count['vowelE']],
    ["2","i",p2Count['vowelI']],
    ["2","o",p2Count['vowelO']],
    ["2","u",p2Count['vowelU']],
    ["---------","-----","-------"],
    ["1","a, e, i, o, u",sum(p1Count.values())],
    ["2","a, e, i, o, u",sum(p2Count.values())],
    ["Both","All",sum(p2Count.values())+sum(p1Count.values())],
]
print("The first paragraph is: ")
print(p1)
print("The secondt paragraph is: ")
print(p2)
print(AsciiTable(dataTable3).table)
