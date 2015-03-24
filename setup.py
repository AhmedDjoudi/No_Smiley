#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by: python.exe -m py2exe api.py -W api_setup.py

from distutils.core import setup
import py2exe

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

py2exe_options = dict(
    packages = [],
##    excludes = "tof_specials Tkinter".split(),
##    ignores = "dotblas gnosis.xml.pickle.parsers._cexpat mx.DateTime".split(),
##    dll_excludes = "MSVCP90.dll mswsock.dll powrprof.dll".split(),
    optimize=1,
    compressed=True, # uncompressed may or may not have a faster startup
    bundle_files=1,
    dist_dir='no_smilay_dist'
    )

setup(
	console=["no_smilay.py"],
	data_files=data_files,
	zipfile=None,
	options={"py2exe": py2exe_options}
)