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

class ImageFormat (SpireObject) :
    """

    """
#    @property
#
#    def Guid(self)->'Guid':
#        """
#
#        """
#        dlllib.ImageFormat_get_Guid.argtypes=[c_void_p]
#        dlllib.ImageFormat_get_Guid.restype=c_void_p
#        intPtr = dlllib.ImageFormat_get_Guid(self.Ptr)
#        ret = None if intPtr==None else Guid(intPtr)
#        return ret
#


    @staticmethod

    def get_MemoryBmp()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_MemoryBmp.argtypes=[]
        dlllib.ImageFormat_get_MemoryBmp.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_MemoryBmp()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Bmp()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Bmp.argtypes=[]
        dlllib.ImageFormat_get_Bmp.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Bmp()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Emf()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Emf.argtypes=[]
        dlllib.ImageFormat_get_Emf.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Emf()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Wmf()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Wmf.argtypes=[]
        dlllib.ImageFormat_get_Wmf.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Wmf()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Gif()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Gif.argtypes=[]
        dlllib.ImageFormat_get_Gif.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Gif()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Jpeg()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Jpeg.argtypes=[]
        dlllib.ImageFormat_get_Jpeg.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Jpeg()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Png()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Png.argtypes=[]
        dlllib.ImageFormat_get_Png.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Png()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Tiff()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Tiff.argtypes=[]
        dlllib.ImageFormat_get_Tiff.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Tiff()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Exif()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Exif.argtypes=[]
        dlllib.ImageFormat_get_Exif.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Exif()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret


    @staticmethod

    def get_Icon()->'ImageFormat':
        """

        """
        #dlllib.ImageFormat_get_Icon.argtypes=[]
        dlllib.ImageFormat_get_Icon.restype=c_void_p
        intPtr = dlllib.ImageFormat_get_Icon()
        ret = None if intPtr==None else ImageFormat(intPtr)
        return ret



    def Equals(self ,o:'SpireObject')->bool:
        """

        """
        intPtro:c_void_p = o.Ptr

        dlllib.ImageFormat_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.ImageFormat_Equals.restype=c_bool
        ret = dlllib.ImageFormat_Equals(self.Ptr, intPtro)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.ImageFormat_GetHashCode.argtypes=[c_void_p]
        dlllib.ImageFormat_GetHashCode.restype=c_int
        ret = dlllib.ImageFormat_GetHashCode(self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.ImageFormat_ToString.argtypes=[c_void_p]
        dlllib.ImageFormat_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.ImageFormat_ToString(self.Ptr))
        return ret


