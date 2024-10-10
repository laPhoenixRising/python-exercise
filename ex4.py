cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print('Sono disponibili', cars, 'auto.')
print('Ci sono solo', drivers, 'guidatori disponibili.')
print('Ci saranno', cars_not_driven, 'auto vuote oggi.')
print('Possiamo trasportare', carpool_capacity, 'persone oggi.')
print('Abbiamo', passengers, 'passeggeri da trasportare oggi.')
print('Dobbiamo caricare circa', average_passengers_per_car, 'persone in ogni auto.')
