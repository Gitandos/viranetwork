import socket
from time import sleep
from random import randint

class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 8888))
        self.server.listen(4)

        print("Server Started!\n\n")

        self.handleClients(server=self.server)

    def generateToken(self):
        return randint(100000, 1000000)

    def returnStatusCode(self, code: int):
        if code == 777:
            return "HTTP/1.1 777 Vira-Error\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode()
        
        else:
            return f"HTTP/1.1 {code}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode()

    def handleClients(self, server):
        while True:
            client, address = server.accept()
            data = client.recv(4096).decode()

            if client:
                print(f"Client: {address[0]}:{address[1]}")
                print(data)
                self.sendData(client=client, data=data, address=address)

    def sendData(self, client, address, data):
        output = ""
        with open("index.html", "r") as content:
            htmlData = content.readlines()
            
            for data in htmlData:
                output += data.strip() + "\n"
            
            #client.send(self.returnStatusCode(200) + "wait for response\n".encode())
            #print("press enter to render page")
            #input()
            client.send(self.returnStatusCode(200) + output.encode())

            client.close()
        #client.send(self.returnStatusCode(code=777) + f"Hello, Your token: {self.generateToken()}".encode())

if __name__ == "__main__":
    Server()