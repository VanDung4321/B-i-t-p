import pickle

class TuLanh:
    def __init__(self):
        self.nhanhieu = "Electrolux"  
        self.maso = "ETB2807-H"      
        self.nuocsx = "Việt Nam"      
        self.tukdien = True           
        self.dungtich = 256           
        self.gia = 7000000            

    def hamXayDungMacNghiem(self):
        self.nhanhieu = "Electrolux"
        self.maso = "UNKNOWN"
        self.nuocsx = "Việt Nam"
        self.tukdien = True
        self.dungtich = 256
        self.gia = 7000000

    def makeCopy(self, tl):
        self.nhanhieu = tl.nhanhieu
        self.maso = tl.maso
        self.nuocsx = tl.nuocsx
        self.tukdien = tl.tukdien
        self.dungtich = tl.dungtich
        self.gia = tl.gia

    def nhapThongTin(self):
        print("Nhập thông tin tủ lạnh:")
        self.nhanhieu = input("Nhãn hiệu: ")
        self.maso = input("Mã số: ")
        self.nuocsx = input("Nước sản xuất: ")
        self.tukdien = bool(int(input("Tủ kiểm điện (1: Có, 0: Không): ")))
        self.dungtich = int(input("Dung tích (lít): "))
        self.gia = int(input("Giá (VND): "))

    def hienThi(self):
        print("\nThông tin tủ lạnh:")
        print(f"Nhãn hiệu: {self.nhanhieu}")
        print(f"Mã số: {self.maso}")
        print(f"Nước SX: {self.nuocsx}")
        print(f"Tủ kiểm điện: {'Có' if self.tukdien else 'Không'}")
        print(f"Dung tích: {self.dungtich}")
        print(f"Giá: {self.gia}")

    def layNhanHieu(self):
        return self.nhanhieu

    def layGia(self):
        return self.gia

    def soNguoiSD(self):
        return int(self.dungtich / 100)

    def cungNhanHieu(self, tl):
        return self.nhanhieu == tl.nhanhieu

    def nhHon(self, tl):
        return True if self.dungtich > tl.dungtich else False

def main():
    tuLanh1 = TuLanh()
    print("Thông tin tủ lạnh mặc định:")
    tuLanh1.hienThi()

    tuLanh2 = TuLanh()
    tuLanh2.nhapThongTin()

    tuLanh3 = TuLanh()
    tuLanh3.makeCopy(tuLanh1)
    print("\nThông tin tủ lạnh 3 (sao chép từ tủ lạnh 1):")
    tuLanh3.hienThi()

    print("\nThông tin tủ lạnh 2 (nhập từ bàn phím):")
    tuLanh2.hienThi()

    print("\nKiểm tra nhãn hiệu:")
    if tuLanh1.cungNhanHieu(tuLanh2):
        print("Tủ lạnh 1 và tủ lạnh 2 có cùng nhãn hiệu.")
    else:
        print("Tủ lạnh 1 và tủ lạnh 2 không cùng nhãn hiệu.")

    print("\nKiểm tra dung tích:")
    if tuLanh1.nhHon(tuLanh2):
        print("Tủ lạnh 1 nhỉnh hơn tủ lạnh 2 về dung tích.")
    else:
        print("Tủ lạnh 1 không nhỉnh hơn tủ lạnh 2 về dung tích.")

    print(f"\nSố người sử dụng phù hợp với tủ lạnh 1: {tuLanh1.soNguoiSD()} người")

    with open("tuLanh1.dat", "wb") as file:
        pickle.dump(tuLanh1, file)
    print("\nĐã lưu thông tin tủ lạnh 1 vào file tuLanh1.dat")

if __name__ == "__main__":
    main()
