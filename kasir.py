print('\r\n')
print(5*'=', 'KANTIN FASILKOM', 5*'=')
print('\r\n')

total = 0.00
while True:
    jumlah = int(input('masukkan jumlah barang: '))
    print('\r\n')
    harga = int(input('masukkan harga barang:'))
    print('\r\n')
    tothar = jumlah*harga
    print(f'total pembelian: {tothar}')
    print('\r\n')
    total += tothar
    tambah = input('apakah ada barang tambahan lain? (y/t)')
    print('\r\n')

    if tambah == "t":
        break
print(f"total pembelian = Rp {total} ")

print('\r\n')
print(3*'=', 'TERIMAKASIH TELAH BERBELANJA', 3*'=')

