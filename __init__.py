from inc.ReactLaravel import *

string = ''
from_ = 'for_test/object.js'
to_ = 'for_test/array.blade.php'
from_path = open(from_, "r",  encoding="utf8")
string = ''.join(from_path.readlines())

# string = obj_to_array(string)
# string = map_to_loop(string)
string = heading(string)


with open(to_, "a") as result:
    result.write(string)
