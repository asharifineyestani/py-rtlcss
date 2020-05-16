from inc.ReactLaravel import *
import io

string = ''
from_ = 'for_test/object.js'
to_ = 'for_test/result.txt'
from_path = io.open(from_, "r", encoding="utf-8")
string = ''.join(from_path.read())

string = obj_to_array(string)
# string = map_to_loop(string)
string = heading(string)
string = maps(string)
string = cols(string)
string = other(string)

with open(to_, "a") as result:
    result.write(string)
