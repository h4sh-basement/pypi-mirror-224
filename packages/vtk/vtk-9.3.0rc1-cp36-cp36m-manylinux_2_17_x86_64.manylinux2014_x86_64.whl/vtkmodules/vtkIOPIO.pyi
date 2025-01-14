from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

MAX_CHILD:int
MAX_DIM:int
NZero0:int
NZero1:int
NZero2:int
Ncylin:int
Nd0:int
Nd1:int
Nd2:int
Nmesh0:int
Nmesh1:int
Nmesh2:int
Nnumdim:int
Nsphere:int
Ntime:int

class vtkPIOReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def DisableAllCellArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def GetActiveTimeDataArrayName(self) -> str: ...
    def GetCellArrayName(self, index:int) -> str: ...
    def GetCellArrayStatus(self, name:str) -> int: ...
    def GetCellDataArraySelection(self) -> vtkDataArraySelection: ...
    def GetCurrentTimeStep(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetFloat64(self) -> bool: ...
    def GetHyperTreeGrid(self) -> bool: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfTimeDataArrays(self) -> int: ...
    @overload
    def GetOutput(self) -> vtkMultiBlockDataSet: ...
    @overload
    def GetOutput(self, index:int) -> vtkMultiBlockDataSet: ...
    def GetTimeDataArray(self, idx:int) -> str: ...
    def GetTimeDataStringArray(self) -> vtkStringArray: ...
    def GetTracers(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkPIOReader: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkPIOReader: ...
    def SetActiveTimeDataArrayName(self, _arg:str) -> None: ...
    def SetCellArrayStatus(self, name:str, status:int) -> None: ...
    def SetCurrentTimeStep(self, _arg:int) -> None: ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetFloat64(self, _arg:bool) -> None: ...
    def SetHyperTreeGrid(self, _arg:bool) -> None: ...
    def SetTracers(self, _arg:bool) -> None: ...

