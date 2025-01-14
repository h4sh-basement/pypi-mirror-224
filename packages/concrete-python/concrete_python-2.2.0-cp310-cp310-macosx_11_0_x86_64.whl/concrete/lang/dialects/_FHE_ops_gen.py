
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _FHE_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "FHE"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AddEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.add_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AddEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.add_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ApplyLookupTableEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.apply_lookup_table"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, lut, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(lut))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def lut(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BoolAndOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.and"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, left, right, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(left))
    operands.append(_get_op_result_or_value(right))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def left(self):
    return self.operation.operands[0]

  @builtins.property
  def right(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BoolNandOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.nand"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, left, right, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(left))
    operands.append(_get_op_result_or_value(right))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def left(self):
    return self.operation.operands[0]

  @builtins.property
  def right(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BoolNotOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.not"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, value, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(value))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def value(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BoolOrOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.or"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, left, right, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(left))
    operands.append(_get_op_result_or_value(right))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def left(self):
    return self.operation.operands[0]

  @builtins.property
  def right(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class BoolXorOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.xor"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, left, right, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(left))
    operands.append(_get_op_result_or_value(right))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def left(self):
    return self.operation.operands[0]

  @builtins.property
  def right(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FromBoolOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.from_bool"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class GenGateOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.gen_gate"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, left, right, truth_table, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(left))
    operands.append(_get_op_result_or_value(right))
    operands.append(_get_op_result_or_value(truth_table))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def left(self):
    return self.operation.operands[0]

  @builtins.property
  def right(self):
    return self.operation.operands[1]

  @builtins.property
  def truth_table(self):
    return self.operation.operands[2]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MaxEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.max_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, x, y, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(x))
    operands.append(_get_op_result_or_value(y))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def x(self):
    return self.operation.operands[0]

  @builtins.property
  def y(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MulEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.mul_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MulEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.mul_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, rhs, lhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(rhs))
    operands.append(_get_op_result_or_value(lhs))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def rhs(self):
    return self.operation.operands[0]

  @builtins.property
  def lhs(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MuxOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.mux"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, cond, c1, c2, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(cond))
    operands.append(_get_op_result_or_value(c1))
    operands.append(_get_op_result_or_value(c2))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def cond(self):
    return self.operation.operands[0]

  @builtins.property
  def c1(self):
    return self.operation.operands[1]

  @builtins.property
  def c2(self):
    return self.operation.operands[2]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class NegEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.neg_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RoundEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.round"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubEintIntOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.sub_eint_int"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.sub_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SubIntEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.sub_int_eint"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, a, b, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToBoolOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.to_bool"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToSignedOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.to_signed"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ToUnsignedOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.to_unsigned"

  _ODS_REGIONS = (0, True)

  def __init__(self, result, input, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(input))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(result)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def input(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ZeroEintOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.zero"

  _ODS_REGIONS = (0, True)

  def __init__(self, out, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(out)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def out(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ZeroTensorOp(_ods_ir.OpView):
  OPERATION_NAME = "FHE.zero_tensor"

  _ODS_REGIONS = (0, True)

  def __init__(self, tensor, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(tensor)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def tensor(self):
    return self.operation.results[0]
