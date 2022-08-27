#Dependencies - pip3 install paramiko
import paramiko
def main():
    ip = '0.0.0.0'
    username = 'test'
    password = 'test@123'
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    client.connect(ip, username=username,password=password)
    print(client)


if __name__ == "__main__":
    main()
