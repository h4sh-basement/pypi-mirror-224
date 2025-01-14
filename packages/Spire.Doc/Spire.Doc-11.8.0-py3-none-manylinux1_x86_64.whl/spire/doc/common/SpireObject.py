from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from ctypes import *
import abc
from spire import *
if GETSPIREPRODUCT(__file__) == "PDF":
    from spire.pdf.common import *
elif GETSPIREPRODUCT(__file__) == "XLS" :
    from spire.xls.common import *
elif GETSPIREPRODUCT(__file__) == "DOC" :
    from spire.doc.common import *
else :
    from spire.presentation.common import *

class SpireObject(object):
    
    @dispatch
    def __init__(self, ptr):
        self._ptr = ptr
        self._gtype = None
    @dispatch
    def __init__(self, obj:'SpireObject'):
        self._ptr = obj.Ptr
        self._gtype = None
    @property
    def Ptr(self):
        return self._ptr

    def __del__(self):
        dlllib.Spire_FreeHandle.argtypes = [c_void_p]
        dlllib.Spire_FreeHandle(self.Ptr)

    #support x[]
    def __getitem__(self, key):
        #try:
        ret = self.get_Item(key)
        #    if ret == None:
        #        raise StopIteration()
        return ret
        #except:
        #    raise StopIteration()

    @dispatch
    def get_Item(self ,key:tuple):
        l = len(key)
        if(l == 1):
            return self.get_Item(key[0])
        elif(l == 2):
            return self.get_Item(key[0],key[1])
        elif(l == 3):
            return self.get_Item(key[0],key[1],key[2])
        elif(l == 4):
            return self.get_Item(key[0],key[1],key[2],key[3])
        else:
            return Exception("argument not correct")

    #support len()
    def __len__(self):
        return self.Count

    @property
    def Length(self):
        return self.Count

    #__enter__ / __exit__ support with .... as
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        try:
           getattr(self,"Close")
           self.Close()
        except:
            pass
        try:
           getattr(self,"Dispose")
           self.Dispose()
        except:
            pass
            