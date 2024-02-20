#!/usr/bin/env python3

import re
import io
from minio import Minio

# Scan the given bucket and for any object having a name in the form `fib-*`
# read the contents and if it is a single integer N, make a new object having
# the name `result-*` that contains the N-th fibinocci number.

ACCESS_KEY = ""
SECRET_KEY = ""
bucket_name = "cicf-data"

c = Minio("localhost:9000", ACCESS_KEY, SECRET_KEY, secure=False)

def fib(n):
    a,b = 0, 1
    while n > 0:
        a,b = b, a+b
        n -= 1
    return a

for obj in c.list_objects(bucket_name):
    name = obj.object_name
    if not re.match("fib-.*", name):
        continue
    # make sure object is not too big. This limit is arbitrary.
    if obj.size > 1000:
        continue
    data = c.get_object(bucket_name, name)
    data_s = data.read()
    n = int(data_s)
    result = ""
    # if N is too big
    if n > 100:
        result = "Too big"
    else:
        result = str(fib(n))
    new_name = "result-" + name
    c.put_object(bucket_name, new_name, io.BytesIO(bytes(result, 'utf-8')), len(result))


