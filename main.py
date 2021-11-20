# We will be using requests library to make API requests
import requests

# The endpoint we will be using for this demo is PeterPortal API.

# This endpoint returns all course information
URL = 'https://api.peterportal.org/rest/v0/courses/all'

# This endpoint requires a query which will specify what information we want.
URL2 = 'https://api.peterportal.org/rest/v0/grades/calculated'

def main():
    # response = requests.get(URL)
    # print(response.json())


    query = {
        'year': '2019-20',
        'instructor': 'PATTIS, R.',
        'department': 'I&C SCI',
        'numer': '33'
    }
    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(URL2, params = query, headers = headers, timeout = 5)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)




if __name__ == '__main__':
    main()