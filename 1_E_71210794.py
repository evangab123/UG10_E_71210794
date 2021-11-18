print("===== Kalkulator Akar dan Pangkat =====")
print("Pilihan menu : ")
print("1. Pangkat 2 (Kuadrat) ")
print("2. Pangkat 3 (Kubik) ")
print("3. Akar Kuadrat")
n = int(input("Masukan menu yang anda pilih : "))
print(" ")

if n==1:
    a= int(input("Masukan bilangan yang ingin dipangkatkan : "))
    y= a**2
    print("Hasil dari pemangkatan bilangan ", a, "dengan 2 (Kuadrat) adalah ", y)

elif n == 2 :
    a = int(input("Masukan bilangan yang ingin dipangkatkan : "))
    y = a**3
    print ("Hasil dari pemangkatan bilangan", a, "dengan 3 (Kubik) adalah ", y)

elif n== 3:
    a = int(input("Masukan bilangan yang ingin diakarkan : "))
    y = a**(1/2)
    print ("Hasil Akar kuadrat dari bilangan ", a,"adalah",y)

else :
    print("Pilihan menu yang dimasukan tidak sesuai!")