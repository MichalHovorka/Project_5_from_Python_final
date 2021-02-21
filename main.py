#Textový analýzátor - Projekt 5

# Registrovaní uživatelé
#| USER      |   PASSWORD  |
#-----------------------
#| bob       |     123     |
#| ann       |    pass123  |
#| mike      | password123 |
#| liz       |    pass123  |
#| Miky      |    123      |

data = {
	'bob': '123',
	'ann': 'pass123',
	'mike': 'password123',
  'liz' : 'pass123',
  'Miky' : '123'
			}

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input('Zadej své jméno: ' )
heslo = input('Zadej heslo: ')

print('-' *100)

# definování proměnných (3 texty k vyhodnocení)
zdroj1 = 'BBC'
text1 = 'Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.'
zdroj2 = 'REUTER'
text2 = 'At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.'
zdroj3 = 'AFP'
text3 = 'The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.'


# vytvoření databáze TEXTS a naplnění z proměnných Text 1-3
TEXTS = {}
TEXTS['1'] = dict((("zdroj",zdroj1),("text",text1)))
TEXTS['2'] = dict((("zdroj",zdroj2),("text",text2)))
TEXTS['3'] = dict((("zdroj",zdroj3),("text",text3)))
#print(TEXTS)

# Vyhodnocení jména a hesla
if data.get(jmeno) == heslo :
	print(
'Vítej v aplikaci "TexAN", '  + jmeno + '!' +
' K analýze textu je aktuálně k dispozici tento počet článků: ' + str(len(TEXTS))
  )
else:
    print('Heslo, nebo uživatelské jméno je špatně!')
    exit()

print('-' *100)

vyber_text = input('Zadej pořadové číslo článku (v rozmezí 1 až ' + str(len(TEXTS)) + '): ' )

print('-' *100)

#možnosti jak porovnat že zadaná hodnota je typu INT:
# - Mohu změnit type pro input (int('input('Enter... '))),'
# - nebo použít import numbers, nebo try-expect block,
# - použil jsem try-expect block:
try:
    tmp = int(vyber_text)
    print('Vybral jsi článek číslo: ' + vyber_text )
except:
    print('Nezadal jsi celé číslo')
    exit()
# Vyhodnocení pořadí text (1-3)
if vyber_text in TEXTS.keys():
    print('Analyzuji text...')
else:
    print('K dispozici jsou pouze ' + str(len(TEXTS)) + ' články')
    exit()
print('-' *100)

# počítám slova ve vybranem textu
if vyber_text in TEXTS: #upravena podminka. Ptam se zda je klic ve slovniku.
  pocet_slov = {}
  text = TEXTS[vyber_text]["text"].split(" ") #Takto se dostanu k jednotlivym slovum
  for slovo in text:
    ciste_slovo = slovo.strip(",.?!")
    pocet_slov[ciste_slovo] = pocet_slov.get(ciste_slovo,0) + 1
else:
    print("Tento klic neni ve slovniku")
    exit() #vyskoci z programu

#vybírám zdroj článku do textu odpovědí s počtem slov
vybrany_text = TEXTS.get(vyber_text)
zdroj_clanku = (vybrany_text["zdroj"])

# odpověď na první úkol (počet slov v článku)
print('Počet slov ve vybraném článku od agentury'+ ' ' + str(zdroj_clanku) + ': ' + str(sum(pocet_slov.values()))  )

# počítám slova s velkym a malym pocatecnim pismenem ve vybranem textu
if vyber_text in TEXTS: #upravena podminka. Ptam se zda je klic ve slovniku.
  word_supp = {}
  t_sup = TEXTS[vyber_text]["text"].split(" ") #Takto se dostanu k jednotlivym slovum
  for slovo in t_sup:
    ciste_slovo_s = slovo.strip(",.?!")
    word_supp[ciste_slovo_s] = word_supp.get(ciste_slovo_s,0) + 1

word_supp_k = word_supp.keys()
s = list(word_supp_k)

withcap = []
without = []
for word in s:
    if word.islower():
         without.append(word)
    else:
         withcap.append(word)
withcap_alpha = [word for word in withcap if word.isalpha()]
print('Počet slov začínajících velkým písmenem ve vybraném článku: ' + str(len(withcap_alpha)) )



#Počet slov psaných velkými písmeny (všechna písmena ve slově jsou velká)
other_low = []
uppers = []
for word in t_sup:
    uppers.append(word) if word.isupper() else other_low.append(word)

uppers_alpha = [word for word in uppers if word.isalpha()]
print('Počet slov psaných velkým písmem: ' + str(len(uppers_alpha)))


other_upp = []
lowers = []
for word in t_sup:
    lowers.append(word) if word.islower() else other_upp.append(word)

print('Počet slov psaných malým písmem: ' + str(len(lowers)) )

#počet cisel
def pocet_cisel(cislo_v_textu):
    return  len([int(i) for i in cislo_v_textu if type(i)== int or i.isdigit()])
print('Počet všech čísel (ne cifer) ve vybraném článku: '+ str(pocet_cisel(t_sup)))

#součet cisel
def soucet_cisel(cislo_v_textu):
    return  sum([int(i) for i in cislo_v_textu if type(i)== int or i.isdigit()])
print('Součet všech čísel (ne cifer) ve vybraném článku: '+ str(soucet_cisel(t_sup)))

print('-' *100)

#graf
pocet = [len(i) for i in t_sup]

[[x,pocet.count(x)] for x in set(pocet)]
[['a', 1], ['b', 2]]
slo = dict((x,pocet.count(x)) for x in set(pocet))

print( '=' *100 )
print('LEN | OCCURENCES         | NR.' )
print( '=' *100 )
print(' 1  | ------------------ |' + ' ' + str(slo.get(1))  )
print(' 2  | ------------------ |' + ' ' + str(slo.get(2))  )
print(' 3  | ------------------ |' + ' ' + str(slo.get(3))  )
print(' 4  | ------------------ |' + ' ' + str(slo.get(4))  )
print(' 5  | ------------------ |' + ' ' + str(slo.get(5))  )
print(' 6  | ------------------ |' + ' ' + str(slo.get(6))  )
print(' 7  | ------------------ |' + ' ' + str(slo.get(7))  )
print(' 8  | ------------------ |' + ' ' + str(slo.get(8))  )
print(' 9  | ------------------ |' + ' ' + str(slo.get(9))  )
print('10  | ------------------ |' + ' ' + str(slo.get(10)) )
print('11  | ------------------ |' + ' ' + str(slo.get(11)) )
print('12  | ------------------ |' + ' ' + str(slo.get(12)) )
print('13  | ------------------ |' + ' ' + str(slo.get(13)) )
print('14  | ------------------ |' + ' ' + str(slo.get(14)) )
print('15  | ------------------ |' + ' ' + str(slo.get(15)) )
print('16  | ------------------ |' + ' ' + str(slo.get(16)) )

print( '=' *100 )