#!/usr/bin/python
from os import mkdir
from shutil import copy, copytree
from time import localtime, strftime

time = strftime('%Y%m%d_%H%M', localtime())
base_dir = './archive/' + time

mkdir(base_dir)

copy('DavidLuuResume.html', base_dir + '/DavidLuuResume.html')
copytree('css', base_dir + '/css')
copytree('fonts', base_dir + '/fonts')
