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


class Account(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        r"""
        :param _User: New account name
        :type User: str
        :param _Host: New account domain name
        :type Host: str
        """
        self._User = None
        self._Host = None

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    """Account details

    """

    def __init__(self):
        r"""
        :param _Notes: Account remarks
        :type Notes: str
        :param _Host: Account domain name
        :type Host: str
        :param _User: Account name
        :type User: str
        :param _ModifyTime: Account information modification time
        :type ModifyTime: str
        :param _ModifyPasswordTime: Password modification time
        :type ModifyPasswordTime: str
        :param _CreateTime: This parameter is deprecated.
        :type CreateTime: str
        :param _MaxUserConnections: The maximum number of instance connections supported by an account
        :type MaxUserConnections: int
        """
        self._Notes = None
        self._Host = None
        self._User = None
        self._ModifyTime = None
        self._ModifyPasswordTime = None
        self._CreateTime = None
        self._MaxUserConnections = None

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyPasswordTime(self):
        return self._ModifyPasswordTime

    @ModifyPasswordTime.setter
    def ModifyPasswordTime(self, ModifyPasswordTime):
        self._ModifyPasswordTime = ModifyPasswordTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._Notes = params.get("Notes")
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyPasswordTime = params.get("ModifyPasswordTime")
        self._CreateTime = params.get("CreateTime")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowRequest(AbstractModel):
    """AddTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Monday: Maintenance window on Monday. The format should be 10:00-12:00. You can set multiple time windows on a day. Each time window lasts from half an hour to three hours, and must start and end on the hour or half hour. At least one time window is required in a week. The same rule applies to the following parameters.
        :type Monday: list of str
        :param _Tuesday: Maintenance window on Tuesday. At least one time window is required in a week.
        :type Tuesday: list of str
        :param _Wednesday: Maintenance window on Wednesday. At least one time window is required in a week.
        :type Wednesday: list of str
        :param _Thursday: Maintenance window on Thursday. At least one time window is required in a week.
        :type Thursday: list of str
        :param _Friday: Maintenance window on Friday. At least one time window is required in a week.
        :type Friday: list of str
        :param _Saturday: Maintenance window on Saturday. At least one time window is required in a week.
        :type Saturday: list of str
        :param _Sunday: Maintenance window on Sunday. At least one time window is required in a week.
        :type Sunday: list of str
        :param _MaxDelayTime: Maximum delay threshold, which takes effect only for source instances and disaster recovery instances.
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowResponse(AbstractModel):
    """AddTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Address(AbstractModel):
    """Address

    """

    def __init__(self):
        r"""
        :param _Vip: Address
Note: this field may return `null`, indicating that no valid value can be found.
        :type Vip: str
        :param _VPort: Port
Note: this field may return `null`, indicating that no valid value can be found.
        :type VPort: int
        :param _UniqVpcId: VPC ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type UniqVpcId: str
        :param _UniqSubnet: VPC subnet ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type UniqSubnet: str
        :param _Desc: Description
Note: this field may return `null`, indicating that no valid value can be found.
        :type Desc: str
        """
        self._Vip = None
        self._VPort = None
        self._UniqVpcId = None
        self._UniqSubnet = None
        self._Desc = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnet(self):
        return self._UniqSubnet

    @UniqSubnet.setter
    def UniqSubnet(self, UniqSubnet):
        self._UniqSubnet = UniqSubnet

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnet = params.get("UniqSubnet")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustCdbProxyAddressRequest(AbstractModel):
    """AdjustCdbProxyAddress request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _WeightMode: Assignment mode of weights. Valid values: `system` (auto-assigned), `custom`.
        :type WeightMode: str
        :param _IsKickOut: Whether to remove delayed read-only instances from the proxy group Valid values: `true`, `false`.
        :type IsKickOut: bool
        :param _MinCount: Least read-only instances. Minimum value:  `0`
        :type MinCount: int
        :param _MaxDelay: The delay threshold. Minimum value:  `0`
        :type MaxDelay: int
        :param _FailOver: Whether to enable failover. Valid values: `true`, `false`.
        :type FailOver: bool
        :param _AutoAddRo: Whether to automatically add newly created read-only instances. Valid values: `true`, `false`.
        :type AutoAddRo: bool
        :param _ReadOnly: Whether it is read-only. Valid values: `true`, `false`.
        :type ReadOnly: bool
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        :param _TransSplit: Whether to enable transaction splitting. Valid values: `true`, `false`.
        :type TransSplit: bool
        :param _ConnectionPool: Whether to enable the connection pool
        :type ConnectionPool: bool
        :param _ProxyAllocation: Assignment of read/write weights If `system` is passed in for `WeightMode`, only the default weight assigned by the system will take effect.
        :type ProxyAllocation: list of ProxyAllocation
        """
        self._ProxyGroupId = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._ProxyAddressId = None
        self._TransSplit = None
        self._ConnectionPool = None
        self._ProxyAllocation = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._TransSplit = params.get("TransSplit")
        self._ConnectionPool = params.get("ConnectionPool")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustCdbProxyAddressResponse(AbstractModel):
    """AdjustCdbProxyAddress response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class AdjustCdbProxyRequest(AbstractModel):
    """AdjustCdbProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyNodeCustom: The specification configuration of a node
        :type ProxyNodeCustom: list of ProxyNodeCustom
        :param _ReloadBalance: Rebalance. Valid values:  `auto` (automatic), `manual` (manual).
        :type ReloadBalance: str
        :param _UpgradeTime: The upgrade switch time. Valid values:  `nowTime` (upgrade immediately), `timeWindow` (upgrade during instance maintenance time).
        :type UpgradeTime: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._ProxyNodeCustom = None
        self._ReloadBalance = None
        self._UpgradeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyNodeCustom(self):
        return self._ProxyNodeCustom

    @ProxyNodeCustom.setter
    def ProxyNodeCustom(self, ProxyNodeCustom):
        self._ProxyNodeCustom = ProxyNodeCustom

    @property
    def ReloadBalance(self):
        return self._ReloadBalance

    @ReloadBalance.setter
    def ReloadBalance(self, ReloadBalance):
        self._ReloadBalance = ReloadBalance

    @property
    def UpgradeTime(self):
        return self._UpgradeTime

    @UpgradeTime.setter
    def UpgradeTime(self, UpgradeTime):
        self._UpgradeTime = UpgradeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        if params.get("ProxyNodeCustom") is not None:
            self._ProxyNodeCustom = []
            for item in params.get("ProxyNodeCustom"):
                obj = ProxyNodeCustom()
                obj._deserialize(item)
                self._ProxyNodeCustom.append(obj)
        self._ReloadBalance = params.get("ReloadBalance")
        self._UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustCdbProxyResponse(AbstractModel):
    """AdjustCdbProxy response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class AggregationCondition(AbstractModel):
    """Aggregation condition for an audit log

    """

    def __init__(self):
        r"""
        :param _AggregationField: Aggregation field. Valid values: `host` (source IP), `user` （username), `dbName` (database name), `sqlType` (SQL type).
        :type AggregationField: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number of buckets returned under this field. Maximum value: `100`.
        :type Limit: int
        """
        self._AggregationField = None
        self._Offset = None
        self._Limit = None

    @property
    def AggregationField(self):
        return self._AggregationField

    @AggregationField.setter
    def AggregationField(self, AggregationField):
        self._AggregationField = AggregationField

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AggregationField = params.get("AggregationField")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeAuditLogsRequest(AbstractModel):
    """AnalyzeAuditLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Start time of the log to be analyzed in the format of `2023-02-16 00:00:20`.
        :type StartTime: str
        :param _EndTime: End time of the log to be analyzed in the format of `2023-02-16 00:00:20`.
        :type EndTime: str
        :param _AggregationConditions: Sorting conditions for aggregation dimension
        :type AggregationConditions: list of AggregationCondition
        :param _AuditLogFilter: The result set of the audit log filtered by this condition is set as the analysis Log.
        :type AuditLogFilter: :class:`tencentcloud.cdb.v20170320.models.AuditLogFilter`
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._AggregationConditions = None
        self._AuditLogFilter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def AggregationConditions(self):
        return self._AggregationConditions

    @AggregationConditions.setter
    def AggregationConditions(self, AggregationConditions):
        self._AggregationConditions = AggregationConditions

    @property
    def AuditLogFilter(self):
        return self._AuditLogFilter

    @AuditLogFilter.setter
    def AuditLogFilter(self, AuditLogFilter):
        self._AuditLogFilter = AuditLogFilter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("AggregationConditions") is not None:
            self._AggregationConditions = []
            for item in params.get("AggregationConditions"):
                obj = AggregationCondition()
                obj._deserialize(item)
                self._AggregationConditions.append(obj)
        if params.get("AuditLogFilter") is not None:
            self._AuditLogFilter = AuditLogFilter()
            self._AuditLogFilter._deserialize(params.get("AuditLogFilter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeAuditLogsResponse(AbstractModel):
    """AnalyzeAuditLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Information set of the aggregation bucket returned
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of AuditLogAggregationResult
        :param _TotalCount: Number of scanned logs
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditLogAggregationResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _InstanceIds: List of instance IDs, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        :param _ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be bound to the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be bound to the read-only replicas themselves.
        :type ForReadonlyInstance: bool
        """
        self._SecurityGroupId = None
        self._InstanceIds = None
        self._ForReadonlyInstance = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AuditFilter(AbstractModel):
    """Audit rule filters

    """

    def __init__(self):
        r"""
        :param _Type: Filter parameter names. Valid values:
SrcIp: Client IP;
User: Database account;
DB: Database name.
        :type Type: str
        :param _Compare: Filter match type. Valid value:
`INC`: Include;
`EXC`: Exclude;
`EQ`: Equal to;
`NEQ`: Not equal to.
        :type Compare: str
        :param _Value: Filter match value
        :type Value: str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogAggregationResult(AbstractModel):
    """Analysis result of an audit log

    """

    def __init__(self):
        r"""
        :param _AggregationField: Aggregation dimension
Note: This field may return null, indicating that no valid values can be obtained.
        :type AggregationField: str
        :param _Buckets: Result set of an aggregation bucket
Note: This field may return null, indicating that no valid values can be obtained.
        :type Buckets: list of Bucket
        """
        self._AggregationField = None
        self._Buckets = None

    @property
    def AggregationField(self):
        return self._AggregationField

    @AggregationField.setter
    def AggregationField(self, AggregationField):
        self._AggregationField = AggregationField

    @property
    def Buckets(self):
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets


    def _deserialize(self, params):
        self._AggregationField = params.get("AggregationField")
        if params.get("Buckets") is not None:
            self._Buckets = []
            for item in params.get("Buckets"):
                obj = Bucket()
                obj._deserialize(item)
                self._Buckets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """Filter condition for an audit log, which is used by users to filter the returned audit logs when querying them.

    """

    def __init__(self):
        r"""
        :param _Host: Client address
        :type Host: list of str
        :param _User: Username
        :type User: list of str
        :param _DBName: 
        :type DBName: list of str
        :param _TableName: Table name
        :type TableName: list of str
        :param _PolicyName: Audit policy name
        :type PolicyName: list of str
        :param _Sql: 
        :type Sql: str
        :param _SqlType: 
        :type SqlType: str
        :param _ExecTime: Execution time in ms, which is used to filter the audit log with execution time greater than this value.
        :type ExecTime: int
        :param _AffectRows: Number of affected rows, which is used to filter the audit log with affected rows greater than this value.
        :type AffectRows: int
        :param _SqlTypes: SQL type (Multiple types can be queried at same time). Valid values: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `ALTER`, `SET`, `REPLACE`, `EXECUTE`.
        :type SqlTypes: list of str
        :param _Sqls: SQL statement. Multiple SQL statements can be passed in.
        :type Sqls: list of str
        :param _AffectRowsSection: Number of rows affected in the format of M-N, such as 10-200.
        :type AffectRowsSection: str
        :param _SentRowsSection: Number of rows returned in the format of M-N, such as 10-200.
        :type SentRowsSection: str
        :param _ExecTimeSection: Execution time in the format of M-N, such as 10-200.
        :type ExecTimeSection: str
        :param _LockWaitTimeSection: Lock wait time in the format of M-N, such as 10-200.
        :type LockWaitTimeSection: str
        :param _IoWaitTimeSection: IO wait time in the format of M-N, such as 10-200.
        :type IoWaitTimeSection: str
        :param _TransactionLivingTimeSection: Transaction duration in the format of M-N, such as 10-200.
        :type TransactionLivingTimeSection: str
        :param _ThreadId: Thread ID
        :type ThreadId: list of str
        :param _SentRows: Number of returned rows,  which is used to filter the audit log with affected rows greater than this value.
        :type SentRows: int
        :param _ErrCode: MySQL error codes
        :type ErrCode: list of int
        """
        self._Host = None
        self._User = None
        self._DBName = None
        self._TableName = None
        self._PolicyName = None
        self._Sql = None
        self._SqlType = None
        self._ExecTime = None
        self._AffectRows = None
        self._SqlTypes = None
        self._Sqls = None
        self._AffectRowsSection = None
        self._SentRowsSection = None
        self._ExecTimeSection = None
        self._LockWaitTimeSection = None
        self._IoWaitTimeSection = None
        self._TransactionLivingTimeSection = None
        self._ThreadId = None
        self._SentRows = None
        self._ErrCode = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Sql(self):
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def SqlType(self):
        return self._SqlType

    @SqlType.setter
    def SqlType(self, SqlType):
        self._SqlType = SqlType

    @property
    def ExecTime(self):
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def AffectRows(self):
        return self._AffectRows

    @AffectRows.setter
    def AffectRows(self, AffectRows):
        self._AffectRows = AffectRows

    @property
    def SqlTypes(self):
        return self._SqlTypes

    @SqlTypes.setter
    def SqlTypes(self, SqlTypes):
        self._SqlTypes = SqlTypes

    @property
    def Sqls(self):
        return self._Sqls

    @Sqls.setter
    def Sqls(self, Sqls):
        self._Sqls = Sqls

    @property
    def AffectRowsSection(self):
        return self._AffectRowsSection

    @AffectRowsSection.setter
    def AffectRowsSection(self, AffectRowsSection):
        self._AffectRowsSection = AffectRowsSection

    @property
    def SentRowsSection(self):
        return self._SentRowsSection

    @SentRowsSection.setter
    def SentRowsSection(self, SentRowsSection):
        self._SentRowsSection = SentRowsSection

    @property
    def ExecTimeSection(self):
        return self._ExecTimeSection

    @ExecTimeSection.setter
    def ExecTimeSection(self, ExecTimeSection):
        self._ExecTimeSection = ExecTimeSection

    @property
    def LockWaitTimeSection(self):
        return self._LockWaitTimeSection

    @LockWaitTimeSection.setter
    def LockWaitTimeSection(self, LockWaitTimeSection):
        self._LockWaitTimeSection = LockWaitTimeSection

    @property
    def IoWaitTimeSection(self):
        return self._IoWaitTimeSection

    @IoWaitTimeSection.setter
    def IoWaitTimeSection(self, IoWaitTimeSection):
        self._IoWaitTimeSection = IoWaitTimeSection

    @property
    def TransactionLivingTimeSection(self):
        return self._TransactionLivingTimeSection

    @TransactionLivingTimeSection.setter
    def TransactionLivingTimeSection(self, TransactionLivingTimeSection):
        self._TransactionLivingTimeSection = TransactionLivingTimeSection

    @property
    def ThreadId(self):
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId

    @property
    def SentRows(self):
        return self._SentRows

    @SentRows.setter
    def SentRows(self, SentRows):
        self._SentRows = SentRows

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._User = params.get("User")
        self._DBName = params.get("DBName")
        self._TableName = params.get("TableName")
        self._PolicyName = params.get("PolicyName")
        self._Sql = params.get("Sql")
        self._SqlType = params.get("SqlType")
        self._ExecTime = params.get("ExecTime")
        self._AffectRows = params.get("AffectRows")
        self._SqlTypes = params.get("SqlTypes")
        self._Sqls = params.get("Sqls")
        self._AffectRowsSection = params.get("AffectRowsSection")
        self._SentRowsSection = params.get("SentRowsSection")
        self._ExecTimeSection = params.get("ExecTimeSection")
        self._LockWaitTimeSection = params.get("LockWaitTimeSection")
        self._IoWaitTimeSection = params.get("IoWaitTimeSection")
        self._TransactionLivingTimeSection = params.get("TransactionLivingTimeSection")
        self._ThreadId = params.get("ThreadId")
        self._SentRows = params.get("SentRows")
        self._ErrCode = params.get("ErrCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditPolicy(AbstractModel):
    """Audit Policy

    """

    def __init__(self):
        r"""
        :param _PolicyId: Audit policy ID.
        :type PolicyId: str
        :param _Status: Audit policy status. Valid values:
`creating`;
`running`,
`paused`;
`failed`.
        :type Status: str
        :param _InstanceId: Database instance ID
        :type InstanceId: str
        :param _CreateTime: Creation time of audit policy in the format of 2019-03-20 17:09:13
        :type CreateTime: str
        :param _ModifyTime: Last modified time of audit policy in the format of 2019-03-20 17:09:13
        :type ModifyTime: str
        :param _PolicyName: Audit policy name
        :type PolicyName: str
        :param _RuleId: Audit rule ID
        :type RuleId: str
        :param _RuleName: Audit rule name
Note: This field may return `null`, indicating that no valid value was found.
        :type RuleName: str
        :param _InstanceName: Database instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        """
        self._PolicyId = None
        self._Status = None
        self._InstanceId = None
        self._CreateTime = None
        self._ModifyTime = None
        self._PolicyName = None
        self._RuleId = None
        self._RuleName = None
        self._InstanceName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._PolicyName = params.get("PolicyName")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRule(AbstractModel):
    """Audit rule

    """

    def __init__(self):
        r"""
        :param _RuleId: Audit rule ID
        :type RuleId: str
        :param _CreateTime: Creation time of audit rule in the format of 2019-03-20 17:09:13
        :type CreateTime: str
        :param _ModifyTime: Last modified time of audit rule in the format of 2019-03-20 17:09:13
        :type ModifyTime: str
        :param _RuleName: Audit rule name
Note: This field may return `null`, indicating that no valid value was found.
        :type RuleName: str
        :param _Description: Audit rule description
Note: This field may return `null`, indicating that no valid value was found.
        :type Description: str
        :param _RuleFilters: Audit rule filters
Note: This field may return `null`, indicating that no valid value was found.
        :type RuleFilters: list of AuditFilter
        :param _AuditAll: Whether to enable full audit
        :type AuditAll: bool
        """
        self._RuleId = None
        self._CreateTime = None
        self._ModifyTime = None
        self._RuleName = None
        self._Description = None
        self._RuleFilters = None
        self._AuditAll = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters

    @property
    def AuditAll(self):
        return self._AuditAll

    @AuditAll.setter
    def AuditAll(self, AuditAll):
        self._AuditAll = AuditAll


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        self._AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleFilters(AbstractModel):
    """Filter of rule audit

    """

    def __init__(self):
        r"""
        :param _RuleFilters: Audit rule 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type RuleFilters: list of RuleFilters
        """
        self._RuleFilters = None

    @property
    def RuleFilters(self):
        return self._RuleFilters

    @RuleFilters.setter
    def RuleFilters(self, RuleFilters):
        self._RuleFilters = RuleFilters


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self._RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self._RuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupConfig(AbstractModel):
    """Configuration information of ECDB secondary database 2. This field is only applicable to ECDB instances

    """

    def __init__(self):
        r"""
        :param _ReplicationMode: Replication mode of secondary database 2. Value range: async, semi-sync
        :type ReplicationMode: str
        :param _Zone: Name of the AZ of secondary database 2, such as ap-shanghai-1
        :type Zone: str
        :param _Vip: Private IP address of secondary database 2
        :type Vip: str
        :param _Vport: Access port of secondary database 2
        :type Vport: int
        """
        self._ReplicationMode = None
        self._Zone = None
        self._Vip = None
        self._Vport = None

    @property
    def ReplicationMode(self):
        return self._ReplicationMode

    @ReplicationMode.setter
    def ReplicationMode(self, ReplicationMode):
        self._ReplicationMode = ReplicationMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._ReplicationMode = params.get("ReplicationMode")
        self._Zone = params.get("Zone")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """Backup details

    """

    def __init__(self):
        r"""
        :param _Name: Backup filename
        :type Name: str
        :param _Size: Backup file size in bytes
        :type Size: int
        :param _Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: Download address
        :type IntranetUrl: str
        :param _InternetUrl: Download address
        :type InternetUrl: str
        :param _Type: Log type. Valid values: `logical` (logical cold backup), `physical` (physical cold backup).
        :type Type: str
        :param _BackupId: Backup subtask ID, which is used when backup files are deleted
        :type BackupId: int
        :param _Status: Backup task status. Valid values: `SUCCESS` (backup succeeded), `FAILED` (backup failed), `RUNNING` (backup is in progress).
        :type Status: str
        :param _FinishTime: Backup task completion time
        :type FinishTime: str
        :param _Creator: (This field will be disused and is thus not recommended) backup creator. Valid values: `SYSTEM` (created by system), `Uin` (initiator's `Uin` value).
        :type Creator: str
        :param _StartTime: Backup task start time
        :type StartTime: str
        :param _Method: Backup method. Valid values: `full` (full backup), `partial` (partial backup).
        :type Method: str
        :param _Way: Backup mode. Valid values: `manual` (manual backup), `automatic` (automatic backup).
        :type Way: str
        :param _ManualBackupName: Manual backup alias
        :type ManualBackupName: str
        :param _SaveMode: Backup retention type. Valid values: `save_mode_regular` (non-archive backup), save_mode_period`(archive backup).
        :type SaveMode: str
        :param _Region: The region where local backup resides
        :type Region: str
        :param _RemoteInfo: Detailed information of remote backups
        :type RemoteInfo: list of RemoteBackupInfo
        :param _CosStorageType: Storage method. Valid values: `0` (regular storage), `1`(archive storage). Default value: `0`.
        :type CosStorageType: int
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _EncryptionFlag: Whether the backup file is encrypted. Valid values: `on` (encrypted), `off` (unencrypted).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptionFlag: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None
        self._BackupId = None
        self._Status = None
        self._FinishTime = None
        self._Creator = None
        self._StartTime = None
        self._Method = None
        self._Way = None
        self._ManualBackupName = None
        self._SaveMode = None
        self._Region = None
        self._RemoteInfo = None
        self._CosStorageType = None
        self._InstanceId = None
        self._EncryptionFlag = None

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

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Way(self):
        return self._Way

    @Way.setter
    def Way(self, Way):
        self._Way = Way

    @property
    def ManualBackupName(self):
        return self._ManualBackupName

    @ManualBackupName.setter
    def ManualBackupName(self, ManualBackupName):
        self._ManualBackupName = ManualBackupName

    @property
    def SaveMode(self):
        return self._SaveMode

    @SaveMode.setter
    def SaveMode(self, SaveMode):
        self._SaveMode = SaveMode

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RemoteInfo(self):
        return self._RemoteInfo

    @RemoteInfo.setter
    def RemoteInfo(self, RemoteInfo):
        self._RemoteInfo = RemoteInfo

    @property
    def CosStorageType(self):
        return self._CosStorageType

    @CosStorageType.setter
    def CosStorageType(self, CosStorageType):
        self._CosStorageType = CosStorageType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptionFlag(self):
        return self._EncryptionFlag

    @EncryptionFlag.setter
    def EncryptionFlag(self, EncryptionFlag):
        self._EncryptionFlag = EncryptionFlag


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        self._BackupId = params.get("BackupId")
        self._Status = params.get("Status")
        self._FinishTime = params.get("FinishTime")
        self._Creator = params.get("Creator")
        self._StartTime = params.get("StartTime")
        self._Method = params.get("Method")
        self._Way = params.get("Way")
        self._ManualBackupName = params.get("ManualBackupName")
        self._SaveMode = params.get("SaveMode")
        self._Region = params.get("Region")
        if params.get("RemoteInfo") is not None:
            self._RemoteInfo = []
            for item in params.get("RemoteInfo"):
                obj = RemoteBackupInfo()
                obj._deserialize(item)
                self._RemoteInfo.append(obj)
        self._CosStorageType = params.get("CosStorageType")
        self._InstanceId = params.get("InstanceId")
        self._EncryptionFlag = params.get("EncryptionFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupItem(AbstractModel):
    """When creating a backup, you need to specify the information of the table to be backed up.

    """

    def __init__(self):
        r"""
        :param _Db: Name of the database to be backed up
        :type Db: str
        :param _Table: Name of the table to be backed up. If this parameter is passed in, the specified table in the database will be backed up; otherwise, the database will be backed up.
        :type Table: str
        """
        self._Db = None
        self._Table = None

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    """VPCs used to restrict backup download

    """

    def __init__(self):
        r"""
        :param _Region: The region where the backup download restrictions take effect. It must be the same as the common request parameter `Region` of the API.
        :type Region: str
        :param _VpcList: The list of VPCs used to restrict backup download
        :type VpcList: list of str
        """
        self._Region = None
        self._VpcList = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummaryItem(AbstractModel):
    """Statistical items of instance backup

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _AutoBackupCount: Number of automatic data backups of an instance.
        :type AutoBackupCount: int
        :param _AutoBackupVolume: Capacity of automatic data backups of an instance.
        :type AutoBackupVolume: int
        :param _ManualBackupCount: Number of manual data backups of an instance.
        :type ManualBackupCount: int
        :param _ManualBackupVolume: Capacity of manual data backups of an instance.
        :type ManualBackupVolume: int
        :param _DataBackupCount: Total number of data backups of an instance (including automatic backups and manual backups).
        :type DataBackupCount: int
        :param _DataBackupVolume: Total capacity of data backups of an instance.
        :type DataBackupVolume: int
        :param _BinlogBackupCount: Number of log backups of an instance.
        :type BinlogBackupCount: int
        :param _BinlogBackupVolume: Capacity of log backups of an instance.
        :type BinlogBackupVolume: int
        :param _BackupVolume: Total capacity of backups of an instance (including data backups and log backups).
        :type BackupVolume: int
        """
        self._InstanceId = None
        self._AutoBackupCount = None
        self._AutoBackupVolume = None
        self._ManualBackupCount = None
        self._ManualBackupVolume = None
        self._DataBackupCount = None
        self._DataBackupVolume = None
        self._BinlogBackupCount = None
        self._BinlogBackupVolume = None
        self._BackupVolume = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def AutoBackupVolume(self):
        return self._AutoBackupVolume

    @AutoBackupVolume.setter
    def AutoBackupVolume(self, AutoBackupVolume):
        self._AutoBackupVolume = AutoBackupVolume

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def ManualBackupVolume(self):
        return self._ManualBackupVolume

    @ManualBackupVolume.setter
    def ManualBackupVolume(self, ManualBackupVolume):
        self._ManualBackupVolume = ManualBackupVolume

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def DataBackupVolume(self):
        return self._DataBackupVolume

    @DataBackupVolume.setter
    def DataBackupVolume(self, DataBackupVolume):
        self._DataBackupVolume = DataBackupVolume

    @property
    def BinlogBackupCount(self):
        return self._BinlogBackupCount

    @BinlogBackupCount.setter
    def BinlogBackupCount(self, BinlogBackupCount):
        self._BinlogBackupCount = BinlogBackupCount

    @property
    def BinlogBackupVolume(self):
        return self._BinlogBackupVolume

    @BinlogBackupVolume.setter
    def BinlogBackupVolume(self, BinlogBackupVolume):
        self._BinlogBackupVolume = BinlogBackupVolume

    @property
    def BackupVolume(self):
        return self._BackupVolume

    @BackupVolume.setter
    def BackupVolume(self, BackupVolume):
        self._BackupVolume = BackupVolume


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._AutoBackupVolume = params.get("AutoBackupVolume")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._ManualBackupVolume = params.get("ManualBackupVolume")
        self._DataBackupCount = params.get("DataBackupCount")
        self._DataBackupVolume = params.get("DataBackupVolume")
        self._BinlogBackupCount = params.get("BinlogBackupCount")
        self._BinlogBackupVolume = params.get("BinlogBackupVolume")
        self._BackupVolume = params.get("BackupVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadRequest(AbstractModel):
    """BalanceRoGroupLoad request structure.

    """

    def __init__(self):
        r"""
        :param _RoGroupId: RO group ID in the format of `cdbrg-c1nl9rpv`.
        :type RoGroupId: str
        """
        self._RoGroupId = None

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId


    def _deserialize(self, params):
        self._RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadResponse(AbstractModel):
    """BalanceRoGroupLoad response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BaseGroupInfo(AbstractModel):
    """Proxy group information

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyGroupId: str
        :param _NodeCount: Number of proxy nodes
Note: this field may return `null`, indicating that no valid value can be found.
        :type NodeCount: int
        :param _Status: Proxy group status. Valid values: `init` (delivering), `online` (active), `offline` (inactive), `destroy` (destoryed)
Note: this field may return `null`, indicating that no valid value can be found.
        :type Status: str
        :param _Region: Region
Note: this field may return `null`, indicating that no valid value can be found.
        :type Region: str
        :param _Zone: Availability zone
Note: this field may return `null`, indicating that no valid value can be found.
        :type Zone: str
        :param _OpenRW: Whether read/write separation is enabled
Note: this field may return `null`, indicating that no valid value can be found.
        :type OpenRW: bool
        :param _CurrentProxyVersion: Current proxy version
Note: this field may return `null`, indicating that no valid value can be found.
        :type CurrentProxyVersion: str
        :param _SupportUpgradeProxyVersion: Target version to which the proxy can be upgraded
Note: this field may return `null`, indicating that no valid value can be found.
        :type SupportUpgradeProxyVersion: str
        """
        self._ProxyGroupId = None
        self._NodeCount = None
        self._Status = None
        self._Region = None
        self._Zone = None
        self._OpenRW = None
        self._CurrentProxyVersion = None
        self._SupportUpgradeProxyVersion = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OpenRW(self):
        return self._OpenRW

    @OpenRW.setter
    def OpenRW(self, OpenRW):
        self._OpenRW = OpenRW

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def SupportUpgradeProxyVersion(self):
        return self._SupportUpgradeProxyVersion

    @SupportUpgradeProxyVersion.setter
    def SupportUpgradeProxyVersion(self, SupportUpgradeProxyVersion):
        self._SupportUpgradeProxyVersion = SupportUpgradeProxyVersion


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._NodeCount = params.get("NodeCount")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._OpenRW = params.get("OpenRW")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._SupportUpgradeProxyVersion = params.get("SupportUpgradeProxyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    """Binlog information

    """

    def __init__(self):
        r"""
        :param _Name: Binlog backup filename
        :type Name: str
        :param _Size: Backup file size in bytes
        :type Size: int
        :param _Date: File stored time in the format of 2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: Download address
        :type IntranetUrl: str
        :param _InternetUrl: Download address
        :type InternetUrl: str
        :param _Type: Log type. Value range: binlog
        :type Type: str
        :param _BinlogStartTime: Binlog file start file
        :type BinlogStartTime: str
        :param _BinlogFinishTime: Binlog file end time
        :type BinlogFinishTime: str
        :param _Region: The region where the binlog file resides
        :type Region: str
        :param _Status: Backup task status. Valid values: `SUCCESS` (backup succeeded), `FAILED` (backup failed), `RUNNING` (backup is in progress).
        :type Status: str
        :param _RemoteInfo: The detailed information of remote binlog backups
        :type RemoteInfo: list of RemoteBackupInfo
        :param _CosStorageType: Storage method. Valid values: `0` (regular storage), `1`(archive storage). Default value: `0`.
        :type CosStorageType: int
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None
        self._BinlogStartTime = None
        self._BinlogFinishTime = None
        self._Region = None
        self._Status = None
        self._RemoteInfo = None
        self._CosStorageType = None
        self._InstanceId = None

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

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BinlogStartTime(self):
        return self._BinlogStartTime

    @BinlogStartTime.setter
    def BinlogStartTime(self, BinlogStartTime):
        self._BinlogStartTime = BinlogStartTime

    @property
    def BinlogFinishTime(self):
        return self._BinlogFinishTime

    @BinlogFinishTime.setter
    def BinlogFinishTime(self, BinlogFinishTime):
        self._BinlogFinishTime = BinlogFinishTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RemoteInfo(self):
        return self._RemoteInfo

    @RemoteInfo.setter
    def RemoteInfo(self, RemoteInfo):
        self._RemoteInfo = RemoteInfo

    @property
    def CosStorageType(self):
        return self._CosStorageType

    @CosStorageType.setter
    def CosStorageType(self, CosStorageType):
        self._CosStorageType = CosStorageType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        self._BinlogStartTime = params.get("BinlogStartTime")
        self._BinlogFinishTime = params.get("BinlogFinishTime")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        if params.get("RemoteInfo") is not None:
            self._RemoteInfo = []
            for item in params.get("RemoteInfo"):
                obj = RemoteBackupInfo()
                obj._deserialize(item)
                self._RemoteInfo.append(obj)
        self._CosStorageType = params.get("CosStorageType")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bucket(AbstractModel):
    """Information of an aggregation bucket

    """

    def __init__(self):
        r"""
        :param _Key: None
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Count: Number of occurrences of the key value
        :type Count: int
        """
        self._Key = None
        self._Count = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbRegionSellConf(AbstractModel):
    """The purchasable configuration in a region

    """

    def __init__(self):
        r"""
        :param _RegionName: Region name
        :type RegionName: str
        :param _Area: Area
        :type Area: str
        :param _IsDefaultRegion: Whether it is a default region
        :type IsDefaultRegion: int
        :param _Region: Region name
        :type Region: str
        :param _RegionConfig: The purchasable configuration in an AZ in a region
        :type RegionConfig: list of CdbZoneSellConf
        """
        self._RegionName = None
        self._Area = None
        self._IsDefaultRegion = None
        self._Region = None
        self._RegionConfig = None

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def IsDefaultRegion(self):
        return self._IsDefaultRegion

    @IsDefaultRegion.setter
    def IsDefaultRegion(self, IsDefaultRegion):
        self._IsDefaultRegion = IsDefaultRegion

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionConfig(self):
        return self._RegionConfig

    @RegionConfig.setter
    def RegionConfig(self, RegionConfig):
        self._RegionConfig = RegionConfig


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._Area = params.get("Area")
        self._IsDefaultRegion = params.get("IsDefaultRegion")
        self._Region = params.get("Region")
        if params.get("RegionConfig") is not None:
            self._RegionConfig = []
            for item in params.get("RegionConfig"):
                obj = CdbZoneSellConf()
                obj._deserialize(item)
                self._RegionConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbSellConfig(AbstractModel):
    """The details of purchasable configuration

    """

    def __init__(self):
        r"""
        :param _Memory: Memory size in MB
        :type Memory: int
        :param _Cpu: CPU core count
        :type Cpu: int
        :param _VolumeMin: Minimum disk size in GB
        :type VolumeMin: int
        :param _VolumeMax: Maximum disk size in GB
        :type VolumeMax: int
        :param _VolumeStep: Disk capacity increment in GB
        :type VolumeStep: int
        :param _Iops: IO operations per second
        :type Iops: int
        :param _Info: Application scenario description
        :type Info: str
        :param _Status: Status. The value `0` indicates that this specification is available.
        :type Status: int
        :param _DeviceType: Instance type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance), `BASIC_V2` (basic v2 instance).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeviceType: str
        :param _EngineType: Engine type description. Valid values: `Innodb`, `RocksDB`.
        :type EngineType: str
        :param _Id: Purchasable specifications ID
        :type Id: int
        """
        self._Memory = None
        self._Cpu = None
        self._VolumeMin = None
        self._VolumeMax = None
        self._VolumeStep = None
        self._Iops = None
        self._Info = None
        self._Status = None
        self._DeviceType = None
        self._EngineType = None
        self._Id = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def VolumeMin(self):
        return self._VolumeMin

    @VolumeMin.setter
    def VolumeMin(self, VolumeMin):
        self._VolumeMin = VolumeMin

    @property
    def VolumeMax(self):
        return self._VolumeMax

    @VolumeMax.setter
    def VolumeMax(self, VolumeMax):
        self._VolumeMax = VolumeMax

    @property
    def VolumeStep(self):
        return self._VolumeStep

    @VolumeStep.setter
    def VolumeStep(self, VolumeStep):
        self._VolumeStep = VolumeStep

    @property
    def Iops(self):
        return self._Iops

    @Iops.setter
    def Iops(self, Iops):
        self._Iops = Iops

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Cpu = params.get("Cpu")
        self._VolumeMin = params.get("VolumeMin")
        self._VolumeMax = params.get("VolumeMax")
        self._VolumeStep = params.get("VolumeStep")
        self._Iops = params.get("Iops")
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._DeviceType = params.get("DeviceType")
        self._EngineType = params.get("EngineType")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbSellType(AbstractModel):
    """Purchasable instance type

    """

    def __init__(self):
        r"""
        :param _TypeName: Name of the purchasable instance. Valid values: `Z3` (High-availability instance. `DeviceType`:`UNIVERSAL`, `EXCLUSIVE`; `CVM` (basic instance. `DeviceType`: `BASIC`); `TKE` (basic v2 instance. `DeviceType`: `BASIC_V2`).
        :type TypeName: str
        :param _EngineVersion: Engine version number
        :type EngineVersion: list of str
        :param _ConfigIds: Purchasable specifications ID
        :type ConfigIds: list of int
        """
        self._TypeName = None
        self._EngineVersion = None
        self._ConfigIds = None

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def ConfigIds(self):
        return self._ConfigIds

    @ConfigIds.setter
    def ConfigIds(self, ConfigIds):
        self._ConfigIds = ConfigIds


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._EngineVersion = params.get("EngineVersion")
        self._ConfigIds = params.get("ConfigIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbZoneDataResult(AbstractModel):
    """The purchasable specifications in a region

    """

    def __init__(self):
        r"""
        :param _Configs: List of purchasable specifications
        :type Configs: list of CdbSellConfig
        :param _Regions: List of AZs in purchasable regions
        :type Regions: list of CdbRegionSellConf
        """
        self._Configs = None
        self._Regions = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = CdbSellConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = CdbRegionSellConf()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbZoneSellConf(AbstractModel):
    """Purchasable specifications in an AZ

    """

    def __init__(self):
        r"""
        :param _Status: AZ status, which is used to indicate whether instances are purchasable. Valid values: `1` (purchasable), `3` (not purchasable), `4` (AZ not displayed)
        :type Status: int
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _IsCustom: Whether it is a custom instance type
        :type IsCustom: bool
        :param _IsSupportDr: Whether disaster recovery is supported
        :type IsSupportDr: bool
        :param _IsSupportVpc: Whether VPC is supported
        :type IsSupportVpc: bool
        :param _HourInstanceSaleMaxNum: Maximum purchasable quantity of hourly billed instances
        :type HourInstanceSaleMaxNum: int
        :param _IsDefaultZone: Whether it is a default AZ
        :type IsDefaultZone: bool
        :param _IsBm: Whether it is a BM zone
        :type IsBm: bool
        :param _PayType: Supported billing method. Valid values: `0` (monthly subscribed), `1` (hourly billed), `2` (pay-as-you-go)
        :type PayType: list of str
        :param _ProtectMode: Data replication type. Valid values: `0` (async), `1` (semi-sync), `2` (strong sync)
        :type ProtectMode: list of str
        :param _Zone: AZ name
        :type Zone: str
        :param _ZoneConf: Multi-AZ information
        :type ZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        :param _DrZone: Information of supported disaster recovery AZs
        :type DrZone: list of str
        :param _IsSupportRemoteRo: Whether cross-AZ read-only access is supported
        :type IsSupportRemoteRo: bool
        :param _RemoteRoZone: Information of supported cross-AZ read-only zone
        :type RemoteRoZone: list of str
        :param _ExClusterStatus: AZ status, which is used to indicate whether dedicated instances are purchasable. Valid values: `1 (purchasable), `3` (not purchasable), `4` (AZ not displayed)
        :type ExClusterStatus: int
        :param _ExClusterRemoteRoZone: Information of cross-AZ read-only zones supported by a dedicated instance
        :type ExClusterRemoteRoZone: list of str
        :param _ExClusterZoneConf: AZ information of a multi-AZ deployed dedicated instance.
        :type ExClusterZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        :param _SellType: Array of purchasable instance types. The value of `configIds` and `configs` have a one-to-one correspondence.
        :type SellType: list of CdbSellType
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _IsSupportIpv6: Whether IPv6 is supported
        :type IsSupportIpv6: bool
        :param _EngineType: Supported engine types for purchasable database
        :type EngineType: list of str
        """
        self._Status = None
        self._ZoneName = None
        self._IsCustom = None
        self._IsSupportDr = None
        self._IsSupportVpc = None
        self._HourInstanceSaleMaxNum = None
        self._IsDefaultZone = None
        self._IsBm = None
        self._PayType = None
        self._ProtectMode = None
        self._Zone = None
        self._ZoneConf = None
        self._DrZone = None
        self._IsSupportRemoteRo = None
        self._RemoteRoZone = None
        self._ExClusterStatus = None
        self._ExClusterRemoteRoZone = None
        self._ExClusterZoneConf = None
        self._SellType = None
        self._ZoneId = None
        self._IsSupportIpv6 = None
        self._EngineType = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsCustom(self):
        return self._IsCustom

    @IsCustom.setter
    def IsCustom(self, IsCustom):
        self._IsCustom = IsCustom

    @property
    def IsSupportDr(self):
        return self._IsSupportDr

    @IsSupportDr.setter
    def IsSupportDr(self, IsSupportDr):
        self._IsSupportDr = IsSupportDr

    @property
    def IsSupportVpc(self):
        return self._IsSupportVpc

    @IsSupportVpc.setter
    def IsSupportVpc(self, IsSupportVpc):
        self._IsSupportVpc = IsSupportVpc

    @property
    def HourInstanceSaleMaxNum(self):
        return self._HourInstanceSaleMaxNum

    @HourInstanceSaleMaxNum.setter
    def HourInstanceSaleMaxNum(self, HourInstanceSaleMaxNum):
        self._HourInstanceSaleMaxNum = HourInstanceSaleMaxNum

    @property
    def IsDefaultZone(self):
        return self._IsDefaultZone

    @IsDefaultZone.setter
    def IsDefaultZone(self, IsDefaultZone):
        self._IsDefaultZone = IsDefaultZone

    @property
    def IsBm(self):
        return self._IsBm

    @IsBm.setter
    def IsBm(self, IsBm):
        self._IsBm = IsBm

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneConf(self):
        return self._ZoneConf

    @ZoneConf.setter
    def ZoneConf(self, ZoneConf):
        self._ZoneConf = ZoneConf

    @property
    def DrZone(self):
        return self._DrZone

    @DrZone.setter
    def DrZone(self, DrZone):
        self._DrZone = DrZone

    @property
    def IsSupportRemoteRo(self):
        return self._IsSupportRemoteRo

    @IsSupportRemoteRo.setter
    def IsSupportRemoteRo(self, IsSupportRemoteRo):
        self._IsSupportRemoteRo = IsSupportRemoteRo

    @property
    def RemoteRoZone(self):
        return self._RemoteRoZone

    @RemoteRoZone.setter
    def RemoteRoZone(self, RemoteRoZone):
        self._RemoteRoZone = RemoteRoZone

    @property
    def ExClusterStatus(self):
        return self._ExClusterStatus

    @ExClusterStatus.setter
    def ExClusterStatus(self, ExClusterStatus):
        self._ExClusterStatus = ExClusterStatus

    @property
    def ExClusterRemoteRoZone(self):
        return self._ExClusterRemoteRoZone

    @ExClusterRemoteRoZone.setter
    def ExClusterRemoteRoZone(self, ExClusterRemoteRoZone):
        self._ExClusterRemoteRoZone = ExClusterRemoteRoZone

    @property
    def ExClusterZoneConf(self):
        return self._ExClusterZoneConf

    @ExClusterZoneConf.setter
    def ExClusterZoneConf(self, ExClusterZoneConf):
        self._ExClusterZoneConf = ExClusterZoneConf

    @property
    def SellType(self):
        return self._SellType

    @SellType.setter
    def SellType(self, SellType):
        self._SellType = SellType

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IsSupportIpv6(self):
        return self._IsSupportIpv6

    @IsSupportIpv6.setter
    def IsSupportIpv6(self, IsSupportIpv6):
        self._IsSupportIpv6 = IsSupportIpv6

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ZoneName = params.get("ZoneName")
        self._IsCustom = params.get("IsCustom")
        self._IsSupportDr = params.get("IsSupportDr")
        self._IsSupportVpc = params.get("IsSupportVpc")
        self._HourInstanceSaleMaxNum = params.get("HourInstanceSaleMaxNum")
        self._IsDefaultZone = params.get("IsDefaultZone")
        self._IsBm = params.get("IsBm")
        self._PayType = params.get("PayType")
        self._ProtectMode = params.get("ProtectMode")
        self._Zone = params.get("Zone")
        if params.get("ZoneConf") is not None:
            self._ZoneConf = ZoneConf()
            self._ZoneConf._deserialize(params.get("ZoneConf"))
        self._DrZone = params.get("DrZone")
        self._IsSupportRemoteRo = params.get("IsSupportRemoteRo")
        self._RemoteRoZone = params.get("RemoteRoZone")
        self._ExClusterStatus = params.get("ExClusterStatus")
        self._ExClusterRemoteRoZone = params.get("ExClusterRemoteRoZone")
        if params.get("ExClusterZoneConf") is not None:
            self._ExClusterZoneConf = ZoneConf()
            self._ExClusterZoneConf._deserialize(params.get("ExClusterZoneConf"))
        if params.get("SellType") is not None:
            self._SellType = []
            for item in params.get("SellType"):
                obj = CdbSellType()
                obj._deserialize(item)
                self._SellType.append(obj)
        self._ZoneId = params.get("ZoneId")
        self._IsSupportIpv6 = params.get("IsSupportIpv6")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneItem(AbstractModel):
    """Clone task information.

    """

    def __init__(self):
        r"""
        :param _SrcInstanceId: ID of the original instance in a clone task
        :type SrcInstanceId: str
        :param _DstInstanceId: ID of the cloned instance in a clone task
        :type DstInstanceId: str
        :param _CloneJobId: Clone task ID
        :type CloneJobId: int
        :param _RollbackStrategy: The policy used in a clone task. Valid values: `timepoint` (roll back to a specific point in time), `backupset` (roll back by using a specific backup file).
        :type RollbackStrategy: str
        :param _RollbackTargetTime: The point in time to which the cloned instance will be rolled back
        :type RollbackTargetTime: str
        :param _StartTime: Task start time
        :type StartTime: str
        :param _EndTime: Task end time
        :type EndTime: str
        :param _TaskStatus: Task status. Valid values: `initial`, `running`, `wait_complete`, `success`, `failed`.
        :type TaskStatus: str
        :param _NewRegionId: Clone instance region ID
        :type NewRegionId: int
        :param _SrcRegionId: Source instance region ID
        :type SrcRegionId: int
        """
        self._SrcInstanceId = None
        self._DstInstanceId = None
        self._CloneJobId = None
        self._RollbackStrategy = None
        self._RollbackTargetTime = None
        self._StartTime = None
        self._EndTime = None
        self._TaskStatus = None
        self._NewRegionId = None
        self._SrcRegionId = None

    @property
    def SrcInstanceId(self):
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def DstInstanceId(self):
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def CloneJobId(self):
        return self._CloneJobId

    @CloneJobId.setter
    def CloneJobId(self, CloneJobId):
        self._CloneJobId = CloneJobId

    @property
    def RollbackStrategy(self):
        return self._RollbackStrategy

    @RollbackStrategy.setter
    def RollbackStrategy(self, RollbackStrategy):
        self._RollbackStrategy = RollbackStrategy

    @property
    def RollbackTargetTime(self):
        return self._RollbackTargetTime

    @RollbackTargetTime.setter
    def RollbackTargetTime(self, RollbackTargetTime):
        self._RollbackTargetTime = RollbackTargetTime

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
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def NewRegionId(self):
        return self._NewRegionId

    @NewRegionId.setter
    def NewRegionId(self, NewRegionId):
        self._NewRegionId = NewRegionId

    @property
    def SrcRegionId(self):
        return self._SrcRegionId

    @SrcRegionId.setter
    def SrcRegionId(self, SrcRegionId):
        self._SrcRegionId = SrcRegionId


    def _deserialize(self, params):
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._DstInstanceId = params.get("DstInstanceId")
        self._CloneJobId = params.get("CloneJobId")
        self._RollbackStrategy = params.get("RollbackStrategy")
        self._RollbackTargetTime = params.get("RollbackTargetTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        self._NewRegionId = params.get("NewRegionId")
        self._SrcRegionId = params.get("SrcRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyRequest(AbstractModel):
    """CloseCDBProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _OnlyCloseRW: Whether only to disable read/write separation. Valid values: `true`, `false`. Default value: `false`.
        :type OnlyCloseRW: bool
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._OnlyCloseRW = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OnlyCloseRW(self):
        return self._OnlyCloseRW

    @OnlyCloseRW.setter
    def OnlyCloseRW(self, OnlyCloseRW):
        self._OnlyCloseRW = OnlyCloseRW


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._OnlyCloseRW = params.get("OnlyCloseRW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyResponse(AbstractModel):
    """CloseCDBProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CloseCdbProxyAddressRequest(AbstractModel):
    """CloseCdbProxyAddress request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCdbProxyAddressResponse(AbstractModel):
    """CloseCdbProxyAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Column: Column name
        :type Column: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Column = None
        self._Privileges = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Column(self):
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Column = params.get("Column")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonTimeWindow(AbstractModel):
    """Common time window

    """

    def __init__(self):
        r"""
        :param _Monday: Time window on Monday in the format of 02:00-06:00
        :type Monday: str
        :param _Tuesday: Time window on Tuesday in the format of 02:00-06:00
        :type Tuesday: str
        :param _Wednesday: Time window on Wednesday in the format of 02:00-06:00
        :type Wednesday: str
        :param _Thursday: Time window on Thursday in the format of 02:00-06:00
        :type Thursday: str
        :param _Friday: Time window on Friday in the format of 02:00-06:00
        :type Friday: str
        :param _Saturday: Time window on Saturday in the format of 02:00-06:00
        :type Saturday: str
        :param _Sunday: Time window on Sunday in the format of 02:00-06:00
        :type Sunday: str
        :param _BackupPeriodStrategy: Non-archive backup retention policy. Valid values: `weekly` (back up by week), monthly (back up by month), default value: `weekly`.
        :type BackupPeriodStrategy: str
        :param _Days: If `BackupPeriodStrategy` is `monthly`, you need to pass in the specific backup dates. The time interval between any two adjacent dates cannot exceed 2 days, for example, [1,4,7,9,11,14,17,19,22,25,28,30,31].
        :type Days: list of int
        :param _BackupPeriodTime: Backup time by month in the format of 02:00–06:00, which is required when `BackupPeriodStrategy` is `monthly`.
        :type BackupPeriodTime: str
        """
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._BackupPeriodStrategy = None
        self._Days = None
        self._BackupPeriodTime = None

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def BackupPeriodStrategy(self):
        return self._BackupPeriodStrategy

    @BackupPeriodStrategy.setter
    def BackupPeriodStrategy(self, BackupPeriodStrategy):
        self._BackupPeriodStrategy = BackupPeriodStrategy

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def BackupPeriodTime(self):
        return self._BackupPeriodTime

    @BackupPeriodTime.setter
    def BackupPeriodTime(self, BackupPeriodTime):
        self._BackupPeriodTime = BackupPeriodTime


    def _deserialize(self, params):
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._BackupPeriodStrategy = params.get("BackupPeriodStrategy")
        self._Days = params.get("Days")
        self._BackupPeriodTime = params.get("BackupPeriodTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionPoolInfo(AbstractModel):
    """Connection pool information

    """

    def __init__(self):
        r"""
        :param _ConnectionPool: Whether the connection pool is enabled
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPool: bool
        :param _ConnectionPoolType: Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPoolType: str
        :param _PoolConnectionTimeOut: Connection persistence timeout in seconds
Note: this field may return `null`, indicating that no valid value can be found.
        :type PoolConnectionTimeOut: int
        """
        self._ConnectionPool = None
        self._ConnectionPoolType = None
        self._PoolConnectionTimeOut = None

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def PoolConnectionTimeOut(self):
        return self._PoolConnectionTimeOut

    @PoolConnectionTimeOut.setter
    def PoolConnectionTimeOut(self, PoolConnectionTimeOut):
        self._PoolConnectionTimeOut = PoolConnectionTimeOut


    def _deserialize(self, params):
        self._ConnectionPool = params.get("ConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._PoolConnectionTimeOut = params.get("PoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _Accounts: List of TencentDB accounts
        :type Accounts: list of Account
        :param _Password: Password of the new account
        :type Password: str
        :param _Description: Remarks
        :type Description: str
        :param _MaxUserConnections: Maximum connections of the new account. Default value: `10240`. Maximum value: `10240`.
        :type MaxUserConnections: int
        """
        self._InstanceId = None
        self._Accounts = None
        self._Password = None
        self._Description = None
        self._MaxUserConnections = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateAuditPolicyRequest(AbstractModel):
    """CreateAuditPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Audit policy name.
        :type Name: str
        :param _RuleId: Audit rule ID.
        :type RuleId: str
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _LogExpireDay: Retention period of audit logs. Valid values:
7: seven days (a week);
30: 30 days (a month);
180: 180 days (six months);
365: 365 days (a year);
1095: 1095 days (three years);
1825: 1825 days (five years).
This parameter specifies the retention period (30 days by default) of audit logs, which is valid when you create the first audit policy for an instance. If the instance already has audit policies, this parameter is invalid, but you can use the `ModifyAuditConfig` API to modify the retention period.
        :type LogExpireDay: int
        """
        self._Name = None
        self._RuleId = None
        self._InstanceId = None
        self._LogExpireDay = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RuleId = params.get("RuleId")
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditPolicyResponse(AbstractModel):
    """CreateAuditPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Audit policy ID.
        :type PolicyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _BackupMethod: Target backup method. Valid values: `logical` (logical cold backup), `physical` (physical cold backup), `snapshot` (snapshot backup). Basic Edition instances only support snapshot backups.
        :type BackupMethod: str
        :param _BackupDBTableList: Information of the table to be backed up. If this parameter is not set, the entire instance will be backed up by default. It can be set only in logical backup (i.e., BackupMethod = logical). The specified table must exist; otherwise, backup may fail.
For example, if you want to backup tb1 and tb2 in db1 and the entire db2, you should set the parameter as [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ].
        :type BackupDBTableList: list of BackupItem
        :param _ManualBackupName: Manual backup alias
        :type ManualBackupName: str
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._BackupDBTableList = None
        self._ManualBackupName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupDBTableList(self):
        return self._BackupDBTableList

    @BackupDBTableList.setter
    def BackupDBTableList(self, BackupDBTableList):
        self._BackupDBTableList = BackupDBTableList

    @property
    def ManualBackupName(self):
        return self._ManualBackupName

    @ManualBackupName.setter
    def ManualBackupName(self, ManualBackupName):
        self._ManualBackupName = ManualBackupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self._BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self._BackupDBTableList.append(obj)
        self._ManualBackupName = params.get("ManualBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup response structure.

    """

    def __init__(self):
        r"""
        :param _BackupId: Backup task ID
        :type BackupId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupId = None
        self._RequestId = None

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._RequestId = params.get("RequestId")


class CreateCdbProxyAddressRequest(AbstractModel):
    """CreateCdbProxyAddress request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _WeightMode: Assignment mode of weights. Valid values: `system` (auto-assigned), `custom`.
        :type WeightMode: str
        :param _IsKickOut: Whether to remove delayed read-only instances from the proxy group. Valid values: `true`, `false`.
        :type IsKickOut: bool
        :param _MinCount: Least read-only instances. Minimum value:  `0`
        :type MinCount: int
        :param _MaxDelay: The delay threshold. Minimum value:  `0`
        :type MaxDelay: int
        :param _FailOver: Whether to enable failover. Valid values: `true`, `false`.
        :type FailOver: bool
        :param _AutoAddRo: Whether to automatically add newly created read-only instances. Valid values: `true`, `false`.
        :type AutoAddRo: bool
        :param _ReadOnly: Whether it is read-only. Valid values: `true`, `false`.
        :type ReadOnly: bool
        :param _TransSplit: Whether to enable transaction splitting. Valid values: `true`, `false`.
        :type TransSplit: bool
        :param _ProxyAllocation: Assignment of read/write weights
        :type ProxyAllocation: list of ProxyAllocation
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID
        :type UniqSubnetId: str
        :param _ConnectionPool: Whether to enable the connection pool. Valid values: 
        :type ConnectionPool: bool
        :param _Desc: Description
        :type Desc: str
        :param _Vip: IP address
        :type Vip: str
        :param _VPort: Port
        :type VPort: int
        :param _SecurityGroup: Security group
        :type SecurityGroup: list of str
        :param _ConnectionPoolType: Connection pool type, which will take effect only when `ConnectionPool` is `true`. Valid values:  `transaction` (transaction-level), `connection` (session-level).
        :type ConnectionPoolType: str
        """
        self._ProxyGroupId = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._TransSplit = None
        self._ProxyAllocation = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ConnectionPool = None
        self._Desc = None
        self._Vip = None
        self._VPort = None
        self._SecurityGroup = None
        self._ConnectionPoolType = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._TransSplit = params.get("TransSplit")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ConnectionPool = params.get("ConnectionPool")
        self._Desc = params.get("Desc")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._SecurityGroup = params.get("SecurityGroup")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdbProxyAddressResponse(AbstractModel):
    """CreateCdbProxyAddress response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateCdbProxyRequest(AbstractModel):
    """CreateCdbProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID
        :type UniqSubnetId: str
        :param _ProxyNodeCustom: The specification configuration of a node
        :type ProxyNodeCustom: list of ProxyNodeCustom
        :param _SecurityGroup: Security group
        :type SecurityGroup: list of str
        :param _Desc: Description
        :type Desc: str
        :param _ConnectionPoolLimit: Connection pool threshold
        :type ConnectionPoolLimit: int
        """
        self._InstanceId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProxyNodeCustom = None
        self._SecurityGroup = None
        self._Desc = None
        self._ConnectionPoolLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProxyNodeCustom(self):
        return self._ProxyNodeCustom

    @ProxyNodeCustom.setter
    def ProxyNodeCustom(self, ProxyNodeCustom):
        self._ProxyNodeCustom = ProxyNodeCustom

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("ProxyNodeCustom") is not None:
            self._ProxyNodeCustom = []
            for item in params.get("ProxyNodeCustom"):
                obj = ProxyNodeCustom()
                obj._deserialize(item)
                self._ProxyNodeCustom.append(obj)
        self._SecurityGroup = params.get("SecurityGroup")
        self._Desc = params.get("Desc")
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCdbProxyResponse(AbstractModel):
    """CreateCdbProxy response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateCloneInstanceRequest(AbstractModel):
    """CreateCloneInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be cloned from
        :type InstanceId: str
        :param _SpecifiedRollbackTime: To roll back the cloned instance to a specific point in time, set this parameter to a value in the format of "yyyy-mm-dd hh:mm:ss".
        :type SpecifiedRollbackTime: str
        :param _SpecifiedBackupId: To roll back the cloned instance to a specific physical backup file, set this parameter to the ID of the physical backup file. The ID can be obtained by the [DescribeBackups](https://intl.cloud.tencent.com/document/api/236/15842?from_cn_redirect=1) API.
        :type SpecifiedBackupId: int
        :param _UniqVpcId: VPC ID, which can be obtained by the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API. If this parameter is left empty, the classic network will be used by default.
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID, which can be obtained by the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API. If `UniqVpcId` is set, `UniqSubnetId` will be required.
        :type UniqSubnetId: str
        :param _Memory: Memory of the cloned instance in MB, which should be equal to (by default) or larger than that of the original instance
        :type Memory: int
        :param _Volume: Disk capacity of the cloned instance in GB, which should be equal to (by default) or larger than that of the original instance
        :type Volume: int
        :param _InstanceName: Name of the cloned instance
        :type InstanceName: str
        :param _SecurityGroup: Security group parameter, which can be obtained by the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API
        :type SecurityGroup: list of str
        :param _ResourceTags: Information of the cloned instance tag
        :type ResourceTags: list of TagInfo
        :param _Cpu: The number of CPU cores of the cloned instance. It should be equal to (by default) or larger than that of the original instance.
        :type Cpu: int
        :param _ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0.
        :type ProtectMode: int
        :param _DeployMode: Multi-AZ or single-AZ. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0.
        :type DeployMode: int
        :param _SlaveZone: Availability zone information of replica 1 of the cloned instance, which is the same as the value of `Zone` of the original instance by default
        :type SlaveZone: str
        :param _BackupZone: Availability zone information of replica 2 of the cloned instance, 
which is left empty by default. Specify this parameter when cloning a strong sync source instance.
        :type BackupZone: str
        :param _DeviceType: Resource isolation type of the clone. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance). Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param _InstanceNodes: The number of nodes of the clone. If this parameter is set to `3` or the `BackupZone` parameter is specified, the clone will have three nodes. If this parameter is set to `2` or left empty, the clone will have two nodes.
        :type InstanceNodes: int
        :param _DeployGroupId: Placement group ID.
        :type DeployGroupId: str
        :param _DryRun: Whether to check the request without creating any instance. Valid values: `true`, `false` (default). After being submitted, the request will be checked to see if it is in correct format and has all required parameters with valid values. An error code is returned if the check failed, and `RequestId` is returned if the check succeeded. After a successful check, no instance will be created if this parameter is set to `true`, whereas an instance will be created and if it is set to `false`.
        :type DryRun: bool
        :param _CageId: Financial cage ID.
        :type CageId: str
        :param _ProjectId: Project ID. Default value: 0.
        :type ProjectId: int
        """
        self._InstanceId = None
        self._SpecifiedRollbackTime = None
        self._SpecifiedBackupId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Memory = None
        self._Volume = None
        self._InstanceName = None
        self._SecurityGroup = None
        self._ResourceTags = None
        self._Cpu = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._BackupZone = None
        self._DeviceType = None
        self._InstanceNodes = None
        self._DeployGroupId = None
        self._DryRun = None
        self._CageId = None
        self._ProjectId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecifiedRollbackTime(self):
        return self._SpecifiedRollbackTime

    @SpecifiedRollbackTime.setter
    def SpecifiedRollbackTime(self, SpecifiedRollbackTime):
        self._SpecifiedRollbackTime = SpecifiedRollbackTime

    @property
    def SpecifiedBackupId(self):
        return self._SpecifiedBackupId

    @SpecifiedBackupId.setter
    def SpecifiedBackupId(self, SpecifiedBackupId):
        self._SpecifiedBackupId = SpecifiedBackupId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecifiedRollbackTime = params.get("SpecifiedRollbackTime")
        self._SpecifiedBackupId = params.get("SpecifiedBackupId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Cpu = params.get("Cpu")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        self._DeviceType = params.get("DeviceType")
        self._InstanceNodes = params.get("InstanceNodes")
        self._DeployGroupId = params.get("DeployGroupId")
        self._DryRun = params.get("DryRun")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    """CreateCloneInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: LimitAsync task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _User: TencentDB username
        :type User: str
        :param _FileName: Filename. The file must be a .sql file uploaded to Tencent Cloud.
        :type FileName: str
        :param _Password: Password of a TencentDB instance user account
        :type Password: str
        :param _DbName: Name of the target database. If this parameter is not passed in, no database is specified.
        :type DbName: str
        :param _CosUrl: URL of a .sql file stored in COS. Either `FileName` or `CosUrl` must be specified.
        :type CosUrl: str
        """
        self._InstanceId = None
        self._User = None
        self._FileName = None
        self._Password = None
        self._DbName = None
        self._CosUrl = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._FileName = params.get("FileName")
        self._Password = params.get("Password")
        self._DbName = params.get("DbName")
        self._CosUrl = params.get("CosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour request structure.

    """

    def __init__(self):
        r"""
        :param _GoodsNum: Number of instances. Value range: 1-100. Default value: 1.
        :type GoodsNum: int
        :param _Memory: Instance memory size in MB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported memory specifications.
        :type Memory: int
        :param _Volume: Instance disk size in GB. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported disk specifications.
        :type Volume: int
        :param _EngineVersion: MySQL version. Valid values: `5.5`, `5.6`, `5.7`, `8.0`. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported versions.
        :type EngineVersion: str
        :param _UniqVpcId: VPC ID. If this parameter is not passed in, the basic network will be selected by default. Please use the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API to query the VPCs.
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. Please use the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API to query the subnet lists.
        :type UniqSubnetId: str
        :param _ProjectId: Project ID. If this is left empty, the default project will be used.
        :type ProjectId: int
        :param _Zone: AZ information. By default, the system will automatically select an AZ. Please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported AZs.
        :type Zone: str
        :param _MasterInstanceId: Instance ID, which is required and the same as the primary instance ID when purchasing read-only or disaster recovery instances. Please use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance IDs.
        :type MasterInstanceId: str
        :param _InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.
        :type InstanceRole: str
        :param _MasterRegion: Region information of the source instance, which is required when purchasing a read-only or disaster recovery instance.
        :type MasterRegion: str
        :param _Port: Custom port. Value range: [1024-65535].
        :type Port: int
        :param _Password: Sets the root account password. Rule: the password can contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special symbols (_+-&=!@#$%^*()). This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type Password: str
        :param _ParamList: List of parameters in the format of `ParamList.0.Name=auto_increment&ParamList.0.Value=1`. You can use the [DescribeDefaultParams](https://intl.cloud.tencent.com/document/api/236/32662?from_cn_redirect=1) API to query the configurable parameters.
        :type ParamList: list of ParamInfo
        :param _ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type ProtectMode: int
        :param _DeployMode: Multi-AZ. Valid value: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type DeployMode: int
        :param _SlaveZone: AZ information of secondary database 1, which is the `Zone` value by default. This parameter can be specified when purchasing primary instances and is meaningless for read-only or disaster recovery instances.
        :type SlaveZone: str
        :param _BackupZone: The availability zone information of Replica 2, which is left empty by default. Specify this parameter when purchasing a source instance in the one-source-two-replica architecture.
        :type BackupZone: str
        :param _SecurityGroup: Security group parameter. You can use the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API to query the security group details of a project.
        :type SecurityGroup: list of str
        :param _RoGroup: Read-only instance information. This parameter must be passed in when purchasing read-only instances.
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param _AutoRenewFlag: This field is meaningless when purchasing pay-as-you-go instances.
        :type AutoRenewFlag: int
        :param _InstanceName: Instance name For multiple instances purchased at one time, they will be distinguished by the name suffix number, such as instnaceName=db and goodsNum=3, and their instance names are db1, db2, and db3, respectively.
        :type InstanceName: str
        :param _ResourceTags: Instance tag information.
        :type ResourceTags: list of TagInfo
        :param _DeployGroupId: Placement group ID.
        :type DeployGroupId: str
        :param _ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _DeviceType: Instance resource isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param _ParamTemplateId: Parameter template ID.
        :type ParamTemplateId: int
        :param _AlarmPolicyList: Array of alarm policy IDs,  which is `OriginId` obtained through the `DescribeAlarmPolicy` API.
        :type AlarmPolicyList: list of int
        :param _InstanceNodes: The number of nodes of the instance. To purchase a read-only replica or a basic instance, set this parameter to `1` or leave it empty. To purchase a three-node instance, set this parameter to `3` or specify the `BackupZone` parameter. If the instance to be purchased is a source instance and both `BackupZone` and this parameter are left empty, the value `2` will be used, which indicates the source instance will have two nodes.
        :type InstanceNodes: int
        :param _Cpu: The number of CPU cores of the instance. If this parameter is left empty, the number of CPU cores depends on the `Memory` value.
        :type Cpu: int
        :param _AutoSyncFlag: Whether to automatically start disaster recovery synchronization. This parameter takes effect only for disaster recovery instances. Valid values: `0` (no), `1` (yes). Default value: `0`.
        :type AutoSyncFlag: int
        :param _CageId: Financial cage ID.
        :type CageId: str
        :param _ParamTemplateType: Type of the default parameter template. Valid values: `HIGH_STABILITY` (high-stability template), `HIGH_PERFORMANCE` (high-performance template). Default value: `HIGH_STABILITY`.
        :type ParamTemplateType: str
        :param _AlarmPolicyIdList: The array of alarm policy names, such as ["policy-uyoee9wg"]. If the `AlarmPolicyList` parameter is specified, this parameter is invalid.
        :type AlarmPolicyIdList: list of str
        :param _DryRun: Whether to check the request without creating any instance. Valid values: `true`, `false` (default). After being submitted, the request will be checked to see if it is in correct format and has all required parameters with valid values. An error code is returned if the check failed, and `RequestId` is returned if the check succeeded. After a successful check, no instance will be created if this parameter is set to `true`, whereas an instance will be created and if it is set to `false`.
        :type DryRun: bool
        :param _EngineType: Instance engine type. Valid values: `InnoDB` (default); `RocksDB`.
        :type EngineType: str
        :param _Vips: The list of IPs for sources instances. Only one IP address can be assigned to a single source instance. If all IPs are used up, the system will automatically assign IPs to the remaining source instances that do not have one.
        :type Vips: list of str
        """
        self._GoodsNum = None
        self._Memory = None
        self._Volume = None
        self._EngineVersion = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProjectId = None
        self._Zone = None
        self._MasterInstanceId = None
        self._InstanceRole = None
        self._MasterRegion = None
        self._Port = None
        self._Password = None
        self._ParamList = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._BackupZone = None
        self._SecurityGroup = None
        self._RoGroup = None
        self._AutoRenewFlag = None
        self._InstanceName = None
        self._ResourceTags = None
        self._DeployGroupId = None
        self._ClientToken = None
        self._DeviceType = None
        self._ParamTemplateId = None
        self._AlarmPolicyList = None
        self._InstanceNodes = None
        self._Cpu = None
        self._AutoSyncFlag = None
        self._CageId = None
        self._ParamTemplateType = None
        self._AlarmPolicyIdList = None
        self._DryRun = None
        self._EngineType = None
        self._Vips = None

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RoGroup(self):
        return self._RoGroup

    @RoGroup.setter
    def RoGroup(self, RoGroup):
        self._RoGroup = RoGroup

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def AutoSyncFlag(self):
        return self._AutoSyncFlag

    @AutoSyncFlag.setter
    def AutoSyncFlag(self, AutoSyncFlag):
        self._AutoSyncFlag = AutoSyncFlag

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ParamTemplateType(self):
        return self._ParamTemplateType

    @ParamTemplateType.setter
    def ParamTemplateType(self, ParamTemplateType):
        self._ParamTemplateType = ParamTemplateType

    @property
    def AlarmPolicyIdList(self):
        return self._AlarmPolicyIdList

    @AlarmPolicyIdList.setter
    def AlarmPolicyIdList(self, AlarmPolicyIdList):
        self._AlarmPolicyIdList = AlarmPolicyIdList

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._EngineVersion = params.get("EngineVersion")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Zone = params.get("Zone")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._MasterRegion = params.get("MasterRegion")
        self._Port = params.get("Port")
        self._Password = params.get("Password")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self._RoGroup = RoGroup()
            self._RoGroup._deserialize(params.get("RoGroup"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DeployGroupId = params.get("DeployGroupId")
        self._ClientToken = params.get("ClientToken")
        self._DeviceType = params.get("DeviceType")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._AutoSyncFlag = params.get("AutoSyncFlag")
        self._CageId = params.get("CageId")
        self._ParamTemplateType = params.get("ParamTemplateType")
        self._AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self._DryRun = params.get("DryRun")
        self._EngineType = params.get("EngineType")
        self._Vips = params.get("Vips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour response structure.

    """

    def __init__(self):
        r"""
        :param _DealIds: Short order ID.
        :type DealIds: list of str
        :param _InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Memory: Instance memory size in MB. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported memory specifications.
        :type Memory: int
        :param _Volume: Instance disk size in GB. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported disk specifications.
        :type Volume: int
        :param _Period: Instance validity period in months. Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`.
        :type Period: int
        :param _GoodsNum: Number of instances. Value range: 1-100. Default value: `1`.
        :type GoodsNum: int
        :param _Zone: AZ information. The system will automatically select an AZ by default. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported AZs.
        :type Zone: str
        :param _UniqVpcId: VPC ID. If this parameter is not passed in, the basic network will be selected by default. You can use the [DescribeVpcs](https://intl.cloud.tencent.com/document/api/215/15778?from_cn_redirect=1) API to query the VPCs.
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID. If `UniqVpcId` is set, then `UniqSubnetId` will be required. You can use the [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) API to query the subnet lists.
        :type UniqSubnetId: str
        :param _ProjectId: Project ID. If this parameter is left empty, the default project will be used. When you purchase read-only instances and disaster recovery instances, the project ID is the same as that of the source instance by default.
        :type ProjectId: int
        :param _Port: Custom port. Value range: 1024-65535.
        :type Port: int
        :param _InstanceRole: Instance typeA. Valid values: `master` (source instance), `dr` (disaster recovery instance), `ro` (read-only instance).
        :type InstanceRole: str
        :param _MasterInstanceId: Instance ID. It is required when purchasing a read-only instance, which is the same as the source instance ID. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the instance ID.
        :type MasterInstanceId: str
        :param _EngineVersion: MySQL version. Valid values: `5.5`, `5.6`, `5.7`. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1) API to query the supported versions.
        :type EngineVersion: str
        :param _Password: The root account password. It can contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and symbols (_+-&=!@#$%^*()). This parameter can be specified when purchasing a replica instance and is invalid for read-only or disaster recovery instances.
        :type Password: str
        :param _ProtectMode: Data replication mode. Valid values: `0` (async replication), `1` (semi-sync replication), `2` (strong sync replication). Default value: `0`.
        :type ProtectMode: int
        :param _DeployMode: Multi-AZ or single-AZ. Valid values: `0` (single-AZ), `1` (multi-AZ). Default value: `0`.
        :type DeployMode: int
        :param _SlaveZone: Information of replica AZ 1, which is the `Zone` value by default.
        :type SlaveZone: str
        :param _ParamList: List of parameters in the format of ParamList.0.Name=auto_increment&ParamList.0.Value=1. You can use the [DescribeDefaultParams](https://intl.cloud.tencent.com/document/api/236/32662?from_cn_redirect=1) API to query the configurable parameters.
        :type ParamList: list of ParamInfo
        :param _BackupZone: Information of replica AZ 2, which is left empty by default. Specify this parameter when purchasing a source instance in the one-source-two-replica architecture.
        :type BackupZone: str
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: `0` (auto-renewal not enabled), `1` (auto-renewal enabled).
        :type AutoRenewFlag: int
        :param _MasterRegion: Region information of the source instance, which is required when purchasing a read-only or disaster recovery instance.
        :type MasterRegion: str
        :param _SecurityGroup: Security group parameter. You can use the [DescribeProjectSecurityGroups](https://intl.cloud.tencent.com/document/api/236/15850?from_cn_redirect=1) API to query the security group details of a project.
        :type SecurityGroup: list of str
        :param _RoGroup: Read-only instance parameter. This parameter must be passed in when purchasing read-only instances.
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param _InstanceName: Instance name. For multiple instances purchased at one time, they will be distinguished by the name suffix number, such as instnaceName=db and goodsNum=3, and their instance names are db1, db2, and db3, respectively.
        :type InstanceName: str
        :param _ResourceTags: Instance tag information
        :type ResourceTags: list of TagInfo
        :param _DeployGroupId: Placement group ID
        :type DeployGroupId: str
        :param _ClientToken: A string unique in 48 hours, which is supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param _DeviceType: Instance isolation type. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param _ParamTemplateId: Parameter template ID
        :type ParamTemplateId: int
        :param _AlarmPolicyList: Array of alarm policy IDs, which is `OriginId` obtained through the `DescribeAlarmPolicy` API.
        :type AlarmPolicyList: list of int
        :param _InstanceNodes: The number of nodes of the instance. To purchase a read-only instance or a basic instance, set this parameter to `1` or leave it empty. To purchase a three-node instance, set this parameter to `3` or specify the `BackupZone` parameter. If the instance to be purchased is a source instance and both `BackupZone` and this parameter are left empty, the value `2` will be used, which indicates the source instance will have two nodes.
        :type InstanceNodes: int
        :param _Cpu: The number of the instance CPU cores. If this parameter is left empty, it will be subject to the `Memory` value.
        :type Cpu: int
        :param _AutoSyncFlag: Whether to automatically start disaster recovery synchronization. This parameter takes effect only for disaster recovery instances. Valid values: `0` (no), `1` (yes). Default value: `0`.
        :type AutoSyncFlag: int
        :param _CageId: Financial cage ID.
        :type CageId: str
        :param _ParamTemplateType: Type of the default parameter template. Valid values: `HIGH_STABILITY` (high-stability template), `HIGH_PERFORMANCE` (high-performance template).
        :type ParamTemplateType: str
        :param _AlarmPolicyIdList: The array of alarm policy names, such as ["policy-uyoee9wg"]. If the `AlarmPolicyList` parameter is specified, this parameter is invalid.
        :type AlarmPolicyIdList: list of str
        :param _DryRun: Whether to check the request without creating any instance. Valid values: `true`, `false` (default). After being submitted, the request will be checked to see if it is in correct format and has all required parameters with valid values. An error code is returned if the check failed, and `RequestId` is returned if the check succeeded. After a successful check, no instance will be created if this parameter is set to `true`, whereas an instance will be created and if it is set to `false`.
        :type DryRun: bool
        :param _EngineType: Instance engine type. Valid values: `InnoDB` (default), `RocksDB`.
        :type EngineType: str
        :param _Vips: The list of IPs for sources instances. Only one IP address can be assigned to a single source instance. If all IPs are used up, the system will automatically assign IPs to the remaining source instances that do not have one.
        :type Vips: list of str
        """
        self._Memory = None
        self._Volume = None
        self._Period = None
        self._GoodsNum = None
        self._Zone = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ProjectId = None
        self._Port = None
        self._InstanceRole = None
        self._MasterInstanceId = None
        self._EngineVersion = None
        self._Password = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._ParamList = None
        self._BackupZone = None
        self._AutoRenewFlag = None
        self._MasterRegion = None
        self._SecurityGroup = None
        self._RoGroup = None
        self._InstanceName = None
        self._ResourceTags = None
        self._DeployGroupId = None
        self._ClientToken = None
        self._DeviceType = None
        self._ParamTemplateId = None
        self._AlarmPolicyList = None
        self._InstanceNodes = None
        self._Cpu = None
        self._AutoSyncFlag = None
        self._CageId = None
        self._ParamTemplateType = None
        self._AlarmPolicyIdList = None
        self._DryRun = None
        self._EngineType = None
        self._Vips = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RoGroup(self):
        return self._RoGroup

    @RoGroup.setter
    def RoGroup(self, RoGroup):
        self._RoGroup = RoGroup

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ParamTemplateId(self):
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def AutoSyncFlag(self):
        return self._AutoSyncFlag

    @AutoSyncFlag.setter
    def AutoSyncFlag(self, AutoSyncFlag):
        self._AutoSyncFlag = AutoSyncFlag

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ParamTemplateType(self):
        return self._ParamTemplateType

    @ParamTemplateType.setter
    def ParamTemplateType(self, ParamTemplateType):
        self._ParamTemplateType = ParamTemplateType

    @property
    def AlarmPolicyIdList(self):
        return self._AlarmPolicyIdList

    @AlarmPolicyIdList.setter
    def AlarmPolicyIdList(self, AlarmPolicyIdList):
        self._AlarmPolicyIdList = AlarmPolicyIdList

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._Period = params.get("Period")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ProjectId = params.get("ProjectId")
        self._Port = params.get("Port")
        self._InstanceRole = params.get("InstanceRole")
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._EngineVersion = params.get("EngineVersion")
        self._Password = params.get("Password")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._BackupZone = params.get("BackupZone")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._MasterRegion = params.get("MasterRegion")
        self._SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self._RoGroup = RoGroup()
            self._RoGroup._deserialize(params.get("RoGroup"))
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._DeployGroupId = params.get("DeployGroupId")
        self._ClientToken = params.get("ClientToken")
        self._DeviceType = params.get("DeviceType")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._AutoSyncFlag = params.get("AutoSyncFlag")
        self._CageId = params.get("CageId")
        self._ParamTemplateType = params.get("ParamTemplateType")
        self._AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self._DryRun = params.get("DryRun")
        self._EngineType = params.get("EngineType")
        self._Vips = params.get("Vips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealIds: Short order ID
        :type DealIds: list of str
        :param _InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealIds = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDatabaseRequest(AbstractModel):
    """CreateDatabase request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `cdb-c1nl9rpv`,  which is the same as the one displayed in the TencentDB console.
        :type InstanceId: str
        :param _DBName: 
        :type DBName: str
        :param _CharacterSetName: Character set. Valid values:  `utf8`, `gbk`, `latin1`, `utf8mb4`.
        :type CharacterSetName: str
        """
        self._InstanceId = None
        self._DBName = None
        self._CharacterSetName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DBName(self):
        return self._DBName

    @DBName.setter
    def DBName(self, DBName):
        self._DBName = DBName

    @property
    def CharacterSetName(self):
        return self._CharacterSetName

    @CharacterSetName.setter
    def CharacterSetName(self, CharacterSetName):
        self._CharacterSetName = CharacterSetName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DBName = params.get("DBName")
        self._CharacterSetName = params.get("CharacterSetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseResponse(AbstractModel):
    """CreateDatabase response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Parameter template name.
        :type Name: str
        :param _Description: Parameter template description.
        :type Description: str
        :param _EngineVersion: MySQL version number.
        :type EngineVersion: str
        :param _TemplateId: Source parameter template ID.
        :type TemplateId: int
        :param _ParamList: List of parameters.
        :type ParamList: list of Parameter
        :param _TemplateType: Type of the default parameter template. Valid values: `HIGH_STABILITY` (high-stability template), `HIGH_PERFORMANCE` (high-performance template).
        :type TemplateType: str
        :param _EngineType: Instance engine type. Valid values: `InnoDB` (default), `RocksDB`.
        :type EngineType: str
        """
        self._Name = None
        self._Description = None
        self._EngineVersion = None
        self._TemplateId = None
        self._ParamList = None
        self._TemplateType = None
        self._EngineType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateRoInstanceIpRequest(AbstractModel):
    """CreateRoInstanceIp request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Read-only instance ID in the format of "cdbro-3i70uj0k". Its value is the same as the read-only instance ID in the TencentDB Console.
        :type InstanceId: str
        :param _UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d".
        :type UniqSubnetId: str
        :param _UniqVpcId: VPC descriptor, such as "vpc-a23yt67j". If this field is passed in, `UniqSubnetId` will be required.
        :type UniqVpcId: str
        """
        self._InstanceId = None
        self._UniqSubnetId = None
        self._UniqVpcId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoInstanceIpResponse(AbstractModel):
    """CreateRoInstanceIp response structure.

    """

    def __init__(self):
        r"""
        :param _RoVpcId: VPC ID of the read-only instance.
        :type RoVpcId: int
        :param _RoSubnetId: Subnet ID of the read-only instance.
        :type RoSubnetId: int
        :param _RoVip: Private IP address of the read-only instance.
        :type RoVip: str
        :param _RoVport: Private port number of the read-only instance.
        :type RoVport: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoVpcId = None
        self._RoSubnetId = None
        self._RoVip = None
        self._RoVport = None
        self._RequestId = None

    @property
    def RoVpcId(self):
        return self._RoVpcId

    @RoVpcId.setter
    def RoVpcId(self, RoVpcId):
        self._RoVpcId = RoVpcId

    @property
    def RoSubnetId(self):
        return self._RoSubnetId

    @RoSubnetId.setter
    def RoSubnetId(self, RoSubnetId):
        self._RoSubnetId = RoSubnetId

    @property
    def RoVip(self):
        return self._RoVip

    @RoVip.setter
    def RoVip(self, RoVip):
        self._RoVip = RoVip

    @property
    def RoVport(self):
        return self._RoVport

    @RoVport.setter
    def RoVport(self, RoVport):
        self._RoVport = RoVport

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoVpcId = params.get("RoVpcId")
        self._RoSubnetId = params.get("RoSubnetId")
        self._RoVip = params.get("RoVip")
        self._RoVport = params.get("RoVport")
        self._RequestId = params.get("RequestId")


class CustomConfig(AbstractModel):
    """Proxy configuration

    """

    def __init__(self):
        r"""
        :param _Device: Device
Note: this field may return `null`, indicating that no valid value can be found.
        :type Device: str
        :param _Type: Type
Note: this field may return `null`, indicating that no valid value can be found.
        :type Type: str
        :param _DeviceType: Device type
Note: this field may return `null`, indicating that no valid value can be found.
        :type DeviceType: str
        :param _Memory: Memory
Note: this field may return `null`, indicating that no valid value can be found.
        :type Memory: int
        :param _Cpu: Number of CPU cores
Note: this field may return `null`, indicating that no valid value can be found.
        :type Cpu: int
        """
        self._Device = None
        self._Type = None
        self._DeviceType = None
        self._Memory = None
        self._Cpu = None

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu


    def _deserialize(self, params):
        self._Device = params.get("Device")
        self._Type = params.get("Type")
        self._DeviceType = params.get("DeviceType")
        self._Memory = params.get("Memory")
        self._Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBSwitchInfo(AbstractModel):
    """TencentDB instance switch records

    """

    def __init__(self):
        r"""
        :param _SwitchTime: Switch time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-09-03 01:34:31
        :type SwitchTime: str
        :param _SwitchType: Switch type. Value range: TRANSFER (data migration), MASTER2SLAVE (primary/secondary switch), RECOVERY (primary/secondary recovery)
        :type SwitchType: str
        """
        self._SwitchTime = None
        self._SwitchType = None

    @property
    def SwitchTime(self):
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime

    @property
    def SwitchType(self):
        return self._SwitchType

    @SwitchType.setter
    def SwitchType(self, SwitchType):
        self._SwitchType = SwitchType


    def _deserialize(self, params):
        self._SwitchTime = params.get("SwitchTime")
        self._SwitchType = params.get("SwitchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        r"""
        :param _Privileges: Permission information
        :type Privileges: list of str
        :param _Database: Database name
        :type Database: str
        """
        self._Privileges = None
        self._Database = None

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database


    def _deserialize(self, params):
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesWithCharacterLists(AbstractModel):
    """Database name and character set

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Database name
        :type DatabaseName: str
        :param _CharacterSet: Character set
        :type CharacterSet: str
        """
        self._DatabaseName = None
        self._CharacterSet = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def CharacterSet(self):
        return self._CharacterSet

    @CharacterSet.setter
    def CharacterSet(self, CharacterSet):
        self._CharacterSet = CharacterSet


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._CharacterSet = params.get("CharacterSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Accounts: TencentDB account.
        :type Accounts: list of Account
        """
        self._InstanceId = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _BackupId: Backup task ID, which is the task ID returned by the [TencentDB instance backup creating API](https://intl.cloud.tencent.com/document/api/236/15844?from_cn_redirect=1).
        :type BackupId: int
        """
        self._InstanceId = None
        self._BackupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _User: Database user account.
        :type User: str
        :param _Host: Database account domain name.
        :type Host: str
        """
        self._InstanceId = None
        self._User = None
        self._Host = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalPrivileges: Array of global permissions.
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Array of database permissions.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: Array of table permissions in the database.
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: Array of column permissions in the table.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._RequestId = None

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _Offset: Record offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Value range: 1-100. Default value: `20`.
        :type Limit: int
        :param _AccountRegexp: Regex for matching account names, which complies with the rules at MySQL's official website
        :type AccountRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._AccountRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AccountRegexp(self):
        return self._AccountRegexp

    @AccountRegexp.setter
    def AccountRegexp(self, AccountRegexp):
        self._AccountRegexp = AccountRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AccountRegexp = params.get("AccountRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible accounts
        :type TotalCount: int
        :param _Items: Details of eligible accounts
        :type Items: list of AccountInfo
        :param _MaxUserConnections: The maximum number of instance connections
        :type MaxUserConnections: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._MaxUserConnections = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._MaxUserConnections = params.get("MaxUserConnections")
        self._RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task execution result. Valid values: INITIAL, RUNNING, SUCCESS, FAILED, KILLED, REMOVED, PAUSED.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Info: Task execution information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Info: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DescribeAuditPoliciesRequest(AbstractModel):
    """DescribeAuditPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _PolicyId: Audit policy ID.
        :type PolicyId: str
        :param _PolicyName: Audit policy name. Fuzzy match query is supported.
        :type PolicyName: str
        :param _Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _RuleId: Audit rule ID, which can be used to query its associated audit policies.
Note: At least one of the parameters (“RuleId”, “PolicyId”, PolicyId”, or “PolicyName”) must be passed in.
        :type RuleId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        """
        self._InstanceId = None
        self._PolicyId = None
        self._PolicyName = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditPoliciesResponse(AbstractModel):
    """DescribeAuditPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible audit policies
        :type TotalCount: int
        :param _Items: Audit policy details
Note: This field may return `null`, indicating that no valid value was found.
        :type Items: list of AuditPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditRulesRequest(AbstractModel):
    """DescribeAuditRules request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Audit rule ID.
        :type RuleId: str
        :param _RuleName: Audit rule name. Fuzzy match query is supported.
        :type RuleName: str
        :param _Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _Offset: Pagination offset. Default value: 0
        :type Offset: int
        """
        self._RuleId = None
        self._RuleName = None
        self._Limit = None
        self._Offset = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRulesResponse(AbstractModel):
    """DescribeAuditRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible audit rules
        :type TotalCount: int
        :param _Items: Audit rule details
Note: This field may return `null`, indicating that no valid value was found.
        :type Items: list of AuditRule
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuditRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _StartTimeMin: Earliest start time point of automatic backup, such as 2 (for 2:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)
        :type StartTimeMin: int
        :param _StartTimeMax: Latest start time point of automatic backup, such as 6 (for 6:00 AM). (This field has been disused. You are recommended to use the `BackupTimeWindow` field)
        :type StartTimeMax: int
        :param _BackupExpireDays: Backup file retention period in days.
        :type BackupExpireDays: int
        :param _BackupMethod: Backup mode. Value range: physical, logical
        :type BackupMethod: str
        :param _BinlogExpireDays: Binlog file retention period in days.
        :type BinlogExpireDays: int
        :param _BackupTimeWindow: Time window for automatic instance backup.
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param _EnableBackupPeriodSave: Switch for archive backup retention. Valid values: `off` (disable), `on` (enable). Default value:`off`.
        :type EnableBackupPeriodSave: str
        :param _BackupPeriodSaveDays: Maximum days of archive backup retention. Valid range: 90-3650. Default value: 1080.
        :type BackupPeriodSaveDays: int
        :param _BackupPeriodSaveInterval: Archive backup retention period. Valid values: `weekly` (a week), `monthly` (a month), `quarterly` (a quarter), `yearly` (a year). Default value: `monthly`.
        :type BackupPeriodSaveInterval: str
        :param _BackupPeriodSaveCount: Number of archive backups. Minimum value: `1`, Maximum value: Number of non-archive backups in archive backup retention period. Default value: `1`.
        :type BackupPeriodSaveCount: int
        :param _StartBackupPeriodSaveDate: The start time in the format: yyyy-mm-dd HH:MM:SS, which is used to enable archive backup retention policy.
        :type StartBackupPeriodSaveDate: str
        :param _EnableBackupArchive: Whether to enable the archive backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBackupArchive: str
        :param _BackupArchiveDays: The period (in days) of how long a data backup is retained before being archived, which falls between 180 days and the number of days from the time it is created until it expires.
        :type BackupArchiveDays: int
        :param _EnableBinlogArchive: Whether to enable the archive backup of logs. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBinlogArchive: str
        :param _BinlogArchiveDays: The period (in days) of how long a log backup is retained before being archived, which falls between 180 days and the number of days from the time it is created until it expires.
        :type BinlogArchiveDays: int
        :param _EnableBackupStandby: Whether to enable the standard storage policy for data backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBackupStandby: str
        :param _BackupStandbyDays: The period (in days) of how long a data backup is retained before switching to standard storage, which falls between 30 days and the number of days from the time it is created until it expires. If the archive backup is enabled, this period cannot be greater than archive backup period.
        :type BackupStandbyDays: int
        :param _EnableBinlogStandby: Whether to enable the standard storage policy for log backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBinlogStandby: str
        :param _BinlogStandbyDays: The period (in days) of how long a log backup is retained before switching to standard storage, which falls between 30 days and the number of days from the time it is created until it expires. If the archive backup is enabled, this period cannot be greater than archive backup period.
        :type BinlogStandbyDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTimeMin = None
        self._StartTimeMax = None
        self._BackupExpireDays = None
        self._BackupMethod = None
        self._BinlogExpireDays = None
        self._BackupTimeWindow = None
        self._EnableBackupPeriodSave = None
        self._BackupPeriodSaveDays = None
        self._BackupPeriodSaveInterval = None
        self._BackupPeriodSaveCount = None
        self._StartBackupPeriodSaveDate = None
        self._EnableBackupArchive = None
        self._BackupArchiveDays = None
        self._EnableBinlogArchive = None
        self._BinlogArchiveDays = None
        self._EnableBackupStandby = None
        self._BackupStandbyDays = None
        self._EnableBinlogStandby = None
        self._BinlogStandbyDays = None
        self._RequestId = None

    @property
    def StartTimeMin(self):
        return self._StartTimeMin

    @StartTimeMin.setter
    def StartTimeMin(self, StartTimeMin):
        self._StartTimeMin = StartTimeMin

    @property
    def StartTimeMax(self):
        return self._StartTimeMax

    @StartTimeMax.setter
    def StartTimeMax(self, StartTimeMax):
        self._StartTimeMax = StartTimeMax

    @property
    def BackupExpireDays(self):
        return self._BackupExpireDays

    @BackupExpireDays.setter
    def BackupExpireDays(self, BackupExpireDays):
        self._BackupExpireDays = BackupExpireDays

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BinlogExpireDays(self):
        return self._BinlogExpireDays

    @BinlogExpireDays.setter
    def BinlogExpireDays(self, BinlogExpireDays):
        self._BinlogExpireDays = BinlogExpireDays

    @property
    def BackupTimeWindow(self):
        return self._BackupTimeWindow

    @BackupTimeWindow.setter
    def BackupTimeWindow(self, BackupTimeWindow):
        self._BackupTimeWindow = BackupTimeWindow

    @property
    def EnableBackupPeriodSave(self):
        return self._EnableBackupPeriodSave

    @EnableBackupPeriodSave.setter
    def EnableBackupPeriodSave(self, EnableBackupPeriodSave):
        self._EnableBackupPeriodSave = EnableBackupPeriodSave

    @property
    def BackupPeriodSaveDays(self):
        return self._BackupPeriodSaveDays

    @BackupPeriodSaveDays.setter
    def BackupPeriodSaveDays(self, BackupPeriodSaveDays):
        self._BackupPeriodSaveDays = BackupPeriodSaveDays

    @property
    def BackupPeriodSaveInterval(self):
        return self._BackupPeriodSaveInterval

    @BackupPeriodSaveInterval.setter
    def BackupPeriodSaveInterval(self, BackupPeriodSaveInterval):
        self._BackupPeriodSaveInterval = BackupPeriodSaveInterval

    @property
    def BackupPeriodSaveCount(self):
        return self._BackupPeriodSaveCount

    @BackupPeriodSaveCount.setter
    def BackupPeriodSaveCount(self, BackupPeriodSaveCount):
        self._BackupPeriodSaveCount = BackupPeriodSaveCount

    @property
    def StartBackupPeriodSaveDate(self):
        return self._StartBackupPeriodSaveDate

    @StartBackupPeriodSaveDate.setter
    def StartBackupPeriodSaveDate(self, StartBackupPeriodSaveDate):
        self._StartBackupPeriodSaveDate = StartBackupPeriodSaveDate

    @property
    def EnableBackupArchive(self):
        return self._EnableBackupArchive

    @EnableBackupArchive.setter
    def EnableBackupArchive(self, EnableBackupArchive):
        self._EnableBackupArchive = EnableBackupArchive

    @property
    def BackupArchiveDays(self):
        return self._BackupArchiveDays

    @BackupArchiveDays.setter
    def BackupArchiveDays(self, BackupArchiveDays):
        self._BackupArchiveDays = BackupArchiveDays

    @property
    def EnableBinlogArchive(self):
        return self._EnableBinlogArchive

    @EnableBinlogArchive.setter
    def EnableBinlogArchive(self, EnableBinlogArchive):
        self._EnableBinlogArchive = EnableBinlogArchive

    @property
    def BinlogArchiveDays(self):
        return self._BinlogArchiveDays

    @BinlogArchiveDays.setter
    def BinlogArchiveDays(self, BinlogArchiveDays):
        self._BinlogArchiveDays = BinlogArchiveDays

    @property
    def EnableBackupStandby(self):
        return self._EnableBackupStandby

    @EnableBackupStandby.setter
    def EnableBackupStandby(self, EnableBackupStandby):
        self._EnableBackupStandby = EnableBackupStandby

    @property
    def BackupStandbyDays(self):
        return self._BackupStandbyDays

    @BackupStandbyDays.setter
    def BackupStandbyDays(self, BackupStandbyDays):
        self._BackupStandbyDays = BackupStandbyDays

    @property
    def EnableBinlogStandby(self):
        return self._EnableBinlogStandby

    @EnableBinlogStandby.setter
    def EnableBinlogStandby(self, EnableBinlogStandby):
        self._EnableBinlogStandby = EnableBinlogStandby

    @property
    def BinlogStandbyDays(self):
        return self._BinlogStandbyDays

    @BinlogStandbyDays.setter
    def BinlogStandbyDays(self, BinlogStandbyDays):
        self._BinlogStandbyDays = BinlogStandbyDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTimeMin = params.get("StartTimeMin")
        self._StartTimeMax = params.get("StartTimeMax")
        self._BackupExpireDays = params.get("BackupExpireDays")
        self._BackupMethod = params.get("BackupMethod")
        self._BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self._BackupTimeWindow = CommonTimeWindow()
            self._BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self._EnableBackupPeriodSave = params.get("EnableBackupPeriodSave")
        self._BackupPeriodSaveDays = params.get("BackupPeriodSaveDays")
        self._BackupPeriodSaveInterval = params.get("BackupPeriodSaveInterval")
        self._BackupPeriodSaveCount = params.get("BackupPeriodSaveCount")
        self._StartBackupPeriodSaveDate = params.get("StartBackupPeriodSaveDate")
        self._EnableBackupArchive = params.get("EnableBackupArchive")
        self._BackupArchiveDays = params.get("BackupArchiveDays")
        self._EnableBinlogArchive = params.get("EnableBinlogArchive")
        self._BinlogArchiveDays = params.get("BinlogArchiveDays")
        self._EnableBackupStandby = params.get("EnableBackupStandby")
        self._BackupStandbyDays = params.get("BackupStandbyDays")
        self._EnableBinlogStandby = params.get("EnableBinlogStandby")
        self._BinlogStandbyDays = params.get("BinlogStandbyDays")
        self._RequestId = params.get("RequestId")


class DescribeBackupDecryptionKeyRequest(AbstractModel):
    """DescribeBackupDecryptionKey request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of  cdb-XXXX,  which is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _BackupId: Instance backup ID, which can be obtained by the `DescribeBackups` API.
        :type BackupId: int
        """
        self._InstanceId = None
        self._BackupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDecryptionKeyResponse(AbstractModel):
    """DescribeBackupDecryptionKey response structure.

    """

    def __init__(self):
        r"""
        :param _DecryptionKey: The decryption key of a backup file
        :type DecryptionKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DecryptionKey = None
        self._RequestId = None

    @property
    def DecryptionKey(self):
        return self._DecryptionKey

    @DecryptionKey.setter
    def DecryptionKey(self, DecryptionKey):
        self._DecryptionKey = DecryptionKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DecryptionKey = params.get("DecryptionKey")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction request structure.

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _LimitType: Valid values: `NoLimit` (backups can be downloaded over both private and public networks with any IPs), `LimitOnlyIntranet` (backups can be downloaded over the private network with any private IPs), `Customize` (backups can be downloaded over specified VPCs with specified IPs). The `LimitVpc` and `LimitIp` parameters are valid only when this parameter is set to `Customize`.
        :type LimitType: str
        :param _VpcComparisonSymbol: Valid value: `In` (backups can only be downloaded over the VPCs specified in `LimitVpc`).
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Valid values: `In` (backups can only be downloaded with the IPs specified in `LimitIp`), `NotIn` (backups cannot be downloaded with the IPs specified in `LimitIp`).
        :type IpComparisonSymbol: str
        :param _LimitVpc: VPCs used to restrict backup download.
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: IPs used to restrict backup download.
        :type LimitIp: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None
        self._RequestId = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        self._RequestId = params.get("RequestId")


class DescribeBackupEncryptionStatusRequest(AbstractModel):
    """DescribeBackupEncryptionStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-XXXX, which is the same as that displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupEncryptionStatusResponse(AbstractModel):
    """DescribeBackupEncryptionStatus response structure.

    """

    def __init__(self):
        r"""
        :param _EncryptionStatus: Whether the physical cold backup is enabled for the instance. Valid values: `on`, `off`.
        :type EncryptionStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EncryptionStatus = None
        self._RequestId = None

    @property
    def EncryptionStatus(self):
        return self._EncryptionStatus

    @EncryptionStatus.setter
    def EncryptionStatus(self, EncryptionStatus):
        self._EncryptionStatus = EncryptionStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptionStatus = params.get("EncryptionStatus")
        self._RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupOverviewResponse(AbstractModel):
    """DescribeBackupOverview response structure.

    """

    def __init__(self):
        r"""
        :param _BackupCount: Total number of backups of a user in the current region (including data backups and log backups).
        :type BackupCount: int
        :param _BackupVolume: Total capacity of backups of a user in the current region.
        :type BackupVolume: int
        :param _BillingVolume: Paid capacity of backups of a user in the current region, i.e., capacity that exceeds the free tier.
        :type BillingVolume: int
        :param _FreeVolume: Backup capacity in the free tier of a user in the current region.
        :type FreeVolume: int
        :param _RemoteBackupVolume: Total capacity of backups of a user in the current region
Note: This field may return null, indicating that no valid value can be obtained.
        :type RemoteBackupVolume: int
        :param _BackupArchiveVolume: Archive backup capacity, which includes data backups and log backups.
Note: This field may return null, indicating that no valid value can be obtained.
        :type BackupArchiveVolume: int
        :param _BackupStandbyVolume: Backup capacity of standard storage, which includes data backups and log backups.
Note: This field may return null, indicating that no valid value can be obtained.
        :type BackupStandbyVolume: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupCount = None
        self._BackupVolume = None
        self._BillingVolume = None
        self._FreeVolume = None
        self._RemoteBackupVolume = None
        self._BackupArchiveVolume = None
        self._BackupStandbyVolume = None
        self._RequestId = None

    @property
    def BackupCount(self):
        return self._BackupCount

    @BackupCount.setter
    def BackupCount(self, BackupCount):
        self._BackupCount = BackupCount

    @property
    def BackupVolume(self):
        return self._BackupVolume

    @BackupVolume.setter
    def BackupVolume(self, BackupVolume):
        self._BackupVolume = BackupVolume

    @property
    def BillingVolume(self):
        return self._BillingVolume

    @BillingVolume.setter
    def BillingVolume(self, BillingVolume):
        self._BillingVolume = BillingVolume

    @property
    def FreeVolume(self):
        return self._FreeVolume

    @FreeVolume.setter
    def FreeVolume(self, FreeVolume):
        self._FreeVolume = FreeVolume

    @property
    def RemoteBackupVolume(self):
        return self._RemoteBackupVolume

    @RemoteBackupVolume.setter
    def RemoteBackupVolume(self, RemoteBackupVolume):
        self._RemoteBackupVolume = RemoteBackupVolume

    @property
    def BackupArchiveVolume(self):
        return self._BackupArchiveVolume

    @BackupArchiveVolume.setter
    def BackupArchiveVolume(self, BackupArchiveVolume):
        self._BackupArchiveVolume = BackupArchiveVolume

    @property
    def BackupStandbyVolume(self):
        return self._BackupStandbyVolume

    @BackupStandbyVolume.setter
    def BackupStandbyVolume(self, BackupStandbyVolume):
        self._BackupStandbyVolume = BackupStandbyVolume

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupCount = params.get("BackupCount")
        self._BackupVolume = params.get("BackupVolume")
        self._BillingVolume = params.get("BillingVolume")
        self._FreeVolume = params.get("FreeVolume")
        self._RemoteBackupVolume = params.get("RemoteBackupVolume")
        self._BackupArchiveVolume = params.get("BackupArchiveVolume")
        self._BackupStandbyVolume = params.get("BackupStandbyVolume")
        self._RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    """DescribeBackupSummaries request structure.

    """

    def __init__(self):
        r"""
        :param _Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        :param _Offset: Paginated query offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Maximum entries returned per page, which ranges from 1 to 100. Default value: `20`.
        :type Limit: int
        :param _OrderBy: Sorting criterion. Valid values: `BackupVolume` (backup capacity), `DataBackupVolume` (data backup capacity), `BinlogBackupVolume` (log backup capacity), `AutoBackupVolume` (automatic backup capacity), `ManualBackupVolume` (manual backup capacity). Default value: `BackupVolume`.
        :type OrderBy: str
        :param _OrderDirection: Sorting order. Valid values: `ASC` (ascending), `DESC` (descending). Default value: `ASC`.
        :type OrderDirection: str
        """
        self._Product = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderDirection = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    """DescribeBackupSummaries response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Statistical items of instance backup.
        :type Items: list of BackupSummaryItem
        :param _TotalCount: Total number of instance backups.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupSummaryItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Details of eligible backups.
        :type Items: list of BackupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBinlogBackupOverviewRequest(AbstractModel):
    """DescribeBinlogBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogBackupOverviewResponse(AbstractModel):
    """DescribeBinlogBackupOverview response structure.

    """

    def __init__(self):
        r"""
        :param _BinlogBackupVolume: Total capacity of log backups in bytes (including remote log backups)
        :type BinlogBackupVolume: int
        :param _BinlogBackupCount: Total number of log backups (include remote log backups)
        :type BinlogBackupCount: int
        :param _RemoteBinlogVolume: Capacity of remote log backups in bytes
        :type RemoteBinlogVolume: int
        :param _RemoteBinlogCount: Number of remote backups
        :type RemoteBinlogCount: int
        :param _BinlogArchiveVolume: Capacity of archive log backups in bytes
        :type BinlogArchiveVolume: int
        :param _BinlogArchiveCount: Number of archived log backups
        :type BinlogArchiveCount: int
        :param _BinlogStandbyVolume: Log backup capacity of standard storage in bytes
        :type BinlogStandbyVolume: int
        :param _BinlogStandbyCount: Number of log backups of standard storage
        :type BinlogStandbyCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BinlogBackupVolume = None
        self._BinlogBackupCount = None
        self._RemoteBinlogVolume = None
        self._RemoteBinlogCount = None
        self._BinlogArchiveVolume = None
        self._BinlogArchiveCount = None
        self._BinlogStandbyVolume = None
        self._BinlogStandbyCount = None
        self._RequestId = None

    @property
    def BinlogBackupVolume(self):
        return self._BinlogBackupVolume

    @BinlogBackupVolume.setter
    def BinlogBackupVolume(self, BinlogBackupVolume):
        self._BinlogBackupVolume = BinlogBackupVolume

    @property
    def BinlogBackupCount(self):
        return self._BinlogBackupCount

    @BinlogBackupCount.setter
    def BinlogBackupCount(self, BinlogBackupCount):
        self._BinlogBackupCount = BinlogBackupCount

    @property
    def RemoteBinlogVolume(self):
        return self._RemoteBinlogVolume

    @RemoteBinlogVolume.setter
    def RemoteBinlogVolume(self, RemoteBinlogVolume):
        self._RemoteBinlogVolume = RemoteBinlogVolume

    @property
    def RemoteBinlogCount(self):
        return self._RemoteBinlogCount

    @RemoteBinlogCount.setter
    def RemoteBinlogCount(self, RemoteBinlogCount):
        self._RemoteBinlogCount = RemoteBinlogCount

    @property
    def BinlogArchiveVolume(self):
        return self._BinlogArchiveVolume

    @BinlogArchiveVolume.setter
    def BinlogArchiveVolume(self, BinlogArchiveVolume):
        self._BinlogArchiveVolume = BinlogArchiveVolume

    @property
    def BinlogArchiveCount(self):
        return self._BinlogArchiveCount

    @BinlogArchiveCount.setter
    def BinlogArchiveCount(self, BinlogArchiveCount):
        self._BinlogArchiveCount = BinlogArchiveCount

    @property
    def BinlogStandbyVolume(self):
        return self._BinlogStandbyVolume

    @BinlogStandbyVolume.setter
    def BinlogStandbyVolume(self, BinlogStandbyVolume):
        self._BinlogStandbyVolume = BinlogStandbyVolume

    @property
    def BinlogStandbyCount(self):
        return self._BinlogStandbyCount

    @BinlogStandbyCount.setter
    def BinlogStandbyCount(self, BinlogStandbyCount):
        self._BinlogStandbyCount = BinlogStandbyCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BinlogBackupVolume = params.get("BinlogBackupVolume")
        self._BinlogBackupCount = params.get("BinlogBackupCount")
        self._RemoteBinlogVolume = params.get("RemoteBinlogVolume")
        self._RemoteBinlogCount = params.get("RemoteBinlogCount")
        self._BinlogArchiveVolume = params.get("BinlogArchiveVolume")
        self._BinlogArchiveCount = params.get("BinlogArchiveCount")
        self._BinlogStandbyVolume = params.get("BinlogStandbyVolume")
        self._BinlogStandbyCount = params.get("BinlogStandbyCount")
        self._RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _MinStartTime: The earliest start time of binlog  in the format of 2016-03-17 02:10:37.
        :type MinStartTime: str
        :param _MaxStartTime: The latest start time of binlog  in the format of 2016-03-17 02:10:37.
        :type MaxStartTime: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._MinStartTime = None
        self._MaxStartTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MinStartTime(self):
        return self._MinStartTime

    @MinStartTime.setter
    def MinStartTime(self, MinStartTime):
        self._MinStartTime = MinStartTime

    @property
    def MaxStartTime(self):
        return self._MaxStartTime

    @MaxStartTime.setter
    def MaxStartTime(self, MaxStartTime):
        self._MaxStartTime = MaxStartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MinStartTime = params.get("MinStartTime")
        self._MaxStartTime = params.get("MaxStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible log files.
        :type TotalCount: int
        :param _Items: Number of eligible binlog files.
        :type Items: list of BinlogInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCDBProxyRequest(AbstractModel):
    """DescribeCDBProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCDBProxyResponse(AbstractModel):
    """DescribeCDBProxy response structure.

    """

    def __init__(self):
        r"""
        :param _BaseGroup: Basic information of the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param _Address: Address information of the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type Address: :class:`tencentcloud.cdb.v20170320.models.Address`
        :param _ProxyNode: Node information of the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNode: :class:`tencentcloud.cdb.v20170320.models.ProxyNodeInfo`
        :param _RWInstInfo: Read/Write separation information
Note: this field may return `null`, indicating that no valid value can be found.
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfo`
        :param _ConnectionPoolInfo: Connection pool information
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param _Count: Number of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type Count: int
        :param _ProxyGroup: Proxy information
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyGroup: list of ProxyGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaseGroup = None
        self._Address = None
        self._ProxyNode = None
        self._RWInstInfo = None
        self._ConnectionPoolInfo = None
        self._Count = None
        self._ProxyGroup = None
        self._RequestId = None

    @property
    def BaseGroup(self):
        return self._BaseGroup

    @BaseGroup.setter
    def BaseGroup(self, BaseGroup):
        self._BaseGroup = BaseGroup

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ProxyNode(self):
        return self._ProxyNode

    @ProxyNode.setter
    def ProxyNode(self, ProxyNode):
        self._ProxyNode = ProxyNode

    @property
    def RWInstInfo(self):
        return self._RWInstInfo

    @RWInstInfo.setter
    def RWInstInfo(self, RWInstInfo):
        self._RWInstInfo = RWInstInfo

    @property
    def ConnectionPoolInfo(self):
        return self._ConnectionPoolInfo

    @ConnectionPoolInfo.setter
    def ConnectionPoolInfo(self, ConnectionPoolInfo):
        self._ConnectionPoolInfo = ConnectionPoolInfo

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProxyGroup(self):
        return self._ProxyGroup

    @ProxyGroup.setter
    def ProxyGroup(self, ProxyGroup):
        self._ProxyGroup = ProxyGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self._BaseGroup = BaseGroupInfo()
            self._BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        if params.get("ProxyNode") is not None:
            self._ProxyNode = ProxyNodeInfo()
            self._ProxyNode._deserialize(params.get("ProxyNode"))
        if params.get("RWInstInfo") is not None:
            self._RWInstInfo = RWInfo()
            self._RWInstInfo._deserialize(params.get("RWInstInfo"))
        if params.get("ConnectionPoolInfo") is not None:
            self._ConnectionPoolInfo = ConnectionPoolInfo()
            self._ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        self._Count = params.get("Count")
        if params.get("ProxyGroup") is not None:
            self._ProxyGroup = []
            for item in params.get("ProxyGroup"):
                obj = ProxyGroup()
                obj._deserialize(item)
                self._ProxyGroup.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdbProxyInfoRequest(AbstractModel):
    """DescribeCdbProxyInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdbProxyInfoResponse(AbstractModel):
    """DescribeCdbProxyInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of proxy groups Note: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        :param _ProxyInfos: Proxy group information Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyInfos: list of ProxyGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._ProxyInfos = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProxyInfos(self):
        return self._ProxyInfos

    @ProxyInfos.setter
    def ProxyInfos(self, ProxyInfos):
        self._ProxyInfos = ProxyInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("ProxyInfos") is not None:
            self._ProxyInfos = []
            for item in params.get("ProxyInfos"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdbZoneConfigRequest(AbstractModel):
    """DescribeCdbZoneConfig request structure.

    """


class DescribeCdbZoneConfigResponse(AbstractModel):
    """DescribeCdbZoneConfig response structure.

    """

    def __init__(self):
        r"""
        :param _DataResult: List of purchasable specification and region information
        :type DataResult: :class:`tencentcloud.cdb.v20170320.models.CdbZoneDataResult`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataResult = None
        self._RequestId = None

    @property
    def DataResult(self):
        return self._DataResult

    @DataResult.setter
    def DataResult(self, DataResult):
        self._DataResult = DataResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataResult") is not None:
            self._DataResult = CdbZoneDataResult()
            self._DataResult._deserialize(params.get("DataResult"))
        self._RequestId = params.get("RequestId")


class DescribeCloneListRequest(AbstractModel):
    """DescribeCloneList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the original instance. This parameter is used to query the clone task list of a specific original instance.
        :type InstanceId: str
        :param _Offset: Paginated query offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of results per page. Default value: `20`.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloneListResponse(AbstractModel):
    """DescribeCloneList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of results which meet the conditions
        :type TotalCount: int
        :param _Items: Clone task list
        :type Items: list of CloneItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CloneItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBFeaturesRequest(AbstractModel):
    """DescribeDBFeatures request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBFeaturesResponse(AbstractModel):
    """DescribeDBFeatures response structure.

    """

    def __init__(self):
        r"""
        :param _IsSupportAudit: Whether database audit is supported
        :type IsSupportAudit: bool
        :param _AuditNeedUpgrade: Whether enabling audit requires a kernel version upgrade
        :type AuditNeedUpgrade: bool
        :param _IsSupportEncryption: Whether database encryption is supported
        :type IsSupportEncryption: bool
        :param _EncryptionNeedUpgrade: Whether enabling encryption requires a kernel version upgrade
        :type EncryptionNeedUpgrade: bool
        :param _IsRemoteRo: Whether the instance is a remote read-only instance
        :type IsRemoteRo: bool
        :param _MasterRegion: Region of the source instance
        :type MasterRegion: str
        :param _IsSupportUpdateSubVersion: Whether minor version upgrade is supported
        :type IsSupportUpdateSubVersion: bool
        :param _CurrentSubVersion: The current kernel version
        :type CurrentSubVersion: str
        :param _TargetSubVersion: Available kernel version for upgrade
        :type TargetSubVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSupportAudit = None
        self._AuditNeedUpgrade = None
        self._IsSupportEncryption = None
        self._EncryptionNeedUpgrade = None
        self._IsRemoteRo = None
        self._MasterRegion = None
        self._IsSupportUpdateSubVersion = None
        self._CurrentSubVersion = None
        self._TargetSubVersion = None
        self._RequestId = None

    @property
    def IsSupportAudit(self):
        return self._IsSupportAudit

    @IsSupportAudit.setter
    def IsSupportAudit(self, IsSupportAudit):
        self._IsSupportAudit = IsSupportAudit

    @property
    def AuditNeedUpgrade(self):
        return self._AuditNeedUpgrade

    @AuditNeedUpgrade.setter
    def AuditNeedUpgrade(self, AuditNeedUpgrade):
        self._AuditNeedUpgrade = AuditNeedUpgrade

    @property
    def IsSupportEncryption(self):
        return self._IsSupportEncryption

    @IsSupportEncryption.setter
    def IsSupportEncryption(self, IsSupportEncryption):
        self._IsSupportEncryption = IsSupportEncryption

    @property
    def EncryptionNeedUpgrade(self):
        return self._EncryptionNeedUpgrade

    @EncryptionNeedUpgrade.setter
    def EncryptionNeedUpgrade(self, EncryptionNeedUpgrade):
        self._EncryptionNeedUpgrade = EncryptionNeedUpgrade

    @property
    def IsRemoteRo(self):
        return self._IsRemoteRo

    @IsRemoteRo.setter
    def IsRemoteRo(self, IsRemoteRo):
        self._IsRemoteRo = IsRemoteRo

    @property
    def MasterRegion(self):
        return self._MasterRegion

    @MasterRegion.setter
    def MasterRegion(self, MasterRegion):
        self._MasterRegion = MasterRegion

    @property
    def IsSupportUpdateSubVersion(self):
        return self._IsSupportUpdateSubVersion

    @IsSupportUpdateSubVersion.setter
    def IsSupportUpdateSubVersion(self, IsSupportUpdateSubVersion):
        self._IsSupportUpdateSubVersion = IsSupportUpdateSubVersion

    @property
    def CurrentSubVersion(self):
        return self._CurrentSubVersion

    @CurrentSubVersion.setter
    def CurrentSubVersion(self, CurrentSubVersion):
        self._CurrentSubVersion = CurrentSubVersion

    @property
    def TargetSubVersion(self):
        return self._TargetSubVersion

    @TargetSubVersion.setter
    def TargetSubVersion(self, TargetSubVersion):
        self._TargetSubVersion = TargetSubVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsSupportAudit = params.get("IsSupportAudit")
        self._AuditNeedUpgrade = params.get("AuditNeedUpgrade")
        self._IsSupportEncryption = params.get("IsSupportEncryption")
        self._EncryptionNeedUpgrade = params.get("EncryptionNeedUpgrade")
        self._IsRemoteRo = params.get("IsRemoteRo")
        self._MasterRegion = params.get("MasterRegion")
        self._IsSupportUpdateSubVersion = params.get("IsSupportUpdateSubVersion")
        self._CurrentSubVersion = params.get("CurrentSubVersion")
        self._TargetSubVersion = params.get("TargetSubVersion")
        self._RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _StartTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 00:00:01.
        :type StartTime: str
        :param _EndTime: End time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-01-01 23:59:59.
        :type EndTime: str
        :param _Offset: Pagination parameter indicating the offset. Default value: 0.
        :type Offset: int
        :param _Limit: Pagination parameter indicating the number of results to be returned for a single request. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible import task operation logs.
        :type TotalCount: int
        :param _Items: List of import operation records.
        :type Items: list of ImportRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ImportRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset response structure.

    """

    def __init__(self):
        r"""
        :param _Charset: Default character set of the instance, such as "latin1" and "utf8".
        :type Charset: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Charset = None
        self._RequestId = None

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Charset = params.get("Charset")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ProtectMode: Data protection mode of the primary instance. Value range: 0 (async replication), 1 (semi-sync replication), 2 (strong sync replication).
        :type ProtectMode: int
        :param _DeployMode: Master instance deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: int
        :param _Zone: Instance AZ information in the format of "ap-shanghai-1".
        :type Zone: str
        :param _SlaveConfig: Configurations of the replica node
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`
        :param _BackupConfig: Configurations of the second replica node of a strong-sync instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`
        :param _Switched: This parameter is only available for multi-AZ instances. It indicates whether the source AZ is the same as the one specified upon purchase. `true`: not the same, `false`: the same.
        :type Switched: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProtectMode = None
        self._DeployMode = None
        self._Zone = None
        self._SlaveConfig = None
        self._BackupConfig = None
        self._Switched = None
        self._RequestId = None

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SlaveConfig(self):
        return self._SlaveConfig

    @SlaveConfig.setter
    def SlaveConfig(self, SlaveConfig):
        self._SlaveConfig = SlaveConfig

    @property
    def BackupConfig(self):
        return self._BackupConfig

    @BackupConfig.setter
    def BackupConfig(self, BackupConfig):
        self._BackupConfig = BackupConfig

    @property
    def Switched(self):
        return self._Switched

    @Switched.setter
    def Switched(self, Switched):
        self._Switched = Switched

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._Zone = params.get("Zone")
        if params.get("SlaveConfig") is not None:
            self._SlaveConfig = SlaveConfig()
            self._SlaveConfig._deserialize(params.get("SlaveConfig"))
        if params.get("BackupConfig") is not None:
            self._BackupConfig = BackupConfig()
            self._BackupConfig._deserialize(params.get("BackupConfig"))
        self._Switched = params.get("Switched")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID response structure.

    """

    def __init__(self):
        r"""
        :param _IsGTIDOpen: GTID enablement flag. Value range: 0 (not enabled), 1 (enabled).
        :type IsGTIDOpen: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsGTIDOpen = None
        self._RequestId = None

    @property
    def IsGTIDOpen(self):
        return self._IsGTIDOpen

    @IsGTIDOpen.setter
    def IsGTIDOpen(self, IsGTIDOpen):
        self._IsGTIDOpen = IsGTIDOpen

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsGTIDOpen = params.get("IsGTIDOpen")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceInfoRequest(AbstractModel):
    """DescribeDBInstanceInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInfoResponse(AbstractModel):
    """DescribeDBInstanceInfo response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _Encryption: Whether encryption is enabled. YES: enabled, NO: not enabled.
        :type Encryption: str
        :param _KeyId: Encryption key ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param _KeyRegion: Key region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyRegion: str
        :param _DefaultKmsRegion: The default region of the KMS service currently used by the TencentDB backend service.
Note: this field may return `null`, indicating that no valid value can be found.
        :type DefaultKmsRegion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Encryption = None
        self._KeyId = None
        self._KeyRegion = None
        self._DefaultKmsRegion = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion

    @property
    def DefaultKmsRegion(self):
        return self._DefaultKmsRegion

    @DefaultKmsRegion.setter
    def DefaultKmsRegion(self, DefaultKmsRegion):
        self._DefaultKmsRegion = DefaultKmsRegion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Encryption = params.get("Encryption")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        self._DefaultKmsRegion = params.get("DefaultKmsRegion")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Returned parameter information.
        :type Items: list of InstanceRebootTime
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _InstanceTypes: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only).
        :type InstanceTypes: list of int non-negative
        :param _Vips: Private IP address of the instance.
        :type Vips: list of str
        :param _Status: Instance status. Valid values: <br>`0` (creating) <br>`1` (running) <br>`4` (isolating) <br>`5` (isolated; the instance can be restored and started in the recycle bin)
        :type Status: list of int non-negative
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.
        :type Limit: int
        :param _SecurityGroupId: Security group ID. When it is used as a filter, the `WithSecurityGroup` parameter should be set to 1.
        :type SecurityGroupId: str
        :param _PayTypes: Billing method. Value range: 0 (monthly subscribed), 1 (hourly).
        :type PayTypes: list of int non-negative
        :param _InstanceNames: Instance name.
        :type InstanceNames: list of str
        :param _TaskStatus: Instance task status. Valid values: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - enabling secondary instance access <br>4 - enabling public network access <br>5 - batch operation in progress <br>6 - rolling back <br>7 - disabling public network access <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built database <br>13 - dropping tables <br>14 - Disaster recovery instance creating sync task <br>15 - waiting for switch <br>16 - switching <br>17 - upgrade and switch completed <br>19 - parameter settings to be executed
        :type TaskStatus: list of int non-negative
        :param _EngineVersions: Version of the instance database engine. Value range: 5.1, 5.5, 5.6, 5.7.
        :type EngineVersions: list of str
        :param _VpcIds: VPC ID.
        :type VpcIds: list of int non-negative
        :param _ZoneIds: AZ ID.
        :type ZoneIds: list of int non-negative
        :param _SubnetIds: Subnet ID.
        :type SubnetIds: list of int non-negative
        :param _CdbErrors: Whether to lock disk write. Valid values: `0`(unlock), `1`(lock). Default value: 0.
        :type CdbErrors: list of int
        :param _OrderBy: Sort by field of the returned result set. Currently, supported values include "InstanceId", "InstanceName", "CreateTime", and "DeadlineTime".
        :type OrderBy: str
        :param _OrderDirection: Sorting method of the returned result set. Currently, "ASC" or "DESC" is supported.
        :type OrderDirection: str
        :param _WithSecurityGroup: Whether security group ID is used as a filter
        :type WithSecurityGroup: int
        :param _WithExCluster: Whether dedicated cluster details are included. Value range: 0 (not included), 1 (included)
        :type WithExCluster: int
        :param _ExClusterId: Exclusive cluster ID.
        :type ExClusterId: str
        :param _InstanceIds: Instance ID.
        :type InstanceIds: list of str
        :param _InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized).
        :type InitFlag: int
        :param _WithDr: Whether instances corresponding to the disaster recovery relationship are included. Valid values: 0 (not included), 1 (included). Default value: 1. If a primary instance is pulled, the data of the disaster recovery relationship will be in the `DrInfo` field. If a disaster recovery instance is pulled, the data of the disaster recovery relationship will be in the `MasterInfo` field. The disaster recovery relationship contains only partial basic data. To get the detailed data, you need to call an API to pull it.
        :type WithDr: int
        :param _WithRo: Whether read-only instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.
        :type WithRo: int
        :param _WithMaster: Whether primary instances are included. Valid values: 0 (not included), 1 (included). Default value: 1.
        :type WithMaster: int
        :param _DeployGroupIds: Placement group ID list.
        :type DeployGroupIds: list of str
        :param _TagKeysForSearch: Whether to use the tag key as a filter condition
        :type TagKeysForSearch: list of str
        :param _CageIds: Financial cage IDs.
        :type CageIds: list of str
        :param _TagValues: Tag value
        :type TagValues: list of str
        :param _UniqueVpcIds: VPC character vpcId
        :type UniqueVpcIds: list of str
        :param _UniqSubnetIds: VPC character subnetId
        :type UniqSubnetIds: list of str
        :param _Tags: Tag key value
        :type Tags: list of Tag
        :param _ProxyVips: Database proxy IP
        :type ProxyVips: list of str
        :param _ProxyIds: Database proxy ID
        :type ProxyIds: list of str
        :param _EngineTypes: Database engine type
        :type EngineTypes: list of str
        """
        self._ProjectId = None
        self._InstanceTypes = None
        self._Vips = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._SecurityGroupId = None
        self._PayTypes = None
        self._InstanceNames = None
        self._TaskStatus = None
        self._EngineVersions = None
        self._VpcIds = None
        self._ZoneIds = None
        self._SubnetIds = None
        self._CdbErrors = None
        self._OrderBy = None
        self._OrderDirection = None
        self._WithSecurityGroup = None
        self._WithExCluster = None
        self._ExClusterId = None
        self._InstanceIds = None
        self._InitFlag = None
        self._WithDr = None
        self._WithRo = None
        self._WithMaster = None
        self._DeployGroupIds = None
        self._TagKeysForSearch = None
        self._CageIds = None
        self._TagValues = None
        self._UniqueVpcIds = None
        self._UniqSubnetIds = None
        self._Tags = None
        self._ProxyVips = None
        self._ProxyIds = None
        self._EngineTypes = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def PayTypes(self):
        return self._PayTypes

    @PayTypes.setter
    def PayTypes(self, PayTypes):
        self._PayTypes = PayTypes

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CdbErrors(self):
        return self._CdbErrors

    @CdbErrors.setter
    def CdbErrors(self, CdbErrors):
        self._CdbErrors = CdbErrors

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def WithSecurityGroup(self):
        return self._WithSecurityGroup

    @WithSecurityGroup.setter
    def WithSecurityGroup(self, WithSecurityGroup):
        self._WithSecurityGroup = WithSecurityGroup

    @property
    def WithExCluster(self):
        return self._WithExCluster

    @WithExCluster.setter
    def WithExCluster(self, WithExCluster):
        self._WithExCluster = WithExCluster

    @property
    def ExClusterId(self):
        return self._ExClusterId

    @ExClusterId.setter
    def ExClusterId(self, ExClusterId):
        self._ExClusterId = ExClusterId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def WithDr(self):
        return self._WithDr

    @WithDr.setter
    def WithDr(self, WithDr):
        self._WithDr = WithDr

    @property
    def WithRo(self):
        return self._WithRo

    @WithRo.setter
    def WithRo(self, WithRo):
        self._WithRo = WithRo

    @property
    def WithMaster(self):
        return self._WithMaster

    @WithMaster.setter
    def WithMaster(self, WithMaster):
        self._WithMaster = WithMaster

    @property
    def DeployGroupIds(self):
        return self._DeployGroupIds

    @DeployGroupIds.setter
    def DeployGroupIds(self, DeployGroupIds):
        self._DeployGroupIds = DeployGroupIds

    @property
    def TagKeysForSearch(self):
        return self._TagKeysForSearch

    @TagKeysForSearch.setter
    def TagKeysForSearch(self, TagKeysForSearch):
        self._TagKeysForSearch = TagKeysForSearch

    @property
    def CageIds(self):
        return self._CageIds

    @CageIds.setter
    def CageIds(self, CageIds):
        self._CageIds = CageIds

    @property
    def TagValues(self):
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues

    @property
    def UniqueVpcIds(self):
        return self._UniqueVpcIds

    @UniqueVpcIds.setter
    def UniqueVpcIds(self, UniqueVpcIds):
        self._UniqueVpcIds = UniqueVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProxyVips(self):
        return self._ProxyVips

    @ProxyVips.setter
    def ProxyVips(self, ProxyVips):
        self._ProxyVips = ProxyVips

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Vips = params.get("Vips")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._PayTypes = params.get("PayTypes")
        self._InstanceNames = params.get("InstanceNames")
        self._TaskStatus = params.get("TaskStatus")
        self._EngineVersions = params.get("EngineVersions")
        self._VpcIds = params.get("VpcIds")
        self._ZoneIds = params.get("ZoneIds")
        self._SubnetIds = params.get("SubnetIds")
        self._CdbErrors = params.get("CdbErrors")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._WithSecurityGroup = params.get("WithSecurityGroup")
        self._WithExCluster = params.get("WithExCluster")
        self._ExClusterId = params.get("ExClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._InitFlag = params.get("InitFlag")
        self._WithDr = params.get("WithDr")
        self._WithRo = params.get("WithRo")
        self._WithMaster = params.get("WithMaster")
        self._DeployGroupIds = params.get("DeployGroupIds")
        self._TagKeysForSearch = params.get("TagKeysForSearch")
        self._CageIds = params.get("CageIds")
        self._TagValues = params.get("TagValues")
        self._UniqueVpcIds = params.get("UniqueVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ProxyVips = params.get("ProxyVips")
        self._ProxyIds = params.get("ProxyIds")
        self._EngineTypes = params.get("EngineTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: List of instance details
        :type Items: list of InstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBPriceRequest(AbstractModel):
    """DescribeDBPrice request structure.

    """

    def __init__(self):
        r"""
        :param _Period: Instance validity period in months. Value range: 1-36. This field is invalid when querying the prices of pay-as-you-go instances.
        :type Period: int
        :param _Zone: AZ information in the format of "ap-guangzhou-2". You can use the <a href="https://intl.cloud.tencent.com/document/api/236/17229?from_cn_redirect=1">DescribeDBZoneConfig</a> API to query the configurable values. This parameter is required when `InstanceId` is empty.
        :type Zone: str
        :param _GoodsNum: Number of instances. Value range: 1-100. Default value: 1. This parameter is required when `InstanceId` is empty.
        :type GoodsNum: int
        :param _Memory: Instance memory size in MB. This parameter is required when `InstanceId` is empty.
        :type Memory: int
        :param _Volume: Instance disk size in GB. This parameter is required when `InstanceId` is empty.
        :type Volume: int
        :param _InstanceRole: Instance type. Valid values: `master` (source instance), `dr` (disaster recovery instance), `ro` (read-only instance). Default value: `master`. This parameter is required when `InstanceId` is empty.
        :type InstanceRole: str
        :param _PayType: Billing mode. Valid values: `PRE_PAID` (monthly subscribed), `HOUR_PAID` (pay-as-you-go). This parameter is required when `InstanceId` is empty.
        :type PayType: str
        :param _ProtectMode: Data replication mode. Valid values: `0` (async), 1 (semi-sync), `2` (strong sync). Default value: `0`.
        :type ProtectMode: int
        :param _DeviceType: Instance isolation types Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). Default value: `UNIVERSAL`.  Default value: `UNIVERSAL`.
        :type DeviceType: str
        :param _InstanceNodes: The number of the instance. Valid values: `1` (for read-only and basic instances), `2` (for other source instances). To query the price of a three-node instance, set this value to `3`.
        :type InstanceNodes: int
        :param _Cpu: CPU core count of the price-queried instance. To ensure that the CPU value to be passed in is valid, use the [DescribeDBZoneConfig](https://www.tencentcloud.com/document/product/236/17229) API to query the number of purchasable cores. If this value is not specified, a default value based on memory size will be set.
        :type Cpu: int
        :param _InstanceId: Instance ID for querying renewal price. To query the renewal price of the instance, pass in the values of `InstanceId` and `Period`.
        :type InstanceId: str
        :param _Ladder: Tiered pay-as-you-go pricing, which is valid only when `PayType` is set to `HOUR_PAID`. Valid values: `1`, `2`, `3`. For more information on tiered duration, visit https://intl.cloud.tencent.com/document/product/236/18335.?from_cn_redirect=1
        :type Ladder: int
        """
        self._Period = None
        self._Zone = None
        self._GoodsNum = None
        self._Memory = None
        self._Volume = None
        self._InstanceRole = None
        self._PayType = None
        self._ProtectMode = None
        self._DeviceType = None
        self._InstanceNodes = None
        self._Cpu = None
        self._InstanceId = None
        self._Ladder = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ladder(self):
        return self._Ladder

    @Ladder.setter
    def Ladder(self, Ladder):
        self._Ladder = Ladder


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._Zone = params.get("Zone")
        self._GoodsNum = params.get("GoodsNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._InstanceRole = params.get("InstanceRole")
        self._PayType = params.get("PayType")
        self._ProtectMode = params.get("ProtectMode")
        self._DeviceType = params.get("DeviceType")
        self._InstanceNodes = params.get("InstanceNodes")
        self._Cpu = params.get("Cpu")
        self._InstanceId = params.get("InstanceId")
        self._Ladder = params.get("Ladder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPriceResponse(AbstractModel):
    """DescribeDBPrice response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Instance price. If `Currency` is set to `CNY`, the unit will be 0.01 CNY. If `Currency` is set to `USD`, the unit will be US Cent.
        :type Price: int
        :param _OriginalPrice: Original price of the instance. If `Currency` is set to `CNY`, the unit will be 0.01 CNY. If `Currency` is set to `USD`, the unit will be US Cent.
        :type OriginalPrice: int
        :param _Currency: Currency: `CNY`, `USD`.
        :type Currency: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._OriginalPrice = None
        self._Currency = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._OriginalPrice = params.get("OriginalPrice")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _ForReadonlyInstance: This parameter takes effect only when the ID of a read-only instance is passed in. If the parameter is set to `False` or left empty, the security groups bound with the RO groups of the read-only instance can only be queried. If it is set to `True`, the security groups can be modified.
        :type ForReadonlyInstance: bool
        """
        self._InstanceId = None
        self._ForReadonlyInstance = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details.
        :type Groups: list of SecurityGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSwitchRecordsRequest(AbstractModel):
    """DescribeDBSwitchRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Offset: Pagination offset.
        :type Offset: int
        :param _Limit: Number of entries per page. Value range: 1-2,000. Default value: 50.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instance switches.
        :type TotalCount: int
        :param _Items: Details of instance switches.
        :type Items: list of DBSwitchInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DBSwitchInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataBackupOverviewRequest(AbstractModel):
    """DescribeDataBackupOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Product: TencentDB product type to be queried. Currently, only `mysql` is supported.
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBackupOverviewResponse(AbstractModel):
    """DescribeDataBackupOverview response structure.

    """

    def __init__(self):
        r"""
        :param _DataBackupVolume: Total capacity of data backups in bytes in the current region (including automatic backups and manual backups).
        :type DataBackupVolume: int
        :param _DataBackupCount: Total number of data backups in the current region.
        :type DataBackupCount: int
        :param _AutoBackupVolume: Total capacity of automatic backups in the current region.
        :type AutoBackupVolume: int
        :param _AutoBackupCount: Total number of automatic backups in the current region.
        :type AutoBackupCount: int
        :param _ManualBackupVolume: Total capacity of manual backups in the current region.
        :type ManualBackupVolume: int
        :param _ManualBackupCount: Total number of manual backups in the current region.
        :type ManualBackupCount: int
        :param _RemoteBackupVolume: Total capacity of remote backups
        :type RemoteBackupVolume: int
        :param _RemoteBackupCount: Total number of remote backups
        :type RemoteBackupCount: int
        :param _DataBackupArchiveVolume: Total capacity of archive backups in the current region
        :type DataBackupArchiveVolume: int
        :param _DataBackupArchiveCount: Total number of archive backups in the current region
        :type DataBackupArchiveCount: int
        :param _DataBackupStandbyVolume: Total backup capacity of standard storage in current region
        :type DataBackupStandbyVolume: int
        :param _DataBackupStandbyCount: Total number of standard storage backups in current region
        :type DataBackupStandbyCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataBackupVolume = None
        self._DataBackupCount = None
        self._AutoBackupVolume = None
        self._AutoBackupCount = None
        self._ManualBackupVolume = None
        self._ManualBackupCount = None
        self._RemoteBackupVolume = None
        self._RemoteBackupCount = None
        self._DataBackupArchiveVolume = None
        self._DataBackupArchiveCount = None
        self._DataBackupStandbyVolume = None
        self._DataBackupStandbyCount = None
        self._RequestId = None

    @property
    def DataBackupVolume(self):
        return self._DataBackupVolume

    @DataBackupVolume.setter
    def DataBackupVolume(self, DataBackupVolume):
        self._DataBackupVolume = DataBackupVolume

    @property
    def DataBackupCount(self):
        return self._DataBackupCount

    @DataBackupCount.setter
    def DataBackupCount(self, DataBackupCount):
        self._DataBackupCount = DataBackupCount

    @property
    def AutoBackupVolume(self):
        return self._AutoBackupVolume

    @AutoBackupVolume.setter
    def AutoBackupVolume(self, AutoBackupVolume):
        self._AutoBackupVolume = AutoBackupVolume

    @property
    def AutoBackupCount(self):
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def ManualBackupVolume(self):
        return self._ManualBackupVolume

    @ManualBackupVolume.setter
    def ManualBackupVolume(self, ManualBackupVolume):
        self._ManualBackupVolume = ManualBackupVolume

    @property
    def ManualBackupCount(self):
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def RemoteBackupVolume(self):
        return self._RemoteBackupVolume

    @RemoteBackupVolume.setter
    def RemoteBackupVolume(self, RemoteBackupVolume):
        self._RemoteBackupVolume = RemoteBackupVolume

    @property
    def RemoteBackupCount(self):
        return self._RemoteBackupCount

    @RemoteBackupCount.setter
    def RemoteBackupCount(self, RemoteBackupCount):
        self._RemoteBackupCount = RemoteBackupCount

    @property
    def DataBackupArchiveVolume(self):
        return self._DataBackupArchiveVolume

    @DataBackupArchiveVolume.setter
    def DataBackupArchiveVolume(self, DataBackupArchiveVolume):
        self._DataBackupArchiveVolume = DataBackupArchiveVolume

    @property
    def DataBackupArchiveCount(self):
        return self._DataBackupArchiveCount

    @DataBackupArchiveCount.setter
    def DataBackupArchiveCount(self, DataBackupArchiveCount):
        self._DataBackupArchiveCount = DataBackupArchiveCount

    @property
    def DataBackupStandbyVolume(self):
        return self._DataBackupStandbyVolume

    @DataBackupStandbyVolume.setter
    def DataBackupStandbyVolume(self, DataBackupStandbyVolume):
        self._DataBackupStandbyVolume = DataBackupStandbyVolume

    @property
    def DataBackupStandbyCount(self):
        return self._DataBackupStandbyCount

    @DataBackupStandbyCount.setter
    def DataBackupStandbyCount(self, DataBackupStandbyCount):
        self._DataBackupStandbyCount = DataBackupStandbyCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataBackupVolume = params.get("DataBackupVolume")
        self._DataBackupCount = params.get("DataBackupCount")
        self._AutoBackupVolume = params.get("AutoBackupVolume")
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._ManualBackupVolume = params.get("ManualBackupVolume")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._RemoteBackupVolume = params.get("RemoteBackupVolume")
        self._RemoteBackupCount = params.get("RemoteBackupCount")
        self._DataBackupArchiveVolume = params.get("DataBackupArchiveVolume")
        self._DataBackupArchiveCount = params.get("DataBackupArchiveCount")
        self._DataBackupStandbyVolume = params.get("DataBackupStandbyVolume")
        self._DataBackupStandbyCount = params.get("DataBackupStandbyCount")
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Offset: Offset. Minimum value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Value range: 1-100. Maximum value: 20.
        :type Limit: int
        :param _DatabaseRegexp: Regular expression for matching database names.
        :type DatabaseRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._DatabaseRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DatabaseRegexp(self):
        return self._DatabaseRegexp

    @DatabaseRegexp.setter
    def DatabaseRegexp(self, DatabaseRegexp):
        self._DatabaseRegexp = DatabaseRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DatabaseRegexp = params.get("DatabaseRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Information of an instance.
        :type Items: list of str
        :param _DatabaseList: Database name and character set
        :type DatabaseList: list of DatabasesWithCharacterLists
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._DatabaseList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def DatabaseList(self):
        return self._DatabaseList

    @DatabaseList.setter
    def DatabaseList(self, DatabaseList):
        self._DatabaseList = DatabaseList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Items = params.get("Items")
        if params.get("DatabaseList") is not None:
            self._DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabasesWithCharacterLists()
                obj._deserialize(item)
                self._DatabaseList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams request structure.

    """

    def __init__(self):
        r"""
        :param _EngineVersion: Engine version. Currently, the supported versions are `5.1`, `5.5`, `5.6`, `5.7`, and `8.0`.
        :type EngineVersion: str
        :param _TemplateType: Type of the default parameter template. Valid values: `HIGH_STABILITY` (high-stability template), `HIGH_PERFORMANCE` (high-performance template).
        :type TemplateType: str
        :param _EngineType: Parameter template engine. Default value: `InnoDB`.
        :type EngineType: str
        """
        self._EngineVersion = None
        self._TemplateType = None
        self._EngineType = None

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParamsResponse(AbstractModel):
    """DescribeDefaultParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameters
        :type TotalCount: int
        :param _Items: Parameter details.
        :type Items: list of ParameterDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceMonitorInfoRequest(AbstractModel):
    """DescribeDeviceMonitorInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Count: This parameter is used to return the monitoring data of Count 5-minute time periods on the day. Value range: 1-288. If this parameter is not passed in, all monitoring data in a 5-minute granularity on the day will be returned by default.
        :type Count: int
        """
        self._InstanceId = None
        self._Count = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorInfoResponse(AbstractModel):
    """DescribeDeviceMonitorInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Cpu: CPU monitoring data of the instance
        :type Cpu: :class:`tencentcloud.cdb.v20170320.models.DeviceCpuInfo`
        :param _Mem: Memory monitoring data of the instance
        :type Mem: :class:`tencentcloud.cdb.v20170320.models.DeviceMemInfo`
        :param _Net: Network monitoring data of the instance
        :type Net: :class:`tencentcloud.cdb.v20170320.models.DeviceNetInfo`
        :param _Disk: Disk monitoring data of the instance
        :type Disk: :class:`tencentcloud.cdb.v20170320.models.DeviceDiskInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Cpu = None
        self._Mem = None
        self._Net = None
        self._Disk = None
        self._RequestId = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Net(self):
        return self._Net

    @Net.setter
    def Net(self, Net):
        self._Net = Net

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Cpu") is not None:
            self._Cpu = DeviceCpuInfo()
            self._Cpu._deserialize(params.get("Cpu"))
        if params.get("Mem") is not None:
            self._Mem = DeviceMemInfo()
            self._Mem._deserialize(params.get("Mem"))
        if params.get("Net") is not None:
            self._Net = DeviceNetInfo()
            self._Net._deserialize(params.get("Net"))
        if params.get("Disk") is not None:
            self._Disk = DeviceDiskInfo()
            self._Disk._deserialize(params.get("Disk"))
        self._RequestId = params.get("RequestId")


class DescribeErrorLogDataRequest(AbstractModel):
    """DescribeErrorLogData request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start timestamp, such as 1585142640.
        :type StartTime: int
        :param _EndTime: End timestamp, such as 1585142640.
        :type EndTime: int
        :param _KeyWords: List of keywords to match. Up to 15 keywords are supported.
        :type KeyWords: list of str
        :param _Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.
        :type InstType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._KeyWords = None
        self._Limit = None
        self._Offset = None
        self._InstType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def KeyWords(self):
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstType(self):
        return self._InstType

    @InstType.setter
    def InstType(self, InstType):
        self._InstType = InstType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._KeyWords = params.get("KeyWords")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogDataResponse(AbstractModel):
    """DescribeErrorLogData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Items: Returned result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of ErrlogItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ErrlogItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 20.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible records.
        :type TotalCount: int
        :param _Items: Parameter modification records.
        :type Items: list of ParamRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instance parameters.
        :type TotalCount: int
        :param _Items: Parameter details.
        :type Items: list of ParameterDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLocalBinlogConfigRequest(AbstractModel):
    """DescribeLocalBinlogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalBinlogConfigResponse(AbstractModel):
    """DescribeLocalBinlogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _LocalBinlogConfig: Binlog retention policy of the instance.
        :type LocalBinlogConfig: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfig`
        :param _LocalBinlogConfigDefault: Default binlog retention policy in the region.
        :type LocalBinlogConfigDefault: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfigDefault`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LocalBinlogConfig = None
        self._LocalBinlogConfigDefault = None
        self._RequestId = None

    @property
    def LocalBinlogConfig(self):
        return self._LocalBinlogConfig

    @LocalBinlogConfig.setter
    def LocalBinlogConfig(self, LocalBinlogConfig):
        self._LocalBinlogConfig = LocalBinlogConfig

    @property
    def LocalBinlogConfigDefault(self):
        return self._LocalBinlogConfigDefault

    @LocalBinlogConfigDefault.setter
    def LocalBinlogConfigDefault(self, LocalBinlogConfigDefault):
        self._LocalBinlogConfigDefault = LocalBinlogConfigDefault

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LocalBinlogConfig") is not None:
            self._LocalBinlogConfig = LocalBinlogConfig()
            self._LocalBinlogConfig._deserialize(params.get("LocalBinlogConfig"))
        if params.get("LocalBinlogConfigDefault") is not None:
            self._LocalBinlogConfigDefault = LocalBinlogConfigDefault()
            self._LocalBinlogConfigDefault._deserialize(params.get("LocalBinlogConfigDefault"))
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: int
        :param _Name: Parameter template name.
        :type Name: str
        :param _EngineVersion: Database engine version specified in the parameter template
        :type EngineVersion: str
        :param _TotalCount: Number of parameters in the parameter template
        :type TotalCount: int
        :param _Items: Parameter details
        :type Items: list of ParameterDetail
        :param _Description: Parameter template description
        :type Description: str
        :param _TemplateType: Type of the parameter template. Valid values: `HIGH_STABILITY` (high-stability template), `HIGH_PERFORMANCE` (high-performance template).
        :type TemplateType: str
        :param _EngineType: Parameter template engine.  Valid values: `InnoDB`, `RocksDB`. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type EngineType: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._Name = None
        self._EngineVersion = None
        self._TotalCount = None
        self._Items = None
        self._Description = None
        self._TemplateType = None
        self._EngineType = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._EngineVersion = params.get("EngineVersion")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Description = params.get("Description")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _EngineVersions: Engine version. If it is left empty, all parameter templates will be queried.
        :type EngineVersions: list of str
        :param _EngineTypes: Engine type. If it is left empty, all engine types will be queried.
        :type EngineTypes: list of str
        :param _TemplateNames: Template name. If it is left empty, all template names will be queried.
        :type TemplateNames: list of str
        :param _TemplateIds: Template ID. If it is left empty, all template IDs will be queried.
        :type TemplateIds: list of int
        """
        self._EngineVersions = None
        self._EngineTypes = None
        self._TemplateNames = None
        self._TemplateIds = None

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def EngineTypes(self):
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds


    def _deserialize(self, params):
        self._EngineVersions = params.get("EngineVersions")
        self._EngineTypes = params.get("EngineTypes")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameter templates of the user.
        :type TotalCount: int
        :param _Items: Parameter template details.
        :type Items: list of ParamTemplateInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group details.
        :type Groups: list of SecurityGroup
        :param _TotalCount: Number of security group rules
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProxyConnectionPoolConfRequest(AbstractModel):
    """DescribeProxyConnectionPoolConf request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Paginated query offset
        :type Offset: int
        :param _Limit: Maximum entries returned per page
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyConnectionPoolConfResponse(AbstractModel):
    """DescribeProxyConnectionPoolConf response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of queried configurations
Note: this field may return `null`, indicating that no valid value can be found.
        :type Count: int
        :param _PoolConf: Connection pool configuration details
Note: this field may return `null`, indicating that no valid value can be found.
        :type PoolConf: :class:`tencentcloud.cdb.v20170320.models.PoolConf`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._PoolConf = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def PoolConf(self):
        return self._PoolConf

    @PoolConf.setter
    def PoolConf(self, PoolConf):
        self._PoolConf = PoolConf

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("PoolConf") is not None:
            self._PoolConf = PoolConf()
            self._PoolConf._deserialize(params.get("PoolConf"))
        self._RequestId = params.get("RequestId")


class DescribeProxyCustomConfRequest(AbstractModel):
    """DescribeProxyCustomConf request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Paginated query offset
        :type Offset: int
        :param _Limit: Maximum entries returned per page
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyCustomConfResponse(AbstractModel):
    """DescribeProxyCustomConf response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of queried proxy configurations
Note: this field may return `null`, indicating that no valid value can be found.
        :type Count: int
        :param _CustomConf: Proxy configuration details
Note: this field may return `null`, indicating that no valid value can be found.
        :type CustomConf: :class:`tencentcloud.cdb.v20170320.models.CustomConfig`
        :param _WeightRule: Weight rule
Note: this field may return `null`, indicating that no valid value can be found.
        :type WeightRule: :class:`tencentcloud.cdb.v20170320.models.Rule`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._CustomConf = None
        self._WeightRule = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CustomConf(self):
        return self._CustomConf

    @CustomConf.setter
    def CustomConf(self, CustomConf):
        self._CustomConf = CustomConf

    @property
    def WeightRule(self):
        return self._WeightRule

    @WeightRule.setter
    def WeightRule(self, WeightRule):
        self._WeightRule = WeightRule

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("CustomConf") is not None:
            self._CustomConf = CustomConfig()
            self._CustomConf._deserialize(params.get("CustomConf"))
        if params.get("WeightRule") is not None:
            self._WeightRule = Rule()
            self._WeightRule._deserialize(params.get("WeightRule"))
        self._RequestId = params.get("RequestId")


class DescribeProxySupportParamRequest(AbstractModel):
    """DescribeProxySupportParam request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySupportParamResponse(AbstractModel):
    """DescribeProxySupportParam response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyVersion: The supported maximum proxy version Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyVersion: str
        :param _SupportPool: Whether to support the connection pool Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportPool: bool
        :param _PoolMin: Minimum connections in the connection pool Note: This field may return null, indicating that no valid values can be obtained.
        :type PoolMin: int
        :param _PoolMax: Maximum connections in the connection pool Note: This field may return null, indicating that no valid values can be obtained.
        :type PoolMax: int
        :param _SupportTransSplit: Whether to support transaction splitting Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportTransSplit: bool
        :param _SupportPoolMinVersion: Minimum proxy version supporting connection pool Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportPoolMinVersion: str
        :param _SupportTransSplitMinVersion: Minimum proxy version supporting transaction splitting Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportTransSplitMinVersion: str
        :param _SupportReadOnly: Whether read-only mode is supported Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportReadOnly: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyVersion = None
        self._SupportPool = None
        self._PoolMin = None
        self._PoolMax = None
        self._SupportTransSplit = None
        self._SupportPoolMinVersion = None
        self._SupportTransSplitMinVersion = None
        self._SupportReadOnly = None
        self._RequestId = None

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def SupportPool(self):
        return self._SupportPool

    @SupportPool.setter
    def SupportPool(self, SupportPool):
        self._SupportPool = SupportPool

    @property
    def PoolMin(self):
        return self._PoolMin

    @PoolMin.setter
    def PoolMin(self, PoolMin):
        self._PoolMin = PoolMin

    @property
    def PoolMax(self):
        return self._PoolMax

    @PoolMax.setter
    def PoolMax(self, PoolMax):
        self._PoolMax = PoolMax

    @property
    def SupportTransSplit(self):
        return self._SupportTransSplit

    @SupportTransSplit.setter
    def SupportTransSplit(self, SupportTransSplit):
        self._SupportTransSplit = SupportTransSplit

    @property
    def SupportPoolMinVersion(self):
        return self._SupportPoolMinVersion

    @SupportPoolMinVersion.setter
    def SupportPoolMinVersion(self, SupportPoolMinVersion):
        self._SupportPoolMinVersion = SupportPoolMinVersion

    @property
    def SupportTransSplitMinVersion(self):
        return self._SupportTransSplitMinVersion

    @SupportTransSplitMinVersion.setter
    def SupportTransSplitMinVersion(self, SupportTransSplitMinVersion):
        self._SupportTransSplitMinVersion = SupportTransSplitMinVersion

    @property
    def SupportReadOnly(self):
        return self._SupportReadOnly

    @SupportReadOnly.setter
    def SupportReadOnly(self, SupportReadOnly):
        self._SupportReadOnly = SupportReadOnly

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyVersion = params.get("ProxyVersion")
        self._SupportPool = params.get("SupportPool")
        self._PoolMin = params.get("PoolMin")
        self._PoolMax = params.get("PoolMax")
        self._SupportTransSplit = params.get("SupportTransSplit")
        self._SupportPoolMinVersion = params.get("SupportPoolMinVersion")
        self._SupportTransSplitMinVersion = params.get("SupportTransSplitMinVersion")
        self._SupportReadOnly = params.get("SupportReadOnly")
        self._RequestId = params.get("RequestId")


class DescribeRemoteBackupConfigRequest(AbstractModel):
    """DescribeRemoteBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRemoteBackupConfigResponse(AbstractModel):
    """DescribeRemoteBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ExpireDays: Remote backup retention period in days
        :type ExpireDays: int
        :param _RemoteBackupSave: Remote data backup. Valid values:`off` (disable), `on` (enable).
        :type RemoteBackupSave: str
        :param _RemoteBinlogSave: Remote log backup. Valid values: `off` (disable), `on` (enable). Only when the parameter `RemoteBackupSave` is `on`, the `RemoteBinlogSave` parameter can be set to `on`.
        :type RemoteBinlogSave: str
        :param _RemoteRegion: List of configured remote backup regions
        :type RemoteRegion: list of str
        :param _RegionList: List of remote backup regions
        :type RegionList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExpireDays = None
        self._RemoteBackupSave = None
        self._RemoteBinlogSave = None
        self._RemoteRegion = None
        self._RegionList = None
        self._RequestId = None

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays

    @property
    def RemoteBackupSave(self):
        return self._RemoteBackupSave

    @RemoteBackupSave.setter
    def RemoteBackupSave(self, RemoteBackupSave):
        self._RemoteBackupSave = RemoteBackupSave

    @property
    def RemoteBinlogSave(self):
        return self._RemoteBinlogSave

    @RemoteBinlogSave.setter
    def RemoteBinlogSave(self, RemoteBinlogSave):
        self._RemoteBinlogSave = RemoteBinlogSave

    @property
    def RemoteRegion(self):
        return self._RemoteRegion

    @RemoteRegion.setter
    def RemoteRegion(self, RemoteRegion):
        self._RemoteRegion = RemoteRegion

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExpireDays = params.get("ExpireDays")
        self._RemoteBackupSave = params.get("RemoteBackupSave")
        self._RemoteBinlogSave = params.get("RemoteBinlogSave")
        self._RemoteRegion = params.get("RemoteRegion")
        self._RegionList = params.get("RegionList")
        self._RequestId = params.get("RequestId")


class DescribeRoGroupsRequest(AbstractModel):
    """DescribeRoGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoGroupsResponse(AbstractModel):
    """DescribeRoGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RoGroups: RO group information array. An instance can be associated with multiple RO groups.
        :type RoGroups: list of RoGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoGroups = None
        self._RequestId = None

    @property
    def RoGroups(self):
        return self._RoGroups

    @RoGroups.setter
    def RoGroups(self, RoGroups):
        self._RoGroups = RoGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoGroups") is not None:
            self._RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self._RoGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoMinScaleRequest(AbstractModel):
    """DescribeRoMinScale request structure.

    """

    def __init__(self):
        r"""
        :param _RoInstanceId: Read-only instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `MasterInstanceId` parameter cannot both be empty.
        :type RoInstanceId: str
        :param _MasterInstanceId: Primary instance ID in the format of "cdbro-c1nl9rpv". Its value is the same as the instance ID in the TencentDB Console. This parameter and the `RoInstanceId` parameter cannot both be empty. Note: when the parameters are passed in with `RoInstanceId`, the return value refers to the minimum specification to which a read-only instance can be upgraded; when the parameters are passed in with `MasterInstanceId` but without `RoInstanceId`, the return value refers to the minimum purchasable specification for a read-only instance.
        :type MasterInstanceId: str
        """
        self._RoInstanceId = None
        self._MasterInstanceId = None

    @property
    def RoInstanceId(self):
        return self._RoInstanceId

    @RoInstanceId.setter
    def RoInstanceId(self, RoInstanceId):
        self._RoInstanceId = RoInstanceId

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId


    def _deserialize(self, params):
        self._RoInstanceId = params.get("RoInstanceId")
        self._MasterInstanceId = params.get("MasterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoMinScaleResponse(AbstractModel):
    """DescribeRoMinScale response structure.

    """

    def __init__(self):
        r"""
        :param _Memory: Memory size in MB.
        :type Memory: int
        :param _Volume: Disk size in GB.
        :type Volume: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Memory = None
        self._Volume = None
        self._RequestId = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        :param _IsRemoteZone: Whether the clone instance and the source instance are in one AZ. Valid values: `true` (yes), `false` (no).
        :type IsRemoteZone: str
        :param _BackupRegion: The region of the clone instance, such as `ap-guangzhou`.
        :type BackupRegion: str
        """
        self._InstanceIds = None
        self._IsRemoteZone = None
        self._BackupRegion = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IsRemoteZone(self):
        return self._IsRemoteZone

    @IsRemoteZone.setter
    def IsRemoteZone(self, IsRemoteZone):
        self._IsRemoteZone = IsRemoteZone

    @property
    def BackupRegion(self):
        return self._BackupRegion

    @BackupRegion.setter
    def BackupRegion(self, BackupRegion):
        self._BackupRegion = BackupRegion


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._IsRemoteZone = params.get("IsRemoteZone")
        self._BackupRegion = params.get("BackupRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Returned parameter information.
        :type Items: list of InstanceRollbackRangeTime
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRollbackTaskDetailRequest(AbstractModel):
    """DescribeRollbackTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, which is the same as the instance ID displayed in the TencentDB Console. You can use the [DescribeDBInstances API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID.
        :type InstanceId: str
        :param _AsyncRequestId: Async task ID.
        :type AsyncRequestId: str
        :param _Limit: Pagination parameter, i.e., the number of entries to be returned for a single request. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTaskDetailResponse(AbstractModel):
    """DescribeRollbackTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Items: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of RollbackTask
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = RollbackTask()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogDataRequest(AbstractModel):
    """DescribeSlowLogData request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start timestamp, such as 1585142640.
        :type StartTime: int
        :param _EndTime: End timestamp, such as 1585142640.
        :type EndTime: int
        :param _UserHosts: Client `Host` list.
        :type UserHosts: list of str
        :param _UserNames: Client username list.
        :type UserNames: list of str
        :param _DataBases: Accessed database list.
        :type DataBases: list of str
        :param _SortBy: Sort by field. Valid values: Timestamp, QueryTime, LockTime, RowsExamined, RowsSent.
        :type SortBy: str
        :param _OrderBy: Sorting order. Valid values: ASC (ascending), DESC (descending).
        :type OrderBy: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: The number of results per page in paginated queries. Default value: 100. Maximum value: 400.
        :type Limit: int
        :param _InstType: This parameter is valid only for source or disaster recovery instances. Valid value: `slave`, which indicates pulling logs from the replica.
        :type InstType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._UserHosts = None
        self._UserNames = None
        self._DataBases = None
        self._SortBy = None
        self._OrderBy = None
        self._Offset = None
        self._Limit = None
        self._InstType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def UserHosts(self):
        return self._UserHosts

    @UserHosts.setter
    def UserHosts(self, UserHosts):
        self._UserHosts = UserHosts

    @property
    def UserNames(self):
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames

    @property
    def DataBases(self):
        return self._DataBases

    @DataBases.setter
    def DataBases(self, DataBases):
        self._DataBases = DataBases

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstType(self):
        return self._InstType

    @InstType.setter
    def InstType(self, InstType):
        self._InstType = InstType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserHosts = params.get("UserHosts")
        self._UserNames = params.get("UserNames")
        self._DataBases = params.get("DataBases")
        self._SortBy = params.get("SortBy")
        self._OrderBy = params.get("OrderBy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogDataResponse(AbstractModel):
    """DescribeSlowLogData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible entries.
        :type TotalCount: int
        :param _Items: Queried results.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of SlowLogItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Offset: Pagination offset, starting from `0`. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of entries per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible slow logs.
        :type TotalCount: int
        :param _Items: Details of eligible slow logs.
        :type Items: list of SlowLogInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalSupportedPrivileges: Global permissions supported by the instance
        :type GlobalSupportedPrivileges: list of str
        :param _DatabaseSupportedPrivileges: Database permissions supported by the instance.
        :type DatabaseSupportedPrivileges: list of str
        :param _TableSupportedPrivileges: Table permissions supported by the instance.
        :type TableSupportedPrivileges: list of str
        :param _ColumnSupportedPrivileges: Column permissions supported by the instance.
        :type ColumnSupportedPrivileges: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalSupportedPrivileges = None
        self._DatabaseSupportedPrivileges = None
        self._TableSupportedPrivileges = None
        self._ColumnSupportedPrivileges = None
        self._RequestId = None

    @property
    def GlobalSupportedPrivileges(self):
        return self._GlobalSupportedPrivileges

    @GlobalSupportedPrivileges.setter
    def GlobalSupportedPrivileges(self, GlobalSupportedPrivileges):
        self._GlobalSupportedPrivileges = GlobalSupportedPrivileges

    @property
    def DatabaseSupportedPrivileges(self):
        return self._DatabaseSupportedPrivileges

    @DatabaseSupportedPrivileges.setter
    def DatabaseSupportedPrivileges(self, DatabaseSupportedPrivileges):
        self._DatabaseSupportedPrivileges = DatabaseSupportedPrivileges

    @property
    def TableSupportedPrivileges(self):
        return self._TableSupportedPrivileges

    @TableSupportedPrivileges.setter
    def TableSupportedPrivileges(self, TableSupportedPrivileges):
        self._TableSupportedPrivileges = TableSupportedPrivileges

    @property
    def ColumnSupportedPrivileges(self):
        return self._ColumnSupportedPrivileges

    @ColumnSupportedPrivileges.setter
    def ColumnSupportedPrivileges(self, ColumnSupportedPrivileges):
        self._ColumnSupportedPrivileges = ColumnSupportedPrivileges

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GlobalSupportedPrivileges = params.get("GlobalSupportedPrivileges")
        self._DatabaseSupportedPrivileges = params.get("DatabaseSupportedPrivileges")
        self._TableSupportedPrivileges = params.get("TableSupportedPrivileges")
        self._ColumnSupportedPrivileges = params.get("ColumnSupportedPrivileges")
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Database: Database name.
        :type Database: str
        :param _Offset: Record offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 2,000.
        :type Limit: int
        :param _TableRegexp: Regular expression for matching table names, which complies with the rules at MySQL's official website
        :type TableRegexp: str
        """
        self._InstanceId = None
        self._Database = None
        self._Offset = None
        self._Limit = None
        self._TableRegexp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TableRegexp(self):
        return self._TableRegexp

    @TableRegexp.setter
    def TableRegexp(self, TableRegexp):
        self._TableRegexp = TableRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Database = params.get("Database")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TableRegexp = params.get("TableRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible tables.
        :type TotalCount: int
        :param _Items: Information of a table.
        :type Items: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Items = params.get("Items")
        self._RequestId = params.get("RequestId")


class DescribeTagsOfInstanceIdsRequest(AbstractModel):
    """DescribeTagsOfInstanceIds request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instances.
        :type InstanceIds: list of str
        :param _Offset: Pagination offset.
        :type Offset: int
        :param _Limit: Number of entries per page.
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsOfInstanceIdsResponse(AbstractModel):
    """DescribeTagsOfInstanceIds response structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset.
        :type Offset: int
        :param _Limit: Number of entries per page.
        :type Limit: int
        :param _Rows: Instance tag information.
        :type Rows: list of TagsInfoOfInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfInstance()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param _AsyncRequestId: ID of an async task request, i.e., `AsyncRequestId` returned by relevant TencentDB operations.
        :type AsyncRequestId: str
        :param _TaskTypes: Task type. If no value is passed in, all task types will be queried. Valid values:
1 - rolling back a database;
2 - performing an SQL operation;
3 - importing data;
5 - setting a parameter;
6 - initializing a TencentDB instance;
7 - restarting a TencentDB instance;
8 - enabling GTID of a TencentDB instance;
9 - upgrading a read-only instance;
10 - rolling back databases in batches;
11 - upgrading a primary instance;
12 - deleting a TencentDB table;
13 - promoting a disaster recovery instance.
        :type TaskTypes: list of int
        :param _TaskStatus: Task status. If no value is passed in, all task statuses will be queried. Valid values:
-1 - undefined;
0 - initializing;
1 - running;
2 - succeeded;
3 - failed;
4 - terminated;
5 - deleted;
6 - paused.
        :type TaskStatus: list of int
        :param _StartTimeBegin: Start time of the first task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.
        :type StartTimeBegin: str
        :param _StartTimeEnd: End time of the last task in the format of yyyy-MM-dd HH:mm:ss, such as 2017-12-31 10:40:01. It is used for queries by time range.
        :type StartTimeEnd: str
        :param _Offset: Record offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceId = None
        self._AsyncRequestId = None
        self._TaskTypes = None
        self._TaskStatus = None
        self._StartTimeBegin = None
        self._StartTimeEnd = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def StartTimeBegin(self):
        return self._StartTimeBegin

    @StartTimeBegin.setter
    def StartTimeBegin(self, StartTimeBegin):
        self._StartTimeBegin = StartTimeBegin

    @property
    def StartTimeEnd(self):
        return self._StartTimeEnd

    @StartTimeEnd.setter
    def StartTimeEnd(self, StartTimeEnd):
        self._StartTimeEnd = StartTimeEnd

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._TaskTypes = params.get("TaskTypes")
        self._TaskStatus = params.get("TaskStatus")
        self._StartTimeBegin = params.get("StartTimeBegin")
        self._StartTimeEnd = params.get("StartTimeEnd")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Information of an instance task.
        :type Items: list of TaskDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param _Monday: List of maintenance time windows on Monday.
        :type Monday: list of str
        :param _Tuesday: List of maintenance time windows on Tuesday.
        :type Tuesday: list of str
        :param _Wednesday: List of maintenance time windows on Wednesday.
        :type Wednesday: list of str
        :param _Thursday: List of maintenance time windows on Thursday.
        :type Thursday: list of str
        :param _Friday: List of maintenance time windows on Friday.
        :type Friday: list of str
        :param _Saturday: List of maintenance time windows on Saturday.
        :type Saturday: list of str
        :param _Sunday: List of maintenance time windows on Sunday.
        :type Sunday: list of str
        :param _MaxDelayTime: Maximum data delay threshold
        :type MaxDelayTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None
        self._MaxDelayTime = None
        self._RequestId = None

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Monday = params.get("Monday")
        self._Tuesday = params.get("Tuesday")
        self._Wednesday = params.get("Wednesday")
        self._Thursday = params.get("Thursday")
        self._Friday = params.get("Friday")
        self._Saturday = params.get("Saturday")
        self._Sunday = params.get("Sunday")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._RequestId = params.get("RequestId")


class DescribeUploadedFilesRequest(AbstractModel):
    """DescribeUploadedFiles request structure.

    """

    def __init__(self):
        r"""
        :param _Path: File path. `OwnerUin` information of the root account should be entered in this field.
        :type Path: str
        :param _Offset: Record offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned for a single request. Default value: 20.
        :type Limit: int
        """
        self._Path = None
        self._Offset = None
        self._Limit = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadedFilesResponse(AbstractModel):
    """DescribeUploadedFiles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible SQL files.
        :type TotalCount: int
        :param _Items: List of returned SQL files.
        :type Items: list of SqlFileInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SqlFileInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU load

    """

    def __init__(self):
        r"""
        :param _Rate: Average instance CPU utilization
        :type Rate: list of DeviceCpuRateInfo
        :param _Load: CPU monitoring data of the instance
        :type Load: list of int
        """
        self._Rate = None
        self._Load = None

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load


    def _deserialize(self, params):
        if params.get("Rate") is not None:
            self._Rate = []
            for item in params.get("Rate"):
                obj = DeviceCpuRateInfo()
                obj._deserialize(item)
                self._Rate.append(obj)
        self._Load = params.get("Load")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceCpuRateInfo(AbstractModel):
    """Average instance CPU utilization

    """

    def __init__(self):
        r"""
        :param _CpuCore: CPU core number
        :type CpuCore: int
        :param _Rate: CPU utilization
        :type Rate: list of int
        """
        self._CpuCore = None
        self._Rate = None

    @property
    def CpuCore(self):
        return self._CpuCore

    @CpuCore.setter
    def CpuCore(self, CpuCore):
        self._CpuCore = CpuCore

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate


    def _deserialize(self, params):
        self._CpuCore = params.get("CpuCore")
        self._Rate = params.get("Rate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskInfo(AbstractModel):
    """Disk monitoring data of the instance

    """

    def __init__(self):
        r"""
        :param _IoRatioPerSec: Time percentage of IO operations per second
        :type IoRatioPerSec: list of int
        :param _IoWaitTime: Average wait time of device I/O operations * 100 in milliseconds. For example, if the value is 201, the average wait time of I/O operations is 201/100 = 2.1 milliseconds.
        :type IoWaitTime: list of int
        :param _Read: Average number of read operations completed by the disk per second * 100. For example, if the value is 2,002, the average number of read operations completed by the disk per second is 2,002/100=20.2.
        :type Read: list of int
        :param _Write: Average number of write operations completed by the disk per second * 100. For example, if the value is 30,001, the average number of write operations completed by the disk per second is 30,001/100=300.01.
        :type Write: list of int
        :param _CapacityRatio: Disk capacity. Each value is comprised of two data, with the first data representing the used capacity and the second one representing the total disk capacity.
        :type CapacityRatio: list of int
        """
        self._IoRatioPerSec = None
        self._IoWaitTime = None
        self._Read = None
        self._Write = None
        self._CapacityRatio = None

    @property
    def IoRatioPerSec(self):
        return self._IoRatioPerSec

    @IoRatioPerSec.setter
    def IoRatioPerSec(self, IoRatioPerSec):
        self._IoRatioPerSec = IoRatioPerSec

    @property
    def IoWaitTime(self):
        return self._IoWaitTime

    @IoWaitTime.setter
    def IoWaitTime(self, IoWaitTime):
        self._IoWaitTime = IoWaitTime

    @property
    def Read(self):
        return self._Read

    @Read.setter
    def Read(self, Read):
        self._Read = Read

    @property
    def Write(self):
        return self._Write

    @Write.setter
    def Write(self, Write):
        self._Write = Write

    @property
    def CapacityRatio(self):
        return self._CapacityRatio

    @CapacityRatio.setter
    def CapacityRatio(self, CapacityRatio):
        self._CapacityRatio = CapacityRatio


    def _deserialize(self, params):
        self._IoRatioPerSec = params.get("IoRatioPerSec")
        self._IoWaitTime = params.get("IoWaitTime")
        self._Read = params.get("Read")
        self._Write = params.get("Write")
        self._CapacityRatio = params.get("CapacityRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMemInfo(AbstractModel):
    """Memory monitoring information of the physical server where the instance is located

    """

    def __init__(self):
        r"""
        :param _Total: Total memory size in KB, which is the value of `total` in the `Mem:` in the `free` command
        :type Total: list of int
        :param _Used: Used memory size in KB, which is the value of `used` in the `Mem:` row in the `free` command
        :type Used: list of int
        """
        self._Total = None
        self._Used = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetInfo(AbstractModel):
    """Network monitoring information of the physical server where the instance is located

    """

    def __init__(self):
        r"""
        :param _Conn: Number of TCP connections
        :type Conn: list of int
        :param _PackageIn: ENI inbound packets per second
        :type PackageIn: list of int
        :param _PackageOut: ENI outbound packets per second
        :type PackageOut: list of int
        :param _FlowIn: Inbound traffic in Kbps
        :type FlowIn: list of int
        :param _FlowOut: Outbound traffic in Kbps
        :type FlowOut: list of int
        """
        self._Conn = None
        self._PackageIn = None
        self._PackageOut = None
        self._FlowIn = None
        self._FlowOut = None

    @property
    def Conn(self):
        return self._Conn

    @Conn.setter
    def Conn(self, Conn):
        self._Conn = Conn

    @property
    def PackageIn(self):
        return self._PackageIn

    @PackageIn.setter
    def PackageIn(self, PackageIn):
        self._PackageIn = PackageIn

    @property
    def PackageOut(self):
        return self._PackageOut

    @PackageOut.setter
    def PackageOut(self, PackageOut):
        self._PackageOut = PackageOut

    @property
    def FlowIn(self):
        return self._FlowIn

    @FlowIn.setter
    def FlowIn(self, FlowIn):
        self._FlowIn = FlowIn

    @property
    def FlowOut(self):
        return self._FlowOut

    @FlowOut.setter
    def FlowOut(self, FlowOut):
        self._FlowOut = FlowOut


    def _deserialize(self, params):
        self._Conn = params.get("Conn")
        self._PackageIn = params.get("PackageIn")
        self._PackageOut = params.get("PackageOut")
        self._FlowIn = params.get("FlowIn")
        self._FlowOut = params.get("FlowOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _InstanceIds: List of instance IDs, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        :param _ForReadonlyInstance: This parameter takes effect only when the IDs of read-only replicas are passed in. If this parameter is set to `False` or left empty, the security group will be unbound from the RO groups of these read-only replicas. If this parameter is set to `True`, the security group will be unbound from the read-only replicas themselves.
        :type ForReadonlyInstance: bool
        """
        self._SecurityGroupId = None
        self._InstanceIds = None
        self._ForReadonlyInstance = None

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """Disaster recovery instance information

    """

    def __init__(self):
        r"""
        :param _Status: Disaster recovery instance status
        :type Status: int
        :param _Zone: AZ information
        :type Zone: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Region: Region information
        :type Region: str
        :param _SyncStatus: Instance sync status. Possible returned values include:
0 - disaster recovery not synced;
1 - disaster recovery syncing;
2 - disaster recovery synced successfully;
3 - disaster recovery sync failed;
4 - repairing disaster recovery sync;
        :type SyncStatus: int
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceType: Instance type
        :type InstanceType: int
        """
        self._Status = None
        self._Zone = None
        self._InstanceId = None
        self._Region = None
        self._SyncStatus = None
        self._InstanceName = None
        self._InstanceType = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SyncStatus(self):
        return self._SyncStatus

    @SyncStatus.setter
    def SyncStatus(self, SyncStatus):
        self._SyncStatus = SyncStatus

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._SyncStatus = params.get("SyncStatus")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrlogItem(AbstractModel):
    """Structured error log details

    """

    def __init__(self):
        r"""
        :param _Timestamp: Error occurrence time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _Content: Error details
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: str
        """
        self._Timestamp = None
        self._Content = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRecord(AbstractModel):
    """Import task records

    """

    def __init__(self):
        r"""
        :param _Status: Status value
        :type Status: int
        :param _Code: Status value
        :type Code: int
        :param _CostTime: Execution duration
        :type CostTime: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _WorkId: Backend task ID
        :type WorkId: str
        :param _FileName: Name of the file to be imported
        :type FileName: str
        :param _Process: Execution progress
        :type Process: int
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _FileSize: File size
        :type FileSize: str
        :param _Message: Task execution information
        :type Message: str
        :param _JobId: Task ID
        :type JobId: int
        :param _DbName: Name of the table to be imported
        :type DbName: str
        :param _AsyncRequestId: Async task request ID
        :type AsyncRequestId: str
        """
        self._Status = None
        self._Code = None
        self._CostTime = None
        self._InstanceId = None
        self._WorkId = None
        self._FileName = None
        self._Process = None
        self._CreateTime = None
        self._FileSize = None
        self._Message = None
        self._JobId = None
        self._DbName = None
        self._AsyncRequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Process(self):
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._CostTime = params.get("CostTime")
        self._InstanceId = params.get("InstanceId")
        self._WorkId = params.get("WorkId")
        self._FileName = params.get("FileName")
        self._Process = params.get("Process")
        self._CreateTime = params.get("CreateTime")
        self._FileSize = params.get("FileSize")
        self._Message = params.get("Message")
        self._JobId = params.get("JobId")
        self._DbName = params.get("DbName")
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """Security group inbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy, which can be ACCEPT or DROP
        :type Action: str
        :param _CidrIp: Source IP or IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param _PortRange: Port
        :type PortRange: str
        :param _IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        :param _Dir: The direction of the rule, which is INPUT for inbound rules
        :type Dir: str
        :param _AddressModule: Address module
        :type AddressModule: str
        :param _Desc: Rule description
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None
        self._AddressModule = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        self._AddressModule = params.get("AddressModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceIds: list of str
        :param _NewPassword: New password of the instance. Rule: It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (!@#$%^*()).
        :type NewPassword: str
        :param _Parameters: List of instance parameters. Currently, "character_set_server" and "lower_case_table_names" are supported, whose value ranges are ["utf8","latin1","gbk","utf8mb4"] and ["0","1"], respectively.
        :type Parameters: list of ParamInfo
        :param _Vport: Instance port. Value range: [1024, 65535].
        :type Vport: int
        """
        self._InstanceIds = None
        self._NewPassword = None
        self._Parameters = None
        self._Vport = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def NewPassword(self):
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._NewPassword = params.get("NewPassword")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestIds: Array of async task request IDs, which can be used to query the execution results of async tasks.
        :type AsyncRequestIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestIds = None
        self._RequestId = None

    @property
    def AsyncRequestIds(self):
        return self._AsyncRequestIds

    @AsyncRequestIds.setter
    def AsyncRequestIds(self, AsyncRequestIds):
        self._AsyncRequestIds = AsyncRequestIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestIds = params.get("AsyncRequestIds")
        self._RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """Instance details

    """

    def __init__(self):
        r"""
        :param _WanStatus: Public network access status. Value range: 0 (not enabled), 1 (enabled), 2 (disabled)
        :type WanStatus: int
        :param _Zone: AZ information
        :type Zone: str
        :param _InitFlag: Initialization flag. Value range: 0 (not initialized), 1 (initialized)
        :type InitFlag: int
        :param _RoVipInfo: VIP information of a read-only instance. This field is exclusive to read-only instances where read-only access is enabled separately
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`
        :param _Memory: Memory capacity in MB
        :type Memory: int
        :param _Status: Instance status. Valid values: `0` (creating), `1` (running), `4` (isolating), `5` (isolated).
        :type Status: int
        :param _VpcId: VPC ID, such as 51102
        :type VpcId: int
        :param _SlaveInfo: Information of a secondary server
Note: This field may return null, indicating that no valid values can be obtained.
        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Volume: Disk capacity in GB
        :type Volume: int
        :param _AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled), 2 (auto-renewal disabled)
        :type AutoRenew: int
        :param _ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync)
        :type ProtectMode: int
        :param _RoGroups: Details of a read-only group
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoGroups: list of RoGroup
        :param _SubnetId: Subnet ID, such as 2333
        :type SubnetId: int
        :param _InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)
        :type InstanceType: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Region: Region information
        :type Region: str
        :param _DeadlineTime: Instance expiration time
        :type DeadlineTime: str
        :param _DeployMode: AZ deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: int
        :param _TaskStatus: Instance task status. 0 - no task; 1 - upgrading; 2 - importing data; 3 - activating secondary; 4 - enabling public network access; 5 - batch operation in progress; 6 - rolling back; 7 - disabling public network access; 8 - changing password; 9 - renaming instance; 10 - restarting; 12 - migrating self-built instance; 13 - dropping table; 14 - creating and syncing disaster recovery instance; 15 - pending upgrade and switch; 16 - upgrade and switch in progress; 17 - upgrade and switch completed
        :type TaskStatus: int
        :param _MasterInfo: Details of a primary instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`
        :param _DeviceType: Instance type
        :type DeviceType: str
        :param _EngineVersion: Kernel version
        :type EngineVersion: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _DrInfo: Details of a disaster recovery instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type DrInfo: list of DrInfo
        :param _WanDomain: Public domain name
        :type WanDomain: str
        :param _WanPort: Public network port number
        :type WanPort: int
        :param _PayType: Billing type
        :type PayType: int
        :param _CreateTime: Instance creation time
        :type CreateTime: str
        :param _Vip: Instance IP
        :type Vip: str
        :param _Vport: Port number
        :type Vport: int
        :param _CdbError: Whether the disk write is locked (It depends on whether the instance data in disk exceeds its quota). Valid values: `0` (unlocked), `1` (locked).
        :type CdbError: int
        :param _UniqVpcId: VPC descriptor, such as "vpc-5v8wn9mg"
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet descriptor, such as "subnet-1typ0s7d"
        :type UniqSubnetId: str
        :param _PhysicalId: Physical ID
        :type PhysicalId: str
        :param _Cpu: Number of cores
        :type Cpu: int
        :param _Qps: Queries per second
        :type Qps: int
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _DeviceClass: Physical machine model
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeviceClass: str
        :param _DeployGroupId: Placement group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployGroupId: str
        :param _ZoneId: AZ ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _InstanceNodes: Number of nodes
        :type InstanceNodes: int
        :param _TagList: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagList: list of TagInfoItem
        :param _EngineType: Engine type
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineType: str
        :param _MaxDelayTime: Maximum delay threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDelayTime: int
        :param _DiskType: Instance disk type, which is returned only for the instances of cloud disk edition. Valid values: `CLOUD_SSD` (SSD), `CLOUD_HSSD` (Enhanced SSD).
        :type DiskType: str
        """
        self._WanStatus = None
        self._Zone = None
        self._InitFlag = None
        self._RoVipInfo = None
        self._Memory = None
        self._Status = None
        self._VpcId = None
        self._SlaveInfo = None
        self._InstanceId = None
        self._Volume = None
        self._AutoRenew = None
        self._ProtectMode = None
        self._RoGroups = None
        self._SubnetId = None
        self._InstanceType = None
        self._ProjectId = None
        self._Region = None
        self._DeadlineTime = None
        self._DeployMode = None
        self._TaskStatus = None
        self._MasterInfo = None
        self._DeviceType = None
        self._EngineVersion = None
        self._InstanceName = None
        self._DrInfo = None
        self._WanDomain = None
        self._WanPort = None
        self._PayType = None
        self._CreateTime = None
        self._Vip = None
        self._Vport = None
        self._CdbError = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._PhysicalId = None
        self._Cpu = None
        self._Qps = None
        self._ZoneName = None
        self._DeviceClass = None
        self._DeployGroupId = None
        self._ZoneId = None
        self._InstanceNodes = None
        self._TagList = None
        self._EngineType = None
        self._MaxDelayTime = None
        self._DiskType = None

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InitFlag(self):
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def RoVipInfo(self):
        return self._RoVipInfo

    @RoVipInfo.setter
    def RoVipInfo(self, RoVipInfo):
        self._RoVipInfo = RoVipInfo

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SlaveInfo(self):
        return self._SlaveInfo

    @SlaveInfo.setter
    def SlaveInfo(self, SlaveInfo):
        self._SlaveInfo = SlaveInfo

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def RoGroups(self):
        return self._RoGroups

    @RoGroups.setter
    def RoGroups(self, RoGroups):
        self._RoGroups = RoGroups

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def MasterInfo(self):
        return self._MasterInfo

    @MasterInfo.setter
    def MasterInfo(self, MasterInfo):
        self._MasterInfo = MasterInfo

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DrInfo(self):
        return self._DrInfo

    @DrInfo.setter
    def DrInfo(self, DrInfo):
        self._DrInfo = DrInfo

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CdbError(self):
        return self._CdbError

    @CdbError.setter
    def CdbError(self, CdbError):
        self._CdbError = CdbError

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def PhysicalId(self):
        return self._PhysicalId

    @PhysicalId.setter
    def PhysicalId(self, PhysicalId):
        self._PhysicalId = PhysicalId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def InstanceNodes(self):
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._WanStatus = params.get("WanStatus")
        self._Zone = params.get("Zone")
        self._InitFlag = params.get("InitFlag")
        if params.get("RoVipInfo") is not None:
            self._RoVipInfo = RoVipInfo()
            self._RoVipInfo._deserialize(params.get("RoVipInfo"))
        self._Memory = params.get("Memory")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        if params.get("SlaveInfo") is not None:
            self._SlaveInfo = SlaveInfo()
            self._SlaveInfo._deserialize(params.get("SlaveInfo"))
        self._InstanceId = params.get("InstanceId")
        self._Volume = params.get("Volume")
        self._AutoRenew = params.get("AutoRenew")
        self._ProtectMode = params.get("ProtectMode")
        if params.get("RoGroups") is not None:
            self._RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self._RoGroups.append(obj)
        self._SubnetId = params.get("SubnetId")
        self._InstanceType = params.get("InstanceType")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._DeadlineTime = params.get("DeadlineTime")
        self._DeployMode = params.get("DeployMode")
        self._TaskStatus = params.get("TaskStatus")
        if params.get("MasterInfo") is not None:
            self._MasterInfo = MasterInfo()
            self._MasterInfo._deserialize(params.get("MasterInfo"))
        self._DeviceType = params.get("DeviceType")
        self._EngineVersion = params.get("EngineVersion")
        self._InstanceName = params.get("InstanceName")
        if params.get("DrInfo") is not None:
            self._DrInfo = []
            for item in params.get("DrInfo"):
                obj = DrInfo()
                obj._deserialize(item)
                self._DrInfo.append(obj)
        self._WanDomain = params.get("WanDomain")
        self._WanPort = params.get("WanPort")
        self._PayType = params.get("PayType")
        self._CreateTime = params.get("CreateTime")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CdbError = params.get("CdbError")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._PhysicalId = params.get("PhysicalId")
        self._Cpu = params.get("Cpu")
        self._Qps = params.get("Qps")
        self._ZoneName = params.get("ZoneName")
        self._DeviceClass = params.get("DeviceClass")
        self._DeployGroupId = params.get("DeployGroupId")
        self._ZoneId = params.get("ZoneId")
        self._InstanceNodes = params.get("InstanceNodes")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfoItem()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._EngineType = params.get("EngineType")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRebootTime(AbstractModel):
    """Estimated time of instance restart

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _TimeInSeconds: Estimated restart time
        :type TimeInSeconds: int
        """
        self._InstanceId = None
        self._TimeInSeconds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeInSeconds(self):
        return self._TimeInSeconds

    @TimeInSeconds.setter
    def TimeInSeconds(self, TimeInSeconds):
        self._TimeInSeconds = TimeInSeconds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeInSeconds = params.get("TimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRollbackRangeTime(AbstractModel):
    """Time range available for instance rollback

    """

    def __init__(self):
        r"""
        :param _Code: Queries database error code
        :type Code: int
        :param _Message: Queries database error message
        :type Message: str
        :param _InstanceId: List of instance IDs. An instance ID is in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Times: Time range available for rollback
        :type Times: list of RollbackTimeRange
        """
        self._Code = None
        self._Message = None
        self._InstanceId = None
        self._Times = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Times(self):
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self._Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task. (This returned field has been disused. You can query the isolation status of an instance through the `DescribeDBInstances` API.)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class LocalBinlogConfig(AbstractModel):
    """Retention policy of local binlog

    """

    def __init__(self):
        r"""
        :param _SaveHours: Retention period of local binlog. Value range: [72,168].
        :type SaveHours: int
        :param _MaxUsage: Space utilization of local binlog. Value range: [30,50].
        :type MaxUsage: int
        """
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalBinlogConfigDefault(AbstractModel):
    """Default retention policy of local binlog.

    """

    def __init__(self):
        r"""
        :param _SaveHours: Retention period of local binlog. Value range: [72,168].
        :type SaveHours: int
        :param _MaxUsage: Space utilization of local binlog. Value range: [30,50].
        :type MaxUsage: int
        """
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterInfo(AbstractModel):
    """Master instance information

    """

    def __init__(self):
        r"""
        :param _Region: Region information
        :type Region: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _Zone: AZ information
        :type Zone: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ResourceId: Long instance ID
        :type ResourceId: str
        :param _Status: Instance status
        :type Status: int
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceType: Instance type
        :type InstanceType: int
        :param _TaskStatus: Task status
        :type TaskStatus: int
        :param _Memory: Memory capacity
        :type Memory: int
        :param _Volume: Disk capacity
        :type Volume: int
        :param _DeviceType: Instance model
        :type DeviceType: str
        :param _Qps: Queries per second
        :type Qps: int
        :param _VpcId: VPC ID
        :type VpcId: int
        :param _SubnetId: Subnet ID
        :type SubnetId: int
        :param _ExClusterId: Dedicated cluster ID
        :type ExClusterId: str
        :param _ExClusterName: Dedicated cluster name
        :type ExClusterName: str
        """
        self._Region = None
        self._RegionId = None
        self._ZoneId = None
        self._Zone = None
        self._InstanceId = None
        self._ResourceId = None
        self._Status = None
        self._InstanceName = None
        self._InstanceType = None
        self._TaskStatus = None
        self._Memory = None
        self._Volume = None
        self._DeviceType = None
        self._Qps = None
        self._VpcId = None
        self._SubnetId = None
        self._ExClusterId = None
        self._ExClusterName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ExClusterId(self):
        return self._ExClusterId

    @ExClusterId.setter
    def ExClusterId(self, ExClusterId):
        self._ExClusterId = ExClusterId

    @property
    def ExClusterName(self):
        return self._ExClusterName

    @ExClusterName.setter
    def ExClusterName(self, ExClusterName):
        self._ExClusterName = ExClusterName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._TaskStatus = params.get("TaskStatus")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._DeviceType = params.get("DeviceType")
        self._Qps = params.get("Qps")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ExClusterId = params.get("ExClusterId")
        self._ExClusterName = params.get("ExClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Accounts: TencentDB account
        :type Accounts: list of Account
        :param _Description: Database account remarks
        :type Description: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._Description = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountMaxUserConnectionsRequest(AbstractModel):
    """ModifyAccountMaxUserConnections request structure.

    """

    def __init__(self):
        r"""
        :param _Accounts: List of TencentDB accounts
        :type Accounts: list of Account
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _MaxUserConnections: Maximum connections of the account. Maximum value: `10240`.
        :type MaxUserConnections: int
        """
        self._Accounts = None
        self._InstanceId = None
        self._MaxUserConnections = None

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaxUserConnections(self):
        return self._MaxUserConnections

    @MaxUserConnections.setter
    def MaxUserConnections(self, MaxUserConnections):
        self._MaxUserConnections = MaxUserConnections


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountMaxUserConnectionsResponse(AbstractModel):
    """ModifyAccountMaxUserConnections response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _NewPassword: New password of the database account. It can only contain 8-64 characters and must contain at least two of the following types of characters: letters, digits, and special characters (_+-&=!@#$%^*()).
        :type NewPassword: str
        :param _Accounts: TencentDB account
        :type Accounts: list of Account
        """
        self._InstanceId = None
        self._NewPassword = None
        self._Accounts = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewPassword(self):
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewPassword = params.get("NewPassword")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _Accounts: Database account, including username and domain name.
        :type Accounts: list of Account
        :param _GlobalPrivileges: Global permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "PROCESS", "DROP", "REFERENCES", "INDEX", "ALTER", "SHOW DATABASES", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER", "CREATE USER", "RELOAD", "REPLICATION CLIENT", "REPLICATION SLAVE".
Note: When “ModifyAction” is empty, if `GlobalPrivileges` is not passed in, it indicates the global permission will become ineffective.
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Database permission. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "SHOW VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER".
Note: When “ModifyAction” is empty, if `DatabasePrivileges` is not passed in, it indicates the permission of the database will become ineffective.
        :type DatabasePrivileges: list of DatabasePrivilege
        :param _TablePrivileges: Table permission in the database. Valid values: "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "REFERENCES", "INDEX", "ALTER", "CREATE VIEW", "SHOW VIEW", "TRIGGER".
Note: When “ModifyAction” is empty, if `TablePrivileges` is not passed in, it indicates the permission of the table will become ineffective.
        :type TablePrivileges: list of TablePrivilege
        :param _ColumnPrivileges: Column permission in the table. Valid values: "SELECT", "INSERT", "UPDATE", "REFERENCES".
Note: When “ModifyAction” is empty, if `ColumnPrivileges` is not passed in, it indicates the permission of the column will become ineffective.
        :type ColumnPrivileges: list of ColumnPrivilege
        :param _ModifyAction: When this parameter is not empty, it indicates that the permission will be modified. Valid values: `grant` (grant permission), `revoke` (revoke permission)
        :type ModifyAction: str
        """
        self._InstanceId = None
        self._Accounts = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None
        self._ColumnPrivileges = None
        self._ModifyAction = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def GlobalPrivileges(self):
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges

    @property
    def ColumnPrivileges(self):
        return self._ColumnPrivileges

    @ColumnPrivileges.setter
    def ColumnPrivileges(self, ColumnPrivileges):
        self._ColumnPrivileges = ColumnPrivileges

    @property
    def ModifyAction(self):
        return self._ModifyAction

    @ModifyAction.setter
    def ModifyAction(self, ModifyAction):
        self._ModifyAction = ModifyAction


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self._ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self._ColumnPrivileges.append(obj)
        self._ModifyAction = params.get("ModifyAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        :param _AutoRenew: Auto-renewal flag. Value range: 0 (auto-renewal not enabled), 1 (auto-renewal enabled).
        :type AutoRenew: int
        """
        self._InstanceIds = None
        self._AutoRenew = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _ExpireDays: Backup file retention period in days. Value range: 7-1830.
        :type ExpireDays: int
        :param _StartTime: (This parameter will be disused. The `BackupTimeWindow` parameter is recommended.) Backup time range in the format of 02:00-06:00, with the start time and end time on the hour. Valid values: 00:00-12:00, 02:00-06:00, 06:00-10:00, 10:00-14:00, 14:00-18:00, 18:00-22:00, 22:00-02:00.
        :type StartTime: str
        :param _BackupMethod: Automatic backup mode. Only `physical` (physical cold backup) is supported
        :type BackupMethod: str
        :param _BinlogExpireDays: Binlog retention period in days. Value range: 7-1830. It can’t be greater than the retention period of backup files.
        :type BinlogExpireDays: int
        :param _BackupTimeWindow: Backup time window; for example, to set up backup between 10:00 and 14:00 on every Tuesday and Sunday, you should set this parameter as follows: {"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"} (Note: You can set up backup on different days, but the backup time windows need to be the same. If this field is set, the `StartTime` field will be ignored)
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param _EnableBackupPeriodSave: Switch for periodic archive. Valid values: `off` (disable), `on` (enable). Default value:`off`. When you enable the periodic archive policy for the first time, you need to enter the `BackupPeriodSaveDays`, `BackupPeriodSaveInterval`, `BackupPeriodSaveCount`, and `StartBackupPeriodSaveDate` parameters; otherwise, the policy will not take effect.
        :type EnableBackupPeriodSave: str
        :param _EnableBackupPeriodLongTermSave: Switch for long-term backup retention (This field can be ignored, for its feature hasn’t been launched). Valid values: `off` (disable), `on` (enable). Default value: `off`. Once enabled, the parameters (BackupPeriodSaveDays, BackupPeriodSaveInterval, and BackupPeriodSaveCount) will be invalid.
        :type EnableBackupPeriodLongTermSave: str
        :param _BackupPeriodSaveDays: Maximum days of archive backup retention. Valid range: 90-3650. Default value: 1080.
        :type BackupPeriodSaveDays: int
        :param _BackupPeriodSaveInterval: Archive backup retention period. Valid values: `weekly` (a week), `monthly` (a month), `quarterly` (a quarter), `yearly` (a year). Default value: `monthly`.
        :type BackupPeriodSaveInterval: str
        :param _BackupPeriodSaveCount: Number of archive backups. Minimum value: `1`, Maximum value: Number of non-archive backups in archive backup retention period. Default value: `1`.
        :type BackupPeriodSaveCount: int
        :param _StartBackupPeriodSaveDate: The start time in the format of yyyy-mm-dd HH:MM:SS, which is used to enable archive backup retention policy.
        :type StartBackupPeriodSaveDate: str
        :param _EnableBackupArchive: Whether to enable the archive backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBackupArchive: str
        :param _BackupArchiveDays: The period (in days) of how long a data backup is retained before being archived, which falls between 180 days and the number of days from the time it is created until it expires.
        :type BackupArchiveDays: int
        :param _BinlogArchiveDays: The period (in days) of how long a log backup is retained before being archived, which falls between 180 days and the number of days from the time it is created until it expires.
        :type BinlogArchiveDays: int
        :param _EnableBinlogArchive: Whether to enable the archive backup of the log. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBinlogArchive: str
        :param _EnableBackupStandby: Whether to enable the standard storage policy for data backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBackupStandby: str
        :param _BackupStandbyDays: The period (in days) of how long a data backup is retained before switching to standard storage, which falls between 30 days and the number of days from the time it is created until it expires. If the archive backup is enabled, this period cannot be greater than archive backup period.
        :type BackupStandbyDays: int
        :param _EnableBinlogStandby: Whether to enable the standard storage policy for log backup. Valid values: `off` (disable), `on` (enable). Default value: `off`.
        :type EnableBinlogStandby: str
        :param _BinlogStandbyDays: The period (in days) of how long a log backup is retained before switching to standard storage, which falls between 30 days and the number of days from the time it is created until it expires. If the archive backup is enabled, this period cannot be greater than archive backup period.
        :type BinlogStandbyDays: int
        """
        self._InstanceId = None
        self._ExpireDays = None
        self._StartTime = None
        self._BackupMethod = None
        self._BinlogExpireDays = None
        self._BackupTimeWindow = None
        self._EnableBackupPeriodSave = None
        self._EnableBackupPeriodLongTermSave = None
        self._BackupPeriodSaveDays = None
        self._BackupPeriodSaveInterval = None
        self._BackupPeriodSaveCount = None
        self._StartBackupPeriodSaveDate = None
        self._EnableBackupArchive = None
        self._BackupArchiveDays = None
        self._BinlogArchiveDays = None
        self._EnableBinlogArchive = None
        self._EnableBackupStandby = None
        self._BackupStandbyDays = None
        self._EnableBinlogStandby = None
        self._BinlogStandbyDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BinlogExpireDays(self):
        return self._BinlogExpireDays

    @BinlogExpireDays.setter
    def BinlogExpireDays(self, BinlogExpireDays):
        self._BinlogExpireDays = BinlogExpireDays

    @property
    def BackupTimeWindow(self):
        return self._BackupTimeWindow

    @BackupTimeWindow.setter
    def BackupTimeWindow(self, BackupTimeWindow):
        self._BackupTimeWindow = BackupTimeWindow

    @property
    def EnableBackupPeriodSave(self):
        return self._EnableBackupPeriodSave

    @EnableBackupPeriodSave.setter
    def EnableBackupPeriodSave(self, EnableBackupPeriodSave):
        self._EnableBackupPeriodSave = EnableBackupPeriodSave

    @property
    def EnableBackupPeriodLongTermSave(self):
        return self._EnableBackupPeriodLongTermSave

    @EnableBackupPeriodLongTermSave.setter
    def EnableBackupPeriodLongTermSave(self, EnableBackupPeriodLongTermSave):
        self._EnableBackupPeriodLongTermSave = EnableBackupPeriodLongTermSave

    @property
    def BackupPeriodSaveDays(self):
        return self._BackupPeriodSaveDays

    @BackupPeriodSaveDays.setter
    def BackupPeriodSaveDays(self, BackupPeriodSaveDays):
        self._BackupPeriodSaveDays = BackupPeriodSaveDays

    @property
    def BackupPeriodSaveInterval(self):
        return self._BackupPeriodSaveInterval

    @BackupPeriodSaveInterval.setter
    def BackupPeriodSaveInterval(self, BackupPeriodSaveInterval):
        self._BackupPeriodSaveInterval = BackupPeriodSaveInterval

    @property
    def BackupPeriodSaveCount(self):
        return self._BackupPeriodSaveCount

    @BackupPeriodSaveCount.setter
    def BackupPeriodSaveCount(self, BackupPeriodSaveCount):
        self._BackupPeriodSaveCount = BackupPeriodSaveCount

    @property
    def StartBackupPeriodSaveDate(self):
        return self._StartBackupPeriodSaveDate

    @StartBackupPeriodSaveDate.setter
    def StartBackupPeriodSaveDate(self, StartBackupPeriodSaveDate):
        self._StartBackupPeriodSaveDate = StartBackupPeriodSaveDate

    @property
    def EnableBackupArchive(self):
        return self._EnableBackupArchive

    @EnableBackupArchive.setter
    def EnableBackupArchive(self, EnableBackupArchive):
        self._EnableBackupArchive = EnableBackupArchive

    @property
    def BackupArchiveDays(self):
        return self._BackupArchiveDays

    @BackupArchiveDays.setter
    def BackupArchiveDays(self, BackupArchiveDays):
        self._BackupArchiveDays = BackupArchiveDays

    @property
    def BinlogArchiveDays(self):
        return self._BinlogArchiveDays

    @BinlogArchiveDays.setter
    def BinlogArchiveDays(self, BinlogArchiveDays):
        self._BinlogArchiveDays = BinlogArchiveDays

    @property
    def EnableBinlogArchive(self):
        return self._EnableBinlogArchive

    @EnableBinlogArchive.setter
    def EnableBinlogArchive(self, EnableBinlogArchive):
        self._EnableBinlogArchive = EnableBinlogArchive

    @property
    def EnableBackupStandby(self):
        return self._EnableBackupStandby

    @EnableBackupStandby.setter
    def EnableBackupStandby(self, EnableBackupStandby):
        self._EnableBackupStandby = EnableBackupStandby

    @property
    def BackupStandbyDays(self):
        return self._BackupStandbyDays

    @BackupStandbyDays.setter
    def BackupStandbyDays(self, BackupStandbyDays):
        self._BackupStandbyDays = BackupStandbyDays

    @property
    def EnableBinlogStandby(self):
        return self._EnableBinlogStandby

    @EnableBinlogStandby.setter
    def EnableBinlogStandby(self, EnableBinlogStandby):
        self._EnableBinlogStandby = EnableBinlogStandby

    @property
    def BinlogStandbyDays(self):
        return self._BinlogStandbyDays

    @BinlogStandbyDays.setter
    def BinlogStandbyDays(self, BinlogStandbyDays):
        self._BinlogStandbyDays = BinlogStandbyDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ExpireDays = params.get("ExpireDays")
        self._StartTime = params.get("StartTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self._BackupTimeWindow = CommonTimeWindow()
            self._BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self._EnableBackupPeriodSave = params.get("EnableBackupPeriodSave")
        self._EnableBackupPeriodLongTermSave = params.get("EnableBackupPeriodLongTermSave")
        self._BackupPeriodSaveDays = params.get("BackupPeriodSaveDays")
        self._BackupPeriodSaveInterval = params.get("BackupPeriodSaveInterval")
        self._BackupPeriodSaveCount = params.get("BackupPeriodSaveCount")
        self._StartBackupPeriodSaveDate = params.get("StartBackupPeriodSaveDate")
        self._EnableBackupArchive = params.get("EnableBackupArchive")
        self._BackupArchiveDays = params.get("BackupArchiveDays")
        self._BinlogArchiveDays = params.get("BinlogArchiveDays")
        self._EnableBinlogArchive = params.get("EnableBinlogArchive")
        self._EnableBackupStandby = params.get("EnableBackupStandby")
        self._BackupStandbyDays = params.get("BackupStandbyDays")
        self._EnableBinlogStandby = params.get("EnableBinlogStandby")
        self._BinlogStandbyDays = params.get("BinlogStandbyDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _LimitType: Valid values: `NoLimit` (backups can be downloaded over both private and public networks with any IPs), `LimitOnlyIntranet` (backups can be downloaded over the private network with any private IPs), `Customize` (backups can be downloaded over specified VPCs with specified IPs). The `LimitVpc` and `LimitIp` parameters are valid only when this parameter is set to `Customize`.
        :type LimitType: str
        :param _VpcComparisonSymbol: Valid value: `In` (backups can only be downloaded over the VPCs specified in `LimitVpc`). Default value: `In`.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Valid values: `In` (backups can only be downloaded with the IPs specified in `LimitIp`), `NotIn` (backups cannot be downloaded with the IPs specified in `LimitIp`). Default value: `In`.
        :type IpComparisonSymbol: str
        :param _LimitVpc: VPCs used to restrict backup download.
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: IPs used to restrict backup download.
        :type LimitIp: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyBackupEncryptionStatusRequest(AbstractModel):
    """ModifyBackupEncryptionStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-XXXX, which is the same as that displayed in the TencentDB console.
        :type InstanceId: str
        :param _EncryptionStatus: Default encryption status for the new auto-generated physical backup files. Valid values: `on`, `off`.
        :type EncryptionStatus: str
        """
        self._InstanceId = None
        self._EncryptionStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EncryptionStatus(self):
        return self._EncryptionStatus

    @EncryptionStatus.setter
    def EncryptionStatus(self, EncryptionStatus):
        self._EncryptionStatus = EncryptionStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EncryptionStatus = params.get("EncryptionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupEncryptionStatusResponse(AbstractModel):
    """ModifyBackupEncryptionStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCDBProxyConnectionPoolRequest(AbstractModel):
    """ModifyCDBProxyConnectionPool request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Database proxy ID
        :type ProxyGroupId: str
        :param _OpenConnectionPool: Whether to enable the connection pool. Valid values: `true` (enable);
                             `false` (disable).
        :type OpenConnectionPool: bool
        :param _ConnectionPoolType: Connection pool type.
You can use the `DescribeProxyConnectionPoolConf` API to query the connection pool type.
        :type ConnectionPoolType: str
        :param _PoolConnectionTimeOut: Connection persistence timeout in seconds
        :type PoolConnectionTimeOut: int
        """
        self._ProxyGroupId = None
        self._OpenConnectionPool = None
        self._ConnectionPoolType = None
        self._PoolConnectionTimeOut = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def OpenConnectionPool(self):
        return self._OpenConnectionPool

    @OpenConnectionPool.setter
    def OpenConnectionPool(self, OpenConnectionPool):
        self._OpenConnectionPool = OpenConnectionPool

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def PoolConnectionTimeOut(self):
        return self._PoolConnectionTimeOut

    @PoolConnectionTimeOut.setter
    def PoolConnectionTimeOut(self, PoolConnectionTimeOut):
        self._PoolConnectionTimeOut = PoolConnectionTimeOut


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._OpenConnectionPool = params.get("OpenConnectionPool")
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._PoolConnectionTimeOut = params.get("PoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyConnectionPoolResponse(AbstractModel):
    """ModifyCDBProxyConnectionPool response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async request ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyCDBProxyDescRequest(AbstractModel):
    """ModifyCDBProxyDesc request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Database proxy ID
        :type ProxyGroupId: str
        :param _Desc: Database proxy description
        :type Desc: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._Desc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyDescResponse(AbstractModel):
    """ModifyCDBProxyDesc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCDBProxyVipVPortRequest(AbstractModel):
    """ModifyCDBProxyVipVPort request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID
        :type UniqSubnetId: str
        :param _DstIp: New IP
        :type DstIp: str
        :param _DstPort: New port
        :type DstPort: int
        :param _ReleaseDuration: Valid hours of the old IP
        :type ReleaseDuration: int
        """
        self._ProxyGroupId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._DstIp = None
        self._DstPort = None
        self._ReleaseDuration = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def ReleaseDuration(self):
        return self._ReleaseDuration

    @ReleaseDuration.setter
    def ReleaseDuration(self, ReleaseDuration):
        self._ReleaseDuration = ReleaseDuration


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyVipVPortResponse(AbstractModel):
    """ModifyCDBProxyVipVPort response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCdbProxyAddressDescRequest(AbstractModel):
    """ModifyCdbProxyAddressDesc request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        :param _Desc: Description
        :type Desc: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None
        self._Desc = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyAddressDescResponse(AbstractModel):
    """ModifyCdbProxyAddressDesc response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCdbProxyAddressVipAndVPortRequest(AbstractModel):
    """ModifyCdbProxyAddressVipAndVPort request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID
        :type UniqSubnetId: str
        :param _Vip: IP address
        :type Vip: str
        :param _VPort: Port
        :type VPort: int
        :param _ReleaseDuration: Valid Hours of Old IP
        :type ReleaseDuration: int
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._VPort = None
        self._ReleaseDuration = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def ReleaseDuration(self):
        return self._ReleaseDuration

    @ReleaseDuration.setter
    def ReleaseDuration(self, ReleaseDuration):
        self._ReleaseDuration = ReleaseDuration


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyAddressVipAndVPortResponse(AbstractModel):
    """ModifyCdbProxyAddressVipAndVPort response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCdbProxyParamRequest(AbstractModel):
    """ModifyCdbProxyParam request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ConnectionPoolLimit: Connection pool threshold
        :type ConnectionPoolLimit: int
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._ConnectionPoolLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCdbProxyParamResponse(AbstractModel):
    """ModifyCdbProxyParam response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param _InstanceName: The modified instance name.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceIds: list of str
        :param _NewProjectId: Project ID.
        :type NewProjectId: int
        """
        self._InstanceIds = None
        self._NewProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def NewProjectId(self):
        return self._NewProjectId

    @NewProjectId.setter
    def NewProjectId(self, NewProjectId):
        self._NewProjectId = NewProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._NewProjectId = params.get("NewProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        :param _ForReadonlyInstance: This parameter takes effect only when the ID of read-only replica is passed in. If this parameter is set to `False` or left empty, the security groups bound with the RO group of the read-only replicas will be modified. If this parameter is set to `True`, the security groups bound with the read-only replica itself will be modified.
        :type ForReadonlyInstance: bool
        """
        self._InstanceId = None
        self._SecurityGroupIds = None
        self._ForReadonlyInstance = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ForReadonlyInstance(self):
        return self._ForReadonlyInstance

    @ForReadonlyInstance.setter
    def ForReadonlyInstance(self, ForReadonlyInstance):
        self._ForReadonlyInstance = ForReadonlyInstance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ForReadonlyInstance = params.get("ForReadonlyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv, cdbro-c2nl9rpv, or cdbrg-c3nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://www.tencentcloud.com/document/product/236/15872) API to query the ID, which is the value of the `InstanceId` output parameter.
        :type InstanceId: str
        :param _DstIp: Target IP. Either this parameter or `DstPort` must be passed in.
        :type DstIp: str
        :param _DstPort: Target port number. Value range: 1024-65535. Either this parameter or `DstIp` must be passed in.
        :type DstPort: int
        :param _UniqVpcId: Unified VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: Unified subnet ID
        :type UniqSubnetId: str
        :param _ReleaseDuration: Repossession duration in hours for old IP in the original network when changing from classic network to VPC or changing the VPC subnet. Value range: 0–168. Default value: `24`.
        :type ReleaseDuration: int
        """
        self._InstanceId = None
        self._DstIp = None
        self._DstPort = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ReleaseDuration = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DstIp(self):
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ReleaseDuration(self):
        return self._ReleaseDuration

    @ReleaseDuration.setter
    def ReleaseDuration(self, ReleaseDuration):
        self._ReleaseDuration = ReleaseDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID. This parameter is deprecated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of short instance IDs.
        :type InstanceIds: list of str
        :param _ParamList: List of parameters to be modified. Every element is a combination of `Name` (parameter name) and `CurrentValue` (new value).
        :type ParamList: list of Parameter
        :param _TemplateId: Template ID. At least one of `ParamList` and `TemplateId` must be passed in.
        :type TemplateId: int
        :param _WaitSwitch: When to perform the parameter adjustment task. Default value: 0. Valid values: 0 - execute immediately, 1 - execute during window. When its value is 1, only one instance ID can be passed in (i.e., only one `InstanceIds` can be passed in).
        :type WaitSwitch: int
        :param _NotSyncRo: Whether to sync the parameters to read-only instance of the source instance. Valid values: `true` (not sync), `false` (sync). Default value: `false`.
        :type NotSyncRo: bool
        :param _NotSyncDr: Whether to sync the parameters to disaster recovery instance of the source instance. Valid values: `true` (not sync), `false` (sync). Default value: `false`.
        :type NotSyncDr: bool
        """
        self._InstanceIds = None
        self._ParamList = None
        self._TemplateId = None
        self._WaitSwitch = None
        self._NotSyncRo = None
        self._NotSyncDr = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def NotSyncRo(self):
        return self._NotSyncRo

    @NotSyncRo.setter
    def NotSyncRo(self, NotSyncRo):
        self._NotSyncRo = NotSyncRo

    @property
    def NotSyncDr(self):
        return self._NotSyncDr

    @NotSyncDr.setter
    def NotSyncDr(self, NotSyncDr):
        self._NotSyncDr = NotSyncDr


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._WaitSwitch = params.get("WaitSwitch")
        self._NotSyncRo = params.get("NotSyncRo")
        self._NotSyncDr = params.get("NotSyncDr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID, which can be used to query task progress.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstancePasswordComplexityRequest(AbstractModel):
    """ModifyInstancePasswordComplexity request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list
        :type InstanceIds: list of str
        :param _ParamList: List of parameters to be modified. Every element is a combination of `Name` (parameter name) and `CurrentValue` (new value). Valid values for `Name` of version 8.0: `validate_password.policy`, `validate_password.lengt`, `validate_password.mixed_case_coun`, `validate_password.number_coun`, `validate_password.special_char_count`. Valid values for `Name` of version 5.6 and 5.7: `validate_password_polic`, `validate_password_lengt` `validate_password_mixed_case_coun`, `validate_password_number_coun`, `validate_password_special_char_coun`.
        :type ParamList: list of Parameter
        """
        self._InstanceIds = None
        self._ParamList = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancePasswordComplexityResponse(AbstractModel):
    """ModifyInstancePasswordComplexity response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID, which can be used to query task progress.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ReplaceTags: Tag to be added or modified.
        :type ReplaceTags: list of TagInfo
        :param _DeleteTags: Tag to be deleted.
        :type DeleteTags: list of TagInfo
        """
        self._InstanceId = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTagResponse(AbstractModel):
    """ModifyInstanceTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLocalBinlogConfigRequest(AbstractModel):
    """ModifyLocalBinlogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _SaveHours: Retention period of local binlog. Valid range: 72-168 hours. When there is disaster recovery instance, the valid range will be 120-168 hours.
        :type SaveHours: int
        :param _MaxUsage: Space utilization of local binlog. Value range: [30,50].
        :type MaxUsage: int
        """
        self._InstanceId = None
        self._SaveHours = None
        self._MaxUsage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SaveHours(self):
        return self._SaveHours

    @SaveHours.setter
    def SaveHours(self, SaveHours):
        self._SaveHours = SaveHours

    @property
    def MaxUsage(self):
        return self._MaxUsage

    @MaxUsage.setter
    def MaxUsage(self, MaxUsage):
        self._MaxUsage = MaxUsage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SaveHours = params.get("SaveHours")
        self._MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLocalBinlogConfigResponse(AbstractModel):
    """ModifyLocalBinlogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNameOrDescByDpIdRequest(AbstractModel):
    """ModifyNameOrDescByDpId request structure.

    """

    def __init__(self):
        r"""
        :param _DeployGroupId: Placement group ID
        :type DeployGroupId: str
        :param _DeployGroupName: Name of a placement group, which can contain up to 60 characters. The placement group name and description can’t be empty.
        :type DeployGroupName: str
        :param _Description: Description of a placement group, which can contain up to 200 characters. The placement group name and description can’t be empty.
        :type Description: str
        """
        self._DeployGroupId = None
        self._DeployGroupName = None
        self._Description = None

    @property
    def DeployGroupId(self):
        return self._DeployGroupId

    @DeployGroupId.setter
    def DeployGroupId(self, DeployGroupId):
        self._DeployGroupId = DeployGroupId

    @property
    def DeployGroupName(self):
        return self._DeployGroupName

    @DeployGroupName.setter
    def DeployGroupName(self, DeployGroupName):
        self._DeployGroupName = DeployGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._DeployGroupId = params.get("DeployGroupId")
        self._DeployGroupName = params.get("DeployGroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNameOrDescByDpIdResponse(AbstractModel):
    """ModifyNameOrDescByDpId response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID.
        :type TemplateId: int
        :param _Name: Template name (up to 64 characters)
        :type Name: str
        :param _Description: Template description (up to 255 characters)
        :type Description: str
        :param _ParamList: List of parameters.
        :type ParamList: list of Parameter
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ParamList = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRemoteBackupConfigRequest(AbstractModel):
    """ModifyRemoteBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        :param _RemoteBackupSave: Remote data backup. Valid values:`off` (disable), `on` (enable).
        :type RemoteBackupSave: str
        :param _RemoteBinlogSave: Remote log backup. Valid values: `off` (disable), `on` (enable). Only when the parameter `RemoteBackupSave` is `on`, the `RemoteBinlogSave` parameter can be set to `on`.
        :type RemoteBinlogSave: str
        :param _RemoteRegion: The custom backup region list
        :type RemoteRegion: list of str
        :param _ExpireDays: Remote backup retention period in days
        :type ExpireDays: int
        """
        self._InstanceId = None
        self._RemoteBackupSave = None
        self._RemoteBinlogSave = None
        self._RemoteRegion = None
        self._ExpireDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RemoteBackupSave(self):
        return self._RemoteBackupSave

    @RemoteBackupSave.setter
    def RemoteBackupSave(self, RemoteBackupSave):
        self._RemoteBackupSave = RemoteBackupSave

    @property
    def RemoteBinlogSave(self):
        return self._RemoteBinlogSave

    @RemoteBinlogSave.setter
    def RemoteBinlogSave(self, RemoteBinlogSave):
        self._RemoteBinlogSave = RemoteBinlogSave

    @property
    def RemoteRegion(self):
        return self._RemoteRegion

    @RemoteRegion.setter
    def RemoteRegion(self, RemoteRegion):
        self._RemoteRegion = RemoteRegion

    @property
    def ExpireDays(self):
        return self._ExpireDays

    @ExpireDays.setter
    def ExpireDays(self, ExpireDays):
        self._ExpireDays = ExpireDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RemoteBackupSave = params.get("RemoteBackupSave")
        self._RemoteBinlogSave = params.get("RemoteBinlogSave")
        self._RemoteRegion = params.get("RemoteRegion")
        self._ExpireDays = params.get("ExpireDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRemoteBackupConfigResponse(AbstractModel):
    """ModifyRemoteBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRoGroupInfoRequest(AbstractModel):
    """ModifyRoGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _RoGroupId: RO group ID.
        :type RoGroupId: str
        :param _RoGroupInfo: RO group details.
        :type RoGroupInfo: :class:`tencentcloud.cdb.v20170320.models.RoGroupAttr`
        :param _RoWeightValues: Weights of instances in RO group. If the weighting mode of an RO group is changed to custom mode, this parameter must be set, and a weight value needs to be set for each RO instance.
        :type RoWeightValues: list of RoWeightValue
        :param _IsBalanceRoLoad: Whether to rebalance the loads of read-only replicas in the RO group. Valid values: `1` (yes), `0` (no). Default value: `0`. If this parameter is set to `1`, connections to the read-only replicas in the RO group will be interrupted transiently. Please ensure that your application has a reconnection mechanism.
        :type IsBalanceRoLoad: int
        :param _ReplicationDelayTime: This field has been deprecated.
        :type ReplicationDelayTime: int
        """
        self._RoGroupId = None
        self._RoGroupInfo = None
        self._RoWeightValues = None
        self._IsBalanceRoLoad = None
        self._ReplicationDelayTime = None

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId

    @property
    def RoGroupInfo(self):
        return self._RoGroupInfo

    @RoGroupInfo.setter
    def RoGroupInfo(self, RoGroupInfo):
        self._RoGroupInfo = RoGroupInfo

    @property
    def RoWeightValues(self):
        return self._RoWeightValues

    @RoWeightValues.setter
    def RoWeightValues(self, RoWeightValues):
        self._RoWeightValues = RoWeightValues

    @property
    def IsBalanceRoLoad(self):
        return self._IsBalanceRoLoad

    @IsBalanceRoLoad.setter
    def IsBalanceRoLoad(self, IsBalanceRoLoad):
        self._IsBalanceRoLoad = IsBalanceRoLoad

    @property
    def ReplicationDelayTime(self):
        return self._ReplicationDelayTime

    @ReplicationDelayTime.setter
    def ReplicationDelayTime(self, ReplicationDelayTime):
        self._ReplicationDelayTime = ReplicationDelayTime


    def _deserialize(self, params):
        self._RoGroupId = params.get("RoGroupId")
        if params.get("RoGroupInfo") is not None:
            self._RoGroupInfo = RoGroupAttr()
            self._RoGroupInfo._deserialize(params.get("RoGroupInfo"))
        if params.get("RoWeightValues") is not None:
            self._RoWeightValues = []
            for item in params.get("RoWeightValues"):
                obj = RoWeightValue()
                obj._deserialize(item)
                self._RoWeightValues.append(obj)
        self._IsBalanceRoLoad = params.get("IsBalanceRoLoad")
        self._ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoGroupInfoResponse(AbstractModel):
    """ModifyRoGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        :param _TimeRanges: Time period available for maintenance after modification in the format of 10:00-12:00. Each period lasts from half an hour to three hours, with the start time and end time aligned by half-hour. Up to two time periods can be set. Start and end time range: [00:00, 24:00].
        :type TimeRanges: list of str
        :param _Weekdays: Specifies for which day to modify the time period. Value range: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. If it is not specified or is left blank, the time period will be modified for every day by default.
        :type Weekdays: list of str
        :param _MaxDelayTime: Data delay threshold. It takes effect only for source instance and disaster recovery instance. Default value: 10.
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._TimeRanges = None
        self._Weekdays = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeRanges(self):
        return self._TimeRanges

    @TimeRanges.setter
    def TimeRanges(self, TimeRanges):
        self._TimeRanges = TimeRanges

    @property
    def Weekdays(self):
        return self._Weekdays

    @Weekdays.setter
    def Weekdays(self, Weekdays):
        self._Weekdays = Weekdays

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeRanges = params.get("TimeRanges")
        self._Weekdays = params.get("Weekdays")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTimeWindowResponse(AbstractModel):
    """ModifyTimeWindow response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OfflineIsolatedInstancesRequest(AbstractModel):
    """OfflineIsolatedInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedInstancesResponse(AbstractModel):
    """OfflineIsolatedInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TencentDB for MySQL instance ID
        :type InstanceId: str
        :param _LogExpireDay: Retention period of the audit log. Valid values:  `7` (one week), `30` (one month), `90` (three months), `180` (six months), `365` (one year), `1095` (three years), `1825` (five years).
        :type LogExpireDay: int
        :param _HighLogExpireDay: Retention period of high-frequency audit logs. Valid values:  `7` (one week), `30` (one month).
        :type HighLogExpireDay: int
        :param _AuditRuleFilters: Audit rule If both this parameter and `RuleTemplateIds` are left empty, full audit will be applied.
        :type AuditRuleFilters: list of AuditRuleFilters
        :param _RuleTemplateIds: Rule template ID If both this parameter and `AuditRuleFilters` are left empty, full audit will be applied.
        :type RuleTemplateIds: list of str
        """
        self._InstanceId = None
        self._LogExpireDay = None
        self._HighLogExpireDay = None
        self._AuditRuleFilters = None
        self._RuleTemplateIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogExpireDay(self):
        return self._LogExpireDay

    @LogExpireDay.setter
    def LogExpireDay(self, LogExpireDay):
        self._LogExpireDay = LogExpireDay

    @property
    def HighLogExpireDay(self):
        return self._HighLogExpireDay

    @HighLogExpireDay.setter
    def HighLogExpireDay(self, HighLogExpireDay):
        self._HighLogExpireDay = HighLogExpireDay

    @property
    def AuditRuleFilters(self):
        return self._AuditRuleFilters

    @AuditRuleFilters.setter
    def AuditRuleFilters(self, AuditRuleFilters):
        self._AuditRuleFilters = AuditRuleFilters

    @property
    def RuleTemplateIds(self):
        return self._RuleTemplateIds

    @RuleTemplateIds.setter
    def RuleTemplateIds(self, RuleTemplateIds):
        self._RuleTemplateIds = RuleTemplateIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogExpireDay = params.get("LogExpireDay")
        self._HighLogExpireDay = params.get("HighLogExpireDay")
        if params.get("AuditRuleFilters") is not None:
            self._AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self._AuditRuleFilters.append(obj)
        self._RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceResponse(AbstractModel):
    """OpenAuditService response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OpenDBInstanceEncryptionRequest(AbstractModel):
    """OpenDBInstanceEncryption request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TencentDB instance ID
        :type InstanceId: str
        :param _KeyId: Custom key ID, which is the unique CMK ID. If this value is empty, the key KMS-CDB auto-generated by Tencent Cloud will be used.
        :type KeyId: str
        :param _KeyRegion: Custom storage region, such as ap-guangzhou. When `KeyId` is not empty, this parameter is required.
        :type KeyRegion: str
        """
        self._InstanceId = None
        self._KeyId = None
        self._KeyRegion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyRegion(self):
        return self._KeyRegion

    @KeyRegion.setter
    def KeyRegion(self, KeyRegion):
        self._KeyRegion = KeyRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KeyId = params.get("KeyId")
        self._KeyRegion = params.get("KeyRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceEncryptionResponse(AbstractModel):
    """OpenDBInstanceEncryption response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """Security group outbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy, which can be ACCEPT or DROP
        :type Action: str
        :param _CidrIp: Destination IP or IP range, such as 172.16.0.0/12
        :type CidrIp: str
        :param _PortRange: Port or port range
        :type PortRange: str
        :param _IpProtocol: Network protocol. UDP and TCP are supported
        :type IpProtocol: str
        :param _Dir: The direction of the rule, which is OUTPUT for inbound rules
        :type Dir: str
        :param _AddressModule: Address module
        :type AddressModule: str
        :param _Desc: Rule description
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Dir = None
        self._AddressModule = None
        self._Desc = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Dir(self):
        return self._Dir

    @Dir.setter
    def Dir(self, Dir):
        self._Dir = Dir

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Dir = params.get("Dir")
        self._AddressModule = params.get("AddressModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """Instance parameter information

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _Value: Parameter value
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
        


class ParamRecord(AbstractModel):
    """Parameter modification records

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _OldValue: Parameter value before modification
        :type OldValue: str
        :param _NewValue: Parameter value after modification
        :type NewValue: str
        :param _IsSucess: Whether the parameter is modified successfully
        :type IsSucess: bool
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._ParamName = None
        self._OldValue = None
        self._NewValue = None
        self._IsSucess = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def IsSucess(self):
        return self._IsSucess

    @IsSucess.setter
    def IsSucess(self, IsSucess):
        self._IsSucess = IsSucess

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ParamName = params.get("ParamName")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        self._IsSucess = params.get("IsSucess")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """Parameter template information

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: int
        :param _Name: Parameter template name
        :type Name: str
        :param _Description: Parameter template description
        :type Description: str
        :param _EngineVersion: Instance engine version
        :type EngineVersion: str
        :param _TemplateType: Parameter template type
        :type TemplateType: str
        :param _EngineType: Parameter template engine Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineType: str
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._EngineVersion = None
        self._TemplateType = None
        self._EngineType = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EngineVersion = params.get("EngineVersion")
        self._TemplateType = params.get("TemplateType")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Parameter(AbstractModel):
    """Database instance parameter

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _CurrentValue: Parameter value
        :type CurrentValue: str
        """
        self._Name = None
        self._CurrentValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CurrentValue = params.get("CurrentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """Instance parameter details

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _ParamType: Parameter type. Valid values: `integer`, `enum`, `float`, `string`, `func`
        :type ParamType: str
        :param _Default: Default value of the parameter
        :type Default: str
        :param _Description: Parameter description
        :type Description: str
        :param _CurrentValue: Current value of the parameter
        :type CurrentValue: str
        :param _NeedReboot: Whether the database needs to be restarted for the modified parameter to take effect. Value range: 0 (no); 1 (yes)
        :type NeedReboot: int
        :param _Max: Maximum value of the parameter
        :type Max: int
        :param _Min: Minimum value of the parameter
        :type Min: int
        :param _EnumValue: Enumerated values of the parameter. It is null if the parameter is non-enumerated
        :type EnumValue: list of str
        :param _MaxFunc: Maximum parameter value, which is valid only when `ParamType` is set to `func`
        :type MaxFunc: str
        :param _MinFunc: Minimum parameter value, which is valid only when `ParamType` is set to `func`
        :type MinFunc: str
        :param _IsNotSupportEdit: Whether the parameter can be modified Note: This field may return null, indicating that no valid values can be obtained.
        :type IsNotSupportEdit: bool
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None
        self._MaxFunc = None
        self._MinFunc = None
        self._IsNotSupportEdit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def MaxFunc(self):
        return self._MaxFunc

    @MaxFunc.setter
    def MaxFunc(self, MaxFunc):
        self._MaxFunc = MaxFunc

    @property
    def MinFunc(self):
        return self._MinFunc

    @MinFunc.setter
    def MinFunc(self, MinFunc):
        self._MinFunc = MinFunc

    @property
    def IsNotSupportEdit(self):
        return self._IsNotSupportEdit

    @IsNotSupportEdit.setter
    def IsNotSupportEdit(self, IsNotSupportEdit):
        self._IsNotSupportEdit = IsNotSupportEdit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        self._MaxFunc = params.get("MaxFunc")
        self._MinFunc = params.get("MinFunc")
        self._IsNotSupportEdit = params.get("IsNotSupportEdit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolConf(AbstractModel):
    """Connection pool configuration of database proxy

    """

    def __init__(self):
        r"""
        :param _ConnectionPoolType: Connection pool type. Valid value: `SessionConnectionPool` (session-level connection pool)
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPoolType: str
        :param _MaxPoolConnectionTimeOut: Maximum value of connection persistence timeout in seconds
Note: this field may return `null`, indicating that no valid value can be found.
        :type MaxPoolConnectionTimeOut: int
        :param _MinPoolConnectionTimeOut: Minimum value of connection persistence timeout in seconds
Note: this field may return `null`, indicating that no valid value can be found.
        :type MinPoolConnectionTimeOut: int
        """
        self._ConnectionPoolType = None
        self._MaxPoolConnectionTimeOut = None
        self._MinPoolConnectionTimeOut = None

    @property
    def ConnectionPoolType(self):
        return self._ConnectionPoolType

    @ConnectionPoolType.setter
    def ConnectionPoolType(self, ConnectionPoolType):
        self._ConnectionPoolType = ConnectionPoolType

    @property
    def MaxPoolConnectionTimeOut(self):
        return self._MaxPoolConnectionTimeOut

    @MaxPoolConnectionTimeOut.setter
    def MaxPoolConnectionTimeOut(self, MaxPoolConnectionTimeOut):
        self._MaxPoolConnectionTimeOut = MaxPoolConnectionTimeOut

    @property
    def MinPoolConnectionTimeOut(self):
        return self._MinPoolConnectionTimeOut

    @MinPoolConnectionTimeOut.setter
    def MinPoolConnectionTimeOut(self, MinPoolConnectionTimeOut):
        self._MinPoolConnectionTimeOut = MinPoolConnectionTimeOut


    def _deserialize(self, params):
        self._ConnectionPoolType = params.get("ConnectionPoolType")
        self._MaxPoolConnectionTimeOut = params.get("MaxPoolConnectionTimeOut")
        self._MinPoolConnectionTimeOut = params.get("MinPoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyAddress(AbstractModel):
    """Information of the database proxy address

    """

    def __init__(self):
        r"""
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID
        :type UniqSubnetId: str
        :param _Vip: IP address
        :type Vip: str
        :param _VPort: Port
        :type VPort: int
        :param _WeightMode: Assignment mode of weights. Valid values: `system` (auto-assigned), `custom`. Note: This field may return null, indicating that no valid values can be obtained.
        :type WeightMode: str
        :param _IsKickOut: Whether to remove delayed read-only instances from the proxy group Valid values: `true`, `false`. Note: This field may return null, indicating that no valid values can be obtained.
        :type IsKickOut: bool
        :param _MinCount: Least read-only instances. Minimum value:  `0`. Note: This field may return null, indicating that no valid values can be obtained.
        :type MinCount: int
        :param _MaxDelay: The delay threshold. Minimum value:  `0`. Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDelay: int
        :param _AutoAddRo: Whether to automatically add newly created read-only instances. Valid values: `true`, `false`. Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoAddRo: bool
        :param _ReadOnly: Whether it is read-only. Valid values: `true`, `false`. Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadOnly: bool
        :param _TransSplit: Whether to enable transaction splitting Note: This field may return null, indicating that no valid values can be obtained.
        :type TransSplit: bool
        :param _FailOver: Whether to enable failover Note: This field may return null, indicating that no valid values can be obtained.
        :type FailOver: bool
        :param _ConnectionPool: Whether to enable the connection pool Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionPool: bool
        :param _Desc: Note:  This field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param _ProxyAllocation: Read weight assignment for an instance Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyAllocation: list of ProxyAllocation
        """
        self._ProxyAddressId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._Vip = None
        self._VPort = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._AutoAddRo = None
        self._ReadOnly = None
        self._TransSplit = None
        self._FailOver = None
        self._ConnectionPool = None
        self._Desc = None
        self._ProxyAllocation = None

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def TransSplit(self):
        return self._TransSplit

    @TransSplit.setter
    def TransSplit(self, TransSplit):
        self._TransSplit = TransSplit

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def ConnectionPool(self):
        return self._ConnectionPool

    @ConnectionPool.setter
    def ConnectionPool(self, ConnectionPool):
        self._ConnectionPool = ConnectionPool

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ProxyAllocation(self):
        return self._ProxyAllocation

    @ProxyAllocation.setter
    def ProxyAllocation(self, ProxyAllocation):
        self._ProxyAllocation = ProxyAllocation


    def _deserialize(self, params):
        self._ProxyAddressId = params.get("ProxyAddressId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._AutoAddRo = params.get("AutoAddRo")
        self._ReadOnly = params.get("ReadOnly")
        self._TransSplit = params.get("TransSplit")
        self._FailOver = params.get("FailOver")
        self._ConnectionPool = params.get("ConnectionPool")
        self._Desc = params.get("Desc")
        if params.get("ProxyAllocation") is not None:
            self._ProxyAllocation = []
            for item in params.get("ProxyAllocation"):
                obj = ProxyAllocation()
                obj._deserialize(item)
                self._ProxyAllocation.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyAllocation(AbstractModel):
    """Weight allocation for a proxy node

    """

    def __init__(self):
        r"""
        :param _Region: Proxy node region
        :type Region: str
        :param _Zone: AZ of proxy node region
        :type Zone: str
        :param _ProxyInstance: Proxy instance allocation
        :type ProxyInstance: list of ProxyInst
        """
        self._Region = None
        self._Zone = None
        self._ProxyInstance = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProxyInstance(self):
        return self._ProxyInstance

    @ProxyInstance.setter
    def ProxyInstance(self, ProxyInstance):
        self._ProxyInstance = ProxyInstance


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("ProxyInstance") is not None:
            self._ProxyInstance = []
            for item in params.get("ProxyInstance"):
                obj = ProxyInst()
                obj._deserialize(item)
                self._ProxyInstance.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroup(AbstractModel):
    """Database proxy group information

    """

    def __init__(self):
        r"""
        :param _BaseGroup: Basic information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param _Address: Address information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type Address: list of Address
        :param _ConnectionPoolInfo: Connection pool information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param _ProxyNode: Node information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNode: list of ProxyNodeInfo
        :param _RWInstInfo: Routing information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfo`
        """
        self._BaseGroup = None
        self._Address = None
        self._ConnectionPoolInfo = None
        self._ProxyNode = None
        self._RWInstInfo = None

    @property
    def BaseGroup(self):
        return self._BaseGroup

    @BaseGroup.setter
    def BaseGroup(self, BaseGroup):
        self._BaseGroup = BaseGroup

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ConnectionPoolInfo(self):
        return self._ConnectionPoolInfo

    @ConnectionPoolInfo.setter
    def ConnectionPoolInfo(self, ConnectionPoolInfo):
        self._ConnectionPoolInfo = ConnectionPoolInfo

    @property
    def ProxyNode(self):
        return self._ProxyNode

    @ProxyNode.setter
    def ProxyNode(self, ProxyNode):
        self._ProxyNode = ProxyNode

    @property
    def RWInstInfo(self):
        return self._RWInstInfo

    @RWInstInfo.setter
    def RWInstInfo(self, RWInstInfo):
        self._RWInstInfo = RWInstInfo


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self._BaseGroup = BaseGroupInfo()
            self._BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self._Address = []
            for item in params.get("Address"):
                obj = Address()
                obj._deserialize(item)
                self._Address.append(obj)
        if params.get("ConnectionPoolInfo") is not None:
            self._ConnectionPoolInfo = ConnectionPoolInfo()
            self._ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        if params.get("ProxyNode") is not None:
            self._ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNode.append(obj)
        if params.get("RWInstInfo") is not None:
            self._RWInstInfo = RWInfo()
            self._RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """Details of proxy group

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyVersion: Proxy version Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyVersion: str
        :param _SupportUpgradeProxyVersion: Supported proxy upgrade version Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportUpgradeProxyVersion: str
        :param _Status: Proxy status Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _TaskStatus: Proxy task status Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskStatus: str
        :param _ProxyNode: Node information of the proxy group Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyNode: list of ProxyNode
        :param _ProxyAddress: Address information of the proxy group Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyAddress: list of ProxyAddress
        :param _ConnectionPoolLimit: Connection pool threshold Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectionPoolLimit: int
        :param _SupportCreateProxyAddress: Whether to support address creation Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportCreateProxyAddress: bool
        :param _SupportUpgradeProxyMysqlVersion: TencentDB versions supporting proxy versions upgrade Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportUpgradeProxyMysqlVersion: str
        """
        self._ProxyGroupId = None
        self._ProxyVersion = None
        self._SupportUpgradeProxyVersion = None
        self._Status = None
        self._TaskStatus = None
        self._ProxyNode = None
        self._ProxyAddress = None
        self._ConnectionPoolLimit = None
        self._SupportCreateProxyAddress = None
        self._SupportUpgradeProxyMysqlVersion = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyVersion(self):
        return self._ProxyVersion

    @ProxyVersion.setter
    def ProxyVersion(self, ProxyVersion):
        self._ProxyVersion = ProxyVersion

    @property
    def SupportUpgradeProxyVersion(self):
        return self._SupportUpgradeProxyVersion

    @SupportUpgradeProxyVersion.setter
    def SupportUpgradeProxyVersion(self, SupportUpgradeProxyVersion):
        self._SupportUpgradeProxyVersion = SupportUpgradeProxyVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ProxyNode(self):
        return self._ProxyNode

    @ProxyNode.setter
    def ProxyNode(self, ProxyNode):
        self._ProxyNode = ProxyNode

    @property
    def ProxyAddress(self):
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def ConnectionPoolLimit(self):
        return self._ConnectionPoolLimit

    @ConnectionPoolLimit.setter
    def ConnectionPoolLimit(self, ConnectionPoolLimit):
        self._ConnectionPoolLimit = ConnectionPoolLimit

    @property
    def SupportCreateProxyAddress(self):
        return self._SupportCreateProxyAddress

    @SupportCreateProxyAddress.setter
    def SupportCreateProxyAddress(self, SupportCreateProxyAddress):
        self._SupportCreateProxyAddress = SupportCreateProxyAddress

    @property
    def SupportUpgradeProxyMysqlVersion(self):
        return self._SupportUpgradeProxyMysqlVersion

    @SupportUpgradeProxyMysqlVersion.setter
    def SupportUpgradeProxyMysqlVersion(self, SupportUpgradeProxyMysqlVersion):
        self._SupportUpgradeProxyMysqlVersion = SupportUpgradeProxyMysqlVersion


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyVersion = params.get("ProxyVersion")
        self._SupportUpgradeProxyVersion = params.get("SupportUpgradeProxyVersion")
        self._Status = params.get("Status")
        self._TaskStatus = params.get("TaskStatus")
        if params.get("ProxyNode") is not None:
            self._ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNode()
                obj._deserialize(item)
                self._ProxyNode.append(obj)
        if params.get("ProxyAddress") is not None:
            self._ProxyAddress = []
            for item in params.get("ProxyAddress"):
                obj = ProxyAddress()
                obj._deserialize(item)
                self._ProxyAddress.append(obj)
        self._ConnectionPoolLimit = params.get("ConnectionPoolLimit")
        self._SupportCreateProxyAddress = params.get("SupportCreateProxyAddress")
        self._SupportUpgradeProxyMysqlVersion = params.get("SupportUpgradeProxyMysqlVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroups(AbstractModel):
    """Database proxy group information

    """

    def __init__(self):
        r"""
        :param _BaseGroup: Basic information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param _Address: Address information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type Address: list of Address
        :param _ConnectionPoolInfo: Connection pool information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param _ProxyNode: Node information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNode: list of ProxyNodeInfo
        :param _RWInstInfo: Routing information of the proxy
Note: this field may return `null`, indicating that no valid value can be found.
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfos`
        """
        self._BaseGroup = None
        self._Address = None
        self._ConnectionPoolInfo = None
        self._ProxyNode = None
        self._RWInstInfo = None

    @property
    def BaseGroup(self):
        return self._BaseGroup

    @BaseGroup.setter
    def BaseGroup(self, BaseGroup):
        self._BaseGroup = BaseGroup

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ConnectionPoolInfo(self):
        return self._ConnectionPoolInfo

    @ConnectionPoolInfo.setter
    def ConnectionPoolInfo(self, ConnectionPoolInfo):
        self._ConnectionPoolInfo = ConnectionPoolInfo

    @property
    def ProxyNode(self):
        return self._ProxyNode

    @ProxyNode.setter
    def ProxyNode(self, ProxyNode):
        self._ProxyNode = ProxyNode

    @property
    def RWInstInfo(self):
        return self._RWInstInfo

    @RWInstInfo.setter
    def RWInstInfo(self, RWInstInfo):
        self._RWInstInfo = RWInstInfo


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self._BaseGroup = BaseGroupInfo()
            self._BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self._Address = []
            for item in params.get("Address"):
                obj = Address()
                obj._deserialize(item)
                self._Address.append(obj)
        if params.get("ConnectionPoolInfo") is not None:
            self._ConnectionPoolInfo = ConnectionPoolInfo()
            self._ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        if params.get("ProxyNode") is not None:
            self._ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._ProxyNode.append(obj)
        if params.get("RWInstInfo") is not None:
            self._RWInstInfo = RWInfos()
            self._RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInst(AbstractModel):
    """Proxy instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Instance name Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _InstanceType: Instance type. Valid values:  `master` (source instance), `ro` (read-only instance), `dr` (disaster recovery instance), `sdr` (disaster recovery instance of small specifications). Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _Status: Instance status. Valid values:  `0` (creating), `1` (running), `4` (isolating), `5` (isolated). Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Weight: Read weight. If it is assigned by the system automatically, the modification will not take effect but represents whether the instance is enabled. Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _Region: Instance region Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Instance AZ Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._Status = None
        self._Weight = None
        self._Region = None
        self._Zone = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNode(AbstractModel):
    """Proxy node

    """

    def __init__(self):
        r"""
        :param _ProxyId: Proxy node ID Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param _Cpu: Number of CPU cores Note: This field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _Mem: Memory size Note: This field may return null, indicating that no valid values can be obtained.
        :type Mem: int
        :param _Status: Node status Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Zone: Proxy node AZ Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _Region: Proxy node region Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Connection: Connections Note: This field may return null, indicating that no valid values can be obtained.
        :type Connection: int
        """
        self._ProxyId = None
        self._Cpu = None
        self._Mem = None
        self._Status = None
        self._Zone = None
        self._Region = None
        self._Connection = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Connection(self):
        return self._Connection

    @Connection.setter
    def Connection(self, Connection):
        self._Connection = Connection


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Status = params.get("Status")
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._Connection = params.get("Connection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeCustom(AbstractModel):
    """The specification configuration of a node

    """

    def __init__(self):
        r"""
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Mem: Memory size
        :type Mem: int
        :param _Region: Region
        :type Region: str
        :param _Zone: AZ
        :type Zone: str
        """
        self._NodeCount = None
        self._Cpu = None
        self._Mem = None
        self._Region = None
        self._Zone = None

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._NodeCount = params.get("NodeCount")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """Node information of the proxy

    """

    def __init__(self):
        r"""
        :param _ProxyNodeId: Proxy node ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNodeId: str
        :param _ProxyNodeConnections: Current number of connections to the node
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNodeConnections: int
        :param _ProxyNodeCpu: CPU
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNodeCpu: int
        :param _ProxyNodeMem: Memory
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyNodeMem: int
        :param _ProxyStatus: Node status:
init (applying)
online (active)
offline (inactive)
destroy (destroyed)
recovering (recovering from fault)
error (failed)
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyStatus: str
        """
        self._ProxyNodeId = None
        self._ProxyNodeConnections = None
        self._ProxyNodeCpu = None
        self._ProxyNodeMem = None
        self._ProxyStatus = None

    @property
    def ProxyNodeId(self):
        return self._ProxyNodeId

    @ProxyNodeId.setter
    def ProxyNodeId(self, ProxyNodeId):
        self._ProxyNodeId = ProxyNodeId

    @property
    def ProxyNodeConnections(self):
        return self._ProxyNodeConnections

    @ProxyNodeConnections.setter
    def ProxyNodeConnections(self, ProxyNodeConnections):
        self._ProxyNodeConnections = ProxyNodeConnections

    @property
    def ProxyNodeCpu(self):
        return self._ProxyNodeCpu

    @ProxyNodeCpu.setter
    def ProxyNodeCpu(self, ProxyNodeCpu):
        self._ProxyNodeCpu = ProxyNodeCpu

    @property
    def ProxyNodeMem(self):
        return self._ProxyNodeMem

    @ProxyNodeMem.setter
    def ProxyNodeMem(self, ProxyNodeMem):
        self._ProxyNodeMem = ProxyNodeMem

    @property
    def ProxyStatus(self):
        return self._ProxyStatus

    @ProxyStatus.setter
    def ProxyStatus(self, ProxyStatus):
        self._ProxyStatus = ProxyStatus


    def _deserialize(self, params):
        self._ProxyNodeId = params.get("ProxyNodeId")
        self._ProxyNodeConnections = params.get("ProxyNodeConnections")
        self._ProxyNodeCpu = params.get("ProxyNodeCpu")
        self._ProxyNodeMem = params.get("ProxyNodeMem")
        self._ProxyStatus = params.get("ProxyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCDBProxyRequest(AbstractModel):
    """QueryCDBProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Proxy ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCDBProxyResponse(AbstractModel):
    """QueryCDBProxy response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Number of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type Count: int
        :param _ProxyGroup: Proxy information
Note: this field may return `null`, indicating that no valid value can be found.
        :type ProxyGroup: list of ProxyGroups
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._ProxyGroup = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProxyGroup(self):
        return self._ProxyGroup

    @ProxyGroup.setter
    def ProxyGroup(self, ProxyGroup):
        self._ProxyGroup = ProxyGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("ProxyGroup") is not None:
            self._ProxyGroup = []
            for item in params.get("ProxyGroup"):
                obj = ProxyGroups()
                obj._deserialize(item)
                self._ProxyGroup.append(obj)
        self._RequestId = params.get("RequestId")


class RWInfo(AbstractModel):
    """Read/Write separation information of the proxy

    """

    def __init__(self):
        r"""
        :param _InstCount: Number of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type InstCount: int
        :param _WeightMode: Assignment mode of read/write weights
Valid values: `system` (auto-assigned), `custom`
Note: this field may return `null`, indicating that no valid value can be found.
        :type WeightMode: str
        :param _IsKickOut: Whether to remove delayed read-only instances from the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type IsKickOut: bool
        :param _MinCount: The minimum number of read-only instances allowed by the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type MinCount: int
        :param _MaxDelay: Delay threshold
Note: this field may return `null`, indicating that no valid value can be found.
        :type MaxDelay: int
        :param _FailOver: Whether to enable failover
Note: this field may return `null`, indicating that no valid value can be found.
        :type FailOver: bool
        :param _AutoAddRo: Whether to automatically add newly created read-only instances to the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type AutoAddRo: bool
        :param _RWInstInfo: Information of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInstanceInfo`
        """
        self._InstCount = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._RWInstInfo = None

    @property
    def InstCount(self):
        return self._InstCount

    @InstCount.setter
    def InstCount(self, InstCount):
        self._InstCount = InstCount

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def RWInstInfo(self):
        return self._RWInstInfo

    @RWInstInfo.setter
    def RWInstInfo(self, RWInstInfo):
        self._RWInstInfo = RWInstInfo


    def _deserialize(self, params):
        self._InstCount = params.get("InstCount")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        if params.get("RWInstInfo") is not None:
            self._RWInstInfo = RWInstanceInfo()
            self._RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RWInfos(AbstractModel):
    """Read/Write separation information of the proxy

    """

    def __init__(self):
        r"""
        :param _InstCount: Number of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type InstCount: int
        :param _WeightMode: Assignment mode of read/write weights
Valid values: `system` (auto-assigned), `custom`
Note: this field may return `null`, indicating that no valid value can be found.
        :type WeightMode: str
        :param _IsKickOut: Whether to remove delayed read-only instances from the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type IsKickOut: bool
        :param _MinCount: The minimum number of read-only instances allowed by the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type MinCount: int
        :param _MaxDelay: Delay threshold
Note: this field may return `null`, indicating that no valid value can be found.
        :type MaxDelay: int
        :param _FailOver: Whether to enable failover
Note: this field may return `null`, indicating that no valid value can be found.
        :type FailOver: bool
        :param _AutoAddRo: Whether to automatically add newly created read-only instances to the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type AutoAddRo: bool
        :param _RWInstInfo: Information of instances in the proxy group
Note: this field may return `null`, indicating that no valid value can be found.
        :type RWInstInfo: list of RWInstanceInfo
        """
        self._InstCount = None
        self._WeightMode = None
        self._IsKickOut = None
        self._MinCount = None
        self._MaxDelay = None
        self._FailOver = None
        self._AutoAddRo = None
        self._RWInstInfo = None

    @property
    def InstCount(self):
        return self._InstCount

    @InstCount.setter
    def InstCount(self, InstCount):
        self._InstCount = InstCount

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def IsKickOut(self):
        return self._IsKickOut

    @IsKickOut.setter
    def IsKickOut(self, IsKickOut):
        self._IsKickOut = IsKickOut

    @property
    def MinCount(self):
        return self._MinCount

    @MinCount.setter
    def MinCount(self, MinCount):
        self._MinCount = MinCount

    @property
    def MaxDelay(self):
        return self._MaxDelay

    @MaxDelay.setter
    def MaxDelay(self, MaxDelay):
        self._MaxDelay = MaxDelay

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def AutoAddRo(self):
        return self._AutoAddRo

    @AutoAddRo.setter
    def AutoAddRo(self, AutoAddRo):
        self._AutoAddRo = AutoAddRo

    @property
    def RWInstInfo(self):
        return self._RWInstInfo

    @RWInstInfo.setter
    def RWInstInfo(self, RWInstInfo):
        self._RWInstInfo = RWInstInfo


    def _deserialize(self, params):
        self._InstCount = params.get("InstCount")
        self._WeightMode = params.get("WeightMode")
        self._IsKickOut = params.get("IsKickOut")
        self._MinCount = params.get("MinCount")
        self._MaxDelay = params.get("MaxDelay")
        self._FailOver = params.get("FailOver")
        self._AutoAddRo = params.get("AutoAddRo")
        if params.get("RWInstInfo") is not None:
            self._RWInstInfo = []
            for item in params.get("RWInstInfo"):
                obj = RWInstanceInfo()
                obj._deserialize(item)
                self._RWInstInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RWInstanceInfo(AbstractModel):
    """Information of instances in the proxy group

    """


class ReleaseIsolatedDBInstancesRequest(AbstractModel):
    """ReleaseIsolatedDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Array of instance IDs in the format of `cdb-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in the output parameters.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesResponse(AbstractModel):
    """ReleaseIsolatedDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Deisolation result set.
        :type Items: list of ReleaseResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ReleaseResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ReleaseResult(AbstractModel):
    """Deisolation task result

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Code: Result value of instance deisolation. A returned value of 0 indicates success.
        :type Code: int
        :param _Message: Error message for instance deisolation.
        :type Message: str
        """
        self._InstanceId = None
        self._Code = None
        self._Message = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeRequest(AbstractModel):
    """ReloadBalanceProxyNode request structure.

    """

    def __init__(self):
        r"""
        :param _ProxyGroupId: Proxy group ID
        :type ProxyGroupId: str
        :param _ProxyAddressId: Address ID of the proxy group
        :type ProxyAddressId: str
        """
        self._ProxyGroupId = None
        self._ProxyAddressId = None

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def ProxyAddressId(self):
        return self._ProxyAddressId

    @ProxyAddressId.setter
    def ProxyAddressId(self, ProxyAddressId):
        self._ProxyAddressId = ProxyAddressId


    def _deserialize(self, params):
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._ProxyAddressId = params.get("ProxyAddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeResponse(AbstractModel):
    """ReloadBalanceProxyNode response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RemoteBackupInfo(AbstractModel):
    """Information of the remote backup

    """

    def __init__(self):
        r"""
        :param _SubBackupId: ID of the remote backup subtask
        :type SubBackupId: list of int
        :param _Region: The region where the remote backup resides
        :type Region: str
        :param _Status: Backup task status. Valid values: `SUCCESS` (backup succeeded), `FAILED` (backup failed), `RUNNING` (backup is in progress).
        :type Status: str
        :param _StartTime: The start time of remote backup
        :type StartTime: str
        :param _FinishTime: The end time of remote backup
        :type FinishTime: str
        :param _Url: The download address
        :type Url: str
        """
        self._SubBackupId = None
        self._Region = None
        self._Status = None
        self._StartTime = None
        self._FinishTime = None
        self._Url = None

    @property
    def SubBackupId(self):
        return self._SubBackupId

    @SubBackupId.setter
    def SubBackupId(self, SubBackupId):
        self._SubBackupId = SubBackupId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._SubBackupId = params.get("SubBackupId")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._FinishTime = params.get("FinishTime")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be renewed in the format of cdb-c1nl9rpv, which is the same as the instance ID displayed in the TencentDB console. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID.
        :type InstanceId: str
        :param _TimeSpan: Renewal period in months. Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`.
        :type TimeSpan: int
        :param _ModifyPayType: To renew a pay-as-you-go instance to a monthly subscribed one, you need to set this parameter to `PREPAID`.
        :type ModifyPayType: str
        """
        self._InstanceId = None
        self._TimeSpan = None
        self._ModifyPayType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ModifyPayType(self):
        return self._ModifyPayType

    @ModifyPayType.setter
    def ModifyPayType(self, ModifyPayType):
        self._ModifyPayType = ModifyPayType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TimeSpan = params.get("TimeSpan")
        self._ModifyPayType = params.get("ModifyPayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ResetRootAccountRequest(AbstractModel):
    """ResetRootAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRootAccountResponse(AbstractModel):
    """ResetRootAccount response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Array of instance IDs in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """Read-only group parameter

    """

    def __init__(self):
        r"""
        :param _RoGroupMode: Read-only group mode. Valid values: `alone` (the system assigns a read-only group automatically), `allinone` (a new read-only group will be created), `join` (an existing read-only group will be used).
        :type RoGroupMode: str
        :param _RoGroupId: Read-only group ID.
        :type RoGroupId: str
        :param _RoGroupName: Read-only group name.
        :type RoGroupName: str
        :param _RoOfflineDelay: Whether to enable the function of isolating an instance that exceeds the latency threshold. If it is enabled, when the latency between the read-only instance and the primary instance exceeds the latency threshold, the read-only instance will be isolated. Valid values: 1 (enabled), 0 (not enabled)
        :type RoOfflineDelay: int
        :param _RoMaxDelayTime: Latency threshold
        :type RoMaxDelayTime: int
        :param _MinRoInGroup: Minimum number of instances to be retained. If the number of the purchased read-only instances is smaller than the set value, they will not be removed.
        :type MinRoInGroup: int
        :param _WeightMode: Read/write weight distribution mode. Valid values: `system` (weights are assigned by the system automatically), `custom` (weights are customized)
        :type WeightMode: str
        :param _Weight: This field has been disused. To view the weight of a read-only instance, check the `Weight` value in the `RoInstances` field.
        :type Weight: int
        :param _RoInstances: Details of read-only instances in read-only group
        :type RoInstances: list of RoInstanceInfo
        :param _Vip: Private IP of read-only group.
        :type Vip: str
        :param _Vport: Private network port number of read-only group.
        :type Vport: int
        :param _UniqVpcId: VPC ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param _RoGroupRegion: Read-only group region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoGroupRegion: str
        :param _RoGroupZone: Read-only group AZ.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoGroupZone: str
        :param _DelayReplicationTime: Replication delay.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DelayReplicationTime: int
        """
        self._RoGroupMode = None
        self._RoGroupId = None
        self._RoGroupName = None
        self._RoOfflineDelay = None
        self._RoMaxDelayTime = None
        self._MinRoInGroup = None
        self._WeightMode = None
        self._Weight = None
        self._RoInstances = None
        self._Vip = None
        self._Vport = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._RoGroupRegion = None
        self._RoGroupZone = None
        self._DelayReplicationTime = None

    @property
    def RoGroupMode(self):
        return self._RoGroupMode

    @RoGroupMode.setter
    def RoGroupMode(self, RoGroupMode):
        self._RoGroupMode = RoGroupMode

    @property
    def RoGroupId(self):
        return self._RoGroupId

    @RoGroupId.setter
    def RoGroupId(self, RoGroupId):
        self._RoGroupId = RoGroupId

    @property
    def RoGroupName(self):
        return self._RoGroupName

    @RoGroupName.setter
    def RoGroupName(self, RoGroupName):
        self._RoGroupName = RoGroupName

    @property
    def RoOfflineDelay(self):
        return self._RoOfflineDelay

    @RoOfflineDelay.setter
    def RoOfflineDelay(self, RoOfflineDelay):
        self._RoOfflineDelay = RoOfflineDelay

    @property
    def RoMaxDelayTime(self):
        return self._RoMaxDelayTime

    @RoMaxDelayTime.setter
    def RoMaxDelayTime(self, RoMaxDelayTime):
        self._RoMaxDelayTime = RoMaxDelayTime

    @property
    def MinRoInGroup(self):
        return self._MinRoInGroup

    @MinRoInGroup.setter
    def MinRoInGroup(self, MinRoInGroup):
        self._MinRoInGroup = MinRoInGroup

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def RoInstances(self):
        return self._RoInstances

    @RoInstances.setter
    def RoInstances(self, RoInstances):
        self._RoInstances = RoInstances

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def RoGroupRegion(self):
        return self._RoGroupRegion

    @RoGroupRegion.setter
    def RoGroupRegion(self, RoGroupRegion):
        self._RoGroupRegion = RoGroupRegion

    @property
    def RoGroupZone(self):
        return self._RoGroupZone

    @RoGroupZone.setter
    def RoGroupZone(self, RoGroupZone):
        self._RoGroupZone = RoGroupZone

    @property
    def DelayReplicationTime(self):
        return self._DelayReplicationTime

    @DelayReplicationTime.setter
    def DelayReplicationTime(self, DelayReplicationTime):
        self._DelayReplicationTime = DelayReplicationTime


    def _deserialize(self, params):
        self._RoGroupMode = params.get("RoGroupMode")
        self._RoGroupId = params.get("RoGroupId")
        self._RoGroupName = params.get("RoGroupName")
        self._RoOfflineDelay = params.get("RoOfflineDelay")
        self._RoMaxDelayTime = params.get("RoMaxDelayTime")
        self._MinRoInGroup = params.get("MinRoInGroup")
        self._WeightMode = params.get("WeightMode")
        self._Weight = params.get("Weight")
        if params.get("RoInstances") is not None:
            self._RoInstances = []
            for item in params.get("RoInstances"):
                obj = RoInstanceInfo()
                obj._deserialize(item)
                self._RoInstances.append(obj)
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._RoGroupRegion = params.get("RoGroupRegion")
        self._RoGroupZone = params.get("RoGroupZone")
        self._DelayReplicationTime = params.get("DelayReplicationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoGroupAttr(AbstractModel):
    """RO group configuration information.

    """

    def __init__(self):
        r"""
        :param _RoGroupName: RO group name.
        :type RoGroupName: str
        :param _RoMaxDelayTime: Maximum delay threshold for RO instances in seconds. Minimum value: 1. Please note that this value will take effect only if an instance removal policy is enabled in the RO group.
        :type RoMaxDelayTime: int
        :param _RoOfflineDelay: Whether to enable instance removal. Valid values: 1 (enabled), 0 (not enabled). Please note that if instance removal is enabled, the delay threshold parameter (`RoMaxDelayTime`) must be set.
        :type RoOfflineDelay: int
        :param _MinRoInGroup: Minimum number of instances to be retained, which can be set to any value less than or equal to the number of RO instances in the RO group. Please note that if this value is set to be greater than the number of RO instances, no removal will be performed, and if it is set to 0, all instances with an excessive delay will be removed.
        :type MinRoInGroup: int
        :param _WeightMode: Weighting mode. Supported values include `system` (automatically assigned by the system) and `custom` (defined by user). Please note that if the `custom` mode is selected, the RO instance weight configuration parameter (RoWeightValues) must be set.
        :type WeightMode: str
        :param _ReplicationDelayTime: Replication delay.
        :type ReplicationDelayTime: int
        """
        self._RoGroupName = None
        self._RoMaxDelayTime = None
        self._RoOfflineDelay = None
        self._MinRoInGroup = None
        self._WeightMode = None
        self._ReplicationDelayTime = None

    @property
    def RoGroupName(self):
        return self._RoGroupName

    @RoGroupName.setter
    def RoGroupName(self, RoGroupName):
        self._RoGroupName = RoGroupName

    @property
    def RoMaxDelayTime(self):
        return self._RoMaxDelayTime

    @RoMaxDelayTime.setter
    def RoMaxDelayTime(self, RoMaxDelayTime):
        self._RoMaxDelayTime = RoMaxDelayTime

    @property
    def RoOfflineDelay(self):
        return self._RoOfflineDelay

    @RoOfflineDelay.setter
    def RoOfflineDelay(self, RoOfflineDelay):
        self._RoOfflineDelay = RoOfflineDelay

    @property
    def MinRoInGroup(self):
        return self._MinRoInGroup

    @MinRoInGroup.setter
    def MinRoInGroup(self, MinRoInGroup):
        self._MinRoInGroup = MinRoInGroup

    @property
    def WeightMode(self):
        return self._WeightMode

    @WeightMode.setter
    def WeightMode(self, WeightMode):
        self._WeightMode = WeightMode

    @property
    def ReplicationDelayTime(self):
        return self._ReplicationDelayTime

    @ReplicationDelayTime.setter
    def ReplicationDelayTime(self, ReplicationDelayTime):
        self._ReplicationDelayTime = ReplicationDelayTime


    def _deserialize(self, params):
        self._RoGroupName = params.get("RoGroupName")
        self._RoMaxDelayTime = params.get("RoMaxDelayTime")
        self._RoOfflineDelay = params.get("RoOfflineDelay")
        self._MinRoInGroup = params.get("MinRoInGroup")
        self._WeightMode = params.get("WeightMode")
        self._ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoInstanceInfo(AbstractModel):
    """RO instance details

    """

    def __init__(self):
        r"""
        :param _MasterInstanceId: Master instance ID corresponding to the RO group
        :type MasterInstanceId: str
        :param _RoStatus: RO instance status in the RO group. Value range: online, offline
        :type RoStatus: str
        :param _OfflineTime: Last deactivation time of a RO instance in the RO group
        :type OfflineTime: str
        :param _Weight: RO instance weight in the RO group
        :type Weight: int
        :param _Region: RO instance region name, such as ap-shanghai
        :type Region: str
        :param _Zone: Name of RO AZ, such as ap-shanghai-1
        :type Zone: str
        :param _InstanceId: RO instance ID in the format of cdbro-c1nl9rpv
        :type InstanceId: str
        :param _Status: RO instance status. Valid values: `0` (creating), `1` (running), `3` (remote RO), `4` (deleting). When the `DescribeDBInstances` API is used to query the information of the source instance, if the source instance is associated with a remote read-only instance, the returned status value of the remote read-only instance always shows 3.
        :type Status: int
        :param _InstanceType: Instance type. Value range: 1 (primary), 2 (disaster recovery), 3 (read-only)
        :type InstanceType: int
        :param _InstanceName: RO instance name
        :type InstanceName: str
        :param _HourFeeStatus: Pay-as-you-go billing status. Value range: 1 (normal), 2 (in arrears)
        :type HourFeeStatus: int
        :param _TaskStatus: RO instance task status. Value range: <br>0 - no task <br>1 - upgrading <br>2 - importing data <br>3 - activating secondary <br>4 - public network access enabled <br>5 - batch operation in progress <br>6 - rolling back <br>7 - public network access not enabled <br>8 - modifying password <br>9 - renaming instance <br>10 - restarting <br>12 - migrating self-built instance <br>13 - dropping table <br>14 - creating and syncing disaster recovery instance
        :type TaskStatus: int
        :param _Memory: RO instance memory size in MB
        :type Memory: int
        :param _Volume: RO instance disk size in GB
        :type Volume: int
        :param _Qps: Queries per second
        :type Qps: int
        :param _Vip: Private IP address of the RO instance
        :type Vip: str
        :param _Vport: Access port of the RO instance
        :type Vport: int
        :param _VpcId: VPC ID of the RO instance
        :type VpcId: int
        :param _SubnetId: VPC subnet ID of the RO instance
        :type SubnetId: int
        :param _DeviceType: RO instance specification description. Value range: CUSTOM
        :type DeviceType: str
        :param _EngineVersion: Database engine version of the read-only replica. Valid values: `5.1`, `5.5`, `5.6`, `5.7`, `8.0`
        :type EngineVersion: str
        :param _DeadlineTime: RO instance expiration time in the format of yyyy-mm-dd hh:mm:ss. If it is a pay-as-you-go instance, the value of this field is 0000-00-00 00:00:00
        :type DeadlineTime: str
        :param _PayType: RO instance billing method. Value range: 0 (monthly subscribed), 1 (pay-as-you-go), 2 (monthly postpaid)
        :type PayType: int
        """
        self._MasterInstanceId = None
        self._RoStatus = None
        self._OfflineTime = None
        self._Weight = None
        self._Region = None
        self._Zone = None
        self._InstanceId = None
        self._Status = None
        self._InstanceType = None
        self._InstanceName = None
        self._HourFeeStatus = None
        self._TaskStatus = None
        self._Memory = None
        self._Volume = None
        self._Qps = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._SubnetId = None
        self._DeviceType = None
        self._EngineVersion = None
        self._DeadlineTime = None
        self._PayType = None

    @property
    def MasterInstanceId(self):
        return self._MasterInstanceId

    @MasterInstanceId.setter
    def MasterInstanceId(self, MasterInstanceId):
        self._MasterInstanceId = MasterInstanceId

    @property
    def RoStatus(self):
        return self._RoStatus

    @RoStatus.setter
    def RoStatus(self, RoStatus):
        self._RoStatus = RoStatus

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HourFeeStatus(self):
        return self._HourFeeStatus

    @HourFeeStatus.setter
    def HourFeeStatus(self, HourFeeStatus):
        self._HourFeeStatus = HourFeeStatus

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._MasterInstanceId = params.get("MasterInstanceId")
        self._RoStatus = params.get("RoStatus")
        self._OfflineTime = params.get("OfflineTime")
        self._Weight = params.get("Weight")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._HourFeeStatus = params.get("HourFeeStatus")
        self._TaskStatus = params.get("TaskStatus")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._Qps = params.get("Qps")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DeviceType = params.get("DeviceType")
        self._EngineVersion = params.get("EngineVersion")
        self._DeadlineTime = params.get("DeadlineTime")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoVipInfo(AbstractModel):
    """VIP information of the read-only instance

    """

    def __init__(self):
        r"""
        :param _RoVipStatus: VIP status of the read-only instance
        :type RoVipStatus: int
        :param _RoSubnetId: VPC subnet of the read-only instance
        :type RoSubnetId: int
        :param _RoVpcId: VPC of the read-only instance
        :type RoVpcId: int
        :param _RoVport: VIP port number of the read-only instance
        :type RoVport: int
        :param _RoVip: VIP of the read-only instance
        :type RoVip: str
        """
        self._RoVipStatus = None
        self._RoSubnetId = None
        self._RoVpcId = None
        self._RoVport = None
        self._RoVip = None

    @property
    def RoVipStatus(self):
        return self._RoVipStatus

    @RoVipStatus.setter
    def RoVipStatus(self, RoVipStatus):
        self._RoVipStatus = RoVipStatus

    @property
    def RoSubnetId(self):
        return self._RoSubnetId

    @RoSubnetId.setter
    def RoSubnetId(self, RoSubnetId):
        self._RoSubnetId = RoSubnetId

    @property
    def RoVpcId(self):
        return self._RoVpcId

    @RoVpcId.setter
    def RoVpcId(self, RoVpcId):
        self._RoVpcId = RoVpcId

    @property
    def RoVport(self):
        return self._RoVport

    @RoVport.setter
    def RoVport(self, RoVport):
        self._RoVport = RoVport

    @property
    def RoVip(self):
        return self._RoVip

    @RoVip.setter
    def RoVip(self, RoVip):
        self._RoVip = RoVip


    def _deserialize(self, params):
        self._RoVipStatus = params.get("RoVipStatus")
        self._RoSubnetId = params.get("RoSubnetId")
        self._RoVpcId = params.get("RoVpcId")
        self._RoVport = params.get("RoVport")
        self._RoVip = params.get("RoVip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoWeightValue(AbstractModel):
    """RO instance weight value

    """

    def __init__(self):
        r"""
        :param _InstanceId: RO instance ID.
        :type InstanceId: str
        :param _Weight: Weight value. Value range: [0, 100].
        :type Weight: int
        """
        self._InstanceId = None
        self._Weight = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDBName(AbstractModel):
    """Name of the database for rollback

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Original database name before rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _NewDatabaseName: New database name after rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewDatabaseName: str
        """
        self._DatabaseName = None
        self._NewDatabaseName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def NewDatabaseName(self):
        return self._NewDatabaseName

    @NewDatabaseName.setter
    def NewDatabaseName(self, NewDatabaseName):
        self._NewDatabaseName = NewDatabaseName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._NewDatabaseName = params.get("NewDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstancesInfo(AbstractModel):
    """Details of the instance for rollback

    """

    def __init__(self):
        r"""
        :param _InstanceId: TencentDB instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Strategy: Rollback policy. Valid values: `table` (ultrafast mode), `db` (faster mode), and `full` (fast mode). Default value: `full`. In the ultrafast mode, only backups and binlogs of the tables specified by the `Tables` parameter are imported; if `Tables` does not include all of the tables involved in cross-table operations, the rollback may fail; and the `Database` parameter must be left empty. In the faster mode, only backups and binlogs of the databases specified by the `Databases` parameter are imported, and if `Databases` does not include all of the databases involved in cross-database operations, the rollback may fail. In the fast mode, backups and binlogs of the entire instance will be imported in a speed slower than the other modes.
        :type Strategy: str
        :param _RollbackTime: Database rollback time in the format of yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param _Databases: Information of the databases to be rolled back, which means rollback at the database level
Note: this field may return null, indicating that no valid values can be obtained.
        :type Databases: list of RollbackDBName
        :param _Tables: Information of the tables to be rolled back, which means rollback at the table level
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tables: list of RollbackTables
        """
        self._InstanceId = None
        self._Strategy = None
        self._RollbackTime = None
        self._Databases = None
        self._Tables = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def RollbackTime(self):
        return self._RollbackTime

    @RollbackTime.setter
    def RollbackTime(self, RollbackTime):
        self._RollbackTime = RollbackTime

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Tables(self):
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Strategy = params.get("Strategy")
        self._RollbackTime = params.get("RollbackTime")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = RollbackDBName()
                obj._deserialize(item)
                self._Databases.append(obj)
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = RollbackTables()
                obj._deserialize(item)
                self._Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableName(AbstractModel):
    """Name of the table for rollback

    """

    def __init__(self):
        r"""
        :param _TableName: Original table name before rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _NewTableName: New table name after rollback
Note: this field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        """
        self._TableName = None
        self._NewTableName = None

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTables(AbstractModel):
    """Details of the table for rollback

    """

    def __init__(self):
        r"""
        :param _Database: Database name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _Table: Table details
Note: this field may return null, indicating that no valid values can be obtained.
        :type Table: list of RollbackTableName
        """
        self._Database = None
        self._Table = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Database = params.get("Database")
        if params.get("Table") is not None:
            self._Table = []
            for item in params.get("Table"):
                obj = RollbackTableName()
                obj._deserialize(item)
                self._Table.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTask(AbstractModel):
    """Rollback task details

    """

    def __init__(self):
        r"""
        :param _Info: Task execution information.
        :type Info: str
        :param _Status: Task execution result. Valid values: INITIAL: initializing, RUNNING: running, SUCCESS: succeeded, FAILED: failed, KILLED: terminated, REMOVED: deleted, PAUSED: paused.
        :type Status: str
        :param _Progress: Task execution progress. Value range: [0,100].
        :type Progress: int
        :param _StartTime: Task start time.
        :type StartTime: str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _Detail: Rollback task details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Detail: list of RollbackInstancesInfo
        """
        self._Info = None
        self._Status = None
        self._Progress = None
        self._StartTime = None
        self._EndTime = None
        self._Detail = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

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
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Info = params.get("Info")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """Time range available for rollback

    """

    def __init__(self):
        r"""
        :param _Begin: Start time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-10-29 01:06:04
        :type Begin: str
        :param _End: End time available for rollback in the format of yyyy-MM-dd HH:mm:ss, such as 2016-11-02 11:44:47
        :type End: str
        """
        self._Begin = None
        self._End = None

    @property
    def Begin(self):
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Weight rule

    """

    def __init__(self):
        r"""
        :param _LessThan: The maximum weight
Note: this field may return `null`, indicating that no valid value can be found.
        :type LessThan: int
        :param _Weight: Weight
Note: this field may return `null`, indicating that no valid value can be found.
        :type Weight: int
        """
        self._LessThan = None
        self._Weight = None

    @property
    def LessThan(self):
        return self._LessThan

    @LessThan.setter
    def LessThan(self, LessThan):
        self._LessThan = LessThan

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LessThan = params.get("LessThan")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilters(AbstractModel):
    """Filter of the audit rule

    """

    def __init__(self):
        r"""
        :param _Type: Parameter name of the audit rule filter.  Valid values:  `host` (client IP), `user` (database account), `dbName` (database name), `sqlType` (SQL type), `sql` (SQL statement), `affectRows` (affected rows), `sentRows` (returned rows), `checkRows` (scanned rows), `execTime` (execution rows).
        :type Type: str
        :param _Compare: Filter match value of the audit rule Valid values:  `INC` (including), `EXC` (excluding), `EQS` (equal to), `NEQ` (not equal to), `REG` (regex), `GT` (greater than), `LT` (less than).
        :type Compare: str
        :param _Value: Filter match value of the audit rule Valid values for `sqlType`: `alter`, `changeuser`, `create`, `delete`, `drop`, `execute`, `insert`, `login`, `logout`, `other`, `replace`, `select`, `set, `update`.
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param _Inbound: Inbound rule
        :type Inbound: list of Inbound
        :param _Outbound: Outbound rule
        :type Outbound: list of Outbound
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveConfig(AbstractModel):
    """Configuration information of the salve database

    """

    def __init__(self):
        r"""
        :param _ReplicationMode: Replication mode of the secondary database. Value range: async, semi-sync
        :type ReplicationMode: str
        :param _Zone: AZ name of the secondary database, such as ap-shanghai-1
        :type Zone: str
        """
        self._ReplicationMode = None
        self._Zone = None

    @property
    def ReplicationMode(self):
        return self._ReplicationMode

    @ReplicationMode.setter
    def ReplicationMode(self, ReplicationMode):
        self._ReplicationMode = ReplicationMode

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ReplicationMode = params.get("ReplicationMode")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInfo(AbstractModel):
    """Slave server information

    """

    def __init__(self):
        r"""
        :param _First: Information of secondary server 1
        :type First: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        :param _Second: Information of secondary server 2
Note: This field may return null, indicating that no valid values can be obtained.
        :type Second: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        """
        self._First = None
        self._Second = None

    @property
    def First(self):
        return self._First

    @First.setter
    def First(self, First):
        self._First = First

    @property
    def Second(self):
        return self._Second

    @Second.setter
    def Second(self, Second):
        self._Second = Second


    def _deserialize(self, params):
        if params.get("First") is not None:
            self._First = SlaveInstanceInfo()
            self._First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self._Second = SlaveInstanceInfo()
            self._Second._deserialize(params.get("Second"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInstanceInfo(AbstractModel):
    """Slave server information

    """

    def __init__(self):
        r"""
        :param _Vport: Port number
        :type Vport: int
        :param _Region: Region information
        :type Region: str
        :param _Vip: Virtual IP information
        :type Vip: str
        :param _Zone: AZ information
        :type Zone: str
        """
        self._Vport = None
        self._Region = None
        self._Vip = None
        self._Zone = None

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Vport = params.get("Vport")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfo(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        r"""
        :param _Name: Backup filename
        :type Name: str
        :param _Size: Backup file size in bytes
        :type Size: int
        :param _Date: Backup snapshot time in the format of yyyy-MM-dd HH:mm:ss, such as 2016-03-17 02:10:37
        :type Date: str
        :param _IntranetUrl: Download address on the private network
        :type IntranetUrl: str
        :param _InternetUrl: Download address on the public network
        :type InternetUrl: str
        :param _Type: Log type. Value range: slowlog (slow log)
        :type Type: str
        """
        self._Name = None
        self._Size = None
        self._Date = None
        self._IntranetUrl = None
        self._InternetUrl = None
        self._Type = None

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

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def IntranetUrl(self):
        return self._IntranetUrl

    @IntranetUrl.setter
    def IntranetUrl(self, IntranetUrl):
        self._IntranetUrl = IntranetUrl

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Date = params.get("Date")
        self._IntranetUrl = params.get("IntranetUrl")
        self._InternetUrl = params.get("InternetUrl")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogItem(AbstractModel):
    """Structured slow log details

    """

    def __init__(self):
        r"""
        :param _Timestamp: SQL execution time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Timestamp: int
        :param _QueryTime: SQL execution duration in seconds.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type QueryTime: float
        :param _SqlText: SQL statement.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SqlText: str
        :param _UserHost: Client address.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserHost: str
        :param _UserName: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Database: Database name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _LockTime: Lock duration in seconds.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LockTime: float
        :param _RowsExamined: Number of scanned rows.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RowsExamined: int
        :param _RowsSent: Number of rows in result set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RowsSent: int
        :param _SqlTemplate: SQL template.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SqlTemplate: str
        :param _Md5: SQL statement MD5.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Md5: str
        """
        self._Timestamp = None
        self._QueryTime = None
        self._SqlText = None
        self._UserHost = None
        self._UserName = None
        self._Database = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None
        self._SqlTemplate = None
        self._Md5 = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def SqlTemplate(self):
        return self._SqlTemplate

    @SqlTemplate.setter
    def SqlTemplate(self, SqlTemplate):
        self._SqlTemplate = SqlTemplate

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._QueryTime = params.get("QueryTime")
        self._SqlText = params.get("SqlText")
        self._UserHost = params.get("UserHost")
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        self._SqlTemplate = params.get("SqlTemplate")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlFileInfo(AbstractModel):
    """SQL file information

    """

    def __init__(self):
        r"""
        :param _UploadTime: Upload time
        :type UploadTime: str
        :param _UploadInfo: Upload progress
        :type UploadInfo: :class:`tencentcloud.cdb.v20170320.models.UploadInfo`
        :param _FileName: Filename
        :type FileName: str
        :param _FileSize: File size in bytes
        :type FileSize: int
        :param _IsUploadFinished: Whether upload is finished. Valid values: 0 (not completed), 1 (completed)
        :type IsUploadFinished: int
        :param _FileId: File ID
        :type FileId: str
        """
        self._UploadTime = None
        self._UploadInfo = None
        self._FileName = None
        self._FileSize = None
        self._IsUploadFinished = None
        self._FileId = None

    @property
    def UploadTime(self):
        return self._UploadTime

    @UploadTime.setter
    def UploadTime(self, UploadTime):
        self._UploadTime = UploadTime

    @property
    def UploadInfo(self):
        return self._UploadInfo

    @UploadInfo.setter
    def UploadInfo(self, UploadInfo):
        self._UploadInfo = UploadInfo

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def IsUploadFinished(self):
        return self._IsUploadFinished

    @IsUploadFinished.setter
    def IsUploadFinished(self, IsUploadFinished):
        self._IsUploadFinished = IsUploadFinished

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._UploadTime = params.get("UploadTime")
        if params.get("UploadInfo") is not None:
            self._UploadInfo = UploadInfo()
            self._UploadInfo._deserialize(params.get("UploadInfo"))
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._IsUploadFinished = params.get("IsUploadFinished")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback request structure.

    """

    def __init__(self):
        r"""
        :param _Instances: Details of the instance for rollback
        :type Instances: list of RollbackInstancesInfo
        """
        self._Instances = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StartReplicationRequest(AbstractModel):
    """StartReplication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Read-Only instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartReplicationResponse(AbstractModel):
    """StartReplication response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopReplicationRequest(AbstractModel):
    """StopReplication request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Read-Only instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopReplicationResponse(AbstractModel):
    """StopReplication response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class StopRollbackRequest(AbstractModel):
    """StopRollback request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance whose rollback task is canceled
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRollbackResponse(AbstractModel):
    """StopRollback response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchCDBProxyRequest(AbstractModel):
    """SwitchCDBProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Database proxy ID
        :type ProxyGroupId: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCDBProxyResponse(AbstractModel):
    """SwitchCDBProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SwitchDBInstanceMasterSlaveRequest(AbstractModel):
    """SwitchDBInstanceMasterSlave request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DstSlave: Specifies the replica server to switched to. Valid values: `first` (the first replica server), `second` (the second replica server). Default value: `first`. `second` is valid only for a multi-AZ instance.
        :type DstSlave: str
        :param _ForceSwitch: Whether to force the switch. Valid values: `True`, `False` (default). If this parameter is set to `True`, instance data may be lost during the switch.
        :type ForceSwitch: bool
        :param _WaitSwitch: Whether to perform the switch during a time window. Valid values: `True`, `False` (default). If `ForceSwitch` is set to `True`, this parameter is invalid.
        :type WaitSwitch: bool
        """
        self._InstanceId = None
        self._DstSlave = None
        self._ForceSwitch = None
        self._WaitSwitch = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DstSlave(self):
        return self._DstSlave

    @DstSlave.setter
    def DstSlave(self, DstSlave):
        self._DstSlave = DstSlave

    @property
    def ForceSwitch(self):
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DstSlave = params.get("DstSlave")
        self._ForceSwitch = params.get("ForceSwitch")
        self._WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceMasterSlaveResponse(AbstractModel):
    """SwitchDBInstanceMasterSlave response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchDrInstanceToMasterRequest(AbstractModel):
    """SwitchDrInstanceToMaster request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Disaster recovery instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrInstanceToMasterResponse(AbstractModel):
    """SwitchDrInstanceToMaster response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        r"""
        :param _Database: Database name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Privileges: Permission information
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag structure

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoItem(AbstractModel):
    """Tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoUnit(AbstractModel):
    """Tag information unit

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagsInfoOfInstance(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Tags: Tag information
        :type Tags: list of TagInfoUnit
        """
        self._InstanceId = None
        self._Tags = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """Details of an instance task

    """

    def __init__(self):
        r"""
        :param _Code: Error code.
        :type Code: int
        :param _Message: Error message.
        :type Message: str
        :param _JobId: ID of an instance task.
        :type JobId: int
        :param _Progress: Instance task progress.
        :type Progress: int
        :param _TaskStatus: Instance task status. Valid values:
"UNDEFINED" - undefined;
"INITIAL" - initializing;
"RUNNING" - running;
"SUCCEED" - succeeded;
"FAILED" - failed;
"KILLED" - terminated;
"REMOVED" - deleted;
"PAUSED" - paused.
"WAITING" - waiting (which can be canceled)
        :type TaskStatus: str
        :param _TaskType: Instance task type. Valid values:
"ROLLBACK" - rolling back a database;
"SQL OPERATION" - performing an SQL operation;
"IMPORT DATA" - importing data;
"MODIFY PARAM" - setting a parameter;
"INITIAL" - initializing a TencentDB instance;
"REBOOT" - restarting a TencentDB instance;
"OPEN GTID" - enabling GTID of a TencentDB instance;
"UPGRADE RO" - upgrading a read-only instance;
"BATCH ROLLBACK" - rolling back databases in batches;
"UPGRADE MASTER" - upgrading a primary instance;
"DROP TABLES" - dropping a TencentDB table;
"SWITCH DR TO MASTER" - promoting a disaster recovery instance.
        :type TaskType: str
        :param _StartTime: Instance task start time.
        :type StartTime: str
        :param _EndTime: Instance task end time.
        :type EndTime: str
        :param _InstanceIds: ID of an instance associated with a task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceIds: list of str
        :param _AsyncRequestId: Async task request ID.
        :type AsyncRequestId: str
        """
        self._Code = None
        self._Message = None
        self._JobId = None
        self._Progress = None
        self._TaskStatus = None
        self._TaskType = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceIds = None
        self._AsyncRequestId = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._JobId = params.get("JobId")
        self._Progress = params.get("Progress")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskType = params.get("TaskType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceIds = params.get("InstanceIds")
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyVersionRequest(AbstractModel):
    """UpgradeCDBProxyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyGroupId: Database proxy ID
        :type ProxyGroupId: str
        :param _SrcProxyVersion: Current version of database proxy
        :type SrcProxyVersion: str
        :param _DstProxyVersion: Target version of database proxy
        :type DstProxyVersion: str
        :param _UpgradeTime: Upgrade time. Valid values: `nowTime` (upgrade immediately), `timeWindow` (upgrade during instance maintenance time)
        :type UpgradeTime: str
        """
        self._InstanceId = None
        self._ProxyGroupId = None
        self._SrcProxyVersion = None
        self._DstProxyVersion = None
        self._UpgradeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyGroupId(self):
        return self._ProxyGroupId

    @ProxyGroupId.setter
    def ProxyGroupId(self, ProxyGroupId):
        self._ProxyGroupId = ProxyGroupId

    @property
    def SrcProxyVersion(self):
        return self._SrcProxyVersion

    @SrcProxyVersion.setter
    def SrcProxyVersion(self, SrcProxyVersion):
        self._SrcProxyVersion = SrcProxyVersion

    @property
    def DstProxyVersion(self):
        return self._DstProxyVersion

    @DstProxyVersion.setter
    def DstProxyVersion(self, DstProxyVersion):
        self._DstProxyVersion = DstProxyVersion

    @property
    def UpgradeTime(self):
        return self._UpgradeTime

    @UpgradeTime.setter
    def UpgradeTime(self, UpgradeTime):
        self._UpgradeTime = UpgradeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyGroupId = params.get("ProxyGroupId")
        self._SrcProxyVersion = params.get("SrcProxyVersion")
        self._DstProxyVersion = params.get("DstProxyVersion")
        self._UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyVersionResponse(AbstractModel):
    """UpgradeCDBProxyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async request ID
Note: this field may return `null`, indicating that no valid value can be found.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [instance list querying API](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param _EngineVersion: Version of primary instance database engine. Value range: 5.6, 5.7
        :type EngineVersion: str
        :param _WaitSwitch: Switch mode for accessing the new instance.  Valid values:  `0` (switch immediately), `1` (switch within a time window). Default value: `0`. If the value is `1`, the switch process will be performed within a time window. Or, you can call the [SwitchForUpgrade](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) API to trigger the process.
        :type WaitSwitch: int
        :param _UpgradeSubversion: Whether to upgrade kernel minor version. Valid values: 1 (upgrade kernel minor version), 0 (upgrade database engine).
        :type UpgradeSubversion: int
        :param _MaxDelayTime: Delay threshold. Value range: 1-10
        :type MaxDelayTime: int
        """
        self._InstanceId = None
        self._EngineVersion = None
        self._WaitSwitch = None
        self._UpgradeSubversion = None
        self._MaxDelayTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def UpgradeSubversion(self):
        return self._UpgradeSubversion

    @UpgradeSubversion.setter
    def UpgradeSubversion(self, UpgradeSubversion):
        self._UpgradeSubversion = UpgradeSubversion

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EngineVersion = params.get("EngineVersion")
        self._WaitSwitch = params.get("WaitSwitch")
        self._UpgradeSubversion = params.get("UpgradeSubversion")
        self._MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task ID. The task execution result can be queried using the [async task execution result querying API](https://intl.cloud.tencent.com/document/api/236/20410?from_cn_redirect=1).
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of `cdb-c1nl9rpv` or `cdbro-c1nl9rpv`. It is the same as the instance ID displayed on the TencentDB Console page. You can use the [DescribeDBInstances](https://intl.cloud.tencent.com/document/api/236/15872?from_cn_redirect=1) API to query the ID, whose value is the `InstanceId` value in output parameters.
        :type InstanceId: str
        :param _Memory: Memory size in MB after upgrade. To ensure that the `Memory` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the memory that can be upgraded to.
        :type Memory: int
        :param _Volume: Disk size in GB after upgrade. To ensure that the `Volume` value to be passed in is valid, please use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the specifications of the disk that can be upgraded to.
        :type Volume: int
        :param _ProtectMode: Data replication mode. Valid values: 0 (async), 1 (semi-sync), 2 (strong sync). This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type ProtectMode: int
        :param _DeployMode: Deployment mode. Valid values: 0 (single-AZ), 1 (multi-AZ). Default value: 0. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type DeployMode: int
        :param _SlaveZone: AZ information of secondary database 1, which is the `Zone` value of the instance by default. This parameter can be specified when upgrading primary instances in multi-AZ mode and is meaningless for read-only or disaster recovery instances. You can use the [DescribeDBZoneConfig](https://intl.cloud.tencent.com/document/product/236/17229?from_cn_redirect=1) API to query the supported AZs.
        :type SlaveZone: str
        :param _EngineVersion: Version of primary instance database engine. Valid values: 5.5, 5.6, 5.7.
        :type EngineVersion: str
        :param _WaitSwitch: Switch mode for accessing the new instance.  Valid values:  `0` (switch immediately), `1` (switch within a time window). Default value: `0`. If the value is `1`, the switch process will be performed within a time window. Or, you can call the [SwitchForUpgrade](https://intl.cloud.tencent.com/document/product/236/15864?from_cn_redirect=1) API to trigger the process.
        :type WaitSwitch: int
        :param _BackupZone: AZ information of secondary database 2, which is empty by default. This parameter can be specified when upgrading primary instances and is meaningless for read-only or disaster recovery instances.
        :type BackupZone: str
        :param _InstanceRole: Instance type. Valid values: master (primary instance), dr (disaster recovery instance), ro (read-only instance). Default value: master.
        :type InstanceRole: str
        :param _DeviceType: The resource isolation type after the instance is upgraded. Valid values: `UNIVERSAL` (general instance), `EXCLUSIVE` (dedicated instance), `BASIC` (basic instance). If this parameter is left empty, the resource isolation type will be the same as the original one.
        :type DeviceType: str
        :param _Cpu: The number of CPU cores after the instance is upgraded. If this parameter is left empty, it will be subject to the `Memory` value.
        :type Cpu: int
        :param _FastUpgrade: QuickChange options. Valid values: `0` (common upgrade), `1` (QuickChange), `2` (QuickChange first). After QuickChange is enabled, the required resources will be checked. QuickChange will be performed only when the required resources support the feature; otherwise, an error message will be returned.
        :type FastUpgrade: int
        :param _MaxDelayTime: Delay threshold. Value range: 1-10. Default value: `10`.
        :type MaxDelayTime: int
        :param _CrossCluster: Whether to migrate the source node across AZs. Valid values: `0` (no), `1`(yes). Default value: `0`. If it is `1`, you can modify the source node AZ.
        :type CrossCluster: int
        :param _ZoneId: New AZ of the source node. This field is only valid when `CrossCluster` is `1`. Only migration across AZs in the same region is supported.
        :type ZoneId: str
        :param _RoTransType: Processing logic of the intra-AZ read-only instance for cross-cluster migration. Valid values: `together` (intra-AZ read-only instances will be migrated to the target AZ with the source instance by default.), `severally` (intra-AZ read-only instances will maintain the original deployment mode and will not be migrated to the target AZ.).
        :type RoTransType: str
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._ProtectMode = None
        self._DeployMode = None
        self._SlaveZone = None
        self._EngineVersion = None
        self._WaitSwitch = None
        self._BackupZone = None
        self._InstanceRole = None
        self._DeviceType = None
        self._Cpu = None
        self._FastUpgrade = None
        self._MaxDelayTime = None
        self._CrossCluster = None
        self._ZoneId = None
        self._RoTransType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def ProtectMode(self):
        return self._ProtectMode

    @ProtectMode.setter
    def ProtectMode(self, ProtectMode):
        self._ProtectMode = ProtectMode

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def WaitSwitch(self):
        return self._WaitSwitch

    @WaitSwitch.setter
    def WaitSwitch(self, WaitSwitch):
        self._WaitSwitch = WaitSwitch

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def FastUpgrade(self):
        return self._FastUpgrade

    @FastUpgrade.setter
    def FastUpgrade(self, FastUpgrade):
        self._FastUpgrade = FastUpgrade

    @property
    def MaxDelayTime(self):
        return self._MaxDelayTime

    @MaxDelayTime.setter
    def MaxDelayTime(self, MaxDelayTime):
        self._MaxDelayTime = MaxDelayTime

    @property
    def CrossCluster(self):
        return self._CrossCluster

    @CrossCluster.setter
    def CrossCluster(self, CrossCluster):
        self._CrossCluster = CrossCluster

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoTransType(self):
        return self._RoTransType

    @RoTransType.setter
    def RoTransType(self, RoTransType):
        self._RoTransType = RoTransType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._ProtectMode = params.get("ProtectMode")
        self._DeployMode = params.get("DeployMode")
        self._SlaveZone = params.get("SlaveZone")
        self._EngineVersion = params.get("EngineVersion")
        self._WaitSwitch = params.get("WaitSwitch")
        self._BackupZone = params.get("BackupZone")
        self._InstanceRole = params.get("InstanceRole")
        self._DeviceType = params.get("DeviceType")
        self._Cpu = params.get("Cpu")
        self._FastUpgrade = params.get("FastUpgrade")
        self._MaxDelayTime = params.get("MaxDelayTime")
        self._CrossCluster = params.get("CrossCluster")
        self._ZoneId = params.get("ZoneId")
        self._RoTransType = params.get("RoTransType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealIds: Order ID.
        :type DealIds: list of str
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealIds = None
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def AsyncRequestId(self):
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UploadInfo(AbstractModel):
    """File upload description

    """

    def __init__(self):
        r"""
        :param _AllSliceNum: Number of parts of file
        :type AllSliceNum: int
        :param _CompleteNum: Number of completed parts
        :type CompleteNum: int
        """
        self._AllSliceNum = None
        self._CompleteNum = None

    @property
    def AllSliceNum(self):
        return self._AllSliceNum

    @AllSliceNum.setter
    def AllSliceNum(self, AllSliceNum):
        self._AllSliceNum = AllSliceNum

    @property
    def CompleteNum(self):
        return self._CompleteNum

    @CompleteNum.setter
    def CompleteNum(self, CompleteNum):
        self._CompleteNum = CompleteNum


    def _deserialize(self, params):
        self._AllSliceNum = params.get("AllSliceNum")
        self._CompleteNum = params.get("CompleteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneConf(AbstractModel):
    """Multi-AZ information

    """

    def __init__(self):
        r"""
        :param _DeployMode: AZ deployment mode. Value range: 0 (single-AZ), 1 (multi-AZ)
        :type DeployMode: list of int
        :param _MasterZone: AZ where the primary instance is located
        :type MasterZone: list of str
        :param _SlaveZone: AZ where salve database 1 is located when the instance is deployed in multi-AZ mode
        :type SlaveZone: list of str
        :param _BackupZone: AZ where salve database 2 is located when the instance is deployed in multi-AZ mode
        :type BackupZone: list of str
        """
        self._DeployMode = None
        self._MasterZone = None
        self._SlaveZone = None
        self._BackupZone = None

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MasterZone(self):
        return self._MasterZone

    @MasterZone.setter
    def MasterZone(self, MasterZone):
        self._MasterZone = MasterZone

    @property
    def SlaveZone(self):
        return self._SlaveZone

    @SlaveZone.setter
    def SlaveZone(self, SlaveZone):
        self._SlaveZone = SlaveZone

    @property
    def BackupZone(self):
        return self._BackupZone

    @BackupZone.setter
    def BackupZone(self, BackupZone):
        self._BackupZone = BackupZone


    def _deserialize(self, params):
        self._DeployMode = params.get("DeployMode")
        self._MasterZone = params.get("MasterZone")
        self._SlaveZone = params.get("SlaveZone")
        self._BackupZone = params.get("BackupZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        