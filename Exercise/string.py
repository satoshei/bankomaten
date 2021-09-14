#STRINGS LABBAR V2

#Be användaren mata in 3 strängar. Addera ihop strängarna och skriv ut alla tre strängarna på skärmen
'''
while True:

    try:
        str1 = str(input("Mata in första strängen: "))
        str2 = str(input("Mata in den andra strängen: "))
        str3 = str(input("Mata in den sista strängen: "))

        x = str1 + str2+ str3
        print(x)
    except Exception():
        str1,str2,str3 == str
        print("Mata in en sträng, int eller floats är inte valbart")
        input("Testa igen genom att trycka på enter")
'''
#Du har en strängvariabel som innehåller följande text, ”Hello, world”
#Ta med hjälp av kod ut första förekomsten av bokstaven w
#Skriv ut vilken position bokstaven w har i strängen (H har position 0). Ta fram positionen genom kod
'''
var = "Hello, world"
print(var[-5])
'''
#Du har strängen string namn="kurt andersson";
#Skriv kod så att förnamn och efternamn i variabeln namn börjar med stora bokstäver.
#Resultatet skall bli så här "Kurt Andersson"
'''
namn = "kurt andersson"
lst = [word[0].upper() + word[1:] for word in namn.split()]
namn = " ".join(lst)
print(namn)
'''

var = "Detta är en sträng som du skall ändra"
