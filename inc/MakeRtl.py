import os


class MakeRtl:
    dirs = []

    def __init__(self):
        self.target_dir = '../scss'
        self.set_files()

    def set_files(self):
        for path, sub_dirs, files in os.walk(self.target_dir):
            for name in files:
                self.dirs.append(os.path.join(path, name))


s = MakeRtl()

for x in s.dirs:
    print(x)
