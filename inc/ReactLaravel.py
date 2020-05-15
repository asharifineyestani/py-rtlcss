import re


def map_to_loop(string):
    # convert Link to <a/>

    pattern_link = r'<Link\sto=(\{*\"*.*?\"*}*)>([\s\S]*?)</Link>'
    translate_a = r'<a href="\1">\2</a>'
    map_with_a = re.sub(pattern_link, translate_a, string)

    # map_with_a = self.get_form() # todo ______testing_____

    # print(map_with_a.strip())

    # find maps
    pattern_map = r'\{[\s\S]*?\s*(.*)\.map\(\((.*),.*\(([\s\S]*?)\)\)\}'

    maps_found = re.findall(pattern_map, map_with_a)

    # print(maps_found)
    # pass
    joined_maps_found = ''.join(maps_found[0][2])

    # print(maps_found)

    # convert js variables to php variables
    temp_map = re.sub(r'{', '{{$', joined_maps_found)
    temp_map = re.sub(r'\}', '}}', temp_map)
    temp_map = re.sub(r'\.', '->', temp_map)

    # remove key
    temp_map = re.sub(r'\s*key=\{.*}', '', temp_map)

    map_child = re.sub(pattern_map, temp_map, map_with_a)
    laravel_foreach_template = "@foreach($items as $item)%@endforeach"
    laravel_foreach_final = re.sub(r'%', map_child, laravel_foreach_template)
    # print(laravel_foreach_final)

    return laravel_foreach_final


def obj_to_array(s):
    s = re.sub(r'let\s*(.*)\s*=', r'$\1=', s)
    p = r'\s*(.*):\s*(\"*.*?\"*),'
    to = r'"\1"=>\2,\n'
    s = re.sub(p, to, s)
    s = re.sub('\s*{', '\n[\n', s)
    s = re.sub('\s*}', '\n]', s)
    return s


def heading(string):
    p = r'<Heading([\s\S]*?)/>'

    def replacement(m):
        s = '<x-heading @ />'
        s = re.sub(r'@', m[1], s)
        return s

    # string = re.findall(p, string)
    string = re.sub(p, replacement, string)
    return string


def maps(string):
    p = r'(\{[a-zA-Z]*\.map[.\s\S]*?\)\)})'

    def replacement(m):
        return map_to_loop(m[0])

    string = re.sub(p, replacement, string)

    return string


def cols(string):
    p = r'<Col\s+([.\s\S]*?)>'

    def replacement(m):
        classes = []

        def child_replacement(_m):
            col_class = 'col-@1-@2'
            col_class = re.sub(r'@1', _m[1], col_class)
            col_class = re.sub(r'@2', _m[2], col_class)
            classes.append(col_class)

        re.sub(r'([a-z]{2})=\{([0-9]*)}', child_replacement, m[1])

        return re.sub(r'@', ' '.join(classes), '<div class="@">')

    return re.sub(p, replacement, string)
