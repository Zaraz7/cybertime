# time-RG #
import time
import os
import pickle

logo = '''
   ___     _            _____ _           
  / __|  _| |__  ___ _ |_   _(_)_ __  ___ 
 | (_| || | '_ \/ -_) '_|| | | | '  \/ -_)
  \___\_, |_.__/\___|_|  |_| |_|_|_|_\___|
      |__/                      Mini 0.1.0

'''
print(logo)
path = 'time.data'
help = '''
help        помощь по командам
real        замена игрового времени на настоящее
start       запустить таймер
fast <X>    запустить ускоренный в X раз таймер
slow <X>    запустить замедленный в X раз таймер
plus <X> [s|m|h|d]      отправиться на X едениц времени вперед
minus <X> [s|m|h|d]     отправиться на X едениц времени назад
CTRL + C    остановить таймер
exit [f|s]  выход (опционально: f - быстрый выход, s - с сохранением)

Примеры команд:
 fast 10
 slow 2
 plus 30 m
 plus 1 h
'''
helpplus = 'cmd <VELUE> <m|h|d>\n\n\
 plus 60 m:     отправиться в будущее на 60 минут'
def load():
    file = open(path, 'rb')
    pickl = pickle.load(file)
    file.close()
    return pickl
def save():
    file=open(path, 'wb')
    pickle.dump(sec, file)
    file.close()

if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
    sec = load()
else:
    print('WARNING: Data файл не найден (если это первый запуск, то игнорируйте это сообщение)')
    sec = time.time()

def start(mod=1):
    global sec
    try:
        while True:
            print(time.ctime(sec), end='\r')
            time.sleep(1 * mod)
            sec += 1
    except KeyboardInterrupt:
        print('\rStopped                   ')
def real():
    global sec
    sec = time.time()

def asciiart(text, file='ASCII art letters.txt'):
    conf = open(file).read()
    """Produces an ascii art representation of text using the conf data"""
    if isinstance(conf, str):
        conf = conf.split('\n')

    height, key, data = int(conf[0]), conf[1], conf[2:]
    figures = dict(map(
        lambda x: (x, data[key.index(x) * height: (key.index(x) + 1) * height]),
        key))
    art = '\n'.join([
        '\n'.join([
            ' '.join([figures[x][i] for x in t.lower() if x in figures])
            for i in range(height)])
        for t in text.split('\n')])
    return art


while True:
    cmd = input('{}> '.format(time.ctime(sec))).split()
    try:
        if cmd[0] == 'exit':
            if 'f' in cmd:
                break
            elif 's' in cmd:
                save()
                break
            cmd = input('Вы точно уверены? Все несохраненные изменения пропадут бесследно\
        \n[y] Выйти без сохранений\
        \n[s] Сохранить и выйти\n')
            if cmd == 'y':
                break
            elif cmd == 's':
                save()
                break
            else:
                pass
        elif cmd[0] == 'help':
            print(help)
        elif cmd[0] == 'fast':
            mod = 1 / int(cmd[1])
            start(mod)
        elif cmd[0] == 'load':
            sec = load()
        elif cmd[0] == 'plus':
            if len(cmd) == 1:
                print(helpplus)
            else:
                vel = int(cmd[1])
                if 's' in cmd:
                    sec += vel
                elif 'm' in cmd:
                    sec += vel * 60
                elif 'h' in cmd:
                    sec += vel * 3600
                elif 'd' in cmd:
                    sec += vel * 86400
                else:
                    print(helpplus)
        elif cmd[0] == 'minus':
            if 's' in cmd:
                sec -= vel
            elif 'm' in cmd:
                sec -= vel * 60
            elif 'h' in cmd:
                sec -= vel * 3600
            elif 'd' in cmd:
                sec -= vel * 86400
            else:
                print(helpplus)
        elif cmd[0] == 'real':
            real()
        elif cmd[0] == 'save':
            save()
        elif cmd[0] == 'slow':
            mod = 1 * int(cmd[1])
            start(mod)
        elif cmd[0] == 'start':
            start()
        elif cmd[0] == 'test':
            asciiart('1')
        else:
            print('ERROR: Недопустимая команда')
    except IndexError:
        print('ERROR: Недостаточно аргументов')
    except ValueError:
        print('ERROR: Недопустимое значение')
