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

class Int16 (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Int16_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Int16_CompareTo.restype=c_int
        ret = dlllib.Int16_CompareTo(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'Int16')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Int16_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.Int16_CompareToV.restype=c_int
        ret = dlllib.Int16_CompareToV(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Int16_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Int16_Equals.restype=c_bool
        ret = dlllib.Int16_Equals(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:'Int16')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Int16_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.Int16_EqualsO.restype=c_bool
        ret = dlllib.Int16_EqualsO(self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Int16_GetHashCode.argtypes=[c_void_p]
        dlllib.Int16_GetHashCode.restype=c_int
        ret = dlllib.Int16_GetHashCode(self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Int16_ToString.argtypes=[c_void_p]
        dlllib.Int16_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Int16_ToString(self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int16_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Int16_ToStringP.restype=c_wchar_p
#        ret = dlllib.Int16_ToStringP(self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.Int16_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.Int16_ToStringF.restype=c_void_p
        ret = PtrToStr(dlllib.Int16_ToStringF(self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int16_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Int16_ToStringFP.restype=c_wchar_p
#        ret = dlllib.Int16_ToStringFP(self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->'Int16':
        """

        """
        
        dlllib.Int16_Parse.argtypes=[ c_void_p]
        dlllib.Int16_Parse.restype=c_void_p
        intPtr = dlllib.Int16_Parse( s)
        ret = None if intPtr==None else Int16(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->'Int16':
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.Int16_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.Int16_ParseSS.restype=c_void_p
#        intPtr = dlllib.Int16_ParseSS( s,enumstyle)
#        ret = None if intPtr==None else Int16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->'Int16':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int16_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.Int16_ParseSP.restype=c_void_p
#        intPtr = dlllib.Int16_ParseSP( s,intPtrprovider)
#        ret = None if intPtr==None else Int16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->'Int16':
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int16_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.Int16_ParseSSP.restype=c_void_p
#        intPtr = dlllib.Int16_ParseSSP( s,enumstyle,intPtrprovider)
#        ret = None if intPtr==None else Int16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'Int16&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Int16_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Int16_TryParse.restype=c_bool
#        ret = dlllib.Int16_TryParse( s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Int16&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Int16_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.Int16_TryParseSSPR.restype=c_bool
#        ret = dlllib.Int16_TryParseSSPR( s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Int16_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Int16_GetTypeCode.restype=c_int
#        ret = dlllib.Int16_GetTypeCode(self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod

    def MaxValue()->'Int16':
        """

        """
        #dlllib.Int16_MaxValue.argtypes=[]
        dlllib.Int16_MaxValue.restype=c_void_p
        intPtr = dlllib.Int16_MaxValue()
        ret = None if intPtr==None else Int16(intPtr)
        return ret


    @staticmethod

    def MinValue()->'Int16':
        """

        """
        #dlllib.Int16_MinValue.argtypes=[]
        dlllib.Int16_MinValue.restype=c_void_p
        intPtr = dlllib.Int16_MinValue()
        ret = None if intPtr==None else Int16(intPtr)
        return ret


