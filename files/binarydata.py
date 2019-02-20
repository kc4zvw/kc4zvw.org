#!/usr/local/bin/python3
#
# $Id: binarydata.py,v 0.2 2018/10/12 02:37:30 kc4zvw Exp kc4zvw $

"""
	Copyright 2007 by Dennis Shimer
	Vr Mapping copyright Cardinal Systems, LLC

	No warranties as to safety or usability expressed or implied.
	Free to use, copy, modify, distribute with author credit.
	
	Just a lesson in binary data. Either run from a command line 3 times like
	python testbinary.py or open or paste into pyedi and execute 3 times.

"""
 
import math, os, struct

# We'll use os to test for the existence of the file, an struct to 
# interact with the binary data.
 
print()
print("TestBinary.py -- created 11:00 PM 7/10/2007")
print()
print("Revised: Thursday, October 11, 2018 at 21:44:17 PM (EDT)")
print()

FormatString = '10s2di'
ParFileName = 'testbinary.dat'

# The file by this name will show up in the directory the script is run in.

"""
	The format string tells several parts of the program what we are working with in regards to
	binary data. The format string listed above represents a 10 character string, 2 double
	precision real numbers, and an integer.  Same as before but I added the int to show by
	example. Note that it is just a string with letters representing different kinds of data.
"""

print("Bytes occupied by binary data: %d\n" % struct.calcsize(FormatString))
print()

"""
	Sometimes you need to know how many bytes to read from a file in order to get one set of
	data when multiple sets exist, a good example goes back to the coordinate file mentioned
	earlier. In order to read and process one point at a time you can only read the necessary
	bytes. the calcsize method in struct will read a format string and tell how many bytes are
	represented. You can go into a python interpreter, import struct then evaluate some single
	item format strings like the following for a float, a double, an int, and a 1 character
	string.

>>> struct.calcsize('f')
4
>>> struct.calcsize('d')
8
>>> struct.calcsize('i')
4
>>> struct.calcsize('s')
1
"""
 

def subroutine1():
	parFile = open(ParFileName, 'wb')

	# Then open it in write (create or erase) mode with a binary modifier
 
	BinaryData = struct.pack(FormatString, b'Word', .2, math.pi, 0)

	"""
		The pack method in the struct module uses the format string to process the data that
		comes next into the bytes which represent them in binary form. It is important that
		the amount and type of data following the format string match, notice I am passing
		in a string (less than 10 characters allowed, 2 real numbers and an integer.
	"""
 
	print(BinaryData)
	parFile.write(BinaryData)
	parFile.close()

	# We have a binary file and binary data so just and write and close it.
 
	print("The program will run with no existing data file")
	print()
	print("Data set to defaults.")
	print(f'{ParFileName} should now exist.')


def subroutine2():
	parFile = open(ParFileName, 'r+b')

	DataList = []

	# If it does exist open for reading + writing with binary modifier.
 
	BinaryData = parFile.read()

	"""
		This time since the file exists we are going to get the binary data right out of the
		file with a read. Since we want the whole file there is no reason to use calcsize to
		tell it how many bytes to read.
	"""

	DataList = struct.unpack(FormatString, BinaryData)

	# Going the other direction, lets use unpack to use the format string
	# to convert the binary data into a list of values.
 
	print("Data from file, note it is a list\n", DataList)

	# and print the list.
 
	parFile.seek(0, 0)

	"""
		Now assuming that there are new values that need to be used to update the parameter
		file. The first thing we need to do is go back to the beginning of the file, read up
		on seek, but this basically moves you 0 bytes from the beginning. If in the
		coordinate file example I had a data structure that require 24 bytes and wanted to
		get the 3rd value from the file I could to the 48th byte and read 24. This way you
		can read, write, and overwrite data in place within a file.
	"""
	
	print("File position after seek: ", parFile.tell())
	
	# Every open file has a tell method which gives the current position.
	
	BinaryData = struct.pack(FormatString, b'Updated', 1, 2, 3)
	parFile.write(BinaryData)

	# Same idea as above, just using the changed data (wherever it came from)
 
	print(DataList[0])

	### if DataList[0].split('\x00')[0] == b'Updated':
	if b'Updated' == b'Updated':
		print("")
		print("You have seen it all.")
		print("")
		print(f"Remove {ParFileName} to start over")
	
		"""
			There may be a better way to convert this 10 character string to what you
			normally think of as a string, but it comes back padded with the 0 bytes and
			this works simply enough. Think of it this way 'Updated\x00\x00\x00' has 3
			extra bytes, if you split on that character you get back ['Updated', '', '',
			''] of which 'Updated' is the first or [0] element. Ugly but I've never
			really look into a better way.
		"""

	else:
		print("Program run with an existing file")
		print("Data was updated run again to see change")

		# 2nd run string doesn't equal 'Updated' so print appropriate message.
 
	parFile.close() # Good form to explicitely close files.
 
if not os.path.isfile(ParFileName): # If the file doesn't exist.
	subroutine1()
else:
	subroutine2() 

print()
print("Finished.")

## End of Program
