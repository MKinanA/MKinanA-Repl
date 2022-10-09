from flask import abort
from textifier import textify
import os, json, datetime
from werkzeug.utils import secure_filename

allowed_file_extensions = ['html', 'htm', 'pdf']
afe_exceptions = ['coba']


def namext(filename):
    name = ''
    extension = ''
    for x in range(len(filename)):
        if filename[-x] == '.':
            name = filename[0:-x]
            break
        else:
            if not filename[-(x + 1)] == '.':
                extension = filename[-(x + 1)] + extension
    return {'name': name, 'extension': extension}


#this blog page function (below) returns any file type, discontinued because blog pages should just be html
'''def blog(page):
    for file in os.scandir('blog pages'):
        name = ''
        for x in range(len(file.name)):
            if file.name[-x] == '.':
                name = file.name[0:-x]
                break
        if name == page:
            try:
                return textify(open('blog pages/' + file.name, 'rt').read(),
                               mimetype='')
            except:
                return textify(open('blog pages/' + file.name, 'rb').read(),
                               mimetype='')
    abort(
        404,
        'The server failed to return the blog page you are looking for, either the page does not exist or you mistyped the url'
    )'''


#now this blog page function (below) returns any file with the extension listed in allowed_file_extensions, returns error 500 for other file extensions
def blog(page, request):
    global allowed_file_extensions, afe_exceptions
    for file in os.scandir('blog pages'):
        name = namext(file.name)['name']
        extension = namext(file.name)['extension']
        if name == page:
            if extension not in allowed_file_extensions and name not in afe_exceptions:
                abort(
                    500,
                    'The file for the blog page you requested has a not allowed extension ('
                    + extension + ')')
            try:
                return textify(open('blog pages/' + file.name, 'rt').read(),
                               mimetype='')
            except:
                return textify(open('blog pages/' + file.name, 'rb').read(),
                               mimetype='')
    abort(
        404,
        'The server failed to return the blog page you are looking for, either the page does not exist or you mistyped the url'
    )


def upload(page, request):
    global allowed_file_extensions
    uploaded_files = []
    for file in request.files:
        name = namext(secure_filename(request.files[file].filename))['name']
        extension = namext(secure_filename(
            request.files[file].filename))['extension']
        if extension not in allowed_file_extensions and name not in afe_exceptions:
            abort(
                500,
                'The file for the blog page you requested has a not allowed extension ('
                + extension + ')')
        if not name == request.path[6:len(request.path)]:
            abort(
                500,
                'The name of the file you are trying to upload does not match the url path (\''
                + name + '\' and \'' + request.path[6:len(request.path)] +
                '\')')
        request.files[file].save('blog pages/pending/' + name + '.' +
                                 extension)
        uploaded_files.append(name + '.' + extension)
    return textify(
        json.dumps(
            {
                'status': 'success',
                'message': 'successfully uploaded files for blog page \'' +
                page + '\' (pending for check)',
                'uploaded files': uploaded_files
            },
            indent=4))
