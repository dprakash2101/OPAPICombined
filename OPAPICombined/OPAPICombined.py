

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
from openapi_client.models.employee import Employee


# Defining the host is optional and defaults to https://localhost:7044
# See configuration.py for a list of all supported configuration parameters.
def contact():
    configuration = openapi_client.Configuration(host = "https://localhost:7207")
    configuration.verify_ssl = False



# Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = openapi_client.ContactApi(api_client)

        try:
            api_response = api_instance.contact_get()
            print("The response of ContactApi->contact_get:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ContactApi->contact_get: %s\n" % e)

       
            
       

def employee():
    configuration = openapi_client.Configuration(
    host = "https://localhost:7044"
    )
    configuration.verify_ssl =False


# Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = openapi_client.EmployeeApi(api_client)

        try:
            api_response = api_instance.employee_get()
            print("The response of EmployeeApi->employee_get:\n")
            print(list(api_response))
        except Exception as e:
            print("Exception when calling EmployeeApi->employee_get: %s\n" % e)

contact()
employee()