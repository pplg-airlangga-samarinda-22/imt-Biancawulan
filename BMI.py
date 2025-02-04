Berat_Badan = int(input('Berat Badan (kg) : '))
Tinggi_Badan = int(input('Tinggi Badan (Cm) : '))


Tinggi_Badan = Tinggi_Badan/100

Nilai_BMI = Berat_Badan / (Tinggi_Badan**2)


print('Nilai BMI Anda adalah : ' , Nilai_BMI)

if Nilai_BMI < 17.0 : 
    print('Berat badan anda mirip ikan teri ')
elif Nilai_BMI >17.0 and Nilai_BMI <18.4 :
    print('sepertinya anda belum makan 3 hari ')
elif Nilai_BMI > 18.5 and Nilai_BMI < 25.0:
    print('Anda manusia normal')
elif Nilai_BMI > 25.1 and Nilai_BMI < 27.0:
    print('Anda gemuk tingkat normal')
elif Nilai_BMI > 27.1 :
    print('Anda gemuk tingkat tinggi')