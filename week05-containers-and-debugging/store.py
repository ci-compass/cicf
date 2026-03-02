#!/usr/bin/env python3

import re
import io
import redis

# Scan key having a name in the form `fib-*`
# read the value. if it is an empty string, replace it with the nth fibinocci number

def fib(n):
    a,b = 0, 1
    while n > 0:
        a,b = b, a+b
        n -= 1
    return a

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# scan through all keys starting with "fib-"
for k in r.scan_iter(match="fib-*"):
    v = r.get(k)
    # skip non empty values
    if v != '':
        continue
    try:
        n = int(k[len('fib-'):])
        r.set(k, str(fib(n)))
    except ValueError:
        pass


