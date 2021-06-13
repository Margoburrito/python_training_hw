from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", email="", home_tel="", work_tel="", mobile="", phone2="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 20), email=random_string("email", 20), email2=random_string("@", 20),
            email3=random_string("email@", 20), home_tel=random_string("22", 10), work_tel=random_string("12", 10),
            mobile=random_string("44", 10), phone2=random_string("+7", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda  x: x.__dict__, indent=2))