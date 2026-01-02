class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Rectangle_area(self):
        area=self.length*self.width
        return area
newrectangle=Rectangle(200,150)
print("Rectangle Area Is: ",newrectangle.Rectangle_area())