ma_may = input("Nhap ma may: ")
print(type(ma_may))
cong_suat_W = input("Nhap cong suat (W): ")
print(type(cong_suat_W))
so_phut_su_dung = input("Nhap so phut su dung: ")
print(type(so_phut_su_dung))
don_gia_dien = input("Nhap don gia dien (kWh): ")
print(type(don_gia_dien))
# chuyen kieu du lieu
cong_suat_W = float(input("Nhap cong suat (W): "))
so_phut_su_dung = int(input("Nhap so phut su dung: "))
don_gia_dien = float(input("Nhap don gia dien (kWh): "))
dien_nang_kwh = (cong_suat_W * so_phut_su_dung) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_dien
print("Dien nang tieu thu: ", dien_nang_kwh, "kWh")
print("Chi phi: ", chi_phi, "VND")