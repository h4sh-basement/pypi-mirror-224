# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AdmissionConditionBlock(AbstractModel):
    """入院情况

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文

注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdmissionDiagnosisBlock(AbstractModel):
    """入院诊断

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Advice(AbstractModel):
    """建议

    """

    def __init__(self):
        r"""
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AspectRatio(AbstractModel):
    """纵横比

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Number: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: str
        :param _Relation: 关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Relation: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Index = None
        self._Number = None
        self._Relation = None
        self._Src = None
        self._Value = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Number = params.get("Number")
        self._Relation = params.get("Relation")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseInfo(AbstractModel):
    """标准信息类

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 标准值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Index = None
        self._Src = None
        self._Value = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param _Name: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Alias: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Alias = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Alias = params.get("Alias")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem2(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param _Name: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem3(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param _Name: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        :param _Order: 第几次
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Coords = None
        self._Order = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BiopsyPart(AbstractModel):
    """活检部位

    """

    def __init__(self):
        r"""
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Value = None
        self._Src = None
        self._Coords = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Src = params.get("Src")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BirthCert(AbstractModel):
    """出生证明结构化信息

    """

    def __init__(self):
        r"""
        :param _NeonatalInfo: 新生儿信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalInfo: :class:`tencentcloud.mrs.v20200910.models.NeonatalInfo`
        :param _MotherInfo: 母亲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MotherInfo: :class:`tencentcloud.mrs.v20200910.models.ParentInfo`
        :param _FatherInfo: 父亲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FatherInfo: :class:`tencentcloud.mrs.v20200910.models.ParentInfo`
        :param _IssueInfo: 签发信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueInfo: :class:`tencentcloud.mrs.v20200910.models.IssueInfo`
        """
        self._NeonatalInfo = None
        self._MotherInfo = None
        self._FatherInfo = None
        self._IssueInfo = None

    @property
    def NeonatalInfo(self):
        return self._NeonatalInfo

    @NeonatalInfo.setter
    def NeonatalInfo(self, NeonatalInfo):
        self._NeonatalInfo = NeonatalInfo

    @property
    def MotherInfo(self):
        return self._MotherInfo

    @MotherInfo.setter
    def MotherInfo(self, MotherInfo):
        self._MotherInfo = MotherInfo

    @property
    def FatherInfo(self):
        return self._FatherInfo

    @FatherInfo.setter
    def FatherInfo(self, FatherInfo):
        self._FatherInfo = FatherInfo

    @property
    def IssueInfo(self):
        return self._IssueInfo

    @IssueInfo.setter
    def IssueInfo(self, IssueInfo):
        self._IssueInfo = IssueInfo


    def _deserialize(self, params):
        if params.get("NeonatalInfo") is not None:
            self._NeonatalInfo = NeonatalInfo()
            self._NeonatalInfo._deserialize(params.get("NeonatalInfo"))
        if params.get("MotherInfo") is not None:
            self._MotherInfo = ParentInfo()
            self._MotherInfo._deserialize(params.get("MotherInfo"))
        if params.get("FatherInfo") is not None:
            self._FatherInfo = ParentInfo()
            self._FatherInfo._deserialize(params.get("FatherInfo"))
        if params.get("IssueInfo") is not None:
            self._IssueInfo = IssueInfo()
            self._IssueInfo._deserialize(params.get("IssueInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BirthPlaceBlock(AbstractModel):
    """出生地

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockInfo(AbstractModel):
    """块信息

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        """
        self._Index = None
        self._Positive = None
        self._Src = None
        self._Value = None
        self._Type = None
        self._Name = None
        self._Size = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Positive = params.get("Positive")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        if params.get("Size") is not None:
            self._Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self._Size.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockInfoV2(AbstractModel):
    """块信息

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Code: 疾病编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        """
        self._Index = None
        self._Src = None
        self._Value = None
        self._Name = None
        self._Code = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BloodPressureBlock(AbstractModel):
    """血压

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _NormDiastolic: 舒张压
注意：此字段可能返回 null，表示取不到有效值。
        :type NormDiastolic: str
        :param _NormSystolic: 收缩压
注意：此字段可能返回 null，表示取不到有效值。
        :type NormSystolic: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Unit = None
        self._Value = None
        self._NormDiastolic = None
        self._NormSystolic = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def NormDiastolic(self):
        return self._NormDiastolic

    @NormDiastolic.setter
    def NormDiastolic(self, NormDiastolic):
        self._NormDiastolic = NormDiastolic

    @property
    def NormSystolic(self):
        return self._NormSystolic

    @NormSystolic.setter
    def NormSystolic(self, NormSystolic):
        self._NormSystolic = NormSystolic


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        self._NormDiastolic = params.get("NormDiastolic")
        self._NormSystolic = params.get("NormSystolic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyExaminationBlock(AbstractModel):
    """查体

    """

    def __init__(self):
        r"""
        :param _BodyTemperature: 体温
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyTemperature: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param _Pulse: 脉搏
注意：此字段可能返回 null，表示取不到有效值。
        :type Pulse: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param _Breathe: 呼吸
注意：此字段可能返回 null，表示取不到有效值。
        :type Breathe: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param _BloodPressure: 血压
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodPressure: :class:`tencentcloud.mrs.v20200910.models.BloodPressureBlock`
        """
        self._BodyTemperature = None
        self._Pulse = None
        self._Breathe = None
        self._BloodPressure = None

    @property
    def BodyTemperature(self):
        return self._BodyTemperature

    @BodyTemperature.setter
    def BodyTemperature(self, BodyTemperature):
        self._BodyTemperature = BodyTemperature

    @property
    def Pulse(self):
        return self._Pulse

    @Pulse.setter
    def Pulse(self, Pulse):
        self._Pulse = Pulse

    @property
    def Breathe(self):
        return self._Breathe

    @Breathe.setter
    def Breathe(self, Breathe):
        self._Breathe = Breathe

    @property
    def BloodPressure(self):
        return self._BloodPressure

    @BloodPressure.setter
    def BloodPressure(self, BloodPressure):
        self._BloodPressure = BloodPressure


    def _deserialize(self, params):
        if params.get("BodyTemperature") is not None:
            self._BodyTemperature = BodyTemperatureBlock()
            self._BodyTemperature._deserialize(params.get("BodyTemperature"))
        if params.get("Pulse") is not None:
            self._Pulse = BodyTemperatureBlock()
            self._Pulse._deserialize(params.get("Pulse"))
        if params.get("Breathe") is not None:
            self._Breathe = BodyTemperatureBlock()
            self._Breathe._deserialize(params.get("Breathe"))
        if params.get("BloodPressure") is not None:
            self._BloodPressure = BloodPressureBlock()
            self._BloodPressure._deserialize(params.get("BloodPressure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyTemperatureBlock(AbstractModel):
    """体温名称

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Unit = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Check(AbstractModel):
    """检查报告单

    """

    def __init__(self):
        r"""
        :param _Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.Desc`
        :param _Summary: 结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.Summary`
        """
        self._Desc = None
        self._Summary = None

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary


    def _deserialize(self, params):
        if params.get("Desc") is not None:
            self._Desc = Desc()
            self._Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self._Summary = Summary()
            self._Summary._deserialize(params.get("Summary"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChiefComplaintBlock(AbstractModel):
    """主诉

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 单位输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Detail: 主诉详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of ChiefComplaintDetailBlock
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Detail = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = ChiefComplaintDetailBlock()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChiefComplaintDetailBlock(AbstractModel):
    """主诉详情

    """

    def __init__(self):
        r"""
        :param _DiseaseName: 疾病名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseName: str
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param _Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        """
        self._DiseaseName = None
        self._Part = None
        self._Time = None
        self._TimeType = None

    @property
    def DiseaseName(self):
        return self._DiseaseName

    @DiseaseName.setter
    def DiseaseName(self, DiseaseName):
        self._DiseaseName = DiseaseName

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType


    def _deserialize(self, params):
        self._DiseaseName = params.get("DiseaseName")
        self._Part = params.get("Part")
        self._Time = params.get("Time")
        self._TimeType = params.get("TimeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClinicalStaging(AbstractModel):
    """临床分期

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _Points: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of Point
        """
        self._Points = None

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = Point()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _X: 左上角x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param _Y: 左上角y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param _Width: 宽度，单位像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 高度，单位像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CovidItem(AbstractModel):
    """核酸报告结论结构

    """

    def __init__(self):
        r"""
        :param _SampleTime: 采样时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _TestTime: 检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TestTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _TestOrganization: 检测机构
注意：此字段可能返回 null，表示取不到有效值。
        :type TestOrganization: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _TestResult: 检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TestResult: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _CodeColor: 健康码颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeColor: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self._SampleTime = None
        self._TestTime = None
        self._TestOrganization = None
        self._TestResult = None
        self._CodeColor = None

    @property
    def SampleTime(self):
        return self._SampleTime

    @SampleTime.setter
    def SampleTime(self, SampleTime):
        self._SampleTime = SampleTime

    @property
    def TestTime(self):
        return self._TestTime

    @TestTime.setter
    def TestTime(self, TestTime):
        self._TestTime = TestTime

    @property
    def TestOrganization(self):
        return self._TestOrganization

    @TestOrganization.setter
    def TestOrganization(self, TestOrganization):
        self._TestOrganization = TestOrganization

    @property
    def TestResult(self):
        return self._TestResult

    @TestResult.setter
    def TestResult(self, TestResult):
        self._TestResult = TestResult

    @property
    def CodeColor(self):
        return self._CodeColor

    @CodeColor.setter
    def CodeColor(self, CodeColor):
        self._CodeColor = CodeColor


    def _deserialize(self, params):
        if params.get("SampleTime") is not None:
            self._SampleTime = BaseItem()
            self._SampleTime._deserialize(params.get("SampleTime"))
        if params.get("TestTime") is not None:
            self._TestTime = BaseItem()
            self._TestTime._deserialize(params.get("TestTime"))
        if params.get("TestOrganization") is not None:
            self._TestOrganization = BaseItem()
            self._TestOrganization._deserialize(params.get("TestOrganization"))
        if params.get("TestResult") is not None:
            self._TestResult = BaseItem()
            self._TestResult._deserialize(params.get("TestResult"))
        if params.get("CodeColor") is not None:
            self._CodeColor = BaseItem()
            self._CodeColor._deserialize(params.get("CodeColor"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CovidItemsInfo(AbstractModel):
    """核酸报告结论

    """

    def __init__(self):
        r"""
        :param _CovidItems: 核酸报告结论
注意：此字段可能返回 null，表示取不到有效值。
        :type CovidItems: list of CovidItem
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._CovidItems = None
        self._Version = None

    @property
    def CovidItems(self):
        return self._CovidItems

    @CovidItems.setter
    def CovidItems(self, CovidItems):
        self._CovidItems = CovidItems

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        if params.get("CovidItems") is not None:
            self._CovidItems = []
            for item in params.get("CovidItems"):
                obj = CovidItem()
                obj._deserialize(item)
                self._CovidItems.append(obj)
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeathDateBlock(AbstractModel):
    """死亡时间

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Type = None
        self._Norm = None
        self._Unit = None
        self._Timestamp = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Type = params.get("Type")
        self._Norm = params.get("Norm")
        self._Unit = params.get("Unit")
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Desc(AbstractModel):
    """描述

    """

    def __init__(self):
        r"""
        :param _Text: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Organ: 器官
注意：此字段可能返回 null，表示取不到有效值。
        :type Organ: list of Organ
        :param _Tuber: 结节
注意：此字段可能返回 null，表示取不到有效值。
        :type Tuber: list of TuberInfo
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Text = None
        self._Organ = None
        self._Tuber = None
        self._Coords = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Organ(self):
        return self._Organ

    @Organ.setter
    def Organ(self, Organ):
        self._Organ = Organ

    @property
    def Tuber(self):
        return self._Tuber

    @Tuber.setter
    def Tuber(self, Tuber):
        self._Tuber = Tuber

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Organ") is not None:
            self._Organ = []
            for item in params.get("Organ"):
                obj = Organ()
                obj._deserialize(item)
                self._Organ.append(obj)
        if params.get("Tuber") is not None:
            self._Tuber = []
            for item in params.get("Tuber"):
                obj = TuberInfo()
                obj._deserialize(item)
                self._Tuber.append(obj)
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescInfo(AbstractModel):
    """描述段落

    """

    def __init__(self):
        r"""
        :param _Text: 描述段落文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Infos: 描述段落详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Infos: list of DetailInformation
        """
        self._Text = None
        self._Infos = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self._Text = BaseInfo()
            self._Text._deserialize(params.get("Text"))
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DetailInformation()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetailInformation(AbstractModel):
    """详情

    """

    def __init__(self):
        r"""
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _TissueSizes: 组织大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TissueSizes: list of Size
        :param _TuberSizes: 结节大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TuberSizes: list of Size
        :param _CancerSizes: 肿瘤大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerSizes: list of Size
        :param _HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyLevel: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyType: :class:`tencentcloud.mrs.v20200910.models.HistologyTypeV2`
        :param _Invasive: 侵犯
注意：此字段可能返回 null，表示取不到有效值。
        :type Invasive: list of InvasiveV2
        :param _PTNM: pTNM
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.PTNM`
        :param _InfiltrationDepth: 浸润深度
注意：此字段可能返回 null，表示取不到有效值。
        :type InfiltrationDepth: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _TuberNum: 结节数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TuberNum: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Calcification: 钙化
注意：此字段可能返回 null，表示取不到有效值。
        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Necrosis: 坏死
注意：此字段可能返回 null，表示取不到有效值。
        :type Necrosis: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Abnormity: 异形
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormity: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Breaked: 断链
注意：此字段可能返回 null，表示取不到有效值。
        :type Breaked: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        """
        self._Part = None
        self._TissueSizes = None
        self._TuberSizes = None
        self._CancerSizes = None
        self._HistologyLevel = None
        self._HistologyType = None
        self._Invasive = None
        self._PTNM = None
        self._InfiltrationDepth = None
        self._TuberNum = None
        self._Calcification = None
        self._Necrosis = None
        self._Abnormity = None
        self._Breaked = None

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def TissueSizes(self):
        return self._TissueSizes

    @TissueSizes.setter
    def TissueSizes(self, TissueSizes):
        self._TissueSizes = TissueSizes

    @property
    def TuberSizes(self):
        return self._TuberSizes

    @TuberSizes.setter
    def TuberSizes(self, TuberSizes):
        self._TuberSizes = TuberSizes

    @property
    def CancerSizes(self):
        return self._CancerSizes

    @CancerSizes.setter
    def CancerSizes(self, CancerSizes):
        self._CancerSizes = CancerSizes

    @property
    def HistologyLevel(self):
        return self._HistologyLevel

    @HistologyLevel.setter
    def HistologyLevel(self, HistologyLevel):
        self._HistologyLevel = HistologyLevel

    @property
    def HistologyType(self):
        return self._HistologyType

    @HistologyType.setter
    def HistologyType(self, HistologyType):
        self._HistologyType = HistologyType

    @property
    def Invasive(self):
        return self._Invasive

    @Invasive.setter
    def Invasive(self, Invasive):
        self._Invasive = Invasive

    @property
    def PTNM(self):
        return self._PTNM

    @PTNM.setter
    def PTNM(self, PTNM):
        self._PTNM = PTNM

    @property
    def InfiltrationDepth(self):
        return self._InfiltrationDepth

    @InfiltrationDepth.setter
    def InfiltrationDepth(self, InfiltrationDepth):
        self._InfiltrationDepth = InfiltrationDepth

    @property
    def TuberNum(self):
        return self._TuberNum

    @TuberNum.setter
    def TuberNum(self, TuberNum):
        self._TuberNum = TuberNum

    @property
    def Calcification(self):
        return self._Calcification

    @Calcification.setter
    def Calcification(self, Calcification):
        self._Calcification = Calcification

    @property
    def Necrosis(self):
        return self._Necrosis

    @Necrosis.setter
    def Necrosis(self, Necrosis):
        self._Necrosis = Necrosis

    @property
    def Abnormity(self):
        return self._Abnormity

    @Abnormity.setter
    def Abnormity(self, Abnormity):
        self._Abnormity = Abnormity

    @property
    def Breaked(self):
        return self._Breaked

    @Breaked.setter
    def Breaked(self, Breaked):
        self._Breaked = Breaked


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        if params.get("TissueSizes") is not None:
            self._TissueSizes = []
            for item in params.get("TissueSizes"):
                obj = Size()
                obj._deserialize(item)
                self._TissueSizes.append(obj)
        if params.get("TuberSizes") is not None:
            self._TuberSizes = []
            for item in params.get("TuberSizes"):
                obj = Size()
                obj._deserialize(item)
                self._TuberSizes.append(obj)
        if params.get("CancerSizes") is not None:
            self._CancerSizes = []
            for item in params.get("CancerSizes"):
                obj = Size()
                obj._deserialize(item)
                self._CancerSizes.append(obj)
        if params.get("HistologyLevel") is not None:
            self._HistologyLevel = BaseInfo()
            self._HistologyLevel._deserialize(params.get("HistologyLevel"))
        if params.get("HistologyType") is not None:
            self._HistologyType = HistologyTypeV2()
            self._HistologyType._deserialize(params.get("HistologyType"))
        if params.get("Invasive") is not None:
            self._Invasive = []
            for item in params.get("Invasive"):
                obj = InvasiveV2()
                obj._deserialize(item)
                self._Invasive.append(obj)
        if params.get("PTNM") is not None:
            self._PTNM = PTNM()
            self._PTNM._deserialize(params.get("PTNM"))
        if params.get("InfiltrationDepth") is not None:
            self._InfiltrationDepth = BaseInfo()
            self._InfiltrationDepth._deserialize(params.get("InfiltrationDepth"))
        if params.get("TuberNum") is not None:
            self._TuberNum = BaseInfo()
            self._TuberNum._deserialize(params.get("TuberNum"))
        if params.get("Calcification") is not None:
            self._Calcification = BaseInfo()
            self._Calcification._deserialize(params.get("Calcification"))
        if params.get("Necrosis") is not None:
            self._Necrosis = BaseInfo()
            self._Necrosis._deserialize(params.get("Necrosis"))
        if params.get("Abnormity") is not None:
            self._Abnormity = BaseInfo()
            self._Abnormity._deserialize(params.get("Abnormity"))
        if params.get("Breaked") is not None:
            self._Breaked = BaseInfo()
            self._Breaked._deserialize(params.get("Breaked"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagCert(AbstractModel):
    """诊断证明

    """

    def __init__(self):
        r"""
        :param _Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`
        :param _Diagnosis: 诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnosis: list of DiagCertItem
        """
        self._Advice = None
        self._Diagnosis = None

    @property
    def Advice(self):
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def Diagnosis(self):
        return self._Diagnosis

    @Diagnosis.setter
    def Diagnosis(self, Diagnosis):
        self._Diagnosis = Diagnosis


    def _deserialize(self, params):
        if params.get("Advice") is not None:
            self._Advice = Advice()
            self._Advice._deserialize(params.get("Advice"))
        if params.get("Diagnosis") is not None:
            self._Diagnosis = []
            for item in params.get("Diagnosis"):
                obj = DiagCertItem()
                obj._deserialize(item)
                self._Diagnosis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagCertItem(AbstractModel):
    """诊断证明项

    """

    def __init__(self):
        r"""
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self._Text = None
        self._Type = None
        self._Value = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeConditionBlock(AbstractModel):
    """出院情况

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Norm = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Norm = params.get("Norm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeDiagnosis(AbstractModel):
    """出入院诊断

    """

    def __init__(self):
        r"""
        :param _TableIndex: 表格位置
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIndex: int
        :param _OutDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _DiseaseCode: 疾病编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseCode: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _InStatus: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type InStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _OutStatus: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type OutStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        """
        self._TableIndex = None
        self._OutDiagnosis = None
        self._DiseaseCode = None
        self._InStatus = None
        self._OutStatus = None

    @property
    def TableIndex(self):
        return self._TableIndex

    @TableIndex.setter
    def TableIndex(self, TableIndex):
        self._TableIndex = TableIndex

    @property
    def OutDiagnosis(self):
        return self._OutDiagnosis

    @OutDiagnosis.setter
    def OutDiagnosis(self, OutDiagnosis):
        self._OutDiagnosis = OutDiagnosis

    @property
    def DiseaseCode(self):
        return self._DiseaseCode

    @DiseaseCode.setter
    def DiseaseCode(self, DiseaseCode):
        self._DiseaseCode = DiseaseCode

    @property
    def InStatus(self):
        return self._InStatus

    @InStatus.setter
    def InStatus(self, InStatus):
        self._InStatus = InStatus

    @property
    def OutStatus(self):
        return self._OutStatus

    @OutStatus.setter
    def OutStatus(self, OutStatus):
        self._OutStatus = OutStatus


    def _deserialize(self, params):
        self._TableIndex = params.get("TableIndex")
        if params.get("OutDiagnosis") is not None:
            self._OutDiagnosis = BlockInfo()
            self._OutDiagnosis._deserialize(params.get("OutDiagnosis"))
        if params.get("DiseaseCode") is not None:
            self._DiseaseCode = BlockInfo()
            self._DiseaseCode._deserialize(params.get("DiseaseCode"))
        if params.get("InStatus") is not None:
            self._InStatus = BlockInfo()
            self._InStatus._deserialize(params.get("InStatus"))
        if params.get("OutStatus") is not None:
            self._OutStatus = BlockInfo()
            self._OutStatus._deserialize(params.get("OutStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeDiagnosisBlock(AbstractModel):
    """出院诊断

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeInfoBlock(AbstractModel):
    """出入院结构体

    """

    def __init__(self):
        r"""
        :param _DiseaseHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseHistoryBlock`
        :param _PersonalHistory: 个人史
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalHistoryBlock`
        :param _DrugHistory: 药物史
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugHistory: :class:`tencentcloud.mrs.v20200910.models.DrugHistoryBlock`
        :param _TreatmentRecord: 治疗相关
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentRecord: :class:`tencentcloud.mrs.v20200910.models.TreatmentRecordBlock`
        :param _ParagraphBlock: 文本段落
注意：此字段可能返回 null，表示取不到有效值。
        :type ParagraphBlock: :class:`tencentcloud.mrs.v20200910.models.ParagraphBlock`
        """
        self._DiseaseHistory = None
        self._PersonalHistory = None
        self._DrugHistory = None
        self._TreatmentRecord = None
        self._ParagraphBlock = None

    @property
    def DiseaseHistory(self):
        return self._DiseaseHistory

    @DiseaseHistory.setter
    def DiseaseHistory(self, DiseaseHistory):
        self._DiseaseHistory = DiseaseHistory

    @property
    def PersonalHistory(self):
        return self._PersonalHistory

    @PersonalHistory.setter
    def PersonalHistory(self, PersonalHistory):
        self._PersonalHistory = PersonalHistory

    @property
    def DrugHistory(self):
        return self._DrugHistory

    @DrugHistory.setter
    def DrugHistory(self, DrugHistory):
        self._DrugHistory = DrugHistory

    @property
    def TreatmentRecord(self):
        return self._TreatmentRecord

    @TreatmentRecord.setter
    def TreatmentRecord(self, TreatmentRecord):
        self._TreatmentRecord = TreatmentRecord

    @property
    def ParagraphBlock(self):
        return self._ParagraphBlock

    @ParagraphBlock.setter
    def ParagraphBlock(self, ParagraphBlock):
        self._ParagraphBlock = ParagraphBlock


    def _deserialize(self, params):
        if params.get("DiseaseHistory") is not None:
            self._DiseaseHistory = DiseaseHistoryBlock()
            self._DiseaseHistory._deserialize(params.get("DiseaseHistory"))
        if params.get("PersonalHistory") is not None:
            self._PersonalHistory = PersonalHistoryBlock()
            self._PersonalHistory._deserialize(params.get("PersonalHistory"))
        if params.get("DrugHistory") is not None:
            self._DrugHistory = DrugHistoryBlock()
            self._DrugHistory._deserialize(params.get("DrugHistory"))
        if params.get("TreatmentRecord") is not None:
            self._TreatmentRecord = TreatmentRecordBlock()
            self._TreatmentRecord._deserialize(params.get("TreatmentRecord"))
        if params.get("ParagraphBlock") is not None:
            self._ParagraphBlock = ParagraphBlock()
            self._ParagraphBlock._deserialize(params.get("ParagraphBlock"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseaseHistoryBlock(AbstractModel):
    """疾病史

    """

    def __init__(self):
        r"""
        :param _MainDiseaseHistory: 主要病史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param _AllergyHistory: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param _InfectHistory: 注射史
注意：此字段可能返回 null，表示取不到有效值。
        :type InfectHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param _SurgeryHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryHistory: :class:`tencentcloud.mrs.v20200910.models.SurgeryHistoryBlock`
        :param _TransfusionHistory: 输血史
注意：此字段可能返回 null，表示取不到有效值。
        :type TransfusionHistory: :class:`tencentcloud.mrs.v20200910.models.TransfusionHistoryBlock`
        """
        self._MainDiseaseHistory = None
        self._AllergyHistory = None
        self._InfectHistory = None
        self._SurgeryHistory = None
        self._TransfusionHistory = None

    @property
    def MainDiseaseHistory(self):
        return self._MainDiseaseHistory

    @MainDiseaseHistory.setter
    def MainDiseaseHistory(self, MainDiseaseHistory):
        self._MainDiseaseHistory = MainDiseaseHistory

    @property
    def AllergyHistory(self):
        return self._AllergyHistory

    @AllergyHistory.setter
    def AllergyHistory(self, AllergyHistory):
        self._AllergyHistory = AllergyHistory

    @property
    def InfectHistory(self):
        return self._InfectHistory

    @InfectHistory.setter
    def InfectHistory(self, InfectHistory):
        self._InfectHistory = InfectHistory

    @property
    def SurgeryHistory(self):
        return self._SurgeryHistory

    @SurgeryHistory.setter
    def SurgeryHistory(self, SurgeryHistory):
        self._SurgeryHistory = SurgeryHistory

    @property
    def TransfusionHistory(self):
        return self._TransfusionHistory

    @TransfusionHistory.setter
    def TransfusionHistory(self, TransfusionHistory):
        self._TransfusionHistory = TransfusionHistory


    def _deserialize(self, params):
        if params.get("MainDiseaseHistory") is not None:
            self._MainDiseaseHistory = MainDiseaseHistoryBlock()
            self._MainDiseaseHistory._deserialize(params.get("MainDiseaseHistory"))
        if params.get("AllergyHistory") is not None:
            self._AllergyHistory = MainDiseaseHistoryBlock()
            self._AllergyHistory._deserialize(params.get("AllergyHistory"))
        if params.get("InfectHistory") is not None:
            self._InfectHistory = MainDiseaseHistoryBlock()
            self._InfectHistory._deserialize(params.get("InfectHistory"))
        if params.get("SurgeryHistory") is not None:
            self._SurgeryHistory = SurgeryHistoryBlock()
            self._SurgeryHistory._deserialize(params.get("SurgeryHistory"))
        if params.get("TransfusionHistory") is not None:
            self._TransfusionHistory = TransfusionHistoryBlock()
            self._TransfusionHistory._deserialize(params.get("TransfusionHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseaseMedicalHistory(AbstractModel):
    """疾病史

    """

    def __init__(self):
        r"""
        :param _MainDiseaseHistory: 主病史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistory: str
        :param _AllergyHistory: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistory: str
        :param _InfectHistory: 传染疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type InfectHistory: str
        :param _OperationHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationHistory: str
        :param _TransfusionHistory: 输血史
注意：此字段可能返回 null，表示取不到有效值。
        :type TransfusionHistory: str
        """
        self._MainDiseaseHistory = None
        self._AllergyHistory = None
        self._InfectHistory = None
        self._OperationHistory = None
        self._TransfusionHistory = None

    @property
    def MainDiseaseHistory(self):
        return self._MainDiseaseHistory

    @MainDiseaseHistory.setter
    def MainDiseaseHistory(self, MainDiseaseHistory):
        self._MainDiseaseHistory = MainDiseaseHistory

    @property
    def AllergyHistory(self):
        return self._AllergyHistory

    @AllergyHistory.setter
    def AllergyHistory(self, AllergyHistory):
        self._AllergyHistory = AllergyHistory

    @property
    def InfectHistory(self):
        return self._InfectHistory

    @InfectHistory.setter
    def InfectHistory(self, InfectHistory):
        self._InfectHistory = InfectHistory

    @property
    def OperationHistory(self):
        return self._OperationHistory

    @OperationHistory.setter
    def OperationHistory(self, OperationHistory):
        self._OperationHistory = OperationHistory

    @property
    def TransfusionHistory(self):
        return self._TransfusionHistory

    @TransfusionHistory.setter
    def TransfusionHistory(self, TransfusionHistory):
        self._TransfusionHistory = TransfusionHistory


    def _deserialize(self, params):
        self._MainDiseaseHistory = params.get("MainDiseaseHistory")
        self._AllergyHistory = params.get("AllergyHistory")
        self._InfectHistory = params.get("InfectHistory")
        self._OperationHistory = params.get("OperationHistory")
        self._TransfusionHistory = params.get("TransfusionHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseasePresentBlock(AbstractModel):
    """现病史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Norm: 归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Norm = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Norm = params.get("Norm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DosageBlock(AbstractModel):
    """药物用法用量

    """

    def __init__(self):
        r"""
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _SingleMeasurement: 单次计量
注意：此字段可能返回 null，表示取不到有效值。
        :type SingleMeasurement: str
        :param _Frequency: 频次
注意：此字段可能返回 null，表示取不到有效值。
        :type Frequency: str
        :param _DrugDeliveryRoute: 给药途径
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugDeliveryRoute: str
        """
        self._Value = None
        self._SingleMeasurement = None
        self._Frequency = None
        self._DrugDeliveryRoute = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SingleMeasurement(self):
        return self._SingleMeasurement

    @SingleMeasurement.setter
    def SingleMeasurement(self, SingleMeasurement):
        self._SingleMeasurement = SingleMeasurement

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def DrugDeliveryRoute(self):
        return self._DrugDeliveryRoute

    @DrugDeliveryRoute.setter
    def DrugDeliveryRoute(self, DrugDeliveryRoute):
        self._DrugDeliveryRoute = DrugDeliveryRoute


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._SingleMeasurement = params.get("SingleMeasurement")
        self._Frequency = params.get("Frequency")
        self._DrugDeliveryRoute = params.get("DrugDeliveryRoute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugHistoryBlock(AbstractModel):
    """药物史

    """

    def __init__(self):
        r"""
        :param _Name: 药品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _DrugList: 药物列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugList: list of DrugListBlock
        :param _Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._DrugList = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def DrugList(self):
        return self._DrugList

    @DrugList.setter
    def DrugList(self, DrugList):
        self._DrugList = DrugList

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        if params.get("DrugList") is not None:
            self._DrugList = []
            for item in params.get("DrugList"):
                obj = DrugListBlock()
                obj._deserialize(item)
                self._DrugList.append(obj)
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugListBlock(AbstractModel):
    """药物史

    """

    def __init__(self):
        r"""
        :param _CommonName: 通用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param _TradeName: 商品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeName: str
        :param _Dosage: 用法用量
注意：此字段可能返回 null，表示取不到有效值。
        :type Dosage: :class:`tencentcloud.mrs.v20200910.models.DosageBlock`
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._CommonName = None
        self._TradeName = None
        self._Dosage = None
        self._Value = None

    @property
    def CommonName(self):
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName

    @property
    def TradeName(self):
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def Dosage(self):
        return self._Dosage

    @Dosage.setter
    def Dosage(self, Dosage):
        self._Dosage = Dosage

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._CommonName = params.get("CommonName")
        self._TradeName = params.get("TradeName")
        if params.get("Dosage") is not None:
            self._Dosage = DosageBlock()
            self._Dosage._deserialize(params.get("Dosage"))
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcgDescription(AbstractModel):
    """心电图详情

    """

    def __init__(self):
        r"""
        :param _HeartRate: 心率
注意：此字段可能返回 null，表示取不到有效值。
        :type HeartRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _AuricularRate: 心房率
注意：此字段可能返回 null，表示取不到有效值。
        :type AuricularRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _VentricularRate: 心室率
注意：此字段可能返回 null，表示取不到有效值。
        :type VentricularRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _Rhythm: 节律
注意：此字段可能返回 null，表示取不到有效值。
        :type Rhythm: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PDuration: P波时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PDuration: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _QrsDuration: QRS时间
注意：此字段可能返回 null，表示取不到有效值。
        :type QrsDuration: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _QrsAxis: QRS电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type QrsAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PRInterval: P-R间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PRInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PPInterval: P-P间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PPInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _RRInterval: R-R间期
注意：此字段可能返回 null，表示取不到有效值。
        :type RRInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PJInterval: P-J间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PJInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _QTInterval: Q-T间期
注意：此字段可能返回 null，表示取不到有效值。
        :type QTInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _QTCInterval: qt/qtc间期
注意：此字段可能返回 null，表示取不到有效值。
        :type QTCInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _Rv5SV1Amplitude: RV5/SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5SV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _Rv5AddSV1Amplitude: RV5+SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5AddSV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PRTAxis: PRT电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type PRTAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _Rv5Amplitude: RV5振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _SV1Amplitude: SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type SV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _RV6SV2: RV6/SV2
注意：此字段可能返回 null，表示取不到有效值。
        :type RV6SV2: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param _PQRSTAxis: P/QRS/T电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type PQRSTAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        """
        self._HeartRate = None
        self._AuricularRate = None
        self._VentricularRate = None
        self._Rhythm = None
        self._PDuration = None
        self._QrsDuration = None
        self._QrsAxis = None
        self._PRInterval = None
        self._PPInterval = None
        self._RRInterval = None
        self._PJInterval = None
        self._QTInterval = None
        self._QTCInterval = None
        self._Rv5SV1Amplitude = None
        self._Rv5AddSV1Amplitude = None
        self._PRTAxis = None
        self._Rv5Amplitude = None
        self._SV1Amplitude = None
        self._RV6SV2 = None
        self._PQRSTAxis = None

    @property
    def HeartRate(self):
        return self._HeartRate

    @HeartRate.setter
    def HeartRate(self, HeartRate):
        self._HeartRate = HeartRate

    @property
    def AuricularRate(self):
        return self._AuricularRate

    @AuricularRate.setter
    def AuricularRate(self, AuricularRate):
        self._AuricularRate = AuricularRate

    @property
    def VentricularRate(self):
        return self._VentricularRate

    @VentricularRate.setter
    def VentricularRate(self, VentricularRate):
        self._VentricularRate = VentricularRate

    @property
    def Rhythm(self):
        return self._Rhythm

    @Rhythm.setter
    def Rhythm(self, Rhythm):
        self._Rhythm = Rhythm

    @property
    def PDuration(self):
        return self._PDuration

    @PDuration.setter
    def PDuration(self, PDuration):
        self._PDuration = PDuration

    @property
    def QrsDuration(self):
        return self._QrsDuration

    @QrsDuration.setter
    def QrsDuration(self, QrsDuration):
        self._QrsDuration = QrsDuration

    @property
    def QrsAxis(self):
        return self._QrsAxis

    @QrsAxis.setter
    def QrsAxis(self, QrsAxis):
        self._QrsAxis = QrsAxis

    @property
    def PRInterval(self):
        return self._PRInterval

    @PRInterval.setter
    def PRInterval(self, PRInterval):
        self._PRInterval = PRInterval

    @property
    def PPInterval(self):
        return self._PPInterval

    @PPInterval.setter
    def PPInterval(self, PPInterval):
        self._PPInterval = PPInterval

    @property
    def RRInterval(self):
        return self._RRInterval

    @RRInterval.setter
    def RRInterval(self, RRInterval):
        self._RRInterval = RRInterval

    @property
    def PJInterval(self):
        return self._PJInterval

    @PJInterval.setter
    def PJInterval(self, PJInterval):
        self._PJInterval = PJInterval

    @property
    def QTInterval(self):
        return self._QTInterval

    @QTInterval.setter
    def QTInterval(self, QTInterval):
        self._QTInterval = QTInterval

    @property
    def QTCInterval(self):
        return self._QTCInterval

    @QTCInterval.setter
    def QTCInterval(self, QTCInterval):
        self._QTCInterval = QTCInterval

    @property
    def Rv5SV1Amplitude(self):
        return self._Rv5SV1Amplitude

    @Rv5SV1Amplitude.setter
    def Rv5SV1Amplitude(self, Rv5SV1Amplitude):
        self._Rv5SV1Amplitude = Rv5SV1Amplitude

    @property
    def Rv5AddSV1Amplitude(self):
        return self._Rv5AddSV1Amplitude

    @Rv5AddSV1Amplitude.setter
    def Rv5AddSV1Amplitude(self, Rv5AddSV1Amplitude):
        self._Rv5AddSV1Amplitude = Rv5AddSV1Amplitude

    @property
    def PRTAxis(self):
        return self._PRTAxis

    @PRTAxis.setter
    def PRTAxis(self, PRTAxis):
        self._PRTAxis = PRTAxis

    @property
    def Rv5Amplitude(self):
        return self._Rv5Amplitude

    @Rv5Amplitude.setter
    def Rv5Amplitude(self, Rv5Amplitude):
        self._Rv5Amplitude = Rv5Amplitude

    @property
    def SV1Amplitude(self):
        return self._SV1Amplitude

    @SV1Amplitude.setter
    def SV1Amplitude(self, SV1Amplitude):
        self._SV1Amplitude = SV1Amplitude

    @property
    def RV6SV2(self):
        return self._RV6SV2

    @RV6SV2.setter
    def RV6SV2(self, RV6SV2):
        self._RV6SV2 = RV6SV2

    @property
    def PQRSTAxis(self):
        return self._PQRSTAxis

    @PQRSTAxis.setter
    def PQRSTAxis(self, PQRSTAxis):
        self._PQRSTAxis = PQRSTAxis


    def _deserialize(self, params):
        if params.get("HeartRate") is not None:
            self._HeartRate = EcgItem()
            self._HeartRate._deserialize(params.get("HeartRate"))
        if params.get("AuricularRate") is not None:
            self._AuricularRate = EcgItem()
            self._AuricularRate._deserialize(params.get("AuricularRate"))
        if params.get("VentricularRate") is not None:
            self._VentricularRate = EcgItem()
            self._VentricularRate._deserialize(params.get("VentricularRate"))
        if params.get("Rhythm") is not None:
            self._Rhythm = EcgItem()
            self._Rhythm._deserialize(params.get("Rhythm"))
        if params.get("PDuration") is not None:
            self._PDuration = EcgItem()
            self._PDuration._deserialize(params.get("PDuration"))
        if params.get("QrsDuration") is not None:
            self._QrsDuration = EcgItem()
            self._QrsDuration._deserialize(params.get("QrsDuration"))
        if params.get("QrsAxis") is not None:
            self._QrsAxis = EcgItem()
            self._QrsAxis._deserialize(params.get("QrsAxis"))
        if params.get("PRInterval") is not None:
            self._PRInterval = EcgItem()
            self._PRInterval._deserialize(params.get("PRInterval"))
        if params.get("PPInterval") is not None:
            self._PPInterval = EcgItem()
            self._PPInterval._deserialize(params.get("PPInterval"))
        if params.get("RRInterval") is not None:
            self._RRInterval = EcgItem()
            self._RRInterval._deserialize(params.get("RRInterval"))
        if params.get("PJInterval") is not None:
            self._PJInterval = EcgItem()
            self._PJInterval._deserialize(params.get("PJInterval"))
        if params.get("QTInterval") is not None:
            self._QTInterval = EcgItem()
            self._QTInterval._deserialize(params.get("QTInterval"))
        if params.get("QTCInterval") is not None:
            self._QTCInterval = EcgItem()
            self._QTCInterval._deserialize(params.get("QTCInterval"))
        if params.get("Rv5SV1Amplitude") is not None:
            self._Rv5SV1Amplitude = EcgItem()
            self._Rv5SV1Amplitude._deserialize(params.get("Rv5SV1Amplitude"))
        if params.get("Rv5AddSV1Amplitude") is not None:
            self._Rv5AddSV1Amplitude = EcgItem()
            self._Rv5AddSV1Amplitude._deserialize(params.get("Rv5AddSV1Amplitude"))
        if params.get("PRTAxis") is not None:
            self._PRTAxis = EcgItem()
            self._PRTAxis._deserialize(params.get("PRTAxis"))
        if params.get("Rv5Amplitude") is not None:
            self._Rv5Amplitude = EcgItem()
            self._Rv5Amplitude._deserialize(params.get("Rv5Amplitude"))
        if params.get("SV1Amplitude") is not None:
            self._SV1Amplitude = EcgItem()
            self._SV1Amplitude._deserialize(params.get("SV1Amplitude"))
        if params.get("RV6SV2") is not None:
            self._RV6SV2 = EcgItem()
            self._RV6SV2._deserialize(params.get("RV6SV2"))
        if params.get("PQRSTAxis") is not None:
            self._PQRSTAxis = EcgItem()
            self._PQRSTAxis._deserialize(params.get("PQRSTAxis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcgDiagnosis(AbstractModel):
    """心电图诊断

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcgItem(AbstractModel):
    """心电图指标项

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._Name = None
        self._Value = None
        self._Unit = None
        self._Src = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Elastic(AbstractModel):
    """弹性质地

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Index = None
        self._Score = None
        self._Src = None
        self._Value = None
        self._Name = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Score = params.get("Score")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Electrocardiogram(AbstractModel):
    """心电图

    """

    def __init__(self):
        r"""
        :param _EcgDescription: 心电图详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EcgDescription: :class:`tencentcloud.mrs.v20200910.models.EcgDescription`
        :param _EcgDiagnosis: 心电图诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type EcgDiagnosis: :class:`tencentcloud.mrs.v20200910.models.EcgDiagnosis`
        """
        self._EcgDescription = None
        self._EcgDiagnosis = None

    @property
    def EcgDescription(self):
        return self._EcgDescription

    @EcgDescription.setter
    def EcgDescription(self, EcgDescription):
        self._EcgDescription = EcgDescription

    @property
    def EcgDiagnosis(self):
        return self._EcgDiagnosis

    @EcgDiagnosis.setter
    def EcgDiagnosis(self, EcgDiagnosis):
        self._EcgDiagnosis = EcgDiagnosis


    def _deserialize(self, params):
        if params.get("EcgDescription") is not None:
            self._EcgDescription = EcgDescription()
            self._EcgDescription._deserialize(params.get("EcgDescription"))
        if params.get("EcgDiagnosis") is not None:
            self._EcgDiagnosis = EcgDiagnosis()
            self._EcgDiagnosis._deserialize(params.get("EcgDiagnosis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endoscopy(AbstractModel):
    """内窥镜报告

    """

    def __init__(self):
        r"""
        :param _BiopsyPart: 活检部位
注意：此字段可能返回 null，表示取不到有效值。
        :type BiopsyPart: :class:`tencentcloud.mrs.v20200910.models.BiopsyPart`
        :param _Desc: 可见描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.EndoscopyDesc`
        :param _Summary: 结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.Summary`
        """
        self._BiopsyPart = None
        self._Desc = None
        self._Summary = None

    @property
    def BiopsyPart(self):
        return self._BiopsyPart

    @BiopsyPart.setter
    def BiopsyPart(self, BiopsyPart):
        self._BiopsyPart = BiopsyPart

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary


    def _deserialize(self, params):
        if params.get("BiopsyPart") is not None:
            self._BiopsyPart = BiopsyPart()
            self._BiopsyPart._deserialize(params.get("BiopsyPart"))
        if params.get("Desc") is not None:
            self._Desc = EndoscopyDesc()
            self._Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self._Summary = Summary()
            self._Summary._deserialize(params.get("Summary"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndoscopyDesc(AbstractModel):
    """内窥镜描述

    """

    def __init__(self):
        r"""
        :param _Text: 描述内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Organ: 器官
注意：此字段可能返回 null，表示取不到有效值。
        :type Organ: list of EndoscopyOrgan
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Text = None
        self._Organ = None
        self._Coords = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Organ(self):
        return self._Organ

    @Organ.setter
    def Organ(self, Organ):
        self._Organ = Organ

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Organ") is not None:
            self._Organ = []
            for item in params.get("Organ"):
                obj = EndoscopyOrgan()
                obj._deserialize(item)
                self._Organ.append(obj)
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndoscopyOrgan(AbstractModel):
    """内窥部位

    """

    def __init__(self):
        r"""
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _PartAlias: 部位别名
注意：此字段可能返回 null，表示取不到有效值。
        :type PartAlias: str
        :param _SymDescList: 症状描述
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDescList: list of BlockInfo
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Part = None
        self._Index = None
        self._Src = None
        self._PartAlias = None
        self._SymDescList = None
        self._Coords = None

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def PartAlias(self):
        return self._PartAlias

    @PartAlias.setter
    def PartAlias(self, PartAlias):
        self._PartAlias = PartAlias

    @property
    def SymDescList(self):
        return self._SymDescList

    @SymDescList.setter
    def SymDescList(self, SymDescList):
        self._SymDescList = SymDescList

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._PartAlias = params.get("PartAlias")
        if params.get("SymDescList") is not None:
            self._SymDescList = []
            for item in params.get("SymDescList"):
                obj = BlockInfo()
                obj._deserialize(item)
                self._SymDescList.append(obj)
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Exame(AbstractModel):
    """体检结论

    """

    def __init__(self):
        r"""
        :param _OverView: 结论段落
注意：此字段可能返回 null，表示取不到有效值。
        :type OverView: list of ResultInfo
        :param _Abnormality: 异常与建议段落
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormality: list of ResultInfo
        """
        self._OverView = None
        self._Abnormality = None

    @property
    def OverView(self):
        return self._OverView

    @OverView.setter
    def OverView(self, OverView):
        self._OverView = OverView

    @property
    def Abnormality(self):
        return self._Abnormality

    @Abnormality.setter
    def Abnormality(self, Abnormality):
        self._Abnormality = Abnormality


    def _deserialize(self, params):
        if params.get("OverView") is not None:
            self._OverView = []
            for item in params.get("OverView"):
                obj = ResultInfo()
                obj._deserialize(item)
                self._OverView.append(obj)
        if params.get("Abnormality") is not None:
            self._Abnormality = []
            for item in params.get("Abnormality"):
                obj = ResultInfo()
                obj._deserialize(item)
                self._Abnormality.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeChildItem(AbstractModel):
    """眼科子结构

    """

    def __init__(self):
        r"""
        :param _Sph: 球镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Sph: list of BaseItem3
        :param _Cyl: 柱镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Cyl: list of BaseItem3
        :param _Ax: 轴位
注意：此字段可能返回 null，表示取不到有效值。
        :type Ax: list of BaseItem3
        :param _Se: 等效球镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Se: :class:`tencentcloud.mrs.v20200910.models.BaseItem2`
        """
        self._Sph = None
        self._Cyl = None
        self._Ax = None
        self._Se = None

    @property
    def Sph(self):
        return self._Sph

    @Sph.setter
    def Sph(self, Sph):
        self._Sph = Sph

    @property
    def Cyl(self):
        return self._Cyl

    @Cyl.setter
    def Cyl(self, Cyl):
        self._Cyl = Cyl

    @property
    def Ax(self):
        return self._Ax

    @Ax.setter
    def Ax(self, Ax):
        self._Ax = Ax

    @property
    def Se(self):
        return self._Se

    @Se.setter
    def Se(self, Se):
        self._Se = Se


    def _deserialize(self, params):
        if params.get("Sph") is not None:
            self._Sph = []
            for item in params.get("Sph"):
                obj = BaseItem3()
                obj._deserialize(item)
                self._Sph.append(obj)
        if params.get("Cyl") is not None:
            self._Cyl = []
            for item in params.get("Cyl"):
                obj = BaseItem3()
                obj._deserialize(item)
                self._Cyl.append(obj)
        if params.get("Ax") is not None:
            self._Ax = []
            for item in params.get("Ax"):
                obj = BaseItem3()
                obj._deserialize(item)
                self._Ax.append(obj)
        if params.get("Se") is not None:
            self._Se = BaseItem2()
            self._Se._deserialize(params.get("Se"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeItem(AbstractModel):
    """眼科结构体

    """

    def __init__(self):
        r"""
        :param _Left: 左眼
注意：此字段可能返回 null，表示取不到有效值。
        :type Left: :class:`tencentcloud.mrs.v20200910.models.EyeChildItem`
        :param _Right: 右眼
注意：此字段可能返回 null，表示取不到有效值。
        :type Right: :class:`tencentcloud.mrs.v20200910.models.EyeChildItem`
        :param _Pd: 瞳距
注意：此字段可能返回 null，表示取不到有效值。
        :type Pd: :class:`tencentcloud.mrs.v20200910.models.BaseItem2`
        """
        self._Left = None
        self._Right = None
        self._Pd = None

    @property
    def Left(self):
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Right(self):
        return self._Right

    @Right.setter
    def Right(self, Right):
        self._Right = Right

    @property
    def Pd(self):
        return self._Pd

    @Pd.setter
    def Pd(self, Pd):
        self._Pd = Pd


    def _deserialize(self, params):
        if params.get("Left") is not None:
            self._Left = EyeChildItem()
            self._Left._deserialize(params.get("Left"))
        if params.get("Right") is not None:
            self._Right = EyeChildItem()
            self._Right._deserialize(params.get("Right"))
        if params.get("Pd") is not None:
            self._Pd = BaseItem2()
            self._Pd._deserialize(params.get("Pd"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeItemsInfo(AbstractModel):
    """眼科报告结构体

    """

    def __init__(self):
        r"""
        :param _EyeItems: 眼科报告
注意：此字段可能返回 null，表示取不到有效值。
        :type EyeItems: :class:`tencentcloud.mrs.v20200910.models.EyeItem`
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._EyeItems = None
        self._Version = None

    @property
    def EyeItems(self):
        return self._EyeItems

    @EyeItems.setter
    def EyeItems(self, EyeItems):
        self._EyeItems = EyeItems

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        if params.get("EyeItems") is not None:
            self._EyeItems = EyeItem()
            self._EyeItems._deserialize(params.get("EyeItems"))
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilyHistoryBlock(AbstractModel):
    """家族史

    """

    def __init__(self):
        r"""
        :param _RelativeHistory: 家庭成员
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeHistory: :class:`tencentcloud.mrs.v20200910.models.RelativeHistoryBlock`
        :param _RelativeCancerHistory: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerHistory: :class:`tencentcloud.mrs.v20200910.models.RelativeCancerHistoryBlock`
        :param _GeneticHistory: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticHistory: :class:`tencentcloud.mrs.v20200910.models.GeneticHistoryBlock`
        """
        self._RelativeHistory = None
        self._RelativeCancerHistory = None
        self._GeneticHistory = None

    @property
    def RelativeHistory(self):
        return self._RelativeHistory

    @RelativeHistory.setter
    def RelativeHistory(self, RelativeHistory):
        self._RelativeHistory = RelativeHistory

    @property
    def RelativeCancerHistory(self):
        return self._RelativeCancerHistory

    @RelativeCancerHistory.setter
    def RelativeCancerHistory(self, RelativeCancerHistory):
        self._RelativeCancerHistory = RelativeCancerHistory

    @property
    def GeneticHistory(self):
        return self._GeneticHistory

    @GeneticHistory.setter
    def GeneticHistory(self, GeneticHistory):
        self._GeneticHistory = GeneticHistory


    def _deserialize(self, params):
        if params.get("RelativeHistory") is not None:
            self._RelativeHistory = RelativeHistoryBlock()
            self._RelativeHistory._deserialize(params.get("RelativeHistory"))
        if params.get("RelativeCancerHistory") is not None:
            self._RelativeCancerHistory = RelativeCancerHistoryBlock()
            self._RelativeCancerHistory._deserialize(params.get("RelativeCancerHistory"))
        if params.get("GeneticHistory") is not None:
            self._GeneticHistory = GeneticHistoryBlock()
            self._GeneticHistory._deserialize(params.get("GeneticHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilyMedicalHistory(AbstractModel):
    """家族疾病史

    """

    def __init__(self):
        r"""
        :param _RelativeHistory: 家族成员史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeHistory: str
        :param _RelativeCancerHistory: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerHistory: str
        :param _GeneticHistory: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticHistory: str
        """
        self._RelativeHistory = None
        self._RelativeCancerHistory = None
        self._GeneticHistory = None

    @property
    def RelativeHistory(self):
        return self._RelativeHistory

    @RelativeHistory.setter
    def RelativeHistory(self, RelativeHistory):
        self._RelativeHistory = RelativeHistory

    @property
    def RelativeCancerHistory(self):
        return self._RelativeCancerHistory

    @RelativeCancerHistory.setter
    def RelativeCancerHistory(self, RelativeCancerHistory):
        self._RelativeCancerHistory = RelativeCancerHistory

    @property
    def GeneticHistory(self):
        return self._GeneticHistory

    @GeneticHistory.setter
    def GeneticHistory(self, GeneticHistory):
        self._GeneticHistory = GeneticHistory


    def _deserialize(self, params):
        self._RelativeHistory = params.get("RelativeHistory")
        self._RelativeCancerHistory = params.get("RelativeCancerHistory")
        self._GeneticHistory = params.get("GeneticHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FertilityHistoryBlock(AbstractModel):
    """婚育史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _PregCount: 妊娠次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PregCount: str
        :param _ProduCount: 生产次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProduCount: str
        """
        self._Name = None
        self._Src = None
        self._State = None
        self._Norm = None
        self._Value = None
        self._PregCount = None
        self._ProduCount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def PregCount(self):
        return self._PregCount

    @PregCount.setter
    def PregCount(self, PregCount):
        self._PregCount = PregCount

    @property
    def ProduCount(self):
        return self._ProduCount

    @ProduCount.setter
    def ProduCount(self, ProduCount):
        self._ProduCount = ProduCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._State = params.get("State")
        self._Norm = params.get("Norm")
        self._Value = params.get("Value")
        self._PregCount = params.get("PregCount")
        self._ProduCount = params.get("ProduCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Fetus(AbstractModel):
    """胎儿数据结构

    """

    def __init__(self):
        r"""
        :param _BPD: 双顶径
注意：此字段可能返回 null，表示取不到有效值。
        :type BPD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _APTD: 腹前后径
注意：此字段可能返回 null，表示取不到有效值。
        :type APTD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _TTD: 腹左右径
注意：此字段可能返回 null，表示取不到有效值。
        :type TTD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _CRL: 头臀径
注意：此字段可能返回 null，表示取不到有效值。
        :type CRL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _HC: 头围
注意：此字段可能返回 null，表示取不到有效值。
        :type HC: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _AC: 腹围
注意：此字段可能返回 null，表示取不到有效值。
        :type AC: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _FL: 股骨长
注意：此字段可能返回 null，表示取不到有效值。
        :type FL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _HL: 肱骨长
注意：此字段可能返回 null，表示取不到有效值。
        :type HL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Weight: 胎儿重量
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _NT: 颈项透明层
注意：此字段可能返回 null，表示取不到有效值。
        :type NT: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _UmbilicalCord: 脐动脉血流
注意：此字段可能返回 null，表示取不到有效值。
        :type UmbilicalCord: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _WaterDeep: 羊水最大深度
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterDeep: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _WaterQuad: 羊水四象限测量
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterQuad: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _AFI: 羊水指数
注意：此字段可能返回 null，表示取不到有效值。
        :type AFI: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _FHR: 胎心
注意：此字段可能返回 null，表示取不到有效值。
        :type FHR: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Movement: 胎动
注意：此字段可能返回 null，表示取不到有效值。
        :type Movement: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Num: 胎数
注意：此字段可能返回 null，表示取不到有效值。
        :type Num: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Position: 胎位
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Alive: 是否活胎
注意：此字段可能返回 null，表示取不到有效值。
        :type Alive: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _PlacentaLocation: 胎盘位置
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaLocation: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _PlacentaThickness: 胎盘厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaThickness: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _PlacentaGrade: 胎盘成熟度
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaGrade: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _GestationTime: 妊娠时间
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationTime: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _GestationPeriod: 妊娠周期
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationPeriod: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _AroundNeck: 绕颈
注意：此字段可能返回 null，表示取不到有效值。
        :type AroundNeck: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Sym: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Sym: list of FieldInfo
        :param _Src: 原文内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._BPD = None
        self._APTD = None
        self._TTD = None
        self._CRL = None
        self._HC = None
        self._AC = None
        self._FL = None
        self._HL = None
        self._Weight = None
        self._NT = None
        self._UmbilicalCord = None
        self._WaterDeep = None
        self._WaterQuad = None
        self._AFI = None
        self._FHR = None
        self._Movement = None
        self._Num = None
        self._Position = None
        self._Alive = None
        self._PlacentaLocation = None
        self._PlacentaThickness = None
        self._PlacentaGrade = None
        self._GestationTime = None
        self._GestationPeriod = None
        self._AroundNeck = None
        self._Sym = None
        self._Src = None

    @property
    def BPD(self):
        return self._BPD

    @BPD.setter
    def BPD(self, BPD):
        self._BPD = BPD

    @property
    def APTD(self):
        return self._APTD

    @APTD.setter
    def APTD(self, APTD):
        self._APTD = APTD

    @property
    def TTD(self):
        return self._TTD

    @TTD.setter
    def TTD(self, TTD):
        self._TTD = TTD

    @property
    def CRL(self):
        return self._CRL

    @CRL.setter
    def CRL(self, CRL):
        self._CRL = CRL

    @property
    def HC(self):
        return self._HC

    @HC.setter
    def HC(self, HC):
        self._HC = HC

    @property
    def AC(self):
        return self._AC

    @AC.setter
    def AC(self, AC):
        self._AC = AC

    @property
    def FL(self):
        return self._FL

    @FL.setter
    def FL(self, FL):
        self._FL = FL

    @property
    def HL(self):
        return self._HL

    @HL.setter
    def HL(self, HL):
        self._HL = HL

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def NT(self):
        return self._NT

    @NT.setter
    def NT(self, NT):
        self._NT = NT

    @property
    def UmbilicalCord(self):
        return self._UmbilicalCord

    @UmbilicalCord.setter
    def UmbilicalCord(self, UmbilicalCord):
        self._UmbilicalCord = UmbilicalCord

    @property
    def WaterDeep(self):
        return self._WaterDeep

    @WaterDeep.setter
    def WaterDeep(self, WaterDeep):
        self._WaterDeep = WaterDeep

    @property
    def WaterQuad(self):
        return self._WaterQuad

    @WaterQuad.setter
    def WaterQuad(self, WaterQuad):
        self._WaterQuad = WaterQuad

    @property
    def AFI(self):
        return self._AFI

    @AFI.setter
    def AFI(self, AFI):
        self._AFI = AFI

    @property
    def FHR(self):
        return self._FHR

    @FHR.setter
    def FHR(self, FHR):
        self._FHR = FHR

    @property
    def Movement(self):
        return self._Movement

    @Movement.setter
    def Movement(self, Movement):
        self._Movement = Movement

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Alive(self):
        return self._Alive

    @Alive.setter
    def Alive(self, Alive):
        self._Alive = Alive

    @property
    def PlacentaLocation(self):
        return self._PlacentaLocation

    @PlacentaLocation.setter
    def PlacentaLocation(self, PlacentaLocation):
        self._PlacentaLocation = PlacentaLocation

    @property
    def PlacentaThickness(self):
        return self._PlacentaThickness

    @PlacentaThickness.setter
    def PlacentaThickness(self, PlacentaThickness):
        self._PlacentaThickness = PlacentaThickness

    @property
    def PlacentaGrade(self):
        return self._PlacentaGrade

    @PlacentaGrade.setter
    def PlacentaGrade(self, PlacentaGrade):
        self._PlacentaGrade = PlacentaGrade

    @property
    def GestationTime(self):
        return self._GestationTime

    @GestationTime.setter
    def GestationTime(self, GestationTime):
        self._GestationTime = GestationTime

    @property
    def GestationPeriod(self):
        return self._GestationPeriod

    @GestationPeriod.setter
    def GestationPeriod(self, GestationPeriod):
        self._GestationPeriod = GestationPeriod

    @property
    def AroundNeck(self):
        return self._AroundNeck

    @AroundNeck.setter
    def AroundNeck(self, AroundNeck):
        self._AroundNeck = AroundNeck

    @property
    def Sym(self):
        return self._Sym

    @Sym.setter
    def Sym(self, Sym):
        self._Sym = Sym

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        if params.get("BPD") is not None:
            self._BPD = FieldInfo()
            self._BPD._deserialize(params.get("BPD"))
        if params.get("APTD") is not None:
            self._APTD = FieldInfo()
            self._APTD._deserialize(params.get("APTD"))
        if params.get("TTD") is not None:
            self._TTD = FieldInfo()
            self._TTD._deserialize(params.get("TTD"))
        if params.get("CRL") is not None:
            self._CRL = FieldInfo()
            self._CRL._deserialize(params.get("CRL"))
        if params.get("HC") is not None:
            self._HC = FieldInfo()
            self._HC._deserialize(params.get("HC"))
        if params.get("AC") is not None:
            self._AC = FieldInfo()
            self._AC._deserialize(params.get("AC"))
        if params.get("FL") is not None:
            self._FL = FieldInfo()
            self._FL._deserialize(params.get("FL"))
        if params.get("HL") is not None:
            self._HL = FieldInfo()
            self._HL._deserialize(params.get("HL"))
        if params.get("Weight") is not None:
            self._Weight = FieldInfo()
            self._Weight._deserialize(params.get("Weight"))
        if params.get("NT") is not None:
            self._NT = FieldInfo()
            self._NT._deserialize(params.get("NT"))
        if params.get("UmbilicalCord") is not None:
            self._UmbilicalCord = FieldInfo()
            self._UmbilicalCord._deserialize(params.get("UmbilicalCord"))
        if params.get("WaterDeep") is not None:
            self._WaterDeep = FieldInfo()
            self._WaterDeep._deserialize(params.get("WaterDeep"))
        if params.get("WaterQuad") is not None:
            self._WaterQuad = FieldInfo()
            self._WaterQuad._deserialize(params.get("WaterQuad"))
        if params.get("AFI") is not None:
            self._AFI = FieldInfo()
            self._AFI._deserialize(params.get("AFI"))
        if params.get("FHR") is not None:
            self._FHR = FieldInfo()
            self._FHR._deserialize(params.get("FHR"))
        if params.get("Movement") is not None:
            self._Movement = FieldInfo()
            self._Movement._deserialize(params.get("Movement"))
        if params.get("Num") is not None:
            self._Num = FieldInfo()
            self._Num._deserialize(params.get("Num"))
        if params.get("Position") is not None:
            self._Position = FieldInfo()
            self._Position._deserialize(params.get("Position"))
        if params.get("Alive") is not None:
            self._Alive = FieldInfo()
            self._Alive._deserialize(params.get("Alive"))
        if params.get("PlacentaLocation") is not None:
            self._PlacentaLocation = FieldInfo()
            self._PlacentaLocation._deserialize(params.get("PlacentaLocation"))
        if params.get("PlacentaThickness") is not None:
            self._PlacentaThickness = FieldInfo()
            self._PlacentaThickness._deserialize(params.get("PlacentaThickness"))
        if params.get("PlacentaGrade") is not None:
            self._PlacentaGrade = FieldInfo()
            self._PlacentaGrade._deserialize(params.get("PlacentaGrade"))
        if params.get("GestationTime") is not None:
            self._GestationTime = FieldInfo()
            self._GestationTime._deserialize(params.get("GestationTime"))
        if params.get("GestationPeriod") is not None:
            self._GestationPeriod = FieldInfo()
            self._GestationPeriod._deserialize(params.get("GestationPeriod"))
        if params.get("AroundNeck") is not None:
            self._AroundNeck = FieldInfo()
            self._AroundNeck._deserialize(params.get("AroundNeck"))
        if params.get("Sym") is not None:
            self._Sym = []
            for item in params.get("Sym"):
                obj = FieldInfo()
                obj._deserialize(item)
                self._Sym.append(obj)
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    """通用块信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Nums: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Nums: list of NumValue
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._Name = None
        self._Value = None
        self._Nums = None
        self._Src = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Nums(self):
        return self._Nums

    @Nums.setter
    def Nums(self, Nums):
        self._Nums = Nums

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Nums") is not None:
            self._Nums = []
            for item in params.get("Nums"):
                obj = NumValue()
                obj._deserialize(item)
                self._Nums.append(obj)
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirstPage(AbstractModel):
    """病案首页

    """

    def __init__(self):
        r"""
        :param _DischargeDiagnosis: 出入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: list of DischargeDiagnosis
        :param _PathologicalDiagnosis: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type ClinicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _DamagePoi: 受伤中毒的外部原因
注意：此字段可能返回 null，表示取不到有效值。
        :type DamagePoi: :class:`tencentcloud.mrs.v20200910.models.BlockInfoV2`
        :param _Fp2NdItems: 病案首页第二页
注意：此字段可能返回 null，表示取不到有效值。
        :type Fp2NdItems: list of Fp2NdItem
        """
        self._DischargeDiagnosis = None
        self._PathologicalDiagnosis = None
        self._ClinicalDiagnosis = None
        self._DamagePoi = None
        self._Fp2NdItems = None

    @property
    def DischargeDiagnosis(self):
        return self._DischargeDiagnosis

    @DischargeDiagnosis.setter
    def DischargeDiagnosis(self, DischargeDiagnosis):
        self._DischargeDiagnosis = DischargeDiagnosis

    @property
    def PathologicalDiagnosis(self):
        return self._PathologicalDiagnosis

    @PathologicalDiagnosis.setter
    def PathologicalDiagnosis(self, PathologicalDiagnosis):
        self._PathologicalDiagnosis = PathologicalDiagnosis

    @property
    def ClinicalDiagnosis(self):
        return self._ClinicalDiagnosis

    @ClinicalDiagnosis.setter
    def ClinicalDiagnosis(self, ClinicalDiagnosis):
        self._ClinicalDiagnosis = ClinicalDiagnosis

    @property
    def DamagePoi(self):
        return self._DamagePoi

    @DamagePoi.setter
    def DamagePoi(self, DamagePoi):
        self._DamagePoi = DamagePoi

    @property
    def Fp2NdItems(self):
        return self._Fp2NdItems

    @Fp2NdItems.setter
    def Fp2NdItems(self, Fp2NdItems):
        self._Fp2NdItems = Fp2NdItems


    def _deserialize(self, params):
        if params.get("DischargeDiagnosis") is not None:
            self._DischargeDiagnosis = []
            for item in params.get("DischargeDiagnosis"):
                obj = DischargeDiagnosis()
                obj._deserialize(item)
                self._DischargeDiagnosis.append(obj)
        if params.get("PathologicalDiagnosis") is not None:
            self._PathologicalDiagnosis = BlockInfo()
            self._PathologicalDiagnosis._deserialize(params.get("PathologicalDiagnosis"))
        if params.get("ClinicalDiagnosis") is not None:
            self._ClinicalDiagnosis = BlockInfo()
            self._ClinicalDiagnosis._deserialize(params.get("ClinicalDiagnosis"))
        if params.get("DamagePoi") is not None:
            self._DamagePoi = BlockInfoV2()
            self._DamagePoi._deserialize(params.get("DamagePoi"))
        if params.get("Fp2NdItems") is not None:
            self._Fp2NdItems = []
            for item in params.get("Fp2NdItems"):
                obj = Fp2NdItem()
                obj._deserialize(item)
                self._Fp2NdItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Fp2NdItem(AbstractModel):
    """病案首页第二页

    """

    def __init__(self):
        r"""
        :param _Code: 手术编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Name: 手术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _StartTime: 手术开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _EndTime: 手术结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Level: 手术等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Type: 手术类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _IncisionHealingGrade: 醉愈合方式
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingGrade: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _AnesthesiaMethod: 麻醉方法
注意：此字段可能返回 null，表示取不到有效值。
        :type AnesthesiaMethod: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self._Code = None
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._Level = None
        self._Type = None
        self._IncisionHealingGrade = None
        self._AnesthesiaMethod = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IncisionHealingGrade(self):
        return self._IncisionHealingGrade

    @IncisionHealingGrade.setter
    def IncisionHealingGrade(self, IncisionHealingGrade):
        self._IncisionHealingGrade = IncisionHealingGrade

    @property
    def AnesthesiaMethod(self):
        return self._AnesthesiaMethod

    @AnesthesiaMethod.setter
    def AnesthesiaMethod(self, AnesthesiaMethod):
        self._AnesthesiaMethod = AnesthesiaMethod


    def _deserialize(self, params):
        if params.get("Code") is not None:
            self._Code = BaseItem()
            self._Code._deserialize(params.get("Code"))
        if params.get("Name") is not None:
            self._Name = BaseItem()
            self._Name._deserialize(params.get("Name"))
        if params.get("StartTime") is not None:
            self._StartTime = BaseItem()
            self._StartTime._deserialize(params.get("StartTime"))
        if params.get("EndTime") is not None:
            self._EndTime = BaseItem()
            self._EndTime._deserialize(params.get("EndTime"))
        if params.get("Level") is not None:
            self._Level = BaseItem()
            self._Level._deserialize(params.get("Level"))
        if params.get("Type") is not None:
            self._Type = BaseItem()
            self._Type._deserialize(params.get("Type"))
        if params.get("IncisionHealingGrade") is not None:
            self._IncisionHealingGrade = BaseItem()
            self._IncisionHealingGrade._deserialize(params.get("IncisionHealingGrade"))
        if params.get("AnesthesiaMethod") is not None:
            self._AnesthesiaMethod = BaseItem()
            self._AnesthesiaMethod._deserialize(params.get("AnesthesiaMethod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneticHistoryBlock(AbstractModel):
    """家族遗传史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _GeneticList: 遗传列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticList: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._GeneticList = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def GeneticList(self):
        return self._GeneticList

    @GeneticList.setter
    def GeneticList(self, GeneticList):
        self._GeneticList = GeneticList

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._GeneticList = params.get("GeneticList")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleParam(AbstractModel):
    """图片处理参数

    """

    def __init__(self):
        r"""
        :param _OcrEngineType: ocr引擎
        :type OcrEngineType: int
        :param _IsReturnText: 是否返回分行文本内容
        :type IsReturnText: bool
        :param _RotateTheAngle: 顺时针旋转角度
        :type RotateTheAngle: float
        :param _AutoFitDirection: 自动适配方向,仅支持优图引擎
        :type AutoFitDirection: bool
        :param _AutoOptimizeCoordinate: 坐标优化
        :type AutoOptimizeCoordinate: bool
        :param _IsScale: 是否开启图片压缩，开启时imageOriginalSize必须正确填写
        :type IsScale: bool
        :param _ImageOriginalSize: 原始图片大小(单位byes),用来判断该图片是否需要压缩
        :type ImageOriginalSize: int
        :param _ScaleTargetSize: 采用后台默认值(2048Kb)
        :type ScaleTargetSize: int
        """
        self._OcrEngineType = None
        self._IsReturnText = None
        self._RotateTheAngle = None
        self._AutoFitDirection = None
        self._AutoOptimizeCoordinate = None
        self._IsScale = None
        self._ImageOriginalSize = None
        self._ScaleTargetSize = None

    @property
    def OcrEngineType(self):
        return self._OcrEngineType

    @OcrEngineType.setter
    def OcrEngineType(self, OcrEngineType):
        self._OcrEngineType = OcrEngineType

    @property
    def IsReturnText(self):
        return self._IsReturnText

    @IsReturnText.setter
    def IsReturnText(self, IsReturnText):
        self._IsReturnText = IsReturnText

    @property
    def RotateTheAngle(self):
        return self._RotateTheAngle

    @RotateTheAngle.setter
    def RotateTheAngle(self, RotateTheAngle):
        self._RotateTheAngle = RotateTheAngle

    @property
    def AutoFitDirection(self):
        return self._AutoFitDirection

    @AutoFitDirection.setter
    def AutoFitDirection(self, AutoFitDirection):
        self._AutoFitDirection = AutoFitDirection

    @property
    def AutoOptimizeCoordinate(self):
        return self._AutoOptimizeCoordinate

    @AutoOptimizeCoordinate.setter
    def AutoOptimizeCoordinate(self, AutoOptimizeCoordinate):
        self._AutoOptimizeCoordinate = AutoOptimizeCoordinate

    @property
    def IsScale(self):
        return self._IsScale

    @IsScale.setter
    def IsScale(self, IsScale):
        self._IsScale = IsScale

    @property
    def ImageOriginalSize(self):
        return self._ImageOriginalSize

    @ImageOriginalSize.setter
    def ImageOriginalSize(self, ImageOriginalSize):
        self._ImageOriginalSize = ImageOriginalSize

    @property
    def ScaleTargetSize(self):
        return self._ScaleTargetSize

    @ScaleTargetSize.setter
    def ScaleTargetSize(self, ScaleTargetSize):
        self._ScaleTargetSize = ScaleTargetSize


    def _deserialize(self, params):
        self._OcrEngineType = params.get("OcrEngineType")
        self._IsReturnText = params.get("IsReturnText")
        self._RotateTheAngle = params.get("RotateTheAngle")
        self._AutoFitDirection = params.get("AutoFitDirection")
        self._AutoOptimizeCoordinate = params.get("AutoOptimizeCoordinate")
        self._IsScale = params.get("IsScale")
        self._ImageOriginalSize = params.get("ImageOriginalSize")
        self._ScaleTargetSize = params.get("ScaleTargetSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyClass(AbstractModel):
    """组织学类

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Index = None
        self._Src = None
        self._Value = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyLevel(AbstractModel):
    """组织学等级

    """

    def __init__(self):
        r"""
        :param _Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._Grade = None
        self._Index = None
        self._Src = None

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        self._Grade = params.get("Grade")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyType(AbstractModel):
    """组织学类型

    """

    def __init__(self):
        r"""
        :param _Infiltration: 浸润
注意：此字段可能返回 null，表示取不到有效值。
        :type Infiltration: str
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._Infiltration = None
        self._Index = None
        self._Src = None
        self._Type = None

    @property
    def Infiltration(self):
        return self._Infiltration

    @Infiltration.setter
    def Infiltration(self, Infiltration):
        self._Infiltration = Infiltration

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Infiltration = params.get("Infiltration")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyTypeV2(AbstractModel):
    """组织学类型

    """

    def __init__(self):
        r"""
        :param _Infiltration: 浸润
注意：此字段可能返回 null，表示取不到有效值。
        :type Infiltration: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Type: 归一化后的组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Infiltration = None
        self._Index = None
        self._Src = None
        self._Type = None
        self._Name = None
        self._Coords = None

    @property
    def Infiltration(self):
        return self._Infiltration

    @Infiltration.setter
    def Infiltration(self, Infiltration):
        self._Infiltration = Infiltration

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Infiltration = params.get("Infiltration")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hospitalization(AbstractModel):
    """出入院信息

    """

    def __init__(self):
        r"""
        :param _AdmissionTime: 入院时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionTime: str
        :param _DischargeTime: 出院时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeTime: str
        :param _AdmissionDays: 住院天数
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDays: str
        :param _AdmissionDignosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDignosis: str
        :param _AdmissionCondition: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionCondition: str
        :param _DiagnosisTreatment: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisTreatment: str
        :param _DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: str
        :param _DischargeInstruction: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstruction: str
        """
        self._AdmissionTime = None
        self._DischargeTime = None
        self._AdmissionDays = None
        self._AdmissionDignosis = None
        self._AdmissionCondition = None
        self._DiagnosisTreatment = None
        self._DischargeDiagnosis = None
        self._DischargeInstruction = None

    @property
    def AdmissionTime(self):
        return self._AdmissionTime

    @AdmissionTime.setter
    def AdmissionTime(self, AdmissionTime):
        self._AdmissionTime = AdmissionTime

    @property
    def DischargeTime(self):
        return self._DischargeTime

    @DischargeTime.setter
    def DischargeTime(self, DischargeTime):
        self._DischargeTime = DischargeTime

    @property
    def AdmissionDays(self):
        return self._AdmissionDays

    @AdmissionDays.setter
    def AdmissionDays(self, AdmissionDays):
        self._AdmissionDays = AdmissionDays

    @property
    def AdmissionDignosis(self):
        return self._AdmissionDignosis

    @AdmissionDignosis.setter
    def AdmissionDignosis(self, AdmissionDignosis):
        self._AdmissionDignosis = AdmissionDignosis

    @property
    def AdmissionCondition(self):
        return self._AdmissionCondition

    @AdmissionCondition.setter
    def AdmissionCondition(self, AdmissionCondition):
        self._AdmissionCondition = AdmissionCondition

    @property
    def DiagnosisTreatment(self):
        return self._DiagnosisTreatment

    @DiagnosisTreatment.setter
    def DiagnosisTreatment(self, DiagnosisTreatment):
        self._DiagnosisTreatment = DiagnosisTreatment

    @property
    def DischargeDiagnosis(self):
        return self._DischargeDiagnosis

    @DischargeDiagnosis.setter
    def DischargeDiagnosis(self, DischargeDiagnosis):
        self._DischargeDiagnosis = DischargeDiagnosis

    @property
    def DischargeInstruction(self):
        return self._DischargeInstruction

    @DischargeInstruction.setter
    def DischargeInstruction(self, DischargeInstruction):
        self._DischargeInstruction = DischargeInstruction


    def _deserialize(self, params):
        self._AdmissionTime = params.get("AdmissionTime")
        self._DischargeTime = params.get("DischargeTime")
        self._AdmissionDays = params.get("AdmissionDays")
        self._AdmissionDignosis = params.get("AdmissionDignosis")
        self._AdmissionCondition = params.get("AdmissionCondition")
        self._DiagnosisTreatment = params.get("DiagnosisTreatment")
        self._DischargeDiagnosis = params.get("DischargeDiagnosis")
        self._DischargeInstruction = params.get("DischargeInstruction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IHCBlock(AbstractModel):
    """IHC块

    """

    def __init__(self):
        r"""
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 具体值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.ValueBlock`
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Index = None
        self._Src = None
        self._Name = None
        self._Value = None
        self._Coords = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Name = params.get("Name")
        if params.get("Value") is not None:
            self._Value = ValueBlock()
            self._Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IHCInfo(AbstractModel):
    """Ihc信息

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
        :type Value: :class:`tencentcloud.mrs.v20200910.models.Value`
        """
        self._Index = None
        self._Src = None
        self._Name = None
        self._Value = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Name = params.get("Name")
        if params.get("Value") is not None:
            self._Value = Value()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IHCV2(AbstractModel):
    """IHC

    """

    def __init__(self):
        r"""
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Name: ihc归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: ihc详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.Value`
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Index = None
        self._Src = None
        self._Name = None
        self._Value = None
        self._Coords = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Name = params.get("Name")
        if params.get("Value") is not None:
            self._Value = Value()
            self._Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片信息

    """

    def __init__(self):
        r"""
        :param _Id: 图片id
        :type Id: int
        :param _Url: 图片url
        :type Url: str
        :param _Base64: 图片base64编码
        :type Base64: str
        """
        self._Id = None
        self._Url = None
        self._Base64 = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Base64(self):
        return self._Base64

    @Base64.setter
    def Base64(self, Base64):
        self._Base64 = Base64


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Base64 = params.get("Base64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToClassRequest(AbstractModel):
    """ImageToClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfoList: 图片列表，允许传入多张图片，支持传入图片的base64编码，暂不支持图片url
        :type ImageInfoList: list of ImageInfo
        :param _HandleParam: 图片处理参数
        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`
        :param _Type: 不填，默认为0
        :type Type: int
        :param _UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        """
        self._ImageInfoList = None
        self._HandleParam = None
        self._Type = None
        self._UserType = None

    @property
    def ImageInfoList(self):
        return self._ImageInfoList

    @ImageInfoList.setter
    def ImageInfoList(self, ImageInfoList):
        self._ImageInfoList = ImageInfoList

    @property
    def HandleParam(self):
        return self._HandleParam

    @HandleParam.setter
    def HandleParam(self, HandleParam):
        self._HandleParam = HandleParam

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self._ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfoList.append(obj)
        if params.get("HandleParam") is not None:
            self._HandleParam = HandleParam()
            self._HandleParam._deserialize(params.get("HandleParam"))
        self._Type = params.get("Type")
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToClassResponse(AbstractModel):
    """ImageToClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextTypeList: 分类结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTypeList: list of TextType
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextTypeList = None
        self._RequestId = None

    @property
    def TextTypeList(self):
        return self._TextTypeList

    @TextTypeList.setter
    def TextTypeList(self, TextTypeList):
        self._TextTypeList = TextTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextTypeList") is not None:
            self._TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self._TextTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class ImageToObjectRequest(AbstractModel):
    """ImageToObject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfoList: 图片列表，允许传入多张图片，目前只支持传入图片base64编码，图片url暂不支持
        :type ImageInfoList: list of ImageInfo
        :param _HandleParam: 图片处理参数
        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`
        :param _Type: 报告类型，目前支持11（检验报告），12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明），363（心电图），27（内窥镜检查），215（处方单），219（免疫接种证明），301（C14呼气试验）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）
        :type Type: int
        :param _IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为 False，则 Type 字段不能为 0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。
        :type IsUsedClassify: bool
        :param _UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        :param _ReportTypeVersion: 可选。用于指定不同报告使用的结构化引擎版本，不同版本返回的JSON 数据结果不兼容。若不指定版本号，就默认用旧的版本号。
（1）检验报告 11，默认使用 V2，最高支持 V3。
（2）病理报告 15，默认使用 V1，最高支持 V2。
（3）入院记录29、出院记录 28、病历记录 216、病程记录 217、门诊记录 210，默认使用 V1，最高支持 V2。
        :type ReportTypeVersion: list of ReportTypeVersion
        """
        self._ImageInfoList = None
        self._HandleParam = None
        self._Type = None
        self._IsUsedClassify = None
        self._UserType = None
        self._ReportTypeVersion = None

    @property
    def ImageInfoList(self):
        return self._ImageInfoList

    @ImageInfoList.setter
    def ImageInfoList(self, ImageInfoList):
        self._ImageInfoList = ImageInfoList

    @property
    def HandleParam(self):
        return self._HandleParam

    @HandleParam.setter
    def HandleParam(self, HandleParam):
        self._HandleParam = HandleParam

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsUsedClassify(self):
        return self._IsUsedClassify

    @IsUsedClassify.setter
    def IsUsedClassify(self, IsUsedClassify):
        self._IsUsedClassify = IsUsedClassify

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def ReportTypeVersion(self):
        return self._ReportTypeVersion

    @ReportTypeVersion.setter
    def ReportTypeVersion(self, ReportTypeVersion):
        self._ReportTypeVersion = ReportTypeVersion


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self._ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfoList.append(obj)
        if params.get("HandleParam") is not None:
            self._HandleParam = HandleParam()
            self._HandleParam._deserialize(params.get("HandleParam"))
        self._Type = params.get("Type")
        self._IsUsedClassify = params.get("IsUsedClassify")
        self._UserType = params.get("UserType")
        if params.get("ReportTypeVersion") is not None:
            self._ReportTypeVersion = []
            for item in params.get("ReportTypeVersion"):
                obj = ReportTypeVersion()
                obj._deserialize(item)
                self._ReportTypeVersion.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToObjectResponse(AbstractModel):
    """ImageToObject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 报告结构化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`
        :param _TextTypeList: 多级分类结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTypeList: list of TextType
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._TextTypeList = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def TextTypeList(self):
        return self._TextTypeList

    @TextTypeList.setter
    def TextTypeList(self, TextTypeList):
        self._TextTypeList = TextTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("TextTypeList") is not None:
            self._TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self._TextTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class ImmunohistochemistryBlock(AbstractModel):
    """免疫组化

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 免疫组化详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of IHCBlock
        """
        self._Name = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = IHCBlock()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Indicator(AbstractModel):
    """检验报告

    """

    def __init__(self):
        r"""
        :param _Indicators: 检验指标项
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicators: list of IndicatorItem
        """
        self._Indicators = None

    @property
    def Indicators(self):
        return self._Indicators

    @Indicators.setter
    def Indicators(self, Indicators):
        self._Indicators = Indicators


    def _deserialize(self, params):
        if params.get("Indicators") is not None:
            self._Indicators = []
            for item in params.get("Indicators"):
                obj = IndicatorItem()
                obj._deserialize(item)
                self._Indicators.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorItem(AbstractModel):
    """检验指标项

    """

    def __init__(self):
        r"""
        :param _Code: 英文缩写
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Scode: 标准缩写
注意：此字段可能返回 null，表示取不到有效值。
        :type Scode: str
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Sname: 标准名
注意：此字段可能返回 null，表示取不到有效值。
        :type Sname: str
        :param _Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        :param _Arrow: 上下箭头
注意：此字段可能返回 null，表示取不到有效值。
        :type Arrow: str
        :param _Normal: 是否正常
注意：此字段可能返回 null，表示取不到有效值。
        :type Normal: bool
        :param _ItemString: 项目原文
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemString: str
        :param _Id: 指标项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Coords: 指标项坐标位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: :class:`tencentcloud.mrs.v20200910.models.Coordinate`
        :param _InferNormal: 推测结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type InferNormal: str
        """
        self._Code = None
        self._Scode = None
        self._Name = None
        self._Sname = None
        self._Result = None
        self._Unit = None
        self._Range = None
        self._Arrow = None
        self._Normal = None
        self._ItemString = None
        self._Id = None
        self._Coords = None
        self._InferNormal = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Scode(self):
        return self._Scode

    @Scode.setter
    def Scode(self, Scode):
        self._Scode = Scode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sname(self):
        return self._Sname

    @Sname.setter
    def Sname(self, Sname):
        self._Sname = Sname

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def Arrow(self):
        return self._Arrow

    @Arrow.setter
    def Arrow(self, Arrow):
        self._Arrow = Arrow

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def ItemString(self):
        return self._ItemString

    @ItemString.setter
    def ItemString(self, ItemString):
        self._ItemString = ItemString

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords

    @property
    def InferNormal(self):
        return self._InferNormal

    @InferNormal.setter
    def InferNormal(self, InferNormal):
        self._InferNormal = InferNormal


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Scode = params.get("Scode")
        self._Name = params.get("Name")
        self._Sname = params.get("Sname")
        self._Result = params.get("Result")
        self._Unit = params.get("Unit")
        self._Range = params.get("Range")
        self._Arrow = params.get("Arrow")
        self._Normal = params.get("Normal")
        self._ItemString = params.get("ItemString")
        self._Id = params.get("Id")
        if params.get("Coords") is not None:
            self._Coords = Coordinate()
            self._Coords._deserialize(params.get("Coords"))
        self._InferNormal = params.get("InferNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorItemV2(AbstractModel):
    """检验指标项结构v2

    """

    def __init__(self):
        r"""
        :param _Item: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Code: 英文编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Arrow: 上下箭头
注意：此字段可能返回 null，表示取不到有效值。
        :type Arrow: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Method: 检测方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param _Normal: 结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Normal: bool
        :param _Id: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Order: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        :param _InferNormal: 推测结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type InferNormal: str
        """
        self._Item = None
        self._Code = None
        self._Result = None
        self._Unit = None
        self._Range = None
        self._Arrow = None
        self._Method = None
        self._Normal = None
        self._Id = None
        self._Order = None
        self._InferNormal = None

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def Arrow(self):
        return self._Arrow

    @Arrow.setter
    def Arrow(self, Arrow):
        self._Arrow = Arrow

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def InferNormal(self):
        return self._InferNormal

    @InferNormal.setter
    def InferNormal(self, InferNormal):
        self._InferNormal = InferNormal


    def _deserialize(self, params):
        if params.get("Item") is not None:
            self._Item = BaseItem()
            self._Item._deserialize(params.get("Item"))
        if params.get("Code") is not None:
            self._Code = BaseItem()
            self._Code._deserialize(params.get("Code"))
        if params.get("Result") is not None:
            self._Result = BaseItem()
            self._Result._deserialize(params.get("Result"))
        if params.get("Unit") is not None:
            self._Unit = BaseItem()
            self._Unit._deserialize(params.get("Unit"))
        if params.get("Range") is not None:
            self._Range = BaseItem()
            self._Range._deserialize(params.get("Range"))
        if params.get("Arrow") is not None:
            self._Arrow = BaseItem()
            self._Arrow._deserialize(params.get("Arrow"))
        if params.get("Method") is not None:
            self._Method = BaseItem()
            self._Method._deserialize(params.get("Method"))
        self._Normal = params.get("Normal")
        self._Id = params.get("Id")
        self._Order = params.get("Order")
        self._InferNormal = params.get("InferNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorV3(AbstractModel):
    """检验报告v3

    """

    def __init__(self):
        r"""
        :param _TableIndictors: 检验报告V3结论
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIndictors: list of TableIndicators
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._TableIndictors = None
        self._Version = None

    @property
    def TableIndictors(self):
        return self._TableIndictors

    @TableIndictors.setter
    def TableIndictors(self, TableIndictors):
        self._TableIndictors = TableIndictors

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        if params.get("TableIndictors") is not None:
            self._TableIndictors = []
            for item in params.get("TableIndictors"):
                obj = TableIndicators()
                obj._deserialize(item)
                self._TableIndictors.append(obj)
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invas(AbstractModel):
    """侵犯扩散

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._Index = None
        self._Part = None
        self._Positive = None
        self._Src = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        self._Index = params.get("Index")
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Positive = params.get("Positive")
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvasiveV2(AbstractModel):
    """侵犯

    """

    def __init__(self):
        r"""
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Positive: 阴性或阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Index = None
        self._Part = None
        self._Positive = None
        self._Src = None
        self._Coords = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Index = params.get("Index")
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Positive = params.get("Positive")
        self._Src = params.get("Src")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueInfo(AbstractModel):
    """签发信息

    """

    def __init__(self):
        r"""
        :param _CertNumber: 编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CertNumber: str
        :param _IssuedAuthority: 签发机构
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuedAuthority: str
        :param _IssuedDate: 签发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuedDate: str
        """
        self._CertNumber = None
        self._IssuedAuthority = None
        self._IssuedDate = None

    @property
    def CertNumber(self):
        return self._CertNumber

    @CertNumber.setter
    def CertNumber(self, CertNumber):
        self._CertNumber = CertNumber

    @property
    def IssuedAuthority(self):
        return self._IssuedAuthority

    @IssuedAuthority.setter
    def IssuedAuthority(self, IssuedAuthority):
        self._IssuedAuthority = IssuedAuthority

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate


    def _deserialize(self, params):
        self._CertNumber = params.get("CertNumber")
        self._IssuedAuthority = params.get("IssuedAuthority")
        self._IssuedDate = params.get("IssuedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LastMenstrualPeriodBlock(AbstractModel):
    """末次月经

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Type = None
        self._Timestamp = None
        self._Unit = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Type = params.get("Type")
        self._Timestamp = params.get("Timestamp")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Lymph(AbstractModel):
    """淋巴

    """

    def __init__(self):
        r"""
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TransferNum: 转移数
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: int
        """
        self._Src = None
        self._Index = None
        self._Part = None
        self._Total = None
        self._TransferNum = None

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TransferNum(self):
        return self._TransferNum

    @TransferNum.setter
    def TransferNum(self, TransferNum):
        self._TransferNum = TransferNum


    def _deserialize(self, params):
        self._Src = params.get("Src")
        self._Index = params.get("Index")
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Total = params.get("Total")
        self._TransferNum = params.get("TransferNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LymphNode(AbstractModel):
    """单淋巴结转移信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TransferNum: 转移数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: int
        :param _Sizes: 淋巴结大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Sizes: list of int
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Index = None
        self._Part = None
        self._Src = None
        self._Total = None
        self._TransferNum = None
        self._Sizes = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TransferNum(self):
        return self._TransferNum

    @TransferNum.setter
    def TransferNum(self, TransferNum):
        self._TransferNum = TransferNum

    @property
    def Sizes(self):
        return self._Sizes

    @Sizes.setter
    def Sizes(self, Sizes):
        self._Sizes = Sizes

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Src = params.get("Src")
        self._Total = params.get("Total")
        self._TransferNum = params.get("TransferNum")
        self._Sizes = params.get("Sizes")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LymphTotal(AbstractModel):
    """淋巴结总计转移信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _TransferNum: 转移数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: str
        :param _Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._TransferNum = None
        self._Total = None
        self._Src = None
        self._Index = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TransferNum(self):
        return self._TransferNum

    @TransferNum.setter
    def TransferNum(self, TransferNum):
        self._TransferNum = TransferNum

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TransferNum = params.get("TransferNum")
        self._Total = params.get("Total")
        self._Src = params.get("Src")
        self._Index = params.get("Index")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainDiseaseHistoryBlock(AbstractModel):
    """既往史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Neglist: 否定列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Neglist: :class:`tencentcloud.mrs.v20200910.models.NeglistBlock`
        :param _Poslist: 肯定列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Poslist: :class:`tencentcloud.mrs.v20200910.models.PoslistBlock`
        """
        self._Name = None
        self._Src = None
        self._State = None
        self._Value = None
        self._Neglist = None
        self._Poslist = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Neglist(self):
        return self._Neglist

    @Neglist.setter
    def Neglist(self, Neglist):
        self._Neglist = Neglist

    @property
    def Poslist(self):
        return self._Poslist

    @Poslist.setter
    def Poslist(self, Poslist):
        self._Poslist = Poslist


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._State = params.get("State")
        self._Value = params.get("Value")
        if params.get("Neglist") is not None:
            self._Neglist = NeglistBlock()
            self._Neglist._deserialize(params.get("Neglist"))
        if params.get("Poslist") is not None:
            self._Poslist = PoslistBlock()
            self._Poslist._deserialize(params.get("Poslist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Maternity(AbstractModel):
    """孕产报告

    """

    def __init__(self):
        r"""
        :param _Desc: 描述部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.MaternityDesc`
        :param _Summary: 结论部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.MaternitySummary`
        :param _OcrText: 报告原文
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrText: str
        """
        self._Desc = None
        self._Summary = None
        self._OcrText = None

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def OcrText(self):
        return self._OcrText

    @OcrText.setter
    def OcrText(self, OcrText):
        self._OcrText = OcrText


    def _deserialize(self, params):
        if params.get("Desc") is not None:
            self._Desc = MaternityDesc()
            self._Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self._Summary = MaternitySummary()
            self._Summary._deserialize(params.get("Summary"))
        self._OcrText = params.get("OcrText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaternityDesc(AbstractModel):
    """孕产描述部分

    """

    def __init__(self):
        r"""
        :param _Fetus: 胎儿数据结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Fetus: list of Fetus
        :param _FetusNum: 胎儿数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FetusNum: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Text: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Fetus = None
        self._FetusNum = None
        self._Text = None
        self._Coords = None

    @property
    def Fetus(self):
        return self._Fetus

    @Fetus.setter
    def Fetus(self, Fetus):
        self._Fetus = Fetus

    @property
    def FetusNum(self):
        return self._FetusNum

    @FetusNum.setter
    def FetusNum(self, FetusNum):
        self._FetusNum = FetusNum

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Fetus") is not None:
            self._Fetus = []
            for item in params.get("Fetus"):
                obj = Fetus()
                obj._deserialize(item)
                self._Fetus.append(obj)
        if params.get("FetusNum") is not None:
            self._FetusNum = FieldInfo()
            self._FetusNum._deserialize(params.get("FetusNum"))
        self._Text = params.get("Text")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaternitySummary(AbstractModel):
    """孕产结论部分

    """

    def __init__(self):
        r"""
        :param _Fetus: 胎儿数据结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Fetus: list of Fetus
        :param _FetusNum: 胎儿数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FetusNum: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param _Sym: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Sym: list of FieldInfo
        :param _Text: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Fetus = None
        self._FetusNum = None
        self._Sym = None
        self._Text = None
        self._Coords = None

    @property
    def Fetus(self):
        return self._Fetus

    @Fetus.setter
    def Fetus(self, Fetus):
        self._Fetus = Fetus

    @property
    def FetusNum(self):
        return self._FetusNum

    @FetusNum.setter
    def FetusNum(self, FetusNum):
        self._FetusNum = FetusNum

    @property
    def Sym(self):
        return self._Sym

    @Sym.setter
    def Sym(self, Sym):
        self._Sym = Sym

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Fetus") is not None:
            self._Fetus = []
            for item in params.get("Fetus"):
                obj = Fetus()
                obj._deserialize(item)
                self._Fetus.append(obj)
        if params.get("FetusNum") is not None:
            self._FetusNum = FieldInfo()
            self._FetusNum._deserialize(params.get("FetusNum"))
        if params.get("Sym") is not None:
            self._Sym = []
            for item in params.get("Sym"):
                obj = FieldInfo()
                obj._deserialize(item)
                self._Sym.append(obj)
        self._Text = params.get("Text")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedDoc(AbstractModel):
    """医学资料

    """

    def __init__(self):
        r"""
        :param _Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`
        :param _Diagnosis: 诊断结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnosis: list of DiagCertItem
        :param _DiseaseMedicalHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseMedicalHistory`
        :param _PersonalMedicalHistory: 个人史
        :type PersonalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalMedicalHistory`
        :param _ObstericalMedicalHistory: 婚孕史
        :type ObstericalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.ObstericalMedicalHistory`
        :param _FamilyMedicalHistory: 家族史
        :type FamilyMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyMedicalHistory`
        :param _MenstrualMedicalHistory: 月经史
        :type MenstrualMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualMedicalHistory`
        :param _TreatmentRecord: 诊疗记录
        :type TreatmentRecord: :class:`tencentcloud.mrs.v20200910.models.TreatmentRecord`
        """
        self._Advice = None
        self._Diagnosis = None
        self._DiseaseMedicalHistory = None
        self._PersonalMedicalHistory = None
        self._ObstericalMedicalHistory = None
        self._FamilyMedicalHistory = None
        self._MenstrualMedicalHistory = None
        self._TreatmentRecord = None

    @property
    def Advice(self):
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def Diagnosis(self):
        return self._Diagnosis

    @Diagnosis.setter
    def Diagnosis(self, Diagnosis):
        self._Diagnosis = Diagnosis

    @property
    def DiseaseMedicalHistory(self):
        return self._DiseaseMedicalHistory

    @DiseaseMedicalHistory.setter
    def DiseaseMedicalHistory(self, DiseaseMedicalHistory):
        self._DiseaseMedicalHistory = DiseaseMedicalHistory

    @property
    def PersonalMedicalHistory(self):
        return self._PersonalMedicalHistory

    @PersonalMedicalHistory.setter
    def PersonalMedicalHistory(self, PersonalMedicalHistory):
        self._PersonalMedicalHistory = PersonalMedicalHistory

    @property
    def ObstericalMedicalHistory(self):
        return self._ObstericalMedicalHistory

    @ObstericalMedicalHistory.setter
    def ObstericalMedicalHistory(self, ObstericalMedicalHistory):
        self._ObstericalMedicalHistory = ObstericalMedicalHistory

    @property
    def FamilyMedicalHistory(self):
        return self._FamilyMedicalHistory

    @FamilyMedicalHistory.setter
    def FamilyMedicalHistory(self, FamilyMedicalHistory):
        self._FamilyMedicalHistory = FamilyMedicalHistory

    @property
    def MenstrualMedicalHistory(self):
        return self._MenstrualMedicalHistory

    @MenstrualMedicalHistory.setter
    def MenstrualMedicalHistory(self, MenstrualMedicalHistory):
        self._MenstrualMedicalHistory = MenstrualMedicalHistory

    @property
    def TreatmentRecord(self):
        return self._TreatmentRecord

    @TreatmentRecord.setter
    def TreatmentRecord(self, TreatmentRecord):
        self._TreatmentRecord = TreatmentRecord


    def _deserialize(self, params):
        if params.get("Advice") is not None:
            self._Advice = Advice()
            self._Advice._deserialize(params.get("Advice"))
        if params.get("Diagnosis") is not None:
            self._Diagnosis = []
            for item in params.get("Diagnosis"):
                obj = DiagCertItem()
                obj._deserialize(item)
                self._Diagnosis.append(obj)
        if params.get("DiseaseMedicalHistory") is not None:
            self._DiseaseMedicalHistory = DiseaseMedicalHistory()
            self._DiseaseMedicalHistory._deserialize(params.get("DiseaseMedicalHistory"))
        if params.get("PersonalMedicalHistory") is not None:
            self._PersonalMedicalHistory = PersonalMedicalHistory()
            self._PersonalMedicalHistory._deserialize(params.get("PersonalMedicalHistory"))
        if params.get("ObstericalMedicalHistory") is not None:
            self._ObstericalMedicalHistory = ObstericalMedicalHistory()
            self._ObstericalMedicalHistory._deserialize(params.get("ObstericalMedicalHistory"))
        if params.get("FamilyMedicalHistory") is not None:
            self._FamilyMedicalHistory = FamilyMedicalHistory()
            self._FamilyMedicalHistory._deserialize(params.get("FamilyMedicalHistory"))
        if params.get("MenstrualMedicalHistory") is not None:
            self._MenstrualMedicalHistory = MenstrualMedicalHistory()
            self._MenstrualMedicalHistory._deserialize(params.get("MenstrualMedicalHistory"))
        if params.get("TreatmentRecord") is not None:
            self._TreatmentRecord = TreatmentRecord()
            self._TreatmentRecord._deserialize(params.get("TreatmentRecord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedicalRecordInfo(AbstractModel):
    """门诊病历信息

    """

    def __init__(self):
        r"""
        :param _DiagnosisTime: 就诊日期
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisTime: str
        :param _DiagnosisDepartmentName: 就诊科室
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisDepartmentName: str
        :param _DiagnosisDoctorName: 就诊医生
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisDoctorName: str
        :param _ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type ClinicalDiagnosis: str
        :param _MainNarration: 主述
注意：此字段可能返回 null，表示取不到有效值。
        :type MainNarration: str
        :param _PhysicalExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalExamination: str
        :param _InspectionFindings: 检查结论
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectionFindings: str
        :param _TreatmentOpinion: 治疗意见
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentOpinion: str
        """
        self._DiagnosisTime = None
        self._DiagnosisDepartmentName = None
        self._DiagnosisDoctorName = None
        self._ClinicalDiagnosis = None
        self._MainNarration = None
        self._PhysicalExamination = None
        self._InspectionFindings = None
        self._TreatmentOpinion = None

    @property
    def DiagnosisTime(self):
        return self._DiagnosisTime

    @DiagnosisTime.setter
    def DiagnosisTime(self, DiagnosisTime):
        self._DiagnosisTime = DiagnosisTime

    @property
    def DiagnosisDepartmentName(self):
        return self._DiagnosisDepartmentName

    @DiagnosisDepartmentName.setter
    def DiagnosisDepartmentName(self, DiagnosisDepartmentName):
        self._DiagnosisDepartmentName = DiagnosisDepartmentName

    @property
    def DiagnosisDoctorName(self):
        return self._DiagnosisDoctorName

    @DiagnosisDoctorName.setter
    def DiagnosisDoctorName(self, DiagnosisDoctorName):
        self._DiagnosisDoctorName = DiagnosisDoctorName

    @property
    def ClinicalDiagnosis(self):
        return self._ClinicalDiagnosis

    @ClinicalDiagnosis.setter
    def ClinicalDiagnosis(self, ClinicalDiagnosis):
        self._ClinicalDiagnosis = ClinicalDiagnosis

    @property
    def MainNarration(self):
        return self._MainNarration

    @MainNarration.setter
    def MainNarration(self, MainNarration):
        self._MainNarration = MainNarration

    @property
    def PhysicalExamination(self):
        return self._PhysicalExamination

    @PhysicalExamination.setter
    def PhysicalExamination(self, PhysicalExamination):
        self._PhysicalExamination = PhysicalExamination

    @property
    def InspectionFindings(self):
        return self._InspectionFindings

    @InspectionFindings.setter
    def InspectionFindings(self, InspectionFindings):
        self._InspectionFindings = InspectionFindings

    @property
    def TreatmentOpinion(self):
        return self._TreatmentOpinion

    @TreatmentOpinion.setter
    def TreatmentOpinion(self, TreatmentOpinion):
        self._TreatmentOpinion = TreatmentOpinion


    def _deserialize(self, params):
        self._DiagnosisTime = params.get("DiagnosisTime")
        self._DiagnosisDepartmentName = params.get("DiagnosisDepartmentName")
        self._DiagnosisDoctorName = params.get("DiagnosisDoctorName")
        self._ClinicalDiagnosis = params.get("ClinicalDiagnosis")
        self._MainNarration = params.get("MainNarration")
        self._PhysicalExamination = params.get("PhysicalExamination")
        self._InspectionFindings = params.get("InspectionFindings")
        self._TreatmentOpinion = params.get("TreatmentOpinion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Medicine(AbstractModel):
    """药品

    """

    def __init__(self):
        r"""
        :param _Name: 药品名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _TradeName: 商品名
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeName: str
        :param _Firm: 厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Firm: str
        :param _Category: 医保类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param _Specification: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param _MinQuantity: 最小包装数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinQuantity: str
        :param _DosageUnit: 最小制剂单位
注意：此字段可能返回 null，表示取不到有效值。
        :type DosageUnit: str
        :param _PackingUnit: 最小包装单位
注意：此字段可能返回 null，表示取不到有效值。
        :type PackingUnit: str
        """
        self._Name = None
        self._TradeName = None
        self._Firm = None
        self._Category = None
        self._Specification = None
        self._MinQuantity = None
        self._DosageUnit = None
        self._PackingUnit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TradeName(self):
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def Firm(self):
        return self._Firm

    @Firm.setter
    def Firm(self, Firm):
        self._Firm = Firm

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def MinQuantity(self):
        return self._MinQuantity

    @MinQuantity.setter
    def MinQuantity(self, MinQuantity):
        self._MinQuantity = MinQuantity

    @property
    def DosageUnit(self):
        return self._DosageUnit

    @DosageUnit.setter
    def DosageUnit(self, DosageUnit):
        self._DosageUnit = DosageUnit

    @property
    def PackingUnit(self):
        return self._PackingUnit

    @PackingUnit.setter
    def PackingUnit(self, PackingUnit):
        self._PackingUnit = PackingUnit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TradeName = params.get("TradeName")
        self._Firm = params.get("Firm")
        self._Category = params.get("Category")
        self._Specification = params.get("Specification")
        self._MinQuantity = params.get("MinQuantity")
        self._DosageUnit = params.get("DosageUnit")
        self._PackingUnit = params.get("PackingUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualFlowBlock(AbstractModel):
    """月经量

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualHistoryBlock(AbstractModel):
    """月经史

    """

    def __init__(self):
        r"""
        :param _LastMenstrualPeriod: 末次月经
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMenstrualPeriod: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param _MenstrualFlow: 月经量
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualFlow: :class:`tencentcloud.mrs.v20200910.models.MenstrualFlowBlock`
        :param _MenarcheAge: 初潮时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MenarcheAge: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param _MenstruationOrNot: 是否绝经
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruationOrNot: :class:`tencentcloud.mrs.v20200910.models.MenstruationOrNotBlock`
        :param _MenstrualCycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualCycles: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param _MenstrualPeriod: 月经经期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualPeriod: :class:`tencentcloud.mrs.v20200910.models.MenstrualPeriodBlock`
        """
        self._LastMenstrualPeriod = None
        self._MenstrualFlow = None
        self._MenarcheAge = None
        self._MenstruationOrNot = None
        self._MenstrualCycles = None
        self._MenstrualPeriod = None

    @property
    def LastMenstrualPeriod(self):
        return self._LastMenstrualPeriod

    @LastMenstrualPeriod.setter
    def LastMenstrualPeriod(self, LastMenstrualPeriod):
        self._LastMenstrualPeriod = LastMenstrualPeriod

    @property
    def MenstrualFlow(self):
        return self._MenstrualFlow

    @MenstrualFlow.setter
    def MenstrualFlow(self, MenstrualFlow):
        self._MenstrualFlow = MenstrualFlow

    @property
    def MenarcheAge(self):
        return self._MenarcheAge

    @MenarcheAge.setter
    def MenarcheAge(self, MenarcheAge):
        self._MenarcheAge = MenarcheAge

    @property
    def MenstruationOrNot(self):
        return self._MenstruationOrNot

    @MenstruationOrNot.setter
    def MenstruationOrNot(self, MenstruationOrNot):
        self._MenstruationOrNot = MenstruationOrNot

    @property
    def MenstrualCycles(self):
        return self._MenstrualCycles

    @MenstrualCycles.setter
    def MenstrualCycles(self, MenstrualCycles):
        self._MenstrualCycles = MenstrualCycles

    @property
    def MenstrualPeriod(self):
        return self._MenstrualPeriod

    @MenstrualPeriod.setter
    def MenstrualPeriod(self, MenstrualPeriod):
        self._MenstrualPeriod = MenstrualPeriod


    def _deserialize(self, params):
        if params.get("LastMenstrualPeriod") is not None:
            self._LastMenstrualPeriod = LastMenstrualPeriodBlock()
            self._LastMenstrualPeriod._deserialize(params.get("LastMenstrualPeriod"))
        if params.get("MenstrualFlow") is not None:
            self._MenstrualFlow = MenstrualFlowBlock()
            self._MenstrualFlow._deserialize(params.get("MenstrualFlow"))
        if params.get("MenarcheAge") is not None:
            self._MenarcheAge = LastMenstrualPeriodBlock()
            self._MenarcheAge._deserialize(params.get("MenarcheAge"))
        if params.get("MenstruationOrNot") is not None:
            self._MenstruationOrNot = MenstruationOrNotBlock()
            self._MenstruationOrNot._deserialize(params.get("MenstruationOrNot"))
        if params.get("MenstrualCycles") is not None:
            self._MenstrualCycles = LastMenstrualPeriodBlock()
            self._MenstrualCycles._deserialize(params.get("MenstrualCycles"))
        if params.get("MenstrualPeriod") is not None:
            self._MenstrualPeriod = MenstrualPeriodBlock()
            self._MenstrualPeriod._deserialize(params.get("MenstrualPeriod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualHistoryDetailBlock(AbstractModel):
    """月经史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._State = None
        self._Norm = None
        self._TimeType = None
        self._Timestamp = None
        self._Unit = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._State = params.get("State")
        self._Norm = params.get("Norm")
        self._TimeType = params.get("TimeType")
        self._Timestamp = params.get("Timestamp")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualMedicalHistory(AbstractModel):
    """月经史

    """

    def __init__(self):
        r"""
        :param _LastMenstrualPeriod: 末次月经时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMenstrualPeriod: str
        :param _MenstrualFlow: 经量
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualFlow: str
        :param _MenarcheAge: 月经初潮年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type MenarcheAge: str
        :param _MenstruationOrNot: 是否来月经
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruationOrNot: str
        :param _MenstrualCycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualCycles: str
        :param _MenstrualPeriod: 月经持续天数
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualPeriod: str
        """
        self._LastMenstrualPeriod = None
        self._MenstrualFlow = None
        self._MenarcheAge = None
        self._MenstruationOrNot = None
        self._MenstrualCycles = None
        self._MenstrualPeriod = None

    @property
    def LastMenstrualPeriod(self):
        return self._LastMenstrualPeriod

    @LastMenstrualPeriod.setter
    def LastMenstrualPeriod(self, LastMenstrualPeriod):
        self._LastMenstrualPeriod = LastMenstrualPeriod

    @property
    def MenstrualFlow(self):
        return self._MenstrualFlow

    @MenstrualFlow.setter
    def MenstrualFlow(self, MenstrualFlow):
        self._MenstrualFlow = MenstrualFlow

    @property
    def MenarcheAge(self):
        return self._MenarcheAge

    @MenarcheAge.setter
    def MenarcheAge(self, MenarcheAge):
        self._MenarcheAge = MenarcheAge

    @property
    def MenstruationOrNot(self):
        return self._MenstruationOrNot

    @MenstruationOrNot.setter
    def MenstruationOrNot(self, MenstruationOrNot):
        self._MenstruationOrNot = MenstruationOrNot

    @property
    def MenstrualCycles(self):
        return self._MenstrualCycles

    @MenstrualCycles.setter
    def MenstrualCycles(self, MenstrualCycles):
        self._MenstrualCycles = MenstrualCycles

    @property
    def MenstrualPeriod(self):
        return self._MenstrualPeriod

    @MenstrualPeriod.setter
    def MenstrualPeriod(self, MenstrualPeriod):
        self._MenstrualPeriod = MenstrualPeriod


    def _deserialize(self, params):
        self._LastMenstrualPeriod = params.get("LastMenstrualPeriod")
        self._MenstrualFlow = params.get("MenstrualFlow")
        self._MenarcheAge = params.get("MenarcheAge")
        self._MenstruationOrNot = params.get("MenstruationOrNot")
        self._MenstrualCycles = params.get("MenstrualCycles")
        self._MenstrualPeriod = params.get("MenstrualPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualPeriodBlock(AbstractModel):
    """月经经期

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._Type = None
        self._Timestamp = None
        self._Unit = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._Type = params.get("Type")
        self._Timestamp = params.get("Timestamp")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstruationOrNotBlock(AbstractModel):
    """是否绝经

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Norm = None
        self._TimeType = None
        self._Timestamp = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Norm = params.get("Norm")
        self._TimeType = params.get("TimeType")
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Molecular(AbstractModel):
    """分子病理

    """

    def __init__(self):
        r"""
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Name: 基因名称标注化
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 分子病理详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.MolecularValue`
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Index = None
        self._Src = None
        self._Name = None
        self._Value = None
        self._Coords = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Name = params.get("Name")
        if params.get("Value") is not None:
            self._Value = MolecularValue()
            self._Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MolecularValue(AbstractModel):
    """分子病理详细信息

    """

    def __init__(self):
        r"""
        :param _Exon: 外显子
注意：此字段可能返回 null，表示取不到有效值。
        :type Exon: str
        :param _Position: 点位
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Positive: 阳性或阴性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param _Src: 基因名称原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self._Exon = None
        self._Position = None
        self._Type = None
        self._Positive = None
        self._Src = None

    @property
    def Exon(self):
        return self._Exon

    @Exon.setter
    def Exon(self, Exon):
        self._Exon = Exon

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src


    def _deserialize(self, params):
        self._Exon = params.get("Exon")
        self._Position = params.get("Position")
        self._Type = params.get("Type")
        self._Positive = params.get("Positive")
        self._Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Multiple(AbstractModel):
    """多发

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Count: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Index = None
        self._Src = None
        self._Value = None
        self._Count = None
        self._Name = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Count = params.get("Count")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NeglistBlock(AbstractModel):
    """否定列表

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NeonatalInfo(AbstractModel):
    """新生儿信息

    """

    def __init__(self):
        r"""
        :param _NeonatalName: 新生儿名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalName: str
        :param _NeonatalGender: 新生儿性别
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalGender: str
        :param _BirthLength: 出生身长
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthLength: str
        :param _BirthWeight: 出生体重
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthWeight: str
        :param _GestationalAge: 出生孕周
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationalAge: str
        :param _BirthTime: 出生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthTime: str
        :param _BirthPlace: 出生地点
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param _MedicalInstitutions: 医疗机构
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInstitutions: str
        """
        self._NeonatalName = None
        self._NeonatalGender = None
        self._BirthLength = None
        self._BirthWeight = None
        self._GestationalAge = None
        self._BirthTime = None
        self._BirthPlace = None
        self._MedicalInstitutions = None

    @property
    def NeonatalName(self):
        return self._NeonatalName

    @NeonatalName.setter
    def NeonatalName(self, NeonatalName):
        self._NeonatalName = NeonatalName

    @property
    def NeonatalGender(self):
        return self._NeonatalGender

    @NeonatalGender.setter
    def NeonatalGender(self, NeonatalGender):
        self._NeonatalGender = NeonatalGender

    @property
    def BirthLength(self):
        return self._BirthLength

    @BirthLength.setter
    def BirthLength(self, BirthLength):
        self._BirthLength = BirthLength

    @property
    def BirthWeight(self):
        return self._BirthWeight

    @BirthWeight.setter
    def BirthWeight(self, BirthWeight):
        self._BirthWeight = BirthWeight

    @property
    def GestationalAge(self):
        return self._GestationalAge

    @GestationalAge.setter
    def GestationalAge(self, GestationalAge):
        self._GestationalAge = GestationalAge

    @property
    def BirthTime(self):
        return self._BirthTime

    @BirthTime.setter
    def BirthTime(self, BirthTime):
        self._BirthTime = BirthTime

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def MedicalInstitutions(self):
        return self._MedicalInstitutions

    @MedicalInstitutions.setter
    def MedicalInstitutions(self, MedicalInstitutions):
        self._MedicalInstitutions = MedicalInstitutions


    def _deserialize(self, params):
        self._NeonatalName = params.get("NeonatalName")
        self._NeonatalGender = params.get("NeonatalGender")
        self._BirthLength = params.get("BirthLength")
        self._BirthWeight = params.get("BirthWeight")
        self._GestationalAge = params.get("GestationalAge")
        self._BirthTime = params.get("BirthTime")
        self._BirthPlace = params.get("BirthPlace")
        self._MedicalInstitutions = params.get("MedicalInstitutions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormPart(AbstractModel):
    """标准部位

    """

    def __init__(self):
        r"""
        :param _Part: 部位值
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param _PartDirection: 部位方向
注意：此字段可能返回 null，表示取不到有效值。
        :type PartDirection: str
        :param _Tissue: 组织值
注意：此字段可能返回 null，表示取不到有效值。
        :type Tissue: str
        :param _TissueDirection: 组织方向
注意：此字段可能返回 null，表示取不到有效值。
        :type TissueDirection: str
        :param _Upper: 上级部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Upper: str
        :param _PartDetail: 部位详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PartDetail: :class:`tencentcloud.mrs.v20200910.models.PartDesc`
        """
        self._Part = None
        self._PartDirection = None
        self._Tissue = None
        self._TissueDirection = None
        self._Upper = None
        self._PartDetail = None

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def PartDirection(self):
        return self._PartDirection

    @PartDirection.setter
    def PartDirection(self, PartDirection):
        self._PartDirection = PartDirection

    @property
    def Tissue(self):
        return self._Tissue

    @Tissue.setter
    def Tissue(self, Tissue):
        self._Tissue = Tissue

    @property
    def TissueDirection(self):
        return self._TissueDirection

    @TissueDirection.setter
    def TissueDirection(self, TissueDirection):
        self._TissueDirection = TissueDirection

    @property
    def Upper(self):
        return self._Upper

    @Upper.setter
    def Upper(self, Upper):
        self._Upper = Upper

    @property
    def PartDetail(self):
        return self._PartDetail

    @PartDetail.setter
    def PartDetail(self, PartDetail):
        self._PartDetail = PartDetail


    def _deserialize(self, params):
        self._Part = params.get("Part")
        self._PartDirection = params.get("PartDirection")
        self._Tissue = params.get("Tissue")
        self._TissueDirection = params.get("TissueDirection")
        self._Upper = params.get("Upper")
        if params.get("PartDetail") is not None:
            self._PartDetail = PartDesc()
            self._PartDetail._deserialize(params.get("PartDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormSize(AbstractModel):
    """大小

    """

    def __init__(self):
        r"""
        :param _Number: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: list of str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Impl: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Impl: str
        """
        self._Number = None
        self._Type = None
        self._Unit = None
        self._Impl = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Impl(self):
        return self._Impl

    @Impl.setter
    def Impl(self, Impl):
        self._Impl = Impl


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._Type = params.get("Type")
        self._Unit = params.get("Unit")
        self._Impl = params.get("Impl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumValue(AbstractModel):
    """数值结构体

    """

    def __init__(self):
        r"""
        :param _Num: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Num: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
        self._Num = None
        self._Unit = None

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObstericalMedicalHistory(AbstractModel):
    """孕产史

    """

    def __init__(self):
        r"""
        :param _MarriageHistory: 婚史
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriageHistory: str
        :param _FertilityHistory: 孕史
注意：此字段可能返回 null，表示取不到有效值。
        :type FertilityHistory: str
        """
        self._MarriageHistory = None
        self._FertilityHistory = None

    @property
    def MarriageHistory(self):
        return self._MarriageHistory

    @MarriageHistory.setter
    def MarriageHistory(self, MarriageHistory):
        self._MarriageHistory = MarriageHistory

    @property
    def FertilityHistory(self):
        return self._FertilityHistory

    @FertilityHistory.setter
    def FertilityHistory(self, FertilityHistory):
        self._FertilityHistory = FertilityHistory


    def _deserialize(self, params):
        self._MarriageHistory = params.get("MarriageHistory")
        self._FertilityHistory = params.get("FertilityHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObstetricalHistoryBlock(AbstractModel):
    """婚姻-生育史

    """

    def __init__(self):
        r"""
        :param _MarriageHistory: 婚姻史
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriageHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualHistoryDetailBlock`
        :param _FertilityHistory: 婚育史
注意：此字段可能返回 null，表示取不到有效值。
        :type FertilityHistory: :class:`tencentcloud.mrs.v20200910.models.FertilityHistoryBlock`
        """
        self._MarriageHistory = None
        self._FertilityHistory = None

    @property
    def MarriageHistory(self):
        return self._MarriageHistory

    @MarriageHistory.setter
    def MarriageHistory(self, MarriageHistory):
        self._MarriageHistory = MarriageHistory

    @property
    def FertilityHistory(self):
        return self._FertilityHistory

    @FertilityHistory.setter
    def FertilityHistory(self, FertilityHistory):
        self._FertilityHistory = FertilityHistory


    def _deserialize(self, params):
        if params.get("MarriageHistory") is not None:
            self._MarriageHistory = MenstrualHistoryDetailBlock()
            self._MarriageHistory._deserialize(params.get("MarriageHistory"))
        if params.get("FertilityHistory") is not None:
            self._FertilityHistory = FertilityHistoryBlock()
            self._FertilityHistory._deserialize(params.get("FertilityHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Organ(AbstractModel):
    """器官

    """

    def __init__(self):
        r"""
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        :param _Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。
        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Gland: 腺体
注意：此字段可能返回 null，表示取不到有效值。
        :type Gland: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。
        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Thickness: 厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type Thickness: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。
        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _SymDesc: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDesc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。
        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Density: 密度
注意：此字段可能返回 null，表示取不到有效值。
        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。
        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。
        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`
        :param _InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Transparent: 透声度
注意：此字段可能返回 null，表示取不到有效值。
        :type Transparent: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriAdc: MRI ADC
注意：此字段可能返回 null，表示取不到有效值。
        :type MriAdc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriDwi: MRI DWI
注意：此字段可能返回 null，表示取不到有效值。
        :type MriDwi: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriT1: MRI T1信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT1: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriT2: MRI T2信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT2: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _CtHu: CT HU值
注意：此字段可能返回 null，表示取不到有效值。
        :type CtHu: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Suvmax: SUmax值
注意：此字段可能返回 null，表示取不到有效值。
        :type Suvmax: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Metabolism: 代谢情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Metabolism: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _RadioactiveUptake: 放射性摄取
注意：此字段可能返回 null，表示取不到有效值。
        :type RadioactiveUptake: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _LymphEnlargement: 淋巴结情况
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphEnlargement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ImageFeature: 影像特征
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageFeature: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Duct: 导管
注意：此字段可能返回 null，表示取不到有效值。
        :type Duct: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Trend: 趋势
注意：此字段可能返回 null，表示取不到有效值。
        :type Trend: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Operation: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Coords: 器官在报告图片中的坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Part = None
        self._Size = None
        self._Envelope = None
        self._Edge = None
        self._InnerEcho = None
        self._Gland = None
        self._Shape = None
        self._Thickness = None
        self._ShapeAttr = None
        self._CDFI = None
        self._SymDesc = None
        self._SizeStatus = None
        self._Outline = None
        self._Structure = None
        self._Density = None
        self._Vas = None
        self._Cysticwall = None
        self._Capsule = None
        self._IsthmusThicknese = None
        self._InnerEchoDistribution = None
        self._Src = None
        self._Index = None
        self._Transparent = None
        self._MriAdc = None
        self._MriDwi = None
        self._MriT1 = None
        self._MriT2 = None
        self._CtHu = None
        self._Suvmax = None
        self._Metabolism = None
        self._RadioactiveUptake = None
        self._LymphEnlargement = None
        self._ImageFeature = None
        self._Duct = None
        self._Trend = None
        self._Operation = None
        self._Coords = None

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Envelope(self):
        return self._Envelope

    @Envelope.setter
    def Envelope(self, Envelope):
        self._Envelope = Envelope

    @property
    def Edge(self):
        return self._Edge

    @Edge.setter
    def Edge(self, Edge):
        self._Edge = Edge

    @property
    def InnerEcho(self):
        return self._InnerEcho

    @InnerEcho.setter
    def InnerEcho(self, InnerEcho):
        self._InnerEcho = InnerEcho

    @property
    def Gland(self):
        return self._Gland

    @Gland.setter
    def Gland(self, Gland):
        self._Gland = Gland

    @property
    def Shape(self):
        return self._Shape

    @Shape.setter
    def Shape(self, Shape):
        self._Shape = Shape

    @property
    def Thickness(self):
        return self._Thickness

    @Thickness.setter
    def Thickness(self, Thickness):
        self._Thickness = Thickness

    @property
    def ShapeAttr(self):
        return self._ShapeAttr

    @ShapeAttr.setter
    def ShapeAttr(self, ShapeAttr):
        self._ShapeAttr = ShapeAttr

    @property
    def CDFI(self):
        return self._CDFI

    @CDFI.setter
    def CDFI(self, CDFI):
        self._CDFI = CDFI

    @property
    def SymDesc(self):
        return self._SymDesc

    @SymDesc.setter
    def SymDesc(self, SymDesc):
        self._SymDesc = SymDesc

    @property
    def SizeStatus(self):
        return self._SizeStatus

    @SizeStatus.setter
    def SizeStatus(self, SizeStatus):
        self._SizeStatus = SizeStatus

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Structure(self):
        return self._Structure

    @Structure.setter
    def Structure(self, Structure):
        self._Structure = Structure

    @property
    def Density(self):
        return self._Density

    @Density.setter
    def Density(self, Density):
        self._Density = Density

    @property
    def Vas(self):
        return self._Vas

    @Vas.setter
    def Vas(self, Vas):
        self._Vas = Vas

    @property
    def Cysticwall(self):
        return self._Cysticwall

    @Cysticwall.setter
    def Cysticwall(self, Cysticwall):
        self._Cysticwall = Cysticwall

    @property
    def Capsule(self):
        return self._Capsule

    @Capsule.setter
    def Capsule(self, Capsule):
        self._Capsule = Capsule

    @property
    def IsthmusThicknese(self):
        return self._IsthmusThicknese

    @IsthmusThicknese.setter
    def IsthmusThicknese(self, IsthmusThicknese):
        self._IsthmusThicknese = IsthmusThicknese

    @property
    def InnerEchoDistribution(self):
        return self._InnerEchoDistribution

    @InnerEchoDistribution.setter
    def InnerEchoDistribution(self, InnerEchoDistribution):
        self._InnerEchoDistribution = InnerEchoDistribution

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Transparent(self):
        return self._Transparent

    @Transparent.setter
    def Transparent(self, Transparent):
        self._Transparent = Transparent

    @property
    def MriAdc(self):
        return self._MriAdc

    @MriAdc.setter
    def MriAdc(self, MriAdc):
        self._MriAdc = MriAdc

    @property
    def MriDwi(self):
        return self._MriDwi

    @MriDwi.setter
    def MriDwi(self, MriDwi):
        self._MriDwi = MriDwi

    @property
    def MriT1(self):
        return self._MriT1

    @MriT1.setter
    def MriT1(self, MriT1):
        self._MriT1 = MriT1

    @property
    def MriT2(self):
        return self._MriT2

    @MriT2.setter
    def MriT2(self, MriT2):
        self._MriT2 = MriT2

    @property
    def CtHu(self):
        return self._CtHu

    @CtHu.setter
    def CtHu(self, CtHu):
        self._CtHu = CtHu

    @property
    def Suvmax(self):
        return self._Suvmax

    @Suvmax.setter
    def Suvmax(self, Suvmax):
        self._Suvmax = Suvmax

    @property
    def Metabolism(self):
        return self._Metabolism

    @Metabolism.setter
    def Metabolism(self, Metabolism):
        self._Metabolism = Metabolism

    @property
    def RadioactiveUptake(self):
        return self._RadioactiveUptake

    @RadioactiveUptake.setter
    def RadioactiveUptake(self, RadioactiveUptake):
        self._RadioactiveUptake = RadioactiveUptake

    @property
    def LymphEnlargement(self):
        return self._LymphEnlargement

    @LymphEnlargement.setter
    def LymphEnlargement(self, LymphEnlargement):
        self._LymphEnlargement = LymphEnlargement

    @property
    def ImageFeature(self):
        return self._ImageFeature

    @ImageFeature.setter
    def ImageFeature(self, ImageFeature):
        self._ImageFeature = ImageFeature

    @property
    def Duct(self):
        return self._Duct

    @Duct.setter
    def Duct(self, Duct):
        self._Duct = Duct

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        if params.get("Size") is not None:
            self._Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self._Size.append(obj)
        if params.get("Envelope") is not None:
            self._Envelope = BlockInfo()
            self._Envelope._deserialize(params.get("Envelope"))
        if params.get("Edge") is not None:
            self._Edge = BlockInfo()
            self._Edge._deserialize(params.get("Edge"))
        if params.get("InnerEcho") is not None:
            self._InnerEcho = BlockInfo()
            self._InnerEcho._deserialize(params.get("InnerEcho"))
        if params.get("Gland") is not None:
            self._Gland = BlockInfo()
            self._Gland._deserialize(params.get("Gland"))
        if params.get("Shape") is not None:
            self._Shape = BlockInfo()
            self._Shape._deserialize(params.get("Shape"))
        if params.get("Thickness") is not None:
            self._Thickness = BlockInfo()
            self._Thickness._deserialize(params.get("Thickness"))
        if params.get("ShapeAttr") is not None:
            self._ShapeAttr = BlockInfo()
            self._ShapeAttr._deserialize(params.get("ShapeAttr"))
        if params.get("CDFI") is not None:
            self._CDFI = BlockInfo()
            self._CDFI._deserialize(params.get("CDFI"))
        if params.get("SymDesc") is not None:
            self._SymDesc = BlockInfo()
            self._SymDesc._deserialize(params.get("SymDesc"))
        if params.get("SizeStatus") is not None:
            self._SizeStatus = BlockInfo()
            self._SizeStatus._deserialize(params.get("SizeStatus"))
        if params.get("Outline") is not None:
            self._Outline = BlockInfo()
            self._Outline._deserialize(params.get("Outline"))
        if params.get("Structure") is not None:
            self._Structure = BlockInfo()
            self._Structure._deserialize(params.get("Structure"))
        if params.get("Density") is not None:
            self._Density = BlockInfo()
            self._Density._deserialize(params.get("Density"))
        if params.get("Vas") is not None:
            self._Vas = BlockInfo()
            self._Vas._deserialize(params.get("Vas"))
        if params.get("Cysticwall") is not None:
            self._Cysticwall = BlockInfo()
            self._Cysticwall._deserialize(params.get("Cysticwall"))
        if params.get("Capsule") is not None:
            self._Capsule = BlockInfo()
            self._Capsule._deserialize(params.get("Capsule"))
        if params.get("IsthmusThicknese") is not None:
            self._IsthmusThicknese = Size()
            self._IsthmusThicknese._deserialize(params.get("IsthmusThicknese"))
        if params.get("InnerEchoDistribution") is not None:
            self._InnerEchoDistribution = BlockInfo()
            self._InnerEchoDistribution._deserialize(params.get("InnerEchoDistribution"))
        self._Src = params.get("Src")
        self._Index = params.get("Index")
        if params.get("Transparent") is not None:
            self._Transparent = BlockInfo()
            self._Transparent._deserialize(params.get("Transparent"))
        if params.get("MriAdc") is not None:
            self._MriAdc = BlockInfo()
            self._MriAdc._deserialize(params.get("MriAdc"))
        if params.get("MriDwi") is not None:
            self._MriDwi = BlockInfo()
            self._MriDwi._deserialize(params.get("MriDwi"))
        if params.get("MriT1") is not None:
            self._MriT1 = BlockInfo()
            self._MriT1._deserialize(params.get("MriT1"))
        if params.get("MriT2") is not None:
            self._MriT2 = BlockInfo()
            self._MriT2._deserialize(params.get("MriT2"))
        if params.get("CtHu") is not None:
            self._CtHu = BlockInfo()
            self._CtHu._deserialize(params.get("CtHu"))
        if params.get("Suvmax") is not None:
            self._Suvmax = BlockInfo()
            self._Suvmax._deserialize(params.get("Suvmax"))
        if params.get("Metabolism") is not None:
            self._Metabolism = BlockInfo()
            self._Metabolism._deserialize(params.get("Metabolism"))
        if params.get("RadioactiveUptake") is not None:
            self._RadioactiveUptake = BlockInfo()
            self._RadioactiveUptake._deserialize(params.get("RadioactiveUptake"))
        if params.get("LymphEnlargement") is not None:
            self._LymphEnlargement = BlockInfo()
            self._LymphEnlargement._deserialize(params.get("LymphEnlargement"))
        if params.get("ImageFeature") is not None:
            self._ImageFeature = BlockInfo()
            self._ImageFeature._deserialize(params.get("ImageFeature"))
        if params.get("Duct") is not None:
            self._Duct = BlockInfo()
            self._Duct._deserialize(params.get("Duct"))
        if params.get("Trend") is not None:
            self._Trend = BlockInfo()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Operation") is not None:
            self._Operation = BlockInfo()
            self._Operation._deserialize(params.get("Operation"))
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInfo(AbstractModel):
    """其他信息

    """

    def __init__(self):
        r"""
        :param _Anesthesia: 麻醉方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Anesthesia: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _BloodLoss: 术中出血
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodLoss: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _BloodTransfusion: 输血
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodTransfusion: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _Duration: 手术用时
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _EndTime: 手术开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _StartTime: 手术结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        """
        self._Anesthesia = None
        self._BloodLoss = None
        self._BloodTransfusion = None
        self._Duration = None
        self._EndTime = None
        self._StartTime = None

    @property
    def Anesthesia(self):
        return self._Anesthesia

    @Anesthesia.setter
    def Anesthesia(self, Anesthesia):
        self._Anesthesia = Anesthesia

    @property
    def BloodLoss(self):
        return self._BloodLoss

    @BloodLoss.setter
    def BloodLoss(self, BloodLoss):
        self._BloodLoss = BloodLoss

    @property
    def BloodTransfusion(self):
        return self._BloodTransfusion

    @BloodTransfusion.setter
    def BloodTransfusion(self, BloodTransfusion):
        self._BloodTransfusion = BloodTransfusion

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        if params.get("Anesthesia") is not None:
            self._Anesthesia = SurgeryAttr()
            self._Anesthesia._deserialize(params.get("Anesthesia"))
        if params.get("BloodLoss") is not None:
            self._BloodLoss = SurgeryAttr()
            self._BloodLoss._deserialize(params.get("BloodLoss"))
        if params.get("BloodTransfusion") is not None:
            self._BloodTransfusion = SurgeryAttr()
            self._BloodTransfusion._deserialize(params.get("BloodTransfusion"))
        if params.get("Duration") is not None:
            self._Duration = SurgeryAttr()
            self._Duration._deserialize(params.get("Duration"))
        if params.get("EndTime") is not None:
            self._EndTime = SurgeryAttr()
            self._EndTime._deserialize(params.get("EndTime"))
        if params.get("StartTime") is not None:
            self._StartTime = SurgeryAttr()
            self._StartTime._deserialize(params.get("StartTime"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PTNM(AbstractModel):
    """pTNM

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _PT: pT
注意：此字段可能返回 null，表示取不到有效值。
        :type PT: str
        :param _PN: pN
注意：此字段可能返回 null，表示取不到有效值。
        :type PN: str
        :param _PM: pM
注意：此字段可能返回 null，表示取不到有效值。
        :type PM: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Index = None
        self._Src = None
        self._Value = None
        self._PT = None
        self._PN = None
        self._PM = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def PT(self):
        return self._PT

    @PT.setter
    def PT(self, PT):
        self._PT = PT

    @property
    def PN(self):
        return self._PN

    @PN.setter
    def PN(self, PN):
        self._PN = PN

    @property
    def PM(self):
        return self._PM

    @PM.setter
    def PM(self, PM):
        self._PM = PM

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._PT = params.get("PT")
        self._PN = params.get("PN")
        self._PM = params.get("PM")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PTNMBlock(AbstractModel):
    """PTNM分期

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _PTNMM: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMM: str
        :param _PTNMN: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMN: str
        :param _PTNMT: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMT: str
        """
        self._Name = None
        self._Src = None
        self._PTNMM = None
        self._PTNMN = None
        self._PTNMT = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def PTNMM(self):
        return self._PTNMM

    @PTNMM.setter
    def PTNMM(self, PTNMM):
        self._PTNMM = PTNMM

    @property
    def PTNMN(self):
        return self._PTNMN

    @PTNMN.setter
    def PTNMN(self, PTNMN):
        self._PTNMN = PTNMN

    @property
    def PTNMT(self):
        return self._PTNMT

    @PTNMT.setter
    def PTNMT(self, PTNMT):
        self._PTNMT = PTNMT


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._PTNMM = params.get("PTNMM")
        self._PTNMN = params.get("PTNMN")
        self._PTNMT = params.get("PTNMT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParagraphBlock(AbstractModel):
    """文本块

    """

    def __init__(self):
        r"""
        :param _IncisionHealingText: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingText: str
        :param _AuxiliaryExaminationText: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExaminationText: str
        :param _SpecialExamText: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialExamText: str
        :param _OutpatientDiagnosisText: 门诊诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientDiagnosisText: str
        :param _AdmissionConditionText: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionConditionText: str
        :param _CheckAndTreatmentProcessText: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcessText: str
        :param _SymptomsAndSignsText: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSignsText: str
        :param _DischargeInstructionsText: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructionsText: str
        :param _AdmissionDiagnosisText: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosisText: str
        :param _SurgeryConditionText: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryConditionText: str
        :param _PathologicalDiagnosisText: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosisText: str
        :param _DischargeConditionText: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeConditionText: str
        :param _CheckRecordText: 检查记录

注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecordText: str
        :param _ChiefComplaintText: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaintText: str
        :param _DischargeDiagnosisText: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosisText: str
        :param _MainDiseaseHistoryText: 既往史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistoryText: str
        :param _DiseasePresentText: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresentText: str
        :param _PersonalHistoryText: 个人史
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalHistoryText: str
        :param _MenstruallHistoryText: 月经史
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruallHistoryText: str
        :param _ObstericalHistoryText: 婚育史
注意：此字段可能返回 null，表示取不到有效值。
        :type ObstericalHistoryText: str
        :param _FamilyHistoryText: 家族史
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyHistoryText: str
        :param _AllergyHistoryText: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistoryText: str
        :param _DiseaseHistoryText: 病史信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseHistoryText: str
        :param _OtherDiagnosisText: 其它诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherDiagnosisText: str
        :param _BodyExaminationText: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExaminationText: str
        :param _SpecialistExaminationText: 专科检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExaminationText: str
        :param _TreatmentResultText: 治疗结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentResultText: str
        """
        self._IncisionHealingText = None
        self._AuxiliaryExaminationText = None
        self._SpecialExamText = None
        self._OutpatientDiagnosisText = None
        self._AdmissionConditionText = None
        self._CheckAndTreatmentProcessText = None
        self._SymptomsAndSignsText = None
        self._DischargeInstructionsText = None
        self._AdmissionDiagnosisText = None
        self._SurgeryConditionText = None
        self._PathologicalDiagnosisText = None
        self._DischargeConditionText = None
        self._CheckRecordText = None
        self._ChiefComplaintText = None
        self._DischargeDiagnosisText = None
        self._MainDiseaseHistoryText = None
        self._DiseasePresentText = None
        self._PersonalHistoryText = None
        self._MenstruallHistoryText = None
        self._ObstericalHistoryText = None
        self._FamilyHistoryText = None
        self._AllergyHistoryText = None
        self._DiseaseHistoryText = None
        self._OtherDiagnosisText = None
        self._BodyExaminationText = None
        self._SpecialistExaminationText = None
        self._TreatmentResultText = None

    @property
    def IncisionHealingText(self):
        return self._IncisionHealingText

    @IncisionHealingText.setter
    def IncisionHealingText(self, IncisionHealingText):
        self._IncisionHealingText = IncisionHealingText

    @property
    def AuxiliaryExaminationText(self):
        return self._AuxiliaryExaminationText

    @AuxiliaryExaminationText.setter
    def AuxiliaryExaminationText(self, AuxiliaryExaminationText):
        self._AuxiliaryExaminationText = AuxiliaryExaminationText

    @property
    def SpecialExamText(self):
        return self._SpecialExamText

    @SpecialExamText.setter
    def SpecialExamText(self, SpecialExamText):
        self._SpecialExamText = SpecialExamText

    @property
    def OutpatientDiagnosisText(self):
        return self._OutpatientDiagnosisText

    @OutpatientDiagnosisText.setter
    def OutpatientDiagnosisText(self, OutpatientDiagnosisText):
        self._OutpatientDiagnosisText = OutpatientDiagnosisText

    @property
    def AdmissionConditionText(self):
        return self._AdmissionConditionText

    @AdmissionConditionText.setter
    def AdmissionConditionText(self, AdmissionConditionText):
        self._AdmissionConditionText = AdmissionConditionText

    @property
    def CheckAndTreatmentProcessText(self):
        return self._CheckAndTreatmentProcessText

    @CheckAndTreatmentProcessText.setter
    def CheckAndTreatmentProcessText(self, CheckAndTreatmentProcessText):
        self._CheckAndTreatmentProcessText = CheckAndTreatmentProcessText

    @property
    def SymptomsAndSignsText(self):
        return self._SymptomsAndSignsText

    @SymptomsAndSignsText.setter
    def SymptomsAndSignsText(self, SymptomsAndSignsText):
        self._SymptomsAndSignsText = SymptomsAndSignsText

    @property
    def DischargeInstructionsText(self):
        return self._DischargeInstructionsText

    @DischargeInstructionsText.setter
    def DischargeInstructionsText(self, DischargeInstructionsText):
        self._DischargeInstructionsText = DischargeInstructionsText

    @property
    def AdmissionDiagnosisText(self):
        return self._AdmissionDiagnosisText

    @AdmissionDiagnosisText.setter
    def AdmissionDiagnosisText(self, AdmissionDiagnosisText):
        self._AdmissionDiagnosisText = AdmissionDiagnosisText

    @property
    def SurgeryConditionText(self):
        return self._SurgeryConditionText

    @SurgeryConditionText.setter
    def SurgeryConditionText(self, SurgeryConditionText):
        self._SurgeryConditionText = SurgeryConditionText

    @property
    def PathologicalDiagnosisText(self):
        return self._PathologicalDiagnosisText

    @PathologicalDiagnosisText.setter
    def PathologicalDiagnosisText(self, PathologicalDiagnosisText):
        self._PathologicalDiagnosisText = PathologicalDiagnosisText

    @property
    def DischargeConditionText(self):
        return self._DischargeConditionText

    @DischargeConditionText.setter
    def DischargeConditionText(self, DischargeConditionText):
        self._DischargeConditionText = DischargeConditionText

    @property
    def CheckRecordText(self):
        return self._CheckRecordText

    @CheckRecordText.setter
    def CheckRecordText(self, CheckRecordText):
        self._CheckRecordText = CheckRecordText

    @property
    def ChiefComplaintText(self):
        return self._ChiefComplaintText

    @ChiefComplaintText.setter
    def ChiefComplaintText(self, ChiefComplaintText):
        self._ChiefComplaintText = ChiefComplaintText

    @property
    def DischargeDiagnosisText(self):
        return self._DischargeDiagnosisText

    @DischargeDiagnosisText.setter
    def DischargeDiagnosisText(self, DischargeDiagnosisText):
        self._DischargeDiagnosisText = DischargeDiagnosisText

    @property
    def MainDiseaseHistoryText(self):
        return self._MainDiseaseHistoryText

    @MainDiseaseHistoryText.setter
    def MainDiseaseHistoryText(self, MainDiseaseHistoryText):
        self._MainDiseaseHistoryText = MainDiseaseHistoryText

    @property
    def DiseasePresentText(self):
        return self._DiseasePresentText

    @DiseasePresentText.setter
    def DiseasePresentText(self, DiseasePresentText):
        self._DiseasePresentText = DiseasePresentText

    @property
    def PersonalHistoryText(self):
        return self._PersonalHistoryText

    @PersonalHistoryText.setter
    def PersonalHistoryText(self, PersonalHistoryText):
        self._PersonalHistoryText = PersonalHistoryText

    @property
    def MenstruallHistoryText(self):
        return self._MenstruallHistoryText

    @MenstruallHistoryText.setter
    def MenstruallHistoryText(self, MenstruallHistoryText):
        self._MenstruallHistoryText = MenstruallHistoryText

    @property
    def ObstericalHistoryText(self):
        return self._ObstericalHistoryText

    @ObstericalHistoryText.setter
    def ObstericalHistoryText(self, ObstericalHistoryText):
        self._ObstericalHistoryText = ObstericalHistoryText

    @property
    def FamilyHistoryText(self):
        return self._FamilyHistoryText

    @FamilyHistoryText.setter
    def FamilyHistoryText(self, FamilyHistoryText):
        self._FamilyHistoryText = FamilyHistoryText

    @property
    def AllergyHistoryText(self):
        return self._AllergyHistoryText

    @AllergyHistoryText.setter
    def AllergyHistoryText(self, AllergyHistoryText):
        self._AllergyHistoryText = AllergyHistoryText

    @property
    def DiseaseHistoryText(self):
        return self._DiseaseHistoryText

    @DiseaseHistoryText.setter
    def DiseaseHistoryText(self, DiseaseHistoryText):
        self._DiseaseHistoryText = DiseaseHistoryText

    @property
    def OtherDiagnosisText(self):
        return self._OtherDiagnosisText

    @OtherDiagnosisText.setter
    def OtherDiagnosisText(self, OtherDiagnosisText):
        self._OtherDiagnosisText = OtherDiagnosisText

    @property
    def BodyExaminationText(self):
        return self._BodyExaminationText

    @BodyExaminationText.setter
    def BodyExaminationText(self, BodyExaminationText):
        self._BodyExaminationText = BodyExaminationText

    @property
    def SpecialistExaminationText(self):
        return self._SpecialistExaminationText

    @SpecialistExaminationText.setter
    def SpecialistExaminationText(self, SpecialistExaminationText):
        self._SpecialistExaminationText = SpecialistExaminationText

    @property
    def TreatmentResultText(self):
        return self._TreatmentResultText

    @TreatmentResultText.setter
    def TreatmentResultText(self, TreatmentResultText):
        self._TreatmentResultText = TreatmentResultText


    def _deserialize(self, params):
        self._IncisionHealingText = params.get("IncisionHealingText")
        self._AuxiliaryExaminationText = params.get("AuxiliaryExaminationText")
        self._SpecialExamText = params.get("SpecialExamText")
        self._OutpatientDiagnosisText = params.get("OutpatientDiagnosisText")
        self._AdmissionConditionText = params.get("AdmissionConditionText")
        self._CheckAndTreatmentProcessText = params.get("CheckAndTreatmentProcessText")
        self._SymptomsAndSignsText = params.get("SymptomsAndSignsText")
        self._DischargeInstructionsText = params.get("DischargeInstructionsText")
        self._AdmissionDiagnosisText = params.get("AdmissionDiagnosisText")
        self._SurgeryConditionText = params.get("SurgeryConditionText")
        self._PathologicalDiagnosisText = params.get("PathologicalDiagnosisText")
        self._DischargeConditionText = params.get("DischargeConditionText")
        self._CheckRecordText = params.get("CheckRecordText")
        self._ChiefComplaintText = params.get("ChiefComplaintText")
        self._DischargeDiagnosisText = params.get("DischargeDiagnosisText")
        self._MainDiseaseHistoryText = params.get("MainDiseaseHistoryText")
        self._DiseasePresentText = params.get("DiseasePresentText")
        self._PersonalHistoryText = params.get("PersonalHistoryText")
        self._MenstruallHistoryText = params.get("MenstruallHistoryText")
        self._ObstericalHistoryText = params.get("ObstericalHistoryText")
        self._FamilyHistoryText = params.get("FamilyHistoryText")
        self._AllergyHistoryText = params.get("AllergyHistoryText")
        self._DiseaseHistoryText = params.get("DiseaseHistoryText")
        self._OtherDiagnosisText = params.get("OtherDiagnosisText")
        self._BodyExaminationText = params.get("BodyExaminationText")
        self._SpecialistExaminationText = params.get("SpecialistExaminationText")
        self._TreatmentResultText = params.get("TreatmentResultText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParentInfo(AbstractModel):
    """母亲或父亲信息

    """

    def __init__(self):
        r"""
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Age: 年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: str
        :param _IdCard: 证件号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param _Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Ethnicity: str
        :param _Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param _Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        """
        self._Name = None
        self._Age = None
        self._IdCard = None
        self._Ethnicity = None
        self._Nationality = None
        self._Address = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Ethnicity(self):
        return self._Ethnicity

    @Ethnicity.setter
    def Ethnicity(self, Ethnicity):
        self._Ethnicity = Ethnicity

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Age = params.get("Age")
        self._IdCard = params.get("IdCard")
        self._Ethnicity = params.get("Ethnicity")
        self._Nationality = params.get("Nationality")
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Part(AbstractModel):
    """部位信息

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _NormPart: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type NormPart: :class:`tencentcloud.mrs.v20200910.models.NormPart`
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ValueBrief: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueBrief: str
        """
        self._Index = None
        self._NormPart = None
        self._Src = None
        self._Value = None
        self._Name = None
        self._ValueBrief = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def NormPart(self):
        return self._NormPart

    @NormPart.setter
    def NormPart(self, NormPart):
        self._NormPart = NormPart

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ValueBrief(self):
        return self._ValueBrief

    @ValueBrief.setter
    def ValueBrief(self, ValueBrief):
        self._ValueBrief = ValueBrief


    def _deserialize(self, params):
        self._Index = params.get("Index")
        if params.get("NormPart") is not None:
            self._NormPart = NormPart()
            self._NormPart._deserialize(params.get("NormPart"))
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        self._ValueBrief = params.get("ValueBrief")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartDesc(AbstractModel):
    """部位描述

    """

    def __init__(self):
        r"""
        :param _MainDir: 主要部位
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDir: str
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param _SecondaryDir: 次要部位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryDir: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._MainDir = None
        self._Part = None
        self._SecondaryDir = None
        self._Type = None

    @property
    def MainDir(self):
        return self._MainDir

    @MainDir.setter
    def MainDir(self, MainDir):
        self._MainDir = MainDir

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def SecondaryDir(self):
        return self._SecondaryDir

    @SecondaryDir.setter
    def SecondaryDir(self, SecondaryDir):
        self._SecondaryDir = SecondaryDir

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._MainDir = params.get("MainDir")
        self._Part = params.get("Part")
        self._SecondaryDir = params.get("SecondaryDir")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologicalDiagnosisBlock(AbstractModel):
    """病理诊断

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Detail: 病理详细
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of PathologicalDiagnosisDetailBlock
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._Detail = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = PathologicalDiagnosisDetailBlock()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologicalDiagnosisDetailBlock(AbstractModel):
    """病理详细

    """

    def __init__(self):
        r"""
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param _HistologicalType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologicalType: str
        :param _HistologicalGrade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologicalGrade: str
        """
        self._Part = None
        self._HistologicalType = None
        self._HistologicalGrade = None

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def HistologicalType(self):
        return self._HistologicalType

    @HistologicalType.setter
    def HistologicalType(self, HistologicalType):
        self._HistologicalType = HistologicalType

    @property
    def HistologicalGrade(self):
        return self._HistologicalGrade

    @HistologicalGrade.setter
    def HistologicalGrade(self, HistologicalGrade):
        self._HistologicalGrade = HistologicalGrade


    def _deserialize(self, params):
        self._Part = params.get("Part")
        self._HistologicalType = params.get("HistologicalType")
        self._HistologicalGrade = params.get("HistologicalGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologyReport(AbstractModel):
    """病理报告

    """

    def __init__(self):
        r"""
        :param _CancerPart: 癌症部位
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerPart: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _CancerSize: 癌症部位大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerSize: list of Size
        :param _DescText: 描述文本
注意：此字段可能返回 null，表示取不到有效值。
        :type DescText: str
        :param _HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyLevel: :class:`tencentcloud.mrs.v20200910.models.HistologyLevel`
        :param _HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyType: :class:`tencentcloud.mrs.v20200910.models.HistologyType`
        :param _IHC: IHC信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IHC: list of IHCInfo
        :param _InfiltrationDepth: 浸润深度
注意：此字段可能返回 null，表示取不到有效值。
        :type InfiltrationDepth: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Invasive: 肿瘤扩散
注意：此字段可能返回 null，表示取不到有效值。
        :type Invasive: list of Invas
        :param _LymphNodes: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphNodes: list of Lymph
        :param _PTNM: PTNM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _PathologicalReportType: 病理报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalReportType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ReportText: 报告原文
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportText: str
        :param _SampleType: 标本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _SummaryText: 结论文本
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryText: str
        """
        self._CancerPart = None
        self._CancerSize = None
        self._DescText = None
        self._HistologyLevel = None
        self._HistologyType = None
        self._IHC = None
        self._InfiltrationDepth = None
        self._Invasive = None
        self._LymphNodes = None
        self._PTNM = None
        self._PathologicalReportType = None
        self._ReportText = None
        self._SampleType = None
        self._SummaryText = None

    @property
    def CancerPart(self):
        return self._CancerPart

    @CancerPart.setter
    def CancerPart(self, CancerPart):
        self._CancerPart = CancerPart

    @property
    def CancerSize(self):
        return self._CancerSize

    @CancerSize.setter
    def CancerSize(self, CancerSize):
        self._CancerSize = CancerSize

    @property
    def DescText(self):
        return self._DescText

    @DescText.setter
    def DescText(self, DescText):
        self._DescText = DescText

    @property
    def HistologyLevel(self):
        return self._HistologyLevel

    @HistologyLevel.setter
    def HistologyLevel(self, HistologyLevel):
        self._HistologyLevel = HistologyLevel

    @property
    def HistologyType(self):
        return self._HistologyType

    @HistologyType.setter
    def HistologyType(self, HistologyType):
        self._HistologyType = HistologyType

    @property
    def IHC(self):
        return self._IHC

    @IHC.setter
    def IHC(self, IHC):
        self._IHC = IHC

    @property
    def InfiltrationDepth(self):
        return self._InfiltrationDepth

    @InfiltrationDepth.setter
    def InfiltrationDepth(self, InfiltrationDepth):
        self._InfiltrationDepth = InfiltrationDepth

    @property
    def Invasive(self):
        return self._Invasive

    @Invasive.setter
    def Invasive(self, Invasive):
        self._Invasive = Invasive

    @property
    def LymphNodes(self):
        return self._LymphNodes

    @LymphNodes.setter
    def LymphNodes(self, LymphNodes):
        self._LymphNodes = LymphNodes

    @property
    def PTNM(self):
        return self._PTNM

    @PTNM.setter
    def PTNM(self, PTNM):
        self._PTNM = PTNM

    @property
    def PathologicalReportType(self):
        return self._PathologicalReportType

    @PathologicalReportType.setter
    def PathologicalReportType(self, PathologicalReportType):
        self._PathologicalReportType = PathologicalReportType

    @property
    def ReportText(self):
        return self._ReportText

    @ReportText.setter
    def ReportText(self, ReportText):
        self._ReportText = ReportText

    @property
    def SampleType(self):
        return self._SampleType

    @SampleType.setter
    def SampleType(self, SampleType):
        self._SampleType = SampleType

    @property
    def SummaryText(self):
        return self._SummaryText

    @SummaryText.setter
    def SummaryText(self, SummaryText):
        self._SummaryText = SummaryText


    def _deserialize(self, params):
        if params.get("CancerPart") is not None:
            self._CancerPart = Part()
            self._CancerPart._deserialize(params.get("CancerPart"))
        if params.get("CancerSize") is not None:
            self._CancerSize = []
            for item in params.get("CancerSize"):
                obj = Size()
                obj._deserialize(item)
                self._CancerSize.append(obj)
        self._DescText = params.get("DescText")
        if params.get("HistologyLevel") is not None:
            self._HistologyLevel = HistologyLevel()
            self._HistologyLevel._deserialize(params.get("HistologyLevel"))
        if params.get("HistologyType") is not None:
            self._HistologyType = HistologyType()
            self._HistologyType._deserialize(params.get("HistologyType"))
        if params.get("IHC") is not None:
            self._IHC = []
            for item in params.get("IHC"):
                obj = IHCInfo()
                obj._deserialize(item)
                self._IHC.append(obj)
        if params.get("InfiltrationDepth") is not None:
            self._InfiltrationDepth = BlockInfo()
            self._InfiltrationDepth._deserialize(params.get("InfiltrationDepth"))
        if params.get("Invasive") is not None:
            self._Invasive = []
            for item in params.get("Invasive"):
                obj = Invas()
                obj._deserialize(item)
                self._Invasive.append(obj)
        if params.get("LymphNodes") is not None:
            self._LymphNodes = []
            for item in params.get("LymphNodes"):
                obj = Lymph()
                obj._deserialize(item)
                self._LymphNodes.append(obj)
        if params.get("PTNM") is not None:
            self._PTNM = BlockInfo()
            self._PTNM._deserialize(params.get("PTNM"))
        if params.get("PathologicalReportType") is not None:
            self._PathologicalReportType = BlockInfo()
            self._PathologicalReportType._deserialize(params.get("PathologicalReportType"))
        self._ReportText = params.get("ReportText")
        if params.get("SampleType") is not None:
            self._SampleType = BlockInfo()
            self._SampleType._deserialize(params.get("SampleType"))
        self._SummaryText = params.get("SummaryText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologyV2(AbstractModel):
    """病理报告v2

    """

    def __init__(self):
        r"""
        :param _PathologicalReportType: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalReportType: :class:`tencentcloud.mrs.v20200910.models.Report`
        :param _Desc: 描述段落
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.DescInfo`
        :param _Summary: 诊断结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.SummaryInfo`
        :param _ReportText: 报告全文
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportText: str
        :param _LymphTotal: 淋巴结总计转移信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphTotal: list of LymphTotal
        :param _LymphNodes: 单淋巴结转移信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphNodes: list of LymphNode
        :param _Ihc: ihc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Ihc: list of IHCV2
        :param _Clinical: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Clinical: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Precancer: 是否癌前病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Precancer: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param _Malignant: 是否恶性肿瘤
注意：此字段可能返回 null，表示取不到有效值。
        :type Malignant: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param _Benigntumor: 是否良性肿瘤
注意：此字段可能返回 null，表示取不到有效值。
        :type Benigntumor: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param _SampleType: 送检材料
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _LymphSize: 淋巴结大小
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphSize: list of Size
        :param _Molecular: 分子病理
注意：此字段可能返回 null，表示取不到有效值。
        :type Molecular: list of Molecular
        """
        self._PathologicalReportType = None
        self._Desc = None
        self._Summary = None
        self._ReportText = None
        self._LymphTotal = None
        self._LymphNodes = None
        self._Ihc = None
        self._Clinical = None
        self._Precancer = None
        self._Malignant = None
        self._Benigntumor = None
        self._SampleType = None
        self._LymphSize = None
        self._Molecular = None

    @property
    def PathologicalReportType(self):
        return self._PathologicalReportType

    @PathologicalReportType.setter
    def PathologicalReportType(self, PathologicalReportType):
        self._PathologicalReportType = PathologicalReportType

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def ReportText(self):
        return self._ReportText

    @ReportText.setter
    def ReportText(self, ReportText):
        self._ReportText = ReportText

    @property
    def LymphTotal(self):
        return self._LymphTotal

    @LymphTotal.setter
    def LymphTotal(self, LymphTotal):
        self._LymphTotal = LymphTotal

    @property
    def LymphNodes(self):
        return self._LymphNodes

    @LymphNodes.setter
    def LymphNodes(self, LymphNodes):
        self._LymphNodes = LymphNodes

    @property
    def Ihc(self):
        return self._Ihc

    @Ihc.setter
    def Ihc(self, Ihc):
        self._Ihc = Ihc

    @property
    def Clinical(self):
        return self._Clinical

    @Clinical.setter
    def Clinical(self, Clinical):
        self._Clinical = Clinical

    @property
    def Precancer(self):
        return self._Precancer

    @Precancer.setter
    def Precancer(self, Precancer):
        self._Precancer = Precancer

    @property
    def Malignant(self):
        return self._Malignant

    @Malignant.setter
    def Malignant(self, Malignant):
        self._Malignant = Malignant

    @property
    def Benigntumor(self):
        return self._Benigntumor

    @Benigntumor.setter
    def Benigntumor(self, Benigntumor):
        self._Benigntumor = Benigntumor

    @property
    def SampleType(self):
        return self._SampleType

    @SampleType.setter
    def SampleType(self, SampleType):
        self._SampleType = SampleType

    @property
    def LymphSize(self):
        return self._LymphSize

    @LymphSize.setter
    def LymphSize(self, LymphSize):
        self._LymphSize = LymphSize

    @property
    def Molecular(self):
        return self._Molecular

    @Molecular.setter
    def Molecular(self, Molecular):
        self._Molecular = Molecular


    def _deserialize(self, params):
        if params.get("PathologicalReportType") is not None:
            self._PathologicalReportType = Report()
            self._PathologicalReportType._deserialize(params.get("PathologicalReportType"))
        if params.get("Desc") is not None:
            self._Desc = DescInfo()
            self._Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self._Summary = SummaryInfo()
            self._Summary._deserialize(params.get("Summary"))
        self._ReportText = params.get("ReportText")
        if params.get("LymphTotal") is not None:
            self._LymphTotal = []
            for item in params.get("LymphTotal"):
                obj = LymphTotal()
                obj._deserialize(item)
                self._LymphTotal.append(obj)
        if params.get("LymphNodes") is not None:
            self._LymphNodes = []
            for item in params.get("LymphNodes"):
                obj = LymphNode()
                obj._deserialize(item)
                self._LymphNodes.append(obj)
        if params.get("Ihc") is not None:
            self._Ihc = []
            for item in params.get("Ihc"):
                obj = IHCV2()
                obj._deserialize(item)
                self._Ihc.append(obj)
        if params.get("Clinical") is not None:
            self._Clinical = BaseInfo()
            self._Clinical._deserialize(params.get("Clinical"))
        if params.get("Precancer") is not None:
            self._Precancer = HistologyClass()
            self._Precancer._deserialize(params.get("Precancer"))
        if params.get("Malignant") is not None:
            self._Malignant = HistologyClass()
            self._Malignant._deserialize(params.get("Malignant"))
        if params.get("Benigntumor") is not None:
            self._Benigntumor = HistologyClass()
            self._Benigntumor._deserialize(params.get("Benigntumor"))
        if params.get("SampleType") is not None:
            self._SampleType = BaseInfo()
            self._SampleType._deserialize(params.get("SampleType"))
        if params.get("LymphSize") is not None:
            self._LymphSize = []
            for item in params.get("LymphSize"):
                obj = Size()
                obj._deserialize(item)
                self._LymphSize.append(obj)
        if params.get("Molecular") is not None:
            self._Molecular = []
            for item in params.get("Molecular"):
                obj = Molecular()
                obj._deserialize(item)
                self._Molecular.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PatientInfo(AbstractModel):
    """患者信息

    """

    def __init__(self):
        r"""
        :param _Name: 患者姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Sex: 患者性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param _Age: 患者年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: str
        :param _Phone: 患者手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Address: 患者地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _IdCard: 患者身份证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param _HealthCardNo: 健康卡号
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCardNo: str
        :param _SocialSecurityCardNo: 社保卡号
注意：此字段可能返回 null，表示取不到有效值。
        :type SocialSecurityCardNo: str
        :param _Birthday: 出生日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthday: str
        :param _Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Ethnicity: str
        :param _Married: 婚姻状况
注意：此字段可能返回 null，表示取不到有效值。
        :type Married: str
        :param _Profession: 职业
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param _EducationBackground: 教育程度
注意：此字段可能返回 null，表示取不到有效值。
        :type EducationBackground: str
        :param _Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param _BirthPlace: 籍贯
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param _MedicalInsuranceType: 医保类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInsuranceType: str
        :param _AgeNorm: 标准化年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type AgeNorm: str
        :param _Nation: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param _MarriedCode: 婚姻代码
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriedCode: str
        :param _ProfessionCode: 职业代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfessionCode: str
        :param _MedicalInsuranceTypeCode: 居民医保代码
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInsuranceTypeCode: str
        :param _BedNo: 床号
注意：此字段可能返回 null，表示取不到有效值。
        :type BedNo: str
        """
        self._Name = None
        self._Sex = None
        self._Age = None
        self._Phone = None
        self._Address = None
        self._IdCard = None
        self._HealthCardNo = None
        self._SocialSecurityCardNo = None
        self._Birthday = None
        self._Ethnicity = None
        self._Married = None
        self._Profession = None
        self._EducationBackground = None
        self._Nationality = None
        self._BirthPlace = None
        self._MedicalInsuranceType = None
        self._AgeNorm = None
        self._Nation = None
        self._MarriedCode = None
        self._ProfessionCode = None
        self._MedicalInsuranceTypeCode = None
        self._BedNo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def HealthCardNo(self):
        return self._HealthCardNo

    @HealthCardNo.setter
    def HealthCardNo(self, HealthCardNo):
        self._HealthCardNo = HealthCardNo

    @property
    def SocialSecurityCardNo(self):
        return self._SocialSecurityCardNo

    @SocialSecurityCardNo.setter
    def SocialSecurityCardNo(self, SocialSecurityCardNo):
        self._SocialSecurityCardNo = SocialSecurityCardNo

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Ethnicity(self):
        return self._Ethnicity

    @Ethnicity.setter
    def Ethnicity(self, Ethnicity):
        self._Ethnicity = Ethnicity

    @property
    def Married(self):
        return self._Married

    @Married.setter
    def Married(self, Married):
        self._Married = Married

    @property
    def Profession(self):
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def EducationBackground(self):
        return self._EducationBackground

    @EducationBackground.setter
    def EducationBackground(self, EducationBackground):
        self._EducationBackground = EducationBackground

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def MedicalInsuranceType(self):
        return self._MedicalInsuranceType

    @MedicalInsuranceType.setter
    def MedicalInsuranceType(self, MedicalInsuranceType):
        self._MedicalInsuranceType = MedicalInsuranceType

    @property
    def AgeNorm(self):
        return self._AgeNorm

    @AgeNorm.setter
    def AgeNorm(self, AgeNorm):
        self._AgeNorm = AgeNorm

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def MarriedCode(self):
        return self._MarriedCode

    @MarriedCode.setter
    def MarriedCode(self, MarriedCode):
        self._MarriedCode = MarriedCode

    @property
    def ProfessionCode(self):
        return self._ProfessionCode

    @ProfessionCode.setter
    def ProfessionCode(self, ProfessionCode):
        self._ProfessionCode = ProfessionCode

    @property
    def MedicalInsuranceTypeCode(self):
        return self._MedicalInsuranceTypeCode

    @MedicalInsuranceTypeCode.setter
    def MedicalInsuranceTypeCode(self, MedicalInsuranceTypeCode):
        self._MedicalInsuranceTypeCode = MedicalInsuranceTypeCode

    @property
    def BedNo(self):
        return self._BedNo

    @BedNo.setter
    def BedNo(self, BedNo):
        self._BedNo = BedNo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Age = params.get("Age")
        self._Phone = params.get("Phone")
        self._Address = params.get("Address")
        self._IdCard = params.get("IdCard")
        self._HealthCardNo = params.get("HealthCardNo")
        self._SocialSecurityCardNo = params.get("SocialSecurityCardNo")
        self._Birthday = params.get("Birthday")
        self._Ethnicity = params.get("Ethnicity")
        self._Married = params.get("Married")
        self._Profession = params.get("Profession")
        self._EducationBackground = params.get("EducationBackground")
        self._Nationality = params.get("Nationality")
        self._BirthPlace = params.get("BirthPlace")
        self._MedicalInsuranceType = params.get("MedicalInsuranceType")
        self._AgeNorm = params.get("AgeNorm")
        self._Nation = params.get("Nation")
        self._MarriedCode = params.get("MarriedCode")
        self._ProfessionCode = params.get("ProfessionCode")
        self._MedicalInsuranceTypeCode = params.get("MedicalInsuranceTypeCode")
        self._BedNo = params.get("BedNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalHistoryBlock(AbstractModel):
    """个人史

    """

    def __init__(self):
        r"""
        :param _BirthPlace: 出生地
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param _LivePlace: 居住地
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePlace: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param _Job: 职业
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param _SmokeHistory: 吸烟
注意：此字段可能返回 null，表示取不到有效值。
        :type SmokeHistory: :class:`tencentcloud.mrs.v20200910.models.SmokeHistoryBlock`
        :param _AlcoholicHistory: 喝酒
注意：此字段可能返回 null，表示取不到有效值。
        :type AlcoholicHistory: :class:`tencentcloud.mrs.v20200910.models.SmokeHistoryBlock`
        :param _MenstrualHistory: 月经史
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualHistoryBlock`
        :param _ObstericalHistory: 婚姻-生育史
注意：此字段可能返回 null，表示取不到有效值。
        :type ObstericalHistory: :class:`tencentcloud.mrs.v20200910.models.ObstetricalHistoryBlock`
        :param _FamilyHistory: 家族史
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyHistoryBlock`
        """
        self._BirthPlace = None
        self._LivePlace = None
        self._Job = None
        self._SmokeHistory = None
        self._AlcoholicHistory = None
        self._MenstrualHistory = None
        self._ObstericalHistory = None
        self._FamilyHistory = None

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def LivePlace(self):
        return self._LivePlace

    @LivePlace.setter
    def LivePlace(self, LivePlace):
        self._LivePlace = LivePlace

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def SmokeHistory(self):
        return self._SmokeHistory

    @SmokeHistory.setter
    def SmokeHistory(self, SmokeHistory):
        self._SmokeHistory = SmokeHistory

    @property
    def AlcoholicHistory(self):
        return self._AlcoholicHistory

    @AlcoholicHistory.setter
    def AlcoholicHistory(self, AlcoholicHistory):
        self._AlcoholicHistory = AlcoholicHistory

    @property
    def MenstrualHistory(self):
        return self._MenstrualHistory

    @MenstrualHistory.setter
    def MenstrualHistory(self, MenstrualHistory):
        self._MenstrualHistory = MenstrualHistory

    @property
    def ObstericalHistory(self):
        return self._ObstericalHistory

    @ObstericalHistory.setter
    def ObstericalHistory(self, ObstericalHistory):
        self._ObstericalHistory = ObstericalHistory

    @property
    def FamilyHistory(self):
        return self._FamilyHistory

    @FamilyHistory.setter
    def FamilyHistory(self, FamilyHistory):
        self._FamilyHistory = FamilyHistory


    def _deserialize(self, params):
        if params.get("BirthPlace") is not None:
            self._BirthPlace = BirthPlaceBlock()
            self._BirthPlace._deserialize(params.get("BirthPlace"))
        if params.get("LivePlace") is not None:
            self._LivePlace = BirthPlaceBlock()
            self._LivePlace._deserialize(params.get("LivePlace"))
        if params.get("Job") is not None:
            self._Job = BirthPlaceBlock()
            self._Job._deserialize(params.get("Job"))
        if params.get("SmokeHistory") is not None:
            self._SmokeHistory = SmokeHistoryBlock()
            self._SmokeHistory._deserialize(params.get("SmokeHistory"))
        if params.get("AlcoholicHistory") is not None:
            self._AlcoholicHistory = SmokeHistoryBlock()
            self._AlcoholicHistory._deserialize(params.get("AlcoholicHistory"))
        if params.get("MenstrualHistory") is not None:
            self._MenstrualHistory = MenstrualHistoryBlock()
            self._MenstrualHistory._deserialize(params.get("MenstrualHistory"))
        if params.get("ObstericalHistory") is not None:
            self._ObstericalHistory = ObstetricalHistoryBlock()
            self._ObstericalHistory._deserialize(params.get("ObstericalHistory"))
        if params.get("FamilyHistory") is not None:
            self._FamilyHistory = FamilyHistoryBlock()
            self._FamilyHistory._deserialize(params.get("FamilyHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalMedicalHistory(AbstractModel):
    """个人史

    """

    def __init__(self):
        r"""
        :param _BirthPlace: 出生史
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param _LivePlace: 居住史
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePlace: str
        :param _Job: 工作史
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: str
        :param _SmokeHistory: 吸烟史
注意：此字段可能返回 null，表示取不到有效值。
        :type SmokeHistory: str
        :param _AlcoholicHistory: 饮酒史
注意：此字段可能返回 null，表示取不到有效值。
        :type AlcoholicHistory: str
        """
        self._BirthPlace = None
        self._LivePlace = None
        self._Job = None
        self._SmokeHistory = None
        self._AlcoholicHistory = None

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def LivePlace(self):
        return self._LivePlace

    @LivePlace.setter
    def LivePlace(self, LivePlace):
        self._LivePlace = LivePlace

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def SmokeHistory(self):
        return self._SmokeHistory

    @SmokeHistory.setter
    def SmokeHistory(self, SmokeHistory):
        self._SmokeHistory = SmokeHistory

    @property
    def AlcoholicHistory(self):
        return self._AlcoholicHistory

    @AlcoholicHistory.setter
    def AlcoholicHistory(self, AlcoholicHistory):
        self._AlcoholicHistory = AlcoholicHistory


    def _deserialize(self, params):
        self._BirthPlace = params.get("BirthPlace")
        self._LivePlace = params.get("LivePlace")
        self._Job = params.get("Job")
        self._SmokeHistory = params.get("SmokeHistory")
        self._AlcoholicHistory = params.get("AlcoholicHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """点坐标

    """

    def __init__(self):
        r"""
        :param _X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param _Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoslistBlock(AbstractModel):
    """肯定列表

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Prescription(AbstractModel):
    """处方单

    """

    def __init__(self):
        r"""
        :param _MedicineList: 药品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicineList: list of Medicine
        """
        self._MedicineList = None

    @property
    def MedicineList(self):
        return self._MedicineList

    @MedicineList.setter
    def MedicineList(self, MedicineList):
        self._MedicineList = MedicineList


    def _deserialize(self, params):
        if params.get("MedicineList") is not None:
            self._MedicineList = []
            for item in params.get("MedicineList"):
                obj = Medicine()
                obj._deserialize(item)
                self._MedicineList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rectangle(AbstractModel):
    """位置坐标

    """

    def __init__(self):
        r"""
        :param _X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param _Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param _W: 宽
注意：此字段可能返回 null，表示取不到有效值。
        :type W: int
        :param _H: 高
注意：此字段可能返回 null，表示取不到有效值。
        :type H: int
        """
        self._X = None
        self._Y = None
        self._W = None
        self._H = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def W(self):
        return self._W

    @W.setter
    def W(self, W):
        self._W = W

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, H):
        self._H = H


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._W = params.get("W")
        self._H = params.get("H")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelapseDateBlock(AbstractModel):
    """复发时间

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _DiseaseName: 疾病名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseName: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._DiseaseName = None
        self._Type = None
        self._Norm = None
        self._Unit = None
        self._Timestamp = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def DiseaseName(self):
        return self._DiseaseName

    @DiseaseName.setter
    def DiseaseName(self, DiseaseName):
        self._DiseaseName = DiseaseName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Norm(self):
        return self._Norm

    @Norm.setter
    def Norm(self, Norm):
        self._Norm = Norm

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._DiseaseName = params.get("DiseaseName")
        self._Type = params.get("Type")
        self._Norm = params.get("Norm")
        self._Unit = params.get("Unit")
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeCancerHistoryBlock(AbstractModel):
    """家族肿瘤史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _RelativeCancerList: 肿瘤史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerList: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._RelativeCancerList = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def RelativeCancerList(self):
        return self._RelativeCancerList

    @RelativeCancerList.setter
    def RelativeCancerList(self, RelativeCancerList):
        self._RelativeCancerList = RelativeCancerList

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._RelativeCancerList = params.get("RelativeCancerList")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeHistoryBlock(AbstractModel):
    """家庭成员

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Detail: 成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of RelativeHistoryDetailBlock
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Detail = None
        self._Src = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = RelativeHistoryDetailBlock()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeHistoryDetailBlock(AbstractModel):
    """家庭成员详情

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Relation: 关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Relation: str
        :param _TimeOfDeath: 死亡时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOfDeath: str
        :param _TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        """
        self._Name = None
        self._Relation = None
        self._TimeOfDeath = None
        self._TimeType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def TimeOfDeath(self):
        return self._TimeOfDeath

    @TimeOfDeath.setter
    def TimeOfDeath(self, TimeOfDeath):
        self._TimeOfDeath = TimeOfDeath

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Relation = params.get("Relation")
        self._TimeOfDeath = params.get("TimeOfDeath")
        self._TimeType = params.get("TimeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Report(AbstractModel):
    """报告类型

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Name = None
        self._Index = None
        self._Src = None
        self._Value = None
        self._Coords = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportInfo(AbstractModel):
    """报告基本信息

    """

    def __init__(self):
        r"""
        :param _Hospital: 医院名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Hospital: str
        :param _DepartmentName: 科室名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        :param _BillingTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingTime: str
        :param _ReportTime: 报告时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTime: str
        :param _InspectTime: 检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectTime: str
        :param _CheckNum: 检查号
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckNum: str
        :param _ImageNum: 影像号
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageNum: str
        :param _RadiationNum: 放射号
注意：此字段可能返回 null，表示取不到有效值。
        :type RadiationNum: str
        :param _TestNum: 检验号
注意：此字段可能返回 null，表示取不到有效值。
        :type TestNum: str
        :param _OutpatientNum: 门诊号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientNum: str
        :param _PathologyNum: 病理号
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologyNum: str
        :param _InHospitalNum: 住院号
注意：此字段可能返回 null，表示取不到有效值。
        :type InHospitalNum: str
        :param _SampleNum: 样本号
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleNum: str
        :param _SampleType: 标本种类
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: str
        :param _MedicalRecordNum: 病历号
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalRecordNum: str
        :param _ReportName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportName: str
        :param _UltraNum: 超声号
注意：此字段可能返回 null，表示取不到有效值。
        :type UltraNum: str
        :param _Diagnose: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnose: str
        :param _CheckItem: 检查项目
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItem: str
        :param _CheckMethod: 检查方法
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckMethod: str
        :param _DiagnoseTime: 诊断时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseTime: str
        :param _HealthCheckupNum: 体检号
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckupNum: str
        :param _OtherTime: 其它时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherTime: str
        :param _PrintTime: 打印时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PrintTime: str
        :param _Times: 未归类时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Times: list of Time
        """
        self._Hospital = None
        self._DepartmentName = None
        self._BillingTime = None
        self._ReportTime = None
        self._InspectTime = None
        self._CheckNum = None
        self._ImageNum = None
        self._RadiationNum = None
        self._TestNum = None
        self._OutpatientNum = None
        self._PathologyNum = None
        self._InHospitalNum = None
        self._SampleNum = None
        self._SampleType = None
        self._MedicalRecordNum = None
        self._ReportName = None
        self._UltraNum = None
        self._Diagnose = None
        self._CheckItem = None
        self._CheckMethod = None
        self._DiagnoseTime = None
        self._HealthCheckupNum = None
        self._OtherTime = None
        self._PrintTime = None
        self._Times = None

    @property
    def Hospital(self):
        return self._Hospital

    @Hospital.setter
    def Hospital(self, Hospital):
        self._Hospital = Hospital

    @property
    def DepartmentName(self):
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def BillingTime(self):
        return self._BillingTime

    @BillingTime.setter
    def BillingTime(self, BillingTime):
        self._BillingTime = BillingTime

    @property
    def ReportTime(self):
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime

    @property
    def InspectTime(self):
        return self._InspectTime

    @InspectTime.setter
    def InspectTime(self, InspectTime):
        self._InspectTime = InspectTime

    @property
    def CheckNum(self):
        return self._CheckNum

    @CheckNum.setter
    def CheckNum(self, CheckNum):
        self._CheckNum = CheckNum

    @property
    def ImageNum(self):
        return self._ImageNum

    @ImageNum.setter
    def ImageNum(self, ImageNum):
        self._ImageNum = ImageNum

    @property
    def RadiationNum(self):
        return self._RadiationNum

    @RadiationNum.setter
    def RadiationNum(self, RadiationNum):
        self._RadiationNum = RadiationNum

    @property
    def TestNum(self):
        return self._TestNum

    @TestNum.setter
    def TestNum(self, TestNum):
        self._TestNum = TestNum

    @property
    def OutpatientNum(self):
        return self._OutpatientNum

    @OutpatientNum.setter
    def OutpatientNum(self, OutpatientNum):
        self._OutpatientNum = OutpatientNum

    @property
    def PathologyNum(self):
        return self._PathologyNum

    @PathologyNum.setter
    def PathologyNum(self, PathologyNum):
        self._PathologyNum = PathologyNum

    @property
    def InHospitalNum(self):
        return self._InHospitalNum

    @InHospitalNum.setter
    def InHospitalNum(self, InHospitalNum):
        self._InHospitalNum = InHospitalNum

    @property
    def SampleNum(self):
        return self._SampleNum

    @SampleNum.setter
    def SampleNum(self, SampleNum):
        self._SampleNum = SampleNum

    @property
    def SampleType(self):
        return self._SampleType

    @SampleType.setter
    def SampleType(self, SampleType):
        self._SampleType = SampleType

    @property
    def MedicalRecordNum(self):
        return self._MedicalRecordNum

    @MedicalRecordNum.setter
    def MedicalRecordNum(self, MedicalRecordNum):
        self._MedicalRecordNum = MedicalRecordNum

    @property
    def ReportName(self):
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def UltraNum(self):
        return self._UltraNum

    @UltraNum.setter
    def UltraNum(self, UltraNum):
        self._UltraNum = UltraNum

    @property
    def Diagnose(self):
        return self._Diagnose

    @Diagnose.setter
    def Diagnose(self, Diagnose):
        self._Diagnose = Diagnose

    @property
    def CheckItem(self):
        return self._CheckItem

    @CheckItem.setter
    def CheckItem(self, CheckItem):
        self._CheckItem = CheckItem

    @property
    def CheckMethod(self):
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def DiagnoseTime(self):
        return self._DiagnoseTime

    @DiagnoseTime.setter
    def DiagnoseTime(self, DiagnoseTime):
        self._DiagnoseTime = DiagnoseTime

    @property
    def HealthCheckupNum(self):
        return self._HealthCheckupNum

    @HealthCheckupNum.setter
    def HealthCheckupNum(self, HealthCheckupNum):
        self._HealthCheckupNum = HealthCheckupNum

    @property
    def OtherTime(self):
        return self._OtherTime

    @OtherTime.setter
    def OtherTime(self, OtherTime):
        self._OtherTime = OtherTime

    @property
    def PrintTime(self):
        return self._PrintTime

    @PrintTime.setter
    def PrintTime(self, PrintTime):
        self._PrintTime = PrintTime

    @property
    def Times(self):
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times


    def _deserialize(self, params):
        self._Hospital = params.get("Hospital")
        self._DepartmentName = params.get("DepartmentName")
        self._BillingTime = params.get("BillingTime")
        self._ReportTime = params.get("ReportTime")
        self._InspectTime = params.get("InspectTime")
        self._CheckNum = params.get("CheckNum")
        self._ImageNum = params.get("ImageNum")
        self._RadiationNum = params.get("RadiationNum")
        self._TestNum = params.get("TestNum")
        self._OutpatientNum = params.get("OutpatientNum")
        self._PathologyNum = params.get("PathologyNum")
        self._InHospitalNum = params.get("InHospitalNum")
        self._SampleNum = params.get("SampleNum")
        self._SampleType = params.get("SampleType")
        self._MedicalRecordNum = params.get("MedicalRecordNum")
        self._ReportName = params.get("ReportName")
        self._UltraNum = params.get("UltraNum")
        self._Diagnose = params.get("Diagnose")
        self._CheckItem = params.get("CheckItem")
        self._CheckMethod = params.get("CheckMethod")
        self._DiagnoseTime = params.get("DiagnoseTime")
        self._HealthCheckupNum = params.get("HealthCheckupNum")
        self._OtherTime = params.get("OtherTime")
        self._PrintTime = params.get("PrintTime")
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = Time()
                obj._deserialize(item)
                self._Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTypeVersion(AbstractModel):
    """指定报告类型选用其结构化版本

    """

    def __init__(self):
        r"""
        :param _ReportType: 检验报告
        :type ReportType: int
        :param _Version: 版本2
        :type Version: int
        """
        self._ReportType = None
        self._Version = None

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ReportType = params.get("ReportType")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultInfo(AbstractModel):
    """结论信息

    """

    def __init__(self):
        r"""
        :param _Text: 段落文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Items: 结论详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of BaseInfo
        """
        self._Text = None
        self._Items = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self._Text = BaseInfo()
            self._Text._deserialize(params.get("Text"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BaseInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Size(AbstractModel):
    """大小

    """

    def __init__(self):
        r"""
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _NormSize: 标准大小
注意：此字段可能返回 null，表示取不到有效值。
        :type NormSize: :class:`tencentcloud.mrs.v20200910.models.NormSize`
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Index = None
        self._NormSize = None
        self._Src = None
        self._Value = None
        self._Name = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def NormSize(self):
        return self._NormSize

    @NormSize.setter
    def NormSize(self, NormSize):
        self._NormSize = NormSize

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        if params.get("NormSize") is not None:
            self._NormSize = NormSize()
            self._NormSize._deserialize(params.get("NormSize"))
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmokeHistoryBlock(AbstractModel):
    """吸烟史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _TimeUnit: 时间单位
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeNorm: 时间归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeNorm: str
        :param _Amount: 吸烟量
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: str
        :param _QuitState: 戒烟状态
注意：此字段可能返回 null，表示取不到有效值。
        :type QuitState: bool
        :param _State: 是否吸烟
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param _Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._TimeUnit = None
        self._TimeNorm = None
        self._Amount = None
        self._QuitState = None
        self._State = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeNorm(self):
        return self._TimeNorm

    @TimeNorm.setter
    def TimeNorm(self, TimeNorm):
        self._TimeNorm = TimeNorm

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def QuitState(self):
        return self._QuitState

    @QuitState.setter
    def QuitState(self, QuitState):
        self._QuitState = QuitState

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeNorm = params.get("TimeNorm")
        self._Amount = params.get("Amount")
        self._QuitState = params.get("QuitState")
        self._State = params.get("State")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Summary(AbstractModel):
    """结论

    """

    def __init__(self):
        r"""
        :param _Symptom: 症状
注意：此字段可能返回 null，表示取不到有效值。
        :type Symptom: list of SymptomInfo
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Symptom = None
        self._Text = None
        self._Coords = None

    @property
    def Symptom(self):
        return self._Symptom

    @Symptom.setter
    def Symptom(self, Symptom):
        self._Symptom = Symptom

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Symptom") is not None:
            self._Symptom = []
            for item in params.get("Symptom"):
                obj = SymptomInfo()
                obj._deserialize(item)
                self._Symptom.append(obj)
        self._Text = params.get("Text")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryInfo(AbstractModel):
    """诊断结论

    """

    def __init__(self):
        r"""
        :param _Text: 诊断结论文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param _Infos: 诊断结论详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Infos: list of DetailInformation
        """
        self._Text = None
        self._Infos = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self._Text = BaseInfo()
            self._Text._deserialize(params.get("Text"))
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DetailInformation()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Surgery(AbstractModel):
    """手术记录

    """

    def __init__(self):
        r"""
        :param _SurgeryHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryHistory: :class:`tencentcloud.mrs.v20200910.models.SurgeryHistory`
        :param _OtherInfo: 其他信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherInfo: :class:`tencentcloud.mrs.v20200910.models.OtherInfo`
        """
        self._SurgeryHistory = None
        self._OtherInfo = None

    @property
    def SurgeryHistory(self):
        return self._SurgeryHistory

    @SurgeryHistory.setter
    def SurgeryHistory(self, SurgeryHistory):
        self._SurgeryHistory = SurgeryHistory

    @property
    def OtherInfo(self):
        return self._OtherInfo

    @OtherInfo.setter
    def OtherInfo(self, OtherInfo):
        self._OtherInfo = OtherInfo


    def _deserialize(self, params):
        if params.get("SurgeryHistory") is not None:
            self._SurgeryHistory = SurgeryHistory()
            self._SurgeryHistory._deserialize(params.get("SurgeryHistory"))
        if params.get("OtherInfo") is not None:
            self._OtherInfo = OtherInfo()
            self._OtherInfo._deserialize(params.get("OtherInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryAttr(AbstractModel):
    """手术记录属性

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryConditionBlock(AbstractModel):
    """手术经过

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _SurgeryList: 手术历史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryList: list of SurgeryListBlock
        :param _Value: 对外输出值

注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._SurgeryList = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def SurgeryList(self):
        return self._SurgeryList

    @SurgeryList.setter
    def SurgeryList(self, SurgeryList):
        self._SurgeryList = SurgeryList

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        if params.get("SurgeryList") is not None:
            self._SurgeryList = []
            for item in params.get("SurgeryList"):
                obj = SurgeryListBlock()
                obj._deserialize(item)
                self._SurgeryList.append(obj)
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryHistory(AbstractModel):
    """手术史

    """

    def __init__(self):
        r"""
        :param _SurgeryName: 手术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryName: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _SurgeryDate: 手术日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryDate: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _PreoperativePathology: 术前诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PreoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _IntraoperativePathology: 术中诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type IntraoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _PostoperativePathology: 术后诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PostoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param _DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        """
        self._SurgeryName = None
        self._SurgeryDate = None
        self._PreoperativePathology = None
        self._IntraoperativePathology = None
        self._PostoperativePathology = None
        self._DischargeDiagnosis = None

    @property
    def SurgeryName(self):
        return self._SurgeryName

    @SurgeryName.setter
    def SurgeryName(self, SurgeryName):
        self._SurgeryName = SurgeryName

    @property
    def SurgeryDate(self):
        return self._SurgeryDate

    @SurgeryDate.setter
    def SurgeryDate(self, SurgeryDate):
        self._SurgeryDate = SurgeryDate

    @property
    def PreoperativePathology(self):
        return self._PreoperativePathology

    @PreoperativePathology.setter
    def PreoperativePathology(self, PreoperativePathology):
        self._PreoperativePathology = PreoperativePathology

    @property
    def IntraoperativePathology(self):
        return self._IntraoperativePathology

    @IntraoperativePathology.setter
    def IntraoperativePathology(self, IntraoperativePathology):
        self._IntraoperativePathology = IntraoperativePathology

    @property
    def PostoperativePathology(self):
        return self._PostoperativePathology

    @PostoperativePathology.setter
    def PostoperativePathology(self, PostoperativePathology):
        self._PostoperativePathology = PostoperativePathology

    @property
    def DischargeDiagnosis(self):
        return self._DischargeDiagnosis

    @DischargeDiagnosis.setter
    def DischargeDiagnosis(self, DischargeDiagnosis):
        self._DischargeDiagnosis = DischargeDiagnosis


    def _deserialize(self, params):
        if params.get("SurgeryName") is not None:
            self._SurgeryName = SurgeryAttr()
            self._SurgeryName._deserialize(params.get("SurgeryName"))
        if params.get("SurgeryDate") is not None:
            self._SurgeryDate = SurgeryAttr()
            self._SurgeryDate._deserialize(params.get("SurgeryDate"))
        if params.get("PreoperativePathology") is not None:
            self._PreoperativePathology = SurgeryAttr()
            self._PreoperativePathology._deserialize(params.get("PreoperativePathology"))
        if params.get("IntraoperativePathology") is not None:
            self._IntraoperativePathology = SurgeryAttr()
            self._IntraoperativePathology._deserialize(params.get("IntraoperativePathology"))
        if params.get("PostoperativePathology") is not None:
            self._PostoperativePathology = SurgeryAttr()
            self._PostoperativePathology._deserialize(params.get("PostoperativePathology"))
        if params.get("DischargeDiagnosis") is not None:
            self._DischargeDiagnosis = SurgeryAttr()
            self._DischargeDiagnosis._deserialize(params.get("DischargeDiagnosis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryHistoryBlock(AbstractModel):
    """手术史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Surgerylist: 手术列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Surgerylist: list of SurgeryListBlock
        """
        self._Name = None
        self._Src = None
        self._Value = None
        self._Surgerylist = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Surgerylist(self):
        return self._Surgerylist

    @Surgerylist.setter
    def Surgerylist(self, Surgerylist):
        self._Surgerylist = Surgerylist


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._Value = params.get("Value")
        if params.get("Surgerylist") is not None:
            self._Surgerylist = []
            for item in params.get("Surgerylist"):
                obj = SurgeryListBlock()
                obj._deserialize(item)
                self._Surgerylist.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryListBlock(AbstractModel):
    """手术列表

    """

    def __init__(self):
        r"""
        :param _Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _TimeType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: list of str
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        """
        self._Time = None
        self._TimeType = None
        self._Name = None
        self._Part = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TimeType = params.get("TimeType")
        self._Name = params.get("Name")
        self._Part = params.get("Part")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SymptomInfo(AbstractModel):
    """病症描述信息

    """

    def __init__(self):
        r"""
        :param _Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _Symptom: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Symptom: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Attrs: 属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Attrs: list of BlockInfo
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Grade = None
        self._Part = None
        self._Index = None
        self._Symptom = None
        self._Attrs = None
        self._Src = None
        self._Coords = None

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Symptom(self):
        return self._Symptom

    @Symptom.setter
    def Symptom(self, Symptom):
        self._Symptom = Symptom

    @property
    def Attrs(self):
        return self._Attrs

    @Attrs.setter
    def Attrs(self, Attrs):
        self._Attrs = Attrs

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Grade") is not None:
            self._Grade = BlockInfo()
            self._Grade._deserialize(params.get("Grade"))
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        self._Index = params.get("Index")
        if params.get("Symptom") is not None:
            self._Symptom = BlockInfo()
            self._Symptom._deserialize(params.get("Symptom"))
        if params.get("Attrs") is not None:
            self._Attrs = []
            for item in params.get("Attrs"):
                obj = BlockInfo()
                obj._deserialize(item)
                self._Attrs.append(obj)
        self._Src = params.get("Src")
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableIndicators(AbstractModel):
    """检验报告结构

    """

    def __init__(self):
        r"""
        :param _Indicators: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicators: list of IndicatorItemV2
        :param _Sample: 采样标本
注意：此字段可能返回 null，表示取不到有效值。
        :type Sample: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self._Indicators = None
        self._Sample = None

    @property
    def Indicators(self):
        return self._Indicators

    @Indicators.setter
    def Indicators(self, Indicators):
        self._Indicators = Indicators

    @property
    def Sample(self):
        return self._Sample

    @Sample.setter
    def Sample(self, Sample):
        self._Sample = Sample


    def _deserialize(self, params):
        if params.get("Indicators") is not None:
            self._Indicators = []
            for item in params.get("Indicators"):
                obj = IndicatorItemV2()
                obj._deserialize(item)
                self._Indicators.append(obj)
        if params.get("Sample") is not None:
            self._Sample = BaseItem()
            self._Sample._deserialize(params.get("Sample"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """报告模板

    """

    def __init__(self):
        r"""
        :param _PatientInfo: 患者信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PatientInfo: :class:`tencentcloud.mrs.v20200910.models.PatientInfo`
        :param _ReportInfo: 报告信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportInfo: :class:`tencentcloud.mrs.v20200910.models.ReportInfo`
        :param _Check: 检查报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Check: :class:`tencentcloud.mrs.v20200910.models.Check`
        :param _Pathology: 病理报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Pathology: :class:`tencentcloud.mrs.v20200910.models.PathologyReport`
        :param _MedDoc: 出院报告，入院报告，门诊病历
注意：此字段可能返回 null，表示取不到有效值。
        :type MedDoc: :class:`tencentcloud.mrs.v20200910.models.MedDoc`
        :param _DiagCert: 诊断证明
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagCert: :class:`tencentcloud.mrs.v20200910.models.DiagCert`
        :param _FirstPage: 病案首页
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstPage: :class:`tencentcloud.mrs.v20200910.models.FirstPage`
        :param _Indicator: 检验报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicator: :class:`tencentcloud.mrs.v20200910.models.Indicator`
        :param _ReportType: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: str
        :param _MedicalRecordInfo: 门诊病历信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalRecordInfo: :class:`tencentcloud.mrs.v20200910.models.MedicalRecordInfo`
        :param _Hospitalization: 出入院信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Hospitalization: :class:`tencentcloud.mrs.v20200910.models.Hospitalization`
        :param _Surgery: 手术记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Surgery: :class:`tencentcloud.mrs.v20200910.models.Surgery`
        :param _Electrocardiogram: 心电图报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Electrocardiogram: :class:`tencentcloud.mrs.v20200910.models.Electrocardiogram`
        :param _Endoscopy: 内窥镜报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Endoscopy: :class:`tencentcloud.mrs.v20200910.models.Endoscopy`
        :param _Prescription: 处方单
注意：此字段可能返回 null，表示取不到有效值。
        :type Prescription: :class:`tencentcloud.mrs.v20200910.models.Prescription`
        :param _VaccineCertificate: 疫苗接种凭证
注意：此字段可能返回 null，表示取不到有效值。
        :type VaccineCertificate: :class:`tencentcloud.mrs.v20200910.models.VaccineCertificate`
        :param _OcrText: OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrText: str
        :param _OcrResult: OCR拼接后文本
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrResult: str
        :param _ReportTypeDesc: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTypeDesc: str
        :param _PathologyV2: 病理报告v2
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologyV2: :class:`tencentcloud.mrs.v20200910.models.PathologyV2`
        :param _C14: 碳14尿素呼气试验
注意：此字段可能返回 null，表示取不到有效值。
        :type C14: :class:`tencentcloud.mrs.v20200910.models.Indicator`
        :param _Exame: 体检结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Exame: :class:`tencentcloud.mrs.v20200910.models.Exame`
        :param _MedDocV2: 出院报告v2，入院报告v2，门诊病历v2
注意：此字段可能返回 null，表示取不到有效值。
        :type MedDocV2: :class:`tencentcloud.mrs.v20200910.models.DischargeInfoBlock`
        :param _IndicatorV3: 检验报告v3
注意：此字段可能返回 null，表示取不到有效值。
        :type IndicatorV3: :class:`tencentcloud.mrs.v20200910.models.IndicatorV3`
        :param _Covid: 核酸报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Covid: :class:`tencentcloud.mrs.v20200910.models.CovidItemsInfo`
        :param _Maternity: 孕产报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Maternity: :class:`tencentcloud.mrs.v20200910.models.Maternity`
        :param _Eye: 眼科报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Eye: :class:`tencentcloud.mrs.v20200910.models.EyeItemsInfo`
        :param _BirthCert: 出生证明
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthCert: :class:`tencentcloud.mrs.v20200910.models.BirthCert`
        :param _Timeline: 时间轴
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeline: :class:`tencentcloud.mrs.v20200910.models.TimelineInformation`
        """
        self._PatientInfo = None
        self._ReportInfo = None
        self._Check = None
        self._Pathology = None
        self._MedDoc = None
        self._DiagCert = None
        self._FirstPage = None
        self._Indicator = None
        self._ReportType = None
        self._MedicalRecordInfo = None
        self._Hospitalization = None
        self._Surgery = None
        self._Electrocardiogram = None
        self._Endoscopy = None
        self._Prescription = None
        self._VaccineCertificate = None
        self._OcrText = None
        self._OcrResult = None
        self._ReportTypeDesc = None
        self._PathologyV2 = None
        self._C14 = None
        self._Exame = None
        self._MedDocV2 = None
        self._IndicatorV3 = None
        self._Covid = None
        self._Maternity = None
        self._Eye = None
        self._BirthCert = None
        self._Timeline = None

    @property
    def PatientInfo(self):
        return self._PatientInfo

    @PatientInfo.setter
    def PatientInfo(self, PatientInfo):
        self._PatientInfo = PatientInfo

    @property
    def ReportInfo(self):
        return self._ReportInfo

    @ReportInfo.setter
    def ReportInfo(self, ReportInfo):
        self._ReportInfo = ReportInfo

    @property
    def Check(self):
        return self._Check

    @Check.setter
    def Check(self, Check):
        self._Check = Check

    @property
    def Pathology(self):
        return self._Pathology

    @Pathology.setter
    def Pathology(self, Pathology):
        self._Pathology = Pathology

    @property
    def MedDoc(self):
        return self._MedDoc

    @MedDoc.setter
    def MedDoc(self, MedDoc):
        self._MedDoc = MedDoc

    @property
    def DiagCert(self):
        return self._DiagCert

    @DiagCert.setter
    def DiagCert(self, DiagCert):
        self._DiagCert = DiagCert

    @property
    def FirstPage(self):
        return self._FirstPage

    @FirstPage.setter
    def FirstPage(self, FirstPage):
        self._FirstPage = FirstPage

    @property
    def Indicator(self):
        return self._Indicator

    @Indicator.setter
    def Indicator(self, Indicator):
        self._Indicator = Indicator

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def MedicalRecordInfo(self):
        return self._MedicalRecordInfo

    @MedicalRecordInfo.setter
    def MedicalRecordInfo(self, MedicalRecordInfo):
        self._MedicalRecordInfo = MedicalRecordInfo

    @property
    def Hospitalization(self):
        return self._Hospitalization

    @Hospitalization.setter
    def Hospitalization(self, Hospitalization):
        self._Hospitalization = Hospitalization

    @property
    def Surgery(self):
        return self._Surgery

    @Surgery.setter
    def Surgery(self, Surgery):
        self._Surgery = Surgery

    @property
    def Electrocardiogram(self):
        return self._Electrocardiogram

    @Electrocardiogram.setter
    def Electrocardiogram(self, Electrocardiogram):
        self._Electrocardiogram = Electrocardiogram

    @property
    def Endoscopy(self):
        return self._Endoscopy

    @Endoscopy.setter
    def Endoscopy(self, Endoscopy):
        self._Endoscopy = Endoscopy

    @property
    def Prescription(self):
        return self._Prescription

    @Prescription.setter
    def Prescription(self, Prescription):
        self._Prescription = Prescription

    @property
    def VaccineCertificate(self):
        return self._VaccineCertificate

    @VaccineCertificate.setter
    def VaccineCertificate(self, VaccineCertificate):
        self._VaccineCertificate = VaccineCertificate

    @property
    def OcrText(self):
        return self._OcrText

    @OcrText.setter
    def OcrText(self, OcrText):
        self._OcrText = OcrText

    @property
    def OcrResult(self):
        return self._OcrResult

    @OcrResult.setter
    def OcrResult(self, OcrResult):
        self._OcrResult = OcrResult

    @property
    def ReportTypeDesc(self):
        return self._ReportTypeDesc

    @ReportTypeDesc.setter
    def ReportTypeDesc(self, ReportTypeDesc):
        self._ReportTypeDesc = ReportTypeDesc

    @property
    def PathologyV2(self):
        return self._PathologyV2

    @PathologyV2.setter
    def PathologyV2(self, PathologyV2):
        self._PathologyV2 = PathologyV2

    @property
    def C14(self):
        return self._C14

    @C14.setter
    def C14(self, C14):
        self._C14 = C14

    @property
    def Exame(self):
        return self._Exame

    @Exame.setter
    def Exame(self, Exame):
        self._Exame = Exame

    @property
    def MedDocV2(self):
        return self._MedDocV2

    @MedDocV2.setter
    def MedDocV2(self, MedDocV2):
        self._MedDocV2 = MedDocV2

    @property
    def IndicatorV3(self):
        return self._IndicatorV3

    @IndicatorV3.setter
    def IndicatorV3(self, IndicatorV3):
        self._IndicatorV3 = IndicatorV3

    @property
    def Covid(self):
        return self._Covid

    @Covid.setter
    def Covid(self, Covid):
        self._Covid = Covid

    @property
    def Maternity(self):
        return self._Maternity

    @Maternity.setter
    def Maternity(self, Maternity):
        self._Maternity = Maternity

    @property
    def Eye(self):
        return self._Eye

    @Eye.setter
    def Eye(self, Eye):
        self._Eye = Eye

    @property
    def BirthCert(self):
        return self._BirthCert

    @BirthCert.setter
    def BirthCert(self, BirthCert):
        self._BirthCert = BirthCert

    @property
    def Timeline(self):
        return self._Timeline

    @Timeline.setter
    def Timeline(self, Timeline):
        self._Timeline = Timeline


    def _deserialize(self, params):
        if params.get("PatientInfo") is not None:
            self._PatientInfo = PatientInfo()
            self._PatientInfo._deserialize(params.get("PatientInfo"))
        if params.get("ReportInfo") is not None:
            self._ReportInfo = ReportInfo()
            self._ReportInfo._deserialize(params.get("ReportInfo"))
        if params.get("Check") is not None:
            self._Check = Check()
            self._Check._deserialize(params.get("Check"))
        if params.get("Pathology") is not None:
            self._Pathology = PathologyReport()
            self._Pathology._deserialize(params.get("Pathology"))
        if params.get("MedDoc") is not None:
            self._MedDoc = MedDoc()
            self._MedDoc._deserialize(params.get("MedDoc"))
        if params.get("DiagCert") is not None:
            self._DiagCert = DiagCert()
            self._DiagCert._deserialize(params.get("DiagCert"))
        if params.get("FirstPage") is not None:
            self._FirstPage = FirstPage()
            self._FirstPage._deserialize(params.get("FirstPage"))
        if params.get("Indicator") is not None:
            self._Indicator = Indicator()
            self._Indicator._deserialize(params.get("Indicator"))
        self._ReportType = params.get("ReportType")
        if params.get("MedicalRecordInfo") is not None:
            self._MedicalRecordInfo = MedicalRecordInfo()
            self._MedicalRecordInfo._deserialize(params.get("MedicalRecordInfo"))
        if params.get("Hospitalization") is not None:
            self._Hospitalization = Hospitalization()
            self._Hospitalization._deserialize(params.get("Hospitalization"))
        if params.get("Surgery") is not None:
            self._Surgery = Surgery()
            self._Surgery._deserialize(params.get("Surgery"))
        if params.get("Electrocardiogram") is not None:
            self._Electrocardiogram = Electrocardiogram()
            self._Electrocardiogram._deserialize(params.get("Electrocardiogram"))
        if params.get("Endoscopy") is not None:
            self._Endoscopy = Endoscopy()
            self._Endoscopy._deserialize(params.get("Endoscopy"))
        if params.get("Prescription") is not None:
            self._Prescription = Prescription()
            self._Prescription._deserialize(params.get("Prescription"))
        if params.get("VaccineCertificate") is not None:
            self._VaccineCertificate = VaccineCertificate()
            self._VaccineCertificate._deserialize(params.get("VaccineCertificate"))
        self._OcrText = params.get("OcrText")
        self._OcrResult = params.get("OcrResult")
        self._ReportTypeDesc = params.get("ReportTypeDesc")
        if params.get("PathologyV2") is not None:
            self._PathologyV2 = PathologyV2()
            self._PathologyV2._deserialize(params.get("PathologyV2"))
        if params.get("C14") is not None:
            self._C14 = Indicator()
            self._C14._deserialize(params.get("C14"))
        if params.get("Exame") is not None:
            self._Exame = Exame()
            self._Exame._deserialize(params.get("Exame"))
        if params.get("MedDocV2") is not None:
            self._MedDocV2 = DischargeInfoBlock()
            self._MedDocV2._deserialize(params.get("MedDocV2"))
        if params.get("IndicatorV3") is not None:
            self._IndicatorV3 = IndicatorV3()
            self._IndicatorV3._deserialize(params.get("IndicatorV3"))
        if params.get("Covid") is not None:
            self._Covid = CovidItemsInfo()
            self._Covid._deserialize(params.get("Covid"))
        if params.get("Maternity") is not None:
            self._Maternity = Maternity()
            self._Maternity._deserialize(params.get("Maternity"))
        if params.get("Eye") is not None:
            self._Eye = EyeItemsInfo()
            self._Eye._deserialize(params.get("Eye"))
        if params.get("BirthCert") is not None:
            self._BirthCert = BirthCert()
            self._BirthCert._deserialize(params.get("BirthCert"))
        if params.get("Timeline") is not None:
            self._Timeline = TimelineInformation()
            self._Timeline._deserialize(params.get("Timeline"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToClassRequest(AbstractModel):
    """TextToClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 报告文本
        :type Text: str
        :param _UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        """
        self._Text = None
        self._UserType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToClassResponse(AbstractModel):
    """TextToClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextTypeList: 分类结果
        :type TextTypeList: list of TextType
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextTypeList = None
        self._RequestId = None

    @property
    def TextTypeList(self):
        return self._TextTypeList

    @TextTypeList.setter
    def TextTypeList(self, TextTypeList):
        self._TextTypeList = TextTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextTypeList") is not None:
            self._TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self._TextTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class TextToObjectRequest(AbstractModel):
    """TextToObject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 报告文本
        :type Text: str
        :param _Type: 报告类型，目前支持12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明），363（心电图），27（内窥镜检查），215（处方单），219（免疫接种证明），301（C14呼气试验）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）
        :type Type: int
        :param _IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为False，则Type字段不能为0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。
        :type IsUsedClassify: bool
        :param _UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        :param _ReportTypeVersion: 可选。用于指定不同报告使用的结构化引擎版本，不同版本返回的JSON 数据结果不兼容。若不指定版本号，就默认用旧的版本号。
（1）检验报告 11，默认使用 V2，最高支持 V3。
（2）病理报告 15，默认使用 V1，最高支持 V2。
（3）入院记录29、出院记录 28、病历记录 216、病程记录 217、门诊记录 210，默认使用 V1，最高支持 V2。
        :type ReportTypeVersion: list of ReportTypeVersion
        """
        self._Text = None
        self._Type = None
        self._IsUsedClassify = None
        self._UserType = None
        self._ReportTypeVersion = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsUsedClassify(self):
        return self._IsUsedClassify

    @IsUsedClassify.setter
    def IsUsedClassify(self, IsUsedClassify):
        self._IsUsedClassify = IsUsedClassify

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def ReportTypeVersion(self):
        return self._ReportTypeVersion

    @ReportTypeVersion.setter
    def ReportTypeVersion(self, ReportTypeVersion):
        self._ReportTypeVersion = ReportTypeVersion


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._IsUsedClassify = params.get("IsUsedClassify")
        self._UserType = params.get("UserType")
        if params.get("ReportTypeVersion") is not None:
            self._ReportTypeVersion = []
            for item in params.get("ReportTypeVersion"):
                obj = ReportTypeVersion()
                obj._deserialize(item)
                self._ReportTypeVersion.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToObjectResponse(AbstractModel):
    """TextToObject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 报告结构化结果
        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class TextType(AbstractModel):
    """文本类型

    """

    def __init__(self):
        r"""
        :param _Id: 类别Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Level: 类别层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _Name: 类别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Id = None
        self._Level = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Level = params.get("Level")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Time(AbstractModel):
    """时间

    """

    def __init__(self):
        r"""
        :param _Name: 具体时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 时间值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimelineEvent(AbstractModel):
    """时间轴事件

    """

    def __init__(self):
        r"""
        :param _Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Src: 原文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _SubType: 事件子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param _Time: 事件发生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param _Value: 事件值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Rectangle: 位置坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Rectangle: :class:`tencentcloud.mrs.v20200910.models.Rectangle`
        :param _Place: 事件发生地点
注意：此字段可能返回 null，表示取不到有效值。
        :type Place: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._Type = None
        self._Src = None
        self._SubType = None
        self._Time = None
        self._Value = None
        self._Rectangle = None
        self._Place = None
        self._EndTime = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rectangle(self):
        return self._Rectangle

    @Rectangle.setter
    def Rectangle(self, Rectangle):
        self._Rectangle = Rectangle

    @property
    def Place(self):
        return self._Place

    @Place.setter
    def Place(self, Place):
        self._Place = Place

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Src = params.get("Src")
        self._SubType = params.get("SubType")
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        if params.get("Rectangle") is not None:
            self._Rectangle = Rectangle()
            self._Rectangle._deserialize(params.get("Rectangle"))
        self._Place = params.get("Place")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimelineInformation(AbstractModel):
    """时间轴

    """

    def __init__(self):
        r"""
        :param _Timeline: 时间轴
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeline: list of TimelineEvent
        """
        self._Timeline = None

    @property
    def Timeline(self):
        return self._Timeline

    @Timeline.setter
    def Timeline(self, Timeline):
        self._Timeline = Timeline


    def _deserialize(self, params):
        if params.get("Timeline") is not None:
            self._Timeline = []
            for item in params.get("Timeline"):
                obj = TimelineEvent()
                obj._deserialize(item)
                self._Timeline.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransfusionHistoryBlock(AbstractModel):
    """输血史

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Src = None
        self._State = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Src = params.get("Src")
        self._State = params.get("State")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TreatmentRecord(AbstractModel):
    """病历

    """

    def __init__(self):
        r"""
        :param _DmissionCondition: 入院
注意：此字段可能返回 null，表示取不到有效值。
        :type DmissionCondition: str
        :param _ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaint: str
        :param _DiseasePresent: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresent: str
        :param _SymptomsAndSigns: 主要症状体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSigns: str
        :param _AuxiliaryExamination: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExamination: str
        :param _BodyExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExamination: str
        :param _SpecialistExamination: 专科检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExamination: str
        :param _MentalExamination: 精神检查
注意：此字段可能返回 null，表示取不到有效值。
        :type MentalExamination: str
        :param _CheckRecord: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecord: str
        :param _InspectResult: 化验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectResult: str
        :param _IncisionHealing: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealing: str
        :param _TreatmentSuggestion: 处理意见
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentSuggestion: str
        :param _FollowUpRequirements: 门诊随访要求
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUpRequirements: str
        :param _CheckAndTreatmentProcess: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcess: str
        :param _SurgeryCondition: 手术经过
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryCondition: str
        :param _ConditionChanges: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionChanges: str
        :param _DischargeCondition: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeCondition: str
        :param _PTNM: pTNM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: str
        :param _PTNMM: pTNMM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMM: str
        :param _PTNMN: pTNMN信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMN: str
        :param _PTNMT: pTNMT信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMT: str
        :param _ECOG: ECOG信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ECOG: str
        :param _NRS: NRS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NRS: str
        :param _KPS: KPS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KPS: str
        :param _DeathDate: 死亡日期
注意：此字段可能返回 null，表示取不到有效值。
        :type DeathDate: str
        :param _RelapseDate: 复发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RelapseDate: str
        :param _ObservationDays: 观测天数
注意：此字段可能返回 null，表示取不到有效值。
        :type ObservationDays: str
        """
        self._DmissionCondition = None
        self._ChiefComplaint = None
        self._DiseasePresent = None
        self._SymptomsAndSigns = None
        self._AuxiliaryExamination = None
        self._BodyExamination = None
        self._SpecialistExamination = None
        self._MentalExamination = None
        self._CheckRecord = None
        self._InspectResult = None
        self._IncisionHealing = None
        self._TreatmentSuggestion = None
        self._FollowUpRequirements = None
        self._CheckAndTreatmentProcess = None
        self._SurgeryCondition = None
        self._ConditionChanges = None
        self._DischargeCondition = None
        self._PTNM = None
        self._PTNMM = None
        self._PTNMN = None
        self._PTNMT = None
        self._ECOG = None
        self._NRS = None
        self._KPS = None
        self._DeathDate = None
        self._RelapseDate = None
        self._ObservationDays = None

    @property
    def DmissionCondition(self):
        return self._DmissionCondition

    @DmissionCondition.setter
    def DmissionCondition(self, DmissionCondition):
        self._DmissionCondition = DmissionCondition

    @property
    def ChiefComplaint(self):
        return self._ChiefComplaint

    @ChiefComplaint.setter
    def ChiefComplaint(self, ChiefComplaint):
        self._ChiefComplaint = ChiefComplaint

    @property
    def DiseasePresent(self):
        return self._DiseasePresent

    @DiseasePresent.setter
    def DiseasePresent(self, DiseasePresent):
        self._DiseasePresent = DiseasePresent

    @property
    def SymptomsAndSigns(self):
        return self._SymptomsAndSigns

    @SymptomsAndSigns.setter
    def SymptomsAndSigns(self, SymptomsAndSigns):
        self._SymptomsAndSigns = SymptomsAndSigns

    @property
    def AuxiliaryExamination(self):
        return self._AuxiliaryExamination

    @AuxiliaryExamination.setter
    def AuxiliaryExamination(self, AuxiliaryExamination):
        self._AuxiliaryExamination = AuxiliaryExamination

    @property
    def BodyExamination(self):
        return self._BodyExamination

    @BodyExamination.setter
    def BodyExamination(self, BodyExamination):
        self._BodyExamination = BodyExamination

    @property
    def SpecialistExamination(self):
        return self._SpecialistExamination

    @SpecialistExamination.setter
    def SpecialistExamination(self, SpecialistExamination):
        self._SpecialistExamination = SpecialistExamination

    @property
    def MentalExamination(self):
        return self._MentalExamination

    @MentalExamination.setter
    def MentalExamination(self, MentalExamination):
        self._MentalExamination = MentalExamination

    @property
    def CheckRecord(self):
        return self._CheckRecord

    @CheckRecord.setter
    def CheckRecord(self, CheckRecord):
        self._CheckRecord = CheckRecord

    @property
    def InspectResult(self):
        return self._InspectResult

    @InspectResult.setter
    def InspectResult(self, InspectResult):
        self._InspectResult = InspectResult

    @property
    def IncisionHealing(self):
        return self._IncisionHealing

    @IncisionHealing.setter
    def IncisionHealing(self, IncisionHealing):
        self._IncisionHealing = IncisionHealing

    @property
    def TreatmentSuggestion(self):
        return self._TreatmentSuggestion

    @TreatmentSuggestion.setter
    def TreatmentSuggestion(self, TreatmentSuggestion):
        self._TreatmentSuggestion = TreatmentSuggestion

    @property
    def FollowUpRequirements(self):
        return self._FollowUpRequirements

    @FollowUpRequirements.setter
    def FollowUpRequirements(self, FollowUpRequirements):
        self._FollowUpRequirements = FollowUpRequirements

    @property
    def CheckAndTreatmentProcess(self):
        return self._CheckAndTreatmentProcess

    @CheckAndTreatmentProcess.setter
    def CheckAndTreatmentProcess(self, CheckAndTreatmentProcess):
        self._CheckAndTreatmentProcess = CheckAndTreatmentProcess

    @property
    def SurgeryCondition(self):
        return self._SurgeryCondition

    @SurgeryCondition.setter
    def SurgeryCondition(self, SurgeryCondition):
        self._SurgeryCondition = SurgeryCondition

    @property
    def ConditionChanges(self):
        return self._ConditionChanges

    @ConditionChanges.setter
    def ConditionChanges(self, ConditionChanges):
        self._ConditionChanges = ConditionChanges

    @property
    def DischargeCondition(self):
        return self._DischargeCondition

    @DischargeCondition.setter
    def DischargeCondition(self, DischargeCondition):
        self._DischargeCondition = DischargeCondition

    @property
    def PTNM(self):
        return self._PTNM

    @PTNM.setter
    def PTNM(self, PTNM):
        self._PTNM = PTNM

    @property
    def PTNMM(self):
        return self._PTNMM

    @PTNMM.setter
    def PTNMM(self, PTNMM):
        self._PTNMM = PTNMM

    @property
    def PTNMN(self):
        return self._PTNMN

    @PTNMN.setter
    def PTNMN(self, PTNMN):
        self._PTNMN = PTNMN

    @property
    def PTNMT(self):
        return self._PTNMT

    @PTNMT.setter
    def PTNMT(self, PTNMT):
        self._PTNMT = PTNMT

    @property
    def ECOG(self):
        return self._ECOG

    @ECOG.setter
    def ECOG(self, ECOG):
        self._ECOG = ECOG

    @property
    def NRS(self):
        return self._NRS

    @NRS.setter
    def NRS(self, NRS):
        self._NRS = NRS

    @property
    def KPS(self):
        return self._KPS

    @KPS.setter
    def KPS(self, KPS):
        self._KPS = KPS

    @property
    def DeathDate(self):
        return self._DeathDate

    @DeathDate.setter
    def DeathDate(self, DeathDate):
        self._DeathDate = DeathDate

    @property
    def RelapseDate(self):
        return self._RelapseDate

    @RelapseDate.setter
    def RelapseDate(self, RelapseDate):
        self._RelapseDate = RelapseDate

    @property
    def ObservationDays(self):
        return self._ObservationDays

    @ObservationDays.setter
    def ObservationDays(self, ObservationDays):
        self._ObservationDays = ObservationDays


    def _deserialize(self, params):
        self._DmissionCondition = params.get("DmissionCondition")
        self._ChiefComplaint = params.get("ChiefComplaint")
        self._DiseasePresent = params.get("DiseasePresent")
        self._SymptomsAndSigns = params.get("SymptomsAndSigns")
        self._AuxiliaryExamination = params.get("AuxiliaryExamination")
        self._BodyExamination = params.get("BodyExamination")
        self._SpecialistExamination = params.get("SpecialistExamination")
        self._MentalExamination = params.get("MentalExamination")
        self._CheckRecord = params.get("CheckRecord")
        self._InspectResult = params.get("InspectResult")
        self._IncisionHealing = params.get("IncisionHealing")
        self._TreatmentSuggestion = params.get("TreatmentSuggestion")
        self._FollowUpRequirements = params.get("FollowUpRequirements")
        self._CheckAndTreatmentProcess = params.get("CheckAndTreatmentProcess")
        self._SurgeryCondition = params.get("SurgeryCondition")
        self._ConditionChanges = params.get("ConditionChanges")
        self._DischargeCondition = params.get("DischargeCondition")
        self._PTNM = params.get("PTNM")
        self._PTNMM = params.get("PTNMM")
        self._PTNMN = params.get("PTNMN")
        self._PTNMT = params.get("PTNMT")
        self._ECOG = params.get("ECOG")
        self._NRS = params.get("NRS")
        self._KPS = params.get("KPS")
        self._DeathDate = params.get("DeathDate")
        self._RelapseDate = params.get("RelapseDate")
        self._ObservationDays = params.get("ObservationDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TreatmentRecordBlock(AbstractModel):
    """治疗记录

    """

    def __init__(self):
        r"""
        :param _Immunohistochemistry: 免疫组化
注意：此字段可能返回 null，表示取不到有效值。
        :type Immunohistochemistry: :class:`tencentcloud.mrs.v20200910.models.ImmunohistochemistryBlock`
        :param _ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaint: :class:`tencentcloud.mrs.v20200910.models.ChiefComplaintBlock`
        :param _AdmissionCondition: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionCondition: :class:`tencentcloud.mrs.v20200910.models.AdmissionConditionBlock`
        :param _BodyExamination: 查体
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExamination: :class:`tencentcloud.mrs.v20200910.models.BodyExaminationBlock`
        :param _AdmissionDiagnosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param _AdmissionTraditionalDiagnosis: 入院中医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionTraditionalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param _AdmissionModernDiagnosis: 入院西医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionModernDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param _PathologicalDiagnosis: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.PathologicalDiagnosisBlock`
        :param _DiseasePresent: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresent: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _SymptomsAndSigns: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSigns: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _AuxiliaryExamination: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _SpecialistExamination: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _MentalExamination: 精神检查
注意：此字段可能返回 null，表示取不到有效值。
        :type MentalExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _CheckRecord: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecord: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _InspectResult: 检查结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectResult: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _CheckAndTreatmentProcess: 治疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcess: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _SurgeryCondition: 手术经过
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryCondition: :class:`tencentcloud.mrs.v20200910.models.SurgeryConditionBlock`
        :param _IncisionHealing: 切口愈合
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealing: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DischargeDiagnosisBlock`
        :param _DischargeTraditionalDiagnosis: 出院中医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeTraditionalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _DischargeModernDiagnosis: 出院西医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeModernDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DischargeDiagnosisBlock`
        :param _DischargeCondition: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeCondition: :class:`tencentcloud.mrs.v20200910.models.DischargeConditionBlock`
        :param _DischargeInstructions: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructions: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _TreatmentSuggestion: 治疗建议
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentSuggestion: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _FollowUpRequirements: 随访
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUpRequirements: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _ConditionChanges: 治疗情况变化
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionChanges: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _PulmonaryArterySystolicPressure: 收缩压
注意：此字段可能返回 null，表示取不到有效值。
        :type PulmonaryArterySystolicPressure: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _BCLC: bclc分期
注意：此字段可能返回 null，表示取不到有效值。
        :type BCLC: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _PTNM: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.PTNMBlock`
        :param _ECOG: ECOG评分
注意：此字段可能返回 null，表示取不到有效值。
        :type ECOG: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _NRS: NRS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type NRS: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _KPS: kps评分
注意：此字段可能返回 null，表示取不到有效值。
        :type KPS: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param _Cancerstaging: 癌症分期
注意：此字段可能返回 null，表示取不到有效值。
        :type Cancerstaging: :class:`tencentcloud.mrs.v20200910.models.ClinicalStaging`
        :param _DeathDate: 死亡时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeathDate: :class:`tencentcloud.mrs.v20200910.models.DeathDateBlock`
        :param _RelapseDate: 复发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RelapseDate: :class:`tencentcloud.mrs.v20200910.models.RelapseDateBlock`
        :param _ObservationDays: 观察日期
注意：此字段可能返回 null，表示取不到有效值。
        :type ObservationDays: :class:`tencentcloud.mrs.v20200910.models.DeathDateBlock`
        :param _IncisionHealingText: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingText: str
        :param _AuxiliaryExaminationText: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExaminationText: str
        :param _SpecialExamText: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialExamText: str
        :param _OutpatientDiagnosisText: 门诊诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientDiagnosisText: str
        :param _AdmissionConditionText: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionConditionText: str
        :param _CheckAndTreatmentProcessText: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcessText: str
        :param _SymptomsAndSignsText: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSignsText: str
        :param _DischargeInstructionsText: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructionsText: str
        :param _AdmissionDiagnosisText: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosisText: str
        :param _SurgeryConditionText: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryConditionText: str
        :param _PathologicalDiagnosisText: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosisText: str
        :param _DischargeConditionText: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeConditionText: str
        :param _CheckRecordText: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecordText: str
        :param _ChiefComplaintText: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaintText: str
        :param _DischargeDiagnosisText: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosisText: str
        """
        self._Immunohistochemistry = None
        self._ChiefComplaint = None
        self._AdmissionCondition = None
        self._BodyExamination = None
        self._AdmissionDiagnosis = None
        self._AdmissionTraditionalDiagnosis = None
        self._AdmissionModernDiagnosis = None
        self._PathologicalDiagnosis = None
        self._DiseasePresent = None
        self._SymptomsAndSigns = None
        self._AuxiliaryExamination = None
        self._SpecialistExamination = None
        self._MentalExamination = None
        self._CheckRecord = None
        self._InspectResult = None
        self._CheckAndTreatmentProcess = None
        self._SurgeryCondition = None
        self._IncisionHealing = None
        self._DischargeDiagnosis = None
        self._DischargeTraditionalDiagnosis = None
        self._DischargeModernDiagnosis = None
        self._DischargeCondition = None
        self._DischargeInstructions = None
        self._TreatmentSuggestion = None
        self._FollowUpRequirements = None
        self._ConditionChanges = None
        self._PulmonaryArterySystolicPressure = None
        self._BCLC = None
        self._PTNM = None
        self._ECOG = None
        self._NRS = None
        self._KPS = None
        self._Cancerstaging = None
        self._DeathDate = None
        self._RelapseDate = None
        self._ObservationDays = None
        self._IncisionHealingText = None
        self._AuxiliaryExaminationText = None
        self._SpecialExamText = None
        self._OutpatientDiagnosisText = None
        self._AdmissionConditionText = None
        self._CheckAndTreatmentProcessText = None
        self._SymptomsAndSignsText = None
        self._DischargeInstructionsText = None
        self._AdmissionDiagnosisText = None
        self._SurgeryConditionText = None
        self._PathologicalDiagnosisText = None
        self._DischargeConditionText = None
        self._CheckRecordText = None
        self._ChiefComplaintText = None
        self._DischargeDiagnosisText = None

    @property
    def Immunohistochemistry(self):
        return self._Immunohistochemistry

    @Immunohistochemistry.setter
    def Immunohistochemistry(self, Immunohistochemistry):
        self._Immunohistochemistry = Immunohistochemistry

    @property
    def ChiefComplaint(self):
        return self._ChiefComplaint

    @ChiefComplaint.setter
    def ChiefComplaint(self, ChiefComplaint):
        self._ChiefComplaint = ChiefComplaint

    @property
    def AdmissionCondition(self):
        return self._AdmissionCondition

    @AdmissionCondition.setter
    def AdmissionCondition(self, AdmissionCondition):
        self._AdmissionCondition = AdmissionCondition

    @property
    def BodyExamination(self):
        return self._BodyExamination

    @BodyExamination.setter
    def BodyExamination(self, BodyExamination):
        self._BodyExamination = BodyExamination

    @property
    def AdmissionDiagnosis(self):
        return self._AdmissionDiagnosis

    @AdmissionDiagnosis.setter
    def AdmissionDiagnosis(self, AdmissionDiagnosis):
        self._AdmissionDiagnosis = AdmissionDiagnosis

    @property
    def AdmissionTraditionalDiagnosis(self):
        return self._AdmissionTraditionalDiagnosis

    @AdmissionTraditionalDiagnosis.setter
    def AdmissionTraditionalDiagnosis(self, AdmissionTraditionalDiagnosis):
        self._AdmissionTraditionalDiagnosis = AdmissionTraditionalDiagnosis

    @property
    def AdmissionModernDiagnosis(self):
        return self._AdmissionModernDiagnosis

    @AdmissionModernDiagnosis.setter
    def AdmissionModernDiagnosis(self, AdmissionModernDiagnosis):
        self._AdmissionModernDiagnosis = AdmissionModernDiagnosis

    @property
    def PathologicalDiagnosis(self):
        return self._PathologicalDiagnosis

    @PathologicalDiagnosis.setter
    def PathologicalDiagnosis(self, PathologicalDiagnosis):
        self._PathologicalDiagnosis = PathologicalDiagnosis

    @property
    def DiseasePresent(self):
        return self._DiseasePresent

    @DiseasePresent.setter
    def DiseasePresent(self, DiseasePresent):
        self._DiseasePresent = DiseasePresent

    @property
    def SymptomsAndSigns(self):
        return self._SymptomsAndSigns

    @SymptomsAndSigns.setter
    def SymptomsAndSigns(self, SymptomsAndSigns):
        self._SymptomsAndSigns = SymptomsAndSigns

    @property
    def AuxiliaryExamination(self):
        return self._AuxiliaryExamination

    @AuxiliaryExamination.setter
    def AuxiliaryExamination(self, AuxiliaryExamination):
        self._AuxiliaryExamination = AuxiliaryExamination

    @property
    def SpecialistExamination(self):
        return self._SpecialistExamination

    @SpecialistExamination.setter
    def SpecialistExamination(self, SpecialistExamination):
        self._SpecialistExamination = SpecialistExamination

    @property
    def MentalExamination(self):
        return self._MentalExamination

    @MentalExamination.setter
    def MentalExamination(self, MentalExamination):
        self._MentalExamination = MentalExamination

    @property
    def CheckRecord(self):
        return self._CheckRecord

    @CheckRecord.setter
    def CheckRecord(self, CheckRecord):
        self._CheckRecord = CheckRecord

    @property
    def InspectResult(self):
        return self._InspectResult

    @InspectResult.setter
    def InspectResult(self, InspectResult):
        self._InspectResult = InspectResult

    @property
    def CheckAndTreatmentProcess(self):
        return self._CheckAndTreatmentProcess

    @CheckAndTreatmentProcess.setter
    def CheckAndTreatmentProcess(self, CheckAndTreatmentProcess):
        self._CheckAndTreatmentProcess = CheckAndTreatmentProcess

    @property
    def SurgeryCondition(self):
        return self._SurgeryCondition

    @SurgeryCondition.setter
    def SurgeryCondition(self, SurgeryCondition):
        self._SurgeryCondition = SurgeryCondition

    @property
    def IncisionHealing(self):
        return self._IncisionHealing

    @IncisionHealing.setter
    def IncisionHealing(self, IncisionHealing):
        self._IncisionHealing = IncisionHealing

    @property
    def DischargeDiagnosis(self):
        return self._DischargeDiagnosis

    @DischargeDiagnosis.setter
    def DischargeDiagnosis(self, DischargeDiagnosis):
        self._DischargeDiagnosis = DischargeDiagnosis

    @property
    def DischargeTraditionalDiagnosis(self):
        return self._DischargeTraditionalDiagnosis

    @DischargeTraditionalDiagnosis.setter
    def DischargeTraditionalDiagnosis(self, DischargeTraditionalDiagnosis):
        self._DischargeTraditionalDiagnosis = DischargeTraditionalDiagnosis

    @property
    def DischargeModernDiagnosis(self):
        return self._DischargeModernDiagnosis

    @DischargeModernDiagnosis.setter
    def DischargeModernDiagnosis(self, DischargeModernDiagnosis):
        self._DischargeModernDiagnosis = DischargeModernDiagnosis

    @property
    def DischargeCondition(self):
        return self._DischargeCondition

    @DischargeCondition.setter
    def DischargeCondition(self, DischargeCondition):
        self._DischargeCondition = DischargeCondition

    @property
    def DischargeInstructions(self):
        return self._DischargeInstructions

    @DischargeInstructions.setter
    def DischargeInstructions(self, DischargeInstructions):
        self._DischargeInstructions = DischargeInstructions

    @property
    def TreatmentSuggestion(self):
        return self._TreatmentSuggestion

    @TreatmentSuggestion.setter
    def TreatmentSuggestion(self, TreatmentSuggestion):
        self._TreatmentSuggestion = TreatmentSuggestion

    @property
    def FollowUpRequirements(self):
        return self._FollowUpRequirements

    @FollowUpRequirements.setter
    def FollowUpRequirements(self, FollowUpRequirements):
        self._FollowUpRequirements = FollowUpRequirements

    @property
    def ConditionChanges(self):
        return self._ConditionChanges

    @ConditionChanges.setter
    def ConditionChanges(self, ConditionChanges):
        self._ConditionChanges = ConditionChanges

    @property
    def PulmonaryArterySystolicPressure(self):
        return self._PulmonaryArterySystolicPressure

    @PulmonaryArterySystolicPressure.setter
    def PulmonaryArterySystolicPressure(self, PulmonaryArterySystolicPressure):
        self._PulmonaryArterySystolicPressure = PulmonaryArterySystolicPressure

    @property
    def BCLC(self):
        return self._BCLC

    @BCLC.setter
    def BCLC(self, BCLC):
        self._BCLC = BCLC

    @property
    def PTNM(self):
        return self._PTNM

    @PTNM.setter
    def PTNM(self, PTNM):
        self._PTNM = PTNM

    @property
    def ECOG(self):
        return self._ECOG

    @ECOG.setter
    def ECOG(self, ECOG):
        self._ECOG = ECOG

    @property
    def NRS(self):
        return self._NRS

    @NRS.setter
    def NRS(self, NRS):
        self._NRS = NRS

    @property
    def KPS(self):
        return self._KPS

    @KPS.setter
    def KPS(self, KPS):
        self._KPS = KPS

    @property
    def Cancerstaging(self):
        return self._Cancerstaging

    @Cancerstaging.setter
    def Cancerstaging(self, Cancerstaging):
        self._Cancerstaging = Cancerstaging

    @property
    def DeathDate(self):
        return self._DeathDate

    @DeathDate.setter
    def DeathDate(self, DeathDate):
        self._DeathDate = DeathDate

    @property
    def RelapseDate(self):
        return self._RelapseDate

    @RelapseDate.setter
    def RelapseDate(self, RelapseDate):
        self._RelapseDate = RelapseDate

    @property
    def ObservationDays(self):
        return self._ObservationDays

    @ObservationDays.setter
    def ObservationDays(self, ObservationDays):
        self._ObservationDays = ObservationDays

    @property
    def IncisionHealingText(self):
        return self._IncisionHealingText

    @IncisionHealingText.setter
    def IncisionHealingText(self, IncisionHealingText):
        self._IncisionHealingText = IncisionHealingText

    @property
    def AuxiliaryExaminationText(self):
        return self._AuxiliaryExaminationText

    @AuxiliaryExaminationText.setter
    def AuxiliaryExaminationText(self, AuxiliaryExaminationText):
        self._AuxiliaryExaminationText = AuxiliaryExaminationText

    @property
    def SpecialExamText(self):
        return self._SpecialExamText

    @SpecialExamText.setter
    def SpecialExamText(self, SpecialExamText):
        self._SpecialExamText = SpecialExamText

    @property
    def OutpatientDiagnosisText(self):
        return self._OutpatientDiagnosisText

    @OutpatientDiagnosisText.setter
    def OutpatientDiagnosisText(self, OutpatientDiagnosisText):
        self._OutpatientDiagnosisText = OutpatientDiagnosisText

    @property
    def AdmissionConditionText(self):
        return self._AdmissionConditionText

    @AdmissionConditionText.setter
    def AdmissionConditionText(self, AdmissionConditionText):
        self._AdmissionConditionText = AdmissionConditionText

    @property
    def CheckAndTreatmentProcessText(self):
        return self._CheckAndTreatmentProcessText

    @CheckAndTreatmentProcessText.setter
    def CheckAndTreatmentProcessText(self, CheckAndTreatmentProcessText):
        self._CheckAndTreatmentProcessText = CheckAndTreatmentProcessText

    @property
    def SymptomsAndSignsText(self):
        return self._SymptomsAndSignsText

    @SymptomsAndSignsText.setter
    def SymptomsAndSignsText(self, SymptomsAndSignsText):
        self._SymptomsAndSignsText = SymptomsAndSignsText

    @property
    def DischargeInstructionsText(self):
        return self._DischargeInstructionsText

    @DischargeInstructionsText.setter
    def DischargeInstructionsText(self, DischargeInstructionsText):
        self._DischargeInstructionsText = DischargeInstructionsText

    @property
    def AdmissionDiagnosisText(self):
        return self._AdmissionDiagnosisText

    @AdmissionDiagnosisText.setter
    def AdmissionDiagnosisText(self, AdmissionDiagnosisText):
        self._AdmissionDiagnosisText = AdmissionDiagnosisText

    @property
    def SurgeryConditionText(self):
        return self._SurgeryConditionText

    @SurgeryConditionText.setter
    def SurgeryConditionText(self, SurgeryConditionText):
        self._SurgeryConditionText = SurgeryConditionText

    @property
    def PathologicalDiagnosisText(self):
        return self._PathologicalDiagnosisText

    @PathologicalDiagnosisText.setter
    def PathologicalDiagnosisText(self, PathologicalDiagnosisText):
        self._PathologicalDiagnosisText = PathologicalDiagnosisText

    @property
    def DischargeConditionText(self):
        return self._DischargeConditionText

    @DischargeConditionText.setter
    def DischargeConditionText(self, DischargeConditionText):
        self._DischargeConditionText = DischargeConditionText

    @property
    def CheckRecordText(self):
        return self._CheckRecordText

    @CheckRecordText.setter
    def CheckRecordText(self, CheckRecordText):
        self._CheckRecordText = CheckRecordText

    @property
    def ChiefComplaintText(self):
        return self._ChiefComplaintText

    @ChiefComplaintText.setter
    def ChiefComplaintText(self, ChiefComplaintText):
        self._ChiefComplaintText = ChiefComplaintText

    @property
    def DischargeDiagnosisText(self):
        return self._DischargeDiagnosisText

    @DischargeDiagnosisText.setter
    def DischargeDiagnosisText(self, DischargeDiagnosisText):
        self._DischargeDiagnosisText = DischargeDiagnosisText


    def _deserialize(self, params):
        if params.get("Immunohistochemistry") is not None:
            self._Immunohistochemistry = ImmunohistochemistryBlock()
            self._Immunohistochemistry._deserialize(params.get("Immunohistochemistry"))
        if params.get("ChiefComplaint") is not None:
            self._ChiefComplaint = ChiefComplaintBlock()
            self._ChiefComplaint._deserialize(params.get("ChiefComplaint"))
        if params.get("AdmissionCondition") is not None:
            self._AdmissionCondition = AdmissionConditionBlock()
            self._AdmissionCondition._deserialize(params.get("AdmissionCondition"))
        if params.get("BodyExamination") is not None:
            self._BodyExamination = BodyExaminationBlock()
            self._BodyExamination._deserialize(params.get("BodyExamination"))
        if params.get("AdmissionDiagnosis") is not None:
            self._AdmissionDiagnosis = AdmissionDiagnosisBlock()
            self._AdmissionDiagnosis._deserialize(params.get("AdmissionDiagnosis"))
        if params.get("AdmissionTraditionalDiagnosis") is not None:
            self._AdmissionTraditionalDiagnosis = AdmissionDiagnosisBlock()
            self._AdmissionTraditionalDiagnosis._deserialize(params.get("AdmissionTraditionalDiagnosis"))
        if params.get("AdmissionModernDiagnosis") is not None:
            self._AdmissionModernDiagnosis = AdmissionDiagnosisBlock()
            self._AdmissionModernDiagnosis._deserialize(params.get("AdmissionModernDiagnosis"))
        if params.get("PathologicalDiagnosis") is not None:
            self._PathologicalDiagnosis = PathologicalDiagnosisBlock()
            self._PathologicalDiagnosis._deserialize(params.get("PathologicalDiagnosis"))
        if params.get("DiseasePresent") is not None:
            self._DiseasePresent = DiseasePresentBlock()
            self._DiseasePresent._deserialize(params.get("DiseasePresent"))
        if params.get("SymptomsAndSigns") is not None:
            self._SymptomsAndSigns = DiseasePresentBlock()
            self._SymptomsAndSigns._deserialize(params.get("SymptomsAndSigns"))
        if params.get("AuxiliaryExamination") is not None:
            self._AuxiliaryExamination = DiseasePresentBlock()
            self._AuxiliaryExamination._deserialize(params.get("AuxiliaryExamination"))
        if params.get("SpecialistExamination") is not None:
            self._SpecialistExamination = DiseasePresentBlock()
            self._SpecialistExamination._deserialize(params.get("SpecialistExamination"))
        if params.get("MentalExamination") is not None:
            self._MentalExamination = DiseasePresentBlock()
            self._MentalExamination._deserialize(params.get("MentalExamination"))
        if params.get("CheckRecord") is not None:
            self._CheckRecord = DiseasePresentBlock()
            self._CheckRecord._deserialize(params.get("CheckRecord"))
        if params.get("InspectResult") is not None:
            self._InspectResult = DiseasePresentBlock()
            self._InspectResult._deserialize(params.get("InspectResult"))
        if params.get("CheckAndTreatmentProcess") is not None:
            self._CheckAndTreatmentProcess = DiseasePresentBlock()
            self._CheckAndTreatmentProcess._deserialize(params.get("CheckAndTreatmentProcess"))
        if params.get("SurgeryCondition") is not None:
            self._SurgeryCondition = SurgeryConditionBlock()
            self._SurgeryCondition._deserialize(params.get("SurgeryCondition"))
        if params.get("IncisionHealing") is not None:
            self._IncisionHealing = DiseasePresentBlock()
            self._IncisionHealing._deserialize(params.get("IncisionHealing"))
        if params.get("DischargeDiagnosis") is not None:
            self._DischargeDiagnosis = DischargeDiagnosisBlock()
            self._DischargeDiagnosis._deserialize(params.get("DischargeDiagnosis"))
        if params.get("DischargeTraditionalDiagnosis") is not None:
            self._DischargeTraditionalDiagnosis = DiseasePresentBlock()
            self._DischargeTraditionalDiagnosis._deserialize(params.get("DischargeTraditionalDiagnosis"))
        if params.get("DischargeModernDiagnosis") is not None:
            self._DischargeModernDiagnosis = DischargeDiagnosisBlock()
            self._DischargeModernDiagnosis._deserialize(params.get("DischargeModernDiagnosis"))
        if params.get("DischargeCondition") is not None:
            self._DischargeCondition = DischargeConditionBlock()
            self._DischargeCondition._deserialize(params.get("DischargeCondition"))
        if params.get("DischargeInstructions") is not None:
            self._DischargeInstructions = DiseasePresentBlock()
            self._DischargeInstructions._deserialize(params.get("DischargeInstructions"))
        if params.get("TreatmentSuggestion") is not None:
            self._TreatmentSuggestion = DiseasePresentBlock()
            self._TreatmentSuggestion._deserialize(params.get("TreatmentSuggestion"))
        if params.get("FollowUpRequirements") is not None:
            self._FollowUpRequirements = DiseasePresentBlock()
            self._FollowUpRequirements._deserialize(params.get("FollowUpRequirements"))
        if params.get("ConditionChanges") is not None:
            self._ConditionChanges = DiseasePresentBlock()
            self._ConditionChanges._deserialize(params.get("ConditionChanges"))
        if params.get("PulmonaryArterySystolicPressure") is not None:
            self._PulmonaryArterySystolicPressure = DiseasePresentBlock()
            self._PulmonaryArterySystolicPressure._deserialize(params.get("PulmonaryArterySystolicPressure"))
        if params.get("BCLC") is not None:
            self._BCLC = DiseasePresentBlock()
            self._BCLC._deserialize(params.get("BCLC"))
        if params.get("PTNM") is not None:
            self._PTNM = PTNMBlock()
            self._PTNM._deserialize(params.get("PTNM"))
        if params.get("ECOG") is not None:
            self._ECOG = DiseasePresentBlock()
            self._ECOG._deserialize(params.get("ECOG"))
        if params.get("NRS") is not None:
            self._NRS = DiseasePresentBlock()
            self._NRS._deserialize(params.get("NRS"))
        if params.get("KPS") is not None:
            self._KPS = DiseasePresentBlock()
            self._KPS._deserialize(params.get("KPS"))
        if params.get("Cancerstaging") is not None:
            self._Cancerstaging = ClinicalStaging()
            self._Cancerstaging._deserialize(params.get("Cancerstaging"))
        if params.get("DeathDate") is not None:
            self._DeathDate = DeathDateBlock()
            self._DeathDate._deserialize(params.get("DeathDate"))
        if params.get("RelapseDate") is not None:
            self._RelapseDate = RelapseDateBlock()
            self._RelapseDate._deserialize(params.get("RelapseDate"))
        if params.get("ObservationDays") is not None:
            self._ObservationDays = DeathDateBlock()
            self._ObservationDays._deserialize(params.get("ObservationDays"))
        self._IncisionHealingText = params.get("IncisionHealingText")
        self._AuxiliaryExaminationText = params.get("AuxiliaryExaminationText")
        self._SpecialExamText = params.get("SpecialExamText")
        self._OutpatientDiagnosisText = params.get("OutpatientDiagnosisText")
        self._AdmissionConditionText = params.get("AdmissionConditionText")
        self._CheckAndTreatmentProcessText = params.get("CheckAndTreatmentProcessText")
        self._SymptomsAndSignsText = params.get("SymptomsAndSignsText")
        self._DischargeInstructionsText = params.get("DischargeInstructionsText")
        self._AdmissionDiagnosisText = params.get("AdmissionDiagnosisText")
        self._SurgeryConditionText = params.get("SurgeryConditionText")
        self._PathologicalDiagnosisText = params.get("PathologicalDiagnosisText")
        self._DischargeConditionText = params.get("DischargeConditionText")
        self._CheckRecordText = params.get("CheckRecordText")
        self._ChiefComplaintText = params.get("ChiefComplaintText")
        self._DischargeDiagnosisText = params.get("DischargeDiagnosisText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TuberInfo(AbstractModel):
    """结节

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param _Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        :param _Multiple: 多发
注意：此字段可能返回 null，表示取不到有效值。
        :type Multiple: :class:`tencentcloud.mrs.v20200910.models.Multiple`
        :param _AspectRatio: 纵横比
注意：此字段可能返回 null，表示取不到有效值。
        :type AspectRatio: :class:`tencentcloud.mrs.v20200910.models.AspectRatio`
        :param _Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。
        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _RearEcho: 外部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type RearEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Elastic: 弹性质地
注意：此字段可能返回 null，表示取不到有效值。
        :type Elastic: :class:`tencentcloud.mrs.v20200910.models.Elastic`
        :param _Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。
        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _SkinMedulla: 皮髓质信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SkinMedulla: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Trend: 变化趋势
注意：此字段可能返回 null，表示取不到有效值。
        :type Trend: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Calcification: 钙化
注意：此字段可能返回 null，表示取不到有效值。
        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Enhancement: 强化
注意：此字段可能返回 null，表示取不到有效值。
        :type Enhancement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _LymphEnlargement: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphEnlargement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _LymphDoor: 淋巴门
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphDoor: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Activity: 活动度
注意：此字段可能返回 null，表示取不到有效值。
        :type Activity: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Operation: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。
        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param _SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _InnerEchoType: 内部回声类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoType: list of BlockInfo
        :param _Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。
        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Density: 密度
注意：此字段可能返回 null，表示取不到有效值。
        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。
        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。
        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`
        :param _Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param _Transparent: 透声度
注意：此字段可能返回 null，表示取不到有效值。
        :type Transparent: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriAdc: MRI ADC
注意：此字段可能返回 null，表示取不到有效值。
        :type MriAdc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriDwi: MRI DWI
注意：此字段可能返回 null，表示取不到有效值。
        :type MriDwi: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriT1: MRI T1信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT1: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _MriT2: MRI T2信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT2: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _CtHu: CT HU值
注意：此字段可能返回 null，表示取不到有效值。
        :type CtHu: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Suvmax: SUmax值
注意：此字段可能返回 null，表示取不到有效值。
        :type Suvmax: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Metabolism: 代谢情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Metabolism: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _RadioactiveUptake: 放射性摄取
注意：此字段可能返回 null，表示取不到有效值。
        :type RadioactiveUptake: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _SymDesc: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDesc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _ImageFeature: 影像特征
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageFeature: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param _Coords: 在报告图片中的坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self._Type = None
        self._Part = None
        self._Size = None
        self._Multiple = None
        self._AspectRatio = None
        self._Edge = None
        self._InnerEcho = None
        self._RearEcho = None
        self._Elastic = None
        self._Shape = None
        self._ShapeAttr = None
        self._SkinMedulla = None
        self._Trend = None
        self._Calcification = None
        self._Envelope = None
        self._Enhancement = None
        self._LymphEnlargement = None
        self._LymphDoor = None
        self._Activity = None
        self._Operation = None
        self._CDFI = None
        self._Index = None
        self._SizeStatus = None
        self._InnerEchoDistribution = None
        self._InnerEchoType = None
        self._Outline = None
        self._Structure = None
        self._Density = None
        self._Vas = None
        self._Cysticwall = None
        self._Capsule = None
        self._IsthmusThicknese = None
        self._Src = None
        self._Transparent = None
        self._MriAdc = None
        self._MriDwi = None
        self._MriT1 = None
        self._MriT2 = None
        self._CtHu = None
        self._Suvmax = None
        self._Metabolism = None
        self._RadioactiveUptake = None
        self._SymDesc = None
        self._ImageFeature = None
        self._Coords = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Part(self):
        return self._Part

    @Part.setter
    def Part(self, Part):
        self._Part = Part

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Multiple(self):
        return self._Multiple

    @Multiple.setter
    def Multiple(self, Multiple):
        self._Multiple = Multiple

    @property
    def AspectRatio(self):
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Edge(self):
        return self._Edge

    @Edge.setter
    def Edge(self, Edge):
        self._Edge = Edge

    @property
    def InnerEcho(self):
        return self._InnerEcho

    @InnerEcho.setter
    def InnerEcho(self, InnerEcho):
        self._InnerEcho = InnerEcho

    @property
    def RearEcho(self):
        return self._RearEcho

    @RearEcho.setter
    def RearEcho(self, RearEcho):
        self._RearEcho = RearEcho

    @property
    def Elastic(self):
        return self._Elastic

    @Elastic.setter
    def Elastic(self, Elastic):
        self._Elastic = Elastic

    @property
    def Shape(self):
        return self._Shape

    @Shape.setter
    def Shape(self, Shape):
        self._Shape = Shape

    @property
    def ShapeAttr(self):
        return self._ShapeAttr

    @ShapeAttr.setter
    def ShapeAttr(self, ShapeAttr):
        self._ShapeAttr = ShapeAttr

    @property
    def SkinMedulla(self):
        return self._SkinMedulla

    @SkinMedulla.setter
    def SkinMedulla(self, SkinMedulla):
        self._SkinMedulla = SkinMedulla

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def Calcification(self):
        return self._Calcification

    @Calcification.setter
    def Calcification(self, Calcification):
        self._Calcification = Calcification

    @property
    def Envelope(self):
        return self._Envelope

    @Envelope.setter
    def Envelope(self, Envelope):
        self._Envelope = Envelope

    @property
    def Enhancement(self):
        return self._Enhancement

    @Enhancement.setter
    def Enhancement(self, Enhancement):
        self._Enhancement = Enhancement

    @property
    def LymphEnlargement(self):
        return self._LymphEnlargement

    @LymphEnlargement.setter
    def LymphEnlargement(self, LymphEnlargement):
        self._LymphEnlargement = LymphEnlargement

    @property
    def LymphDoor(self):
        return self._LymphDoor

    @LymphDoor.setter
    def LymphDoor(self, LymphDoor):
        self._LymphDoor = LymphDoor

    @property
    def Activity(self):
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def CDFI(self):
        return self._CDFI

    @CDFI.setter
    def CDFI(self, CDFI):
        self._CDFI = CDFI

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def SizeStatus(self):
        return self._SizeStatus

    @SizeStatus.setter
    def SizeStatus(self, SizeStatus):
        self._SizeStatus = SizeStatus

    @property
    def InnerEchoDistribution(self):
        return self._InnerEchoDistribution

    @InnerEchoDistribution.setter
    def InnerEchoDistribution(self, InnerEchoDistribution):
        self._InnerEchoDistribution = InnerEchoDistribution

    @property
    def InnerEchoType(self):
        return self._InnerEchoType

    @InnerEchoType.setter
    def InnerEchoType(self, InnerEchoType):
        self._InnerEchoType = InnerEchoType

    @property
    def Outline(self):
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline

    @property
    def Structure(self):
        return self._Structure

    @Structure.setter
    def Structure(self, Structure):
        self._Structure = Structure

    @property
    def Density(self):
        return self._Density

    @Density.setter
    def Density(self, Density):
        self._Density = Density

    @property
    def Vas(self):
        return self._Vas

    @Vas.setter
    def Vas(self, Vas):
        self._Vas = Vas

    @property
    def Cysticwall(self):
        return self._Cysticwall

    @Cysticwall.setter
    def Cysticwall(self, Cysticwall):
        self._Cysticwall = Cysticwall

    @property
    def Capsule(self):
        return self._Capsule

    @Capsule.setter
    def Capsule(self, Capsule):
        self._Capsule = Capsule

    @property
    def IsthmusThicknese(self):
        return self._IsthmusThicknese

    @IsthmusThicknese.setter
    def IsthmusThicknese(self, IsthmusThicknese):
        self._IsthmusThicknese = IsthmusThicknese

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Transparent(self):
        return self._Transparent

    @Transparent.setter
    def Transparent(self, Transparent):
        self._Transparent = Transparent

    @property
    def MriAdc(self):
        return self._MriAdc

    @MriAdc.setter
    def MriAdc(self, MriAdc):
        self._MriAdc = MriAdc

    @property
    def MriDwi(self):
        return self._MriDwi

    @MriDwi.setter
    def MriDwi(self, MriDwi):
        self._MriDwi = MriDwi

    @property
    def MriT1(self):
        return self._MriT1

    @MriT1.setter
    def MriT1(self, MriT1):
        self._MriT1 = MriT1

    @property
    def MriT2(self):
        return self._MriT2

    @MriT2.setter
    def MriT2(self, MriT2):
        self._MriT2 = MriT2

    @property
    def CtHu(self):
        return self._CtHu

    @CtHu.setter
    def CtHu(self, CtHu):
        self._CtHu = CtHu

    @property
    def Suvmax(self):
        return self._Suvmax

    @Suvmax.setter
    def Suvmax(self, Suvmax):
        self._Suvmax = Suvmax

    @property
    def Metabolism(self):
        return self._Metabolism

    @Metabolism.setter
    def Metabolism(self, Metabolism):
        self._Metabolism = Metabolism

    @property
    def RadioactiveUptake(self):
        return self._RadioactiveUptake

    @RadioactiveUptake.setter
    def RadioactiveUptake(self, RadioactiveUptake):
        self._RadioactiveUptake = RadioactiveUptake

    @property
    def SymDesc(self):
        return self._SymDesc

    @SymDesc.setter
    def SymDesc(self, SymDesc):
        self._SymDesc = SymDesc

    @property
    def ImageFeature(self):
        return self._ImageFeature

    @ImageFeature.setter
    def ImageFeature(self, ImageFeature):
        self._ImageFeature = ImageFeature

    @property
    def Coords(self):
        return self._Coords

    @Coords.setter
    def Coords(self, Coords):
        self._Coords = Coords


    def _deserialize(self, params):
        if params.get("Type") is not None:
            self._Type = BlockInfo()
            self._Type._deserialize(params.get("Type"))
        if params.get("Part") is not None:
            self._Part = Part()
            self._Part._deserialize(params.get("Part"))
        if params.get("Size") is not None:
            self._Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self._Size.append(obj)
        if params.get("Multiple") is not None:
            self._Multiple = Multiple()
            self._Multiple._deserialize(params.get("Multiple"))
        if params.get("AspectRatio") is not None:
            self._AspectRatio = AspectRatio()
            self._AspectRatio._deserialize(params.get("AspectRatio"))
        if params.get("Edge") is not None:
            self._Edge = BlockInfo()
            self._Edge._deserialize(params.get("Edge"))
        if params.get("InnerEcho") is not None:
            self._InnerEcho = BlockInfo()
            self._InnerEcho._deserialize(params.get("InnerEcho"))
        if params.get("RearEcho") is not None:
            self._RearEcho = BlockInfo()
            self._RearEcho._deserialize(params.get("RearEcho"))
        if params.get("Elastic") is not None:
            self._Elastic = Elastic()
            self._Elastic._deserialize(params.get("Elastic"))
        if params.get("Shape") is not None:
            self._Shape = BlockInfo()
            self._Shape._deserialize(params.get("Shape"))
        if params.get("ShapeAttr") is not None:
            self._ShapeAttr = BlockInfo()
            self._ShapeAttr._deserialize(params.get("ShapeAttr"))
        if params.get("SkinMedulla") is not None:
            self._SkinMedulla = BlockInfo()
            self._SkinMedulla._deserialize(params.get("SkinMedulla"))
        if params.get("Trend") is not None:
            self._Trend = BlockInfo()
            self._Trend._deserialize(params.get("Trend"))
        if params.get("Calcification") is not None:
            self._Calcification = BlockInfo()
            self._Calcification._deserialize(params.get("Calcification"))
        if params.get("Envelope") is not None:
            self._Envelope = BlockInfo()
            self._Envelope._deserialize(params.get("Envelope"))
        if params.get("Enhancement") is not None:
            self._Enhancement = BlockInfo()
            self._Enhancement._deserialize(params.get("Enhancement"))
        if params.get("LymphEnlargement") is not None:
            self._LymphEnlargement = BlockInfo()
            self._LymphEnlargement._deserialize(params.get("LymphEnlargement"))
        if params.get("LymphDoor") is not None:
            self._LymphDoor = BlockInfo()
            self._LymphDoor._deserialize(params.get("LymphDoor"))
        if params.get("Activity") is not None:
            self._Activity = BlockInfo()
            self._Activity._deserialize(params.get("Activity"))
        if params.get("Operation") is not None:
            self._Operation = BlockInfo()
            self._Operation._deserialize(params.get("Operation"))
        if params.get("CDFI") is not None:
            self._CDFI = BlockInfo()
            self._CDFI._deserialize(params.get("CDFI"))
        self._Index = params.get("Index")
        if params.get("SizeStatus") is not None:
            self._SizeStatus = BlockInfo()
            self._SizeStatus._deserialize(params.get("SizeStatus"))
        if params.get("InnerEchoDistribution") is not None:
            self._InnerEchoDistribution = BlockInfo()
            self._InnerEchoDistribution._deserialize(params.get("InnerEchoDistribution"))
        if params.get("InnerEchoType") is not None:
            self._InnerEchoType = []
            for item in params.get("InnerEchoType"):
                obj = BlockInfo()
                obj._deserialize(item)
                self._InnerEchoType.append(obj)
        if params.get("Outline") is not None:
            self._Outline = BlockInfo()
            self._Outline._deserialize(params.get("Outline"))
        if params.get("Structure") is not None:
            self._Structure = BlockInfo()
            self._Structure._deserialize(params.get("Structure"))
        if params.get("Density") is not None:
            self._Density = BlockInfo()
            self._Density._deserialize(params.get("Density"))
        if params.get("Vas") is not None:
            self._Vas = BlockInfo()
            self._Vas._deserialize(params.get("Vas"))
        if params.get("Cysticwall") is not None:
            self._Cysticwall = BlockInfo()
            self._Cysticwall._deserialize(params.get("Cysticwall"))
        if params.get("Capsule") is not None:
            self._Capsule = BlockInfo()
            self._Capsule._deserialize(params.get("Capsule"))
        if params.get("IsthmusThicknese") is not None:
            self._IsthmusThicknese = Size()
            self._IsthmusThicknese._deserialize(params.get("IsthmusThicknese"))
        self._Src = params.get("Src")
        if params.get("Transparent") is not None:
            self._Transparent = BlockInfo()
            self._Transparent._deserialize(params.get("Transparent"))
        if params.get("MriAdc") is not None:
            self._MriAdc = BlockInfo()
            self._MriAdc._deserialize(params.get("MriAdc"))
        if params.get("MriDwi") is not None:
            self._MriDwi = BlockInfo()
            self._MriDwi._deserialize(params.get("MriDwi"))
        if params.get("MriT1") is not None:
            self._MriT1 = BlockInfo()
            self._MriT1._deserialize(params.get("MriT1"))
        if params.get("MriT2") is not None:
            self._MriT2 = BlockInfo()
            self._MriT2._deserialize(params.get("MriT2"))
        if params.get("CtHu") is not None:
            self._CtHu = BlockInfo()
            self._CtHu._deserialize(params.get("CtHu"))
        if params.get("Suvmax") is not None:
            self._Suvmax = BlockInfo()
            self._Suvmax._deserialize(params.get("Suvmax"))
        if params.get("Metabolism") is not None:
            self._Metabolism = BlockInfo()
            self._Metabolism._deserialize(params.get("Metabolism"))
        if params.get("RadioactiveUptake") is not None:
            self._RadioactiveUptake = BlockInfo()
            self._RadioactiveUptake._deserialize(params.get("RadioactiveUptake"))
        if params.get("SymDesc") is not None:
            self._SymDesc = BlockInfo()
            self._SymDesc._deserialize(params.get("SymDesc"))
        if params.get("ImageFeature") is not None:
            self._ImageFeature = BlockInfo()
            self._ImageFeature._deserialize(params.get("ImageFeature"))
        if params.get("Coords") is not None:
            self._Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self._Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vaccination(AbstractModel):
    """免疫接种记录

    """

    def __init__(self):
        r"""
        :param _Id: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Vaccine: 疫苗名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Vaccine: str
        :param _Dose: 剂次
注意：此字段可能返回 null，表示取不到有效值。
        :type Dose: str
        :param _Date: 接种日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param _LotNumber: 疫苗批号
注意：此字段可能返回 null，表示取不到有效值。
        :type LotNumber: str
        :param _Manufacturer: 生产企业
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        :param _Clinic: 接种单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Clinic: str
        :param _Site: 接种部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Site: str
        :param _Provider: 接种者
注意：此字段可能返回 null，表示取不到有效值。
        :type Provider: str
        :param _Lot: 疫苗批号
注意：此字段可能返回 null，表示取不到有效值。
        :type Lot: str
        """
        self._Id = None
        self._Vaccine = None
        self._Dose = None
        self._Date = None
        self._LotNumber = None
        self._Manufacturer = None
        self._Clinic = None
        self._Site = None
        self._Provider = None
        self._Lot = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vaccine(self):
        return self._Vaccine

    @Vaccine.setter
    def Vaccine(self, Vaccine):
        self._Vaccine = Vaccine

    @property
    def Dose(self):
        return self._Dose

    @Dose.setter
    def Dose(self, Dose):
        self._Dose = Dose

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def LotNumber(self):
        return self._LotNumber

    @LotNumber.setter
    def LotNumber(self, LotNumber):
        self._LotNumber = LotNumber

    @property
    def Manufacturer(self):
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def Clinic(self):
        return self._Clinic

    @Clinic.setter
    def Clinic(self, Clinic):
        self._Clinic = Clinic

    @property
    def Site(self):
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def Provider(self):
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Lot(self):
        return self._Lot

    @Lot.setter
    def Lot(self, Lot):
        self._Lot = Lot


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Vaccine = params.get("Vaccine")
        self._Dose = params.get("Dose")
        self._Date = params.get("Date")
        self._LotNumber = params.get("LotNumber")
        self._Manufacturer = params.get("Manufacturer")
        self._Clinic = params.get("Clinic")
        self._Site = params.get("Site")
        self._Provider = params.get("Provider")
        self._Lot = params.get("Lot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VaccineCertificate(AbstractModel):
    """免疫接种证明

    """

    def __init__(self):
        r"""
        :param _VaccineList: 免疫接种列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VaccineList: list of Vaccination
        """
        self._VaccineList = None

    @property
    def VaccineList(self):
        return self._VaccineList

    @VaccineList.setter
    def VaccineList(self, VaccineList):
        self._VaccineList = VaccineList


    def _deserialize(self, params):
        if params.get("VaccineList") is not None:
            self._VaccineList = []
            for item in params.get("VaccineList"):
                obj = Vaccination()
                obj._deserialize(item)
                self._VaccineList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    """值

    """

    def __init__(self):
        r"""
        :param _Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param _Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: list of float
        :param _Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        """
        self._Grade = None
        self._Percent = None
        self._Positive = None

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive


    def _deserialize(self, params):
        self._Grade = params.get("Grade")
        self._Percent = params.get("Percent")
        self._Positive = params.get("Positive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueBlock(AbstractModel):
    """值块

    """

    def __init__(self):
        r"""
        :param _Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param _Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: list of float
        :param _Positive: 阳性阴性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        """
        self._Grade = None
        self._Percent = None
        self._Positive = None

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive


    def _deserialize(self, params):
        self._Grade = params.get("Grade")
        self._Percent = params.get("Percent")
        self._Positive = params.get("Positive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        