# Python tahák
Autor: Ladislav Jaromír Pleštil<br>
Licence: MIT Licence

## Obsah
- __Výstup__
- __Komentáře__
- __Proměnné__
- __Datové typy__
- __Aritmetické operace__
- __Podmínky a logické operace__
- __Cykly__
- __Funkce__
- __Práce s textem__
- __Vstup__

## Aritmetické operace
V kódu níže naleznete jak se provádí aritmetické operace v Pythonu.
```python
1 + 1  # Sčítání
2 - 1  # Odčítání
2 * 3  # Násobení
6 / 2  # Dělení
5 % 3  # Zbytek po dělení
3 ** 2 # Umocňování
```

## Cykly
V Pythonu máme různé cykly.
### While
Cyklus while dělá to, že se bude daný kód opakovat, dokud je podmínka platná.
```python
while x <= y:
    print("Apple")
```
V tomto příkladu se bude vypisovat slovo Apple do té doby, dokud bude x menší nebo rovno y. Samozřejmě musíme použít odsazení.<br>
Pomocí while můžeme také opakovat nějaký kód do nekonečna. To můžeme udělat pomocí while True:
```python
while True:
    print("Apple")
```
V tomto příkladu se slovo Apple bude vypisovat do nekonečna (dokud program ručně neukončíte)
### For
Cyklus for se používá ve dvou případech.<br>
```python
for i in range(0, 3, 1):
    print("Raspberry")
```
V tomto příkladu je cyklus for použit k tomu, aby se kód opakoval daný počet kol. Do range jako první vložíme na jakém čísle chceme začínat (v tomto případě 0, je to také výchozí hodnota), jako druhé na jakém čísle chceme končit (v tomto případě 3, tuto hodnotu vždy musíme zadat), a o kolik chceme postupovat (v tomto případě 1, je to výchozí hodnota). V praxi se nám slovo Raspberry vypíše 3x.<br>
Tento cyklus můžeme zjednodušit takto:
```python
for i in range(3):
    print("Raspberry")
```
Hodnota na jakém čísle chceme začínat a o kolik chceme postupovat je nepovinná. Pokud jí nezadáte, použíjí se výchozí hodnoty.<br><br>
```python
fruits = ["Raspberry", "Orange", "Apple"]
for x in fruits:
    print(x)
```
V tomto příkladě je použito druhé využití cyklu for. Cyklus for takto vypíše postupně každou hodnotu v poli fruits. x v tomto cyklu je v prvním kole první hodnota v poli fruits, v druhém kole druhá hodnota..., a tento cyklus se opakuje tak dlouho, dokud se nedojde až k poslední hodnotě. Použití vychází i z překladu do češtiny pro x ve fruits. Za in zadáváme název pole, za for zadáváme jméno proměnné, která bude obsahovat danou hodnotu z pole.
### Prohlášení break
S prohlášením break můžeme zastavit opakování cyklu i před tím, než je cyklus dokončen.
```python
fruits = ["Raspberry", "Orange", "Apple"]
for x in fruits:
    if x == "Orange":
        break
    print(x)
```
V tomto příkladu se stane to, že se budou vypisovat hodnoty z pole fruits a pokud se dojde k hodnotě Orange, vypisování se zastaví.
### Prohlášení continue
S prohlášením continue můžeme přeskočit kolo cyklu a přesunout se na další.
```python
fruits = ["Raspberry", "Orange", "Apple"]
for x in fruits:
    if x == "Orange":
        continue
    print(x)
```
V tomto příkladu se stane to, že se budou vypisovat hodnoty z pole fruits a pokud se dojde k hodnotě Orange, kolo se přeskočí a Orange se nevypíše.

