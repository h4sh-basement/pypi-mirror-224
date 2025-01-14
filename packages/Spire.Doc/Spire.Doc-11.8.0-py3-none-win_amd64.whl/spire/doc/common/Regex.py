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
from ctypes import *
import abc

class Regex (SpireObject) :
    """

    """
    @dispatch
    def __init__(self, pattern:str):
        if GETSPIREPRODUCT(__file__) == "DOC":
            patternPtr = StrToPtr(pattern)
            dlllib.Regex_CreateRegexP.argtypes = [c_char_p]
            dlllib.Regex_CreateRegexP.restype=c_void_p
            intPtr = dlllib.Regex_CreateRegexP(patternPtr)
            super(Regex, self).__init__(intPtr)
        else:
            dlllib.Regex_CreateRegexP.argtypes = [c_wchar_p]
            dlllib.Regex_CreateRegexP.restype=c_void_p
            intPtr = dlllib.Regex_CreateRegexP(pattern)
            super(Regex, self).__init__(intPtr)
        

    @dispatch
    def __init__(self, pattern:str, options:RegexOptions):
        if GETSPIREPRODUCT(__file__) == "DOC":
            patternPtr = StrToPtr(pattern)
            iTypeoptions:c_int = options.value
            dlllib.Regex_CreateRegexPO.argtypes=[c_char_p,c_int]
            dlllib.Regex_CreateRegexPO.restype=c_void_p
            intPtr = dlllib.Regex_CreateRegexPO(patternPtr,iTypeoptions)
            super(Regex, self).__init__(intPtr)
        else:
            iTypeoptions:c_int = options.value
            dlllib.Regex_CreateRegexPO.argtypes=[c_wchar_p,c_int]
            dlllib.Regex_CreateRegexPO.restype=c_void_p
            intPtr = dlllib.Regex_CreateRegexPO(pattern,iTypeoptions)
            super(Regex, self).__init__(intPtr)
        


    @staticmethod

    def Escape(valueStr:str)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            valueStrPtr = StrToPtr(valueStr)
            dlllib.Regex_Escape.argtypes=[ c_char_p]
            dlllib.Regex_Escape.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Escape(valueStrPtr))
            return ret
        else:
            dlllib.Regex_Escape.argtypes=[ c_wchar_p]
            dlllib.Regex_Escape.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Escape(valueStr))
            return ret
        return None
        


    @staticmethod

    def Unescape(valueStr:str)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            strPtr = StrToPtr(valueStr)
            dlllib.Regex_Unescape.argtypes=[ c_char_p]
            dlllib.Regex_Unescape.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Unescape(strPtr))
            return ret
        else:
            dlllib.Regex_Unescape.argtypes=[ c_wchar_p]
            dlllib.Regex_Unescape.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Unescape( valueStr))
            return ret
        


    @staticmethod
    def get_CacheSize()->int:
        """

        """
        #dlllib.Regex_get_CacheSize.argtypes=[]
        dlllib.Regex_get_CacheSize.restype=c_int
        ret = dlllib.Regex_get_CacheSize()
        return ret

    @staticmethod
    def set_CacheSize( value:int):
        dlllib.Regex_set_CacheSize.argtypes=[ c_int]
        dlllib.Regex_set_CacheSize( value)

    @property

    def Options(self)->'RegexOptions':
        """

        """
        dlllib.Regex_get_Options.argtypes=[c_void_p]
        dlllib.Regex_get_Options.restype=c_int
        ret = dlllib.Regex_get_Options(self.Ptr)
        objwraped = RegexOptions(ret)
        return objwraped

    @property

    def MatchTimeout(self)->'TimeSpan':
        """

        """
        dlllib.Regex_get_MatchTimeout.argtypes=[c_void_p]
        dlllib.Regex_get_MatchTimeout.restype=c_void_p
        intPtr = dlllib.Regex_get_MatchTimeout(self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @property
    def RightToLeft(self)->bool:
        """

        """
        dlllib.Regex_get_RightToLeft.argtypes=[c_void_p]
        dlllib.Regex_get_RightToLeft.restype=c_bool
        ret = dlllib.Regex_get_RightToLeft(self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.Regex_ToString.argtypes=[c_void_p]
        dlllib.Regex_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Regex_ToString(self.Ptr))
        return ret



    def GroupNameFromNumber(self ,i:int)->str:
        """

        """
        
        dlllib.Regex_GroupNameFromNumber.argtypes=[c_void_p ,c_int]
        dlllib.Regex_GroupNameFromNumber.restype=c_void_p
        ret = PtrToStr(dlllib.Regex_GroupNameFromNumber(self.Ptr, i))
        return ret



    def GroupNumberFromName(self ,name:str)->int:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            namePtr = StrToPtr(name)
            dlllib.Regex_GroupNumberFromName.argtypes=[c_void_p ,c_char_p]
            dlllib.Regex_GroupNumberFromName.restype=c_int
            ret = dlllib.Regex_GroupNumberFromName(self.Ptr, namePtr)
            return ret
        else:
            dlllib.Regex_GroupNumberFromName.argtypes=[c_void_p ,c_wchar_p]
            dlllib.Regex_GroupNumberFromName.restype=c_int
            ret = dlllib.Regex_GroupNumberFromName(self.Ptr, name)
            return ret
        

    @staticmethod
    @dispatch

    def IsMatch(input:str,pattern:str,options:RegexOptions,matchTimeout:TimeSpan)->bool:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_IsMatch.argtypes=[ c_char_p,c_char_p,c_int,c_void_p]
            dlllib.Regex_IsMatch.restype=c_bool
            ret = dlllib.Regex_IsMatch(inputPtr,patternPtr,enumoptions,intPtrmatchTimeout)
            return ret
        else:
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_IsMatch.argtypes=[ c_wchar_p,c_wchar_p,c_int,c_void_p]
            dlllib.Regex_IsMatch.restype=c_bool
            ret = dlllib.Regex_IsMatch( input,pattern,enumoptions,intPtrmatchTimeout)
            return ret
        

    @dispatch

    def IsMatch(self ,input:str)->bool:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            dlllib.Regex_IsMatchI.argtypes=[c_void_p ,c_char_p]
            dlllib.Regex_IsMatchI.restype=c_bool
            ret = dlllib.Regex_IsMatchI(self.Ptr, inputPtr)
            return ret
        else:
            dlllib.Regex_IsMatchI.argtypes=[c_void_p ,c_wchar_p]
            dlllib.Regex_IsMatchI.restype=c_bool
            ret = dlllib.Regex_IsMatchI(self.Ptr, input)
            return ret
        

    @dispatch

    def IsMatch(self ,input:str,startat:int)->bool:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            dlllib.Regex_IsMatchIS.argtypes=[c_void_p ,c_char_p,c_int]
            dlllib.Regex_IsMatchIS.restype=c_bool
            ret = dlllib.Regex_IsMatchIS(self.Ptr,inputPtr,startat)
            return ret
        else:
            dlllib.Regex_IsMatchIS.argtypes=[c_void_p ,c_wchar_p,c_int]
            dlllib.Regex_IsMatchIS.restype=c_bool
            ret = dlllib.Regex_IsMatchIS(self.Ptr, input,startat)
            return ret
        

#    @staticmethod
#    @dispatch
#
#    def Match(input:str,pattern:str,options:RegexOptions)->Match:
#        """
#
#        """
#        enumoptions:c_int = options.value
#
#        dlllib.Regex_Match.argtypes=[ c_wchar_p,c_wchar_p,c_int]
#        dlllib.Regex_Match.restype=c_void_p
#        intPtr = dlllib.Regex_Match( input,pattern,enumoptions)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Match(input:str,pattern:str,options:RegexOptions,matchTimeout:TimeSpan)->Match:
#        """
#
#        """
#        enumoptions:c_int = options.value
#        intPtrmatchTimeout:c_void_p = matchTimeout.Ptr
#
#        dlllib.Regex_MatchIPOM.argtypes=[ c_wchar_p,c_wchar_p,c_int,c_void_p]
#        dlllib.Regex_MatchIPOM.restype=c_void_p
#        intPtr = dlllib.Regex_MatchIPOM( input,pattern,enumoptions,intPtrmatchTimeout)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @dispatch
#
#    def Match(self ,input:str)->Match:
#        """
#
#        """
#        
#        dlllib.Regex_MatchI.argtypes=[c_void_p ,c_wchar_p]
#        dlllib.Regex_MatchI.restype=c_void_p
#        intPtr = dlllib.Regex_MatchI(self.Ptr, input)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @dispatch
#
#    def Match(self ,input:str,startat:int)->Match:
#        """
#
#        """
#        
#        dlllib.Regex_MatchIS.argtypes=[c_void_p ,c_wchar_p,c_int]
#        dlllib.Regex_MatchIS.restype=c_void_p
#        intPtr = dlllib.Regex_MatchIS(self.Ptr, input,startat)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @dispatch
#
#    def Match(self ,input:str,beginning:int,length:int)->Match:
#        """
#
#        """
#        
#        dlllib.Regex_MatchIBL.argtypes=[c_void_p ,c_wchar_p,c_int,c_int]
#        dlllib.Regex_MatchIBL.restype=c_void_p
#        intPtr = dlllib.Regex_MatchIBL(self.Ptr, input,beginning,length)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Matches(input:str,pattern:str,options:RegexOptions)->MatchCollection:
#        """
#
#        """
#        enumoptions:c_int = options.value
#
#        dlllib.Regex_Matches.argtypes=[ c_wchar_p,c_wchar_p,c_int]
#        dlllib.Regex_Matches.restype=c_void_p
#        intPtr = dlllib.Regex_Matches( input,pattern,enumoptions)
#        ret = None if intPtr==None else MatchCollection(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Matches(input:str,pattern:str,options:RegexOptions,matchTimeout:TimeSpan)->MatchCollection:
#        """
#
#        """
#        enumoptions:c_int = options.value
#        intPtrmatchTimeout:c_void_p = matchTimeout.Ptr
#
#        dlllib.Regex_MatchesIPOM.argtypes=[ c_wchar_p,c_wchar_p,c_int,c_void_p]
#        dlllib.Regex_MatchesIPOM.restype=c_void_p
#        intPtr = dlllib.Regex_MatchesIPOM( input,pattern,enumoptions,intPtrmatchTimeout)
#        ret = None if intPtr==None else MatchCollection(intPtr)
#        return ret
#


#    @dispatch
#
#    def Matches(self ,input:str)->MatchCollection:
#        """
#
#        """
#        
#        dlllib.Regex_MatchesI.argtypes=[c_void_p ,c_wchar_p]
#        dlllib.Regex_MatchesI.restype=c_void_p
#        intPtr = dlllib.Regex_MatchesI(self.Ptr, input)
#        ret = None if intPtr==None else MatchCollection(intPtr)
#        return ret
#


#    @dispatch
#
#    def Matches(self ,input:str,startat:int)->MatchCollection:
#        """
#
#        """
#        
#        dlllib.Regex_MatchesIS.argtypes=[c_void_p ,c_wchar_p,c_int]
#        dlllib.Regex_MatchesIS.restype=c_void_p
#        intPtr = dlllib.Regex_MatchesIS(self.Ptr, input,startat)
#        ret = None if intPtr==None else MatchCollection(intPtr)
#        return ret
#


    @staticmethod
    @dispatch

    def Replace(input:str,pattern:str,replacement:str)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            replacementPtr = StrToPtr(replacement)
            dlllib.Regex_Replace.argtypes=[ c_char_p,c_char_p,c_char_p]
            dlllib.Regex_Replace.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Replace(inputPtr,patternPtr,replacementPtr))
            return ret
        else:
            dlllib.Regex_Replace.argtypes=[ c_wchar_p,c_wchar_p,c_wchar_p]
            dlllib.Regex_Replace.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_Replace( input,pattern,replacement))
            return ret
        


    @staticmethod
    @dispatch

    def Replace(input:str,pattern:str,replacement:str,options:RegexOptions)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            replacementPtr = StrToPtr(replacement)
            enumoptions:c_int = options.value

            dlllib.Regex_ReplaceIPRO.argtypes=[ c_char_p,c_char_p,c_char_p,c_int]
            dlllib.Regex_ReplaceIPRO.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIPRO(inputPtr,patternPtr,replacementPtr,enumoptions))
            return ret
        else:
            enumoptions:c_int = options.value

            dlllib.Regex_ReplaceIPRO.argtypes=[ c_wchar_p,c_wchar_p,c_wchar_p,c_int]
            dlllib.Regex_ReplaceIPRO.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIPRO( input,pattern,replacement,enumoptions))
            return ret
        


    @staticmethod
    @dispatch

    def Replace(input:str,pattern:str,replacement:str,options:RegexOptions,matchTimeout:TimeSpan)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            replacementPtr = StrToPtr(replacement)
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_ReplaceIPROM.argtypes=[ c_char_p,c_char_p,c_char_p,c_int,c_void_p]
            dlllib.Regex_ReplaceIPROM.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIPROM(inputPtr,patternPtr,replacementPtr,enumoptions,intPtrmatchTimeout))
            return ret
        else:
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_ReplaceIPROM.argtypes=[ c_wchar_p,c_wchar_p,c_wchar_p,c_int,c_void_p]
            dlllib.Regex_ReplaceIPROM.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIPROM( input,pattern,replacement,enumoptions,intPtrmatchTimeout))
            return ret
        


    @dispatch

    def Replace(self ,input:str,replacement:str)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            replacementPtr = StrToPtr(replacement)
            dlllib.Regex_ReplaceIR.argtypes=[c_void_p ,c_char_p,c_char_p]
            dlllib.Regex_ReplaceIR.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIR(self.Ptr,inputPtr,replacementPtr))
            return ret
        else:
            dlllib.Regex_ReplaceIR.argtypes=[c_void_p ,c_wchar_p,c_wchar_p]
            dlllib.Regex_ReplaceIR.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIR(self.Ptr, input,replacement))
            return ret
        


    @dispatch

    def Replace(self ,input:str,replacement:str,count:int)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            replacementPtr = StrToPtr(replacement)
            dlllib.Regex_ReplaceIRC.argtypes=[c_void_p ,c_char_p,c_char_p,c_int]
            dlllib.Regex_ReplaceIRC.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIRC(self.Ptr,inputPtr,replacementPtr,count))
            return ret
        else:
            dlllib.Regex_ReplaceIRC.argtypes=[c_void_p ,c_wchar_p,c_wchar_p,c_int]
            dlllib.Regex_ReplaceIRC.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIRC(self.Ptr, input,replacement,count))
            return ret
        


    @dispatch

    def Replace(self ,input:str,replacement:str,count:int,startat:int)->str:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            replacementPtr = StrToPtr(replacement)
            dlllib.Regex_ReplaceIRCS.argtypes=[c_void_p ,c_char_p,c_char_p,c_int,c_int]
            dlllib.Regex_ReplaceIRCS.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIRCS(self.Ptr,inputPtr,replacementPtr,count,startat))
            return ret
        else:
            dlllib.Regex_ReplaceIRCS.argtypes=[c_void_p ,c_wchar_p,c_wchar_p,c_int,c_int]
            dlllib.Regex_ReplaceIRCS.restype=c_void_p
            ret = PtrToStr(dlllib.Regex_ReplaceIRCS(self.Ptr, input,replacement,count,startat))
            return ret
        


