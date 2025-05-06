from bai31 import Point, ColorPoint

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()
        print("Constructor: PASS")

    @staticmethod
    def testCase2():
        B = ColorPoint()
        B.read() 
        B.print()
        B.move(10, 8)
        B.print()
        print("Constructor: PASS")

    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "đen") 
        D = ColorPoint(cp=C)        
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()
        print("Set color: PASS")

    @staticmethod
    def main():
        while True:                       
            c = input("Nhập kịch bản muốn chạy 1/2/3/exit: ")           
            if c == '1':
                C002454.testCase1()
            elif c == '2':
                C002454.testCase2()
            elif c == '3':
                C002454.testCase3()
            elif c == 'exit':
                print("Out.")
                break
            else:
                print("Lựa chọn không hợp lệ ")

if __name__ == "__main__":
    C002454.main()
