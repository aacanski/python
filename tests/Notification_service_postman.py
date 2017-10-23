import json
import requests
import pytest

payload = "{\n\t\"username\": \"admin@htecgroup.com\",\n\t\"password\": \"#Asd123\"\n}"
headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW5AaHRlY2dyb3VwLmNvbTojQXNkMTIz",
    'cache-control': "no-cache",
    'postman-token': "3ae9f0e5-da69-57a3-7780-a230ff4af2c3"
    }

class TestClass:
    # test: url POST method 
    def testPostNotificationservice(url):
        response = requests.post('http://localhost:8083')
        print(response.text)
    # test: status notification service  
    def testStatusNotificationStatusCode(data):
        response = requests.post(url="http://localhost:8083/orders/orders/{orderId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /error POST method
    def testErrorNotificationservice(url):
        response = requests.post('http://localhost:8083/error')
        print(response.text)
    # test:  Mapped "{[/error],produces=[text/html]}"
    def testErrorNotificationserviceStatusCode(data):
        response = requests.post(url="http://localhost:8083/error", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /** POST method
    def testUrlPostNotificationservice(url):
        response = requests.post('http://localhost:8083/**')
        print(response.text)
    # test:  Mapped URL path [/**]
    def testUrlPostNotificationserviceStatusCode(data):
        response = requests.post(url="http://localhost:8083/**", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
            #assert_true(response.ok)







