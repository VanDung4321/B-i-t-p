from bai31 import Point, ColorPoint

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")  # Use constructor directly
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
        C = ColorPoint(6, 3, "đen")  # Use constructor directly
        D = ColorPoint(cp=C)         # Use copy constructor
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
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng nhập 1, 2, 3 hoặc exit.")

if __name__ == "__main__":
    C002454.main()
