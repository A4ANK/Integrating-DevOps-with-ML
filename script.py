with open('training.py') as file:
    if 'keras' and 'mnist' in file.read():
        return True
    else:
        pass