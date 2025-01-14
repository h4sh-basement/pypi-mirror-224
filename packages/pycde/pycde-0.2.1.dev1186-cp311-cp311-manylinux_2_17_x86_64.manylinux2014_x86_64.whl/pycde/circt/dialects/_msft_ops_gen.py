
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _msft_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "msft"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ChannelOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.constructs.channel"

  _ODS_REGIONS = (0, True)

  def __init__(self, input, clk, sym_name, defaultStages, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(clk))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["sym_name"] = (sym_name if (
    issubclass(type(sym_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(sym_name, context=_ods_context))
    attributes["defaultStages"] = (defaultStages if (
    issubclass(type(defaultStages), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('UI64Attr')) else
      _ods_ir.AttrBuilder.get('UI64Attr')(defaultStages, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def clk(self):
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
  def defaultStages(self):
    return self.operation.attributes["defaultStages"]

  @defaultStages.setter
  def defaultStages(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["defaultStages"] = value

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DeclPhysicalRegionOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.physical_region"

  _ODS_REGIONS = (0, True)

  def __init__(self, sym_name, bounds, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["sym_name"] = (sym_name if (
    issubclass(type(sym_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('SymbolNameAttr')) else
      _ods_ir.AttrBuilder.get('SymbolNameAttr')(sym_name, context=_ods_context))
    attributes["bounds"] = (bounds if (
    issubclass(type(bounds), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('PhysicalBoundsArray')) else
      _ods_ir.AttrBuilder.get('PhysicalBoundsArray')(bounds, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sym_name(self):
    return self.operation.attributes["sym_name"]

  @sym_name.setter
  def sym_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["sym_name"] = value

  @builtins.property
  def bounds(self):
    return self.operation.attributes["bounds"]

  @bounds.setter
  def bounds(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["bounds"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DesignPartitionOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.partition"

  _ODS_REGIONS = (0, True)

  def __init__(self, sym_name, verilogName, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["sym_name"] = (sym_name if (
    issubclass(type(sym_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('SymbolNameAttr')) else
      _ods_ir.AttrBuilder.get('SymbolNameAttr')(sym_name, context=_ods_context))
    attributes["verilogName"] = (verilogName if (
    issubclass(type(verilogName), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(verilogName, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sym_name(self):
    return self.operation.attributes["sym_name"]

  @sym_name.setter
  def sym_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["sym_name"] = value

  @builtins.property
  def verilogName(self):
    return self.operation.attributes["verilogName"]

  @verilogName.setter
  def verilogName(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["verilogName"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DynamicInstanceOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.instance.dynamic"

  _ODS_REGIONS = (1, True)

  def __init__(self, instanceRef, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["instanceRef"] = (instanceRef if (
    issubclass(type(instanceRef), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('InnerRefAttr')) else
      _ods_ir.AttrBuilder.get('InnerRefAttr')(instanceRef, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def instanceRef(self):
    return self.operation.attributes["instanceRef"]

  @instanceRef.setter
  def instanceRef(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["instanceRef"] = value

  @builtins.property
  def body(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DynamicInstanceVerbatimAttrOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.instance.verb_attr"

  _ODS_REGIONS = (0, True)

  def __init__(self, name, value, *, subPath=None, ref=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["name"] = (name if (
    issubclass(type(name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(name, context=_ods_context))
    attributes["value"] = (value if (
    issubclass(type(value), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(value, context=_ods_context))
    if subPath is not None: attributes["subPath"] = (subPath if (
        issubclass(type(subPath), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(subPath, context=_ods_context))
    if ref is not None: attributes["ref"] = (ref if (
        issubclass(type(ref), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
          _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(ref, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def name(self):
    return self.operation.attributes["name"]

  @name.setter
  def name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["name"] = value

  @builtins.property
  def value(self):
    return self.operation.attributes["value"]

  @value.setter
  def value(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["value"] = value

  @builtins.property
  def subPath(self):
    if "subPath" not in self.operation.attributes:
      return None
    return self.operation.attributes["subPath"]

  @subPath.setter
  def subPath(self, value):
    if value is not None:
      self.operation.attributes["subPath"] = value
    elif "subPath" in self.operation.attributes:
      del self.operation.attributes["subPath"]

  @subPath.deleter
  def subPath(self):
    del self.operation.attributes["subPath"]

  @builtins.property
  def ref(self):
    if "ref" not in self.operation.attributes:
      return None
    return self.operation.attributes["ref"]

  @ref.setter
  def ref(self, value):
    if value is not None:
      self.operation.attributes["ref"] = value
    elif "ref" in self.operation.attributes:
      del self.operation.attributes["ref"]

  @ref.deleter
  def ref(self):
    del self.operation.attributes["ref"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class EntityExternOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.entity.extern"

  _ODS_REGIONS = (0, True)

  def __init__(self, sym_name, metadata, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["sym_name"] = (sym_name if (
    issubclass(type(sym_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('SymbolNameAttr')) else
      _ods_ir.AttrBuilder.get('SymbolNameAttr')(sym_name, context=_ods_context))
    attributes["metadata"] = (metadata if (
    issubclass(type(metadata), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('AnyAttr')) else
      _ods_ir.AttrBuilder.get('AnyAttr')(metadata, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def sym_name(self):
    return self.operation.attributes["sym_name"]

  @sym_name.setter
  def sym_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["sym_name"] = value

  @builtins.property
  def metadata(self):
    return self.operation.attributes["metadata"]

  @metadata.setter
  def metadata(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["metadata"] = value

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class InstanceHierarchyOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.instance.hierarchy"

  _ODS_REGIONS = (1, True)

  def __init__(self, topModuleRef, *, instName=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["topModuleRef"] = (topModuleRef if (
    issubclass(type(topModuleRef), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
      _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(topModuleRef, context=_ods_context))
    if instName is not None: attributes["instName"] = (instName if (
        issubclass(type(instName), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(instName, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def topModuleRef(self):
    return self.operation.attributes["topModuleRef"]

  @topModuleRef.setter
  def topModuleRef(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["topModuleRef"] = value

  @builtins.property
  def instName(self):
    if "instName" not in self.operation.attributes:
      return None
    return self.operation.attributes["instName"]

  @instName.setter
  def instName(self, value):
    if value is not None:
      self.operation.attributes["instName"] = value
    elif "instName" in self.operation.attributes:
      del self.operation.attributes["instName"]

  @instName.deleter
  def instName(self):
    del self.operation.attributes["instName"]

  @builtins.property
  def body(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class InstanceOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.instance"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, inner_sym, moduleName, inputs, *, parameters=None, targetDesignPartition=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(inputs))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["inner_sym"] = (inner_sym if (
    issubclass(type(inner_sym), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('InnerSymAttr')) else
      _ods_ir.AttrBuilder.get('InnerSymAttr')(inner_sym, context=_ods_context))
    attributes["moduleName"] = (moduleName if (
    issubclass(type(moduleName), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
      _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(moduleName, context=_ods_context))
    if parameters is not None: attributes["parameters"] = (parameters if (
        issubclass(type(parameters), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('ParamDeclArrayAttr')) else
          _ods_ir.AttrBuilder.get('ParamDeclArrayAttr')(parameters, context=_ods_context))
    if targetDesignPartition is not None: attributes["targetDesignPartition"] = (targetDesignPartition if (
        issubclass(type(targetDesignPartition), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('SymbolRefAttr')) else
          _ods_ir.AttrBuilder.get('SymbolRefAttr')(targetDesignPartition, context=_ods_context))
    results.extend(result)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def inputs(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def inner_sym(self):
    return self.operation.attributes["inner_sym"]

  @inner_sym.setter
  def inner_sym(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["inner_sym"] = value

  @builtins.property
  def moduleName(self):
    return self.operation.attributes["moduleName"]

  @moduleName.setter
  def moduleName(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["moduleName"] = value

  @builtins.property
  def parameters(self):
    if "parameters" not in self.operation.attributes:
      return None
    return self.operation.attributes["parameters"]

  @parameters.setter
  def parameters(self, value):
    if value is not None:
      self.operation.attributes["parameters"] = value
    elif "parameters" in self.operation.attributes:
      del self.operation.attributes["parameters"]

  @parameters.deleter
  def parameters(self):
    del self.operation.attributes["parameters"]

  @builtins.property
  def targetDesignPartition(self):
    if "targetDesignPartition" not in self.operation.attributes:
      return None
    return self.operation.attributes["targetDesignPartition"]

  @targetDesignPartition.setter
  def targetDesignPartition(self, value):
    if value is not None:
      self.operation.attributes["targetDesignPartition"] = value
    elif "targetDesignPartition" in self.operation.attributes:
      del self.operation.attributes["targetDesignPartition"]

  @targetDesignPartition.deleter
  def targetDesignPartition(self):
    del self.operation.attributes["targetDesignPartition"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LinearOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.hlc.linear"

  _ODS_REGIONS = (1, True)

  def __init__(self, outs, clock, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(clock))
    _ods_context = _ods_get_default_loc_context(loc)
    results.extend(outs)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def clock(self):
    return self.operation.operands[0]

  @builtins.property
  def outs(self):
    _ods_variadic_group_length = len(self.operation.results) - 1 + 1
    return self.operation.results[0:0 + _ods_variadic_group_length]

  @builtins.property
  def datapath(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MSFTModuleExternOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.module.extern"

  _ODS_REGIONS = (1, True)

  @builtins.property
  def function_type(self):
    return self.operation.attributes["function_type"]

  @function_type.setter
  def function_type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["function_type"] = value

  @builtins.property
  def arg_attrs(self):
    if "arg_attrs" not in self.operation.attributes:
      return None
    return self.operation.attributes["arg_attrs"]

  @arg_attrs.setter
  def arg_attrs(self, value):
    if value is not None:
      self.operation.attributes["arg_attrs"] = value
    elif "arg_attrs" in self.operation.attributes:
      del self.operation.attributes["arg_attrs"]

  @arg_attrs.deleter
  def arg_attrs(self):
    del self.operation.attributes["arg_attrs"]

  @builtins.property
  def res_attrs(self):
    if "res_attrs" not in self.operation.attributes:
      return None
    return self.operation.attributes["res_attrs"]

  @res_attrs.setter
  def res_attrs(self, value):
    if value is not None:
      self.operation.attributes["res_attrs"] = value
    elif "res_attrs" in self.operation.attributes:
      del self.operation.attributes["res_attrs"]

  @res_attrs.deleter
  def res_attrs(self):
    del self.operation.attributes["res_attrs"]

  @builtins.property
  def argNames(self):
    return self.operation.attributes["argNames"]

  @argNames.setter
  def argNames(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["argNames"] = value

  @builtins.property
  def resultNames(self):
    return self.operation.attributes["resultNames"]

  @resultNames.setter
  def resultNames(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["resultNames"] = value

  @builtins.property
  def parameters(self):
    return self.operation.attributes["parameters"]

  @parameters.setter
  def parameters(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["parameters"] = value

  @builtins.property
  def verilogName(self):
    if "verilogName" not in self.operation.attributes:
      return None
    return self.operation.attributes["verilogName"]

  @verilogName.setter
  def verilogName(self, value):
    if value is not None:
      self.operation.attributes["verilogName"] = value
    elif "verilogName" in self.operation.attributes:
      del self.operation.attributes["verilogName"]

  @verilogName.deleter
  def verilogName(self):
    del self.operation.attributes["verilogName"]

  @builtins.property
  def body(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MSFTModuleOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.module"

  _ODS_REGIONS = (1, True)

  @builtins.property
  def function_type(self):
    return self.operation.attributes["function_type"]

  @function_type.setter
  def function_type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["function_type"] = value

  @builtins.property
  def arg_attrs(self):
    if "arg_attrs" not in self.operation.attributes:
      return None
    return self.operation.attributes["arg_attrs"]

  @arg_attrs.setter
  def arg_attrs(self, value):
    if value is not None:
      self.operation.attributes["arg_attrs"] = value
    elif "arg_attrs" in self.operation.attributes:
      del self.operation.attributes["arg_attrs"]

  @arg_attrs.deleter
  def arg_attrs(self):
    del self.operation.attributes["arg_attrs"]

  @builtins.property
  def res_attrs(self):
    if "res_attrs" not in self.operation.attributes:
      return None
    return self.operation.attributes["res_attrs"]

  @res_attrs.setter
  def res_attrs(self, value):
    if value is not None:
      self.operation.attributes["res_attrs"] = value
    elif "res_attrs" in self.operation.attributes:
      del self.operation.attributes["res_attrs"]

  @res_attrs.deleter
  def res_attrs(self):
    del self.operation.attributes["res_attrs"]

  @builtins.property
  def argNames(self):
    return self.operation.attributes["argNames"]

  @argNames.setter
  def argNames(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["argNames"] = value

  @builtins.property
  def resultNames(self):
    return self.operation.attributes["resultNames"]

  @resultNames.setter
  def resultNames(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["resultNames"] = value

  @builtins.property
  def argLocs(self):
    return self.operation.attributes["argLocs"]

  @argLocs.setter
  def argLocs(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["argLocs"] = value

  @builtins.property
  def resultLocs(self):
    return self.operation.attributes["resultLocs"]

  @resultLocs.setter
  def resultLocs(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["resultLocs"] = value

  @builtins.property
  def parameters(self):
    return self.operation.attributes["parameters"]

  @parameters.setter
  def parameters(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["parameters"] = value

  @builtins.property
  def fileName(self):
    if "fileName" not in self.operation.attributes:
      return None
    return self.operation.attributes["fileName"]

  @fileName.setter
  def fileName(self, value):
    if value is not None:
      self.operation.attributes["fileName"] = value
    elif "fileName" in self.operation.attributes:
      del self.operation.attributes["fileName"]

  @fileName.deleter
  def fileName(self):
    del self.operation.attributes["fileName"]

  @builtins.property
  def childAppIDBases(self):
    if "childAppIDBases" not in self.operation.attributes:
      return None
    return self.operation.attributes["childAppIDBases"]

  @childAppIDBases.setter
  def childAppIDBases(self, value):
    if value is not None:
      self.operation.attributes["childAppIDBases"] = value
    elif "childAppIDBases" in self.operation.attributes:
      del self.operation.attributes["childAppIDBases"]

  @childAppIDBases.deleter
  def childAppIDBases(self):
    del self.operation.attributes["childAppIDBases"]

  @builtins.property
  def body(self):
    return self.regions[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class OutputOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.output"

  _ODS_REGIONS = (0, True)

  def __init__(self, operands_, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(operands_))
    _ods_context = _ods_get_default_loc_context(loc)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operands_(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PDPhysLocationOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.pd.location"

  _ODS_REGIONS = (0, True)

  def __init__(self, loc_, *, subPath=None, ref=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["loc"] = (loc_ if (
    issubclass(type(loc_), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('PhysLocation')) else
      _ods_ir.AttrBuilder.get('PhysLocation')(loc_, context=_ods_context))
    if subPath is not None: attributes["subPath"] = (subPath if (
        issubclass(type(subPath), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(subPath, context=_ods_context))
    if ref is not None: attributes["ref"] = (ref if (
        issubclass(type(ref), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
          _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(ref, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def loc_(self):
    return self.operation.attributes["loc"]

  @loc_.setter
  def loc_(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["loc"] = value

  @builtins.property
  def subPath(self):
    if "subPath" not in self.operation.attributes:
      return None
    return self.operation.attributes["subPath"]

  @subPath.setter
  def subPath(self, value):
    if value is not None:
      self.operation.attributes["subPath"] = value
    elif "subPath" in self.operation.attributes:
      del self.operation.attributes["subPath"]

  @subPath.deleter
  def subPath(self):
    del self.operation.attributes["subPath"]

  @builtins.property
  def ref(self):
    if "ref" not in self.operation.attributes:
      return None
    return self.operation.attributes["ref"]

  @ref.setter
  def ref(self, value):
    if value is not None:
      self.operation.attributes["ref"] = value
    elif "ref" in self.operation.attributes:
      del self.operation.attributes["ref"]

  @ref.deleter
  def ref(self):
    del self.operation.attributes["ref"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PDPhysRegionOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.pd.physregion"

  _ODS_REGIONS = (0, True)

  def __init__(self, physRegionRef, *, subPath=None, ref=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["physRegionRef"] = (physRegionRef if (
    issubclass(type(physRegionRef), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
      _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(physRegionRef, context=_ods_context))
    if subPath is not None: attributes["subPath"] = (subPath if (
        issubclass(type(subPath), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('StrAttr')) else
          _ods_ir.AttrBuilder.get('StrAttr')(subPath, context=_ods_context))
    if ref is not None: attributes["ref"] = (ref if (
        issubclass(type(ref), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
          _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(ref, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def physRegionRef(self):
    return self.operation.attributes["physRegionRef"]

  @physRegionRef.setter
  def physRegionRef(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["physRegionRef"] = value

  @builtins.property
  def subPath(self):
    if "subPath" not in self.operation.attributes:
      return None
    return self.operation.attributes["subPath"]

  @subPath.setter
  def subPath(self, value):
    if value is not None:
      self.operation.attributes["subPath"] = value
    elif "subPath" in self.operation.attributes:
      del self.operation.attributes["subPath"]

  @subPath.deleter
  def subPath(self):
    del self.operation.attributes["subPath"]

  @builtins.property
  def ref(self):
    if "ref" not in self.operation.attributes:
      return None
    return self.operation.attributes["ref"]

  @ref.setter
  def ref(self, value):
    if value is not None:
      self.operation.attributes["ref"] = value
    elif "ref" in self.operation.attributes:
      del self.operation.attributes["ref"]

  @ref.deleter
  def ref(self):
    del self.operation.attributes["ref"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PDRegPhysLocationOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.pd.reg_location"

  _ODS_REGIONS = (0, True)

  def __init__(self, locs, *, ref=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["locs"] = (locs if (
    issubclass(type(locs), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('LocationVector')) else
      _ods_ir.AttrBuilder.get('LocationVector')(locs, context=_ods_context))
    if ref is not None: attributes["ref"] = (ref if (
        issubclass(type(ref), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('FlatSymbolRefAttr')) else
          _ods_ir.AttrBuilder.get('FlatSymbolRefAttr')(ref, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def locs(self):
    return self.operation.attributes["locs"]

  @locs.setter
  def locs(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["locs"] = value

  @builtins.property
  def ref(self):
    if "ref" not in self.operation.attributes:
      return None
    return self.operation.attributes["ref"]

  @ref.setter
  def ref(self, value):
    if value is not None:
      self.operation.attributes["ref"] = value
    elif "ref" in self.operation.attributes:
      del self.operation.attributes["ref"]

  @ref.deleter
  def ref(self):
    del self.operation.attributes["ref"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PEOutputOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.pe.output"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(output))
    _ods_context = _ods_get_default_loc_context(loc)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def output(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SystolicArrayOp(_ods_ir.OpView):
  OPERATION_NAME = "msft.systolic.array"

  _ODS_REGIONS = (1, True)

  def __init__(self, peOutputs, rowInputs, colInputs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(rowInputs))
    operands.append(_get_op_result_or_value(colInputs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(peOutputs)
    _ods_successors = None
    super().__init__(self.build_generic(attributes=attributes, results=results, operands=operands, successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def rowInputs(self):
    return self.operation.operands[0]

  @builtins.property
  def colInputs(self):
    return self.operation.operands[1]

  @builtins.property
  def peOutputs(self):
    return self.operation.results[0]

  @builtins.property
  def pe(self):
    return self.regions[0]
