from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocProperty (abc.ABC) :
    """

    """
    @property
    @abc.abstractmethod
    def IsBuiltIn(self)->bool:
        """

        """
        pass


    @property

    @abc.abstractmethod
    def PropertyId(self)->'BuiltInProperty':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Name(self)->str:
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Value(self)->'SpireObject':
        """

        """
        pass


    @Value.setter
    @abc.abstractmethod
    def Value(self, value:'SpireObject'):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Boolean(self)->bool:
        """

        """
        pass


    @Boolean.setter
    @abc.abstractmethod
    def Boolean(self, value:bool):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Integer(self)->int:
        """

        """
        pass


    @Integer.setter
    @abc.abstractmethod
    def Integer(self, value:int):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Int32(self)->int:
        """

        """
        pass


    @Int32.setter
    @abc.abstractmethod
    def Int32(self, value:int):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def Double(self)->float:
        """

        """
        pass


    @Double.setter
    @abc.abstractmethod
    def Double(self, value:float):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Text(self)->str:
        """

        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def DateTime(self)->'DateTime':
        """

        """
        pass


    @DateTime.setter
    @abc.abstractmethod
    def DateTime(self, value:'DateTime'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def TimeSpan(self)->'TimeSpan':
        """

        """
        pass


    @TimeSpan.setter
    @abc.abstractmethod
    def TimeSpan(self, value:'TimeSpan'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def LinkSource(self)->str:
        """

        """
        pass


    @LinkSource.setter
    @abc.abstractmethod
    def LinkSource(self, value:str):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def LinkToContent(self)->bool:
        """

        """
        pass


    @LinkToContent.setter
    @abc.abstractmethod
    def LinkToContent(self, value:bool):
        """

        """
        pass


