from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageNumberStyle(Enum):
    """
    <summary>
        Specifies the Number Style for a page.
    </summary>
    """
    Arabic = 0
    RomanUpper = 1
    RomanLower = 2
    LetterUpper = 3
    LetterLower = 4
    NumberInDash = 57
    ChineseCountingThousand = 39
    none = 255

