from countryinfo import CountryInfo

country = CountryInfo(input('Digite o nome do país: '))

print('Capital: ', country.capital())
print('Moeda: ', country.currencies())
print('Língua: ', country.languages())
print('Fuso horário: ', country.timezones())
print('Área: ', country.area())
print('População: ', country.population())
print('Bandeira: ', country.flag())  