#    @staticmethod
#    @dispatch
#
#    def Replace(input:str,pattern:str,evaluator:'MatchEvaluator')->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#
#        dlllib.Regex_ReplaceIPE.argtypes=[ c_wchar_p,c_wchar_p,c_void_p]
#        dlllib.Regex_ReplaceIPE.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIPE( input,pattern,intPtrevaluator)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Replace(input:str,pattern:str,evaluator:'MatchEvaluator',options:RegexOptions)->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#        enumoptions:c_int = options.value
#
#        dlllib.Regex_ReplaceIPEO.argtypes=[ c_wchar_p,c_wchar_p,c_void_p,c_int]
#        dlllib.Regex_ReplaceIPEO.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIPEO( input,pattern,intPtrevaluator,enumoptions)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Replace(input:str,pattern:str,evaluator:'MatchEvaluator',options:RegexOptions,matchTimeout:TimeSpan)->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#        enumoptions:c_int = options.value
#        intPtrmatchTimeout:c_void_p = matchTimeout.Ptr
#
#        dlllib.Regex_ReplaceIPEOM.argtypes=[ c_wchar_p,c_wchar_p,c_void_p,c_int,c_void_p]
#        dlllib.Regex_ReplaceIPEOM.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIPEOM( input,pattern,intPtrevaluator,enumoptions,intPtrmatchTimeout)
#        return ret
#


