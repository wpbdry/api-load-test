import pprint as pp
import requests
import progress_bar

import exceptions

pprint = pp.PrettyPrinter(indent=4).pprint


def load_test(url, method='GET', body=None, number_of_calls=1):
    if method != 'GET':
        raise exceptions.InvalidMethod()
    response_codes = {}
    for i in range(0, number_of_calls):
        if method == 'GET':
            r = requests.get(url)
            if response_codes.get(r.status_code) == None:
                response_codes[r.status_code] = 0
            response_codes[r.status_code] += 1
    print("Response codes:")
    pprint(response_codes)
