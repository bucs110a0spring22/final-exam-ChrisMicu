import requests

class air:


  url = "https://api.openaq.org/v1/cities?limit=10000"
  city = input("City name: ")

  r = requests.get(url)
  data = r.json()
  

  

  for i in data['results']:
      if i['city'] == city:
          print("The Air Quality of {} is {}".format(i['city'], i['count']))
          break

  else:
      print("Sorry City not found")

    