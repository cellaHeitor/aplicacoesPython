km_por_dia = 19;
ano_2_digitos = 6; #Tive que colocar somente 6, por que sou de 2006 e Python não aceita "06" somente "6"

gasto_diario = 300 + ano_2_digitos;

print('Total na semana: ', km_por_dia * 7);
print('Diferença: ', 100 - gasto_diario);
print('Cobertura diária: ', 500 // gasto_diario);
print('Porcentagem: ', gasto_diario % 100);
print('Média diária: ', gasto_diario / km_por_dia);