# We will be using requests library to make API requests
import requests

# The endpoint we will be using for this demo is PeterPortal API.

# This endpoint returns all course information
URL = 'https://api.peterportal.org/rest/v0/courses/all'

# This endpoint requires a query which will specify what information we want.
URL2 = 'https://api.peterportal.org/rest/v0/grades/calculated'

def main():
    query = {
        'year': '2019-20',
        'instructor': 'PATTIS, R.',
        'department': 'I&C SCI',
        'numer': '33'
    }
    # Not necessary for every Web API, but it's good practice
    # Ensures our response is in JSON format.
    headers = {
        "Content-Type": "application/json",
    }

    try:
       # response = requests.get(URL) 
        response = requests.get(URL2, params = query, headers = headers, timeout = 5)
        response.raise_for_status() #returns HTTPError object in case of error.
        print(response.json())

    #Requests module handles errors by using exception handling. 
    except requests.exceptions.HTTPError as errh: #catches HTTPError object
        print(errh)
    except requests.exceptions.ConnectionError as errc: #if there was an connection error
        print(errc)
    except requests.exceptions.Timeout as errt: #if time exceeds the timeout allotted above. 
        print(errt)
    except requests.exceptions.RequestException as err: #ambiguous exception that occurred while handling your request
        print(err)




if __name__ == '__main__':
    main()