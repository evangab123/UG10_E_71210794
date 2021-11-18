daftar = input("Masukan daftar siswa : ")
x = daftar.title()
y = x.split(",")
print ("Daftar Siswa : ",y)
w = input("Masukan siswa yang ingin ditambahkan : ") 
lowerd= daftar.lower()
lowerw= w.lower()

if lowerw in lowerd:
    upperw = lowerw.upper()
    print("Siswa atas nama",upperw,"sudah berada dalam daftar siswa")
else: 
    z = ''.join(daftar)
    o = z + ", "+ w
    akhir= o.title()
    akhir2= akhir.split(",")
    print("Hasil penambahan pada daftar siswa : ", akhir2)

