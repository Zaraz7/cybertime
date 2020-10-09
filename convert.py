import pickle
import os

def load():
    file = open(path, 'rb')
    pickl = pickle.load(file)
    file.close()
    return pickl
def save(): 
    file=open('time.dat', 'wb')
    pickle.dump(S, file)
    file.close()

while True:
    path = 'time.dat'
    if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
        S = load()
    else:
        S = {}

    value = input('Название файла (по умолчанию time.data)/n> ')
    if value == '':
        path = 'time.data'
    else:
        path = value
    sec = load()

    name = input('Как вы хотите назвать временную линию?/n> ')
    S[name] = sec
    save()