## Datové typy
```python
a = 5  # Int
pi = 3.14  # Float
name = "Ladislav" # String
isMale = True  # Boolean
array = ["banana", 3, False]  # Array
person = {  # Dictionary
    "name": "Karel",
    "surname": "Novák",
    "age": 40,
    "gender": True
}
```
V kódu výše jsou uvedeny důležité datové typy.<br><br>
**Int:** Datový typ, který obsahuje celá čísla.<br><br>
**Float:** Datový typ, který obsahuje čísla s plovoucí desetinnou čárkou.<br><br>
**String:** Datový typ, který obsahuje text. Text se píše do uvozovek jako v příkladovém kódu.<br><br>
**Boolean:** Datový typ, který obsahuje pouze hodnoty True nebo False (Pravda/Nepravda). Počáteční písmeno hodnoty je vždy velké.<br><br>
**Array (pole):** Datový typ, který obsahuje několik hodnot pod jedním jménem. Můžeme do něj ukládat čísla, text a další hodnoty. Do array se můžou hodnoty při průběhu programu vkládat a mazat. Hodnoty se píší do hranatých závorek, oddělují se čárkou. Při zapisování jednotlivých hodnot dodržujeme pravidla pro zapisování daného datového typu. Jednotlivé hodnoty můžeme zavolat pomocí jmenoPromenne[index], kde jmenoArray je název proměnné (v příkladovém kódu je to array), a index je na jakém místě je hodnota obsažena. První hodnota je 0, druhá je 1 atd. V příkladovém kódu by jsme zavolali hodnotu "banana" pomocí array[0], protože je banana první hodnota v array.<br><br>
**Dictionary (slovník):** Datový typ, do kterého můžeme ukládat data do páru klíč:hodnota. V příkladovém kódu pokud by jsme chtěli zavolat name v slovníku person, udělali by jsme to podobně jako v poli pomocí person["name"], kde person je název proměnné (slovníku) a "name" je klíč. Za každou uloženou hodnotu musíme dát čárku, pokud chceme uložit další. Při zadávání hodnot se řídíme pravidly pro zadávání daného datového typu.<br>

### Funkce type()
Funkce type() můžeme použít k tomu aby jsme zjistili datový typ dané hodnoty/proměnné.
```python
print(type(3))
```
V tomto příkladovém kódu chceme vypsat datový typ hodnoty 3. Níže je to co nám program vypíše.
```
<class 'int'>
```
Jelikož 3 je celé číslo, datový typ této hodnoty je int.<br>
Níže naleznete jak se nazývají dané datové typy v Pythonu.<br>
```
Int - int
Float - float
String - str
Boolean - bool
Array - list
Dictionary - dict
```
Vpravo je název daného datového typu v Pythonu.

## Funkce
V Pythonu můžeme vytvářet funkce. Funkce je blok kódu, který běží pouze pokud je zavolán.  To se může hodit v programech kde se v hodně částech kódu provádí ten stejný kód, akorát s jinými hodnotami.
```python
def odmocnina(n, exponent):
    return n ** 1 / exponent
print(odmocnina(27, 3))
```
V tomto příkladu jsme definovali funkci na odmocninu. Funkci definujeme pomocí def, odmocnina je název funkce a n a exponent jsou argumenty funkce, se kterými můžeme ve funkci pracovat. Return slouží k vrácení nějaké hodnoty, např. v tomto případě vracíme odmocninu nějakého čísla.<br>
Argumenty funkce slouží k tomu, aby jsme do funkce mohli vložit nějaký vstup (proměnnou, hodnotu atd.). V příkladu máme dva argumenty: n a exponent. n je číslo které chceme odmocnit, exponent je logicky exponent.<br>
V příkladovém kódu se tedy stane to, že chceme vypsat výsledek funkce odmocnina, kde do argumentu n vkládáme číslo 27 a do argumentu exponent vkládáme 3. S těmito argumenty se ve funkci může pracovat. V tomto případě provedeme odmocninu a vrátíme její výsledek který funkce print vypíše.

## Komentáře
V pythonu můžeme komentovat kód, aby jsme se v něm dobře vyznali. Níže je příklad komentáře
```python
# Toto je komentář v Pythonu
```
Jak můžete vidět v příkladovém kódu výše, komentář se začíná hashtagem. Takto můžeme komentovat kdekoliv v kódu, a python tyto komentáře bude ignorovat.

