# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.


import subprocess
from checher import checkout

path = "/home/gb/archive"
archive = "arx2.7z"


def get_hash(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


def test_hash():
    res1 = get_hash("cd {}; crc32 {}".format(path, archive))
    res2 = checkout("cd {}; 7z h {}".format(path, archive), "Everything is Ok")
    assert res1 and res2, "test FAIL"


