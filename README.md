# No_Smiley

## Presentation

This little Python script Prevents user from writing smileys.

## Principle

No_Smiley uses PyHook to catch key strokes on low-level and decides either to let the key get caught by a program or not. It runs in background and doesn't interract with any other programs.

## Prerequisites

* Python 2.7.8: [link to Python.org](https://www.python.org/download/releases/2.7.8/);
* PythonCOM package (you can get it as part of pyWin32: [link to SourceForge.net](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/));
* PyHook (1.5.1): [link to SourceForge.net](http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/).

## Parameters

Smileys are defined by their first character and all the possible second characters.
This can be enhanced by taking other characters into account, but it doesn't seem to be essential as you can recognize most smileys with the first two characters.

Default value:

	# :- :) :( :'( :') :p :P :d :D :o :O
	# ;- ;)
	# >.< >_< ><
    smileys = {
    	':' : ['-', "'", ')', '(', 'p', 'P', 'd', 'D', 'o', 'O'], 
    	';' : ['-', ')'], 
    	'>' : ['.', '_', '<']
    	}

## Compatibility

The scripts runs correctly on Windows NT 5.1 and earlier versions.

The scripts doesn't run on Python 3.4 as there is no PyHook package for it.

## Make EXE file

In order to make an EXE file from this script, you need to:

1. install py2exe package: http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/;
2. change the setup.py file to define `Microsoft.VC90.CRT` path;
3. launch the command `py -2.7 setup.py py2exe` on the directory where no_smiley.py is.

*Warning: Some antivirus software can prevent py2exe from creating its bundle.
If you fail to make the EXE, try deactivating your antivirus software for the duration of the process (that 10s max).*

## Known issues

* pyHook - [Issue #2: Problem with accents (French local)](sourceforge.net/p/pyhook/bugs/2/)

## Licence

- If you improve my code, I would be glad to see yours. If you don't want me to see it, there would be no problem about it;
- If you use my code, I would be glad if you credit me. If you don't want people to know your sources, there would be no problem about it.

i.e. No licence.
