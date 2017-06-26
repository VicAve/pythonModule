from terminaltables import AsciiTable

#aeiou
#exam scores
arturo = [90, 100, 50, 70]
artemio = [70, 65, 100, 80]
juan = [90, 90, 100, 80]
rene = [50, 60, 70, 80]
pedro = [100, 50, 100, 90]

# Excercise 1 :
# print the average score of each student
# score > 95 : Excentado
# score < 95 and > 85 : Aprobado
# score >= 70 : promedio
# score < 70 : Reprobado
names = ["Arturo", "Artemio", "Juan", "Rene", "Pedro"]
students = [arturo, artemio, juan, rene, pedro]
hl = []
table_data = [
    ['Student', 'Score', 'Status', 'Highest Score', 'Lowest Score']
]
for i in range(len(students)):
    scores = students[i]
    avg = (sum(scores)/len(scores))
    hl.append(avg)
    if avg > 95:
        table_data.append([names[i], avg, "Excentado", max(scores), min(scores)])
    elif avg < 95 and avg > 85:
        table_data.append([names[i], avg, "Aprobado", max(scores), min(scores)])
    elif avg >= 70:
        table_data.append([names[i], avg, "Promedio", max(scores), min(scores)])
    elif avg < 70:
        table_data.append([names[i], avg, "Reprobado", max(scores), min(scores)])

table_hl = [
    ['The highest Score is:', max(hl)],
    ['The lowest Score is:', min(hl)]
]
print("\n")
print("First excercise")
print("\n")
table = AsciiTable(table_data)
print (table.table)
print (AsciiTable(table_hl).table)

# print("Excercise 1:")
# print("The Average score of Arturo is: ",sum(arturo)/len(arturo))
# print("The Average score of Artemio is: ",sum(artemio)/len(artemio))
# print("The Average score of Juan is: ",sum(arturo)/len(arturo))
# print("The Average score of Rene is: ",sum(rene)/len(rene))
# print("The Average score of Pedro is: ",sum(pedro)/len(pedro))

# Excercise 2.2
# a=1, e=2, i=3, o=4, u=5
# x = "Tesla" => [2,1]
# y = "Buick"
# z = "Ferrari"
# w = "Ford"
# t = "Lamborghini"
# p = "Masertati"
# Iterate over all the cars
# **Create an array for each car => print(car_vowels_array)
# Each array will hold the vowel value => x = "Tesla" => [2,1]
# **At the end construct an array containing all the cars vowels
# print(car_vowels_from_all_the_cars)
# **With the previous array filter the vowel value like this:
# vowel_value %2 == 0: 'Buy it'
# vowel_value %3 == 0: 'Sell it'

# Function for extract the vowels from String
def getVowels( string ):
    result_array = []
    vowelCode = 0
    for i in range(len(string)):
        if (string[i] == 'a'):
            vowelCode = 1
            result_array.append(vowelCode)
        elif (string[i] == 'e'):
            vowelCode = 2
            result_array.append(vowelCode)
        elif (string[i] == 'i'):
            vowelCode = 3
            result_array.append(vowelCode)
        elif (string[i] == 'o'):
            vowelCode = 4
            result_array.append(vowelCode)
        elif (string[i] == 'u'):
            vowelCode = 5
            result_array.append(vowelCode)
    return result_array

def getAction( args ):
    arraySum = sum(args)
    resultArray = "You're ok"
    if arraySum % 2 == 0:
        resultArray = "Buy it!"
    elif arraySum % 3 == 0:
        resultArray = "Sell it!"
    return resultArray



x = "Tesla"
y = "Buick"
z = "Ferrari"
w = "Ford"
t = "Lamborghini"
p = "Masertati"
allArrayVowels = []
xVowels = getVowels(x)
yVowels = getVowels(y)
zVowels = getVowels(z)
wVowels = getVowels(w)
tVowels = getVowels(t)
pVowels = getVowels(p)
allArrayVowels.extend([xVowels,yVowels,zVowels,wVowels,tVowels,pVowels])
xDecision = getAction(xVowels)
yDecision = getAction(yVowels)
zDecision = getAction(zVowels)
wDecision = getAction(wVowels)
tDecision = getAction(tVowels)
pDecision = getAction(pVowels)

dataVowels = [
    ["Car Manufacturer","Vowels Code"],
    [x,xVowels],
    [y,yVowels],
    [z,zVowels],[w,wVowels],[t,tVowels],[p,pVowels]
]
dataAllVowels = [["All Data Vowels"],[allArrayVowels]]
dataSellBuy = [
    ["Car Manufacturer","Buy or Sell"],
    [x,xDecision],[y,yDecision],[z,zDecision],[w,wDecision],[t,tDecision],[p,pDecision]
]

print("\n")
print("Second excercise")
print("\n")
print(AsciiTable(dataVowels).table)
print(AsciiTable(dataAllVowels).table)
print(AsciiTable(dataSellBuy).table)
