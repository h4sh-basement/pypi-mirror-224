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

class Single (SpireObject) :
    """

    """
    @staticmethod

    def IsInfinity(f:float)->bool:
        """

        """
        
        dlllib.Single_IsInfinity.argtypes=[ c_float]
        dlllib.Single_IsInfinity.restype=c_bool
        ret = dlllib.Single_IsInfinity( f)
        return ret

    @staticmethod

    def IsPositiveInfinity(f:float)->bool:
        """

        """
        
        dlllib.Single_IsPositiveInfinity.argtypes=[ c_float]
        dlllib.Single_IsPositiveInfinity.restype=c_bool
        ret = dlllib.Single_IsPositiveInfinity( f)
        return ret

    @staticmethod

    def IsNegativeInfinity(f:float)->bool:
        """

        """
        
        dlllib.Single_IsNegativeInfinity.argtypes=[ c_float]
        dlllib.Single_IsNegativeInfinity.restype=c_bool
        ret = dlllib.Single_IsNegativeInfinity( f)
        return ret

    @staticmethod

    def IsNaN(f:float)->bool:
        """

        """
        
        dlllib.Single_IsNaN.argtypes=[ c_float]
        dlllib.Single_IsNaN.restype=c_bool
        ret = dlllib.Single_IsNaN( f)
        return ret

    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Single_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Single_CompareTo.restype=c_int
        ret = dlllib.Single_CompareTo(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:float)->int:
        """

        """
        
        dlllib.Single_CompareToV.argtypes=[c_void_p ,c_float]
        dlllib.Single_CompareToV.restype=c_int
        ret = dlllib.Single_CompareToV(self.Ptr, value)
        return ret

    @staticmethod

    def op_Equality(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_Equality.argtypes=[ c_float,c_float]
        dlllib.Single_op_Equality.restype=c_bool
        ret = dlllib.Single_op_Equality( left,right)
        return ret

    @staticmethod

    def op_Inequality(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_Inequality.argtypes=[ c_float,c_float]
        dlllib.Single_op_Inequality.restype=c_bool
        ret = dlllib.Single_op_Inequality( left,right)
        return ret

    @staticmethod

    def op_LessThan(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_LessThan.argtypes=[ c_float,c_float]
        dlllib.Single_op_LessThan.restype=c_bool
        ret = dlllib.Single_op_LessThan( left,right)
        return ret

    @staticmethod

    def op_GreaterThan(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_GreaterThan.argtypes=[ c_float,c_float]
        dlllib.Single_op_GreaterThan.restype=c_bool
        ret = dlllib.Single_op_GreaterThan( left,right)
        return ret

    @staticmethod

    def op_LessThanOrEqual(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_LessThanOrEqual.argtypes=[ c_float,c_float]
        dlllib.Single_op_LessThanOrEqual.restype=c_bool
        ret = dlllib.Single_op_LessThanOrEqual( left,right)
        return ret

    @staticmethod

    def op_GreaterThanOrEqual(left:float,right:float)->bool:
        """

        """
        
        dlllib.Single_op_GreaterThanOrEqual.argtypes=[ c_float,c_float]
        dlllib.Single_op_GreaterThanOrEqual.restype=c_bool
        ret = dlllib.Single_op_GreaterThanOrEqual( left,right)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Single_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Single_Equals.restype=c_bool
        ret = dlllib.Single_Equals(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:float)->bool:
        """

        """
        
        dlllib.Single_EqualsO.argtypes=[c_void_p ,c_float]
        dlllib.Single_EqualsO.restype=c_bool
        ret = dlllib.Single_EqualsO(self.Ptr, obj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Single_GetHashCode.argtypes=[c_void_p]
        dlllib.Single_GetHashCode.restype=c_int
        ret = dlllib.Single_GetHashCode(self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Single_ToString.argtypes=[c_void_p]
        dlllib.Single_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Single_ToString(self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Single_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Single_ToStringP.restype=c_wchar_p
#        ret = dlllib.Single_ToStringP(self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.Single_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.Single_ToStringF.restype=c_void_p
        ret = PtrToStr(dlllib.Single_ToStringF(self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Single_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Single_ToStringFP.restype=c_wchar_p
#        ret = dlllib.Single_ToStringFP(self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->float:
        """

        """
        
        dlllib.Single_Parse.argtypes=[ c_void_p]
        dlllib.Single_Parse.restype=c_float
        ret = dlllib.Single_Parse( s)
        return ret

#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->float:
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.Single_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.Single_ParseSS.restype=c_float
#        ret = dlllib.Single_ParseSS( s,enumstyle)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->float:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Single_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.Single_ParseSP.restype=c_float
#        ret = dlllib.Single_ParseSP( s,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->float:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Single_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.Single_ParseSSP.restype=c_float
#        ret = dlllib.Single_ParseSSP( s,enumstyle,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'Single&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Single_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Single_TryParse.restype=c_bool
#        ret = dlllib.Single_TryParse( s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Single&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Single_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.Single_TryParseSSPR.restype=c_bool
#        ret = dlllib.Single_TryParseSSPR( s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Single_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Single_GetTypeCode.restype=c_int
#        ret = dlllib.Single_GetTypeCode(self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod
    def MinValue()->float:
        """

        """
        #dlllib.Single_MinValue.argtypes=[]
        dlllib.Single_MinValue.restype=c_float
        ret = dlllib.Single_MinValue()
        return ret

    @staticmethod
    def Epsilon()->float:
        """

        """
        #dlllib.Single_Epsilon.argtypes=[]
        dlllib.Single_Epsilon.restype=c_float
        ret = dlllib.Single_Epsilon()
        return ret

    @staticmethod
    def MaxValue()->float:
        """

        """
        #dlllib.Single_MaxValue.argtypes=[]
        dlllib.Single_MaxValue.restype=c_float
        ret = dlllib.Single_MaxValue()
        return ret

    @staticmethod
    def PositiveInfinity()->float:
        """

        """
        #dlllib.Single_PositiveInfinity.argtypes=[]
        dlllib.Single_PositiveInfinity.restype=c_float
        ret = dlllib.Single_PositiveInfinity()
        return ret

    @staticmethod
    def NegativeInfinity()->float:
        """

        """
        #dlllib.Single_NegativeInfinity.argtypes=[]
        dlllib.Single_NegativeInfinity.restype=c_float
        ret = dlllib.Single_NegativeInfinity()
        return ret

    @staticmethod
    def NaN()->float:
        """

        """
        #dlllib.Single_NaN.argtypes=[]
        dlllib.Single_NaN.restype=c_float
        ret = dlllib.Single_NaN()
        return ret

