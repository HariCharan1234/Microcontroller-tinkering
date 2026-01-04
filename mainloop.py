import machine as m
import time as tm
                    
class initComms:
    global MSG
    def __init__(self, SSID, password, ipConfig):
        m.Pin(2, m.Pin.OUT).off()
        import network as intnet
        import socket
        net = intnet.WLAN(intnet.STA_IF)
        net.active(1)
        net.connect(SSID, password)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.ifconfig(ipConfig)
        print(net.ifconfig())
        self.s.bind(("", 80))
        self.s.listen(1)
        def writeFil(filepath, content):
            with open(filepath, "w+") as f:
                 f.write(content)
        while True:
            m.Pin(2, m.Pin.OUT).on()
            tm.sleep(0.5)
            m.Pin(2, m.Pin.OUT).off()
            client, addr = self.s.accept()
            m.Pin(2, m.Pin.OUT).on()
            tm.sleep(0.5)
            m.Pin(2, m.Pin.OUT).off()
            tm.sleep(2)
            msg = client.recv(1024).decode('utf-8')
            print(msg)
            if msg.split("io")[0] == "Write":
                print("Write mode acitvated")
                MSG = ""
                m.Pin(2, m.Pin.OUT).on()
                tm.sleep(0.25)
                m.Pin(2, m.Pin.OUT).off()
                tm.sleep(0.25)
                m.Pin(2, m.Pin.OUT).on()
                tm.sleep(0.25)
                m.Pin(2, m.Pin.OUT).off()
                tm.sleep(0.25)
                m.Pin(2, m.Pin.OUT).on()
                tm.sleep(0.25)
                m.Pin(2, m.Pin.OUT).off()
                tm.sleep(0.25)
                self.path = msg.split("io")[1].split(",")[0]
                self.iterLen = msg.split("io")[1].split(",")[1]
                print(f"{self.path}, {self.iterLen}")
                while True:
                    self.iterMsg = client.recv(1024).decode('utf-8')
                    if self.iterMsg != "end":
                        print(self.iterMsg)
                        MSG = MSG + str(self.iterMsg + "\n")
                        #print(f"\n\n{MSG}) 
                    else:
                        print(self.iterMsg)
                        print("Write mode deactivated")
                        break
                    
                writeFil(self.path, MSG)
                print(f"\n\n{MSG}")
            
            elif self.msg == "stop":
            
            
                m.Pin(2, m.Pin.OUT).on()
                break
                tm.sleep(1)
            elif self.msg[0:5] == "send(":
                path = self.msg.replace("send(", "").replace(")", "")
                with open(path) as f:
                    self.text = f.read()
                client.send(bytes(f"Transmitting,{len(self.text.split("\n"))-1},", 'utf-8'))
                tm.sleep(0.5)
                x = 0
                for i in range(len(self.text.split("\n"))-1):
                    self.itrmsg = self.text.split("\n")[x]
                    client.send(bytes(self.itmsg, 'uft-8'))
                    tm.sleep(0.5)
                    x = x + 1
