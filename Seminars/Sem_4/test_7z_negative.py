from sshcheckers import ssh_checkout_negative, ssh_getout
from conftest import save_log
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_folders, make_files, make_bad_arx, start_time):
    # test1
    save_log(start_time, "log_neg_step1.txt")
    assert ssh_checkout_negative(data["host"], data["user"], "11", "cd {}; 7z e badarx.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext"]), "ERROR"), "neg_step1 Fail"


def test_step2(clear_folders, make_folders, make_files, make_bad_arx, start_time):
    # test2
    save_log(start_time, "log_neg_step2.txt")
    assert ssh_checkout_negative(data["host"], data["user"], "11", "cd {}; 7z t badarx.{}".format(data["folder_out"], data["type"]), "ERROR"), "neg_step2 Fail"


def test_step3(clear_folders, make_folders, make_files, make_bad_arx, start_time):
    # Создаем архив несуществующего типа
    save_log(start_time, "log_neg_step3.txt")
    assert ssh_checkout_negative(data["host"], data["user"], "11", "cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type_bad_arx"]), "ERROR"), "neg_step3 Fail"
