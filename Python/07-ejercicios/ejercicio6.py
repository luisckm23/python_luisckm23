"""
Mostrar las tablas de multiplicar del 1 al 10

"""

for cabezera in range (1, 11):
    print("\n# # # # # # # # # # # # #")
    print(f"Tablas del {cabezera}")
    print("# # # # # # # # # # # # #")

    for numero in range (1, 11):
        print(f"{numero } x {cabezera} = {numero * cabezera}")
