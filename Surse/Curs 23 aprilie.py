# print("Primul meu string. " * 2)
#
# print(2 + 2 * 2 - 2 / 1)
#
# a = "String"
# a += "String1"
# print(type(a))
#
# # concatenare cu format
# a = "String1"
# b = "String2"
# c = "{1} {0} {1}".format(a, b)
# c = f"{a} {b}"  # asta e cea mai buna
# print(c)
#
# a = 1
# b = 2
# c = a + b
# print(c)
#
# a = input("Primul nr: ")
# b = input("Al doilea nr:")
# while True:
#     euro = input("Valoare euro pentru convertire: ")
#     if euro.isdigit():
#         euro = int(euro)
#         print(euro)
#     elif "." in euro:
#         a = euro.split(".")
#         if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
#             newEuro = float(euro)
#             print(newEuro)
#             # newEuro = int(a[0]) + 10 ** -(len(a[1])) * int(a[1])
#     else:
#         print("Valoarea nu este un numar")
#
#     print("Valoarea convertita este:", euro * 4.87, " RON")


##Var 1
# while True:
#     euro = input("Valoare euro pentru convertire: ")
#     isok = False
#     if euro.isdigit():
#         euro = int(euro)
#         isok = True
#     elif "." in euro:
#         a = euro.split(".")
#         if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
#             euro = float(euro)
#             isok = True
#             # newEuro = int(a[0]) + 10 ** -(len(a[1])) * int(a[1])
#     else:
#         print("Valoarea nu este un numar")
#
#     if isok:
#         print("Valoarea convertita este:", euro * 4.87, " RON")
#


# ok = "1"
##Var 2
# while ok == "1":
#     print("1.Faceti conversie")
#     print("2.Iesiti din program")
#     ok = input()
#
#     if ok.isdigit() and int(ok) == 1:
#         euro = input("Valoare euro pentru convertire: ")
#         if len(euro) > 0:
#             floatSign = 1
#             if euro[0] == "-":
#                 floatSign = -1
#                 euro = euro[1:]
#             a = None
#             if euro.isdigit():
#                 euro = int(euro)
#             elif "." in euro and len(a := euro.split(".")) == 2 and a[0].isdigit() and a[1].isdigit():
#                 euro = float(euro)
#             else:
#                 print("Valoarea nu este un numar")
#                 continue
#             print("Valoarea convertita este:", floatSign * euro * 4.87, " RON")

str = "abecedar"
print(str[-1])
print(str[2::])

for poz, char in enumerate(str):
    print(poz, char)

for x in range(-1, 6, 2):
    print(x)

lista = list(range(10))
print(lista)