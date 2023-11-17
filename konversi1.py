# Fungsi untuk mengkonversi suhu dari Kelvin ke Celcius
def kelvin_ke_celcius(kelvin):
    # Rumus konversi suhu dari Kelvin ke Celcius
    celcius = kelvin - 273.15
    return celcius

# Fungsi untuk mengkonversi suhu dari Celcius ke Kelvin
def celcius_ke_kelvin(celcius):
    # Rumus konversi suhu dari Celcius ke Kelvin
    kelvin = celcius + 273.15
    return kelvin

# Menggunakan fungsi kelvin_ke_celcius untuk mengkonversi suhu dari Kelvin ke Celcius
suhu_celcius = kelvin_ke_celcius(300)
# Mencetak hasil konversi
print("Konversi Kelvin ke Celcius :", suhu_celcius)

# Menggunakan fungsi celcius_ke_kelvin untuk mengkonversi suhu dari Celcius ke Kelvin
suhu_kelvin = celcius_ke_kelvin(15)
# Mencetak hasil konversi
print("Konversi Celcius ke Kelvin :", suhu_kelvin)