#    @dispatch
#
#    def Replace(self ,input:str,evaluator:'MatchEvaluator')->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#
#        dlllib.Regex_ReplaceIE.argtypes=[c_void_p ,c_wchar_p,c_void_p]
#        dlllib.Regex_ReplaceIE.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIE(self.Ptr, input,intPtrevaluator)
#        return ret
#


#    @dispatch
#
#    def Replace(self ,input:str,evaluator:'MatchEvaluator',count:int)->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#
#        dlllib.Regex_ReplaceIEC.argtypes=[c_void_p ,c_wchar_p,c_void_p,c_int]
#        dlllib.Regex_ReplaceIEC.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIEC(self.Ptr, input,intPtrevaluator,count)
#        return ret
#


#    @dispatch
#
#    def Replace(self ,input:str,evaluator:'MatchEvaluator',count:int,startat:int)->str:
#        """
#
#        """
#        intPtrevaluator:c_void_p = evaluator.Ptr
#
#        dlllib.Regex_ReplaceIECS.argtypes=[c_void_p ,c_wchar_p,c_void_p,c_int,c_int]
#        dlllib.Regex_ReplaceIECS.restype=c_wchar_p
#        ret = dlllib.Regex_ReplaceIECS(self.Ptr, input,intPtrevaluator,count,startat)
#        return ret
#


    @staticmethod
    @dispatch

    def Split(input:str,pattern:str)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            dlllib.Regex_Split.argtypes=[ c_char_p,c_char_p]
            dlllib.Regex_Split.restype=IntPtrArray
            intPtrArray = dlllib.Regex_Split(inputPtr,patternPtr)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            dlllib.Regex_Split.argtypes=[ c_wchar_p,c_wchar_p]
            dlllib.Regex_Split.restype=IntPtrArray
            intPtrArray = dlllib.Regex_Split( input,pattern)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        

    @staticmethod
    @dispatch

    def Split(input:str,pattern:str,options:RegexOptions)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            enumoptions:c_int = options.value

            dlllib.Regex_SplitIPO.argtypes=[ c_char_p,c_char_p,c_int]
            dlllib.Regex_SplitIPO.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIPO(inputPtr,patternPtr,enumoptions)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            enumoptions:c_int = options.value

            dlllib.Regex_SplitIPO.argtypes=[ c_wchar_p,c_wchar_p,c_int]
            dlllib.Regex_SplitIPO.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIPO( input,pattern,enumoptions)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        

    @staticmethod
    @dispatch

    def Split(input:str,pattern:str,options:RegexOptions,matchTimeout:TimeSpan)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_SplitIPOM.argtypes=[ c_char_p,c_char_p,c_int,c_void_p]
            dlllib.Regex_SplitIPOM.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIPOM(inputPtr,patternPtr,enumoptions,intPtrmatchTimeout)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            enumoptions:c_int = options.value
            intPtrmatchTimeout:c_void_p = matchTimeout.Ptr

            dlllib.Regex_SplitIPOM.argtypes=[ c_wchar_p,c_wchar_p,c_int,c_void_p]
            dlllib.Regex_SplitIPOM.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIPOM( input,pattern,enumoptions,intPtrmatchTimeout)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret


        

    @dispatch

    def Split(self ,input:str)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            dlllib.Regex_SplitI.argtypes=[c_void_p ,c_char_p]
            dlllib.Regex_SplitI.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitI(self.Ptr,inputPtr)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            dlllib.Regex_SplitI.argtypes=[c_void_p ,c_wchar_p]
            dlllib.Regex_SplitI.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitI(self.Ptr, input)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        

    @dispatch

    def Split(self ,input:str,count:int)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            dlllib.Regex_SplitIC.argtypes=[c_void_p ,c_char_p,c_int]
            dlllib.Regex_SplitIC.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIC(self.Ptr,inputPtr,count)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            dlllib.Regex_SplitIC.argtypes=[c_void_p ,c_wchar_p,c_int]
            dlllib.Regex_SplitIC.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitIC(self.Ptr, input,count)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        

    @dispatch

    def Split(self ,input:str,count:int,startat:int)->List[str]:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            dlllib.Regex_SplitICS.argtypes=[c_void_p ,c_char_p,c_int,c_int]
            dlllib.Regex_SplitICS.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitICS(self.Ptr,inputPtr,count,startat)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        else:
            dlllib.Regex_SplitICS.argtypes=[c_void_p ,c_wchar_p,c_int,c_int]
            dlllib.Regex_SplitICS.restype=IntPtrArray
            intPtrArray = dlllib.Regex_SplitICS(self.Ptr, input,count,startat)
            ret = GetVectorFromArray(intPtrArray, c_wchar_p)
            return ret
        

