import zipfile

import requests
import json
cookies = {
    '_ga': 'GA1.2.1509880747.1571498515',
    '_hjid': 'd86a0ecd-9dd5-4734-9de9-a685b56fb145',
    'launchDarklyUserID': '96443a65-2a2c-4901-9a45-a56333a5574b',
}

headers = {
    'Host': 'api.ricardo.ch',
    'r-client-unique-id': '408892215',
    'r-screen-width': '750',
    'accept': '*/*',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL3JpY2FyZG8uY2gvYXBpL3YyLyIsImV4cCI6MTU3MTkwMzgwOSwiZ3R5IjoicGFzc3dvcmQiLCJpYXQiOjE1NzE4Njc4MDksImlzcyI6Imh0dHBzOi8vcmljYXJkby5jaC8iLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInN1YiI6InJpY2FyZG98NDA4ODkyMjE1In0.Nd8MSB1gHL6QVTkjw0Ra3oMHi7qHtBsSjzHM-my8jW4MOyZPGCq7-_9-StFXdkMGJ07imT1IbueLhyGm2Nj7SuG7C7N-JZIWfxYHSrE7vbKMmkShQCa0junfgCSGE_wNRzZahMriLbVufo8IKHxdtJmhha94pZH_QOJj19DJylDqz9_u9vDjAnbZd9Jh7qEkiYivoYi-haqeZ4FUpL2TGSl2iyC8AsdFs0zsxryysoiICQxLyGAOSdqKEsejGaagoy9-QZtWbR5cvdHnTsYBJp0yl9mnJr4WtIPg4JMjryHkiKaSL1lxo5BhHgtAxqV8Ol9ABIMebeG_xeswEF4mkRalN_dOGE-xwqQ0ZqJgkKsN4FH6lCUbe0sh735Flo7xtOSoAAzNvuKeAHFhXsqT46WUqCARWK5emndGw1sPUUQT0hQumxcBYDkBA0MlDeSqd8etNt8BYaxXOUEDsf1bSYPhzF5idmUWD-mz1ylxmf0iJGzdRJDXw30i9XUIKcxDw4VQlOfI9b5cJ-LVZ9gN0hKWHgYuc3VKVfyUtRf5trjPkknCB2sZll968D3StON9yfOUBZKdgGoh3M1cHQcLkmVsWuZFc7hsUv_ZxZ3Mbb6MYZHd5Zyn8djHSze5ZyxWh1vTydenLu3ff2Dax02XxRK9onSb6yDj4GQqWzHks6I',
    'x-authorization': 'AWS4-HMAC-SHA256 Credential=96A8AAB1-BB3D-4623-A1AA-F76FFAA46DD4/20191023/aws4_request, SignedHeaders=accept-language;host;r-amz-date;r-apiv2-key;r-client-unique-id;r-screen-height;r-screen-width;user-agent, Signature=4e0357b795c2542a0817ae068fd290549419c29a757493f4a0ca814b60f522de',
    'accept-language': 'en',
    'r-amz-date': '20191023T215649Z',
    'r-screen-height': '1334',
    'user-agent': 'MobileRicardo (iPhone; iOS 13.1.3) ricardo.ch/7.5.3-1121 (release) deviceId/96A8AAB1-BB3D-4623-A1AA-F76FFAA46DD4',
    'r-apiv2-key': 'AFDE2010-3B4E-41EC-A72E-1358017F3075',
}

params = (
    ('facet_categories_level', '1'),
    ('offer_types', '1,2,3'),
    ('sorting_type', '0'),
    ('page_size', '15'),
    ('listing_type', '2'),
    ('exclude_promo_offer', 'False'),
)

response = requests.get('https://api.ricardo.ch/m/search/articles', headers=headers, params=params, cookies=cookies)


json_articles = response.json()['articles']

print(json_articles)

with open("result.json", "w") as jsonf:
       json.dump(json_articles, jsonf, indent=4)

zip_file = zipfile.ZipFile("result.zip", "w")
zip_file.write("result.json")
zip_file.close()