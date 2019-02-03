import turtle
yo=turtle.Turtle()
def yoyo(s):
  for i in range(4):
    yo.speed(100)
    yo.fd(s)
    yo.right(90)
for j in range(100):
  yoyo(100)
  yo.right((j+1)*5)
yo.done()

