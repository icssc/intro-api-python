# We will be using requests to make API requests
import requests

# The endpoint we will be using for this workshop is PeterPortal API.

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

    response = requests.get(URL2, params = query)
    print(response.json())


if __name__ == '__main__':
    main()