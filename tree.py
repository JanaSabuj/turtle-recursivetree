import turtle
foo = turtle.Turtle()

#point the foo northward
foo.left(90)
foo.speed(100)

def tree(i):
	if i < 10:
		return
	else:
		foo.forward(i)
		foo.left(30)
		foo.color("green")
		tree(3*i/4)

		foo.right(60)
		foo.color("brown")
		tree(3*i/4)
		
		#return to original position
		foo.left(30)
		foo.backward(i)

#call the tree
tree(100)

# fix the canvas 
turtle.done()