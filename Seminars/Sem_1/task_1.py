# Написать автотест на bash, который читает содержимое файла /etc/os-release
# (в нем хранится информация о версии системы) и выведет на экран “SUCCESS”,
# если в нем содержатся версия 22.04.1, кодовое имя jammy и команда чтения файла выполнена без ошибок.
# В противном случае должно выводится “FAIL”.

import subprocess


if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    print(out)
    if '22.04.1' in out and 'jammy' in out and result.returncode == 0:
        print('SUCCESS')
    else:
        print('FAIL')