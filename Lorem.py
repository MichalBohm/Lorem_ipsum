
import random
import string

abeceda = 'abcčdďeěéfghiíjklmnňoópqrřsštťuúůvyýzž'
abeceda_bez_carek = 'abcčdďeěfghijklmnňopqrřsštťuvyzž'

dlouha_pismena = input("Dlouhé písmena? př.(ý,é) (y/n)")
Pocet_odstavcu = int(input("Počet odstavců? "))
pocet_slov = int(input("Počet slov?"))
if dlouha_pismena == "y":
    for i in range(Pocet_odstavcu):
        pocet_vet_v_odstavci = random.randint(1, 6)
        odstavec=[]
        for y in range(pocet_vet_v_odstavci):

            Slova = []

            while len(Slova) < pocet_slov:
                Slovo = "".join(random.sample(abeceda, random.randint(4,8)))

                if Slovo not in Slova:
                    nalezene_slovo_I = [char for char in Slovo if char in 'cčďjňšťřž']
                    if len(nalezene_slovo_I) > 0:
                        index = Slovo.index(nalezene_slovo_I[0])

                        if index < len(Slovo) - 1 and Slovo[index + 1] != 'y' and Slovo[index + 1] != 'č' and Slovo[index + 1] != 'c' and Slovo[index + 1] != 'ď' and Slovo[index + 1] != 'j' and Slovo[index + 1] != 'ň' and Slovo[index + 1] != 'š' and Slovo[index + 1] != 'ť' and Slovo[index + 1] != 'ř' and Slovo[index + 1] != 'ž' and Slovo[index + 1] != 'ě':
                            Slova.append(Slovo)
                if Slovo not in Slova:
                    nalezene_slovo_Y = [char for char in Slovo if char in 'hkr']
                    if len(nalezene_slovo_Y) > 0:
                        index = Slovo.index(nalezene_slovo_Y[0])

                        if index < len(Slovo) - 1 and Slovo[index + 1] != 'i':
                            Slova.append(Slovo) 

            veta = ' '.join(Slova).capitalize() + '.'
            odstavec.append(veta)

        seznam = '\n'.join(odstavec)
        print(seznam)
        print()

elif dlouha_pismena == "n":
    for i in range(Pocet_odstavcu):
        pocet_vet_v_odstavci = random.randint(1, 6)
        odstavec=[]
        for y in range(pocet_vet_v_odstavci):

            Slova = []

            while len(Slova) < pocet_slov:
                Slovo = "".join(random.sample(abeceda_bez_carek, random.randint(4,8)))

                if Slovo not in Slova:
                    nalezene_slovo_I = [char for char in Slovo if char in 'cčďjňšťřž']
                    if len(nalezene_slovo_I) > 0:
                        index = Slovo.index(nalezene_slovo_I[0])

                        if index < len(Slovo) - 1 and Slovo[index + 1] != 'y' and Slovo[index + 1] != 'č' and Slovo[index + 1] != 'c' and Slovo[index + 1] != 'ď' and Slovo[index + 1] != 'j' and Slovo[index + 1] != 'ň' and Slovo[index + 1] != 'š' and Slovo[index + 1] != 'ť' and Slovo[index + 1] != 'ř' and Slovo[index + 1] != 'ž' and Slovo[index + 1] != 'ě':
                            Slova.append(Slovo)
                if Slovo not in Slova:
                    nalezene_slovo_Y = [char for char in Slovo if char in 'hkr']
                    if len(nalezene_slovo_Y) > 0:
                        index = Slovo.index(nalezene_slovo_Y[0])

                        if index < len(Slovo) - 1 and Slovo[index + 1] != 'i':
                            Slova.append(Slovo) 

            veta = ' '.join(Slova).capitalize() + '.'
            odstavec.append(veta)

        seznam = '\n'.join(odstavec)
        print(seznam)
        print()
        

print("""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
         =) ^Y^ (=            .              '
          \  ^  /
           )=*=(       *
          /     \
          |     |
         /| | | |\
         \| | |_|/\
  jgs_/\_//_// ___/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  | \_) |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
""")
