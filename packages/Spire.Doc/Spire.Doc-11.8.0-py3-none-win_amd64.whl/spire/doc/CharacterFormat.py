from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CharacterFormat (  WordAttrCollection) :
    """

    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().CharacterFormat_CreateCharacterFormatD.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_CreateCharacterFormatD.restype = c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_CreateCharacterFormatD(intPdoc)
        super(CharacterFormat, self).__init__(intPtr)

    def ClearBackground(self):
        """
    <summary>
        Clear the text background.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_ClearBackground.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_ClearBackground(self.Ptr)

    def ClearFormatting(self):
        """

        """
        GetDllLibDoc().CharacterFormat_ClearFormatting.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_ClearFormatting(self.Ptr)

    @property
    def ItalicBidi(self)->bool:
        """
    <summary>
        Returns or sets italic property for right-to-left text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_ItalicBidi.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_ItalicBidi.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_ItalicBidi(self.Ptr)
        return ret

    @ItalicBidi.setter
    def ItalicBidi(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_ItalicBidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_ItalicBidi(self.Ptr, value)

    @property
    def FontSizeBidi(self)->float:
        """
    <summary>
        Returns or sets font size of the right-to-left text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontSizeBidi.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontSizeBidi.restype=c_float
        ret = GetDllLibDoc().CharacterFormat_get_FontSizeBidi(self.Ptr)
        return ret

    @FontSizeBidi.setter
    def FontSizeBidi(self, value:float):
        GetDllLibDoc().CharacterFormat_set_FontSizeBidi.argtypes=[c_void_p, c_float]
        GetDllLibDoc().CharacterFormat_set_FontSizeBidi(self.Ptr, value)

    @property

    def HighlightColor(self)->'Color':
        """
    <summary>
        Gets or sets highlight color of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_HighlightColor.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_HighlightColor.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_HighlightColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @HighlightColor.setter
    def HighlightColor(self, value:'Color'):
        GetDllLibDoc().CharacterFormat_set_HighlightColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CharacterFormat_set_HighlightColor(self.Ptr, value.Ptr)

    @property

    def Border(self)->'Border':
        """
    <summary>
        Gets border.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Border.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Border.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_Border(self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def FontNameAscii(self)->str:
        """
    <summary>
        Gets or setsthe font used for Latin text (characters with character codes from 0 through 127). 
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontNameAscii.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontNameAscii.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CharacterFormat_get_FontNameAscii(self.Ptr))
        return ret


    @FontNameAscii.setter
    def FontNameAscii(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CharacterFormat_set_FontNameAscii.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CharacterFormat_set_FontNameAscii(self.Ptr, valuePtr)

    @property

    def FontNameBidi(self)->str:
        """
    <summary>
        Gets or sets font name for right-to-left text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontNameBidi.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontNameBidi.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CharacterFormat_get_FontNameBidi(self.Ptr))
        return ret


    @FontNameBidi.setter
    def FontNameBidi(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CharacterFormat_set_FontNameBidi.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CharacterFormat_set_FontNameBidi(self.Ptr, valuePtr)

    @property

    def FontNameFarEast(self)->str:
        """
    <summary>
        Gets or sets East Asian font name.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontNameFarEast.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontNameFarEast.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CharacterFormat_get_FontNameFarEast(self.Ptr))
        return ret


    @FontNameFarEast.setter
    def FontNameFarEast(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CharacterFormat_set_FontNameFarEast.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CharacterFormat_set_FontNameFarEast(self.Ptr, valuePtr)

    @property

    def FontNameNonFarEast(self)->str:
        """
    <summary>
        Gets or sets font used for characters with character codes from 128 through 255.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontNameNonFarEast.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontNameNonFarEast.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CharacterFormat_get_FontNameNonFarEast(self.Ptr))
        return ret


    @FontNameNonFarEast.setter
    def FontNameNonFarEast(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CharacterFormat_set_FontNameNonFarEast.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CharacterFormat_set_FontNameNonFarEast(self.Ptr, valuePtr)

    @property

    def FontTypeHint(self)->'FontTypeHint':
        """
    <summary>
        Gets or sets the font type hint.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontTypeHint.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontTypeHint.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_FontTypeHint(self.Ptr)
        objwraped = FontTypeHint(ret)
        return objwraped

    @FontTypeHint.setter
    def FontTypeHint(self, value:'FontTypeHint'):
        GetDllLibDoc().CharacterFormat_set_FontTypeHint.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_FontTypeHint(self.Ptr, value.value)

    @property

    def LocaleIdASCII(self)->'Int16':
        """
    <summary>
        Gets or sets the ASCII locale id .
    </summary>
<value>The ASCII locale id .</value>
        """
        GetDllLibDoc().CharacterFormat_get_LocaleIdASCII.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_LocaleIdASCII.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_LocaleIdASCII(self.Ptr)
        ret = None if intPtr==None else Int16(intPtr)
        return ret


    @LocaleIdASCII.setter
    def LocaleIdASCII(self, value:int):
        GetDllLibDoc().CharacterFormat_set_LocaleIdASCII.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_LocaleIdASCII(self.Ptr, value)

    @property

    def LocaleIdFarEast(self)->'Int16':
        """
    <summary>
        Gets or sets the far east locale id .
    </summary>
<value>The far east locale id .</value>
        """
        GetDllLibDoc().CharacterFormat_get_LocaleIdFarEast.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_LocaleIdFarEast.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_LocaleIdFarEast(self.Ptr)
        ret = None if intPtr==None else Int16(intPtr)
        return ret


    @LocaleIdFarEast.setter
    def LocaleIdFarEast(self, value:'Int16'):
        GetDllLibDoc().CharacterFormat_set_LocaleIdFarEast.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CharacterFormat_set_LocaleIdFarEast(self.Ptr, value.Ptr)

    @property
    def IsOutLine(self)->bool:
        """
    <summary>
        Get/set outline character property.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_IsOutLine.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_IsOutLine.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_IsOutLine(self.Ptr)
        return ret

    @IsOutLine.setter
    def IsOutLine(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_IsOutLine.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_IsOutLine(self.Ptr, value)

    @property
    def AllowContextualAlternates(self)->bool:
        """
    <summary>
        Gets or sets a value indicating whether to allow contextual alternates.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_AllowContextualAlternates.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_AllowContextualAlternates.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_AllowContextualAlternates(self.Ptr)
        return ret

    @AllowContextualAlternates.setter
    def AllowContextualAlternates(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_AllowContextualAlternates.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_AllowContextualAlternates(self.Ptr, value)

    @property

    def LigaturesType(self)->'LigatureType':
        """
    <summary>
        Gets or sets the ligatures type.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_LigaturesType.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_LigaturesType.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_LigaturesType(self.Ptr)
        objwraped = LigatureType(ret)
        return objwraped

    @LigaturesType.setter
    def LigaturesType(self, value:'LigatureType'):
        GetDllLibDoc().CharacterFormat_set_LigaturesType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_LigaturesType(self.Ptr, value.value)

    @property

    def NumberFormType(self)->'NumberFormType':
        """
    <summary>
        Gets or sets the number form type.
    </summary>
<value>The number form.</value>
        """
        GetDllLibDoc().CharacterFormat_get_NumberFormType.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_NumberFormType.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_NumberFormType(self.Ptr)
        objwraped = NumberFormType(ret)
        return objwraped

    @NumberFormType.setter
    def NumberFormType(self, value:'NumberFormType'):
        GetDllLibDoc().CharacterFormat_set_NumberFormType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_NumberFormType(self.Ptr, value.value)

    @property

    def NumberSpaceType(self)->'NumberSpaceType':
        """
    <summary>
        Gets or sets the number space type.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_NumberSpaceType.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_NumberSpaceType.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_NumberSpaceType(self.Ptr)
        objwraped = NumberSpaceType(ret)
        return objwraped

    @NumberSpaceType.setter
    def NumberSpaceType(self, value:'NumberSpaceType'):
        GetDllLibDoc().CharacterFormat_set_NumberSpaceType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_NumberSpaceType(self.Ptr, value.value)

    @property

    def StylisticSetType(self)->'StylisticSetType':
        """
    <summary>
        Gets or sets the stylistic set type.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_StylisticSetType.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_StylisticSetType.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_StylisticSetType(self.Ptr)
        objwraped = StylisticSetType(ret)
        return objwraped

    @StylisticSetType.setter
    def StylisticSetType(self, value:'StylisticSetType'):
        GetDllLibDoc().CharacterFormat_set_StylisticSetType.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_StylisticSetType(self.Ptr, value.value)

    @property

    def FontName(self)->str:
        """
    <summary>
        Returns or sets font name
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontName.restype=c_void_p
        ret = PtrToStr(GetDllLibDoc().CharacterFormat_get_FontName(self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().CharacterFormat_set_FontName.argtypes=[c_void_p, c_char_p]
        GetDllLibDoc().CharacterFormat_set_FontName(self.Ptr, valuePtr)

    @property
    def FontSize(self)->float:
        """
    <summary>
        Returns or sets font size
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_FontSize.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_FontSize.restype=c_float
        ret = GetDllLibDoc().CharacterFormat_get_FontSize(self.Ptr)
        return ret

    @FontSize.setter
    def FontSize(self, value:float):
        GetDllLibDoc().CharacterFormat_set_FontSize.argtypes=[c_void_p, c_float]
        GetDllLibDoc().CharacterFormat_set_FontSize(self.Ptr, value)

    @property
    def Bold(self)->bool:
        """
    <summary>
        Returns or sets bold style
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Bold.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Bold.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Bold(self.Ptr)
        return ret

    @Bold.setter
    def Bold(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Bold.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Bold(self.Ptr, value)

    @property
    def Italic(self)->bool:
        """
    <summary>
        Returns or sets italic style
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Italic.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Italic.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Italic(self.Ptr)
        return ret

    @Italic.setter
    def Italic(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Italic.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Italic(self.Ptr, value)

    @property
    def IsStrikeout(self)->bool:
        """
    <summary>
        Returns or sets strikeout style.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_IsStrikeout.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_IsStrikeout.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_IsStrikeout(self.Ptr)
        return ret

    @IsStrikeout.setter
    def IsStrikeout(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_IsStrikeout.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_IsStrikeout(self.Ptr, value)

    @property
    def DoubleStrike(self)->bool:
        """
    <summary>
        Returns or sets double strikeout style.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_DoubleStrike.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_DoubleStrike.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_DoubleStrike(self.Ptr)
        return ret

    @DoubleStrike.setter
    def DoubleStrike(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_DoubleStrike.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_DoubleStrike(self.Ptr, value)

    @property

    def UnderlineStyle(self)->'UnderlineStyle':
        """
    <summary>
        Returns or sets underline style
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_UnderlineStyle.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_UnderlineStyle.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_UnderlineStyle(self.Ptr)
        objwraped = UnderlineStyle(ret)
        return objwraped

    @UnderlineStyle.setter
    def UnderlineStyle(self, value:'UnderlineStyle'):
        GetDllLibDoc().CharacterFormat_set_UnderlineStyle.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_UnderlineStyle(self.Ptr, value.value)

    @property

    def EmphasisMark(self)->'Emphasis':
        """
    <summary>
        Returns or sets text emphasis mark
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_EmphasisMark.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_EmphasisMark.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_EmphasisMark(self.Ptr)
        objwraped = Emphasis(ret)
        return objwraped

    @EmphasisMark.setter
    def EmphasisMark(self, value:'Emphasis'):
        GetDllLibDoc().CharacterFormat_set_EmphasisMark.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_EmphasisMark(self.Ptr, value.value)

    @property

    def TextColor(self)->'Color':
        """
    <summary>
        Returns or sets text color
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_TextColor.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_TextColor.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_TextColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @TextColor.setter
    def TextColor(self, value:'Color'):
        GetDllLibDoc().CharacterFormat_set_TextColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CharacterFormat_set_TextColor(self.Ptr, value.Ptr)

    @property

    def TextScale(self)->'Int16':
        """
    <summary>
        Gets or sets a value specifies that the percentage by which the contents of a run shall be expanded or compressed
            with respect to its normal(100%) character width,with a minimun width of 1% and maximum width of 600%.       
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_TextScale.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_TextScale.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_TextScale(self.Ptr)
        ret = None if intPtr==None else Int16(intPtr)
        return ret


    @TextScale.setter
    def TextScale(self, value:int):
        GetDllLibDoc().CharacterFormat_set_TextScale.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_TextScale(self.Ptr, value)

    @property

    def TextBackgroundColor(self)->'Color':
        """
    <summary>
        Gets or sets text background color
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_TextBackgroundColor.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_TextBackgroundColor.restype=c_void_p
        intPtr = GetDllLibDoc().CharacterFormat_get_TextBackgroundColor(self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @TextBackgroundColor.setter
    def TextBackgroundColor(self, value:'Color'):
        GetDllLibDoc().CharacterFormat_set_TextBackgroundColor.argtypes=[c_void_p, c_void_p]
        GetDllLibDoc().CharacterFormat_set_TextBackgroundColor(self.Ptr, value.Ptr)

    @property

    def SubSuperScript(self)->'SubSuperScript':
        """

        """
        GetDllLibDoc().CharacterFormat_get_SubSuperScript.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_SubSuperScript.restype=c_int
        ret = GetDllLibDoc().CharacterFormat_get_SubSuperScript(self.Ptr)
        objwraped = SubSuperScript(ret)
        return objwraped

    @SubSuperScript.setter
    def SubSuperScript(self, value:'SubSuperScript'):
        GetDllLibDoc().CharacterFormat_set_SubSuperScript.argtypes=[c_void_p, c_int]
        GetDllLibDoc().CharacterFormat_set_SubSuperScript(self.Ptr, value.value)

    @property
    def CharacterSpacing(self)->float:
        """

        """
        GetDllLibDoc().CharacterFormat_get_CharacterSpacing.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_CharacterSpacing.restype=c_float
        ret = GetDllLibDoc().CharacterFormat_get_CharacterSpacing(self.Ptr)
        formatted_value = "%.6f" % ret
        return formatted_value

    @CharacterSpacing.setter
    def CharacterSpacing(self, value:float):
        GetDllLibDoc().CharacterFormat_set_CharacterSpacing.argtypes=[c_void_p, c_float]
        GetDllLibDoc().CharacterFormat_set_CharacterSpacing(self.Ptr, value)

    @property
    def Position(self)->float:
        """

        """
        GetDllLibDoc().CharacterFormat_get_Position.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Position.restype=c_float
        ret = GetDllLibDoc().CharacterFormat_get_Position(self.Ptr)
        return ret

    @Position.setter
    def Position(self, value:float):
        GetDllLibDoc().CharacterFormat_set_Position.argtypes=[c_void_p, c_float]
        GetDllLibDoc().CharacterFormat_set_Position(self.Ptr, value)

    @property
    def IsShadow(self)->bool:
        """
    <summary>
        Gets or sets shadow property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_IsShadow.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_IsShadow.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_IsShadow(self.Ptr)
        return ret

    @IsShadow.setter
    def IsShadow(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_IsShadow.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_IsShadow(self.Ptr, value)

    @property
    def Emboss(self)->bool:
        """
    <summary>
        Gets or sets emboss property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Emboss.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Emboss.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Emboss(self.Ptr)
        return ret

    @Emboss.setter
    def Emboss(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Emboss.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Emboss(self.Ptr, value)

    @property
    def Engrave(self)->bool:
        """
    <summary>
        Gets or sets Engrave property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Engrave.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Engrave.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Engrave(self.Ptr)
        return ret

    @Engrave.setter
    def Engrave(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Engrave.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Engrave(self.Ptr, value)

    @property
    def Hidden(self)->bool:
        """
    <summary>
        Gets or sets Hidden property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Hidden.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Hidden.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Hidden(self.Ptr)
        return ret

    @Hidden.setter
    def Hidden(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Hidden.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Hidden(self.Ptr, value)

    @property
    def AllCaps(self)->bool:
        """
    <summary>
        Gets or sets AllCaps property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_AllCaps.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_AllCaps.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_AllCaps(self.Ptr)
        return ret

    @AllCaps.setter
    def AllCaps(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_AllCaps.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_AllCaps(self.Ptr, value)

    @property
    def IsSmallCaps(self)->bool:
        """
    <summary>
        Gets or sets IsSmallCaps property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_IsSmallCaps.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_IsSmallCaps.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_IsSmallCaps(self.Ptr)
        return ret

    @IsSmallCaps.setter
    def IsSmallCaps(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_IsSmallCaps.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_IsSmallCaps(self.Ptr, value)

    @property
    def Bidi(self)->bool:
        """
    <summary>
        Returns or sets right-to-left property of text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_Bidi.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_Bidi.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_Bidi(self.Ptr)
        return ret

    @Bidi.setter
    def Bidi(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_Bidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_Bidi(self.Ptr, value)

    @property
    def BoldBidi(self)->bool:
        """
    <summary>
        Returns or sets bold property for right-to-left text.
    </summary>
        """
        GetDllLibDoc().CharacterFormat_get_BoldBidi.argtypes=[c_void_p]
        GetDllLibDoc().CharacterFormat_get_BoldBidi.restype=c_bool
        ret = GetDllLibDoc().CharacterFormat_get_BoldBidi(self.Ptr)
        return ret

    @BoldBidi.setter
    def BoldBidi(self, value:bool):
        GetDllLibDoc().CharacterFormat_set_BoldBidi.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CharacterFormat_set_BoldBidi(self.Ptr, value)

