import time
import random

def key_generator():
        
        random.seed(time.time())
        key = random.randint(0, 256)
        
        return key

def vernam(text, key):
        
        text = str(text)
        text = text.replace(' ','')
        ciphertext = ''
        for x in range(len(text)):
                
                simb = ord(text[x])
                simb = (simb + key)
                ciphertext += chr(simb)
                
        return ciphertext
while True:
        mode = input('(en)crypt or (de)crypt? ')

        if (mode == 'en'):
        
                plaintext = input('text: ')
                in_key = input('key: ')
        
                try:
                        in_key = int(in_key)
                except ValueError:
                        in_key = key_generator()
                        print('key= %s' % in_key)
                
                in_key = int(in_key)
                print(vernam(plaintext, in_key))
        
        elif (mode == 'de'):
        
                ciphertext = input('ciphertext: ')
                in_key = input('key: ')
        
                try:
                        in_key = int(in_key)
                except ValueError:
                        in_key = key_generator()
                        print('key= %s' % in_key)
                
                in_key = int(in_key)
                in_key = (-1) * in_key
                print(vernam(ciphertext, in_key))
        
        else:
        
                print('wrong cmd')
