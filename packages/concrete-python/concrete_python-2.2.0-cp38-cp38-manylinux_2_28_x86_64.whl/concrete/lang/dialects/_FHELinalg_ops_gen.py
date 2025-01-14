
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _FHELinalg_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "FHELinalg"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AddEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.add_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AddEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.add_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ApplyLookupTableEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.apply_lookup_table"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, t, lut, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(t))
    operands.append(_get_op_result_or_value(lut))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def t(self):
    return self.operation.operands[0]

  @builtins.property
  def lut(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ApplyMappedLookupTableEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.apply_mapped_lookup_table"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, t, luts, map, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(t))
    operands.append(_get_op_result_or_value(luts))
    operands.append(_get_op_result_or_value(map))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def t(self):
    return self.operation.operands[0]

  @builtins.property
  def luts(self):
    return self.operation.operands[1]

  @builtins.property
  def map(self):
    return self.operation.operands[2]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ApplyMultiLookupTableEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.apply_multi_lookup_table"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, t, luts, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(t))
    operands.append(_get_op_result_or_value(luts))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def t(self):
    return self.operation.operands[0]

  @builtins.property
  def luts(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ConcatOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.concat"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, ins, *, axis=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(ins))
    _ods_context = _ods_get_default_loc_context(loc)
    if axis is not None: attributes["axis"] = (axis if (
        issubclass(type(axis), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(axis, context=_ods_context))
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def ins(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def axis(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["axis"])

  @axis.setter
  def axis(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["axis"] = value

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Conv2dOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.conv2d"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, weight, *, bias=None, padding=None, strides=None, dilations=None, group=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    operands.append(_get_op_result_or_value(weight))
    if bias is not None: operands.append(_get_op_result_or_value(bias))
    _ods_context = _ods_get_default_loc_context(loc)
    if padding is not None: attributes["padding"] = (padding if (
        issubclass(type(padding), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
          _ods_ir.AttrBuilder.get('I64ElementsAttr')(padding, context=_ods_context))
    if strides is not None: attributes["strides"] = (strides if (
        issubclass(type(strides), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
          _ods_ir.AttrBuilder.get('I64ElementsAttr')(strides, context=_ods_context))
    if dilations is not None: attributes["dilations"] = (dilations if (
        issubclass(type(dilations), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
          _ods_ir.AttrBuilder.get('I64ElementsAttr')(dilations, context=_ods_context))
    if group is not None: attributes["group"] = (group if (
        issubclass(type(group), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(group, context=_ods_context))
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def weight(self):
    return self.operation.operands[1]

  @builtins.property
  def bias(self):
    return None if len(self.operation.operands) < 3 else self.operation.operands[2]

  @builtins.property
  def padding(self):
    if "padding" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["padding"])

  @padding.setter
  def padding(self, value):
    if value is not None:
      self.operation.attributes["padding"] = value
    elif "padding" in self.operation.attributes:
      del self.operation.attributes["padding"]

  @padding.deleter
  def padding(self):
    del self.operation.attributes["padding"]

  @builtins.property
  def strides(self):
    if "strides" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["strides"])

  @strides.setter
  def strides(self, value):
    if value is not None:
      self.operation.attributes["strides"] = value
    elif "strides" in self.operation.attributes:
      del self.operation.attributes["strides"]

  @strides.deleter
  def strides(self):
    del self.operation.attributes["strides"]

  @builtins.property
  def dilations(self):
    if "dilations" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["dilations"])

  @dilations.setter
  def dilations(self, value):
    if value is not None:
      self.operation.attributes["dilations"] = value
    elif "dilations" in self.operation.attributes:
      del self.operation.attributes["dilations"]

  @dilations.deleter
  def dilations(self):
    del self.operation.attributes["dilations"]

  @builtins.property
  def group(self):
    if "group" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["group"])

  @group.setter
  def group(self, value):
    if value is not None:
      self.operation.attributes["group"] = value
    elif "group" in self.operation.attributes:
      del self.operation.attributes["group"]

  @group.deleter
  def group(self):
    del self.operation.attributes["group"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Dot(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.dot_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DotEint(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.dot_eint_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FromElementOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.from_element"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, _gen_arg_0, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(_gen_arg_0))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MatMulEintEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.matmul_eint_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MatMulEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.matmul_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MatMulIntEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.matmul_int_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Maxpool2dOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.maxpool2d"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, kernel_shape, *, strides=None, dilations=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["kernel_shape"] = (kernel_shape if (
    issubclass(type(kernel_shape), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
      _ods_ir.AttrBuilder.get('I64ElementsAttr')(kernel_shape, context=_ods_context))
    if strides is not None: attributes["strides"] = (strides if (
        issubclass(type(strides), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
          _ods_ir.AttrBuilder.get('I64ElementsAttr')(strides, context=_ods_context))
    if dilations is not None: attributes["dilations"] = (dilations if (
        issubclass(type(dilations), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ElementsAttr')) else
          _ods_ir.AttrBuilder.get('I64ElementsAttr')(dilations, context=_ods_context))
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def kernel_shape(self):
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["kernel_shape"])

  @kernel_shape.setter
  def kernel_shape(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["kernel_shape"] = value

  @builtins.property
  def strides(self):
    if "strides" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["strides"])

  @strides.setter
  def strides(self, value):
    if value is not None:
      self.operation.attributes["strides"] = value
    elif "strides" in self.operation.attributes:
      del self.operation.attributes["strides"]

  @strides.deleter
  def strides(self):
    del self.operation.attributes["strides"]

  @builtins.property
  def dilations(self):
    if "dilations" not in self.operation.attributes:
      return None
    return _ods_ir.DenseIntElementsAttr(self.operation.attributes["dilations"])

  @dilations.setter
  def dilations(self, value):
    if value is not None:
      self.operation.attributes["dilations"] = value
    elif "dilations" in self.operation.attributes:
      del self.operation.attributes["dilations"]

  @dilations.deleter
  def dilations(self):
    del self.operation.attributes["dilations"]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MulEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.mul_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MulEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.mul_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class NegEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.neg_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, tensor, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(tensor))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def tensor(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RoundOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.round"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.sub_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.sub_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubIntEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.sub_int_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SumOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.sum"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, tensor, *, axes=None, keep_dims=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(tensor))
    _ods_context = _ods_get_default_loc_context(loc)
    if axes is not None: attributes["axes"] = (axes if (
        issubclass(type(axes), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ArrayAttr')) else
          _ods_ir.AttrBuilder.get('I64ArrayAttr')(axes, context=_ods_context))
    if keep_dims is not None: attributes["keep_dims"] = (keep_dims if (
        issubclass(type(keep_dims), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('BoolAttr')) else
          _ods_ir.AttrBuilder.get('BoolAttr')(keep_dims, context=_ods_context))
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def tensor(self):
    return self.operation.operands[0]

  @builtins.property
  def keep_dims(self):
    return _ods_ir.BoolAttr(self.operation.attributes["keep_dims"])

  @keep_dims.setter
  def keep_dims(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["keep_dims"] = value

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToSignedOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.to_signed"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToUnsignedOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.to_unsigned"

  _ODS_REGIONS = (0, True)

  def __init__(self, output, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(output)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

  @builtins.property
  def output(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class TransposeOp(_ods_ir.OpView):
  OPERATION_NAME = "FHELinalg.transpose"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, tensor, *, axes=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(tensor))
    _ods_context = _ods_get_default_loc_context(loc)
    if axes is not None: attributes["axes"] = (axes if (
        issubclass(type(axes), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64ArrayAttr')) else
          _ods_ir.AttrBuilder.get('I64ArrayAttr')(axes, context=_ods_context))
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def tensor(self):
    return self.operation.operands[0]
