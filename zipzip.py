import os
import sys
import time
import string
import argparse
import itertools
import zipfile
from os.path import *



def tryZipPwd(zipFile, password):
    try:
        zipFile.extractall(path='2014-06/', pwd=password.encode('utf-8'))
        print('[+] Zip File decompression success,password: %s' % (password))
        return True
    except:
        print('[-] Zip File decompression failed,password: %s' % (password))
        return False




if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Python Wordlist Generator')
    parser.add_argument('-chr', '--chars',default=None, help='characters to iterate')
    parser.add_argument('-min', '--min_length', type=int,default=1, help='minimum length of characters')
    parser.add_argument('-max', '--max_length', type=int,default=2, help='maximum length of characters')
    parser.add_argument('-f', '--zFile', type=str, help='The zip file path.')
    zFilePath = None
    try:
        options = parser.parse_args()
        zFilePath = options.zFile
        chrs=options.chars
        min_length=options.min_length
        max_length=options.max_length
        #pwdFilePath = options.pwdFile
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    if zFilePath == None:
        print(parser.parse_args(['-h']))
        exit(0)
	
    #args = parser.parse_args()
    if options.chars is None:
        options.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    #if os.path.exists(os.path.dirname(output)) == False:
        #os.makedirs(os.path.dirname(output))

    #print ('[+] Creating wordlist at `%s`...' % output)
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))

    #output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            with zipfile.ZipFile(zFilePath) as zFile:
                ok=tryZipPwd(zFile, chars.strip('\n'))
                if ok:
                    break
            #output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()
    #output.close()

    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))
