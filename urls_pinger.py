from threading import Thread
import requests, json, time


def pinger():
    while True:
        try:
            urls = dict(json.loads(open('urls to ping.json').read()))
            for site in urls:
                print('pinged ' + site + ', returned status code = ' +
                      str(requests.get(urls[site]).status_code))
                time.sleep(5)
        except:
            pass
        time.sleep(60)


pingerthread = Thread(target=pinger)
pingerthread.start()
