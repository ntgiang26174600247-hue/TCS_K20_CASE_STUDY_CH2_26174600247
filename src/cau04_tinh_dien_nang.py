cong_suat_w = 250
so_phut = 60
don_gia_kwh = 3000
dien_nang_kwh = (cong_suat_w * so_phut) / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu: ", dien_nang_kwh, "kWh")
print("Chi phi dien nang: ", chi_phi, "VND")
print(type(dien_nang_kwh))
print(type(chi_phi))

# du doan:
# Dien nang tieu thu: 0.375
# Chi phi dien nang: 1125.0 VND
# <class 'float'>
# <class 'float'>
# sau khi thay doi so phut = 60, thi ket qua dien nang va chi phi thay doi, it hon khi so phut = 90