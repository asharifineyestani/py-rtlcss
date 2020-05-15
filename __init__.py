from inc.ReactLaravel import *

string = ''
from_ = 'for_test/object.js'
to_ = 'for_test/result.php'
from_path = open(from_, "r",  encoding="utf8")
string = ''.join(from_path.readlines())

# string = obj_to_array(string)
# string = map_to_loop(string)
# string = heading(string)
# string = maps(string)
string = cols(string)

with open(to_, "a") as result:
    result.write(string)
