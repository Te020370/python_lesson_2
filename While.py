# Цикл  While

# Простейший while
i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5: break

answer = None
while answer != 'Volvo':
    answer = input("Введите лучшую марку автомобиля: ")
print("Вы абсолютны правы")

while i < 10:
    print(i)
    i += 1
    if i == 9: break
    if i < 3: continue

# Простейший for
for i in range(10):
    print(i)
    if i == 5: break

for i in range(10):
    answer = input("Введите лучшую марку автомобиля: ")
    if answer == "Volvo":
        print("Вы абсолютны правы")
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)