import main
import ScrapingMethods as sc

country = 'it'
city = 'Chiavari'
checkin = "2023-05-21"
checkout = "2023-05-22"
adults = 1
children = 0
numberOfRooms = 1
currency = 'EUR'

b = sc.getHotelList(country, city)
b['Accomodation Name'] = b['Accomodation Name'].astype(str)
b['Accomodation Type'] = b['Accomodation Type'].astype(str)

for hotel in b['Accomodation Name']:

    typeAcc = b['Accomodation Type'][b['Accomodation Name'] == hotel].reset_index()
    del[typeAcc['index']]
    typeAcc = typeAcc['Accomodation Type'][0]

    a = sc.getSingleHotelDataWithFeatures(typeAcc, hotel, checkin, checkout, adults, children, numberOfRooms, currency)
    sc.aggregaDBHotel(a)
    print(hotel, 'analizzato e storato in DB')

    print('\n')


