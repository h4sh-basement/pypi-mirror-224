from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple,get_args
from spire import *
if GETSPIREPRODUCT(__file__) == "PDF":
    from spire.pdf.common import *
    from spire.pdf.common.ICollection import ICollection
elif GETSPIREPRODUCT(__file__) == "XLS" :
    from spire.xls.common import *
    from spire.xls.common.ICollection import ICollection
elif GETSPIREPRODUCT(__file__) == "DOC" :
    from spire.doc.common import *
    from spire.doc.common.ICollection import ICollection
else :
    from spire.presentation.common import *
    from spire.presentation.common.ICollection import ICollection
#from spire.xls import *
from ctypes import *
import abc



T = TypeVar("T", bound=SpireObject)
class IList (  ICollection[T]) :
    """

    """
    #def __getitem__(self, key):
    #    return self.get_Item(key)
    def __init__(self, ptr):
        super(IList, self).__init__(ptr)
        self._gtype = self.__orig_bases__[0].__args__[0]

    def get_Item(self ,index:int)->T:
        """
        """
        obj = self._gtype
        dlllib.IListT_get_Item.argtypes=[c_void_p, c_int]
        dlllib.IListT_get_Item.restype = c_void_p
        intPtr = dlllib.IListT_get_Item(self.Ptr, index)
        ret = None if intPtr==None else obj(intPtr)
        return ret

    def set_Item(self ,index:int,value:T):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.IList_set_Item.argtypes=[c_void_p ,c_int,c_void_p]
        dlllib.IList_set_Item(self.Ptr, index,intPtrvalue)


    #def Add(self ,value:T)->int:
    #    """

    #    """
    #    intPtrvalue:c_void_p = value.Ptr

    #    dlllib.IList_Add.argtypes=[c_void_p ,c_void_p]
    #    dlllib.IList_Add.restype=c_int
    #    ret = dlllib.IList_Add(self.Ptr, intPtrvalue)
    #    return ret


    def Contains(self ,value:T)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.IList_Contains.argtypes=[c_void_p ,c_void_p]
        dlllib.IList_Contains.restype=c_int
        ret = dlllib.IList_Contains(self.Ptr, intPtrvalue)
        return ret

    def Clear(self):
        """

        """
        dlllib.IList_Clear.argtypes=[c_void_p]
        dlllib.IList_Clear(self.Ptr)

    @property
    def IsReadOnly(self)->int:
        """

        """
        dlllib.IList_get_IsReadOnly.argtypes=[c_void_p]
        dlllib.IList_get_IsReadOnly.restype=c_int
        ret = dlllib.IList_get_IsReadOnly(self.Ptr)
        return ret

    @property
    def IsFixedSize(self)->int:
        """

        """
        dlllib.IList_get_IsFixedSize.argtypes=[c_void_p]
        dlllib.IList_get_IsFixedSize.restype=c_int
        ret = dlllib.IList_get_IsFixedSize(self.Ptr)
        return ret


    def IndexOf(self ,value:T)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.IList_IndexOf.argtypes=[c_void_p ,c_void_p]
        dlllib.IList_IndexOf.restype=c_int
        ret = dlllib.IList_IndexOf(self.Ptr, intPtrvalue)
        return ret


    def Insert(self ,index:int,value:T):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.IList_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        dlllib.IList_Insert(self.Ptr, index,intPtrvalue)


    def Remove(self ,value:T):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.IList_Remove.argtypes=[c_void_p ,c_void_p]
        dlllib.IList_Remove(self.Ptr, intPtrvalue)


    def RemoveAt(self ,index:int):
        """

        """
        
        dlllib.IList_RemoveAt.argtypes=[c_void_p ,c_int]
        dlllib.IList_RemoveAt(self.Ptr, index)


