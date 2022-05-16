import requests



class cities:
  

  url = "https://api.openaq.org/v1/cities?limit=10000"
  

  r = requests.get(url)
  data = r.json()
  
  with open("Cities.txt", "w") as f:
      f.write("Country Code           City Name\n\n")
      for i in data["results"]:
          try:
              temp = "     " + i["country"] + "                " + i["city"] + "\n"
              f.write(temp)
          except:
              pass
  f.close()