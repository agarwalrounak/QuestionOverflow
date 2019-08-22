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

prev_id = []
current_id = []

while True:
    if not prev_id:
        fromDate = time.time()
    else:
        fromDate = time.time() - 10
    time.sleep(150)
    toDate = time.time()

    print(fromDate, toDate, sep=", ")

    # print(time.time())

    url = 'https://api.stackexchange.com/2.2/search/advanced?fromdate=' + str(round(fromDate)) + '&todate=' + str(
        round(toDate)) + '&order=asc&sort=creation&accepted=False&closed=False&tagged=' + tags + '&site=stackoverflow'

    r = requests.get(url)

    print(r.json())

    current_id.clear()

    for item in r.json()['items']:
        current_id.append(item['question_id'])

    next_id = [qid for qid in current_id if qid not in prev_id]

    for item in r.json()['items']:
        if item['question_id'] in next_id:
            print(item['link'])
            print(item['title'])

    prev_id = next_id

    # print(time.time())
