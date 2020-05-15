import re


class MakeDiff:
    from_path = 'css/Footer.js'
    to_path = 'css/section.blade.php'

    def __init__(self):
        self.clear_result_file()

    def clear_result_file(self):
        open(self.to_path, 'w').close()

    def update(self):
        ali = open(self.from_path, "r")
        s = ''.join(ali.readlines())
        s = self.obj_to_array(s)

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
        return s;


diff = MakeDiff()
diff.update()
# diff.test()
