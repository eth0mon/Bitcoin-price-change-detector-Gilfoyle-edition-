import urllib.request, json
from playsound import playsound
 
target = 9592 # you can change this based on your target price
change = True
def value():
    with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
        data = json.loads(url.read().decode())
    return float(data.get('bpi').get('USD').get('rate').replace(",", ""))
price_old = value()
 
while True:
    price = value()
    if price <=target and price_old>=target:
        change = True
        price_old = price
    elif price >= target and price_old<=target:
        change = True
        price_old = price
       
    while change:
        price = value()
        if price <= target:
            print("FUCK YOU DINESH\n")
            change = True
        else:
            print("YOU SUFFER BUT WHY\n")
            playsound('u.mp3')
            change = False
