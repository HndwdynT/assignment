# Function untuk mengkonversi suhu dari Kelvin ke Celcius
def kelvin_ke_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

# Fungsi untuk mengkonversi suhu dari Celcius ke Kelvin
def celcius_ke_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

# Pemanggilan function konversi
suhu_celcius = kelvin_ke_celcius(300)
print("Suhu dalam Celcius: ", suhu_celcius)

suhu_kelvin = celcius_ke_kelvin(15)
print("Suhu dalam Kelvin: ", suhu_kelvin)