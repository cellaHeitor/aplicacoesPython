ano_2_digitos = 6; #Tive que colocar somente "6", pois Pyhton não aceita "06"
tempo_minutos = 150 + ano_2_digitos;
tempo_horas = 2.25;

print(f"Horas: {tempo_minutos / 60:.2f}")
print(f"Minutos: {tempo_horas * 60:.2f}")
