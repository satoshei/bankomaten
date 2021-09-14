#LOOP OCH LISTS LABBAR V2


'''
lst = []
num = 4

for n in range(num):
    numbers = int(input("Skriv in tal: "))
    lst.append(numbers)

print("Största talet i listan är :", max(lst), "\nMinsta talet i listan är:", min(lst))
'''

#Summera alla tal i en lista
'''
lst = [12,1231,515,61]
sumOfList = sum(lst)
print(sumOfList)
'''

#Hitta det största nummret i en lista
'''
lst = [1123,451,5124214,51521]
print(max(lst))
'''

#Räkna där en sträng längd är 2 eller mer och den första och andra bokstaven är samma från en vald lista.
'''
def sampleList(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

print(sampleList(["abc", "xyz", "aba", "1221"]))
'''

#Ta bort dubbletter från lista
'''
lst = ["ada", "ada", "12123", "1233", "hej"]
lst = list(dict.fromkeys(lst))
print(lst)
'''

#Skriv ett Python -program för att hitta listan med ord som är längre än n från en given ordlista.
'''
lst = ["Hejsansvejsan", "Jahop", "Ord"]
n = ["Svacke", "Tja", "Arab"]

for words in lst:
    if len(words) > len(n):
        print("The lenght of words in the list is larger than the n list:", words)
    elif len(words) < len(n):
        print("The lenght of words in the list (n) is bigger the the other list:", n)
'''

