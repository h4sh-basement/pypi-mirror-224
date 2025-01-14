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

class Image (SpireObject) :
    """

    """
    @staticmethod
    @dispatch

    def FromFile(filename:str)->'Image':
        """

        """
        
        dlllib.Image_FromFile.argtypes=[ c_void_p]
        dlllib.Image_FromFile.restype=c_void_p
        intPtr = dlllib.Image_FromFile( filename)
        ret = None if intPtr==None else Image(intPtr)
        return ret


    @staticmethod
    @dispatch

    def FromFile(filename:str,useEmbeddedColorManagement:bool)->'Image':
        """

        """
        
        dlllib.Image_FromFileFU.argtypes=[ c_void_p,c_bool]
        dlllib.Image_FromFileFU.restype=c_void_p
        intPtr = dlllib.Image_FromFileFU( filename,useEmbeddedColorManagement)
        ret = None if intPtr==None else Image(intPtr)
        return ret


    @staticmethod
    @dispatch

    def FromStream(stream:Stream)->'Image':
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        dlllib.Image_FromStream.argtypes=[ c_void_p]
        dlllib.Image_FromStream.restype=c_void_p
        intPtr = dlllib.Image_FromStream( intPtrstream)
        ret = None if intPtr==None else Image(intPtr)
        return ret


    @staticmethod
    @dispatch

    def FromStream(stream:Stream,useEmbeddedColorManagement:bool)->'Image':
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        dlllib.Image_FromStreamSU.argtypes=[ c_void_p,c_bool]
        dlllib.Image_FromStreamSU.restype=c_void_p
        intPtr = dlllib.Image_FromStreamSU( intPtrstream,useEmbeddedColorManagement)
        ret = None if intPtr==None else Image(intPtr)
        return ret



    def Clone(self)->'SpireObject':
        """

        """
        dlllib.Image_Clone.argtypes=[c_void_p]
        dlllib.Image_Clone.restype=c_void_p
        intPtr = dlllib.Image_Clone(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    def Dispose(self):
        """

        """
        dlllib.Image_Dispose.argtypes=[c_void_p]
        dlllib.Image_Dispose(self.Ptr)

#    @staticmethod
#    @dispatch
#
#    def FromHbitmap(hbitmap:'IntPtr')->Bitmap:
#        """
#
#        """
#        intPtrhbitmap:c_void_p = hbitmap.Ptr
#
#        dlllib.Image_FromHbitmap.argtypes=[ c_void_p]
#        dlllib.Image_FromHbitmap.restype=c_void_p
#        intPtr = dlllib.Image_FromHbitmap( intPtrhbitmap)
#        ret = None if intPtr==None else Bitmap(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def FromHbitmap(hbitmap:'IntPtr',hpalette:'IntPtr')->Bitmap:
#        """
#
#        """
#        intPtrhbitmap:c_void_p = hbitmap.Ptr
#        intPtrhpalette:c_void_p = hpalette.Ptr
#
#        dlllib.Image_FromHbitmapHH.argtypes=[ c_void_p,c_void_p]
#        dlllib.Image_FromHbitmapHH.restype=c_void_p
#        intPtr = dlllib.Image_FromHbitmapHH( intPtrhbitmap,intPtrhpalette)
#        ret = None if intPtr==None else Bitmap(intPtr)
#        return ret
#


    @staticmethod

    def GetPixelFormatSize(pixfmt:'PixelFormat')->int:
        """

        """
        enumpixfmt:c_int = pixfmt.value

        dlllib.Image_GetPixelFormatSize.argtypes=[ c_int]
        dlllib.Image_GetPixelFormatSize.restype=c_int
        ret = dlllib.Image_GetPixelFormatSize( enumpixfmt)
        return ret

    @staticmethod

    def IsAlphaPixelFormat(pixfmt:'PixelFormat')->bool:
        """

        """
        enumpixfmt:c_int = pixfmt.value

        dlllib.Image_IsAlphaPixelFormat.argtypes=[ c_int]
        dlllib.Image_IsAlphaPixelFormat.restype=c_bool
        ret = dlllib.Image_IsAlphaPixelFormat( enumpixfmt)
        return ret

    @staticmethod

    def IsExtendedPixelFormat(pixfmt:'PixelFormat')->bool:
        """

        """
        enumpixfmt:c_int = pixfmt.value

        dlllib.Image_IsExtendedPixelFormat.argtypes=[ c_int]
        dlllib.Image_IsExtendedPixelFormat.restype=c_bool
        ret = dlllib.Image_IsExtendedPixelFormat( enumpixfmt)
        return ret

    @staticmethod

    def IsCanonicalPixelFormat(pixfmt:'PixelFormat')->bool:
        """

        """
        enumpixfmt:c_int = pixfmt.value

        dlllib.Image_IsCanonicalPixelFormat.argtypes=[ c_int]
        dlllib.Image_IsCanonicalPixelFormat.restype=c_bool
        ret = dlllib.Image_IsCanonicalPixelFormat( enumpixfmt)
        return ret

    @property

    def Tag(self)->'SpireObject':
        """

        """
        dlllib.Image_get_Tag.argtypes=[c_void_p]
        dlllib.Image_get_Tag.restype=c_void_p
        intPtr = dlllib.Image_get_Tag(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    @Tag.setter
    def Tag(self, value:'SpireObject'):
        dlllib.Image_set_Tag.argtypes=[c_void_p, c_void_p]
        dlllib.Image_set_Tag(self.Ptr, value.Ptr)

#
#    def GetEncoderParameterList(self ,encoder:'Guid')->'EncoderParameters':
#        """
#
#        """
#        intPtrencoder:c_void_p = encoder.Ptr
#
#        dlllib.Image_GetEncoderParameterList.argtypes=[c_void_p ,c_void_p]
#        dlllib.Image_GetEncoderParameterList.restype=c_void_p
#        intPtr = dlllib.Image_GetEncoderParameterList(self.Ptr, intPtrencoder)
#        ret = None if intPtr==None else EncoderParameters(intPtr)
#        return ret
#


    @dispatch

    def Save(self ,filename:str):
        """

        """
        
        dlllib.Image_Save.argtypes=[c_void_p ,c_void_p]
        dlllib.Image_Save(self.Ptr, filename)

    @dispatch

    def Save(self ,filename:str,format:ImageFormat):
        """

        """
        intPtrformat:c_void_p = format.Ptr

        dlllib.Image_SaveFF.argtypes=[c_void_p ,c_void_p,c_void_p]
        dlllib.Image_SaveFF(self.Ptr, filename,intPtrformat)

#    @dispatch
#
#    def Save(self ,filename:str,encoder:'ImageCodecInfo',encoderParams:'EncoderParameters'):
#        """
#
#        """
#        intPtrencoder:c_void_p = encoder.Ptr
#        intPtrencoderParams:c_void_p = encoderParams.Ptr
#
#        dlllib.Image_SaveFEE.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p]
#        dlllib.Image_SaveFEE(self.Ptr, filename,intPtrencoder,intPtrencoderParams)


    @dispatch

    def Save(self ,stream:Stream,format:ImageFormat):
        """

        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrformat:c_void_p = format.Ptr

        dlllib.Image_SaveSF.argtypes=[c_void_p ,c_void_p,c_void_p]
        dlllib.Image_SaveSF(self.Ptr, intPtrstream,intPtrformat)

#    @dispatch
#
#    def Save(self ,stream:Stream,encoder:'ImageCodecInfo',encoderParams:'EncoderParameters'):
#        """
#
#        """
#        intPtrstream:c_void_p = stream.Ptr
#        intPtrencoder:c_void_p = encoder.Ptr
#        intPtrencoderParams:c_void_p = encoderParams.Ptr
#
#        dlllib.Image_SaveSEE.argtypes=[c_void_p ,c_void_p,c_void_p,c_void_p]
#        dlllib.Image_SaveSEE(self.Ptr, intPtrstream,intPtrencoder,intPtrencoderParams)


#    @dispatch
#
#    def SaveAdd(self ,encoderParams:'EncoderParameters'):
#        """
#
#        """
#        intPtrencoderParams:c_void_p = encoderParams.Ptr
#
#        dlllib.Image_SaveAdd.argtypes=[c_void_p ,c_void_p]
#        dlllib.Image_SaveAdd(self.Ptr, intPtrencoderParams)


#    @dispatch
#
#    def SaveAdd(self ,image:'Image',encoderParams:'EncoderParameters'):
#        """
#
#        """
#        intPtrimage:c_void_p = image.Ptr
#        intPtrencoderParams:c_void_p = encoderParams.Ptr
#
#        dlllib.Image_SaveAddIE.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Image_SaveAddIE(self.Ptr, intPtrimage,intPtrencoderParams)


    @property

    def PhysicalDimension(self)->'SizeF':
        """

        """
        dlllib.Image_get_PhysicalDimension.argtypes=[c_void_p]
        dlllib.Image_get_PhysicalDimension.restype=c_void_p
        intPtr = dlllib.Image_get_PhysicalDimension(self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @property

    def Size(self)->'Size':
        """

        """
        dlllib.Image_get_Size.argtypes=[c_void_p]
        dlllib.Image_get_Size.restype=c_void_p
        intPtr = dlllib.Image_get_Size(self.Ptr)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @property
    def Width(self)->int:
        """

        """
        dlllib.Image_get_Width.argtypes=[c_void_p]
        dlllib.Image_get_Width.restype=c_int
        ret = dlllib.Image_get_Width(self.Ptr)
        return ret

    @property
    def Height(self)->int:
        """

        """
        dlllib.Image_get_Height.argtypes=[c_void_p]
        dlllib.Image_get_Height.restype=c_int
        ret = dlllib.Image_get_Height(self.Ptr)
        return ret

    @property
    def HorizontalResolution(self)->float:
        """

        """
        dlllib.Image_get_HorizontalResolution.argtypes=[c_void_p]
        dlllib.Image_get_HorizontalResolution.restype=c_float
        ret = dlllib.Image_get_HorizontalResolution(self.Ptr)
        return ret

    @property
    def VerticalResolution(self)->float:
        """

        """
        dlllib.Image_get_VerticalResolution.argtypes=[c_void_p]
        dlllib.Image_get_VerticalResolution.restype=c_float
        ret = dlllib.Image_get_VerticalResolution(self.Ptr)
        return ret

    @property
    def Flags(self)->int:
        """

        """
        dlllib.Image_get_Flags.argtypes=[c_void_p]
        dlllib.Image_get_Flags.restype=c_int
        ret = dlllib.Image_get_Flags(self.Ptr)
        return ret

    @property

    def RawFormat(self)->'ImageFormat':
        """

        """
        dlllib.Image_get_RawFormat.argtypes=[c_void_p]
        dlllib.Image_get_RawFormat.restype=c_void_p
        intPtr = dlllib.Image_get_RawFormat(self.Ptr)
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @property

    def PixelFormat(self)->'PixelFormat':
        """

        """
        dlllib.Image_get_PixelFormat.argtypes=[c_void_p]
        dlllib.Image_get_PixelFormat.restype=c_int
        ret = dlllib.Image_get_PixelFormat(self.Ptr)
        objwraped = PixelFormat(ret)
        return objwraped

#
#    def GetBounds(self ,pageUnit:'GraphicsUnit&')->'RectangleF':
#        """
#
#        """
#        intPtrpageUnit:c_void_p = pageUnit.Ptr
#
#        dlllib.Image_GetBounds.argtypes=[c_void_p ,c_void_p]
#        dlllib.Image_GetBounds.restype=c_void_p
#        intPtr = dlllib.Image_GetBounds(self.Ptr, intPtrpageUnit)
#        ret = None if intPtr==None else RectangleF(intPtr)
#        return ret
#


#    @property
#
#    def Palette(self)->'ColorPalette':
#        """
#
#        """
#        dlllib.Image_get_Palette.argtypes=[c_void_p]
#        dlllib.Image_get_Palette.restype=c_void_p
#        intPtr = dlllib.Image_get_Palette(self.Ptr)
#        ret = None if intPtr==None else ColorPalette(intPtr)
#        return ret
#


#    @Palette.setter
#    def Palette(self, value:'ColorPalette'):
#        dlllib.Image_set_Palette.argtypes=[c_void_p, c_void_p]
#        dlllib.Image_set_Palette(self.Ptr, value.Ptr)


#
#    def GetThumbnailImage(self ,thumbWidth:int,thumbHeight:int,callback:'GetThumbnailImageAbort',callbackData:'IntPtr')->'Image':
#        """
#
#        """
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrcallbackData:c_void_p = callbackData.Ptr
#
#        dlllib.Image_GetThumbnailImage.argtypes=[c_void_p ,c_int,c_int,c_void_p,c_void_p]
#        dlllib.Image_GetThumbnailImage.restype=c_void_p
#        intPtr = dlllib.Image_GetThumbnailImage(self.Ptr, thumbWidth,thumbHeight,intPtrcallback,intPtrcallbackData)
#        ret = None if intPtr==None else Image(intPtr)
#        return ret
#


#    @property
#
#    def FrameDimensionsList(self)->List['Guid']:
#        """
#
#        """
#        dlllib.Image_get_FrameDimensionsList.argtypes=[c_void_p]
#        dlllib.Image_get_FrameDimensionsList.restype=IntPtrArray
#        intPtrArray = dlllib.Image_get_FrameDimensionsList(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Guid)
#        return ret


#
#    def GetFrameCount(self ,dimension:'FrameDimension')->int:
#        """
#
#        """
#        intPtrdimension:c_void_p = dimension.Ptr
#
#        dlllib.Image_GetFrameCount.argtypes=[c_void_p ,c_void_p]
#        dlllib.Image_GetFrameCount.restype=c_int
#        ret = dlllib.Image_GetFrameCount(self.Ptr, intPtrdimension)
#        return ret


#
#    def SelectActiveFrame(self ,dimension:'FrameDimension',frameIndex:int)->int:
#        """
#
#        """
#        intPtrdimension:c_void_p = dimension.Ptr
#
#        dlllib.Image_SelectActiveFrame.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.Image_SelectActiveFrame.restype=c_int
#        ret = dlllib.Image_SelectActiveFrame(self.Ptr, intPtrdimension,frameIndex)
#        return ret


#
#    def RotateFlip(self ,rotateFlipType:'RotateFlipType'):
#        """
#
#        """
#        enumrotateFlipType:c_int = rotateFlipType.value
#
#        dlllib.Image_RotateFlip.argtypes=[c_void_p ,c_int]
#        dlllib.Image_RotateFlip(self.Ptr, enumrotateFlipType)


    @property

    def PropertyIdList(self)->List[int]:
        """

        """
        dlllib.Image_get_PropertyIdList.argtypes=[c_void_p]
        dlllib.Image_get_PropertyIdList.restype=IntPtrArray
        intPtrArray = dlllib.Image_get_PropertyIdList(self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_int)
        return ret

#
#    def GetPropertyItem(self ,propid:int)->'PropertyItem':
#        """
#
#        """
#        
#        dlllib.Image_GetPropertyItem.argtypes=[c_void_p ,c_int]
#        dlllib.Image_GetPropertyItem.restype=c_void_p
#        intPtr = dlllib.Image_GetPropertyItem(self.Ptr, propid)
#        ret = None if intPtr==None else PropertyItem(intPtr)
#        return ret
#



    def RemovePropertyItem(self ,propid:int):
        """

        """
        
        dlllib.Image_RemovePropertyItem.argtypes=[c_void_p ,c_int]
        dlllib.Image_RemovePropertyItem(self.Ptr, propid)

#
#    def SetPropertyItem(self ,propitem:'PropertyItem'):
#        """
#
#        """
#        intPtrpropitem:c_void_p = propitem.Ptr
#
#        dlllib.Image_SetPropertyItem.argtypes=[c_void_p ,c_void_p]
#        dlllib.Image_SetPropertyItem(self.Ptr, intPtrpropitem)


#    @property
#
#    def PropertyItems(self)->List['PropertyItem']:
#        """
#
#        """
#        dlllib.Image_get_PropertyItems.argtypes=[c_void_p]
#        dlllib.Image_get_PropertyItems.restype=IntPtrArray
#        intPtrArray = dlllib.Image_get_PropertyItems(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, PropertyItem)
#        return ret


    @staticmethod
    @dispatch

    def FromStream(stream:Stream,useEmbeddedColorManagement:bool,validateImageData:bool)->'Image':
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        dlllib.Image_FromStreamSUV.argtypes=[ c_void_p,c_bool,c_bool]
        dlllib.Image_FromStreamSUV.restype=c_void_p
        intPtr = dlllib.Image_FromStreamSUV( intPtrstream,useEmbeddedColorManagement,validateImageData)
        ret = None if intPtr==None else Image(intPtr)
        return ret


