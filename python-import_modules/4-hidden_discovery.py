#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for noms in names:
        if noms[:2] != '__':
            print(noms)
