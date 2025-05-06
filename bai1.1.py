import math
class Point:
    __x = int
    __y = int
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        try:
            tmp = input("Nhập vào x, y: ")
            nums = tmp.split()
            if len(nums) != 2:
                raise ValueError("Vui lòng nhập đúng 2 số.")
            self.__x = int(nums[0])
            self.__y = int(nums[1])
        except (ValueError, IndexError):
            print("Input không hợp lệ, giữ nguyên giá trị cũ.")
    
    def __str__(self):
        return f"({self.__x}, {self.__y})\n"
    def move(self, dx=0, dy=0):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self, *args):
        if len(args)==0:
            return math.sqrt(self.__x**2 + self.__y**2)
        if len(args)==1 and isinstance(args[0], Point):
            return math.sqrt((self.__x-args[0].__x)**2 + (self.__y-args[0].__y)**2)


p1 = Point()
print("p1:", p1)  # (0, 1)
# Tính khoảng cách từ p1 đến gốc (0, 0)
print("Khoảng cách từ p1 đến gốc:", p1.distance())
p2 = Point(-50, 100)
print("p2:", p2)  # (-50, 100)
# Tính khoảng cách từ p2 đến gốc (0, 0)
print("Khoảng cách từ p2 đến gốc:", p2.distance())
# Tính khoảng cách giữa p1 và p2
print("Khoảng cách giữa p1 và p2:", p1.distance(p2))
