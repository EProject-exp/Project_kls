"""listNumra = [5, 3, 8, 6, 7]
print("Lista: ", listNumra)

listNumra.sort()
print("Sorted: ", listNumra)"""

"""listqytet = ["Tiran", "Durres", "Vlore", "Fier", "Korce"]

print("Qytetet -:", listqytet)

listqytet.sort()

print("Qytet renditur -:", listqytet)"""


"""listanr = [4, 9, 20, 7, 8, 10, 15, 32, 5, 44]

listanr.sort()
print("Max min", listanr[0], listanr[-1])"""


def mesatarja(listaa):
    total = sum(listaa)
    madh_list = len(listaa)
    mesat = total / madh_list
    print(f"Mesatarja esht: {mesat}")

mesatarja([4, 9, 8, 7, 10, 43])
