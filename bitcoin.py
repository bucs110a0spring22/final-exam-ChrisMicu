import json
import urllib.request

class convert:

  n=int(input('Enter the number of bitcoins you want to convert to USD: '))
  
  try:
    
      url = "https://api.coindesk.com/v1/bpi/currentprice/CNY.json"
  
      r = urllib.request.urlopen(url)
  
      raw_data=r.read()
  
      data = json.loads(raw_data.decode(r.info().get_param('charset') or 'utf-8'))
  

      bitcoin_price= data['bpi']['USD']['rate_float']
  

      total = bitcoin_price * n
  

      print('\nThe price of {0:d} bitcoin is ${1:.2f}'.format(n,total))
  
  except urllib.error.URLError as e:
  

      print(e.reason)