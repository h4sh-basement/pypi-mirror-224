from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkImageCanvasSource2D(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def DrawCircle(self, c0:int, c1:int, radius:float) -> None: ...
    @overload
    def DrawImage(self, x0:int, y0:int, i:vtkImageData) -> None: ...
    @overload
    def DrawImage(self, x0:int, y0:int, __c:vtkImageData, sx:int, sy:int, width:int, height:int) -> None: ...
    def DrawPoint(self, p0:int, p1:int) -> None: ...
    def DrawSegment(self, x0:int, y0:int, x1:int, y1:int) -> None: ...
    @overload
    def DrawSegment3D(self, p0:[float, ...], p1:[float, ...]) -> None: ...
    @overload
    def DrawSegment3D(self, x1:float, y1:float, z1:float, x2:float, y2:float, z2:float) -> None: ...
    def FillBox(self, min0:int, max0:int, min1:int, max1:int) -> None: ...
    def FillPixel(self, x:int, y:int) -> None: ...
    def FillTriangle(self, x0:int, y0:int, x1:int, y1:int, x2:int, y2:int) -> None: ...
    def FillTube(self, x0:int, y0:int, x1:int, y1:int, radius:float) -> None: ...
    def GetDefaultZ(self) -> int: ...
    def GetDrawColor(self) -> (float, float, float, float): ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfScalarComponents(self) -> int: ...
    def GetRatio(self) -> (float, float, float): ...
    def GetScalarType(self) -> int: ...
    def InitializeCanvasVolume(self, volume:vtkImageData) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageCanvasSource2D: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageCanvasSource2D: ...
    def SetDefaultZ(self, _arg:int) -> None: ...
    @overload
    def SetDrawColor(self, _arg1:float, _arg2:float, _arg3:float, _arg4:float) -> None: ...
    @overload
    def SetDrawColor(self, _arg:(float, float, float, float)) -> None: ...
    @overload
    def SetDrawColor(self, a:float) -> None: ...
    @overload
    def SetDrawColor(self, a:float, b:float) -> None: ...
    @overload
    def SetDrawColor(self, a:float, b:float, c:float) -> None: ...
    @overload
    def SetExtent(self, extent:[int, ...]) -> None: ...
    @overload
    def SetExtent(self, x1:int, x2:int, y1:int, y2:int, z1:int, z2:int) -> None: ...
    def SetNumberOfScalarComponents(self, i:int) -> None: ...
    @overload
    def SetRatio(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetRatio(self, _arg:(float, float, float)) -> None: ...
    def SetScalarType(self, __a:int) -> None: ...
    def SetScalarTypeToChar(self) -> None: ...
    def SetScalarTypeToDouble(self) -> None: ...
    def SetScalarTypeToFloat(self) -> None: ...
    def SetScalarTypeToInt(self) -> None: ...
    def SetScalarTypeToLong(self) -> None: ...
    def SetScalarTypeToShort(self) -> None: ...
    def SetScalarTypeToUnsignedChar(self) -> None: ...
    def SetScalarTypeToUnsignedInt(self) -> None: ...
    def SetScalarTypeToUnsignedLong(self) -> None: ...
    def SetScalarTypeToUnsignedShort(self) -> None: ...

class vtkImageEllipsoidSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetCenter(self) -> (float, float, float): ...
    def GetInValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOutValue(self) -> float: ...
    def GetOutputScalarType(self) -> int: ...
    def GetRadius(self) -> (float, float, float): ...
    @overload
    def GetWholeExtent(self, extent:[int, int, int, int, int, int]) -> None: ...
    @overload
    def GetWholeExtent(self) -> (int, int, int, int, int, int): ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageEllipsoidSource: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageEllipsoidSource: ...
    @overload
    def SetCenter(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetCenter(self, _arg:(float, float, float)) -> None: ...
    def SetInValue(self, _arg:float) -> None: ...
    def SetOutValue(self, _arg:float) -> None: ...
    def SetOutputScalarType(self, _arg:int) -> None: ...
    def SetOutputScalarTypeToChar(self) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetOutputScalarTypeToInt(self) -> None: ...
    def SetOutputScalarTypeToLong(self) -> None: ...
    def SetOutputScalarTypeToShort(self) -> None: ...
    def SetOutputScalarTypeToUnsignedChar(self) -> None: ...
    def SetOutputScalarTypeToUnsignedInt(self) -> None: ...
    def SetOutputScalarTypeToUnsignedLong(self) -> None: ...
    def SetOutputScalarTypeToUnsignedShort(self) -> None: ...
    @overload
    def SetRadius(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetRadius(self, _arg:(float, float, float)) -> None: ...
    @overload
    def SetWholeExtent(self, extent:[int, int, int, int, int, int]) -> None: ...
    @overload
    def SetWholeExtent(self, minX:int, maxX:int, minY:int, maxY:int, minZ:int, maxZ:int) -> None: ...

class vtkImageGaussianSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetCenter(self) -> (float, float, float): ...
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetStandardDeviation(self) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageGaussianSource: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageGaussianSource: ...
    @overload
    def SetCenter(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetCenter(self, _arg:(float, float, float)) -> None: ...
    def SetMaximum(self, _arg:float) -> None: ...
    def SetStandardDeviation(self, _arg:float) -> None: ...
    def SetWholeExtent(self, xMinx:int, xMax:int, yMin:int, yMax:int, zMin:int, zMax:int) -> None: ...

class vtkImageGridSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetDataExtent(self) -> (int, int, int, int, int, int): ...
    def GetDataOrigin(self) -> (float, float, float): ...
    def GetDataScalarType(self) -> int: ...
    def GetDataScalarTypeAsString(self) -> str: ...
    def GetDataSpacing(self) -> (float, float, float): ...
    def GetFillValue(self) -> float: ...
    def GetGridOrigin(self) -> (int, int, int): ...
    def GetGridSpacing(self) -> (int, int, int): ...
    def GetLineValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageGridSource: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageGridSource: ...
    @overload
    def SetDataExtent(self, _arg1:int, _arg2:int, _arg3:int, _arg4:int, _arg5:int, _arg6:int) -> None: ...
    @overload
    def SetDataExtent(self, _arg:(int, int, int, int, int, int)) -> None: ...
    @overload
    def SetDataOrigin(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetDataOrigin(self, _arg:(float, float, float)) -> None: ...
    def SetDataScalarType(self, _arg:int) -> None: ...
    def SetDataScalarTypeToDouble(self) -> None: ...
    def SetDataScalarTypeToInt(self) -> None: ...
    def SetDataScalarTypeToShort(self) -> None: ...
    def SetDataScalarTypeToUnsignedChar(self) -> None: ...
    def SetDataScalarTypeToUnsignedShort(self) -> None: ...
    @overload
    def SetDataSpacing(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetDataSpacing(self, _arg:(float, float, float)) -> None: ...
    def SetFillValue(self, _arg:float) -> None: ...
    @overload
    def SetGridOrigin(self, _arg1:int, _arg2:int, _arg3:int) -> None: ...
    @overload
    def SetGridOrigin(self, _arg:(int, int, int)) -> None: ...
    @overload
    def SetGridSpacing(self, _arg1:int, _arg2:int, _arg3:int) -> None: ...
    @overload
    def SetGridSpacing(self, _arg:(int, int, int)) -> None: ...
    def SetLineValue(self, _arg:float) -> None: ...

class vtkImageMandelbrotSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def ConstantSizeOff(self) -> None: ...
    def ConstantSizeOn(self) -> None: ...
    def CopyOriginAndSample(self, source:vtkImageMandelbrotSource) -> None: ...
    def GetConstantSize(self) -> int: ...
    def GetMaximumNumberOfIterations(self) -> int: ...
    def GetMaximumNumberOfIterationsMaxValue(self) -> int: ...
    def GetMaximumNumberOfIterationsMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOriginCX(self) -> (float, float, float, float): ...
    def GetProjectionAxes(self) -> (int, int, int): ...
    def GetSampleCX(self) -> (float, float, float, float): ...
    @overload
    def GetSizeCX(self) -> (float, float, float, float): ...
    @overload
    def GetSizeCX(self, s:[float, float, float, float]) -> None: ...
    def GetSubsampleRate(self) -> int: ...
    def GetSubsampleRateMaxValue(self) -> int: ...
    def GetSubsampleRateMinValue(self) -> int: ...
    def GetWholeExtent(self) -> (int, int, int, int, int, int): ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageMandelbrotSource: ...
    def Pan(self, x:float, y:float, z:float) -> None: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageMandelbrotSource: ...
    def SetConstantSize(self, _arg:int) -> None: ...
    def SetMaximumNumberOfIterations(self, _arg:int) -> None: ...
    @overload
    def SetOriginCX(self, _arg1:float, _arg2:float, _arg3:float, _arg4:float) -> None: ...
    @overload
    def SetOriginCX(self, _arg:(float, float, float, float)) -> None: ...
    @overload
    def SetProjectionAxes(self, x:int, y:int, z:int) -> None: ...
    @overload
    def SetProjectionAxes(self, a:[int, int, int]) -> None: ...
    @overload
    def SetSampleCX(self, _arg1:float, _arg2:float, _arg3:float, _arg4:float) -> None: ...
    @overload
    def SetSampleCX(self, _arg:(float, float, float, float)) -> None: ...
    def SetSizeCX(self, cReal:float, cImag:float, xReal:float, xImag:float) -> None: ...
    def SetSubsampleRate(self, _arg:int) -> None: ...
    @overload
    def SetWholeExtent(self, extent:[int, int, int, int, int, int]) -> None: ...
    @overload
    def SetWholeExtent(self, minX:int, maxX:int, minY:int, maxY:int, minZ:int, maxZ:int) -> None: ...
    def Zoom(self, factor:float) -> None: ...

class vtkImageNoiseSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetMinimum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageNoiseSource: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageNoiseSource: ...
    def SetMaximum(self, _arg:float) -> None: ...
    def SetMinimum(self, _arg:float) -> None: ...
    @overload
    def SetWholeExtent(self, xMinx:int, xMax:int, yMin:int, yMax:int, zMin:int, zMax:int) -> None: ...
    @overload
    def SetWholeExtent(self, ext:(int, int, int, int, int, int)) -> None: ...

class vtkImageSinusoidSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetAmplitude(self) -> float: ...
    def GetDirection(self) -> (float, float, float): ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPeriod(self) -> float: ...
    def GetPhase(self) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> vtkImageSinusoidSource: ...
    @staticmethod
    def SafeDownCast(o:vtkObjectBase) -> vtkImageSinusoidSource: ...
    def SetAmplitude(self, _arg:float) -> None: ...
    @overload
    def SetDirection(self, __a:float, __b:float, __c:float) -> None: ...
    @overload
    def SetDirection(self, dir:[float, float, float]) -> None: ...
    def SetPeriod(self, _arg:float) -> None: ...
    def SetPhase(self, _arg:float) -> None: ...
    def SetWholeExtent(self, xMinx:int, xMax:int, yMin:int, yMax:int, zMin:int, zMax:int) -> None: ...

