# Оператор условия

brand = 'Volvo'
engine_volume = 1.5
horsepower = 79
sunroof = True
 # Проверка условия if

if horsepower < 80:
    print('No Tax')


# Проверка условия if/else
if horsepower < 80: print('No Tax')
else: print('Tax')

# Проверка уловия if/elif/else

tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else: tax = 50000
print(tax)

# Проверка условия if для присаивания

cool_car = 0
cool_car = 1 if sunroof == 1 else  0
print(sunroof)