#    @staticmethod
#    @dispatch
#
#    def CompileToAssembly(regexinfos:'RegexCompilationInfo[]',assemblyname:'AssemblyName'):
#        """
#
#        """
#        #arrayregexinfos:ArrayTyperegexinfos = ""
#        countregexinfos = len(regexinfos)
#        ArrayTyperegexinfos = c_void_p * countregexinfos
#        arrayregexinfos = ArrayTyperegexinfos()
#        for i in range(0, countregexinfos):
#            arrayregexinfos[i] = regexinfos[i].Ptr
#
#        intPtrassemblyname:c_void_p = assemblyname.Ptr
#
#        dlllib.Regex_CompileToAssembly.argtypes=[ ArrayTyperegexinfos,c_void_p]
#        dlllib.Regex_CompileToAssembly( arrayregexinfos,intPtrassemblyname)


#    @staticmethod
#    @dispatch
#
#    def CompileToAssembly(regexinfos:'RegexCompilationInfo[]',assemblyname:'AssemblyName',attributes:'CustomAttributeBuilder[]'):
#        """
#
#        """
#        #arrayregexinfos:ArrayTyperegexinfos = ""
#        countregexinfos = len(regexinfos)
#        ArrayTyperegexinfos = c_void_p * countregexinfos
#        arrayregexinfos = ArrayTyperegexinfos()
#        for i in range(0, countregexinfos):
#            arrayregexinfos[i] = regexinfos[i].Ptr
#
#        intPtrassemblyname:c_void_p = assemblyname.Ptr
#        #arrayattributes:ArrayTypeattributes = ""
#        countattributes = len(attributes)
#        ArrayTypeattributes = c_void_p * countattributes
#        arrayattributes = ArrayTypeattributes()
#        for i in range(0, countattributes):
#            arrayattributes[i] = attributes[i].Ptr
#
#
#        dlllib.Regex_CompileToAssemblyRAA.argtypes=[ ArrayTyperegexinfos,c_void_p,ArrayTypeattributes]
#        dlllib.Regex_CompileToAssemblyRAA( arrayregexinfos,intPtrassemblyname,arrayattributes)


