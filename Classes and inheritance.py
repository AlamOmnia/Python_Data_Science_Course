class Shape:
    def __init__(self,name):
        self.name=name
    def printName(self):
        return "Shap name:",self.name
    def areaCalculation(self):
        return "Super class"
        
class Circle(Shape):
    def  __init__(self,name,radious):
        super().__init__(name)
        self.radious=radious
  #  def printName(self):
   #     return super().printName()
    def areaCalculation(self):
        area=3.1416*self.radious*self.radious
        return area

class Rectangle(Shape):
    def  __init__(self,name,length, width):
        super().__init__(name)
        self.width=width
        self.length=length
  #  def printName(self):
     #   return super().printName()
    def areaCalculation(self):
        return self.length*self.width

circle1=Circle("Circle",2)
rect=Rectangle("Rectangle",2,3)

print(circle1.printName(),"Circle Area: ",circle1.areaCalculation())
print(rect.printName(),"Circle Area: ",rect.areaCalculation())
#print("Rectangle Area: ",rect.areaCalculation())
