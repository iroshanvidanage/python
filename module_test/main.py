from abc import ABC, abstractmethod


class Phone(ABC):
   @abstractmethod
   def func(self):
       pass


class Samsung(Phone):
   def func(self):
       pass


obJ = Samsung()
