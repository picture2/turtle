import turtle

t = turtle.Turtle()
t.shape("turtle")

def makeDoH(g):
   for i in range(g):
       t.forward(100)
       t.left(360/n)


def square(sqs):
    for i in range(4):
        t.forward(sqs)
        t.left(90)

def penupdown(mva, down):
    for i in range(1):
        t.up()
        t.goto(mva, 0)
        t.down()

        
n = (int(input("어떤도형으로 만드실건가요?")))
sqs = int(input("얼마나 크게 그리실 건가요?"))
mva = int(input("얼마나 움직이실건가요?"))
mva2 = int(input("얼마나 움직이실건가요?"))
mva3 = int(input("얼마나 움직이실건가요?"))
down = 0

square(sqs)
penupdown(mva, down)
square(sqs)
penupdown(mva2, down)
square(sqs)
penupdown(mva3, down)
makeDoH(n)
