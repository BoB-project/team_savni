#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import subprocess

def bash_command(cmd):
	subprocess.Popen(cmd, shell=True, executable='/bin/bash')

##################################2
def usage():
	print """Usage : ./file [option]

[Option]
 -e	[Firmware Path]		: Extract Firmware
 -f [file extension]	: Find all extension
 -t [Find Function]		: getenv Function, Find argument "QUERY_STRING" on Address
 -c [Check File]		: Check strip,Endian,Achitecture
 -p [Parsing Parameter] : Parsing Parameter in path
	 """
	sys.exit(0)
##################################
#Component

def extract():
	if os.path.isdir("fmk"):
		os.system("rm -rf ./fmk")
		os.system("./extract-firmware.sh %s" % path)
	else:
		os.system("./extract-firmware.sh %s" % path)


def find():
	os.system("find -name '*.%s'" % path)

def main():
	try :
		option = sys.argv[1]
	except :
		print("file.py [-Option]")
		sys.exit(1)

	if option in "-h":
		usage()

	elif option in "-e":
		global path

		path = sys.argv[2]
		extract()

	elif option in "-f":
		path = sys.argv[2]
		find()

	elif option in "-t":
		path = sys.argv[2]
		#cmd = "gdb -q %s <<< \"find &getenv,+99999999,\"QUERY_STRING\"\"" % path
		cmd = "gdb -q %s <<< 'find &getenv,+99999999,\"QUERY_STRING\"'" % path
		print "\n"
		bash_command(cmd)
	elif option in "-c":
		path = sys.argv[2]
		x = subprocess.check_output(['file',path]).split()
		
		if "not" in x:
			print "it is not stripped file!"
		else:
			print "stripped"
		if "LSB" in x:
			print "Little Endian"
		else:
			print "Big Endian"
		if "ARM," in x:
			print "ARM"
		elif "MIPS," in x:
			print "MIPS"
		else:
			print "else Achitecture"
	elif option in "-p":
		path = sys.argv[2]
		parsing = os.system("strings %s | grep \"URL=\" > result.txt" % path)



	else :
		usage()
main()
