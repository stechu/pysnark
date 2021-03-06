# automatically generated by the FlatBuffers compiler, do not modify

# namespace: zkinterface

import flatbuffers

# /// R1CSConstraints represents constraints to be added to the constraint system.
# ///
# /// Multiple such messages are equivalent to the concatenation of `constraints` arrays.
class R1CSConstraints(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsR1CSConstraints(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = R1CSConstraints()
        x.Init(buf, n + offset)
        return x

    # R1CSConstraints
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # R1CSConstraints
    def Constraints(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .BilinearConstraint import BilinearConstraint
            obj = BilinearConstraint()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # R1CSConstraints
    def ConstraintsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Optional: Any complementary info that may be useful.
# ///
# /// Example: human-readable descriptions.
# /// Example: custom hints to an optimizer or analyzer.
    # R1CSConstraints
    def Info(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .KeyValue import KeyValue
            obj = KeyValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # R1CSConstraints
    def InfoLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def R1CSConstraintsStart(builder): builder.StartObject(2)
def R1CSConstraintsAddConstraints(builder, constraints): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(constraints), 0)
def R1CSConstraintsStartConstraintsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def R1CSConstraintsAddInfo(builder, info): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(info), 0)
def R1CSConstraintsStartInfoVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def R1CSConstraintsEnd(builder): return builder.EndObject()
