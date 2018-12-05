import os
from os.path import isfile, join, abspath, dirname, getmtime


# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)


def get_recent_file(mypath):
    try:
        files_tuple = [(f, int(getmtime(join(mypath, f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
        sort_by_update = sorted(files_tuple, key=lambda file: file[1])
        return sort_by_update[-1][0]
    except FileNotFoundError:
        return None


def get_bundle(filename):
    if 'dev' in filename:
        return 'com.app.dev'
    elif 'alpha' in filename:
        return 'com.app.alpha'
    else:
        return 'ru.app.android'
