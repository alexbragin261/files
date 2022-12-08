with (
    open('sorted/1.txt') as file1,
    open('sorted/2.txt') as file2,
    open('sorted/3.txt') as file3
):
    f_1 = file1.read()
    f_2 = file2.read()
    f_3 = file3.read()

with (
    open('sorted/1.txt') as file1,
    open('sorted/2.txt') as file2,
    open('sorted/3.txt') as file3,
    open('file.txt', 'w') as file
):

    def iter_file(file_name):
        string_count = 0
        for _ in file_name:
            string_count += 1
        return string_count


    string_count_1 = str(iter_file(file1))
    string_count_2 = str(iter_file(file2))
    string_count_3 = str(iter_file(file3))

    class Files:
        def __init__(self, name, string_count, text):
            self.name = name
            self.string_count = string_count
            self.text = text

        def __str__(self):
            res = f'{self.name}\n{self.string_count}\n{self.text}\n'
            return res

    text_1 = Files('1.txt', string_count_1, f_1)
    text_2 = Files('2.txt', string_count_2, f_2)
    text_3 = Files('3.txt', string_count_3, f_3)

    file.write(str(text_2) + str(text_1) + str(text_3))
