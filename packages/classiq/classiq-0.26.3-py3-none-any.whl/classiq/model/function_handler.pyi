from typing import Optional, Dict

from classiq.interface.generator.function_param_list import *

from classiq.interface.generator.standard_gates.controlled_standard_gates import *

from classiq.interface.generator.standard_gates.standard_angled_gates import *

from classiq.interface.generator.standard_gates.standard_gates import *

import abc
from classiq.exceptions import ClassiqValueError as ClassiqValueError, ClassiqWiringError as ClassiqWiringError
from classiq.interface.generator import function_param_list as function_param_list, function_params as function_params
from classiq.interface.generator.control_state import ControlState as ControlState
from classiq.interface.generator.expressions.expression import Expression as Expression
from classiq.interface.generator.function_params import FunctionParams as FunctionParams, IOName as IOName, PortDirection as PortDirection
from classiq.interface.generator.functions.native_function_definition import SynthesisNativeFunctionDefinition as SynthesisNativeFunctionDefinition
from classiq.interface.generator.functions.port_declaration import PortDeclaration as PortDeclaration, PortDeclarationDirection as PortDeclarationDirection
from classiq.interface.generator.identity import Identity as Identity
from classiq.interface.generator.parameters import ParameterFloatType as ParameterFloatType, ParameterMap as ParameterMap
from classiq.interface.generator.quantum_function_call import SynthesisQuantumFunctionCall as SynthesisQuantumFunctionCall, WireName as WireName
from classiq.interface.generator.slice_parsing_utils import parse_io_slicing as parse_io_slicing
from classiq.interface.generator.user_defined_function_params import CustomFunction as CustomFunction
from classiq.model import logic_flow_change_handler as logic_flow_change_handler
from classiq.model.logic_flow import LogicFlowBuilder as LogicFlowBuilder
from classiq.quantum_functions.function_library import FunctionLibrary as FunctionLibrary, QuantumFunction as QuantumFunction, QuantumFunctionDeclaration as QuantumFunctionDeclaration
from classiq.quantum_register import QReg as QReg, QRegGenericAlias as QRegGenericAlias
from typing import Collection, Dict, Iterable, Mapping, Optional, Union

SupportedInputArgs = Union[Mapping[IOName, QReg], Collection[QReg], QReg]
WireNameDict = Dict[IOName, WireName]
ILLEGAL_INPUT_OR_SLICING_ERROR_MSG: str
ILLEGAL_OUTPUT_ERROR_MSG: str
ASSIGNED: str

