class Fruit:
    name="apple"
    color="red"

print(Fruit.name)  # calling by dot(.)class substitution
print(Fruit.color)


class fruit:
    def __init__ (self,name,color):
        self.name=name
        self.color=color

fruit_1=fruit(name="apple",color="red")
fruit_2=fruit(name="mango",color="yellow")
fruit_3=fruit(name="banana",color="yellow")

print(fruit_1.name,fruit_1.color)
print(fruit_2.name,fruit_2.color)
print(fruit_3.name,fruit_3.color)


