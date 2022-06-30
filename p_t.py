def main():
    import random

    opciones = ["Piedra", "Papel", "Tijeras"]
    n = 0

    def Random(n):
        comp_elec = random.randint(0,2)
        computador = opciones[comp_elec]
        
        return computador

    def Juego(n):
        jugador = int(input("Para Piedra escriba 0, para Papel 1, para Tijeras 2 "))
        while jugador > 2:
            print("Digite un valor válido")
            jugador = int(input("Para Piedra escriba 0, para Papel 1, para Tijeras 2 "))
        while jugador < 0:
            print("Digite un valor válido")
            jugador = int(input("Para Piedra escriba 0, para Papel 1, para Tijeras 2 "))
            
        elec_jug = opciones[jugador]
        print("Usted escogió ", elec_jug)
        
        return  elec_jug
        
    elec_jug = Juego(n)
    computador = Random(n)

    def Elección(elec_jug, computador):
        if (elec_jug == "Piedra"):
            if (computador == "Tijeras"):
                print("El computador escogió ", computador)
                print("Ganó")
            if (computador == "Papel"):
                print("El computador escogió ", computador)
                print("Perdió")
            if (computador == "Piedra"):
                print("El computador escogió ", computador)
                print("Empate")
            
        if (elec_jug == "Tijeras"):
            if (computador == "Tijeras"):
                print("El computador escogió ", computador)
                print("Empate")
            if (computador == "Papel"):
                print("El computador escogió ", computador)
                print("Ganó")
            if (computador == "Piedra"):
                print("El computador escogió ", computador)
                print("Perdió")
                
        if (elec_jug == "Papel"):
            if (computador == "Tijeras"):
                print("El computador escogió ", computador)
                print("Perdió")
            if (computador == "Papel"):
                print("El computador escogió ", computador)
                print("Empate")
            if (computador == "Piedra"):
                print("El computador escogió ", computador)
                print("Ganó")
                
    Elección(elec_jug, computador)




