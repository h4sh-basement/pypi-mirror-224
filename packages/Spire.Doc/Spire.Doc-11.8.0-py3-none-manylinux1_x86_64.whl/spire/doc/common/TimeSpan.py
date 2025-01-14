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

class TimeSpan (SpireObject) :
    """

    """
    @property
    def Ticks(self)->int:
        """

        """
        dlllib.TimeSpan_get_Ticks.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Ticks.restype=c_long
        ret = dlllib.TimeSpan_get_Ticks(self.Ptr)
        return ret

    @property
    def Days(self)->int:
        """

        """
        dlllib.TimeSpan_get_Days.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Days.restype=c_int
        ret = dlllib.TimeSpan_get_Days(self.Ptr)
        return ret

    @property
    def Hours(self)->int:
        """

        """
        dlllib.TimeSpan_get_Hours.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Hours.restype=c_int
        ret = dlllib.TimeSpan_get_Hours(self.Ptr)
        return ret

    @property
    def Milliseconds(self)->int:
        """

        """
        dlllib.TimeSpan_get_Milliseconds.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Milliseconds.restype=c_int
        ret = dlllib.TimeSpan_get_Milliseconds(self.Ptr)
        return ret

    @property
    def Minutes(self)->int:
        """

        """
        dlllib.TimeSpan_get_Minutes.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Minutes.restype=c_int
        ret = dlllib.TimeSpan_get_Minutes(self.Ptr)
        return ret

    @property
    def Seconds(self)->int:
        """

        """
        dlllib.TimeSpan_get_Seconds.argtypes=[c_void_p]
        dlllib.TimeSpan_get_Seconds.restype=c_int
        ret = dlllib.TimeSpan_get_Seconds(self.Ptr)
        return ret

    @property
    def TotalDays(self)->float:
        """

        """
        dlllib.TimeSpan_get_TotalDays.argtypes=[c_void_p]
        dlllib.TimeSpan_get_TotalDays.restype=c_double
        ret = dlllib.TimeSpan_get_TotalDays(self.Ptr)
        return ret

    @property
    def TotalHours(self)->float:
        """

        """
        dlllib.TimeSpan_get_TotalHours.argtypes=[c_void_p]
        dlllib.TimeSpan_get_TotalHours.restype=c_double
        ret = dlllib.TimeSpan_get_TotalHours(self.Ptr)
        return ret

    @property
    def TotalMilliseconds(self)->float:
        """

        """
        dlllib.TimeSpan_get_TotalMilliseconds.argtypes=[c_void_p]
        dlllib.TimeSpan_get_TotalMilliseconds.restype=c_double
        ret = dlllib.TimeSpan_get_TotalMilliseconds(self.Ptr)
        return ret

    @property
    def TotalMinutes(self)->float:
        """

        """
        dlllib.TimeSpan_get_TotalMinutes.argtypes=[c_void_p]
        dlllib.TimeSpan_get_TotalMinutes.restype=c_double
        ret = dlllib.TimeSpan_get_TotalMinutes(self.Ptr)
        return ret

    @property
    def TotalSeconds(self)->float:
        """

        """
        dlllib.TimeSpan_get_TotalSeconds.argtypes=[c_void_p]
        dlllib.TimeSpan_get_TotalSeconds.restype=c_double
        ret = dlllib.TimeSpan_get_TotalSeconds(self.Ptr)
        return ret


    def Add(self ,ts:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrts:c_void_p = ts.Ptr

        dlllib.TimeSpan_Add.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_Add.restype=c_void_p
        intPtr = dlllib.TimeSpan_Add(self.Ptr, intPtrts)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def Compare(t1:'TimeSpan',t2:'TimeSpan')->int:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_Compare.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_Compare.restype=c_int
        ret = dlllib.TimeSpan_Compare( intPtrt1,intPtrt2)
        return ret

    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.TimeSpan_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_CompareTo.restype=c_int
        ret = dlllib.TimeSpan_CompareTo(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'TimeSpan')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.TimeSpan_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_CompareToV.restype=c_int
        ret = dlllib.TimeSpan_CompareToV(self.Ptr, intPtrvalue)
        return ret

    @staticmethod

    def FromDays(value:float)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromDays.argtypes=[ c_double]
        dlllib.TimeSpan_FromDays.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromDays( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret



    def Duration(self)->'TimeSpan':
        """

        """
        dlllib.TimeSpan_Duration.argtypes=[c_void_p]
        dlllib.TimeSpan_Duration.restype=c_void_p
        intPtr = dlllib.TimeSpan_Duration(self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @dispatch

    def Equals(self ,value:SpireObject)->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.TimeSpan_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_Equals.restype=c_bool
        ret = dlllib.TimeSpan_Equals(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,obj:'TimeSpan')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.TimeSpan_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_EqualsO.restype=c_bool
        ret = dlllib.TimeSpan_EqualsO(self.Ptr, intPtrobj)
        return ret

    @staticmethod
    @dispatch

    def Equals(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_EqualsTT.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_EqualsTT.restype=c_bool
        ret = dlllib.TimeSpan_EqualsTT( intPtrt1,intPtrt2)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.TimeSpan_GetHashCode.argtypes=[c_void_p]
        dlllib.TimeSpan_GetHashCode.restype=c_int
        ret = dlllib.TimeSpan_GetHashCode(self.Ptr)
        return ret

    @staticmethod

    def FromHours(value:float)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromHours.argtypes=[ c_double]
        dlllib.TimeSpan_FromHours.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromHours( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def FromMilliseconds(value:float)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromMilliseconds.argtypes=[ c_double]
        dlllib.TimeSpan_FromMilliseconds.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromMilliseconds( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def FromMinutes(value:float)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromMinutes.argtypes=[ c_double]
        dlllib.TimeSpan_FromMinutes.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromMinutes( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret



    def Negate(self)->'TimeSpan':
        """

        """
        dlllib.TimeSpan_Negate.argtypes=[c_void_p]
        dlllib.TimeSpan_Negate.restype=c_void_p
        intPtr = dlllib.TimeSpan_Negate(self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def FromSeconds(value:float)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromSeconds.argtypes=[ c_double]
        dlllib.TimeSpan_FromSeconds.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromSeconds( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret



    def Subtract(self ,ts:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrts:c_void_p = ts.Ptr

        dlllib.TimeSpan_Subtract.argtypes=[c_void_p ,c_void_p]
        dlllib.TimeSpan_Subtract.restype=c_void_p
        intPtr = dlllib.TimeSpan_Subtract(self.Ptr, intPtrts)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def FromTicks(value:int)->'TimeSpan':
        """

        """
        
        dlllib.TimeSpan_FromTicks.argtypes=[ c_long]
        dlllib.TimeSpan_FromTicks.restype=c_void_p
        intPtr = dlllib.TimeSpan_FromTicks( value)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod
    @dispatch

    def Parse(s:str)->'TimeSpan':
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            sPtr = StrToPtr(s)
            dlllib.TimeSpan_Parse.argtypes=[ c_char_p]
            dlllib.TimeSpan_Parse.restype=c_void_p
            intPtr = dlllib.TimeSpan_Parse(sPtr)
            ret = None if intPtr==None else TimeSpan(intPtr)
            return ret
        else:
            dlllib.TimeSpan_Parse.argtypes=[ c_void_p]
            dlllib.TimeSpan_Parse.restype=c_void_p
            intPtr = dlllib.TimeSpan_Parse( s)
            ret = None if intPtr==None else TimeSpan(intPtr)
            return ret
        


#    @staticmethod
#    @dispatch
#
#    def Parse(input:str,formatProvider:'IFormatProvider')->'TimeSpan':
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#
#        dlllib.TimeSpan_ParseIF.argtypes=[ c_void_p,c_void_p]
#        dlllib.TimeSpan_ParseIF.restype=c_void_p
#        intPtr = dlllib.TimeSpan_ParseIF( input,intPtrformatProvider)
#        ret = None if intPtr==None else TimeSpan(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(input:str,format:str,formatProvider:'IFormatProvider')->'TimeSpan':
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#
#        dlllib.TimeSpan_ParseExact.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.TimeSpan_ParseExact.restype=c_void_p
#        intPtr = dlllib.TimeSpan_ParseExact( input,format,intPtrformatProvider)
#        ret = None if intPtr==None else TimeSpan(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(input:str,formats:List[str],formatProvider:'IFormatProvider')->'TimeSpan':
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#
#        dlllib.TimeSpan_ParseExactIFF.argtypes=[ c_void_p,ArrayTypeformats,c_void_p]
#        dlllib.TimeSpan_ParseExactIFF.restype=c_void_p
#        intPtr = dlllib.TimeSpan_ParseExactIFF( input,arrayformats,intPtrformatProvider)
#        ret = None if intPtr==None else TimeSpan(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'TimeSpan&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.TimeSpan_TryParse.restype=c_bool
#        ret = dlllib.TimeSpan_TryParse( s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(input:str,formatProvider:'IFormatProvider',result:'TimeSpan&')->bool:
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParseIFR.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.TimeSpan_TryParseIFR.restype=c_bool
#        ret = dlllib.TimeSpan_TryParseIFR( input,intPtrformatProvider,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(input:str,format:str,formatProvider:'IFormatProvider',result:'TimeSpan&')->bool:
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParseExact.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p]
#        dlllib.TimeSpan_TryParseExact.restype=c_bool
#        ret = dlllib.TimeSpan_TryParseExact( input,format,intPtrformatProvider,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(input:str,formats:List[str],formatProvider:'IFormatProvider',result:'TimeSpan&')->bool:
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParseExactIFFR.argtypes=[ c_void_p,ArrayTypeformats,c_void_p,c_void_p]
#        dlllib.TimeSpan_TryParseExactIFFR.restype=c_bool
#        ret = dlllib.TimeSpan_TryParseExactIFFR( input,arrayformats,intPtrformatProvider,intPtrresult)
#        return ret


    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.TimeSpan_ToString.argtypes=[c_void_p]
        dlllib.TimeSpan_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.TimeSpan_ToString(self.Ptr))
        return ret


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            formatPtr = StrToPtr(format)
            dlllib.TimeSpan_ToStringF.argtypes=[c_void_p ,c_char_p]
            dlllib.TimeSpan_ToStringF.restype=c_void_p
            ret = PtrToStr(dlllib.TimeSpan_ToStringF(self.Ptr,formatPtr))
            return ret
        else:
            dlllib.TimeSpan_ToStringF.argtypes=[c_void_p ,c_void_p]
            dlllib.TimeSpan_ToStringF.restype=c_void_p
            ret = PtrToStr(dlllib.TimeSpan_ToStringF(self.Ptr, format))
            return ret
        


#    @dispatch
#
#    def ToString(self ,format:str,formatProvider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#
#        dlllib.TimeSpan_ToStringFF.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.TimeSpan_ToStringFF.restype=c_wchar_p
#        ret = dlllib.TimeSpan_ToStringFF(self.Ptr, format,intPtrformatProvider)
#        return ret
#


    @staticmethod

    def op_UnaryNegation(t:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrt:c_void_p = t.Ptr

        dlllib.TimeSpan_op_UnaryNegation.argtypes=[ c_void_p]
        dlllib.TimeSpan_op_UnaryNegation.restype=c_void_p
        intPtr = dlllib.TimeSpan_op_UnaryNegation( intPtrt)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def op_Subtraction(t1:'TimeSpan',t2:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_Subtraction.restype=c_void_p
        intPtr = dlllib.TimeSpan_op_Subtraction( intPtrt1,intPtrt2)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def op_UnaryPlus(t:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrt:c_void_p = t.Ptr

        dlllib.TimeSpan_op_UnaryPlus.argtypes=[ c_void_p]
        dlllib.TimeSpan_op_UnaryPlus.restype=c_void_p
        intPtr = dlllib.TimeSpan_op_UnaryPlus( intPtrt)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def op_Addition(t1:'TimeSpan',t2:'TimeSpan')->'TimeSpan':
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_Addition.restype=c_void_p
        intPtr = dlllib.TimeSpan_op_Addition( intPtrt1,intPtrt2)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def op_Equality(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_Equality.restype=c_bool
        ret = dlllib.TimeSpan_op_Equality( intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_Inequality(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_Inequality.restype=c_bool
        ret = dlllib.TimeSpan_op_Inequality( intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_LessThan(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_LessThan.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_LessThan.restype=c_bool
        ret = dlllib.TimeSpan_op_LessThan( intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_LessThanOrEqual(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_LessThanOrEqual.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_LessThanOrEqual.restype=c_bool
        ret = dlllib.TimeSpan_op_LessThanOrEqual( intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_GreaterThan(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_GreaterThan.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_GreaterThan.restype=c_bool
        ret = dlllib.TimeSpan_op_GreaterThan( intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_GreaterThanOrEqual(t1:'TimeSpan',t2:'TimeSpan')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.TimeSpan_op_GreaterThanOrEqual.argtypes=[ c_void_p,c_void_p]
        dlllib.TimeSpan_op_GreaterThanOrEqual.restype=c_bool
        ret = dlllib.TimeSpan_op_GreaterThanOrEqual( intPtrt1,intPtrt2)
        return ret

#    @staticmethod
#    @dispatch
#
#    def ParseExact(input:str,format:str,formatProvider:'IFormatProvider',styles:'TimeSpanStyles')->'TimeSpan':
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        enumstyles:c_int = styles.value
#
#        dlllib.TimeSpan_ParseExactIFFS.argtypes=[ c_void_p,c_void_p,c_void_p,c_int]
#        dlllib.TimeSpan_ParseExactIFFS.restype=c_void_p
#        intPtr = dlllib.TimeSpan_ParseExactIFFS( input,format,intPtrformatProvider,enumstyles)
#        ret = None if intPtr==None else TimeSpan(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(input:str,formats:List[str],formatProvider:'IFormatProvider',styles:'TimeSpanStyles')->'TimeSpan':
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        enumstyles:c_int = styles.value
#
#        dlllib.TimeSpan_ParseExactIFFS1.argtypes=[ c_void_p,ArrayTypeformats,c_void_p,c_int]
#        dlllib.TimeSpan_ParseExactIFFS1.restype=c_void_p
#        intPtr = dlllib.TimeSpan_ParseExactIFFS1( input,arrayformats,intPtrformatProvider,enumstyles)
#        ret = None if intPtr==None else TimeSpan(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(input:str,format:str,formatProvider:'IFormatProvider',styles:'TimeSpanStyles',result:'TimeSpan&')->bool:
#        """
#
#        """
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        enumstyles:c_int = styles.value
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParseExactIFFSR.argtypes=[ c_void_p,c_void_p,c_void_p,c_int,c_void_p]
#        dlllib.TimeSpan_TryParseExactIFFSR.restype=c_bool
#        ret = dlllib.TimeSpan_TryParseExactIFFSR( input,format,intPtrformatProvider,enumstyles,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(input:str,formats:List[str],formatProvider:'IFormatProvider',styles:'TimeSpanStyles',result:'TimeSpan&')->bool:
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrformatProvider:c_void_p = formatProvider.Ptr
#        enumstyles:c_int = styles.value
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.TimeSpan_TryParseExactIFFSR1.argtypes=[ c_void_p,ArrayTypeformats,c_void_p,c_int,c_void_p]
#        dlllib.TimeSpan_TryParseExactIFFSR1.restype=c_bool
#        ret = dlllib.TimeSpan_TryParseExactIFFSR1( input,arrayformats,intPtrformatProvider,enumstyles,intPtrresult)
#        return ret


    @staticmethod

    def Zero()->'TimeSpan':
        """

        """
        #dlllib.TimeSpan_Zero.argtypes=[]
        dlllib.TimeSpan_Zero.restype=c_void_p
        intPtr = dlllib.TimeSpan_Zero()
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def MaxValue()->'TimeSpan':
        """

        """
        #dlllib.TimeSpan_MaxValue.argtypes=[]
        dlllib.TimeSpan_MaxValue.restype=c_void_p
        intPtr = dlllib.TimeSpan_MaxValue()
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def MinValue()->'TimeSpan':
        """

        """
        #dlllib.TimeSpan_MinValue.argtypes=[]
        dlllib.TimeSpan_MinValue.restype=c_void_p
        intPtr = dlllib.TimeSpan_MinValue()
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod
    def TicksPerMillisecond()->int:
        """

        """
        #dlllib.TimeSpan_TicksPerMillisecond.argtypes=[]
        dlllib.TimeSpan_TicksPerMillisecond.restype=c_long
        ret = dlllib.TimeSpan_TicksPerMillisecond()
        return ret

    @staticmethod
    def TicksPerSecond()->int:
        """

        """
        #dlllib.TimeSpan_TicksPerSecond.argtypes=[]
        dlllib.TimeSpan_TicksPerSecond.restype=c_long
        ret = dlllib.TimeSpan_TicksPerSecond()
        return ret

    @staticmethod
    def TicksPerMinute()->int:
        """

        """
        #dlllib.TimeSpan_TicksPerMinute.argtypes=[]
        dlllib.TimeSpan_TicksPerMinute.restype=c_long
        ret = dlllib.TimeSpan_TicksPerMinute()
        return ret

    @staticmethod
    def TicksPerHour()->int:
        """

        """
        #dlllib.TimeSpan_TicksPerHour.argtypes=[]
        dlllib.TimeSpan_TicksPerHour.restype=c_long
        ret = dlllib.TimeSpan_TicksPerHour()
        return ret

    @staticmethod
    def TicksPerDay()->int:
        """

        """
        #dlllib.TimeSpan_TicksPerDay.argtypes=[]
        dlllib.TimeSpan_TicksPerDay.restype=c_long
        ret = dlllib.TimeSpan_TicksPerDay()
        return ret

