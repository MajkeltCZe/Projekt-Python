'''
 Set je množina jedinečných hodnot
 Set(množiny)  není indexováný ani uspořádaný.
 V Pythonu jsou množiny ve složených závorkách {}.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile se set (množina) vytvoří, tak nelze změnit její prvky, ale můžeš přidat nové prvky
# K přidání jednoho prvku je metoda add().
set_chars.add('V')

# K přidání více prvků do set (množiny) je metoda update().
set_chars.update('X', 'Y', 'Z')

# K odstranění prvku v množině (set), se využívá metoda remove(), nebo discard().
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metoda clear() vyprazdňuje množinu (set):
set_chars.clear()

# del odstraní množinu (set):
del set_chars

# Přístup k hodnotám množiny
# K prvkům v množině (set) nelze přistupovat přes index, protože množiny jsou neuspořádané a prvky nemají index.
# my_set[1]

# Ale lze cyklit množinou (set) pomocí for loop, nebo zjistit zda množina (set) obsahuju specifickou hodnotu pomocí klíčového slova in
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
