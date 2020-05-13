import re


class MakeDiff:
    diff_path = 'css/difference.css'
    style_path = 'css/style.css.css'
    rtl_path = 'css/rtl.css.css'
    temp = []

    def __init__(self):
        self.clear_difference_file()

    @staticmethod
    def clear_difference_file():
        open('css/difference.css', 'w').close()

    def update(self):
        style = open("css/style.css", "r")
        rtl = open("css/rtl.css", "r")
        lines_rtl = rtl.readlines()
        for i, lines_style in enumerate(style):
            if lines_style != lines_rtl[i]:
                self.temp.append(lines_rtl[i])
            else:
                x = re.search("^.*[{},]$", lines_rtl[i])
                if x:
                    self.temp.append(lines_rtl[i])

        temp = []
        for line in self.temp:
            temp.append(line)
            if re.search("}", line):
                if ";" in ''.join(temp):
                    with open("css/difference.css", "a") as result:
                        for css_property in temp:
                            result.write(css_property)
                        result.write("\n")

                temp = []

    print('difference updated')


diff = MakeDiff()
diff.update()
