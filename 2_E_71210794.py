x = float(input("Masukan suhu tubuh Anda : "))

if x > 50 :
    print("Anda bukan Manusia :) ")
elif x < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif x >37.5 and x <= 50:
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum. ")
elif x >= 32 and x<= 37.5 :
    print("Suhu Anda normal!")