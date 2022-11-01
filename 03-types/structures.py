def read_txtfile(filename):
    f = open(filename, "r",encoding='utf8')
    return f.read()

def write_txtfile(filename, text):
    f = open(filename, "w",encoding='utf8')
    f.write(text)
    f.close()
    return True

def char_frekvence(txt):
    return sorted([(char, txt.count(char)) for char in set(txt)],
                  reverse =True, key=lambda i: i[1])
print(read_txtfile('list.py'))
pokus = 'rajkldjklgjlksljkf'

write_txtfile('frekvence.txt',str(char_frekvence(read_txtfile('list.py'))))
