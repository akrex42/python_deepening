import os
import tempfile


class File:

    def __init__(self, name, mode="a+"):
        self.f = open(name, mode)
        self.count = 0

    def __enter__(self):
        return self.f

    def __exit__(self, name):
        self.f.close()

    def read(self):
        self.f.seek(0)
        return self.f.read()

    def write(self, new_str):
        return self.f.write(str(new_str))

    def __add__(self, other):
        new_file_path = os.path.join(tempfile.gettempdir(), tempfile.mktemp())
        new_file = File(new_file_path, "a+")
        new_file.write(str(self.read()) + str(other.read()))
        return new_file

    def __str__(self):
        return os.path.abspath(os.path.join(tempfile.gettempdir(), str(self.f.name)))

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            self.f.seek(0)
        self.current = self.f.readline()
        self.count += 1
        if not self.current:
            raise StopIteration
        return self.current


if __name__ == "__main__":

    path_to_file = 'some_filename'
    file_obj_3 = File(path_to_file + '_3')
    file_obj_4 = File(path_to_file + '_4')
    file_obj_3.write('line 1\n')
    file_obj_4.write('line 2\n')
    new_file_obj = file_obj_3 + file_obj_4
    print(isinstance(new_file_obj, File))
    print(new_file_obj)
    for line in new_file_obj:
        print(ascii(line))
    new_path_to_file = str(new_file_obj)
    os.path.exists(new_path_to_file)
    file_obj_3 = File(new_path_to_file)
    print(file_obj_3)
    file_obj_3.write('15b11217c71f432cbadf0cd09812067a')
    file_obj_4.write(file_obj_4.read())
    for line in file_obj_4:
        print(line)
    # print(str(hash(new_file_obj)))
