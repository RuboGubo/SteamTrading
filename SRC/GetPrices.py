import requests


#APIKey = 'bt7Hb_zQZ2s3Go5vcoUllwmi2_c'
#AppID = 730 #CSGO

#API = 'https://api.steamapis.com/market/items'

#SteamAPICompactValue = 'safe_ts.last_30d' # Use safe price calculated from 30 days of data, more info: https://steamapis.com/developers (Market Items - Optional Query Parameters "compact_value")

#print(API + '/' + str(AppID) + '?format=compact&compact_value=' + SteamAPICompactValue + '&api_key=' + APIKey)

#print('http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=M4A1-S | Hyper Beast (Minimal Wear)')


sitedata=requests.get('http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=M4A1-S | Hyper Beast (Minimal Wear)')
print(sitedata.content)
