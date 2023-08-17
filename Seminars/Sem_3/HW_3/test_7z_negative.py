from checkout import checkout_negative
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)

def test_step1(clear_folders, make_folders, make_files, make_bad_arx):
    # test1
    assert checkout_negative("cd {}; 7z e badarx.{} -o{} -y".format(data["folder_out"], data["type"], data["folder_ext"]), "ERROR"), "neg_step1 Fail"


def test_step2(clear_folders, make_folders, make_files, make_bad_arx):
    # test2
    assert checkout_negative("cd {}; 7z t badarx.{}".format(data["folder_out"], data["type"]), "ERROR"), "neg_step2 Fail"


def test_step3(clear_folders, make_folders, make_files, make_bad_arx):
    # Создаем архив несуществующего типа
    assert checkout_negative("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"], data["type_bad_arx"]), "ERROR"), "neg_step3 Fail"
