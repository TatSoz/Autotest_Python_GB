from checkout import checkout_positive
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    # Создаём архив arx1 и проверяем его наличие в директории out
    res1 = checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok")
    res2 = checkout_positive("ls {}".format(data["folder_out"]), "arx1.7z")
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # Разархивируем архив в директорию folder_out и проверяем в ней наличие файлов из архива
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(data["folder_ext"]), item))
    assert all(res), "Test2 Fail"


def test_step3():
    # Целостность архива
    assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "Test3 Fail"


def test_step4():
    # Обновление архива
    assert checkout_positive("cd {}; 7z u {}/arx2.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "Test4 Fail"


def test_step5(clear_folders, make_files):
    # Просмотр содержимого архива без его распаковки
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
    assert all(res), "Test5 Fail"


def test_step6(clear_folders, make_files, make_subfolder):
    # Проверка сохранения путей при распаковки архива

    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z x arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "Everything is Ok"))
    for i in make_files:
        res.append(checkout_positive("ls {}".format(data["folder_ext"]), i))
    res.append(checkout_positive("ls {}".format(data["folder_ext"]), make_subfolder[0]))
    res.append(checkout_positive("ls {}/{}".format(data["folder_ext"], make_subfolder[0]), make_subfolder[1]))
    assert all(res), "test6 FAIL"



def test_step7():
    # Очищаем содержимое архива
    assert checkout_positive("7z d {}/arx1.7z".format(data["folder_out"]), "Everything is Ok"), "Test7 Fail"
