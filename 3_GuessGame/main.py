# Your code here...
import random

flaga=False
liczbaDoZgadniecia=random.randint(1,100)
liczbaProb=0

while flaga ==False:
    zgaduj= int(input("Zgadnij liczbę z zakresu 1-100: "))
    liczbaProb+=1

    if zgaduj==liczbaDoZgadniecia:
        flaga ==True
        print("Gratulacje, zgadłeś. Poszukiwana liczba to: ", liczbaDoZgadniecia, "Udało się po tylu próbach: ", liczbaProb)
    else:
        if zgaduj>liczbaDoZgadniecia:
            print("Liczba za duża")
        else:
            print("Liczba za mała")

