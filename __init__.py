import re


class MakeDiff:
    from_path = 'for_test/object.js'
    to_path = 'for_test/array.php'

    def __init__(self):
        self.clear_result_file()

    def clear_result_file(self):
        open(self.to_path, 'w').close()

    def convert_map_to_laravel_loop(self):
        from_path = open(self.from_path, "r")
        from_lines = ''.join(from_path.readlines())

        # convert Link to <a/>
        pattern_link = r'<Link\sto=(\{*\"*.*?\"*}*)>([\s\S]*?)</Link>'
        translate_a = r'<a href="\1">\2</a>'
        new_string = re.sub(pattern_link, translate_a, from_lines)

        # find maps
        pattern_map = r'\{.*map.*\(([\s\S]*?)\)\)\}'
        maps_found = re.findall(pattern_map, new_string)
        joined_maps_found = ''.join(maps_found)

        # convert js variables to php variables
        temp_map = re.sub(r'{', '{{$', joined_maps_found)
        temp_map = re.sub(r'\}', '}}', temp_map)
        temp_map = re.sub(r'\.', '->', temp_map)

        # remove key
        temp_map = re.sub(r'\s*key=\{.*}', '', temp_map)
        map_child = re.sub(pattern_map, temp_map, new_string)
        laravel_foreach_template = "@foreach($items as $item)%@endforeach"
        laravel_foreach_final = re.sub(r'%', map_child, laravel_foreach_template)
        print(laravel_foreach_final)

    def update(self):
        ali = open(self.from_path, "r")
        s = ''.join(ali.readlines())
        # s = self.obj_to_array(s)
        s = self.react_to_html(s)

        with open(self.to_path, "a") as result:
            result.write(s)
        print('javascript object converted to php array successfully')

    @staticmethod
    def obj_to_array(s):
        s = re.sub(r'let\s*(.*)\s*=', r'$\1=', s)
        p = r'\s*(.*):\s*(\"*.*?\"*),'
        to = r'"\1"=>\2,\n'
        s = re.sub(p, to, s)
        s = re.sub('\s*{', '\n[\n', s)
        s = re.sub('\s*}', '\n]', s)
        return s

    @staticmethod
    def react_to_html(s):
        p = r'<Link\sto=\{*\"*(.*?)\"*}*>([\s\S]*?)</Link>'
        to = r'<a href="\1">\2</a>'
        s = re.sub(p, to, s)

        p = r'className="(.*)"'
        to = r'class="\1"'
        s = re.sub(p, to, s)

        p = r'<Container>'
        to = r'<div class="container">'
        s = re.sub(p, to, s)

        p = r'key=\{.*}'
        to = r''
        s = re.sub(p, to, s)

        return s


diff = MakeDiff()
diff.convert_map_to_laravel_loop()
# diff.test()
