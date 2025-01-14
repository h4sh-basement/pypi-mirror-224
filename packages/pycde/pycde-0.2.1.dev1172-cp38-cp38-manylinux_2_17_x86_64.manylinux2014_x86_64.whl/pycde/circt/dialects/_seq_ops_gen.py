
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _seq_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "seq"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ClockGateOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.clock_gate"

  _ODS_REGIONS = (0, True)

  def __init__(self, input, enable, *, test_enable=None, inner_sym=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(enable))
    if test_enable is not None: operands.append(_get_op_result_or_value(test_enable))
    _ods_context = _ods_get_default_loc_context(loc)
    if inner_sym is not None: attributes["inner_sym"] = (inner_sym if (
        issubclass(type(inner_sym), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('InnerSymAttr')) else
          _ods_ir.AttrBuilder.get('InnerSymAttr')(inner_sym, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def enable(self):
    return self.operation.operands[1]

  @builtins.property
  def test_enable(self):
    return None if len(self.operation.operands) < 3 else self.operation.operands[2]

  @builtins.property
  def inner_sym(self):
    if "inner_sym" not in self.operation.attributes:
      return None
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is not None:
      self.operation.attributes["inner_sym"] = value
    elif "inner_sym" in self.operation.attributes:
      del self.operation.attributes["inner_sym"]

  @inner_sym.deleter
  def inner_sym(self):
    del self.operation.attributes["inner_sym"]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CompRegClockEnabledOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.compreg.ce"

  _ODS_REGIONS = (0, True)

  def __init__(self, input, clk, clockEnable, name, *, reset=None, resetValue=None, inner_sym=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(clockEnable))
    if reset is not None: operands.append(_get_op_result_or_value(reset))
    if resetValue is not None: operands.append(_get_op_result_or_value(resetValue))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["name"] = (name if (
    issubclass(type(name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(name, context=_ods_context))
    if inner_sym is not None: attributes["inner_sym"] = (inner_sym if (
        issubclass(type(inner_sym), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('InnerSymAttr')) else
          _ods_ir.AttrBuilder.get('InnerSymAttr')(inner_sym, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 0, 0)
    return self.operation.operands[start]

  @builtins.property
  def clk(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 1, 0)
    return self.operation.operands[start]

  @builtins.property
  def clockEnable(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 2, 0)
    return self.operation.operands[start]

  @builtins.property
  def reset(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 3, 0)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def resetValue(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 3, 1)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def name(self):
    return self.operation.attributes["name"]

  @name.setter
  def name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["name"] = value

  @builtins.property
  def inner_sym(self):
    if "inner_sym" not in self.operation.attributes:
      return None
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is not None:
      self.operation.attributes["inner_sym"] = value
    elif "inner_sym" in self.operation.attributes:
      del self.operation.attributes["inner_sym"]

  @inner_sym.deleter
  def inner_sym(self):
    del self.operation.attributes["inner_sym"]

  @builtins.property
  def data(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CompRegOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.compreg"

  _ODS_REGIONS = (0, True)

  def __init__(self, input, clk, name, *, reset=None, resetValue=None, inner_sym=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(clk))
    if reset is not None: operands.append(_get_op_result_or_value(reset))
    if resetValue is not None: operands.append(_get_op_result_or_value(resetValue))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["name"] = (name if (
    issubclass(type(name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(name, context=_ods_context))
    if inner_sym is not None: attributes["inner_sym"] = (inner_sym if (
        issubclass(type(inner_sym), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('InnerSymAttr')) else
          _ods_ir.AttrBuilder.get('InnerSymAttr')(inner_sym, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 0, 0)
    return self.operation.operands[start]

  @builtins.property
  def clk(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 1, 0)
    return self.operation.operands[start]

  @builtins.property
  def reset(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 2, 0)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def resetValue(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 2, 1)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def name(self):
    return self.operation.attributes["name"]

  @name.setter
  def name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["name"] = value

  @builtins.property
  def inner_sym(self):
    if "inner_sym" not in self.operation.attributes:
      return None
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is not None:
      self.operation.attributes["inner_sym"] = value
    elif "inner_sym" in self.operation.attributes:
      del self.operation.attributes["inner_sym"]

  @inner_sym.deleter
  def inner_sym(self):
    del self.operation.attributes["inner_sym"]

  @builtins.property
  def data(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FIFOOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.fifo"

  _ODS_RESULT_SEGMENTS = [1,1,1,0,0,]

  _ODS_REGIONS = (0, True)

  def __init__(self, output, full, empty, almostFull, almostEmpty, input, rdEn, wrEn, clk, rst, depth, *, almostFullThreshold=None, almostEmptyThreshold=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(rdEn))
    operands.append(_get_op_result_or_value(wrEn))
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(rst))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["depth"] = (depth if (
    issubclass(type(depth), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I64Attr')) else
      _ods_ir.AttrBuilder.get('I64Attr')(depth, context=_ods_context))
    if almostFullThreshold is not None: attributes["almostFullThreshold"] = (almostFullThreshold if (
        issubclass(type(almostFullThreshold), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(almostFullThreshold, context=_ods_context))
    if almostEmptyThreshold is not None: attributes["almostEmptyThreshold"] = (almostEmptyThreshold if (
        issubclass(type(almostEmptyThreshold), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(almostEmptyThreshold, context=_ods_context))
    results.append(output)
    results.append(full)
    results.append(empty)
    if almostFull is not None: results.append(almostFull)
    if almostEmpty is not None: results.append(almostEmpty)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def rdEn(self):
    return self.operation.operands[1]

  @builtins.property
  def wrEn(self):
    return self.operation.operands[2]

  @builtins.property
  def clk(self):
    return self.operation.operands[3]

  @builtins.property
  def rst(self):
    return self.operation.operands[4]

  @builtins.property
  def depth(self):
    return self.operation.attributes["depth"]

  @depth.setter
  def depth(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["depth"] = value

  @builtins.property
  def almostFullThreshold(self):
    if "almostFullThreshold" not in self.operation.attributes:
      return None
    return self.operation.attributes["almostFullThreshold"]

  @almostFullThreshold.setter
  def almostFullThreshold(self, value):
    if value is not None:
      self.operation.attributes["almostFullThreshold"] = value
    elif "almostFullThreshold" in self.operation.attributes:
      del self.operation.attributes["almostFullThreshold"]

  @almostFullThreshold.deleter
  def almostFullThreshold(self):
    del self.operation.attributes["almostFullThreshold"]

  @builtins.property
  def almostEmptyThreshold(self):
    if "almostEmptyThreshold" not in self.operation.attributes:
      return None
    return self.operation.attributes["almostEmptyThreshold"]

  @almostEmptyThreshold.setter
  def almostEmptyThreshold(self, value):
    if value is not None:
      self.operation.attributes["almostEmptyThreshold"] = value
    elif "almostEmptyThreshold" in self.operation.attributes:
      del self.operation.attributes["almostEmptyThreshold"]

  @almostEmptyThreshold.deleter
  def almostEmptyThreshold(self):
    del self.operation.attributes["almostEmptyThreshold"]

  @builtins.property
  def output(self):
    result_range = _ods_segmented_accessor(
         self.operation.results,
         self.operation.attributes["result_segment_sizes"], 0)
    return result_range[0]

  @builtins.property
  def full(self):
    result_range = _ods_segmented_accessor(
         self.operation.results,
         self.operation.attributes["result_segment_sizes"], 1)
    return result_range[0]

  @builtins.property
  def empty(self):
    result_range = _ods_segmented_accessor(
         self.operation.results,
         self.operation.attributes["result_segment_sizes"], 2)
    return result_range[0]

  @builtins.property
  def almostFull(self):
    result_range = _ods_segmented_accessor(
         self.operation.results,
         self.operation.attributes["result_segment_sizes"], 3)
    return result_range[0] if len(result_range) > 0 else None

  @builtins.property
  def almostEmpty(self):
    result_range = _ods_segmented_accessor(
         self.operation.results,
         self.operation.attributes["result_segment_sizes"], 4)
    return result_range[0] if len(result_range) > 0 else None

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FirMemOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.firmem"

  _ODS_REGIONS = (0, True)

  def __init__(self, memory, readLatency, writeLatency, ruw, wuw, *, name=None, inner_sym=None, init=None, prefix=None, output_file=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["readLatency"] = (readLatency if (
    issubclass(type(readLatency), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I32Attr')) else
      _ods_ir.AttrBuilder.get('I32Attr')(readLatency, context=_ods_context))
    attributes["writeLatency"] = (writeLatency if (
    issubclass(type(writeLatency), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I32Attr')) else
      _ods_ir.AttrBuilder.get('I32Attr')(writeLatency, context=_ods_context))
    attributes["ruw"] = (ruw if (
    issubclass(type(ruw), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('RUWAttr')) else
      _ods_ir.AttrBuilder.get('RUWAttr')(ruw, context=_ods_context))
    attributes["wuw"] = (wuw if (
    issubclass(type(wuw), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('WUWAttr')) else
      _ods_ir.AttrBuilder.get('WUWAttr')(wuw, context=_ods_context))
    if name is not None: attributes["name"] = (name if (
        issubclass(type(name), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(name, context=_ods_context))
    if inner_sym is not None: attributes["inner_sym"] = (inner_sym if (
        issubclass(type(inner_sym), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('InnerSymAttr')) else
          _ods_ir.AttrBuilder.get('InnerSymAttr')(inner_sym, context=_ods_context))
    if init is not None: attributes["init"] = (init if (
        issubclass(type(init), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('FirMemInitAttr')) else
          _ods_ir.AttrBuilder.get('FirMemInitAttr')(init, context=_ods_context))
    if prefix is not None: attributes["prefix"] = (prefix if (
        issubclass(type(prefix), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(prefix, context=_ods_context))
    if output_file is not None: attributes["output_file"] = (output_file if (
        issubclass(type(output_file), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('AnyAttr')) else
          _ods_ir.AttrBuilder.get('AnyAttr')(output_file, context=_ods_context))
    results.append(memory)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def readLatency(self):
    return self.operation.attributes["readLatency"]

  @readLatency.setter
  def readLatency(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["readLatency"] = value

  @builtins.property
  def writeLatency(self):
    return self.operation.attributes["writeLatency"]

  @writeLatency.setter
  def writeLatency(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["writeLatency"] = value

  @builtins.property
  def ruw(self):
    return self.operation.attributes["ruw"]

  @ruw.setter
  def ruw(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["ruw"] = value

  @builtins.property
  def wuw(self):
    return self.operation.attributes["wuw"]

  @wuw.setter
  def wuw(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["wuw"] = value

  @builtins.property
  def name(self):
    if "name" not in self.operation.attributes:
      return None
    return self.operation.attributes["name"]

  @name.setter
  def name(self, value):
    if value is not None:
      self.operation.attributes["name"] = value
    elif "name" in self.operation.attributes:
      del self.operation.attributes["name"]

  @name.deleter
  def name(self):
    del self.operation.attributes["name"]

  @builtins.property
  def inner_sym(self):
    if "inner_sym" not in self.operation.attributes:
      return None
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is not None:
      self.operation.attributes["inner_sym"] = value
    elif "inner_sym" in self.operation.attributes:
      del self.operation.attributes["inner_sym"]

  @inner_sym.deleter
  def inner_sym(self):
    del self.operation.attributes["inner_sym"]

  @builtins.property
  def init(self):
    if "init" not in self.operation.attributes:
      return None
    return self.operation.attributes["init"]

  @init.setter
  def init(self, value):
    if value is not None:
      self.operation.attributes["init"] = value
    elif "init" in self.operation.attributes:
      del self.operation.attributes["init"]

  @init.deleter
  def init(self):
    del self.operation.attributes["init"]

  @builtins.property
  def prefix(self):
    if "prefix" not in self.operation.attributes:
      return None
    return self.operation.attributes["prefix"]

  @prefix.setter
  def prefix(self, value):
    if value is not None:
      self.operation.attributes["prefix"] = value
    elif "prefix" in self.operation.attributes:
      del self.operation.attributes["prefix"]

  @prefix.deleter
  def prefix(self):
    del self.operation.attributes["prefix"]

  @builtins.property
  def output_file(self):
    if "output_file" not in self.operation.attributes:
      return None
    return self.operation.attributes["output_file"]

  @output_file.setter
  def output_file(self, value):
    if value is not None:
      self.operation.attributes["output_file"] = value
    elif "output_file" in self.operation.attributes:
      del self.operation.attributes["output_file"]

  @output_file.deleter
  def output_file(self):
    del self.operation.attributes["output_file"]

  @builtins.property
  def memory(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FirMemReadOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.firmem.read_port"

  _ODS_REGIONS = (0, True)

  def __init__(self, memory, address, clock, *, enable=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(memory))
    operands.append(_get_op_result_or_value(address))
    operands.append(_get_op_result_or_value(clock))
    if enable is not None: operands.append(_get_op_result_or_value(enable))
    _ods_context = _ods_get_default_loc_context(loc)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def memory(self):
    return self.operation.operands[0]

  @builtins.property
  def address(self):
    return self.operation.operands[1]

  @builtins.property
  def clock(self):
    return self.operation.operands[2]

  @builtins.property
  def enable(self):
    return None if len(self.operation.operands) < 4 else self.operation.operands[3]

  @builtins.property
  def data(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FirMemReadWriteOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.firmem.read_write_port"

  _ODS_OPERAND_SEGMENTS = [1,1,1,0,1,1,0,]

  _ODS_REGIONS = (0, True)

  def __init__(self, memory, address, clock, writeData, mode, *, enable=None, mask=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(memory))
    operands.append(_get_op_result_or_value(address))
    operands.append(_get_op_result_or_value(clock))
    operands.append(_get_op_result_or_value(enable) if enable is not None else None)
    operands.append(_get_op_result_or_value(writeData))
    operands.append(_get_op_result_or_value(mode))
    operands.append(_get_op_result_or_value(mask) if mask is not None else None)
    _ods_context = _ods_get_default_loc_context(loc)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def memory(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range[0]

  @builtins.property
  def address(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range[0]

  @builtins.property
  def clock(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 2)
    return operand_range[0]

  @builtins.property
  def enable(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 3)
    return operand_range[0] if len(operand_range) > 0 else None

  @builtins.property
  def writeData(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 4)
    return operand_range[0]

  @builtins.property
  def mode(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 5)
    return operand_range[0]

  @builtins.property
  def mask(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 6)
    return operand_range[0] if len(operand_range) > 0 else None

  @builtins.property
  def readData(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FirMemWriteOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.firmem.write_port"

  _ODS_OPERAND_SEGMENTS = [1,1,1,0,1,0,]

  _ODS_REGIONS = (0, True)

  def __init__(self, memory, address, clock, data, *, enable=None, mask=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(memory))
    operands.append(_get_op_result_or_value(address))
    operands.append(_get_op_result_or_value(clock))
    operands.append(_get_op_result_or_value(enable) if enable is not None else None)
    operands.append(_get_op_result_or_value(data))
    operands.append(_get_op_result_or_value(mask) if mask is not None else None)
    _ods_context = _ods_get_default_loc_context(loc)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def memory(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range[0]

  @builtins.property
  def address(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range[0]

  @builtins.property
  def clock(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 2)
    return operand_range[0]

  @builtins.property
  def enable(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 3)
    return operand_range[0] if len(operand_range) > 0 else None

  @builtins.property
  def data(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 4)
    return operand_range[0]

  @builtins.property
  def mask(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 5)
    return operand_range[0] if len(operand_range) > 0 else None

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FirRegOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.firreg"

  _ODS_REGIONS = (0, True)

  @builtins.property
  def next(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 0, 0)
    return self.operation.operands[start]

  @builtins.property
  def clk(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 1, 0)
    return self.operation.operands[start]

  @builtins.property
  def reset(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 2, 0)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def resetValue(self):
    start, pg = _ods_equally_sized_accessor(operation.operands, 2, 2, 1)
    return self.operation.operands[start:start + pg]

  @builtins.property
  def name(self):
    return self.operation.attributes["name"]

  @name.setter
  def name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["name"] = value

  @builtins.property
  def inner_sym(self):
    if "inner_sym" not in self.operation.attributes:
      return None
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is not None:
      self.operation.attributes["inner_sym"] = value
    elif "inner_sym" in self.operation.attributes:
      del self.operation.attributes["inner_sym"]

  @inner_sym.deleter
  def inner_sym(self):
    del self.operation.attributes["inner_sym"]

  @builtins.property
  def preset(self):
    if "preset" not in self.operation.attributes:
      return None
    return self.operation.attributes["preset"]

  @preset.setter
  def preset(self, value):
    if value is not None:
      self.operation.attributes["preset"] = value
    elif "preset" in self.operation.attributes:
      del self.operation.attributes["preset"]

  @preset.deleter
  def preset(self):
    del self.operation.attributes["preset"]

  @builtins.property
  def isAsync(self):
    return "isAsync" in self.operation.attributes

  @isAsync.setter
  def isAsync(self, value):
    if bool(value):
      self.operation.attributes["isAsync"] = _ods_ir.UnitAttr.get()
    elif "isAsync" in self.operation.attributes:
      del self.operation.attributes["isAsync"]

  @isAsync.deleter
  def isAsync(self):
    del self.operation.attributes["isAsync"]

  @builtins.property
  def data(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class HLMemOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.hlmem"

  _ODS_REGIONS = (0, True)

  def __init__(self, handle, clk, rst, sym_name, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clk))
    operands.append(_get_op_result_or_value(rst))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["sym_name"] = (sym_name if (
    issubclass(type(sym_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('SymbolNameAttr')) else
      _ods_ir.AttrBuilder.get('SymbolNameAttr')(sym_name, context=_ods_context))
    results.append(handle)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clk(self):
    return self.operation.operands[0]

  @builtins.property
  def rst(self):
    return self.operation.operands[1]

  @builtins.property
  def sym_name(self):
    return self.operation.attributes["sym_name"]

  @sym_name.setter
  def sym_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["sym_name"] = value

  @builtins.property
  def handle(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ReadPortOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.read"

  _ODS_OPERAND_SEGMENTS = [1,-1,0,]

  _ODS_REGIONS = (0, True)

  def __init__(self, readData, memory, addresses, latency, *, rdEn=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(memory))
    operands.append(_get_op_results_or_values(addresses))
    operands.append(_get_op_result_or_value(rdEn) if rdEn is not None else None)
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["latency"] = (latency if (
    issubclass(type(latency), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I64Attr')) else
      _ods_ir.AttrBuilder.get('I64Attr')(latency, context=_ods_context))
    results.append(readData)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def memory(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range[0]

  @builtins.property
  def addresses(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range

  @builtins.property
  def rdEn(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 2)
    return operand_range[0] if len(operand_range) > 0 else None

  @builtins.property
  def latency(self):
    return self.operation.attributes["latency"]

  @latency.setter
  def latency(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["latency"] = value

  @builtins.property
  def readData(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class WritePortOp(_ods_ir.OpView):
  OPERATION_NAME = "seq.write"

  _ODS_REGIONS = (0, True)

  def __init__(self, memory, addresses, inData, wrEn, latency, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(memory))
    operands.extend(_get_op_results_or_values(addresses))
    operands.append(_get_op_result_or_value(inData))
    operands.append(_get_op_result_or_value(wrEn))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["latency"] = (latency if (
    issubclass(type(latency), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I64Attr')) else
      _ods_ir.AttrBuilder.get('I64Attr')(latency, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def memory(self):
    return self.operation.operands[0]

  @builtins.property
  def addresses(self):
    _ods_variadic_group_length = len(self.operation.operands) - 4 + 1
    return self.operation.operands[1:1 + _ods_variadic_group_length]

  @builtins.property
  def inData(self):
    _ods_variadic_group_length = len(self.operation.operands) - 4 + 1
    return self.operation.operands[2 + _ods_variadic_group_length - 1]

  @builtins.property
  def wrEn(self):
    _ods_variadic_group_length = len(self.operation.operands) - 4 + 1
    return self.operation.operands[3 + _ods_variadic_group_length - 1]

  @builtins.property
  def latency(self):
    return self.operation.attributes["latency"]

  @latency.setter
  def latency(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["latency"] = value
