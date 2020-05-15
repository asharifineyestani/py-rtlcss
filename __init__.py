from inc.ReactLaravel import *

from_ = 'for_test/object.js'
to_ = 'for_test/array.blade.php'
from_path = open(from_, "r")
string = ''.join(from_path.readlines())

# string = obj_to_array(string)
string = map_to_loop(string)

with open(to_, "a") as result:
    result.write(string)
