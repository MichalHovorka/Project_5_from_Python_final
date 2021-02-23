# Textový analýzátor - Projekt 5 / Michal Hovorka

# Registrovaní uživatelé
# | USER      |   PASSWORD  |
# -----------------------
# | bob       |     123     |
# | ann       |    pass123  |
# | mike      | password123 |
# | liz       |    pass123  |
# | Miky      |    123      |

data = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123', 'Miky': '123'}

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input('Zadej své jméno: ')
heslo = input('Zadej heslo: ')

print('-' * 100)

# definování proměnných (3 texty k vyhodnocení)
zdroj1 = 'BBC'
text1 = 'Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.'
zdroj2 = 'REUTER'
text2 = 'At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.'
zdroj3 = 'AFP'
text3 = 'The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.'

# vytvoření databáze TEXTS a naplnění z proměnných Text 1-3
TEXTS = {}
TEXTS['1'] = dict((("zdroj", zdroj1), ("text", text1)))
TEXTS['2'] = dict((("zdroj", zdroj2), ("text", text2)))
TEXTS['3'] = dict((("zdroj", zdroj3), ("text", text3)))

# Vyhodnocení jména a hesla
if data.get(jmeno) == heslo:
    print('Vítej v aplikaci "TexAN", ' + jmeno + '!' \
          + ' K analýze textu je aktuálně k dispozici tento počet článků: ' \
          + str(len(TEXTS)))
else:
    print('Heslo, nebo uživatelské jméno je špatně!')
    exit()

print('-' * 100)

# vstup od uživatele (výber článku)
vyber_text = input('Zadej pořadové číslo článku (v rozmezí 1 až ' + str(len(TEXTS)) + '): ')

print('-' * 100)

# Porovnávám, že zadaná hodnota je typu INT (nelze porovnávat type v if-else bloku, použil jsem try-expect block):
try:
    tmp = int(vyber_text)
    print('Vybral jsi článek číslo: ' + vyber_text)
except:
    print('Nezadal jsi celé číslo')
    exit()

# Vyhodnocení zdali existuje vybraný článek ve slovníku
if vyber_text in TEXTS.keys():
    print('Analyzuji text...')
else:
    print('K dispozici jsou pouze ' + str(len(TEXTS)) + ' články')
    exit()
print('-' * 100)

# vybírám zdroj článku do textu s první odpovědí
vybrany_text = TEXTS.get(vyber_text)
zdroj_clanku = (vybrany_text["zdroj"])

# List s jednotlivymi slovy a list s ocistenymi slovy
text = TEXTS[vyber_text]["text"].split(" ")  # Takto se dostanu k jednotlivym slovum
# =================================================================================
w_list = []  # očištěná slová !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for word in text:
    w_list.append(word.strip(".,!?/"))
# =================================================================================

# počítám slova ve vybranem textu
words_list = []
for word in w_list:
    words_list.append(word)
print('Počet slov ve vybraném článku od agentury' + ' ' + str(zdroj_clanku) + ': ' + str(len(words_list)))

# počítám slova s velkym a malym pocatecnim pismenem ve vybranem textu
withcap = []
without = []
for word in w_list:
    if word.islower():
        without.append(word)
    else:
        withcap.append(word)
withcap_alpha = [word for word in withcap if word.isalpha()]
print('Počet slov začínajících velkým písmenem ve vybraném článku: ' + str(len(withcap_alpha)))

# Počet slov psaných velkými písmeny (všechna písmena ve slově jsou velká)
other_low = []
uppers = []
for word in w_list:
    uppers.append(word) if word.isupper() else other_low.append(word)
uppers_alpha = [word for word in uppers if word.isalpha()]
print('Počet slov psaných velkým písmem: ' + str(len(uppers_alpha)))

# Počet slov psaných malými písmeny (všechna písmena ve slově jsou malá)
other_upp = []
lowers = []
for word in w_list:
    lowers.append(word) if word.islower() else other_upp.append(word)
print('Počet slov psaných malým písmem: ' + str(len(lowers)))


# Počet cisel
def pocet_cisel(cislo_v_textu):
    return len([int(i) for i in cislo_v_textu if type(i) == int or i.isdigit()])


print('Počet všech čísel (ne cifer) ve vybraném článku: ' + str(pocet_cisel(w_list)))


# Součet cisel
def soucet_cisel(cislo_v_textu):
    return sum([int(i) for i in cislo_v_textu if type(i) == int or i.isdigit()])


print('Součet všech čísel (ne cifer) ve vybraném článku: ' + str(soucet_cisel(w_list)))

print('-' * 100)

# Četnost vyskytu dle délky
podle_delky = dict()
for slovo in w_list:
    for rozmezi in range(30):
        if len(slovo) == rozmezi:
            podle_delky[str(rozmezi)] = podle_delky.setdefault(str(rozmezi), 0) + 1

# Klíče na cisla
klice = list(podle_delky.keys())
for i in range(0, len(klice)):
    klice[i] = int(klice[i])
klice.sort(reverse=True)

# graf tabulka
vyskyt = "             Výskyt              "
print("Délka|" + vyskyt + "|Počet")
print('=' * 100)
for cislovani in range(1, (klice[0] + 1)):
    mezerka = int((4 - len(str(cislovani)))) * " "
    if cislovani in klice:
        print(cislovani, mezerka + "|", podle_delky.get(str(cislovani)) \
              * "*", ((len(vyskyt) - 3) - podle_delky.get(str(cislovani))) \
              * " " + " |", podle_delky.get(str(cislovani)))

print('=' * 100)
