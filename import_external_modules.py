import requests, os


def importmodules(sourcesraw, update=False):
    print('importing external modules')
    modules = []
    allmodules = []
    existing = []
    sources = {}
    for file in os.scandir():
        existing.append(file.name)
    if update:
        print('existing modules will be reimported for updates')
        sources = sourcesraw
    else:
        print('existing modules will not be reimported')
        for name in sourcesraw:
            if not name + '.py' in existing:
                sources[name] = sourcesraw[name]
    for name in sources:
        with open(name + '.py', 'w') as module:
            print('importing ' + name)
            module.write(requests.get(sources[name]).text)
        modules.append(name)
    for module in modules:
        exec('import ' + module)
    for name in sourcesraw:
        allmodules.append(name)
    print('imported all requested external modules')
    return allmodules