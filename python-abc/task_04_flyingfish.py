#!/usr/bin/env python3
'''4. The Enigmatic FlyingFish - Exploring Multiple Inheritance'''

class Fish(FlyingFish):
    '''class Fish that inherits from FlyingFish'''
    def __init__(self):
        '''initialization of the class'''
        FlyingFish.__init__(self)

    def swim(self):
        '''méthode swim'''
        print("The fish is swimming")

    def habitat(self):
        '''méthode habitat'''
        print("The fish lives in water")
    
class Bird(FlyingFish):
    '''class Bird that inherits from FlyingFish'''
    def __init__(self):
        '''initialization of the class'''
        FlyingFish.__init__(self)

    def fly(self):
        '''méthode fly'''
        print("The bird is flying")

    def habitat(self):
        '''méthode habitat'''
        print("The bird lives in the sky")
