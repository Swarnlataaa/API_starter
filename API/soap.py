from zeep import Client

# Create a SOAP client
client = Client('http://example.com/soap-endpoint?wsdl')

# Call a SOAP service method
response = client.service.MyServiceMethod(param1, param2)

print(response)
