# Fungsi untuk mengkonversi suhu ke Fahrenheit
def fahrenheit(temp, suhu):
    # Jika suhu yang dimasukkan adalah Celcius
    if suhu.lower() == 'celcius':
        # Rumus konversi suhu dari Celcius ke Fahrenheit
        return temp * 9/5 + 32
    # Jika suhu yang dimasukkan adalah Kelvin
    elif suhu.lower() == 'kelvin':
        # Rumus konversi suhu dari Kelvin ke Fahrenheit
        return (temp - 273.15) * 9/5 + 32
    else:
        # Jika suhu yang dimasukkan bukan Celcius atau Kelvin
        return "Suhu yang dimasukkan salah. masukkan suhu 'celcius' atau 'kelvin'."

# Nilai suhu yang akan dikonversi
temp = 30
# Jenis suhu yang akan dikonversi
suhu = 'celcius'

# Mencetak hasil konversi suhu ke Fahrenheit
print('Temperatur', suhu, 'dalam Fahrenheit adalah', fahrenheit(temp, suhu))