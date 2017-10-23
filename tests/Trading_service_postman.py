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







