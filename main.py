print("=== kalkulator suhu ===")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Fahrenheit ke Kelvin")
print("6. Kelvin ke Fahrenheit")

pilihan = input("Masukkan pilihan (1-6): ")
suhu = float(input("Masukkan suhu: "))

if pilihan == "1":
    hasil = (suhu * 9/5) + 32
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Celsius = {rounded_hasil} Fahrenheit")
elif pilihan == "2":
    hasil = (suhu - 32) * 5/9
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Fahrenheit = {rounded_hasil} Celsius")
elif pilihan == "3":
    hasil = suhu + 273.15
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Celsius = {rounded_hasil} Kelvin")
elif pilihan == "4":
    hasil = suhu - 273.15
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Kelvin = {rounded_hasil} Celsius")
elif pilihan == "5":
    hasil = (suhu - 32) * 5/9 + 273.15
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Fahrenheit = {rounded_hasil} Kelvin")
elif pilihan == "6":
    hasil = (suhu - 273.15) * 9/5 + 32
    rounded_hasil = round(hasil,2)
    print(f"{suhu} Kelvin = {rounded_hasil} Fahrenheit")
else:
    print("Pilihan tidak valid")