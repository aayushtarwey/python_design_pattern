"""
Naive Singleton Pattern Implementation

This module demonstrates the Singleton design pattern using a Metaclass approach.

For detailed documentation, refer to docs/SINGLETON_GUIDE.md

Author: Aayush Tarwey
Date: December 11, 2025
Version: 1.0
"""


class Singleton(type):
    """A metaclass that implements the Singleton pattern."""
    _instance = {}

    def __call__(self, *args, **kwds):
        if self not in self._instance:
            self._instance[self] = super(Singleton, self).__call__(*args, **kwds)
        return self._instance[self]


class NetworkDriver(metaclass=Singleton):
    """Example class using the Singleton pattern."""
    
    def log(self):
        print(f"NetworkDriver instance id: {id(self)}\n")


def create_singleton():
    """Helper function to create and log a NetworkDriver instance."""
    singleton = NetworkDriver()
    singleton.log()
    return singleton


if __name__ == "__main__":
    driver1 = create_singleton()
    driver2 = create_singleton()
    driver3 = create_singleton()

    if id(driver1) == id(driver2) == id(driver3):
        print("All instances are the same. Singleton pattern works!")
    else:
        print("Instances are different. Singleton pattern failed.")