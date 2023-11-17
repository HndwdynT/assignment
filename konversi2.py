def konversi_fahrenheit(temp, suhu):
    if suhu.lower() == 'celcius':
        return temp * 9/5 + 32
    elif suhu.lower() == 'kelvin':
        return (temp - 273.15) * 9/5 + 32
    else:
        return "Suhu yang dimasukkan salah. masukkan suhu 'celcius' atau 'kelvin'."

temp = 30
suhu = 'celcius'

print('Temperatur', suhu, 'dalam Fahrenheit adalah', konversi_fahrenheit(temp, suhu))