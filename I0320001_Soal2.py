
nama = input('Nama :')
nilai = int(input('Nilai :'))

if nilai >= 85:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah A')
elif nilai >= 80:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah A-')
elif nilai >= 75:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah B+')
elif nilai >= 70:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah B')
elif nilai >= 65:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah C+')
elif nilai >= 60:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah C')
elif nilai < 60:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah E')
print()