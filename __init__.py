import re


class MakeDiff:
    diff_path = 'css/difference.css';
    style_path = 'css/style.css.css';
    rtl_path = 'css/rtl.css.css';

    def __init__(self):
        self.clear_difference_file

    def clear_difference_file(self):
        open('css/difference.css', 'w').close()

    def update(self):
        style = open("css/style.css", "r")
        rtl = open("css/rtl.css", "r")
        lines_rtl = rtl.readlines()
        for i, lines_style in enumerate(style):
            if lines_style != lines_rtl[i]:
                with open("css/difference.css", "a") as result:
                    result.write(lines_rtl[i])
                pass
            else:
                x = re.findall("^..*;$", lines_rtl[i])
                if not x:
                    with open("css/difference.css", "a") as result:
                        result.write(lines_rtl[i])
        print('difference updated')


diff = MakeDiff()
diff.update()