#    @staticmethod
#    @dispatch
#
#    def CompileToAssembly(regexinfos:'RegexCompilationInfo[]',assemblyname:'AssemblyName',attributes:'CustomAttributeBuilder[]',resourceFile:str):
#        """
#
#        """
#        #arrayregexinfos:ArrayTyperegexinfos = ""
#        countregexinfos = len(regexinfos)
#        ArrayTyperegexinfos = c_void_p * countregexinfos
#        arrayregexinfos = ArrayTyperegexinfos()
#        for i in range(0, countregexinfos):
#            arrayregexinfos[i] = regexinfos[i].Ptr
#
#        intPtrassemblyname:c_void_p = assemblyname.Ptr
#        #arrayattributes:ArrayTypeattributes = ""
#        countattributes = len(attributes)
#        ArrayTypeattributes = c_void_p * countattributes
#        arrayattributes = ArrayTypeattributes()
#        for i in range(0, countattributes):
#            arrayattributes[i] = attributes[i].Ptr
#
#
#        dlllib.Regex_CompileToAssemblyRAAR.argtypes=[ ArrayTyperegexinfos,c_void_p,ArrayTypeattributes,c_wchar_p]
#        dlllib.Regex_CompileToAssemblyRAAR( arrayregexinfos,intPtrassemblyname,arrayattributes,resourceFile)



    def GetGroupNumbers(self)->List[int]:
        """

        """
        dlllib.Regex_GetGroupNumbers.argtypes=[c_void_p]
        dlllib.Regex_GetGroupNumbers.restype=IntPtrArray
        intPtrArray = dlllib.Regex_GetGroupNumbers(self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_int)
        return ret

    @staticmethod
    @dispatch

    def IsMatch(input:str,pattern:str)->bool:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            dlllib.Regex_IsMatchIP.argtypes=[ c_char_p,c_char_p]
            dlllib.Regex_IsMatchIP.restype=c_bool
            ret = dlllib.Regex_IsMatchIP(inputPtr,patternPtr)
            return ret
        else:
            dlllib.Regex_IsMatchIP.argtypes=[ c_wchar_p,c_wchar_p]
            dlllib.Regex_IsMatchIP.restype=c_bool
            ret = dlllib.Regex_IsMatchIP( input,pattern)
            return ret
        

    @staticmethod
    @dispatch

    def IsMatch(input:str,pattern:str,options:RegexOptions)->bool:
        """

        """
        if GETSPIREPRODUCT(__file__) == "DOC":
            inputPtr = StrToPtr(input)
            patternPtr = StrToPtr(pattern)
            enumoptions:c_int = options.value

            dlllib.Regex_IsMatchIPO.argtypes=[ c_char_p,c_char_p,c_int]
            dlllib.Regex_IsMatchIPO.restype=c_bool
            ret = dlllib.Regex_IsMatchIPO(inputPtr,patternPtr,enumoptions)
            return ret
        else:
            enumoptions:c_int = options.value

            dlllib.Regex_IsMatchIPO.argtypes=[ c_wchar_p,c_wchar_p,c_int]
            dlllib.Regex_IsMatchIPO.restype=c_bool
            ret = dlllib.Regex_IsMatchIPO( input,pattern,enumoptions)
            return ret
        

