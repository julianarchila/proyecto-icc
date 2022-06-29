def main(name=None):
    if name is None:
        name = input("Name: ")
    print(f"""Hola {name}, tenemos los siguientes juegos disponibles:
    [1] Agario, [2] Pong, [3] 2048""")
    num = input("Ingrese el numero del juego: ")
    if num == "1":
        from agario import main as agario_main
        agario_main(name)

    elif num == "2":
        from pong import main as pong_main
        pong_main()

    elif num == "3":
        from dosmil_curenta_y_ocho import main as dosmil_main
        dosmil_main()

    else:
        print("Ingrese un numero valido")
        main(name)

if __name__ == "__main__":
    main()