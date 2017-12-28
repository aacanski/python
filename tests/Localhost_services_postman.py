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
    # test: url POST method 
    def testAuthUserservice(url):
        response = requests.post('http://localhost:8081/auth')
        print(response.text)
    # test: Mapped "{[/auth],methods=[POST],consumes=[application/json]}"
    def testAuthUserserviceStatusCode(data):
        response = requests.post(url="http://localhost:8081/auth", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url companies GET method 
    def testCompaniesUserservice(url):
        response = requests.get('http://localhost:8081/companies/')
        print(response.text)
    # test: Mapped "{[/companies/],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url companies/{companyID} GET method 
    def testCompaniesIdUserservice(url):
        response = requests.get('http://localhost:8081/companies/{companyId}')
        print(response.text)
    # test: Mapped "{[/companies/{companyId}],methods=[GET],produces=[application/json;charset=UTF-8]}" 
    def testCompaniesIdUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/{companyId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/name/{companyName} GET method 
    def testCompaniesNameUserservice(url):
        response = requests.get('http://localhost:8081/companies/name/{companyName}')
        print(response.text)
    # test: Mapped "{[/companies/name/{companyName}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesNameUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/name/{companyName}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/vat/{companyVatNumber} GET method 
    def testCompaniesVatUserservice(url):
        response = requests.get('http://localhost:8081/companies/vat/{companyVatNumber}')
        print(response.text)
    # test: Mapped "{[/companies/vat/{companyVatNumber}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesVatUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/vat/{companyVatNumber}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/ PUT method
    def testCompaniesPutUserservice(url):
        response = requests.put('http://localhost:8081/companies/')
        print(response.text)
    # test: Mapped "{[/companies/],methods=[PUT],consumes=[application/json],produces=[application/json;charset=UTF-8]}"
    def testCompaniesPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/companies/", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code    
    # test: url /companies/edit PUT method
    def testCompaniesEditPutUserservice(url):
        response = requests.put('http://localhost:8081/companies/edit')
        print(response.text)
    # test: Mapped "{[/companies/edit],methods=[PUT],consumes=[application/json],produces=[application/json;charset=UTF-8]}"
    def testCompaniesEditPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/companies/edit", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/rates/{companyIds} GET method
    def testCompaniesRatesGetUserservice(url):
        response = requests.get('http://localhost:8081/companies/rates/{companyIds}')
        print(response.text)
    # test: Mapped "{[/companies/rates/{companyIds}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesRatesGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/rates/{companyIds}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/blacklist POST method
    def testCompaniesBlackListPostUserservice(url):
        response = requests.post('http://localhost:8081/companies/blacklist')
        print(response.text)
    # test:  Mapped "{[/companies/blacklist],methods=[POST],consumes=[application/json;charset=UTF-8],produces=[application/json;charset=UTF-8]}"
    def testCompaniesBlackListPostUserserviceStatusCode(data):
        response = requests.post(url="http://localhost:8081/companies/blacklist", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/blacklist GET method
    def testCompaniesBlackListGetUserservice(url):
        response = requests.get('http://localhost:8081/companies/blacklist')
        print(response.text)
    # test:  Mapped "{[/companies/blacklist],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesBlackListGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/blacklist", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/blacklist DELETE method
    def testCompaniesBlackListDeleteUserservice(url):
        response = requests.delete('http://localhost:8081/companies/blacklist')
        print(response.text)
    # test:  Mapped "{[/companies/blacklist],methods=[DELETE],produces=[application/json;charset=UTF-8]}"
    def testCompaniesBlackListDeleteUserserviceStatusCode(data):
        response = requests.delete(url="http://localhost:8081/companies/blacklist", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/trading/{companyId} GET method
    def testCompaniesTradingIdGetUserservice(url):
        response = requests.get('http://localhost:8081/companies/trading/{companyId}')
        print(response.text)
    # test:  Mapped "{[/companies/trading/{companyId}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testCompaniesTradingIdGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/companies/trading/{companyId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /email/confirmation/{uuid} GET method
    def testEmailConfirmationUUIDGetUserservice(url):
        response = requests.get('http://localhost:8081/email/confirmation/{uuid}')
        print(response.text)
    # test:  Mapped "{[/email/confirmation/{uuid}],methods=[GET]}"
    def testEmailConfirmationUUIDGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/email/confirmation/{uuid}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /password/reset PUT method
    def testPasswordResetPutUserservice(url):
        response = requests.put('http://localhost:8081/password/reset')
        print(response.text)
    # test:  Mapped "{[/password/reset],methods=[PUT]}"
    def testPasswordResetPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/password/reset", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /password/finish-reset PUT method
    def testPasswordFinishedResetPutUserservice(url):
        response = requests.put('http://localhost:8081/password/finish-reset')
        print(response.text)
    # test:  Mapped "{[/password/finish-reset],methods=[PUT]}"
    def testPasswordFinishedResetPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/password/finish-reset", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /reports/issue] POST method
    def testReportsIssuePostUserservice(url):
        response = requests.post('http://localhost:8081/reports/issue]')
        print(response.text)
    # test:  Mapped "{[/reports/issue],methods=[POST],consumes=[application/json;charset=UTF-8],produces=[application/json;charset=UTF-8]}"
    def testReportsIssuePostUserserviceStatusCode(data):
        response = requests.post(url="http://localhost:8081/reports/issue]", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /roles GET method
    def testRolesGetUserservice(url):
        response = requests.get('http://localhost:8081/roles')
        print(response.text)
    # test:  Mapped "{[/roles],methods=[GET]}"
    def testRolesGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/roles", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /roles POST method
    def testRolesPostUserservice(url):
        response = requests.post('http://localhost:8081/roles')
        print(response.text)
    # test:  Mapped "{[/roles],methods=[POST],produces=[application/json;charset=UTF-8]}"
    def testRolesPostUserserviceStatusCode(data):
        response = requests.post(url="http://localhost:8081/roles", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /roles/{name} GET method
    def testRolesNameGetUserservice(url):
        response = requests.get('http://localhost:8081/companies/trading/{companyId}')
        print(response.text)
    # test:  Mapped "{[/roles/{name}],methods=[GET]}"
    def testRolesNameGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/roles/{name}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users POST method
    def testUsersPostUserservice(url):
        response = requests.post('http://localhost:8081/users')
        print(response.text)
    # test:  Mapped "{[/users],methods=[POST],produces=[application/json;charset=UTF-8]}"
    def testUsersPostUserserviceStatusCode(data):
        response = requests.post(url="http://localhost:8081/users", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/{id} GET method
    def testUsersIDGetUserservice(url):
        response = requests.get('http://localhost:8081/users/{id}')
        print(response.text)
    # test:  Mapped "{[/users/{id}],methods=[GET],produces=[application/json;charset=UTF-8]}" 
    def testUsersIDGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/users/{id}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/username/{username:.+} GET method
    def testUsersUsernameUsernameGetUserservice(url):
        response = requests.get('http://localhost:8081/users/username/{username:.+}')
        print(response.text)
    # test:  Mapped "{[/users/username/{username:.+}],methods=[GET]}"
    def testUsersUsernameUsernameGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/users/username/{username:.+}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/me GET method
    def testUsersMeGetUserservice(url):
        response = requests.get('http://localhost:8081/users/me')
        print(response.text)
    # test:  Mapped "{[/users/me],methods=[GET]}"
    def testUsersMeGetUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/users/me", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users PUT method
    def testUsersPutUserservice(url):
        response = requests.get('http://localhost:8081/users')
        print(response.text)
    # test:  Mapped "{[/users],methods=[PUT]}"
    def testUsersPutUserserviceStatusCode(data):
        response = requests.get(url="http://localhost:8081/users", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/password PUT method
    def testUsersPasswordPutUserservice(url):
        response = requests.put('http://localhost:8081/users/password')
        print(response.text)
    # test:  Mapped "{[/users/password],methods=[PUT]}"
    def testUsersPasswordPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/users/password", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/email PUT method
    def testUsersEmailPutUserservice(url):
        response = requests.put('http://localhost:8081/users/email')
        print(response.text)
    # test:  Mapped "{[/users/email],methods=[PUT]}"
    def testUsersEmailPutUserserviceStatusCode(data):
        response = requests.put(url="http://localhost:8081/users/email", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url GET method 
    def testOrdersOrdersOrderIDGetTradingservice(url):
        response = requests.get('http://localhost:8084/orders/orders/{orderId}')
        print(response.text)
    # test: Mapped "{[/orders/orders/{orderId}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testOrdersOrdersOrderIDGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/orders/orders/{orderId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /orders GET method 
    def testOrdersGetTradingservice(url):
        response = requests.get('http://localhost:8084/orders')
        print(response.text)
    # test: Mapped "{[/orders],methods=[GET]}"
    def testOrdersGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/orders", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /orders/orders PUT method 
    def testOrdersOrdersPutTradingservice(url):
        response = requests.put('http://localhost:8084/orders/orders')
        print(response.text)
    # test: Mapped "{[/orders/orders],methods=[PUT],consumes=[application/json],produces=[application/json;charset=UTF-8]}"
    def testOrdersOrdersPutTradingserviceStatusCode(data):
        response = requests.put(url="http://localhost:8084/orders/orders", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /matches/best-match/{orderId} GET method 
    def testMatchesBestMatchOrderIDGetTradingservice(url):
        response = requests.get('http://localhost:8084/matches/best-match/{orderId}')
        print(response.text)
    # test: Mapped "{[/matches/best-match/{orderId}],methods=[GET],consumes=[application/json;charset=UTF-8],produces=[application/json;charset=UTF-8]}"
    def testMatchesBestMatchOrderIDGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/matches/best-match/{orderId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /matches/{orderId} GET method 
    def testMatchesOrderIDGetTradingservice(url):
        response = requests.get('http://localhost:8084/matches/{orderId}')
        print(response.text)
    # test: Mapped "{[/matches/{orderId}],methods=[GET],consumes=[application/json;charset=UTF-8],produces=[application/json;charset=UTF-8]}"
    def testMatchesOrderIDGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/matches/{orderId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /shipments/{shipmentId} GET method
    def testShipmentsShipmentsIDGetTradingservice(url):
        response = requests.put('http://localhost:8084/shipments/{shipmentId}')
        print(response.text)
    # test: Mapped "{[/shipments/{shipmentId}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testShipmentsShipmentsIDGetTradingserviceStatusCode(data):
        response = requests.put(url="http://localhost:8084/shipments/{shipmentId}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code 
    # test: url /shipments PUT method
    def testShipmentsPutTradingservice(url):
        response = requests.put('http://localhost:8084/shipments')
        print(response.text)
    # test: Mapped "{[/shipments],methods=[PUT],consumes=[application/json],produces=[application/json;charset=UTF-8]}"
    def testShipmentsPutTradingserviceStatusCode(data):
        response = requests.put(url="http://localhost:8084/shipments", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/rates/{companyIds} GET method
    def testDistanceOriginIDDestinationIDGetTradingservice(url):
        response = requests.get('http://localhost:8084/distance/{originID}/{destinationID}')
        print(response.text)
    # test: Mapped "{[/distance/{originID}/{destinationID}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testDistanceOriginIDDestinationIDGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/distance/{originID}/{destinationID}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /companies/blacklist GET method
    def testShipmentsIvanOrderIDGetTradingservice(url):
        response = requests.get('http://localhost:8084/companies/blacklist')
        print(response.text)
    # test:  Mapped "{[/shipments/ivan/{orderID}],methods=[GET],produces=[application/json;charset=UTF-8]}"
    def testShipmentsIvanOrderIDGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/companies/blacklist", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /swagger-resources/configuration/ui POST method
    def testSwaggerResuorcesConfigurationUIPostTradingservice(url):
        response = requests.post('http://localhost:8084/swagger-resources/configuration/ui')
        print(response.text)
    # test:  Mapped "{[/swagger-resources/configuration/ui]}"
    def testSwaggerResuorcesConfigurationUIPostTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/swagger-resources/configuration/ui", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /swagger-resources POST method
    def testSwaggerResuorcesTradingservice(url):
        response = requests.post('http://localhost:8084/swagger-resources')
        print(response.text)
    # test:  Mapped "{[/swagger-resources]}"
    def testSwaggerResuorcesTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/swagger-resources", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /swagger-resources/configuration/security POST method
    def testSwaggerResuorcesConfigurationSecurityTradingservice(url):
        response = requests.post('http://localhost:8084/swagger-resources/configuration/security')
        print(response.text)
    # test:  Mapped "{[/swagger-resources/configuration/security]}"
    def testSwaggerResuorcesConfigurationSecurityTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/swagger-resources/configuration/security", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /error POST method
    def testErrorTradingservice(url):
        response = requests.post('http://localhost:8084/error')
        print(response.text)
    # test:  Mapped "{[/error],produces=[text/html]}"
    def testErrorTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/error", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /env/{name:.*} GET method
    def testEnvNameGetTradingservice(url):
        response = requests.get('http://localhost:8084/env/{name:.*}')
        print(response.text)
    # test:  Mapped "{[/env/{name:.*}],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testEnvNameGetTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/env/{name:.*}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /env GET method
    def testEnvTradingservice(url):
        response = requests.get('http://localhost:8084/env]')
        print(response.text)
    # test:  Mapped "{[/env || /env.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testEnvTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/env]", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /env.json GET method
    def testEnvJSONTradingservice(url):
        response = requests.get('http://localhost:8084/env.json')
        print(response.text)
    # test:  Mapped "{[/env || /env.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testEnvJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/env.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /trace GET method
    def testTraceTradingservice(url):
        response = requests.get('http://localhost:8084/trace')
        print(response.text)
    # test:  Mapped "{[/trace || /trace.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testTraceTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/trace", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /trace.json GET method
    def testTraceJSONTradingservice(url):
        response = requests.get('http://localhost:8084/trace.json')
        print(response.text)
    # test:  Mapped "{[/trace || /trace.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testTraceJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/trace.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /mappings GET method
    def testMappingsTradingservice(url):
        response = requests.get('http://localhost:8084/mappings')
        print(response.text)
    # test:  Mapped "{[/mappings || /mappings.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testMappingsTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/mappings", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /mappings.json GET method
    def testMappingsJSONTradingservice(url):
        response = requests.get('http://localhost:8084/mappings.json')
        print(response.text)
    # test:  Mapped "{[/mappings || /mappings.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testMappingsJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/mappings.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /beans GET method
    def testBeansTradingservice(url):
        response = requests.get('http://localhost:8084/beans')
        print(response.text)
    # test:  Mapped "{[/beans || /beans.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testBeansTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/beans", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /beans.json GET method
    def testBeansJSONTradingservice(url):
        response = requests.get('http://localhost:8084/beans.json')
        print(response.text)
    # test:  Mapped "{[/beans || /beans.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testBeansJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/beans.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /metrics/{name:.*} GET method
    def testMetricsNameGetTradingservice(url):
        response = requests.get('http://localhost:8084/metrics/{name:.*}')
        print(response.text)
    # test:  Mapped "{[/metrics/{name:.*}],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testMetricsNameTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/metrics/{name:.*}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /metrics GET method
    def testMetricsTradingservice(url):
        response = requests.get('http://localhost:8084/metrics')
        print(response.text)
    # test:  Mapped "{[/metrics || /metrics.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}" 
    def testMetricsTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/metrics", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /metrics.json GET method
    def testMetricsJSONTradingservice(url):
        response = requests.get('http://localhost:8084/metrics.json')
        print(response.text)
    # test:  Mapped "{[/metrics || /metrics.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}" 
    def testMetricsJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/metrics.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /health GET method
    def testHealtTradingservice(url):
        response = requests.get('http://localhost:8084/health')
        print(response.text)
    # test:  Mapped "{[/health || /health.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testHealtTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/health", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /health.json GET method
    def testHealtJSONTradingservice(url):
        response = requests.get('http://localhost:8084/health.json')
        print(response.text)
    # test:  Mapped "{[/health || /health.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testHealtJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/health.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /auditevents GET method
    def testAuditevensTradingservice(url):
        response = requests.get('http://localhost:8084/auditevents')
        print(response.text)
    # test:  Mapped "{[/auditevents || /auditevents.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testAuditevensTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/auditevents", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /auditevents.json GET method
    def testAuditevensJSONTradingservice(url):
        response = requests.get('http://localhost:8084/auditevents.json')
        print(response.text)
    # test:  Mapped "{[/auditevents || /auditevents.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testAuditevensJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/auditevents.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /loggers/{name:.*} GET method
    def testLoggersNameTradingservice(url):
        response = requests.get('http://localhost:8084/loggers/{name:.*}')
        print(response.text)
    # test: Mapped "{[/loggers/{name:.*}],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testLoggersNameTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/loggers/{name:.*}", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /users/password PUT method
#    def testLoggersNameTradingservice(url):
#        response = requests.put('http://localhost:8084/users/password')
#        print(response.text)
# test:Mapped "{[/loggers/{name:.*}],methods=[POST],consumes=[application/vnd.spring-boot.actuator.v1+json || application/json],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
#    def testLoggersNameTradingserviceStatusCode(data):
#        response = requests.put(url="http://localhost:8084/users/password", data=payload, headers = headers)
#        if (response.status_code == 200):
#            return response.status_code
    # test: url /loggers GET method
    def testLoggersTradingservice(url):
        response = requests.get('http://localhost:8084/loggers')
        print(response.text)
# test:  Mapped "{[/loggers || /loggers.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testLoggersTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/loggers", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /loggers.json GET method
    def testLoggersJSONTradingservice(url):
        response = requests.get('http://localhost:8084/loggers.json')
        print(response.text)
# test:  Mapped "{[/loggers || /loggers.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testLoggersJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/loggers.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /configprops GET method
    def testConfigPropsTradingservice(url):
        response = requests.get('http://localhost:8084/configprops')
        print(response.text)
    # test: Mapped "{[/configprops || /configprops.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testConfigPropsTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/configprops", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /configprops.json GET method
    def testConfigPropsJSONTradingservice(url):
        response = requests.get('http://localhost:8084/configprops.json')
        print(response.text)
    # test: Mapped "{[/configprops || /configprops.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testConfigPropsJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/configprops.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /dump GET method
    def testDumpTradingservice(url):
        response = requests.get('http://localhost:8084/dump')
        print(response.text)
    # test: Mapped "{[/dump || /dump.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testDumpTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/dump", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /dump.json GET method
    def testDumpTradingservice(url):
        response = requests.get('http://localhost:8084/dump.json')
        print(response.text)
    # test: Mapped "{[/dump || /dump.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testDumpTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/dump.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /info GET method
    def testInfoTradingservice(url):
        response = requests.get('http://localhost:8084/info')
        print(response.text)
    # test: Mapped "{[/info || /info.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testInfoTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/info", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /info.json GET method
    def testInfoJSONTradingservice(url):
        response = requests.get('http://localhost:8084/info.json')
        print(response.text)
    # test: Mapped "{[/info || /info.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testInfoJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/info.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /heapdump GET method
    def testHeadDumpTradingservice(url):
        response = requests.get('http://localhost:8084/heapdump')
        print(response.text)
    # test:  Mapped "{[/heapdump || /heapdump.json],methods=[GET],produces=[application/octet-stream]}"
    def testHeadDumpTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/heapdump", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /heapdump.json GET method
    def testHeadDumpJSONTradingservice(url):
        response = requests.get('http://localhost:8084/heapdump.json')
        print(response.text)
    # test:  Mapped "{[/heapdump || /heapdump.json],methods=[GET],produces=[application/octet-stream]}"
    def testHeadDumpJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/heapdump.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /autoconfig GET method
    def testAutoConfigTradingservice(url):
        response = requests.get('http://localhost:8084/autoconfig')
        print(response.text)
    # test:  Mapped "{[/autoconfig || /autoconfig.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testAutoConfigTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/autoconfig", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /autoconfig.json GET method
    def testAutoConfigJSONTradingservice(url):
        response = requests.get('http://localhost:8084/autoconfig.json')
        print(response.text)
    # test:  Mapped "{[/autoconfig || /autoconfig.json],methods=[GET],produces=[application/vnd.spring-boot.actuator.v1+json || application/json]}"
    def testAutoConfigJSONTradingserviceStatusCode(data):
        response = requests.get(url="http://localhost:8084/autoconfig.json", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /v2/api-docs POST method
    def testV2ApiDocsPostTradingservice(url):
        response = requests.post('http://localhost:8084/v2/api-docs')
        print(response.text)
    # test:  Mapped URL path [/v2/api-docs]
    def testV2ApiDocsPostTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/v2/api-docs", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code
    # test: url /** POST method
    def testUrlPostTradingservice(url):
        response = requests.post('http://localhost:8084/**')
        print(response.text)
    # test:  Mapped URL path [/**]
    def testUrlPostTradingserviceStatusCode(data):
        response = requests.post(url="http://localhost:8084/**", data=payload, headers = headers)
        if (response.status_code == 200):
            return response.status_code




