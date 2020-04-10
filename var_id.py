# Динамическая типизация
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False



temp_var_1 = input("Input samething!  ")
print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_var_2 = input("Input samething again!  ")
print(temp_var_2, type(temp_var_2), id(temp_var_2))

temp_var_1 = temp_var_2
temp_var_1 = int(temp_var_2)

print(temp_var_1, type(temp_var_1), id(temp_var_1))

# Приведение типов

temp_float = input("Input float number!  ")
print(temp_float, type(temp_float), id(temp_float))
if is_digit(temp_float):
    temp_float = float(temp_float)
    print(temp_float, type(temp_float), id(temp_float))
else: print("There is not number!")