
from bbai11 import Point
import math
class LineSegment:
    def __init__(self, *args):
        self.__d1 = None
        self.__d2 = None
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4 and all(isinstance(item, int) for item in args):
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = Point(args[0].getD1().getX(), args[0].getD1().getY())
            self.__d2 = Point(args[0].getD2().getX(), args[0].getD2().getY())
        else:
            raise TypeError("Đối số không hợp lệ")

    def getD1(self):
        return self.__d1
    
    def getD2(self):
        return self.__d2

    def read(self):
        try:
            s = input("Nhập x1 y1 x2 y2 (cách nhau bởi khoảng trắng): ")
            nums = s.split()
            if len(nums) != 4:
                raise ValueError("Vui lòng nhập đúng 4 số.")
            x1, y1, x2, y2 = map(int, nums)
            if not all(-50 <= x <= 100 for x in [x1, y1, x2, y2]):
                raise ValueError("Tọa độ phải trong khoảng [-50, 100].")
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)
        except (ValueError, IndexError):
            print("Input không hợp lệ, giữ nguyên giá trị cũ.")

    def __str__(self):
        return "[({}, {}); ({}, {})]".format(self.__d1.getX(), self.__d1.getY(), self.__d2.getX(), self.__d2.getY())

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        dy = self.__d2.getY() - self.__d1.getY()
        dx = self.__d2.getX() - self.__d1.getX()
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg) % 360

class LineSegmentTest:
    def testCase1(self):
        A = Point(2, 5)
        B = Point(20, 35)
        AB = LineSegment(A, B)
        print(AB)
        AB.move(35, 51)
        print(AB)
    
    def testCase2(self):
        CD = LineSegment()
        print("|CD| = {:.2f}".format(CD.length()))

    def testCase3(self):
        danhsach = []
        n = int(input("Nhập n: "))
        for i in range(n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)
        
        for item in danhsach:
            print(item)
            print(item.length())
        
        danhsach.sort(key=lambda dist: dist.length())
        for item in danhsach:
            print(item)
            print(item.length())

    def main(self):
        while True:
            s = input("Nhập kịch bản muốn chạy 1/2/3/exit: ")
            if s == '1':
                LineSegmentTest().testCase1()
            elif s == '2':
                LineSegmentTest().testCase2()
            elif s == '3':
                LineSegmentTest().testCase3()
            elif s == 'exit':
                break
LineSegmentTest().main()
