#import random
#import string
#
#odstavce = int(input("Počet odstavců? "))
#cisilka = [4, 5, 6, 7, 8]
#
#str_characters = 'abcčdďefghijklmnopqrstuvwxyz'
#
#for _ in range(odstavce):
#    x = random.randint(1, 5)  
#    odstavec = []
#
#    for i in range(x):
#        delka = random.choice(cisilka)
#        Slova = []
#
#        while len(Slova) < delka:
#            Slovo = ''.join(random.sample(str_characters, random.randint(3, 8)))
#            if Slovo not in Slova:
#                Slova.append(Slovo)
#
#        sentence = ' '.join(Slova).capitalize() + '.'
#        odstavec.append(sentence)
#
#    seznam = '\n'.join(odstavec)
#    print(seznam)
#    print()