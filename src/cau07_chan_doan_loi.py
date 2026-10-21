ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = (cong_suat_w * so_phut) / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# ten tep: cau07_chan_doan_loi.py
# so dong: 6
# loai loi: SyntaxError
# thong bao loi: SyntaxError: '(' was never closed
# nguyen nhan: do thieu dau ngoac dong 

# ten tep: cau07_chan_doan_loi.py
# so dong: 6
# loai loi: TypeError
# thong bao loi: TypeError: unsupported operand type(s) for *: 'str'
# nguyen nhan: do cong_suat_w la kieu str, khong phai kieu float

# ten tep: cau07_chan_doan_loi.py
# so dong: 6
# loai loi: NameError
# thong bao loi: NameError: name 'dien_nang' is not defined
# nguyen nhan: bien dien_nang chua duoc khai bao nen se hien loi NameError
# cac loi da phat hien:
# SyntaxError, TpeError, NameError