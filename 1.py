from collections import OrderedDict
from requests import get, post

d = OrderedDict([
    ('pen', 3),
    ('pineapple', 2),
    ('apple', 1),
])

print(d.keys())
