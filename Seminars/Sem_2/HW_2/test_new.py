# 1. Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x)
# Папка folder_test содержит папку test2 и файл test1, а в папке test2 находиться файл test2

from checher import checkout

tst = "/home/gb/folder_test"
out = "/home/gb/archive"
folder = "/home/gb/folder2"


def test_step1():
    # Создаём архив arx2 и проверяем вывод списка файлов в архиве
    res1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    res2 = checkout("cd {}; 7z l arx2.7z".format(out), "test1")
    res3 = checkout("cd {}; 7z l arx2.7z".format(out), "test2")
    assert res1 and res2 and res3, "test1 FAIL"


def test_step2():
    # Разархивируем архив (x) arx2 7z в директорию folder2 и проверяем в ней пути после разорхивирования
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(folder), "test1")
    res3 = checkout("ls {}/test_2".format(folder), "test2")
    assert res1 and res2 and res3, "test2 FAIL"