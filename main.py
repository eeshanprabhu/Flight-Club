import requests
endpoint="https://api.tequila.kiwi.com/v2/search"

sheety_enpoint='https://sheetdb.io/api/v1/fn8fdrvf7rewc'

sheety_response=requests.get(url=sheety_enpoint)
min_flight_list=[]
exel_data=sheety_response.json()

iataCodes=[]
alleg_min_price=[]
city_name=[]


def add_to_list(min_price):
    for i in range(len(flight_data["data"])):
        for key in flight_data["data"][i]:
            if key == 'price' and flight_data["data"][i]['price'] == min_price:
                min_flight_list.append(flight_data["data"][i])


for i in range(9):
    for key in exel_data[i]:
        if key=="IATA Code":
            iataCodes.append(exel_data[i]["IATA Code"])

        elif key=="Lowest Price":
            alleg_min_price.append(int(exel_data[i]["Lowest Price"]))

        elif key=="City":
            city_name.append(exel_data[i]["City"])
print(city_name)
print(iataCodes)
print(alleg_min_price)

headers={
    'apikey':'4zRy8IRggsLJRtta3KUWl8QIbMiWkgEY'
}
for i in range(len(iataCodes)):

    parameters={
        'fly_from':iataCodes[i],
        'date_from':'28/12/2023',
        'date_to':'30/12/2023',
        'adults':1,
        'limit':10
    }

    response=requests.get(url=endpoint,params=parameters,headers=headers)
    flight_data=response.json()
    l1=[]
    for j in range(len(flight_data["data"])):
        for key in flight_data["data"][j]:
            if key=='price':
                l1.append(flight_data["data"][j]['price'])

    min_price=min(l1)

    if min_price<alleg_min_price[i]:
        alleg_min_price[i]=min_price
        add_to_list(min_price)


for i in range(len(city_name)):

    update_endpoint=f'https://sheetdb.io/api/v1/fn8fdrvf7rewc/City/{city_name[i]}'
    flightDealsByEeshan={
        "Lowest Price":str(alleg_min_price[i])
    }
    update=requests.put(url=update_endpoint,json=flightDealsByEeshan)
    print(update.text)

print(len(min_flight_list))
user_input=input("Do you want information of any flight?")
if user_input=="yes":
    city=input("Enter the IATA code of the city: ")
    for i in range(len(min_flight_list)):
        for key in min_flight_list[i]:
            if key=="cityCodeFrom" and min_flight_list[i]["cityCodeFrom"]==city:
                print(f"This is your flight information: {min_flight_list[i]}")
elif user_input=="no":
    print("Have a good day!")