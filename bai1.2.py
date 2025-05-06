from bbai11 import Point

class PointTest:
    def main(self):
        
        diemA = Point(3,4)
        print(diemA)

        diemB = Point()
        diemB.read()
        print(diemB)

        diemC = Point(-diemB.getX(), -diemB.getY())
        print("Tọa độ điểm C là :",diemC)
        print(diemB.distance())
        print(diemA.distance(diemB))

PointTest().main()