#    @staticmethod
#    @dispatch
#
#    def Match(input:str,pattern:str)->Match:
#        """
#
#        """
#        
#        dlllib.Regex_MatchIP.argtypes=[ c_wchar_p,c_wchar_p]
#        dlllib.Regex_MatchIP.restype=c_void_p
#        intPtr = dlllib.Regex_MatchIP( input,pattern)
#        ret = None if intPtr==None else Match(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Matches(input:str,pattern:str)->MatchCollection:
#        """
#
#        """
#        
#        dlllib.Regex_MatchesIP.argtypes=[ c_wchar_p,c_wchar_p]
#        dlllib.Regex_MatchesIP.restype=c_void_p
#        intPtr = dlllib.Regex_MatchesIP( input,pattern)
#        ret = None if intPtr==None else MatchCollection(intPtr)
#        return ret
#



    def GetGroupNames(self)->List[str]:
        """

        """
        dlllib.Regex_GetGroupNames.argtypes=[c_void_p]
        dlllib.Regex_GetGroupNames.restype=IntPtrArray
        intPtrArray = dlllib.Regex_GetGroupNames(self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
        return ret

    @staticmethod

    def InfiniteMatchTimeout()->'TimeSpan':
        """

        """
        #dlllib.Regex_InfiniteMatchTimeout.argtypes=[]
        dlllib.Regex_InfiniteMatchTimeout.restype=c_void_p
        intPtr = dlllib.Regex_InfiniteMatchTimeout()
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


