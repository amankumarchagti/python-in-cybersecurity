import socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 1234
    s.bind((HOST,PORT))
    print("Socket connection established")


if __name__ == '__main__':
    main()