
from socket import *
import json
import requests
from time import sleep

API_URL = "https://charlottesstockapi.azurewebsites.net/api/Chocolate"
PORT = 14014
PRODUCT_NO = 8013
SERVER_ADDRESS = ("", PORT)
SERVER_SOCKET = socket(AF_INET,SOCK_DGRAM)
SERVER_SOCKET.bind(SERVER_ADDRESS)

print("The server is ready")
while True:
    data, addr = SERVER_SOCKET.recvfrom(4080) # Receive UDP packet
    received_data = data.decode()
    sale_info = json.loads(received_data) # Parse the received JSON data
    print("LOGGING SALE_INFO")
    print(sale_info)
    print("AFTER SALE_INFO LOGGING")
    # Set additional properties as null
    #sale_info["chocolateType"] = None
    #sale_info["price"] = None
    #sale_info["inStock"] = None
    #print("sale received:", sale_info)
    response = requests.post(API_URL, json=  sale_info)
    print(response.status_code)
    print(response.text)
    sleep(10)
