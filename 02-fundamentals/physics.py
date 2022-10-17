'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 # normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 # měsíční gravitace
SPEED_OF_LIGHT = 299792458  # rychlost světla ve vakuu
SPEED_OF_SOUND = 343 # rychlost zvuku při teplotě 20 °C v suchém vzduchu

MOON_TO_EARTH = 384400000

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

'''
funkce vypočítává jakou tíhu působíme na Zemi, podle zadané hmotnosti v kg
'''
def zeme(hmotnost):
    return hmotnost * EARTH_GRAVITY

def mesic(hmotnost):
    return hmotnost * MOON_GRAVITY

'''
funkce vypočítá, čas ve vteřinách, za jak dlouho se dá dostat rychlostí světla
'''
def cesta_k_mesici():
    return MOON_TO_EARTH / SPEED_OF_LIGHT

'''
funkce vypočítá, za kolik vteřin zvládeš určitou vzdálenost v metrech, 
pokud bychom cestovali rychlosti světla ve vakuu
'''
def cestovani_svetlem(vzdalenost):
    return vzdalenost / SPEED_OF_LIGHT

def cestovani_zvukem(vzdalenost):
    return vzdalenost / SPEED_OF_SOUND