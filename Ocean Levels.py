#Johnathan Sullivan
#Ocean Levels




#Assuming the ocean's level is currently rising at about 1.6 millimeters per year,/
#create an application that displays the number of millimeters that the ocean will /
#have risen each year for the next 25 years.



total = 0
ocean_level_change_per_year = 1.6 #millimeters per year

for num in range (1,26):
    total = total + ocean_level_change_per_year
    print(f'Year {num}, Ocean rise: {total:.2f} mm')


