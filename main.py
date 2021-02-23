# Textový analýzátor - Projekt 5 / Michal Hovorka

# Registrovaní uživatelé
# | USER      |   PASSWORD  |
# -----------------------
# | bob       |     123     |
# | ann       |    pass123  |
# | mike      | password123 |
# | liz       |    pass123  |

login_data = {'bob': '123',
              'ann': 'pass123',
              'mike': 'password123',
              'liz': 'pass123'
              }

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input('Zadej své jméno: ')
heslo = input('Zadej heslo: ')

print('-' * 65)

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
if login_data.get(jmeno) == heslo:
    print('Vítej v aplikaci "TexAN", ' + jmeno + '!' \
          + ' Počet článků k analýze textu: ' + str(len(TEXTS)))
else:
    print('Heslo, nebo uživatelské jméno je špatně')
    exit()

print('-' * 65)

# vstup od uživatele (výber článku)
vyber_text = input('Zadej pořadové číslo článku (v rozmezí 1 až ' + str(len(TEXTS)) + '): ')

print('-' * 65)

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

print('-' * 65)

# vybírám zdroj článku do textu s první odpovědí
vybrany_text = TEXTS.get(vyber_text)
zdroj_clanku = (vybrany_text["zdroj"])

# List s jednotlivymi slovy a list s ocistenymi slovy
text = TEXTS[vyber_text]["text"].split(" ")
# =================================================================================
w_list = []  # očištěná slová !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for word in text:
    w_list.append(word.strip(".,!?/"))
# =================================================================================

# počítám slova ve vybranem textu
word_lst = []
for word in w_list:
    word_lst.append(word)

# počítám slova s velkym a malym pocatecnim pismenem ve vybranem textu
title_case = []
without_tc = []
for word in w_list:
    if word.islower():
        without_tc.append(word)
    else:
        title_case.append(word)
tc_alpha = [word for word in title_case if word.isalpha()]

# Počet slov psaných velkými písmeny (všechna písmena ve slově jsou velká)
other_low = []
upper_words = []
for word in w_list:
    upper_words.append(word) if word.isupper() else other_low.append(word)
uw_alpha = [word for word in upper_words if word.isalpha()]

# Počet slov psaných malými písmeny (všechna písmena ve slově jsou malá)
other_upp = []
lower_words = []
for word in w_list:
    lower_words.append(word) if word.islower() else other_upp.append(word)


# Počet cisel
def pocet_cisel(cislo_v_textu):
    return len([int(i) for i in cislo_v_textu if type(i) == int or i.isdigit()])


# Součet cisel
def soucet_cisel(cislo_v_textu):
    return sum([int(i) for i in cislo_v_textu if type(i) == int or i.isdigit()])


# Výsledky výpočtů - tisk/zobrazení
print('Počet slov ve vybraném článku od agentury' + ' ' + str(zdroj_clanku) + ': ' + str(len(word_lst)))
print('Počet slov začínajících velkým písmenem ve vybraném článku: ' + str(len(tc_alpha)))
print('Počet slov psaných velkým písmem: ' + str(len(uw_alpha)))
print('Počet slov psaných malým písmem: ' + str(len(lower_words)))
print('Počet všech čísel (ne cifer) ve vybraném článku: ' + str(pocet_cisel(w_list)))
print('Součet všech čísel (ne cifer) ve vybraném článku: ' + str(soucet_cisel(w_list)))

print('-' * 65)

# Četnost occurence_grafu dle délky
by_length = dict()
for slovo in w_list:
    for range_in in range(30):
        if len(slovo) == range_in:
            by_length[str(range_in)] = by_length.setdefault(str(range_in), 0) + 1

# Klíče na cisla
keys_for_num = list(by_length.keys())
for i in range(0, len(keys_for_num)):
    keys_for_num[i] = int(keys_for_num[i])
keys_for_num.sort(reverse=True)

# Graf tabulka
occurence_graf = "  Výskyt - graf. znázornění   "
print("Délka slov |" + occurence_graf + "|Počet znaků")

print('=' * 65)

for numbered_graf in range(1, (keys_for_num[0] + 1)):
    gap_graf = int((4 - len(str(numbered_graf)))) * " "
    if numbered_graf in keys_for_num:
        print('    ' + str(numbered_graf), str(gap_graf) + "  |", by_length.get(str(numbered_graf)) \
              * "*", ((len(occurence_graf) - 3) - by_length.get(str(numbered_graf))) \
              * " " + " |", by_length.get(str(numbered_graf)))

print('=' * 65)
