
import os
import sys
import shutil

def x64(o, b):
    os.environ['OCFLAGS'] = os.environ['CFLAGS']
    del os.environ['CFLAGS']

def x64r(o, b):
    os.environ['CFLAGS'] = os.environ['OCFLAGS']

def p(o, b):
    if sys.platform.startswith('win'):
        tmp = o['compile-directory'] 
        dest = o['location'] 
        cwd = os.getcwd()
        bin = os.path.join(dest, 'bin')
        lib = os.path.join(dest, 'lib')
        include = os.path.join(dest, 'include')
        os.environ['INCLUDE_PATH'] = include
        os.environ['LIBRARY_PATH'] = lib
        for d in bin, include, lib:
            if not os.path.exists(d):
                os.makedirs(d)
        os.chdir(tmp)
        try:
            os.system('make -fwin32/Makefile.gcc install')
        except:
            os.chdir(cwd)
        os.chdir(cwd)
        dll = 'zlib1.dll'
        shutil.copy(os.path.join(tmp, dll), os.path.join(lib, dll))
        for f in os.listdir(lib):
            shutil.copy(os.path.join(lib,f),os.path.join(bin,f))
        
        
        