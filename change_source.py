#! /usr/bin/python3
import sys
import os

list_path = '/etc/apt/sources.list.d/additional-repositories.list'

if sys.argv[1] == "uh":
	http_repo = 'http://ubuntu.uh.cu/ubuntu'
	print('Using source ' + http_repo)
	os.system('echo deb ' + http_repo + ' xenial main restricted universe multiverse > ' + list_path)
	os.system('echo deb ' + http_repo + ' xenial-updates main restricted universe multiverse >> ' + list_path)
elif sys.argv[1] == "hdd":
	local_repo = 'http://0.0.0.0:8000/'
	print('Using source ' + local_repo)
	os.system('echo deb ' + local_repo + ' xenial main restricted universe multiverse > ' + list_path)
	os.system('echo deb ' + local_repo + ' xenial-updates main restricted universe multiverse >> ' + list_path)
elif sys.argv[1] == "net":
	net_repo = 'http://archive.ubuntu.com/ubuntu'
	print('Using source ' + net_repo)
	os.system('echo deb ' + net_repo + ' xenial main restricted universe multiverse > ' + list_path)
	os.system('echo deb ' + net_repo + ' xenial-updates main restricted universe multiverse >> ' + list_path)
os.system('apt update')
