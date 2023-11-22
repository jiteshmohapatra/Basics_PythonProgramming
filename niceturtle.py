'''import turtle as tur
import colorsys as cs
tur.setup(500,500)
tur.speed(10)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
        tur.hideturtle()
        tur.done()'''
from turtle import *
import colorsys
bgcolor('black')
tracer(500)
def draw():
    h =0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt (98)
        circle(i, 5)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2)
        end_fill()
draw()
done()
