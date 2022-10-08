print('Vítej', end='!\n')
print('popis: {0} {1} - {1}, které jsou {0}'.format('náhodné', 'otázky'))
jmeno = input('Zadejte své jméno, pokud byste byli nový člověk: ')
if ((jmeno) == ''):
    print('Dobře, když jsi to tak přejete. Já jsem {name}'.format(name = 'duch'))
else:
    print('Těší mě, %s.' % jmeno)
hodnota_user = input('Zadejte čiselnou hodnotu i s desetinnou čárkou, podle toho, jak dobře se cítíte: ')
hodnota = 2.62

if (float(hodnota_user) >= hodnota):
    print('Vaše hodnota na dvě desetinná místa je %3.2f a je vyšší než má. :)' %float(hodnota_user))
elif  (float(hodnota_user) == hodnota):
    print('Vaše hodnota na dvě desetinná místa je %3.2f a je stejná jako má. :D' % float(hodnota_user))
else:
    print('Vaše hodnota na dvě desetinná místa je %3.2f a je nižší než má. :/' %float(hodnota_user))
 = input('Napiš tvé oblíbené číslo: ')