## Podmínky a logické operace
V Pythonu existují různé podmínky a logické operace.
```python
if 5 == 5: # Zjišťujeme jestli se 5 rovná 5
    print("Hello World")
elif 5 != 5: # Pokud se 5 nerovná 5, zjistíme jestli se 5 nerovná 5
    print("Orange")
else: # Pokud ani jedna z podmínek není platná
    print("Apple")
```
V kódu výše je použita podmínka if, elif a else.<br><br>
If slouží k tomu, aby jsme zjistili pomocí porovnávání a logických operací jestli je nějaké tvrzení pravivé. Pokad ano, provede se daná operace. Zadáváme if podmínka: a příkazy zadáváme pod dvojtečku s odsazením. Python totiž závisí na odsazení.<br><br>
Elif slouží k tomu, když se podmínka nad ním nestane platnou, tak se přejde na elif a zkontroluje se, jestli podmínka na elif je platná. Pokud ano, provede se kód za elif. Takto můžete pod sebou použít více podmínek elif a testovat např. 3x jestli je podmínka platná. <br><br>
Else slouží k tomu, pokud ani jedna podmínka uvedená na if (případně elif) není platná, provede se kód za else.<br><br>
Níže jsou uvedeny porovnávací operace:
```
== (je rovno)
!= (není rovno)
> (větší než)
< (menší než)
>= (větší nebo rovno)
<= (menší nebo rovno)
```
V Pythonu máme také logické operace.
### And
```python
if 5 == 5 and 5 < 6:
    print("Watermelon")
```
Pokud použijeme operaci and, podmínka bude platná pouze v tu chvíli, pokud obě či více podmínek jsou platných.<br>
V příkladu se vypíše slovo Watermelon pouze, pokud 5 je rovno 5 a 5 je menší než 6. 
### Or
```python
if 5 == 5 or 6 == 4:
    print("Watermelon")
```
Pokud použijeme operaci or, podmínka bude platná pouze v tu chvíli, pokud jedna z podmínek bude platná.<br>
V příkladu se vypíše slovo Watermelon pouze, pokud 5 je rovno 5 nebo 6 je rovno 4.

## Práce s textem
Zde si uvedeme tři funkce: lower, upper a strip. Také si uvedeme formátovaní stringu pomocí F-string.
### Lower
Funkce lower slouží k tomu, aby přepsala text na malá písmena.
```python
message = "I LoVE yOu"
print(message.lower())
```
Když spustíme tento příkladový kód, vypíše se:
```
i love you
```
### Upper
Funkce upper slouží k tomu, aby přepsala text na velká písmena.
```python
message = "I LoVE yOu"
print(message.upper())
```
Když spustíme tento příkladový kód, vypíše se:
```
I LOVE YOU
```
### Strip
Funkce strip slouží k tomu, aby vám ze stringu odstranila přebytečné mezery.
```python
message = "          I love you      "
print(message.strip())
```
Když spustíme tento příkladový kód, z proměnné message se odstraní přebytečné mezery a vypíše se:
```
I love you
```
### F-String
F-string slouží k tomu, aby se dali formátovat různé části stringu. Uvedeme si to na příkladu.
```python
n = 1 + 1
print(f"Výsledek: {n}")
```
F-string vytvoříme tak, že před první uvozovku zadáme písmeno f. V F-stringu můžeme do složených závorek dávat názvy proměnných a také porovnávací operace, aritmetické operace a logické operace. U operací se vypíše její výsledek, u proměnné se vypíše její hodnota.<br>
Když by jsme spustili tento příkladový kód, vypíše se nám:
```
Výsledek: 2
```
Místo složených závorek se vypíše hodnota v proměnné uvedené v nich.

## Proměnné
Proměnná je kontejner pro ukládání datových hodnot. Každá proměnná má svůj datový typ.<br>
```python
a = 5
```
V kódu výše ukládáme hodnotu 5 do proměnné a, kde a je jméno proměnné a 5 je hodnota proměnné.

## Vstup
V Pythonu můžeme použít funkci input() k tomu, aby jsme získali vstup od uživatele. Vstup se ukládá vždy do hodnoty v datovém typu string. Uvedeme si tuto funkci na příkladu.
```python
name = input()
print(f"Vaše jméno: {name}")
```
V tomto příkladu se hned na začátku programu bude požadovat vstup od uživatele. Poté ho použijeme ve výpisu. Pokud by uživatel zadal John, výstup programu by vypadal takto.
```
Vaše jméno: John
```
Tento kód můžeme ještě vylepšit tím, že se uživateli když program bude vyžadovat vstup nezobrazí pouze prázdno, ale zobrazí se daný text za který se bude zadávat vstup. Tento text není součástí vstupu, je pouze pro lepší porozumění uživatele tomu co po něm program chce.
```python
name = input("Zadejte vaše jméno: ")
print(f"Vaše jméno: {name}")
```
Když program bude vyžadovat vstup, bude to vypadat takto:
```
Zadejte vaše jméno: 
```

## Výstup
Pomocí příkazu print() můžeme vypsat danou hodnotu
```python
print("Hello World")
```
Kód výše vypíše hodnotu Hello World.