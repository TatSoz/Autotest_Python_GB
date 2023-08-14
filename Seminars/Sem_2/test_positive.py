from checher import checkout

tst = "/home/gb/tst"
out = "/home/gb/out"
folder = "/home/gb/folder1"

def test_step1():
    # Создаём архив arx2 и проверяем его наличие в директории out
    res1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # Разархивируем архив arx2 7z в директорию folder1 и проверяем в ней наличие файлов test1 и test2
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(folder), "test1")
    res3 = checkout("ls {}".format(folder), "test1")
    assert res1 and res2 and res3, "test2 FAIL"

def test_step3():
    # Проверяем целостность архива arx2.7z
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), "test3 FAIL"

def test_step4():
    # Проверяем возможность обновления архива arx2.7z
    assert checkout("cd {}; 7z u {}/arx2.7z".format(tst, out), "Everything is Ok"), "test4 FAIL"


def test_step5():
    # Проверяем удаление содержимого архива arx2.7z
    assert checkout("cd {}; 7z d arx2.7z".format(out), "Everything is Ok"), "test5 FAIL"


