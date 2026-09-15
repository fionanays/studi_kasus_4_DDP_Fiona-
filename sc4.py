buku = {
    "Judul":"Laut Bercerita",
    "Tahun_terbit":2017

}


while True:
    print("\nSELAMAT DATANG DI PERPUSTAKAAN")
    print("1. Tampilkan Data Buku")
    print("2. Tambah data penerbit")
    print("3. Ubah data penerbit")
    print("4. Hapus data penerbit")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-5): ")
    
    if pilihan == "1" :
        print("Data buku yang tersedia: ",buku)

    elif pilihan == "2" :
        penerbit = input("Nama penerbit: ")
        buku["penerbit"] = penerbit
        print("Data penerbit berhasil ditambahkan", buku)

    elif pilihan == "3" :
        penerbit_baru = input("Ubah nama penerbit:")
        buku.update({"penerbit":penerbit_baru})
        print("Nama penerbit berhasil diubah",buku)

    elif pilihan == "4" :
        buku.pop("penerbit")
        print("Data penerbit setelah dihapus: ", buku)

    else :
        print("Program selesai")
        break