import os, datetime, cft, json


class file:
    path = os.getcwd() + '/logs'
    name = ''
    full = path + '/' + name

    def update():
        file.full = file.path + '/' + file.name


def updatefile():
    datecode = cft.chars.delete(str(datetime.datetime.now()), " -:.")[0:8]
    file.name = 'log ' + datecode + '.txt'
    file.update()
    if not file.name in os.listdir(os.getcwd() + '/logs'):
        open(file.full, 'w').close()
        with open(file.full, 'w') as logfile:
            logfile.write(
                cft.chars.fillen('Number', length=8) +
                cft.chars.fillen('Time', length=16) +
                cft.chars.fillen('Request URL', length=64) +
                cft.chars.fillen('Request IP', length=16) +
                cft.chars.fillen('Called function', length=16) +
                cft.chars.fillen('Status code', length=16) +
                cft.chars.fillen('Error', length=48, cut=False))
        print('created new log file')


def log(request, called_function, status_code=200, error=None):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    """print(str(ip))
    print(ip)
    print(list(os.environ['no log ips']))
    print(os.environ['no log ips'])"""
    no_log_IPs = json.loads(open('no log IPs.json').read())
    for name in no_log_IPs:
        if str(ip) in no_log_IPs[name]:
            print('log() called, but request ip (' + str(ip) +
                  ') is listed in "no log ips" (' + name + ')')
            return None
    if request.base_url == 'http://mkinana.repl.co/' + os.environ['wakercode']:
        return None
    updatefile()
    if (error == None):
        errormessage = ''
    else:
        errormessage = error
    with open(file.full, 'a') as logfile:
        logfile.write(
            '\n' +
            cft.chars.fillen(len(open(file.full).readlines()), length=8) +
            cft.chars.fillen(str(datetime.datetime.now())[11:23], length=16) +
            cft.chars.fillen(request.url, length=64) +
            cft.chars.fillen(ip, length=16) +
            cft.chars.fillen(called_function, length=16) +
            cft.chars.fillen(status_code, length=16) +
            cft.chars.fillen(errormessage, length=48, cut=False))
    print('wrote log (' + file.full + ')')


def iprecorder(request, name, ipa=None):
    data = dict(json.loads(open('recorded IPs.json').read()))
    if ipa == None:
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip = request.environ['REMOTE_ADDR']
        else:
            ip = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        ip = ipa
    data[name] = str(ip)
    with open('recorded IPs.json', 'w') as record:
        record.write(str(json.dumps(data, indent=4)))
    print('recorded ip (' + str(ip) + ') from name: ' + name)
