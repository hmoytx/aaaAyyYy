import socket
import threading
import time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 36444))
    s.listen(20)
    timeout = 10
    socket.setdefaulttimeout(timeout)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def tcplink(sock, addr):
    print('Start download shellcode %s:%s...' % addr)
    shellcode = b'1111111' #your shellcode
    print(len(shellcode))
    while True:
        data = sock.recv(1024)
        time.sleep(3)
        sock.send(shellcode)
        sock.close()
    print('Finish %s:%s ' % addr)


if __name__ == '__main__':
    main()