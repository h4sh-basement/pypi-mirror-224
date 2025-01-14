from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FileFormat(Enum):
    """
    <summary>
        Type of file format.
    </summary>
    """
    Doc = 0
    Dot = 1
    Docx = 2
    Docx2010 = 3
    Docx2013 = 4
    Docx2016 = 5
    Docx2019 = 6
    Dotx = 7
    Dotx2010 = 8
    Dotx2013 = 9
    Dotx2016 = 10
    Dotx2019 = 11
    Docm = 12
    Docm2010 = 13
    Docm2013 = 14
    Docm2016 = 15
    Docm2019 = 16
    Dotm = 17
    Dotm2010 = 18
    Dotm2013 = 19
    Dotm2016 = 20
    Dotm2019 = 21
    OOXML = 22
    WordML = 23
    WordXml = 24
    Odt = 25
    Ott = 26
    PDF = 27
    Txt = 28
    Rtf = 29
    SVG = 30
    Xml = 31
    Html = 32
    XPS = 33
    EPub = 34
    DocPre97 = 35
    PostScript = 36
    PCL = 37
    OFD = 38
    OnlineDoc = 39
    Wps = 40
    Wpt = 41
    Auto = 42

