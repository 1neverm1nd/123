
class First:
    color = "red"
    
    def out(self):
        print(self.color + "!")
        
class Second:
    color = "red"
    form = "circle"
    
    def changecolor(self, newcolor):
        self.color = newcolor
    
    def changeform(self, newform):
        self.form = newform

# Creating objects
obj1 = Second()
obj2 = Second()

# Initial values output
print(obj1.color, obj1.form)  # "red circle"
print(obj2.color, obj2.form)  # "red circle"

# Changing object properties
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")

# Output updated values
print(obj1.color, obj1.form)  # "green circle"
print(obj2.color, obj2.form)  # "blue oval"

# Creating third object and changing all its properties
obj3 = Second()
obj3.changecolor("yellow")
obj3.changeform("square")
print(obj3.color, obj3.form)  # "yellow square"
