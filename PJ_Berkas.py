from time import time, sleep
from threading import Thread
from os import scandir
from json import loads, dumps
import datetime
from hijri_converter import Hijri as hijri, Gregorian as gregorian


def check_upload_progresses():
    while True:
        try:
            upload_progresses = loads(open('upload progresses.json').read())
            updateup = False

            for upload in upload_progresses:
                if time() - int(
                        round(
                            float(upload_progresses[upload]
                                  ['last continued']))) > 1800:
                    del upload_progresses[upload]
                    print(
                        'deleted ' + upload +
                        ' from upload progresses (discontinued for longer than 30 minutes)'
                    )
                    updateup = True
                    break

            if updateup:
                with open('upload progresses.json', 'w') as file:
                    file.write(dumps(upload_progresses, indent=4))
        except:
            pass


def update_main_page():
    while True:
        try:
            hijridate = gregorian(datetime.datetime.now().year,
                                  datetime.datetime.now().month,
                                  datetime.datetime.now().day).to_hijri()
            date = datetime.datetime.now()

            if (hijridate.month == 9 and hijridate.day in [29,30,31]) or (hijridate.month == 10 and hijridate.day in [1,2,3]):
                with open('blog pages/main.html', 'wt') as main:
                    main.write(
                        open('blog pages/main pages/eid_fitr.html').read())
            elif hijridate.month == 12 and hijridate.day in [10,11,12,13]:
                with open('blog pages/main.html', 'wt') as main:
                    main.write(
                        open('blog pages/main pages/eid_adha.html').read())
            elif hijridate.month == 9:
                with open('blog pages/main.html', 'wt') as main:
                    main.write(
                        open('blog pages/main pages/ramadan.html').read())
            elif date.month == 8:
                with open('blog pages/main.html', 'wt') as main:
                    main.write(open('blog pages/main pages/hutri.html').read())
            else:
                with open('blog pages/main.html', 'wt') as main:
                    main.write(
                        open('blog pages/main pages/normal.html').read())
        except:
            pass
        sleep(21600)


check_upload_progresses_thread = Thread(target=check_upload_progresses)
update_main_page_thread = Thread(target=update_main_page)

check_upload_progresses_thread.start()
update_main_page_thread.start()
