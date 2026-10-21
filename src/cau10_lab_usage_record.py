ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_thiet_bi = float(input("Nhap cong suat thiet bi (W): "))
thoi_gian_su_dung = float(input("Nhap thoi gian su dung (phut): "))
don_gia_dien = float(input("Nhap don gia dien (VND/kWh): "))
dien_nang_kwh = (cong_suat_thiet_bi * thoi_gian_su_dung) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_dien
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
tren_60_phut = 60
print("Ma phien: ", ma_phien)
print("Ma may: ", ma_may)
print(f"Cong suat:  {cong_suat_thiet_bi:.2f} W")
print("Thoi luong: ", thoi_gian_su_dung, "phut")
print(f"Dien nang:  {dien_nang_kwh:.3f} kWh")
print(f"Chi phi:  {chi_phi:.2f} VND")
print("Tren 60 phut: ", thoi_gian_su_dung > tren_60_phut)
print("Ghi nhan luc: ", thoi_diem_text)
