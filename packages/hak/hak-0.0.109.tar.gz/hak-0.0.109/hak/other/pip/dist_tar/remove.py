from os.path import exists

from hak.one.directory.make import f as mkdir
from hak.one.directory.empty import f as empty_directory
from hak.one.directory.remove import f as rmdirie
from hak.one.file.save import f as save
from hak.pf import f as pf

from copy import deepcopy

def f(x):
  x = deepcopy(x)
  root = x['root'] if 'root' in x else '.'
  return empty_directory(root)

def up():
  temp_root = './_dist_tars_remove'
  filename = f'{temp_root}/junk.tar'
  x = {'filename': filename, 'root': temp_root}
  mkdir(temp_root)
  save(filename, 'junk')
  return x

dn = lambda x: rmdirie(x['root'])

def t():
  x = up()
  f(x)
  if exists(x['filename']): return pf(f'exists({x["filename"]})')
  dn(x)
  if exists(x["root"]): return pf(f'exists({x["root"]})')
  return True
