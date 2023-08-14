# Создать отдельный файл для негативных тестов.
# Функцию проверки вынести в отдельную библиотеку.
# Повредить архив( н-р: отредактировав в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки (е)
# и проверки (t) поврежденного файла


from checher import checkout_negative

tst = "/home/gb/tst"
out = "/home/gb/out"
badarx = "/home/gb/badarx"
folder = "/home/gb/folder1"


def test_step1():
    # Разархивировать архив arx2.7z в директорию folder1 и проверяем наличие файлов test1 и test2 в директории folder1
    assert checkout_negative("cd {}; 7z e arx2.7z -o{} -y".format(badarx, folder), "ERRORS"), "test1 FAIL"


def test_step2():
    # Проверяем целостность архива arx2.7z
    assert checkout_negative("cd {}; 7z t arx2.7z".format(badarx), "ERRORS"), "test2 FAIL"