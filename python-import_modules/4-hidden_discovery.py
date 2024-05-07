#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for noms in dir(hidden_4):
        if noms[:2] != '__':
            print(noms)
