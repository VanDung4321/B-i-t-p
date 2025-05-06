import json
from collections import Counter

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
        print("\n--- Nhập thông tin tủ lạnh ---")
        self.nhanhieu = input("Nhãn hiệu: ").strip()
        self.maso = input("Mã số: ").strip()
        self.nuocsx = input("Nước sản xuất: ").strip()
        self.tukdien = bool(int(input("Tủ kiểm điện (1: Có, 0: Không): ").strip()))
        self.dungtich = int(input("Dung tích (lít): ").strip())
        self.gia = int(input("Giá (VNĐ): ").strip())

    def hienThi(self):
        print(f"Nhãn hiệu: {self.nhanhieu}")
        print(f"Mã số: {self.maso}")
        print(f"Nước SX: {self.nuocsx}")
        print(f"T/K điện: {'Có' if self.tukdien else 'Không'}")
        print(f"Dung tích: {self.dungtich}L")
        print(f"Giá: {self.gia}VNĐ")
        print("==========")

    def layNhanHieu(self):
        return self.nhanhieu

    def layGia(self):
        return self.gia

    def soNguoiSD(self):
        return int(self.dungtich / 100)

    def cungNhanHieu(self, tl):
        return self.nhanhieu == tl.nhanhieu

    def nhHon(self, tl):
        return self.dungtich > tl.dungtich

def testCase1():
    print("\n--- Kịch bản 1: Hiển thị thông tin cố định của 2 tủ lạnh ---")
    tl1 = TuLanh()
    tl1.hamXayDungMacNghiem()

    tl2 = TuLanh()
    tl2.nhanhieu = "LG"
    tl2.maso = "LG-28382"
    tl2.nuocsx = "Hàn Quốc"
    tl2.tukdien = True
    tl2.dungtich = 600
    tl2.gia = 43000000

    tl3 = TuLanh()
    tl3.makeCopy(tl1)

    print("\nKết quả:")
    print("==========")
    tl2.hienThi()
    tl3.hienThi()

def testCase2():
    print("\n--- Kịch bản 2: Nhập và hiển thị danh sách tủ lạnh ---")
    n = int(input("Số lượng tủ lạnh cần nhập: "))
    danh_sach = []

    for i in range(n):
        print(f"\nNhập thông tin tủ lạnh thứ {i + 1}:")
        tl = TuLanh()
        tl.nhapThongTin()
        danh_sach.append(tl)

    print("\nDanh sách tủ lạnh:")
    print("==========")
    for tl in danh_sach:
        tl.hienThi()

def testCase3():
    print("\n--- Kịch bản 3: Nhập và hiển thị danh sách tủ lạnh (sắp xếp theo giá giảm dần) ---")
    n = int(input("Số lượng tủ lạnh cần nhập: "))
    danh_sach = []

    for i in range(n):
        print(f"\nNhập thông tin tủ lạnh thứ {i + 1}:")
        tl = TuLanh()
        tl.nhapThongTin()
        danh_sach.append(tl)

    danh_sach.sort(key=lambda x: x.layGia(), reverse=True)

    print("\nDanh sách tủ lạnh (sắp xếp theo giá giảm dần):")
    print("==========")
    for tl in danh_sach:
        tl.hienThi()

def testCase4():
    print("\n--- Kịch bản 4: Nhập và lưu danh sách tủ lạnh vào file DsTuLanh.json ---")
    n = int(input("Số lượng tủ lạnh cần nhập: "))
    danh_sach = []

    for i in range(n):
        print(f"\nNhập thông tin tủ lạnh thứ {i + 1}:")
        tl = TuLanh()
        tl.nhapThongTin()
        danh_sach.append({
            "nhanhieu": tl.nhanhieu,
            "maso": tl.maso,
            "nuocsx": tl.nuocsx,
            "tukdien": tl.tukdien,
            "dungtich": tl.dungtich,
            "gia": tl.gia
        })

    with open("DsTuLanh.json", "w", encoding="utf-8") as f:
        json.dump(danh_sach, f, ensure_ascii=False, indent=4)
    print("\nĐã lưu danh sách vào file DsTuLanh.json")

def testCase5():
    print("\n--- Kịch bản 5: Nhập và thống kê số lượng tủ lạnh theo nhãn hiệu ---")
    n = int(input("Số lượng tủ lạnh cần nhập: "))
    danh_sach = []

    for i in range(n):
        print(f"\nNhập thông tin tủ lạnh thứ {i + 1}:")
        tl = TuLanh()
        tl.nhapThongTin()
        danh_sach.append(tl)

    nhan_hieu_count = Counter(tl.layNhanHieu() for tl in danh_sach)
    
    nhan_hieu_sorted = sorted(nhan_hieu_count.items(), key=lambda x: x[0])

    print("\nThống kê số lượng tủ lạnh theo nhãn hiệu:")
    print("==========")
    for nhan_hieu, count in nhan_hieu_sorted:
        print(f"{nhan_hieu} ({count})")

def main():
    while True:        
        choice = input("Nhập kịch bản muốn chạy 1/2/3/4/5/exit: ")

        if choice == "0":
            print("Đã thoát chương trình.")
            break
        elif choice == "1":
            testCase1()
        elif choice == "2":
            testCase2()
        elif choice == "3":
            testCase3()
        elif choice == "4":
            testCase4()
        elif choice == "5":
            testCase5()
        elif choice == "exit":
            print("Thoát chương trình")
            break   
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

if __name__ == "__main__":
    main()
