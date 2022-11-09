pilihan="y"
while pilihan=="y":
    print("NIM : 20210801364")
    print("NAMA : Sulistiyawati")
    print("""Pilihan
    1. Capucino
    2. teh
    3. Exit""")
    pesan=str(input("masukkan pilihan ="))
    if pesan == "1":
        print("memilih capucino")
        harga=int(input("masukkan harga ="))
        ppn= float(harga * 0.1)
        totalbayar = harga + ppn
        print("Jumlah yang harus dibayarkan :",totalbayar)
    elif pesan == "2":
        print("memilih teh")
        harga=int(input("masukkan harga ="))
        ppn= float(harga * 0.1)
        totalbayar = harga + ppn
        print("Jumlah yang harus dibayarkan :",totalbayar)
    elif pesan == "3":
        pilihan ="n"