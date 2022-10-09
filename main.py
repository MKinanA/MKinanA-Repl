from flask import Flask, make_response, abort, request, request_finished, redirect, request_started, send_from_directory
from datetime import datetime
from threading import Thread
'''from base64 import b64decode as dec'''
'''from flask import jsonify'''
from werkzeug.utils import secure_filename
from textifier import textify
from blog import blog as blogger
from blog import upload as blogupload
import blinker, json, os, requests, pytz, import_external_modules, logger, time, urls_pinger
'''os.mkdir(os.getcwd()+'\\cloud')'''

for module in import_external_modules.importmodules(
    {
        'cft': 'https://cft.mkinana.repl.co',
    }, update=False):
    exec('import ' + module)

app = Flask(__name__)


def beforecolon(text):
    result = ''
    for e in str(text):
        if not e == ':':
            result = result + e
        else:
            break
    return result


def aftercolon(text):
    result = ''
    for e in range(len(text)):
        if not text[-(e + 1)] == ':':
            if text[-(e + 1)] == ' ' and text[-(e + 2)] == ':':
                break
            else:
                result = text[-(e + 1)] + result
        else:
            break
    return result


@app.errorhandler(400)
def error400(e):
    logger.log(request, 'error400', 400, e)
    return textify(json.dumps(
        {
            'status': 'error',
            'error code': 400,
            'error type': beforecolon(str(e))[4:len(beforecolon(str(e)))],
            'message': aftercolon(str(e))
        },
        indent=4),
                   mimetype='application/json',
                   code=400)


@app.errorhandler(403)
def error403(e):
    logger.log(request, 'error403', 403, e)
    return textify(json.dumps(
        {
            'status': 'error',
            'error code': 403,
            'error type': beforecolon(str(e))[4:len(beforecolon(str(e)))],
            'message': aftercolon(str(e))
        },
        indent=4),
                   mimetype='application/json',
                   code=403)


@app.errorhandler(404)
def error404(e):
    logger.log(request, 'error404', 404, e)
    return textify(json.dumps(
        {
            'status': 'error',
            'error code': 404,
            'error type': beforecolon(str(e))[4:len(beforecolon(str(e)))],
            'message': aftercolon(str(e))
        },
        indent=4),
                   mimetype='application/json',
                   code=404)


@app.errorhandler(405)
def error405(e):
    logger.log(request, 'error405', 405, e)
    return textify(json.dumps(
        {
            'status': 'error',
            'error code': 405,
            'error type': beforecolon(str(e))[4:len(beforecolon(str(e)))],
            'message': aftercolon(str(e))
        },
        indent=4),
                   mimetype='application/json',
                   code=405)


@app.errorhandler(500)
def error500(e):
    logger.log(request, 'error500', 500, e)
    return textify(json.dumps(
        {
            'status': 'error',
            'error code': 500,
            'error type': beforecolon(str(e))[4:len(beforecolon(str(e)))],
            'message': aftercolon(str(e))
        },
        indent=4),
                   mimetype='application/json',
                   code=500)


@request_started.connect
def requeststarted(*args, **kwargs):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    if ip in json.loads(open('banned IPs.json').read()):
        abort(
            403,
            'Our server detected that your current public IP address is listed in our banned IPs list'
        )


@request_finished.connect
def requestfinished(*args, **kwargs):
    if request.method == 'POST':
        for file in request.files:
            request.files[file].save(
                os.path.join('uurfs/' +
                             secure_filename(request.files[file].filename)))
    logger.log(request, '')


for key in eval(os.environ['keys']):
    try:
        os.mkdir(os.getcwd() + '/cloud/' + key)
    except:
        pass


def contains(ledict, tocheck):
    for key in dict(ledict):
        if dict(ledict)[key] == tocheck:
            return True
    return False


def getkeybyvalue(ledict, value):
    for key in dict(ledict):
        if dict(ledict)[key] == value:
            return key
    return None


'''def status():
    return {
        'status':
        'active',
        'message':
        'The repl is awake',
        'routes': {
            '/<string>': 'returns <string>',
            '/write': 'write a file in server cloud',
            '/read': 'read a file or folder from server cloud'
        },
        'dev\'s current time':
        str(datetime.now(pytz.timezone(os.environ['timezone'])))
    }'''


@app.route('/')
def home():
    return blogger('main', request)


@app.route('/' + os.environ['testcode'])
def test():
    abort(403)


@app.route('/status')
def status():
    return redirect('https://stats.uptimerobot.com/vk3KzHEJkG')


@app.route('/ip')
def getip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return textify(request.environ['REMOTE_ADDR'])
    else:
        return textify(request.environ['HTTP_X_FORWARDED_FOR'])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/recordip/<name>')
def recordip(name):
    logger.iprecorder(request, name)
    return textify('recorded your ip')


