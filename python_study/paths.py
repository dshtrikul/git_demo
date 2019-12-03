import os.path
from pathlib import Path
from pprint import pprint
from os import chdir


print(os.path.exists('/aaa'))


print(Path('/dir/file.doc').name, '>>name')
print(Path('/dir/file.doc').parts, '>>parts')
print(Path('/dir/file.doc').parent, '>>parent')
print(Path('/dir/file.doc').suffix, '>>suffix')
print(Path('/dir/file.doc').is_dir(), '>>is_dir')
print(Path('/dir/file.doc').is_file(), '>>is_file (or doesnt exist)')
print(Path('/dir/file.doc').exists(), '>>exitst')
pprint(list(Path.cwd().glob('*.py')), '>>> app .py files')
print('===========================')
# make a new path, create dir, test mkdir args
print(Path(Path.cwd().joinpath('test/test')))
Path.cwd().joinpath('test/test').mkdir(parents=True, exist_ok=True)
print(Path.cwd().resolve())
print('===========================')
# use os.chdir, check
chdir(Path('test/test'))
print(Path.cwd())

