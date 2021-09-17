import time
import random


def key_generator():
    random.seed(time.time())
    key = random.randint(0, 1113993)

    return key


def vernam(text, key):
    text = str(text)
    text = text.replace(' ', '')
    ciphertext = ''
    for x in range(len(text)):
        simb = ord(text[x])
        simb = (simb + key)
        ciphertext += chr(simb)

    return ciphertext


if __name__ == '__main__':
    mode = input('(en)crypt or (de)crypt or cryptoanalysis(ca)? ')

    if str.lower(mode) == 'en' or str.lower(mode) == 'encrypt':

        plaintext = input('text: ')
        in_key = input('key, int(0, 1113993) (random if not filled): ')

        try:
            in_key = int(in_key)
        except ValueError:
            in_key = key_generator()
            print('key= %s' % in_key)

        in_key = int(in_key)
        print(vernam(plaintext, in_key))

    elif str.lower(mode) == 'de' or str.lower(mode) == 'decrypt':

        ciphertext = input('ciphertext: ')
        in_key = input('key: ')

        try:
            in_key = int(in_key)
        except ValueError:
            print('key should be integer!')
            in_key = key_generator()
            print('key = %s' % in_key)

        in_key = int(in_key)
        in_key = (-1) * in_key
        print(vernam(ciphertext, in_key))

    elif str.lower(mode) == 'ca' or str.lower(mode) == 'cryptoanalysis':
        ciphertext = input('ciphertext: ')
        key = int(input('key: '))
        awaitedtext = vernam(ciphertext, -1 * key)
        for i in range(1113994):
            possible_key = -1 * i
            if awaitedtext == vernam(ciphertext, possible_key):
                print('found your text in %d iterations' % i)
                print(vernam(ciphertext, possible_key))
                print('(without key it wouldn\'t be possible)')
                break
            else:
                # print('possible text: %s' % vernam(ciphertext, possible_key).encode('utf-16', 'surrogatepass').decode('utf-16', 'ignore'))
                pass

    else:
        print('wrong cmd')
