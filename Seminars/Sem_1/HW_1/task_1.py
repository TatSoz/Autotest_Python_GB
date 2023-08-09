# (Дорабатываем задание с семенара)
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess

def check_command_output(command: str, text: str) -> bool:

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        out = result.stdout
        print(out)
        if text in out:
            return True
        else:
            return False



if __name__ == '__main__':
    text = '22.04.1'
    com = 'cat /etc/os-release'
    print(check_command_output(com, text))










    