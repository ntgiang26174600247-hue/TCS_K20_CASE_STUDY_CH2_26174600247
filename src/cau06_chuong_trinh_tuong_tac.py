ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat = float(input("Nhap cong suat (W): "))
so_phut_su_dung = float(input("Nhap so phut su dung: "))
don_gia_dien = float(input("Nhap don gia dien (kWh): "))
dien_nang_kwh = (cong_suat * so_phut_su_dung) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_dien
print("Ma phien: ", ma_phien)
print("May: ", ma_may)
print("Dien nang: ", dien_nang_kwh, "kWh")
print("Chi phi: ", chi_phi, "VND")