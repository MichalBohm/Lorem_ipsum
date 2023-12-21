Český Lorem ipsum generátor (tak trochu)

Řešil jsem to pomocí stringu, ve kterém je zapsaná celá abeceda bez W, X, CH. 

    abeceda = 'abcčdďeěéfghiíjklmnňoópqrřsštťuúůvyýzž'
    abeceda_bez_carek = 'abcčdďeěfghijklmnňopqrřsštťuvyzž'
    dlouha_pismena = input("Dlouhé písmena? př.(ý,é) (y/n)")

Uživatel je vyzván programem na počet odstavců a vět a jestli uživatel chce dlouhé písmena.

    Pocet_odstavcu = int(input("Počet odstavců? "))
    pocet_slov =int(input("Počet slov?"))


Poté začne for cyklus který se opakuje na základě počtu odstavců.
V něm se vygeneruje počet vět v odstavci a seznam s názvem odstavec.

    for i in range(Pocet_odstavcu):
        pocet_vet_v_odstavci = random.randint(1, 6)
        odstavec=[]

Dále se spustí cyklus, ve kterém se vytvoří seznam "Slova"

    for y in range(pocet_vet_v_odstavci):
        Slova = []

A začne cyklus while len(Slova) < pocet_slov:
    tento cyklus bude pokračovat dokud aktuální délka seznamu "Slova" nebude dosahovat požadovaného počtu slov.

Poté se generuje náhodné slovo pomocí funkcí random.sample a random.randint.
Slovo je sestaveno náhodným výběrem znaků z abecedy a jeho délka je mezi 8 a 14 znaky
Pomocí iterace a komprehence https://www.itnetwork.cz/python/kolekce/komprehence-lambda-vyrazy-a-funkce-v-pythonu

    Slovo = "".join(random.sample(abeceda, random.randint(8,14))) 

Kontroluje duplikáty v seznamu.
Když není duplikát tak hledá jestli v "Slovo" je nějáké z těchto písmen

    if Slovo not in Slova:
        nalezene_slovo_I = [char for char in Slovo if char in 'cčďjňšťřž']

zjišťuje jestli je nějaký z těhle znaků 'cčďjňšťřž' v nalezene_slovo_I
a jestli je, tak vytvoří proměnnou "index která nachází pozici prvního písmena z "nalezene_slovo_I" v "Slovo"

    if len(nalezene_slovo_I) > 0:
        index = Slovo.index(nalezene_slovo_I[0])
   
pokud proměnná index je menší než délka "Slovo" - 1 a ve "Slovo" není za 'cčďjňšťřž' "y" 
tak se "Slovo" dá do seznamu "Slova"

    if index < len(Slovo) - 1 and Slovo[index + 1] != 'y' ...
        Slova.append(Slovo)

Poté se vytvoří věta s Velkým písmenem a tečkou nakonci
a "veta" se přidá do seznamu "odstavec"

    veta = ' '.join(Slova).capitalize() + '.'
            odstavec.append(veta)

poté spojil "\n" (nový řádek) a odstavec do "seznam" a ten jsem printnul
ten "print()" je pro mezery mezi odstavci. vyřešil jsem to takhle protože kdybych jen printl "odstavec" tak mi to vytiskne jen seznam těch slov

    seznam = '\n'.join(odstavec)
    print(seznam)
    print()
