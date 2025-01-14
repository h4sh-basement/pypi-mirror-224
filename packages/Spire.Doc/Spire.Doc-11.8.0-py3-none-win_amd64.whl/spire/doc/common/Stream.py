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

class Stream (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.Stream_Create.restype = c_void_p
        intPtr = dlllib.Stream_Create()
        super(Stream, self).__init__(intPtr)
    @dispatch
    def __init__(self, filename:str):
        if GETSPIREPRODUCT(__file__) == "DOC":
            filenamePtr = StrToPtr(filename)
            dlllib.Stream_CreateByFile.argtypes=[c_char_p]
            dlllib.Stream_CreateByFile.restype = c_void_p
            intPtr = dlllib.Stream_CreateByFile(filenamePtr)
            super(Stream, self).__init__(intPtr)
        else:
            dlllib.Stream_CreateByFile.argtypes=[c_wchar_p]
            dlllib.Stream_CreateByFile.restype = c_void_p
            intPtr = dlllib.Stream_CreateByFile(filename)
            super(Stream, self).__init__(intPtr)
        
    
    @dispatch
    def __init__(self, data:bytes):
        list_address = cast((c_ubyte * len(data)).from_buffer_copy(data),c_void_p)
        length:c_int = len(data)

        dlllib.Stream_CreateByBytes.argtypes=[c_void_p,c_int]
        dlllib.Stream_CreateByBytes.restype = c_void_p
        intPtr = dlllib.Stream_CreateByBytes(list_address,length)
        super(Stream, self).__init__(intPtr)

    def __del__(self):
        dlllib.Stream_Dispose.argtypes = [c_void_p]
        dlllib.Stream_Dispose(self.Ptr)
        super(Stream, self).__del__()

    def Save(self, filename:str):
        if GETSPIREPRODUCT(__file__) == "DOC":
            filenamePtr = StrToPtr(filename)
            dlllib.Stream_SaveToFile.argtypes=[c_void_p,c_char_p]
            dlllib.Stream_SaveToFile(self.Ptr,filenamePtr)
        else:
            dlllib.Stream_SaveToFile.argtypes=[c_void_p,c_wchar_p]
            dlllib.Stream_SaveToFile(self.Ptr,filename)
        

    @property
    def CanTimeout(self)->bool:
        """

        """
        dlllib.Stream_get_CanTimeout.argtypes=[c_void_p]
        dlllib.Stream_get_CanTimeout.restype=c_bool
        ret = dlllib.Stream_get_CanTimeout(self.Ptr)
        return ret

    @property
    def ReadTimeout(self)->int:
        """

        """
        dlllib.Stream_get_ReadTimeout.argtypes=[c_void_p]
        dlllib.Stream_get_ReadTimeout.restype=c_int
        ret = dlllib.Stream_get_ReadTimeout(self.Ptr)
        return ret

    @ReadTimeout.setter
    def ReadTimeout(self, value:int):
        dlllib.Stream_set_ReadTimeout.argtypes=[c_void_p, c_int]
        dlllib.Stream_set_ReadTimeout(self.Ptr, value)

    @property
    def WriteTimeout(self)->int:
        """

        """
        dlllib.Stream_get_WriteTimeout.argtypes=[c_void_p]
        dlllib.Stream_get_WriteTimeout.restype=c_int
        ret = dlllib.Stream_get_WriteTimeout(self.Ptr)
        return ret

    @WriteTimeout.setter
    def WriteTimeout(self, value:int):
        dlllib.Stream_set_WriteTimeout.argtypes=[c_void_p, c_int]
        dlllib.Stream_set_WriteTimeout(self.Ptr, value)

#    @dispatch
#
#    def CopyToAsync(self ,destination:'Stream',bufferSize:int,cancellationToken:'CancellationToken')->Task:
#        """
#
#        """
#        intPtrdestination:c_void_p = destination.Ptr
#        intPtrcancellationToken:c_void_p = cancellationToken.Ptr
#
#        dlllib.Stream_CopyToAsync.argtypes=[c_void_p ,c_void_p,c_int,c_void_p]
#        dlllib.Stream_CopyToAsync.restype=c_void_p
#        intPtr = dlllib.Stream_CopyToAsync(self.Ptr, intPtrdestination,bufferSize,intPtrcancellationToken)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


    def Close(self):
        """

        """
        dlllib.Stream_Close.argtypes=[c_void_p]
        dlllib.Stream_Close(self.Ptr)

    def Dispose(self):
        """

        """
        dlllib.Stream_Dispose.argtypes=[c_void_p]
        dlllib.Stream_Dispose(self.Ptr)

#
#    def BeginRead(self ,buffer:'Byte[]',offset:int,count:int,callback:'AsyncCallback',state:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrstate:c_void_p = state.Ptr
#
#        dlllib.Stream_BeginRead.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int,c_void_p,c_void_p]
#        dlllib.Stream_BeginRead.restype=c_void_p
#        intPtr = dlllib.Stream_BeginRead(self.Ptr, arraybuffer,offset,count,intPtrcallback,intPtrstate)
#        ret = None if intPtr==None else IAsyncResult(intPtr)
#        return ret
#


#
#    def EndRead(self ,asyncResult:'IAsyncResult')->int:
#        """
#
#        """
#        intPtrasyncResult:c_void_p = asyncResult.Ptr
#
#        dlllib.Stream_EndRead.argtypes=[c_void_p ,c_void_p]
#        dlllib.Stream_EndRead.restype=c_int
#        ret = dlllib.Stream_EndRead(self.Ptr, intPtrasyncResult)
#        return ret


#    @dispatch
#
#    def ReadAsync(self ,buffer:'Byte[]',offset:int,count:int,cancellationToken:'CancellationToken')->Task1:
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#        intPtrcancellationToken:c_void_p = cancellationToken.Ptr
#
#        dlllib.Stream_ReadAsync.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int,c_void_p]
#        dlllib.Stream_ReadAsync.restype=c_void_p
#        intPtr = dlllib.Stream_ReadAsync(self.Ptr, arraybuffer,offset,count,intPtrcancellationToken)
#        ret = None if intPtr==None else Task1(intPtr)
#        return ret
#


#
#    def BeginWrite(self ,buffer:'Byte[]',offset:int,count:int,callback:'AsyncCallback',state:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrstate:c_void_p = state.Ptr
#
#        dlllib.Stream_BeginWrite.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int,c_void_p,c_void_p]
#        dlllib.Stream_BeginWrite.restype=c_void_p
#        intPtr = dlllib.Stream_BeginWrite(self.Ptr, arraybuffer,offset,count,intPtrcallback,intPtrstate)
#        ret = None if intPtr==None else IAsyncResult(intPtr)
#        return ret
#


#
#    def EndWrite(self ,asyncResult:'IAsyncResult'):
#        """
#
#        """
#        intPtrasyncResult:c_void_p = asyncResult.Ptr
#
#        dlllib.Stream_EndWrite.argtypes=[c_void_p ,c_void_p]
#        dlllib.Stream_EndWrite(self.Ptr, intPtrasyncResult)


#    @dispatch
#
#    def WriteAsync(self ,buffer:'Byte[]',offset:int,count:int,cancellationToken:'CancellationToken')->Task:
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#        intPtrcancellationToken:c_void_p = cancellationToken.Ptr
#
#        dlllib.Stream_WriteAsync.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int,c_void_p]
#        dlllib.Stream_WriteAsync.restype=c_void_p
#        intPtr = dlllib.Stream_WriteAsync(self.Ptr, arraybuffer,offset,count,intPtrcancellationToken)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


    def ReadByte(self)->int:
        """

        """
        dlllib.Stream_ReadByte.argtypes=[c_void_p]
        dlllib.Stream_ReadByte.restype=c_int
        ret = dlllib.Stream_ReadByte(self.Ptr)
        return ret


    def WriteByte(self ,value:int):
        """

        """
        
        dlllib.Stream_WriteByte.argtypes=[c_void_p ,c_void_p]
        dlllib.Stream_WriteByte(self.Ptr, value)

    @staticmethod

    def Synchronized(stream:'Stream')->'Stream':
        """

        """
        intPtrstream:c_void_p = stream.Ptr

        dlllib.Stream_Synchronized.argtypes=[ c_void_p]
        dlllib.Stream_Synchronized.restype=c_void_p
        intPtr = dlllib.Stream_Synchronized( intPtrstream)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @property
    def CanRead(self)->bool:
        """

        """
        dlllib.Stream_get_CanRead.argtypes=[c_void_p]
        dlllib.Stream_get_CanRead.restype=c_bool
        ret = dlllib.Stream_get_CanRead(self.Ptr)
        return ret

    @property
    def CanSeek(self)->bool:
        """

        """
        dlllib.Stream_get_CanSeek.argtypes=[c_void_p]
        dlllib.Stream_get_CanSeek.restype=c_bool
        ret = dlllib.Stream_get_CanSeek(self.Ptr)
        return ret

    @property
    def CanWrite(self)->bool:
        """

        """
        dlllib.Stream_get_CanWrite.argtypes=[c_void_p]
        dlllib.Stream_get_CanWrite.restype=c_bool
        ret = dlllib.Stream_get_CanWrite(self.Ptr)
        return ret

    @property
    def Length(self)->int:
        """

        """
        dlllib.Stream_get_Length.argtypes=[c_void_p]
        dlllib.Stream_get_Length.restype=c_long
        ret = dlllib.Stream_get_Length(self.Ptr)
        return ret

    @property
    def Position(self)->int:
        """

        """
        dlllib.Stream_get_Position.argtypes=[c_void_p]
        dlllib.Stream_get_Position.restype=c_long
        ret = dlllib.Stream_get_Position(self.Ptr)
        return ret

    @Position.setter
    def Position(self, value:int):
        dlllib.Stream_set_Position.argtypes=[c_void_p, c_long]
        dlllib.Stream_set_Position(self.Ptr, value)

#    @dispatch
#
#    def CopyToAsync(self ,destination:'Stream')->Task:
#        """
#
#        """
#        intPtrdestination:c_void_p = destination.Ptr
#
#        dlllib.Stream_CopyToAsyncD.argtypes=[c_void_p ,c_void_p]
#        dlllib.Stream_CopyToAsyncD.restype=c_void_p
#        intPtr = dlllib.Stream_CopyToAsyncD(self.Ptr, intPtrdestination)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


#    @dispatch
#
#    def CopyToAsync(self ,destination:'Stream',bufferSize:int)->Task:
#        """
#
#        """
#        intPtrdestination:c_void_p = destination.Ptr
#
#        dlllib.Stream_CopyToAsyncDB.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.Stream_CopyToAsyncDB.restype=c_void_p
#        intPtr = dlllib.Stream_CopyToAsyncDB(self.Ptr, intPtrdestination,bufferSize)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


    @dispatch

    def CopyTo(self ,destination:'Stream'):
        """

        """
        intPtrdestination:c_void_p = destination.Ptr

        dlllib.Stream_CopyTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Stream_CopyTo(self.Ptr, intPtrdestination)

    @dispatch

    def CopyTo(self ,destination:'Stream',bufferSize:int):
        """

        """
        intPtrdestination:c_void_p = destination.Ptr

        dlllib.Stream_CopyToDB.argtypes=[c_void_p ,c_void_p,c_int]
        dlllib.Stream_CopyToDB(self.Ptr, intPtrdestination,bufferSize)

    def Flush(self):
        """

        """
        dlllib.Stream_Flush.argtypes=[c_void_p]
        dlllib.Stream_Flush(self.Ptr)

#    @dispatch
#
#    def FlushAsync(self)->Task:
#        """
#
#        """
#        dlllib.Stream_FlushAsync.argtypes=[c_void_p]
#        dlllib.Stream_FlushAsync.restype=c_void_p
#        intPtr = dlllib.Stream_FlushAsync(self.Ptr)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


#    @dispatch
#
#    def FlushAsync(self ,cancellationToken:'CancellationToken')->Task:
#        """
#
#        """
#        intPtrcancellationToken:c_void_p = cancellationToken.Ptr
#
#        dlllib.Stream_FlushAsyncC.argtypes=[c_void_p ,c_void_p]
#        dlllib.Stream_FlushAsyncC.restype=c_void_p
#        intPtr = dlllib.Stream_FlushAsyncC(self.Ptr, intPtrcancellationToken)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


#    @dispatch
#
#    def ReadAsync(self ,buffer:'Byte[]',offset:int,count:int)->Task1:
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#
#        dlllib.Stream_ReadAsyncBOC.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int]
#        dlllib.Stream_ReadAsyncBOC.restype=c_void_p
#        intPtr = dlllib.Stream_ReadAsyncBOC(self.Ptr, arraybuffer,offset,count)
#        ret = None if intPtr==None else Task1(intPtr)
#        return ret
#


#    @dispatch
#
#    def WriteAsync(self ,buffer:'Byte[]',offset:int,count:int)->Task:
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#
#        dlllib.Stream_WriteAsyncBOC.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int]
#        dlllib.Stream_WriteAsyncBOC.restype=c_void_p
#        intPtr = dlllib.Stream_WriteAsyncBOC(self.Ptr, arraybuffer,offset,count)
#        ret = None if intPtr==None else Task(intPtr)
#        return ret
#


#
#    def Seek(self ,offset:int,origin:'SeekOrigin')->int:
#        """
#
#        """
#        enumorigin:c_int = origin.value
#
#        dlllib.Stream_Seek.argtypes=[c_void_p ,c_long,c_int]
#        dlllib.Stream_Seek.restype=c_long
#        ret = dlllib.Stream_Seek(self.Ptr, offset,enumorigin)
#        return ret



    def SetLength(self ,value:int):
        """

        """
        
        dlllib.Stream_SetLength.argtypes=[c_void_p ,c_long]
        dlllib.Stream_SetLength(self.Ptr, value)

#
#    def Read(self ,buffer:'Byte[]',offset:int,count:int)->int:
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#
#        dlllib.Stream_Read.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int]
#        dlllib.Stream_Read.restype=c_int
#        ret = dlllib.Stream_Read(self.Ptr, arraybuffer,offset,count)
#        return ret


#
#    def Write(self ,buffer:'Byte[]',offset:int,count:int):
#        """
#
#        """
#        #arraybuffer:ArrayTypebuffer = ""
#        countbuffer = len(buffer)
#        ArrayTypebuffer = c_void_p * countbuffer
#        arraybuffer = ArrayTypebuffer()
#        for i in range(0, countbuffer):
#            arraybuffer[i] = buffer[i].Ptr
#
#
#        dlllib.Stream_Write.argtypes=[c_void_p ,ArrayTypebuffer,c_int,c_int]
#        dlllib.Stream_Write(self.Ptr, arraybuffer,offset,count)


    @staticmethod

    def Null()->'Stream':
        """

        """
        #dlllib.Stream_Null.argtypes=[]
        dlllib.Stream_Null.restype=c_void_p
        intPtr = dlllib.Stream_Null()
        ret = None if intPtr==None else Stream(intPtr)
        return ret

    def ToArray(self):
        dlllib.Stream_ToArray.argtypes=[c_void_p]
        dlllib.Stream_ToArray.restype=IntPtrArray
        intPtrArr = dlllib.Stream_ToArray(self.Ptr)
        ret = GetBytesFromArray(intPtrArr)
        return ret
