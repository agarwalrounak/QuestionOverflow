import requests
import time

print("Enter tags in separate lines")
tags = ''
while True:
    tag = input()
    if tag == '':
        break
    if tags == '':
        tags = requests.utils.quote(tag)
    else:
        tags = tags + ';' + requests.utils.quote(tag)

print("Fetching questions...")

while True:
    fromDate = time.time()
    time.sleep(150)
    toDate = time.time()

    url = 'https://api.stackexchange.com/2.2/search/advanced?fromdate=' + str(round(fromDate)) + '&todate=' + str(
        round(toDate)) + '&order=asc&sort=creation&accepted=False&closed=False&tagged=' + tags + '&site=stackoverflow'

    r = requests.get(url)

    print(r.json())

    for item in r.json()['items']:
        print(item['link'])
        print(item['title'])
