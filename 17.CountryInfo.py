from countryinfo import CountryInfo

name = input('Enter Country Name: ')
country = CountryInfo(name)
info = country.info()

with open(f'{name}.txt', 'w', encoding='utf8') as file:
    for i,j in info.items():
        file.write(f'{i.upper()}    : {str(j)}\n')