class FunctionHandler(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @property
    def input_wires(self) -> WireNameDict: ...
    @property
    def output_wires(self) -> WireNameDict: ...
    def create_inputs(self, inputs: Mapping[IOName, QRegGenericAlias]) -> Dict[IOName, QReg]: ...
    def set_outputs(self, outputs: Mapping[IOName, QReg]) -> None: ...
    def apply(self, function_name: Union[str, QuantumFunctionDeclaration, QuantumFunction], in_wires: Optional[SupportedInputArgs] = ..., out_wires: Optional[SupportedInputArgs] = ..., is_inverse: bool = ..., assign_zero_ios: bool = ..., release_by_inverse: bool = ..., control_states: Optional[Union[ControlState, Iterable[ControlState]]] = ..., should_control: bool = ..., power: int = ..., call_name: Optional[str] = ..., parameters_dict: Optional[Dict[str, ParameterFloatType]] = ...) -> Dict[IOName, QReg]: ...
    def release_qregs(self, qregs: Union[QReg, Collection[QReg]]) -> None: ...
    def __getattr__(self, item): ...
    def __dir__(self): ...
    def include_library(self, library: FunctionLibrary) -> None: ...
    @abc.abstractmethod
    def create_library(self) -> None: ...
    def Exponentiation(self, params: Exponentiation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def WeightedAdder(self, params: WeightedAdder, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def BitwiseOr(self, params: BitwiseOr, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def AmplitudeLoading(self, params: AmplitudeLoading, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SXGate(self, params: SXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def WStatePreparation(self, params: WStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GHZStatePreparation(self, params: GHZStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SXdgGate(self, params: SXdgGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def TGate(self, params: TGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def StatePreparation(self, params: StatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CommutingPauliExponentiation(self, params: CommutingPauliExponentiation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def TdgGate(self, params: TdgGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Mcx(self, params: Mcx, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RYYGate(self, params: RYYGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RangeMixer(self, params: RangeMixer, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GreaterThan(self, params: GreaterThan, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CCXGate(self, params: CCXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CRYGate(self, params: CRYGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def UCC(self, params: UCC, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CRXGate(self, params: CRXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def PhaseGate(self, params: PhaseGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def QSVMFeatureMap(self, params: QSVMFeatureMap, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def FinanceModels(self, params: FinanceModels, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RZZGate(self, params: RZZGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def HypercubeEntangler(self, params: HypercubeEntangler, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def C4XGate(self, params: C4XGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Multiplier(self, params: Multiplier, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def PiecewiseLinearRotationAmplitudeLoading(self, params: PiecewiseLinearRotationAmplitudeLoading, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def HardwareEfficientAnsatz(self, params: HardwareEfficientAnsatz, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RGate(self, params: RGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SwapGate(self, params: SwapGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Subtractor(self, params: Subtractor, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LShift(self, params: LShift, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def AmplitudeEstimation(self, params: AmplitudeEstimation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GroverOperator(self, params: GroverOperator, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GreaterEqual(self, params: GreaterEqual, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Negation(self, params: Negation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RShift(self, params: RShift, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RXXGate(self, params: RXXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LogicalOr(self, params: LogicalOr, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CustomOracle(self, params: CustomOracle, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def XGate(self, params: XGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CRZGate(self, params: CRZGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def QFT(self, params: QFT, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LinearPauliRotations(self, params: LinearPauliRotations, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CPhaseGate(self, params: CPhaseGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RZGate(self, params: RZGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Arithmetic(self, params: Arithmetic, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def UnitaryGate(self, params: UnitaryGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Mcu(self, params: Mcu, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def FinancePayoff(self, params: FinancePayoff, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GroverDiffuser(self, params: GroverDiffuser, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def GridEntangler(self, params: GridEntangler, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def ExponentialStatePreparation(self, params: ExponentialStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def TwoDimensionalEntangler(self, params: TwoDimensionalEntangler, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SuzukiTrotter(self, params: SuzukiTrotter, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def BitwiseAnd(self, params: BitwiseAnd, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RYGate(self, params: RYGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def YGate(self, params: YGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CyclicShift(self, params: CyclicShift, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Equal(self, params: Equal, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def ArithmeticOracle(self, params: ArithmeticOracle, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def iSwapGate(self, params: iSwapGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def UniformDistributionStatePreparation(self, params: UniformDistributionStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def MCPhaseGate(self, params: MCPhaseGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LessThan(self, params: LessThan, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Modulo(self, params: Modulo, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Min(self, params: Min, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Max(self, params: Max, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def ComputationalBasisStatePreparation(self, params: ComputationalBasisStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CustomFunction(self, params: CustomFunction, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Adder(self, params: Adder, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LogicalAnd(self, params: LogicalAnd, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def PhaseEstimation(self, params: PhaseEstimation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RandomizedBenchmarking(self, params: RandomizedBenchmarking, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def C3XGate(self, params: C3XGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def StatePropagator(self, params: StatePropagator, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def InequalityMixer(self, params: InequalityMixer, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CZGate(self, params: CZGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CYGate(self, params: CYGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Sign(self, params: Sign, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def BitwiseXor(self, params: BitwiseXor, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def UGate(self, params: UGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def ZGate(self, params: ZGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def HGate(self, params: HGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def IGate(self, params: IGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SGate(self, params: SGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def RXGate(self, params: RXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def SdgGate(self, params: SdgGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LessEqual(self, params: LessEqual, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def PiecewiseLinearAmplitudeLoading(self, params: PiecewiseLinearAmplitudeLoading, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Identity(self, params: Identity, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def HartreeFock(self, params: HartreeFock, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CXGate(self, params: CXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def BellStatePreparation(self, params: BellStatePreparation, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def NotEqual(self, params: NotEqual, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def HVA(self, params: HVA, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def Finance(self, params: Finance, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CHGate(self, params: CHGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def LinearGCI(self, params: LinearGCI, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def CSXGate(self, params: CSXGate, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
    def BitwiseInvert(self, params: BitwiseInvert, in_wires: Optional[Dict[str, Wire]] = None) -> Dict[str, Wire]: ...
