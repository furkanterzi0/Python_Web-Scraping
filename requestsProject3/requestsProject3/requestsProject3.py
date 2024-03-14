import requests

def getWeatherCondition(city):
    url=f'http://api.weatherapi.com/v1/current.json?key=cdddbc337c454c4abc4194233232604&q={city}&aqi=no'
    result=requests.get(url)
    result=result.json()
    print('\nlocal time: '+ str(result['location']['localtime']))
    print('\ncountry: '+ str(result['location']['country']))
    print('temp for C: '+ str(result['current']['temp_c']))
    print('temp for F: '+ str(result['current']['temp_f']))
    print('condition: '+ str(result['current']['condition']['text']))
    print('\nlast update: '+ str(result['current']['last_updated']))
    print('\n------------------------\n')
    


city=input('which city do you want to get information for: ')
getWeatherCondition(city)



