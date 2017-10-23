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
