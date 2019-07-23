import random
import re

import pprint as pp
import pyterm_progress_bar
import requests

import exceptions

pprint = pp.PrettyPrinter(indent=4).pprint


def randomize(match_obj):
    return str(random.randint(0, 90))


def load_test(url, method='GET', body=None, number_of_calls=1):
    if method != 'GET':
        raise exceptions.InvalidMethod()
    response_codes = {}
    pbar = pyterm_progress_bar.ProgressBar(name="Load testing")
    pbar.start()
    for i in range(0, number_of_calls):
        current_url = re.sub(r'{random}', randomize, url)  # TODO: 90 not suitable for general use
        if method == 'GET':
            r = requests.get(current_url)
            if response_codes.get(r.status_code) == None:
                response_codes[r.status_code] = 0
            response_codes[r.status_code] += 1
            pbar.update((i+1)/number_of_calls)
    print("Response codes:")
    pprint(response_codes)
