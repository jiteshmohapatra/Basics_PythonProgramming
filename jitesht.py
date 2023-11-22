from turtle import *
bgcolor('black')
color('red')

def curve():
    for i in range(200):
         right(1)
         forward(1)
begin_fill()
left(140)
forward(120)
curve()
left(125)
curve()
forward(120)
end_fill()
hideturtle()
up()
goto(0,80)
color('white')
write('JITESH',align='center',font=('Hearts (BRK)',40,'bold'))
done()