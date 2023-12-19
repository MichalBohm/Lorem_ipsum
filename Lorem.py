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
#    print()¨
#import random
#import string
#
#abeceda = 'abcčdďeěfghiíjklmnňoópqrsštťuúůvwxyýzž'
#
#Pocet_odstavcu = int(input("Počet odstavců? "))
#
#for i in range(Pocet_odstavcu):
#    x = random.randint(1, 6)
#    
#    for y in range(x):
#        pocet_slov = random.randint(4, 8)
#        Slova = []
#        
#        while len(Slova) < pocet_slov:
#            Slovo = "".join(random.sample(abeceda, random.randint(3, 8)))
#            
#            if Slovo not in Slova:
#                index_č = Slovo.find("č")
#                index_ď = Slovo.find("ď")
#                index_j = Slovo.find("j")
#                index_ň = Slovo.find("ň")
#                index_š = Slovo.find("š")
#                index_ť = Slovo.find("ť")
#                if index_č != -1 or index_č < len(Slovo) - 1 and index_ď != -1 or index_ď < len(Slovo) - 1 and index_j != -1 or index_j < len(Slovo) - 1 and index_ň != -1 or index_ň < len(Slovo) - 1 and index_š != -1 or index_š < len(Slovo) - 1 and index_ť != -1 or index_ť < len(Slovo) - 1:   
#                    next_letter_č = Slovo[index_č + 1]
#                    next_letter_ď = Slovo[index_ď + 1]
#                    next_letter_j = Slovo[index_j + 1]
#                    next_letter_ň = Slovo[index_ň + 1]
#                    next_letter_š = Slovo[index_š + 1]
#                    next_letter_ť = Slovo[index_ť + 1]
#                    if next_letter_č == 'i' or next_letter_ď == 'i' or next_letter_j == 'i' or next_letter_ň == 'i' or next_letter_š == 'i' or next_letter_ť == 'i':
#                        Slova.append(Slovo)
#            else:
#                    Slovo = "".join(random.sample(abeceda, random.randint(3, 8)))
#                    
#                    
#                    
#                    
#                    
#print(Slova)

import random
import string

abeceda = 'abcčdďeěfghiíjklmnňoópqrřsštťuúůvwxyýzž'
abeceda = abeceda.replace('a', 'a' / 3)
Pocet_odstavcu = int(input("Počet odstavců? "))

for i in range(Pocet_odstavcu):
    x = random.randint(1, 6)
    odstavec=[]
    for y in range(x):
        pocet_slov = random.randint(10, 34)
        Slova = []
        
        while len(Slova) < pocet_slov:
            Slovo = "".join(random.sample(abeceda, random.randint(3,8)))
            
            if Slovo not in Slova:
                nalezene_slovo_I = [char for char in Slovo if char in 'cčďjňšťřž']
                if len(nalezene_slovo_I) > 0:
                    index = Slovo.index(nalezene_slovo_I[0])
                    
                    if index < len(Slovo) - 1 and Slovo[index + 1] == 'i':
                        Slova.append(Slovo)
            if Slovo not in Slova:
                nalezene_slovo_Y = [char for char in Slovo if char in 'hkr']
                if len(nalezene_slovo_Y) > 0:
                    index = Slovo.index(nalezene_slovo_Y[0])
                    
                    if index < len(Slovo) - 1 and Slovo[index + 1] == 'y':
                        Slova.append(Slovo) 
        
        sentence = ' '.join(Slova).capitalize() + '.'
        odstavec.append(sentence)

    seznam = '\n'.join(odstavec)
    print(seznam)
    print()

