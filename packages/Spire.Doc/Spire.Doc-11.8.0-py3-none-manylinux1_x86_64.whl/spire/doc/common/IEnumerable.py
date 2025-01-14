from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire import *
if GETSPIREPRODUCT(__file__) == "PDF":
    from spire.pdf.common import *
    from spire.pdf.common.IEnumerator import IEnumerator
elif GETSPIREPRODUCT(__file__) == "XLS" :
    from spire.xls.common import *
    from spire.xls.common.IEnumerator import IEnumerator
elif GETSPIREPRODUCT(__file__) == "DOC" :
    from spire.doc.common import *
    from spire.doc.common.IEnumerator import IEnumerator
else :
    from spire.presentation.common import *
    from spire.presentation.common.IEnumerator import IEnumerator
#from spire.xls import *
from ctypes import *
import abc



T = TypeVar("T", bound=SpireObject)
class IEnumerable (SpireObject, Generic[T]) :
    """

    """
    def __iter__(self)->IEnumerator[T]:
        return self.GetEnumerator()

    def GetEnumerator(self)->IEnumerator[T]:
        """

        """
        dlllib.IEnumerable_GetEnumerator.argtypes=[c_void_p]
        dlllib.IEnumerable_GetEnumerator.restype=c_void_p
        intPtr = dlllib.IEnumerable_GetEnumerator(self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        ret._gtype = self.__orig_bases__[0].__args__[0]
        return ret


