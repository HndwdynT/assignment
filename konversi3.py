# Fungsi untuk mengkonversi suhu dari Fahrenheit
def fahrenheit(temp, konversi_ke):
    # Jika suhu yang dimasukkan adalah Celcius
    if konversi_ke.lower() == 'celcius':
        # Rumus konversi suhu dari Fahrenheit ke Celcius
        return (temp - 32) * 5/9
    # Jika suhu yang dimasukkan adalah Kelvin
    elif konversi_ke.lower() == 'kelvin':
        # Rumus konversi suhu dari Fahrenheit ke Kelvin
        return (temp - 32) * 5/9 + 273.15
    else:
        # Jika suhu yang dimasukkan bukan Celcius atau Kelvin
        return "Suhu yang dimasukkan salah. Masukkan suhu 'celcius' atau 'kelvin'."

# Nilai suhu yang akan dikonversi
temp = 99.5
# Jenis suhu yang akan dikonversi
konversi_ke = 'celcius'

# Mencetak hasil konversi suhu dari Fahrenheit
print('Konversi Fahrenheit ke', konversi_ke, 'adalah : ', fahrenheit(temp, konversi_ke))