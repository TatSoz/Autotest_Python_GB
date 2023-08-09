# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный
# режим работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string

def check_command_output(command: str, text: str, func_mode: int) -> bool:

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')


    if result.returncode == 0:
        out = result.stdout
        if func_mode == 0:
            if text in out:
                return True
            else:
                return False

        elif func_mode == 1:
            punct = string.punctuation
            new_out = ''.join(i for i in out if i not in punct)
            print(new_out.split())
            if text in new_out:
                return True
            else:
                return False



if __name__ == '__main__':
    mode = int(input('Выберите режим функции\n'
                     '0 - знаки препенания не удаляются\n'
                     '1- знаки препенания удаляются: '))
    text = '22.04.1'
    com = 'cat /etc/os-release'
    print(check_command_output(com, text, mode))

    