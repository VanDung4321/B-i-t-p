import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        x, y = map(int, input().split())
        if -50 <= x <= 100 and -50 <= y <= 100:
            self.__x = x
            self.__y = y
        else:
            raise ValueError("x và y nằm trong khoảng từ -50 đến 100")
    
    def print(self):
        print(f"({self.__x}, {self.__y})", end="")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)

class ColorPoint(Point):
    def __init__(self, x=None, y=None, color=None, cp=None):
        if cp is not None and isinstance(cp, ColorPoint):
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.color
        elif x is not None and y is not None and color is not None:
            super().__init__(x, y)
            self.__color = color
        else:
            super().__init__()
            self.__color = "xanh"
    
    def read(self):
        super().read()
        parts = input().strip().split(maxsplit=1)
        self.__color = parts[0] if parts else "xanh"
    
    def print(self):
        super().print()
        print(f": {self.__color}")
    
    def setColor(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

if __name__ == "__main__":
    T = ColorPoint()
    T.print()  # (0, 1): xanh

    c = ColorPoint()
    print("color: " + c.color)  # color: xanh

    c = ColorPoint(5, 10, "cyan")
    print("x: " + str(c.getX()))  #  x: 5
    print("y: " + str(c.getY()))  #  y: 10
    print("color: " + c.color)    # color: cyan

    c = ColorPoint()
    c.setXY(5, 7)
    c.color = "white"
    c.print()  # (5, 7): white