'''
@app.route('/addjson/<filename>/<key>/<value>')
def add(filename, key, value):
    try:
        content = json.loads(open(filename + '.json').read())
    except:
        content = {}
    content[key] = value
    with open(filename + '.json', 'w') as file:
        file.write(json.dumps(content, indent=4))
    return jsonify({'status':'succeeded','message':'added "' + key + '" = "' + value + '" to ' + filename + '.json'})
'''


@app.route('/write')
def write():
    return textify(json.dumps(
        {
            'routes': {
                '/write/<code>/<filename>':
                'creates <filename> in folder of <code> in server cloud',
                '/write/<code>/<filename>/<content>':
                'writes <content> to <filename> in folder of <code> in server cloud'
            }
        },
        indent=4),
                   mimetype='application/json')


@app.route('/write/<code>')
def writee(code):
    abort(400, 'Please specify a file to create or write')


@app.route('/write/<code>/<filename>')
def createfile(code, filename):
    verified = False
    if 'key' in request.args:
        if request.args.get('key') == eval(
                os.environ['write key'])[getkeybyvalue(
                    eval(os.environ['keys']), code)]:
            verified = True
        else:
            verified = False
    else:
        verified = False
    if not verified:
        abort(
            500,
            'Invalid key. If you own the cloud folder, please include ?key=<your folder\'s write key> in the url'
        )
    try:
        try:
            open('cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                 '/' + filename)
            message = 'verified the existence of ' + filename + ' in ' + getkeybyvalue(
                eval(os.environ['keys']), code)
        except:
            message = 'created ' + filename + ' in ' + getkeybyvalue(
                eval(os.environ['keys']), code)
        with open(
                'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                '/' + filename, 'w') as file:
            pass
        return textify(json.dumps({
            'status': 'succeeded',
            'message': message
        },
                                  indent=4),
                       mimetype='application/json')
    except:
        abort(
            404,
            'The folder you requested to create a file in does not exist in the server cloud'
        )


@app.route('/write/<code>/<filename>/<content>')
def writefile(code, filename, content):
    verified = False
    if 'key' in request.args:
        if request.args.get('key') == eval(
                os.environ['write key'])[getkeybyvalue(
                    eval(os.environ['keys']), code)]:
            verified = True
        else:
            verified = False
    else:
        verified = False
    if not verified:
        abort(
            500,
            'Invalid key. If you own the cloud folder, please include ?key=<your folder\'s write key> in the url'
        )
    try:
        with open(
                'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                '/' + filename, 'w') as file:
            file.write(content)
        return textify(json.dumps(
            {
                'status':
                'succeeded',
                'message':
                'wrote \'' + content + '\' to ' + filename + ' in ' +
                getkeybyvalue(eval(os.environ['keys']), code)
            },
            indent=4),
                       mimetype='application/json')
    except TypeError:
        abort(
            404,
            'The folder you requested to write a file in does not exist in the server cloud'
        )


@app.route('/upload/<code>', methods=['POST'])
def upload(code):
    verified = False
    if 'key' in request.args:
        if request.args.get('key') == eval(
                os.environ['write key'])[getkeybyvalue(
                    eval(os.environ['keys']), code)]:
            verified = True
        else:
            verified = False
    else:
        verified = False
    if not verified:
        abort(
            500,
            'Invalid key. If you own the cloud folder, please include ?key=<your folder\'s write key> in the url'
        )
    if request.method == 'POST':
        try:
            uploaded_files = []
            for file in request.files:
                request.files[file].save(
                    os.path.join(
                        'cloud/' +
                        getkeybyvalue(eval(os.environ['keys']), code),
                        secure_filename(request.files[file].filename)))
                uploaded_files.append(
                    secure_filename(request.files[file].filename))
            return textify(
                json.dumps(
                    {
                        'status':
                        'success',
                        'message':
                        'successfully uploaded files to cloud folder \'' +
                        getkeybyvalue(eval(os.environ['keys']), code) + '\'',
                        'uploaded files':
                        uploaded_files
                    },
                    indent=4))
        except TypeError:
            abort(
                404, 'The folder you requested to upload a file to (' + code +
                ') does not exist in the server cloud')


'''@app.route(
    '/upload/<code>/<filename>/<totallen>/<uploadedlen>/<uploadinglen>/<content>'
)
def upload(code, filename, totallen, uploadedlen, uploadinglen, content):
    try:
        with open(
                'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                '/' + filename + '.txt', 'wb') as init:
            pass
        if int(uploadedlen) != len(
                open('cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                     '/' + filename).read()):
            raise Exception(
                '<uploadedlen> (second arg) doesn\'t match the length of uploaded content ('
                + str(totallen) + '!=' + str(
                    len(
                        open('cloud/' +
                             getkeybyvalue(eval(os.environ['keys']), code) +
                             '/' + filename).read())) + ')')
        upload_progresses = json.loads(open('upload progresses.json').read())
        if int(uploadedlen) == 0:
            upload_progresses[getkeybyvalue(eval(os.environ['keys']), code) +
                              '/' + filename] = {
                                  'last continued': str(time.time()),
                                  'progress': '0.0%'
                              }
        else:
            upload_progresses[getkeybyvalue(eval(os.environ['keys']), code) +
                              '/' + filename] = {
                                  'last continued':
                                  str(round(time.time())),
                                  'progress':
                                  str(((int(uploadinglen) + int(uploadedlen)) /
                                       int(totallen)) * 100) + '%'
                              }
        with open('upload progresses.json', 'w') as file:
            file.write(json.dumps(upload_progresses, indent=4))
        with open(
                'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                '/' + filename + '.txt', 'at') as file:
            file.write(content.format(slash='/', plus='+', equals='='))
        upload_progresses[getkeybyvalue(eval(os.environ['keys']), code) + '/' +
                          filename]['progress'] = str(
                              ((int(uploadinglen) + int(uploadedlen)) /
                               int(totallen)) * 100) + '%'
        if str(upload_progresses[getkeybyvalue(eval(os.environ['keys']), code)
                                 + '/' + filename]['progress']) == '100.0%':
            print('an upload finished')
            rawcont = open('cloud/' +
                           getkeybyvalue(eval(os.environ['keys']), code) +
                           '/' + filename + '.txt').read()
            with open(
                    'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                    '/' + filename, 'wb') as file:
                file.write(dec(rawcont))
            del upload_progresses[getkeybyvalue(eval(os.environ['keys']), code)
                                  + '/' + filename]
            os.remove('cloud/' +
                      getkeybyvalue(eval(os.environ['keys']), code) + '/' +
                      filename + '.txt')
        with open('upload progresses.json', 'w') as file:
            file.write(json.dumps(upload_progresses, indent=4))
        return textify(json.dumps(
            {
                'status':
                'succeeded',
                'message':
                'appended <content> to ' + filename + ' in ' +
                getkeybyvalue(eval(os.environ['keys']), code),
                'progress':
                str(((int(uploadinglen) + int(uploadedlen)) / int(totallen)) *
                    100) + '%'
            },
            indent=4),
                       mimetype='application/json')
    except TypeError:
        abort(
            404,
            'The folder you requested to write a file in does not exist in the server cloud'
        )
    except Exception as e:
        abort(400, str(e))'''


@app.route('/read')
def read():
    return textify(json.dumps(
        {
            'routes': {
                '/read/<code>':
                'returns list of files in folder of <code> from server cloud',
                '/read/<code>/<filename>':
                'returns content of <filename> in folder of <code> from server cloud'
            }
        },
        indent=4),
                   mimetype='application/json')


@app.route('/read/<code>')
def readfolder(code):
    def listdir(path):
        toreturn = []
        for dir in os.scandir(path):
            toreturn.append(dir.name)
        return toreturn

    try:
        return textify(json.dumps(
            listdir(os.getcwd() + '/cloud/' +
                    getkeybyvalue(eval(os.environ['keys']), code)),
            indent=4),
                       mimetype='application/json')
    except TypeError:
        abort(
            404, 'The folder you requested to read (' + code +
            ') does not exist in the server cloud')


@app.route('/read/<code>/<filename>')
def readfile(code, filename):
    try:
        try:
            return textify(
                open(
                    'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                    '/' + filename, 'rt').read())
        except:
            return textify(
                open(
                    'cloud/' + getkeybyvalue(eval(os.environ['keys']), code) +
                    '/' + filename, 'rb').read())
    except (FileNotFoundError, TypeError):
        abort(
            404, 'The file you requested to read (' + filename +
            ') does not exist in the server cloud')


serverdict = json.loads(open('serverdata.json').read())


@app.route('/server')
def serverdef():
    global serverdict
    for x in request.args:
        serverdict[x] = request.args.get(x)
    with open('serverdata.json', 'w') as serverdata:
        serverdata.write(json.dumps(serverdict, indent=4))
    return textify(json.dumps(serverdict, indent=4),
                   mimetype='application/json')


@app.route('/blog')
def blog():
    return redirect('https://mkinana.repl.co/')


@app.route('/blog/<page>', methods=['GET', 'POST'])
def blogs(page):
    if request.method == 'GET':
        return blogger(page, request)
    elif request.method == 'POST':
        return blogupload(page, request)


def replwaker(url, interval=10):
    print('replwaker started with args = (url=' + url + ', interval=' +
          str(interval) + ')')
    while True:
        print('HTTP called, returned status code = ' +
              str(requests.get(url).status_code))
        time.sleep(interval)


if __name__ == '__main__':
    #deactivate these two codes to stop waker thread
    waker = Thread(target=replwaker,
                   args=('https://mkinana.repl.co/wake_up_wake_up_stay_awake',
                         20))
    '''waker.start()'''

    import PJ_Berkas

    app.run(host='0.0.0.0')
