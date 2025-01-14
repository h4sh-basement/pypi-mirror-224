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

class Point (SpireObject) :
    """

    """
    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.Point_get_IsEmpty.argtypes=[c_void_p]
        dlllib.Point_get_IsEmpty.restype=c_bool
        ret = dlllib.Point_get_IsEmpty(self.Ptr)
        return ret

    @property
    def X(self)->int:
        """

        """
        dlllib.Point_get_X.argtypes=[c_void_p]
        dlllib.Point_get_X.restype=c_int
        ret = dlllib.Point_get_X(self.Ptr)
        return ret

    @X.setter
    def X(self, value:int):
        dlllib.Point_set_X.argtypes=[c_void_p, c_int]
        dlllib.Point_set_X(self.Ptr, value)

    @property
    def Y(self)->int:
        """

        """
        dlllib.Point_get_Y.argtypes=[c_void_p]
        dlllib.Point_get_Y.restype=c_int
        ret = dlllib.Point_get_Y(self.Ptr)
        return ret

    @Y.setter
    def Y(self, value:int):
        dlllib.Point_set_Y.argtypes=[c_void_p, c_int]
        dlllib.Point_set_Y(self.Ptr, value)

    @staticmethod

    def op_Implicit(p:'Point')->'PointF':
        """

        """
        intPtrp:c_void_p = p.Ptr

        dlllib.Point_op_Implicit.argtypes=[ c_void_p]
        dlllib.Point_op_Implicit.restype=c_void_p
        intPtr = dlllib.Point_op_Implicit( intPtrp)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod

    def op_Explicit(p:'Point')->'Size':
        """

        """
        intPtrp:c_void_p = p.Ptr

        dlllib.Point_op_Explicit.argtypes=[ c_void_p]
        dlllib.Point_op_Explicit.restype=c_void_p
        intPtr = dlllib.Point_op_Explicit( intPtrp)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def op_Addition(pt:'Point',sz:'Size')->'Point':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.Point_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_op_Addition.restype=c_void_p
        intPtr = dlllib.Point_op_Addition( intPtrpt,intPtrsz)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def op_Subtraction(pt:'Point',sz:'Size')->'Point':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.Point_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_op_Subtraction.restype=c_void_p
        intPtr = dlllib.Point_op_Subtraction( intPtrpt,intPtrsz)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def op_Equality(left:'Point',right:'Point')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Point_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_op_Equality.restype=c_bool
        ret = dlllib.Point_op_Equality( intPtrleft,intPtrright)
        return ret

    @staticmethod

    def op_Inequality(left:'Point',right:'Point')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Point_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_op_Inequality.restype=c_bool
        ret = dlllib.Point_op_Inequality( intPtrleft,intPtrright)
        return ret

    @staticmethod

    def Add(pt:'Point',sz:'Size')->'Point':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.Point_Add.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_Add.restype=c_void_p
        intPtr = dlllib.Point_Add( intPtrpt,intPtrsz)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def Subtract(pt:'Point',sz:'Size')->'Point':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.Point_Subtract.argtypes=[ c_void_p,c_void_p]
        dlllib.Point_Subtract.restype=c_void_p
        intPtr = dlllib.Point_Subtract( intPtrpt,intPtrsz)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def Ceiling(value:'PointF')->'Point':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Point_Ceiling.argtypes=[ c_void_p]
        dlllib.Point_Ceiling.restype=c_void_p
        intPtr = dlllib.Point_Ceiling( intPtrvalue)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def Truncate(value:'PointF')->'Point':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Point_Truncate.argtypes=[ c_void_p]
        dlllib.Point_Truncate.restype=c_void_p
        intPtr = dlllib.Point_Truncate( intPtrvalue)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @staticmethod

    def Round(value:'PointF')->'Point':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Point_Round.argtypes=[ c_void_p]
        dlllib.Point_Round.restype=c_void_p
        intPtr = dlllib.Point_Round( intPtrvalue)
        ret = None if intPtr==None else Point(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Point_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Point_Equals.restype=c_bool
        ret = dlllib.Point_Equals(self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Point_GetHashCode.argtypes=[c_void_p]
        dlllib.Point_GetHashCode.restype=c_int
        ret = dlllib.Point_GetHashCode(self.Ptr)
        return ret

    @dispatch

    def Offset(self ,dx:int,dy:int):
        """

        """
        
        dlllib.Point_Offset.argtypes=[c_void_p ,c_int,c_int]
        dlllib.Point_Offset(self.Ptr, dx,dy)

    @dispatch

    def Offset(self ,p:'Point'):
        """

        """
        intPtrp:c_void_p = p.Ptr

        dlllib.Point_OffsetP.argtypes=[c_void_p ,c_void_p]
        dlllib.Point_OffsetP(self.Ptr, intPtrp)


    def ToString(self)->str:
        """

        """
        dlllib.Point_ToString.argtypes=[c_void_p]
        dlllib.Point_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Point_ToString(self.Ptr))
        return ret


    @staticmethod

    def Empty()->'Point':
        """

        """
        #dlllib.Point_Empty.argtypes=[]
        dlllib.Point_Empty.restype=c_void_p
        intPtr = dlllib.Point_Empty()
        ret = None if intPtr==None else Point(intPtr)
        return ret


