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
    def testAuthUIservice(url):
        response = requests.post('http://localhost:8080/auth')
        print(response.text)
    # test: Mapped "{[/auth],methods=[POST],consumes=[application/json]}"
    def testAuthUIserviceStatusCode(data):
        response = requests.post(url="http://localhost:8080/auth", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url POST method 
    def testEmailConfirmationUUIDUIServiceservice(url):
        response = requests.post('http://localhost:8080/email/confirmation/{uuid}')
        print(response.text)
    # test: Mapped "{[/email/confirmation/{uuid}]}"
    def testEmailConfirmationUUIDUIServiceStatusCode(data):
        response = requests.post(url="http://localhost:8080/email/confirmation/{uuid}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testOrdersUIservice(url):
        response = requests.get('http://localhost:8080/orders')
        print(response.text)
    # test: Mapped "{[/orders],methods=[GET]}"
    def testOrdersUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/orders", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testPasswordResetUIservice(url):
        response = requests.put('http://localhost:8080/password/reset')
        print(response.text)
    # test: Mapped "{[/password/reset],methods=[PUT]}"
    def testPasswordResetUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/password/reset", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testPasswordFinishResetUIservice(url):
        response = requests.put('http://localhost:8080/password/finish-reset')
        print(response.text)
    # test: Mapped "{[/password/finish-reset],methods=[PUT]}"
    def testPasswordFinishResetUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/password/finish-reset", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testRolesGetUIservice(url):
        response = requests.get('http://localhost:8080/roles')
        print(response.text)
    # test:Mapped "{[/roles],methods=[GET]}"
    def testRolesGetUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/roles", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testRolesNameUIservice(url):
        response = requests.get('http://localhost:8080/roles/{name}')
        print(response.text)
    # test: Mapped "{[/roles/{name}],methods=[GET]}"
    def testRolesNameUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/roles/{name}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url POST method 
    def testRolesPostUIservice(url):
        response = requests.post('http://localhost:8080/roles')
        print(response.text)
    # test: Mapped "{[/roles],methods=[POST],produces=[application/json;charset=UTF-8]}"
    def testRolesPostUIserviceStatusCode(data):
        response = requests.post(url="http://localhost:8080/roles", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testUIservice(url):
        response = requests.get('http://localhost:8080/')
        print(response.text)
    # test: Mapped "{[/],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testShipmentsPutUIservice(url):
        response = requests.put('http://localhost:8080/shipments')
        print(response.text)
    # test: Mapped "{[/shipments],methods=[PUT],consumes=[application/json;charset=UTF-8],produces=[application/json;charset=UTF-8]}"
    def testShipmentsPutUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/shipments", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testShipmentsGetUIservice(url):
        response = requests.get('http://localhost:8080/shipments')
        print(response.text)
    # test: Mapped Mapped "{[/shipments],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testShipmentsGetUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/shipments", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testUsersMeUIservice(url):
        response = requests.get('http://localhost:8080/users/me')
        print(response.text)
    # test: Mapped "{[/users/me],methods=[GET]}"
    def testUsersMeUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/users/me", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testUserUsernameUsernameUIservice(url):
        response = requests.get('http://localhost:8080/users/username/{username:.+}')
        print(response.text)
    # test: Mapped "{[/users/username/{username:.+}],methods=[GET]}"
    def testUserUsernameUsernameUIserviceStatusCode(data):
        response = requests.get(url="http://localhost:8080/users/username/{username:.+}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url POST method 
    def testUsersPostUIservice(url):
        response = requests.post('http://localhost:8080/users')
        print(response.text)
    # test: Mapped "{[/users],methods=[POST],produces=[application/json;charset=UTF-8]}" 
    def testUsersPostUIserviceStatusCode(data):
        response = requests.post(url="http://localhost:8080/users", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testUsersPutUIservice(url):
        response = requests.put('http://localhost:8080/users')
        print(response.text)
    # test: Mapped "{[/users],methods=[PUT]}"
    def testUsersPutUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/users", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testUserPasswordUIservice(url):
        response = requests.put('http://localhost:8080/users/password')
        print(response.text)
    # test: Mapped "{[/users/password],methods=[PUT]}"
    def testUserPasswordUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/users/password", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url PUT method 
    def testUsersEmailUIservice(url):
        response = requests.put('http://localhost:8080/users/email')
        print(response.text)
    # test: Mapped "{[/users/email],methods=[PUT]}"
    def testUsersEmailUIserviceStatusCode(data):
        response = requests.put(url="http://localhost:8080/users/email", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code






