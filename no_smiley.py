#--------------------------------------------------------------
# Jahus
#----------------------------------------------
# 2015-03-24
#
# NO_SMILEY
# > Prevents user to write smileys
#----------------------------------------------
# :: Known bugs:
# -        pyHook - Issue #2: Problem with accents
#                             (French local)
#          Learn more on: sourceforge.net/p/pyhook/bugs/2/
#--------------------------------------------------------------
#
# INFORMATION
_name_ = "No_Smiley"
_version_ = "No_Smiley 0.1.0 alpha"
#
# PARAMETERS
# dict of 'first_char': [possible_second_chars]
smileys = {
	':' : ['-', ')', '(', 'p', 'P', 'd', 'D', 'o', 'O'], 
	';' : ['-', ')'], 
	'>' : ['.', '_', '<']
	}
#
# LOADING
import os, sys, threading
def quit(reason = None):
	print("Exitting... REASON: %s" % reason)
	exit(1)
try:
	import pythoncom
except:
	quit("ERROR: Package not found: pythoncom")
try:
	import pyHook
except:
	quit("ERROR: Package not found: pyHook")
try:
	import win32event
except:
	quit("ERROR: Package not found: win32event")
try:
	import win32api
except:
	quit("ERROR: Package not found: win32api")
try:
	import winerror
except:
	quit("ERROR: Package not found: winerror")
#
# Verify existing instance
def instance_unicity():
	mutex = win32event.CreateMutex(None, 1, "mutex_var_xboz")
	if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
		mutext = None
		print("ERROR: Multiple instance not allowed!")
		quit("* test_instance(): Another instance has been detected. Quit requested.")
instance_unicity()
#
# Hide console
def hide_console():
	import win32console, win32gui
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window, 0)
	return True
print("Hiding console...")
hide_console()
#
# HOOK
print("Hooking...")
window_last = None
key_last = None
def key_press(event):
	global window_last
	global key_last
	window_current = event.WindowName
	if window_current != window_last:
		window_last = window_current
	# Grabbing event properties
	event_descr = {
		'MessageName': event.MessageName, 
		'Message': event.Message, 
		'Time': event.Time, 
		'Window': event.Window, 
		'WindowName': event.WindowName, 
		'Ascii': event.Ascii, 
		'Key': event.Key, 
		'KeyID': event.KeyID, 
		'ScanCode': event.ScanCode, 
		'Extended': event.Extended, 
		'Injected': event.Injected, 
		'Alt': event.Alt, 
		'Transition': event.Transition, 
		}
	key_ascii = chr(event_descr.get("Ascii"))
	key_name = event_descr.get("Key")
	if key_last in smileys:
		if key_ascii in smileys.get(key_last):
			print("Smiley starting with %s%s detected!" % (key_last, key_ascii))
			return False
		else:
			if key_name not in ["Rshift", "Lshift"]:
				key_last = key_ascii
			return True
	else:
		if key_name not in ["Rshift", "Lshift"]:
			key_last = key_ascii
		return True
#
hook_mgr = pyHook.HookManager()
hook_mgr.KeyDown = key_press
hook_mgr.HookKeyboard()
pythoncom.PumpMessages()
#
print("EOF") # should never happen :D