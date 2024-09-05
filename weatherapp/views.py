from django.shortcuts import render
import json
import urllib.request

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        try:
            # Form the correct URL
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8e93c45e41558bbd1db7799135877cbd'
            res = urllib.request.urlopen(url)
            json_data = json.loads(res.read().decode('utf-8'))
            
            # Extract relevant data
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinate': f"{json_data['coord']['lon']}, {json_data['coord']['lat']}",
                'temp': str(json_data['main']['temp']) + ' K', # temperature in Kelvin
                'pressure': str(json_data['main']['pressure']) + ' hPa',  # atmospheric pressure
                'humidity': str(json_data['main']['humidity']) + ' %'  # humidity percentage
            }
        except Exception as e:
            data['error'] = str(e)
    else:
        city = ''

    return render(request, 'index.html', {'city': city, 'data': data})
