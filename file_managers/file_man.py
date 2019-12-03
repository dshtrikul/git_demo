import os
from glob import glob
from pprint import pprint

# os.chdir('/home/dmytro/Downloads/')
# os.system('pwd')
# # -------------
# files = [item[:-1] for item in os.popen('ls')]
# print (files)
# # -------------
# print(glob('*'))         # same as above
#
#

# ---------------
# pprint(glob('/home/dmytro/Downloads/*.pdf'))  ## how to search /home/*/.pdf ???
# pprint(os.listdir('/home/dmytro/Downloads/'))


def walker(path=".", exts=(), verbose=False):
    """
    Counts the number of files with give file extensions.
    :param path: String path
    :param exts: Comma-separated string of extensions or a tuple
    :param verbose: True to write all filenames and its dirs
    :return: None
    """
    file_list = {}
    if isinstance(exts, str):
        exts = exts.split(',')
    for dirname, dirs, files in os.walk(path):
        for file in files:
            for ext in exts:
                ext = ext.strip()
                if file.endswith(ext):
                    file_list[file] = ext
                    if verbose:
                        print("/".join(dirname.split('/')[1:5])+'...', '>>>', file)

    for ext in exts:
        number = 0
        for item in file_list.values():
            if item == ext.strip():
                number += 1
        print(f'{ext.strip()} : {number}')


# walker('/home', ['.pdf'])
# walker('/home/dmytro/Downloads', '.pdf, .jpg, .txt, .py')
walker('/home/dmytro/Downloads', ('.pdf', '.jpg', '.txt', '.py'))
# ---------------
