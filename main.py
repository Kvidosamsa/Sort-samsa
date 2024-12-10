import random

# Bubble Sort
pole = [random.randint(0, 100) for _ in range(10)]  # Vytvoreni nahodneho pole
print("Puvodni pole1:", pole)
for i in range(len(pole)):  # Prochazeni pole
    for j in range(len(pole) - 1 - i):  # Srovnavani sousednich prvku
        if pole[j] > pole[j + 1]:  # Prohozeni prvku
            pole[j], pole[j + 1] = pole[j + 1], pole[j]
print("Serazene pole (Bubble Sort):", pole)

# Bogo Sort
pole2 = [random.randint(0, 100) for _ in range(5)]  # Nahodne pole
print("Puvodni pole2:", pole2)
while pole2 != sorted(pole2):  # Dokud neni serazene tak prohazovat
    random.shuffle(pole2)
print("Serazene pole (Bogo Sort):", pole2)

# Selection Sort
pole3 = [random.randint(0, 100) for _ in range(10)]  # Nahodne pole
print("Puvodni pole3:", pole3)
for i in range(len(pole3)):  # Hledani minima
    for j in range(i + 1, len(pole3)):
        if pole3[j] < pole3[i]:  # Prohozeni minima
            pole3[i], pole3[j] = pole3[j], pole3[i]
print("Serazene pole (Selection Sort):", pole3)

# Insertion Sort
pole4 = [random.randint(0, 100) for _ in range(10)]  # Nahodne pole
print("Puvodni pole4:", pole4)
for i in range(1, len(pole4)):  # Vkladani na spravne misto
    key = pole4[i]
    j = i - 1
    while j >= 0 and key < pole4[j]:  # Posun prvku
        pole4[j + 1] = pole4[j]
        j -= 1
    pole4[j + 1] = key  # Vlozeni prvku
print("Serazene pole (Insertion Sort):", pole4)
