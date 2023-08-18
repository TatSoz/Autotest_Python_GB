from sshcheckers import ssh_checkout, upload_files, ssh_getout
from conftest import save_log
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step0(start_time):
    res = []
    upload_files(data["host"], data["user"], "11", "{}/p7zip-full.deb".format(data["local_path"]),
                 "{}/p7zip-full.deb".format(data["remote_path"]))
    res.append(ssh_checkout(data["host"], data["user"], "11",
            "echo '11' | sudo -S dpkg -i {}/p7zip-full.deb".format(data["remote_path"]), "Настраивается пакет"))
    res.append(ssh_checkout(data["host"], data["user"], "11",
                            "echo '11' | sudo -S dpkg -s p7zip-full", "Status: install ok installed"))
    save_log(start_time, "log_poz_step0.txt")
    assert all(res)


def test_step1(make_folders, clear_folders, make_files, start_time):
    # Создаём архив arx1 и проверяем его наличие в директории out
    res1 = ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z a {}/arx1 -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                        "Everything is Ok")
    res2 = ssh_checkout(data["host"], data["user"], "11",
                        "ls {}".format(data["folder_out"]), "arx1.{}".format(data["type"]))
    save_log(start_time, "log_poz_step1.txt")
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, start_time):
    # Разархивируем архив в директорию folder_out и проверяем в ней наличие файлов из архива
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z a {}/arx1 -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                            "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z e arx1.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext"]),
                                                                                            "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "11",
                                                            "ls {}".format(data["folder_ext"]), item))
    save_log(start_time, "log_poz_step2.txt")
    assert all(res), "Test2 Fail"


def test_step3(start_time):
    # Целостность архива
    save_log(start_time, "log_poz_step3.txt")
    assert ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z t {}/arx1.{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                "Everything is Ok"), "Test3 Fail"


def test_step4(start_time):
    # Обновление архива
    save_log(start_time, "log_poz_step4.txt")
    assert ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z u {}/arx2.{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                "Everything is Ok"), "Test4 Fail"


def test_step5(clear_folders, make_files, start_time):
    # Просмотр содержимиго архива без его распаковки
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z a {}/arx1 -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                            "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "11",
                                "cd {}; 7z l arx1.{}".format(data["folder_out"], data["type"]), item))
    save_log(start_time, "log_poz_step5.txt")
    assert all(res), "Test5 Fail"


def test_step6(clear_folders, make_files, make_subfolder, start_time):
    # Проверка сохранения путей при распаковки архива
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "11", "cd {}; 7z a {}/arx1 -t{}".format(data["folder_in"], data["folder_out"], data["type"]), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], "11", "cd {}; 7z x arx1.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext"]), "Everything is Ok"))

    for i in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "11", "ls {}".format(data["folder_ext"]), i))
    res.append(ssh_checkout(data["host"], data["user"], "11", "ls {}".format(data["folder_ext"]), make_subfolder[0]))
    res.append(ssh_checkout(data["host"], data["user"], "11", "ls {}/{}".format(data["folder_ext"], make_subfolder[0]), make_subfolder[1]))
    save_log(start_time, "log_poz_step6.txt")
    assert all(res), "Test6 Fail"


def test_step7(start_time):
    # Очищаем содержимое архива
    save_log(start_time, "log_poz_step7.txt")
    assert ssh_checkout(data["host"], data["user"], "11",
                "7z d {}/arx1.{}".format(data["folder_out"], data["type"]), "Everything is Ok"), "Test7 Fail"

def test_step8(make_folders, clear_folders, make_files, start_time):
    # Тест сравнения хэша, из дом.зад.2
    ssh_checkout(data["host"], data["user"], "11",
            "cd {}; 7z a {}/arx1 -t{}".format(data["folder_in"], data["folder_out"], data["type"]),
                                                                                            "Everything is Ok")
    res1 = ssh_getout(data["host"], data["user"], "11",
                      "cd {}; crc32 arx1.{}".format(data["folder_out"], data["type"]))
    res2 = ssh_checkout(data["host"], data["user"], "11",
                         "cd {}; 7z h arx1.{}".format(data["folder_out"], data["type"]), "Everything is Ok")
    save_log(start_time, "log_poz_step8.txt")
    assert res1 and res2, "Test8 Fail"

