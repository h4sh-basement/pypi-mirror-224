from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkCellDistanceSelector(vtkmodules.vtkCommonExecutionModel.vtkSelectionAlgorithm):
    class InputPorts(int): ...
    INPUT_MESH:'InputPorts'
    INPUT_SELECTION:'InputPorts'
    def AddIntermediateOff(self) -> None: ...
    def AddIntermediateOn(self) -> None: ...
    def GetAddIntermediate(self) -> int: ...
    def GetDistance(self) -> int: ...
    def GetIncludeSeed(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IncludeSeedOff(self) -> None: ...
    def IncludeSeedOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCellDistanceSelector': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCellDistanceSelector': ...
    def SetAddIntermediate(self, _arg:int) -> None: ...
    def SetDistance(self, _arg:int) -> None: ...
    def SetIncludeSeed(self, _arg:int) -> None: ...
    def SetInputMesh(self, obj:'vtkDataObject') -> None: ...
    def SetInputMeshConnection(self, in_:'vtkAlgorithmOutput') -> None: ...
    def SetInputSelection(self, obj:'vtkSelection') -> None: ...
    def SetInputSelectionConnection(self, in_:'vtkAlgorithmOutput') -> None: ...

class vtkKdTreeSelector(vtkmodules.vtkCommonExecutionModel.vtkSelectionAlgorithm):
    def GetKdTree(self) -> 'vtkKdTree': ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetSelectionAttribute(self) -> int: ...
    def GetSelectionBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetSelectionFieldName(self) -> str: ...
    def GetSingleSelection(self) -> bool: ...
    def GetSingleSelectionThreshold(self) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkKdTreeSelector': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkKdTreeSelector': ...
    def SetKdTree(self, tree:'vtkKdTree') -> None: ...
    def SetSelectionAttribute(self, _arg:int) -> None: ...
    @overload
    def SetSelectionBounds(self, _arg1:float, _arg2:float, _arg3:float, _arg4:float, _arg5:float, _arg6:float) -> None: ...
    @overload
    def SetSelectionBounds(self, _arg:Sequence[float]) -> None: ...
    def SetSelectionFieldName(self, _arg:str) -> None: ...
    def SetSingleSelection(self, _arg:bool) -> None: ...
    def SetSingleSelectionThreshold(self, _arg:float) -> None: ...
    def SingleSelectionOff(self) -> None: ...
    def SingleSelectionOn(self) -> None: ...

class vtkLinearSelector(vtkmodules.vtkCommonExecutionModel.vtkSelectionAlgorithm):
    def GetEndPoint(self) -> Tuple[float, float, float]: ...
    def GetIncludeVertices(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPoints(self) -> 'vtkPoints': ...
    def GetStartPoint(self) -> Tuple[float, float, float]: ...
    def GetTolerance(self) -> float: ...
    def GetVertexEliminationTolerance(self) -> float: ...
    def GetVertexEliminationToleranceMaxValue(self) -> float: ...
    def GetVertexEliminationToleranceMinValue(self) -> float: ...
    def IncludeVerticesOff(self) -> None: ...
    def IncludeVerticesOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkLinearSelector': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkLinearSelector': ...
    @overload
    def SetEndPoint(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetEndPoint(self, _arg:Sequence[float]) -> None: ...
    def SetIncludeVertices(self, _arg:bool) -> None: ...
    def SetPoints(self, __a:'vtkPoints') -> None: ...
    @overload
    def SetStartPoint(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetStartPoint(self, _arg:Sequence[float]) -> None: ...
    def SetTolerance(self, _arg:float) -> None: ...
    def SetVertexEliminationTolerance(self, _arg:float) -> None: ...

