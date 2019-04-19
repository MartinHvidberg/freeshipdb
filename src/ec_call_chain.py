
#!/usr/bin/python

import os

def get_import_lines(str_fn):
    lst_ret = list()
    try:
        with open(str_fn, 'r') as fil_in:
            for lin in fil_in:
                if lin.lstrip(' ')[:7] == 'import ':
                    lst_ret.append(lin.strip())
    except:
        pass
    return lst_ret


def get_def_lines(str_fn):
    lst_ret = list()
    try:
        with open(str_fn, 'r') as fil_in:
            for lin in fil_in:
                if lin.lstrip(' ')[:4] == 'def ':
                    lst_ret.append(lin.strip())
    except:
        pass
    return lst_ret

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if file.endswith('.py'):
            print(len(path) * '---', file)
            for impor in get_import_lines(file):
                print(len(path) * '   ', '*', impor)
            for defin in get_def_lines(file):
                print(len(path) * '   ', ';', defin)
