def main():
    import turtle
    import time
    import random

    refresh = 0.1

    #marcador0
    Score = 0
    Mejor_puntuacion = 0

    wn = turtle.Screen()
    wn.title("Snake")
    wn.bgcolor("blue")
    wn.setup(width = 600, height = 600)
    wn.tracer(0)

    #Cabeza snake
    cabeza = turtle.Turtle()
    cabeza.speed(0)
    cabeza.color("black")
    cabeza.shape("square")
    cabeza.penup()
    cabeza.goto(0,0)
    cabeza.direction = "stop"

    #comida
    comida = turtle.Turtle()
    comida.speed(0)
    comida.color("red")
    comida.shape("circle")
    comida.penup()
    comida.goto(0,0)
    comida.direction = "stop"

    #cuerpo
    cuerpo_nuevo = []

    #Texto
    texto = turtle.Turtle()
    texto.speed(0)
    texto.color("white")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,260)
    texto.write("Puntuación: 0     Mejor puntuación: 0", align = "center", font =("Courier", 10, "normal"))



    #Funciones
    def arriba():
        cabeza.direction = "up"
    def abajo():
        cabeza.direction = "down"
    def izquierda():
        cabeza.direction = "left"
    def derecha():
        cabeza.direction = "right"

    def mov():
        if cabeza.direction == "up":
            y = cabeza.ycor()
            cabeza.sety(y + 20)
        if cabeza.direction == "down":
            y = cabeza.ycor()
            cabeza.sety(y - 20)
        if cabeza.direction == "left":
            x = cabeza.xcor()
            cabeza.setx(x - 20)
        if cabeza.direction == "right":
            x = cabeza.xcor()
            cabeza.setx(x + 20)
    #teclado
    wn.listen()
    wn.onkeypress(arriba, "Up")
    wn.onkeypress(abajo, "Down")
    wn.onkeypress(izquierda, "Left")
    wn.onkeypress(derecha, "Right")
            
    while True:
        wn.update()
        
        #colision borde
        if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 280 or cabeza.ycor()< -290:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #eliminar cuerpo
            for segmento in cuerpo_nuevo:
                segmento.goto(1000,1000)
                
            #clean
            cuerpo_nuevo.clear()
            
            #reset marcador
            Score = 0
            texto.clear()    
            texto.write("Puntuación: {}     Mejor puntuación: {}".format(Score, Mejor_puntuacion),
                        align = "center", font =("Courier", 10, "normal"))
            
            
        #comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            comida.goto(x,y)
        
            cuerpo = turtle.Turtle()
            cuerpo.speed(0)
            cuerpo.color("grey")
            cuerpo.shape("square")
            cuerpo.penup()
            cuerpo_nuevo.append(cuerpo)
        
            #Aumento marcador
            Score += 10
            if Score > Mejor_puntuacion:
                Mejor_puntuacion = Score
            
            texto.clear()    
            texto.write("Puntuación: {}     Mejor puntuación: {}".format(Score, Mejor_puntuacion),
            align = "center", font =("Courier", 10, "normal"))
            
        totalSeg = len(cuerpo_nuevo)
        for index in range(totalSeg -1, 0 ,-1):
            x = cuerpo_nuevo[index - 1].xcor()
            y = cuerpo_nuevo[index - 1].ycor()
            cuerpo_nuevo[index].goto(x,y)
            
        if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo_nuevo[0].goto(x,y)

        mov()
        
        #colision cuerpo
        for segmento in cuerpo_nuevo:
            if segmento.distance(cabeza) < 20:
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
                
                #esconder
                #eliminar cuerpo
                for segmento in cuerpo_nuevo:
                    segmento.goto(1000,1000)
                cuerpo_nuevo.clear()
                #reset marcador
                Score = 0
                texto.clear()    
                texto.write("Puntuación: {}     Mejor puntuación: {}".format(Score, Mejor_puntuacion),
                            align = "center", font =("Courier", 10, "normal"))
        time.sleep(refresh)