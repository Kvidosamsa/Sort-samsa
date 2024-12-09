import random

# Bubble Sort
pole = [random.randint(0, 100) for _ in range(10)]
print("Původní pole1:", pole)
for i in range(len(pole)):
    for j in range(len(pole) - 1 - i):
        if pole[j] > pole[j + 1]:
            pole[j], pole[j + 1] = pole[j + 1], pole[j]
print("Seřazené pole (Bubble Sort):", pole)

# Bogo Sort
pole2 = [random.randint(0, 100) for _ in range(5)]
print("Původní pole2:", pole2)
while pole2 != sorted(pole2):
    random.shuffle(pole2)
print("Seřazené pole (Bogo Sort):", pole2)

# Selection Sort
pole3 = [random.randint(0, 100) for _ in range(10)]
print("Původní pole3:", pole3)

for i in range(len(pole3)):
    for j in range(i + 1, len(pole3)):
        if pole3[j] < pole3[i]:
            pole3[i], pole3[j] = pole3[j], pole3[i]

print("Seřazené pole (Selection Sort):", pole3)


# Insertion Sort
pole4 = [random.randint(0, 100) for _ in range(10)]
print("Původní pole4:", pole4)
for i in range(1, len(pole4)):
    key = pole4[i]
    j = i - 1
    while j >= 0 and key < pole4[j]:
        pole4[j + 1] = pole4[j]
        j -= 1
    pole4[j + 1] = key
print("Seřazené pole (Insertion Sort):", pole4)
