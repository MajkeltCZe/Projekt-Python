import physics as ph
choice = input("vyberova tabulka:\n"
             "\'zeme\' - Vypocita, jakou tihou pusobis na Zemi, podle zadane hmotnosti \n"
             "\'mesic\' - Vypocita, jakou tihou bys pusobil na Mesic, podle zadane hmotnosti \n"
             "\'svetlo\' - Vypocita, za koliv vterin urazis nejak vzdalenost, pokud bys se pohybal rychlosti svetla\n"
             "\'zvuk\' - Vypocita, za koliv vterin urazis nejak vzdalenost, pokud bys se pohybal rychlosti zvuku\n"
               "Pro vyber vypoctu napis jednu z moznych variant: ")

match choice:
    case "zeme":
        kg = input("Zadej hmotnost v kg:")
        print(f"Pusobite {ph.zeme(float(kg))}N na Zemi.")

    case  "mesic":
        kg = input("Zadej hmotnost v kg:")
        print(f"Pusobili byste {ph.mesic(float(kg))}N na Mesic.")

    case 'svetlo':
        s = input("Zadej vzdalenost v m:")
        print(f"Vzdalenost {s} bys urazil za {ph.cestovani_svetlem(float(s))} vterin pri cestovani svetlem.")

    case 'zvuk':
        s = input("Zadej vzdalenost v m:")
        print(f"Vzdalenost {s} bys urazil za {ph.cestovani_zvukem(float(s))} vterin pri cestovani zvukem.")

    case _:
        print("\nSpatne zadano :/, ale abyste nebyli smutni zde aspon mensi vypocet :)\n"
              f" cestka k mesici, coz je {ph.MOON_TO_EARTH} metru, by trvala svetelnou rychlosti {ph.cesta_k_mesici()} vterin. ")
        


