from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire import *
if GETSPIREPRODUCT(__file__) == "PDF":
    from spire.pdf.common import *
elif GETSPIREPRODUCT(__file__) == "XLS" :
    from spire.xls.common import *
elif GETSPIREPRODUCT(__file__) == "DOC" :
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class SizeF (SpireObject) :
    @dispatch
    def __init__(self, width:float, height:float):
        dlllib.SizeF_CreateWH.argtypes=[c_float,c_float]
        dlllib.SizeF_CreateWH.restype = c_void_p
        intPtr = dlllib.SizeF_CreateWH(width, height)
        super(SizeF, self).__init__(intPtr)

    @dispatch
    def __init__(self, size:'SizeF'):
        ptrSize:c_void_p = size.Ptr

        dlllib.SizeF_CreateS.argtypes=[c_void_p]
        dlllib.SizeF_CreateS.restype = c_void_p
        intPtr = dlllib.SizeF_CreateS(ptrSize)
        super(SizeF, self).__init__(intPtr)

    @dispatch
    def __init__(self, pointf:'PointF'):
        ptrPoint:c_void_p = pointf.Ptr

        dlllib.SizeF_CreateS.argtypes=[c_void_p]
        dlllib.SizeF_CreateS.restype = c_void_p
        intPtr = dlllib.SizeF_CreateS(ptrSize)
        super(SizeF, self).__init__(ptrPoint)
    """

    """
    @staticmethod

    def op_Addition(sz1:'SizeF',sz2:'SizeF')->'SizeF':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_op_Addition.restype=c_void_p
        intPtr = dlllib.SizeF_op_Addition( intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def op_Subtraction(sz1:'SizeF',sz2:'SizeF')->'SizeF':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_op_Subtraction.restype=c_void_p
        intPtr = dlllib.SizeF_op_Subtraction( intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def op_Equality(sz1:'SizeF',sz2:'SizeF')->bool:
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_op_Equality.restype=c_bool
        ret = dlllib.SizeF_op_Equality( intPtrsz1,intPtrsz2)
        return ret

    @staticmethod

    def op_Inequality(sz1:'SizeF',sz2:'SizeF')->bool:
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_op_Inequality.restype=c_bool
        ret = dlllib.SizeF_op_Inequality( intPtrsz1,intPtrsz2)
        return ret

    @staticmethod

    def op_Explicit(size:'SizeF')->'PointF':
        """

        """
        intPtrsize:c_void_p = size.Ptr

        dlllib.SizeF_op_Explicit.argtypes=[ c_void_p]
        dlllib.SizeF_op_Explicit.restype=c_void_p
        intPtr = dlllib.SizeF_op_Explicit( intPtrsize)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.SizeF_get_IsEmpty.argtypes=[c_void_p]
        dlllib.SizeF_get_IsEmpty.restype=c_bool
        ret = dlllib.SizeF_get_IsEmpty(self.Ptr)
        return ret

    @property
    def Width(self)->float:
        """

        """
        dlllib.SizeF_get_Width.argtypes=[c_void_p]
        dlllib.SizeF_get_Width.restype=c_float
        ret = dlllib.SizeF_get_Width(self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        dlllib.SizeF_set_Width.argtypes=[c_void_p, c_float]
        dlllib.SizeF_set_Width(self.Ptr, value)

    @property
    def Height(self)->float:
        """

        """
        dlllib.SizeF_get_Height.argtypes=[c_void_p]
        dlllib.SizeF_get_Height.restype=c_float
        ret = dlllib.SizeF_get_Height(self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        dlllib.SizeF_set_Height.argtypes=[c_void_p, c_float]
        dlllib.SizeF_set_Height(self.Ptr, value)

    @staticmethod

    def Add(sz1:'SizeF',sz2:'SizeF')->'SizeF':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_Add.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_Add.restype=c_void_p
        intPtr = dlllib.SizeF_Add( intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def Subtract(sz1:'SizeF',sz2:'SizeF')->'SizeF':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.SizeF_Subtract.argtypes=[ c_void_p,c_void_p]
        dlllib.SizeF_Subtract.restype=c_void_p
        intPtr = dlllib.SizeF_Subtract( intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.SizeF_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.SizeF_Equals.restype=c_bool
        ret = dlllib.SizeF_Equals(self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.SizeF_GetHashCode.argtypes=[c_void_p]
        dlllib.SizeF_GetHashCode.restype=c_int
        ret = dlllib.SizeF_GetHashCode(self.Ptr)
        return ret


    def ToPointF(self)->'PointF':
        """

        """
        dlllib.SizeF_ToPointF.argtypes=[c_void_p]
        dlllib.SizeF_ToPointF.restype=c_void_p
        intPtr = dlllib.SizeF_ToPointF(self.Ptr)
        ret = None if intPtr==None else PointF(intPtr)
        return ret



    def ToSize(self)->'Size':
        """

        """
        dlllib.SizeF_ToSize.argtypes=[c_void_p]
        dlllib.SizeF_ToSize.restype=c_void_p
        intPtr = dlllib.SizeF_ToSize(self.Ptr)
        ret = None if intPtr==None else Size(intPtr)
        return ret



    def ToString(self)->str:
        """

        """
        dlllib.SizeF_ToString.argtypes=[c_void_p]
        dlllib.SizeF_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.SizeF_ToString(self.Ptr))
        return ret


    @staticmethod

    def Empty()->'SizeF':
        """

        """
        #dlllib.SizeF_Empty.argtypes=[]
        dlllib.SizeF_Empty.restype=c_void_p
        intPtr = dlllib.SizeF_Empty()
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


