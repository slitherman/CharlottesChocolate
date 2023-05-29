from socket import *
import random
import json
from time import sleep

PORT = 14014
PRODUCT_NO = 8013
SERVER_NAME = "255.255.255.255"
CLIENT_SOCKET = socket(AF_INET,SOCK_DGRAM)
CLIENT_SOCKET.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
while True:
    sold = random.randint(1, 10)
    InStock = random.randint(1, 1000)
    price = random.randint(10, 155)

    saleInfo = {"Product_No": PRODUCT_NO, "Amounts_Sold:": sold,"price": price, "Stock": InStock, }
    saleJson = json.dumps(saleInfo)
    CLIENT_SOCKET.sendto(saleJson.encode(), (SERVER_NAME, PORT))
    print(saleInfo)
    sleep(10)
