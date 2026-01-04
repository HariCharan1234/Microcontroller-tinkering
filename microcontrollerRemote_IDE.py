import socket as sock
import time as tm


class connect:
    def __init__(self, ip):
        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.connection = self.s.connect((ip, 80))

    def transmit(self, transferFile, locationFile, mode = "a"):
        self.x = 0
    
        with open(transferFile, "r") as f:
            self.text = f.read()
        interLen = int(len(self.text.split("\n")))-1
        self.s.send(bytes(f"Writeio{locationFile},{interLen}", 'utf-8'))
        tm.sleep(2)
        print("Sending")
        self.l = int(len(self.text.split("\n")))
        for i in range(self.l):
            curMsg = self.text.split("\n")[self.x]
            #print(curMsg)
            self.s.send(bytes(f"{curMsg}\n", 'utf-8'))
            self.x = self.x + 1
            print(f"{curMsg}\n")
        tm.sleep(0.5)
        self.s.send(bytes("end", 'utf-8'))
        print("Sent")
    def default(self):
        self.s.send(bytes("default", 'utf-8'))

    def breaker(self):
        self.s.send(bytes("stop", 'utf-8'))
    
    def Close(self):
        self.s.close()
    
    def readFile(self, file):
        MSG = ""
        self.s.send(bytes(f"send({file})", 'utf-8'))
        while True:
            self.mess = self.s.recv(1024).decode('utf-8')
            if self.mess != "end":
                MSG = str(f"{MSG}{self.mess}")
            else:
                break
        print(MSG)

            
    def runFile(self, path):
        self.s.send(bytes(f"Run({path})", 'utf-8'))
        
        self.mess = self.s.recv()