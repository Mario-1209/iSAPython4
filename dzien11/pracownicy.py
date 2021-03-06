from dzien11.pracownik import Pracownik

prac1 = Pracownik("John", "Travolta", 50000)
print(prac1)

prac2 = Pracownik("John", "Turturo", 30000)
print(prac2)

prac3 = Pracownik("John", "Rambo", 90000)
print(prac3)

# poprzez instancję mogę sprawdzić wartość pola klasy
print(prac1.ilosc_pracownikow)
print(prac2.ilosc_pracownikow)
print(prac3.ilosc_pracownikow)

print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

# przypisanie wartości do pola, które wzięliśmy przez instancję
# utworzy w tym obiekcie taką zmienną instancji, która będzie
# przechowywac indywidualną wartość dla tego obiektu
prac1.roczna_podwyzka = 15
print("\nDaje podwyzke prac1")
print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

Pracownik.roczna_podwyzka = 10
print("\nDaje podwyzke wszystkim")
print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

# del usuwa nam obiekty
del prac1.roczna_podwyzka

print("\nUsuwam podwyzke prac1")
print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)
