'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
N-tice (Tuples) jsou psány v ()
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# K vytvoření tuple s pouze jedním prvkem se musí přidat čárka po prvku, jinak Python to nerozpozná jako proměnnou n-tice (tuple).
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# Lze specifikovat rozsah (range) indexů , když se určí kde začít a kde skončit
#Když se specifikuje rozsah (range), návratová hodnota bude nová n-tince (tuple) se specifickými prvky.
print(f'chars[2:5]: {chars[2:5]}')

#Záporná indexace znamená, že se začíná od konce, -1 je poslední prvek, -2 je předposlední prvek atd.
# Specifikuj záporné indexy jestli chceš začít vyhledávat od konce n-tice (tuple):
# Tento příklad vrací prvky od indexu -4 (také zahrnut) do indexu -1 (není zahrnut)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# K zjištění kolik prvků n-tice (tuple) má se využívá metoda len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
