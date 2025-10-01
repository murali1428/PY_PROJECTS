class triangle:

    def __init__ (self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return 2*0.5*self.base+self.height

triangle_t=triangle(10,10)
print(triangle_t.base)
print(triangle_t.height)
print(triangle_t.perimeter())
print(triangle_t.area())
