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


class CancelSparkSessionBatchSQLRequest(AbstractModel):
    """CancelSparkSessionBatchSQL request structure.

    """

    def __init__(self):
        r"""
        :param _BatchId: The unique identifier of a batch task.
        :type BatchId: str
        """
        self._BatchId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelSparkSessionBatchSQLResponse(AbstractModel):
    """CancelSparkSessionBatchSQL response structure.

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


class CancelTaskRequest(AbstractModel):
    """CancelTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Globally unique task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask response structure.

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


class Column(AbstractModel):
    """Column information of the data table.

    """

    def __init__(self):
        r"""
        :param _Name: Column name, which is case-insensitive and can contain up to 25 characters.
        :type Name: str
        :param _Type: Column type. Valid values:
string|tinyint|smallint|int|bigint|boolean|float|double|decimal|timestamp|date|binary|array<data_type>|map<primitive_type, data_type>|struct<col_name : data_type [COMMENT col_comment], ...>|uniontype<data_type, data_type, ...>.
        :type Type: str
        :param _Comment: Class comment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Comment: str
        :param _Precision: Length of the entire numeric value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Precision: int
        :param _Scale: Length of the decimal part
Note: This field may return null, indicating that no valid values can be obtained.
        :type Scale: int
        :param _Nullable: Whether the column is null.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nullable: str
        :param _Position: Field position
Note: This field may return null, indicating that no valid values can be obtained.
        :type Position: int
        :param _CreateTime: Field creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ModifiedTime: Field modification time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifiedTime: str
        :param _IsPartition: Whether the column is the partition field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPartition: bool
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Precision = None
        self._Scale = None
        self._Nullable = None
        self._Position = None
        self._CreateTime = None
        self._ModifiedTime = None
        self._IsPartition = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Precision(self):
        return self._Precision

    @Precision.setter
    def Precision(self, Precision):
        self._Precision = Precision

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def Nullable(self):
        return self._Nullable

    @Nullable.setter
    def Nullable(self, Nullable):
        self._Nullable = Nullable

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def IsPartition(self):
        return self._IsPartition

    @IsPartition.setter
    def IsPartition(self, IsPartition):
        self._IsPartition = IsPartition


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Precision = params.get("Precision")
        self._Scale = params.get("Scale")
        self._Nullable = params.get("Nullable")
        self._Position = params.get("Position")
        self._CreateTime = params.get("CreateTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._IsPartition = params.get("IsPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMetrics(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _CreateTaskTime: 
        :type CreateTaskTime: float
        :param _ProcessTime: 
        :type ProcessTime: float
        :param _QueueTime: 
        :type QueueTime: float
        :param _ExecutionTime: 
        :type ExecutionTime: float
        :param _IsResultCacheHit: 
        :type IsResultCacheHit: bool
        :param _MatchedMVBytes: 
        :type MatchedMVBytes: int
        :param _MatchedMVs: 
        :type MatchedMVs: str
        :param _AffectedBytes: 
        :type AffectedBytes: str
        :param _AffectedRows: 
        :type AffectedRows: int
        :param _ProcessedBytes: 
        :type ProcessedBytes: int
        :param _ProcessedRows: 
        :type ProcessedRows: int
        """
        self._CreateTaskTime = None
        self._ProcessTime = None
        self._QueueTime = None
        self._ExecutionTime = None
        self._IsResultCacheHit = None
        self._MatchedMVBytes = None
        self._MatchedMVs = None
        self._AffectedBytes = None
        self._AffectedRows = None
        self._ProcessedBytes = None
        self._ProcessedRows = None

    @property
    def CreateTaskTime(self):
        return self._CreateTaskTime

    @CreateTaskTime.setter
    def CreateTaskTime(self, CreateTaskTime):
        self._CreateTaskTime = CreateTaskTime

    @property
    def ProcessTime(self):
        return self._ProcessTime

    @ProcessTime.setter
    def ProcessTime(self, ProcessTime):
        self._ProcessTime = ProcessTime

    @property
    def QueueTime(self):
        return self._QueueTime

    @QueueTime.setter
    def QueueTime(self, QueueTime):
        self._QueueTime = QueueTime

    @property
    def ExecutionTime(self):
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def IsResultCacheHit(self):
        return self._IsResultCacheHit

    @IsResultCacheHit.setter
    def IsResultCacheHit(self, IsResultCacheHit):
        self._IsResultCacheHit = IsResultCacheHit

    @property
    def MatchedMVBytes(self):
        return self._MatchedMVBytes

    @MatchedMVBytes.setter
    def MatchedMVBytes(self, MatchedMVBytes):
        self._MatchedMVBytes = MatchedMVBytes

    @property
    def MatchedMVs(self):
        return self._MatchedMVs

    @MatchedMVs.setter
    def MatchedMVs(self, MatchedMVs):
        self._MatchedMVs = MatchedMVs

    @property
    def AffectedBytes(self):
        return self._AffectedBytes

    @AffectedBytes.setter
    def AffectedBytes(self, AffectedBytes):
        self._AffectedBytes = AffectedBytes

    @property
    def AffectedRows(self):
        return self._AffectedRows

    @AffectedRows.setter
    def AffectedRows(self, AffectedRows):
        self._AffectedRows = AffectedRows

    @property
    def ProcessedBytes(self):
        return self._ProcessedBytes

    @ProcessedBytes.setter
    def ProcessedBytes(self, ProcessedBytes):
        self._ProcessedBytes = ProcessedBytes

    @property
    def ProcessedRows(self):
        return self._ProcessedRows

    @ProcessedRows.setter
    def ProcessedRows(self, ProcessedRows):
        self._ProcessedRows = ProcessedRows


    def _deserialize(self, params):
        self._CreateTaskTime = params.get("CreateTaskTime")
        self._ProcessTime = params.get("ProcessTime")
        self._QueueTime = params.get("QueueTime")
        self._ExecutionTime = params.get("ExecutionTime")
        self._IsResultCacheHit = params.get("IsResultCacheHit")
        self._MatchedMVBytes = params.get("MatchedMVBytes")
        self._MatchedMVs = params.get("MatchedMVs")
        self._AffectedBytes = params.get("AffectedBytes")
        self._AffectedRows = params.get("AffectedRows")
        self._ProcessedBytes = params.get("ProcessedBytes")
        self._ProcessedRows = params.get("ProcessedRows")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataEngineRequest(AbstractModel):
    """CreateDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param _EngineType: The engine type. Valid values: `spark` and `presto`.
        :type EngineType: str
        :param _DataEngineName: The name of the virtual cluster.
        :type DataEngineName: str
        :param _ClusterType: The cluster type. Valid values: `spark_private`, `presto_private`, `presto_cu`, and `spark_cu`.
        :type ClusterType: str
        :param _Mode: The billing mode. Valid values: `0` (shared engine), `1` (pay-as-you-go), and `2` (monthly subscription).
        :type Mode: int
        :param _AutoResume: Whether to automatically start the clusters.
        :type AutoResume: bool
        :param _MinClusters: The minimum number of clusters.
        :type MinClusters: int
        :param _MaxClusters: The maximum number of clusters.
        :type MaxClusters: int
        :param _DefaultDataEngine: Whether the cluster is the default one.
        :type DefaultDataEngine: bool
        :param _CidrBlock: The VPC CIDR block.
        :type CidrBlock: str
        :param _Message: The description.
        :type Message: str
        :param _Size: The cluster size.
        :type Size: int
        :param _PayMode: The pay mode. Valid value: `0` (postpaid, default) and `1` (prepaid) (currently not available).
        :type PayMode: int
        :param _TimeSpan: The resource period. For the postpaid mode, the value is 3600 (default); for the prepaid mode, the value must be in the range of 1–120, representing purchasing the resource for 1–120 months.
        :type TimeSpan: int
        :param _TimeUnit: The unit of the resource period. Valid values: `s` (default) for the postpaid mode and `m` for the prepaid mode.
        :type TimeUnit: str
        :param _AutoRenew: The auto-renewal status of the resource. For the postpaid mode, no renewal is required, and the value is fixed to `0`. For the prepaid mode, valid values are `0` (manual), `1` (auto), and `2` (no renewal). If this parameter is set to `0` for a key account in the prepaid mode, auto-renewal applies. It defaults to `0`.
        :type AutoRenew: int
        :param _Tags: The tags to be set for the resource being created.
        :type Tags: list of TagInfo
        :param _AutoSuspend: Whether to automatically suspend clusters. Valid values: `false` (default, no) and `true` (yes).
        :type AutoSuspend: bool
        :param _CrontabResumeSuspend: Whether to enable scheduled start and suspension of clusters. Valid values: `0` (disable) and `1` (enable). Note: This policy and the auto-suspension policy are mutually exclusive.
        :type CrontabResumeSuspend: int
        :param _CrontabResumeSuspendStrategy: The complex policy for scheduled start and suspension, including the start/suspension time and suspension policy.
        :type CrontabResumeSuspendStrategy: :class:`tencentcloud.dlc.v20210125.models.CrontabResumeSuspendStrategy`
        :param _EngineExecType: The type of tasks to be executed by the engine, which defaults to SQL.
        :type EngineExecType: str
        :param _MaxConcurrency: The max task concurrency of a cluster, which defaults to 5.
        :type MaxConcurrency: int
        :param _TolerableQueueTime: The task queue time limit, which defaults to 0. When the actual queue time exceeds the value set here, scale-out may be triggered. Setting this parameter to 0 represents that scale-out may be triggered immediately after a task queues up.
        :type TolerableQueueTime: int
        :param _AutoSuspendTime: The cluster auto-suspension time, which defaults to 10 min.
        :type AutoSuspendTime: int
        :param _ResourceType: The resource type. Valid values: `Standard_CU` (standard) and `Memory_CU` (memory).
        :type ResourceType: str
        :param _DataEngineConfigPairs: The advanced configurations of clusters.
        :type DataEngineConfigPairs: list of DataEngineConfigPair
        :param _ImageVersionName: The version name of cluster image, such as SuperSQL-P 1.1 and SuperSQL-S 3.2. If no value is passed in, a cluster is created using the latest image version.
        :type ImageVersionName: str
        :param _MainClusterName: The name of the primary cluster.
        :type MainClusterName: str
        :param _ElasticSwitch: Whether to enable the scaling feature for a monthly subscribed Spark job cluster.
        :type ElasticSwitch: bool
        :param _ElasticLimit: The upper limit (in CUs) for scaling of the monthly subscribed Spark job cluster.
        :type ElasticLimit: int
        :param _SessionResourceTemplate: The session resource configuration template for a Spark job cluster.
        :type SessionResourceTemplate: :class:`tencentcloud.dlc.v20210125.models.SessionResourceTemplate`
        """
        self._EngineType = None
        self._DataEngineName = None
        self._ClusterType = None
        self._Mode = None
        self._AutoResume = None
        self._MinClusters = None
        self._MaxClusters = None
        self._DefaultDataEngine = None
        self._CidrBlock = None
        self._Message = None
        self._Size = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._AutoRenew = None
        self._Tags = None
        self._AutoSuspend = None
        self._CrontabResumeSuspend = None
        self._CrontabResumeSuspendStrategy = None
        self._EngineExecType = None
        self._MaxConcurrency = None
        self._TolerableQueueTime = None
        self._AutoSuspendTime = None
        self._ResourceType = None
        self._DataEngineConfigPairs = None
        self._ImageVersionName = None
        self._MainClusterName = None
        self._ElasticSwitch = None
        self._ElasticLimit = None
        self._SessionResourceTemplate = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def AutoResume(self):
        return self._AutoResume

    @AutoResume.setter
    def AutoResume(self, AutoResume):
        self._AutoResume = AutoResume

    @property
    def MinClusters(self):
        return self._MinClusters

    @MinClusters.setter
    def MinClusters(self, MinClusters):
        self._MinClusters = MinClusters

    @property
    def MaxClusters(self):
        return self._MaxClusters

    @MaxClusters.setter
    def MaxClusters(self, MaxClusters):
        self._MaxClusters = MaxClusters

    @property
    def DefaultDataEngine(self):
        return self._DefaultDataEngine

    @DefaultDataEngine.setter
    def DefaultDataEngine(self, DefaultDataEngine):
        self._DefaultDataEngine = DefaultDataEngine

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSuspend(self):
        return self._AutoSuspend

    @AutoSuspend.setter
    def AutoSuspend(self, AutoSuspend):
        self._AutoSuspend = AutoSuspend

    @property
    def CrontabResumeSuspend(self):
        return self._CrontabResumeSuspend

    @CrontabResumeSuspend.setter
    def CrontabResumeSuspend(self, CrontabResumeSuspend):
        self._CrontabResumeSuspend = CrontabResumeSuspend

    @property
    def CrontabResumeSuspendStrategy(self):
        return self._CrontabResumeSuspendStrategy

    @CrontabResumeSuspendStrategy.setter
    def CrontabResumeSuspendStrategy(self, CrontabResumeSuspendStrategy):
        self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy

    @property
    def EngineExecType(self):
        return self._EngineExecType

    @EngineExecType.setter
    def EngineExecType(self, EngineExecType):
        self._EngineExecType = EngineExecType

    @property
    def MaxConcurrency(self):
        return self._MaxConcurrency

    @MaxConcurrency.setter
    def MaxConcurrency(self, MaxConcurrency):
        self._MaxConcurrency = MaxConcurrency

    @property
    def TolerableQueueTime(self):
        return self._TolerableQueueTime

    @TolerableQueueTime.setter
    def TolerableQueueTime(self, TolerableQueueTime):
        self._TolerableQueueTime = TolerableQueueTime

    @property
    def AutoSuspendTime(self):
        return self._AutoSuspendTime

    @AutoSuspendTime.setter
    def AutoSuspendTime(self, AutoSuspendTime):
        self._AutoSuspendTime = AutoSuspendTime

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def DataEngineConfigPairs(self):
        return self._DataEngineConfigPairs

    @DataEngineConfigPairs.setter
    def DataEngineConfigPairs(self, DataEngineConfigPairs):
        self._DataEngineConfigPairs = DataEngineConfigPairs

    @property
    def ImageVersionName(self):
        return self._ImageVersionName

    @ImageVersionName.setter
    def ImageVersionName(self, ImageVersionName):
        self._ImageVersionName = ImageVersionName

    @property
    def MainClusterName(self):
        return self._MainClusterName

    @MainClusterName.setter
    def MainClusterName(self, MainClusterName):
        self._MainClusterName = MainClusterName

    @property
    def ElasticSwitch(self):
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticLimit(self):
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def SessionResourceTemplate(self):
        return self._SessionResourceTemplate

    @SessionResourceTemplate.setter
    def SessionResourceTemplate(self, SessionResourceTemplate):
        self._SessionResourceTemplate = SessionResourceTemplate


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        self._DataEngineName = params.get("DataEngineName")
        self._ClusterType = params.get("ClusterType")
        self._Mode = params.get("Mode")
        self._AutoResume = params.get("AutoResume")
        self._MinClusters = params.get("MinClusters")
        self._MaxClusters = params.get("MaxClusters")
        self._DefaultDataEngine = params.get("DefaultDataEngine")
        self._CidrBlock = params.get("CidrBlock")
        self._Message = params.get("Message")
        self._Size = params.get("Size")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoRenew = params.get("AutoRenew")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSuspend = params.get("AutoSuspend")
        self._CrontabResumeSuspend = params.get("CrontabResumeSuspend")
        if params.get("CrontabResumeSuspendStrategy") is not None:
            self._CrontabResumeSuspendStrategy = CrontabResumeSuspendStrategy()
            self._CrontabResumeSuspendStrategy._deserialize(params.get("CrontabResumeSuspendStrategy"))
        self._EngineExecType = params.get("EngineExecType")
        self._MaxConcurrency = params.get("MaxConcurrency")
        self._TolerableQueueTime = params.get("TolerableQueueTime")
        self._AutoSuspendTime = params.get("AutoSuspendTime")
        self._ResourceType = params.get("ResourceType")
        if params.get("DataEngineConfigPairs") is not None:
            self._DataEngineConfigPairs = []
            for item in params.get("DataEngineConfigPairs"):
                obj = DataEngineConfigPair()
                obj._deserialize(item)
                self._DataEngineConfigPairs.append(obj)
        self._ImageVersionName = params.get("ImageVersionName")
        self._MainClusterName = params.get("MainClusterName")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticLimit = params.get("ElasticLimit")
        if params.get("SessionResourceTemplate") is not None:
            self._SessionResourceTemplate = SessionResourceTemplate()
            self._SessionResourceTemplate._deserialize(params.get("SessionResourceTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataEngineResponse(AbstractModel):
    """CreateDataEngine response structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineId: The ID of the virtual engine.
        :type DataEngineId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataEngineId = None
        self._RequestId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        self._RequestId = params.get("RequestId")


class CreateInternalTableRequest(AbstractModel):
    """CreateInternalTable request structure.

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: The basic table information.
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: The table fields.
        :type Columns: list of TColumn
        :param _Partitions: The table partitions.
        :type Partitions: list of TPartition
        :param _Properties: The table properties.
        :type Properties: list of Property
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Properties = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInternalTableResponse(AbstractModel):
    """CreateInternalTable response structure.

    """

    def __init__(self):
        r"""
        :param _Execution: The SQL statements for creating the managed internal table.
        :type Execution: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Execution = params.get("Execution")
        self._RequestId = params.get("RequestId")


class CreateResultDownloadRequest(AbstractModel):
    """CreateResultDownload request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The result query task ID.
        :type TaskId: str
        :param _Format: The result format.
        :type Format: str
        :param _Force: Whether to re-generate a file to download. This parameter applies only when the last task is `timeout` or `error`.
        :type Force: bool
        """
        self._TaskId = None
        self._Format = None
        self._Force = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Format = params.get("Format")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResultDownloadResponse(AbstractModel):
    """CreateResultDownload response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadId: The download task ID.
        :type DownloadId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadId = None
        self._RequestId = None

    @property
    def DownloadId(self):
        return self._DownloadId

    @DownloadId.setter
    def DownloadId(self, DownloadId):
        self._DownloadId = DownloadId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadId = params.get("DownloadId")
        self._RequestId = params.get("RequestId")


class CreateSparkAppRequest(AbstractModel):
    """CreateSparkApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppName: Spark application name
        :type AppName: str
        :param _AppType: 1: Spark JAR application; 2: Spark streaming application
        :type AppType: int
        :param _DataEngine: The data engine executing the Spark job
        :type DataEngine: str
        :param _AppFile: Execution entry of the Spark application
        :type AppFile: str
        :param _RoleArn: Execution role ID of the Spark job
        :type RoleArn: int
        :param _AppDriverSize: Driver resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppDriverSize: str
        :param _AppExecutorSize: Executor resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppExecutorSize: str
        :param _AppExecutorNums: Number of Spark job executors
        :type AppExecutorNums: int
        :param _Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param _IsLocal: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param _MainClass: Main class of the Spark JAR job during execution
        :type MainClass: str
        :param _AppConf: Spark configurations separated by line break
        :type AppConf: str
        :param _IsLocalJars: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocalJars: str
        :param _AppJars: Dependency JAR packages of the Spark JAR job separated by comma
        :type AppJars: str
        :param _IsLocalFiles: Whether it is upload locally. Valid values: `cos`, `lakefs`.
        :type IsLocalFiles: str
        :param _AppFiles: Dependency resources of the Spark job separated by comma
        :type AppFiles: str
        :param _CmdArgs: Command line parameters of the Spark job
        :type CmdArgs: str
        :param _MaxRetries: This parameter takes effect only for Spark flow tasks.
        :type MaxRetries: int
        :param _DataSource: Data source name
        :type DataSource: str
        :param _IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
        :type AppPythonFiles: str
        :param _IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalArchives: str
        :param _AppArchives: Archives: Dependency resources
        :type AppArchives: str
        :param _SparkImage: The Spark image version.
        :type SparkImage: str
        :param _SparkImageVersion: The Spark image version name.
        :type SparkImageVersion: str
        :param _AppExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `AppExecutorNums`.
        :type AppExecutorMaxNumbers: int
        :param _SessionId: The ID of the associated Data Lake Compute query script.
        :type SessionId: str
        :param _IsInherit: Whether to inherit the task resource configuration from the cluster template. Valid values: `0` (default): No; `1`: Yes.
        :type IsInherit: int
        """
        self._AppName = None
        self._AppType = None
        self._DataEngine = None
        self._AppFile = None
        self._RoleArn = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._Eni = None
        self._IsLocal = None
        self._MainClass = None
        self._AppConf = None
        self._IsLocalJars = None
        self._AppJars = None
        self._IsLocalFiles = None
        self._AppFiles = None
        self._CmdArgs = None
        self._MaxRetries = None
        self._DataSource = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._IsLocalArchives = None
        self._AppArchives = None
        self._SparkImage = None
        self._SparkImageVersion = None
        self._AppExecutorMaxNumbers = None
        self._SessionId = None
        self._IsInherit = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppFile(self):
        return self._AppFile

    @AppFile.setter
    def AppFile(self, AppFile):
        self._AppFile = AppFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def AppConf(self):
        return self._AppConf

    @AppConf.setter
    def AppConf(self, AppConf):
        self._AppConf = AppConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def AppJars(self):
        return self._AppJars

    @AppJars.setter
    def AppJars(self, AppJars):
        self._AppJars = AppJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def AppFiles(self):
        return self._AppFiles

    @AppFiles.setter
    def AppFiles(self, AppFiles):
        self._AppFiles = AppFiles

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def MaxRetries(self):
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def AppArchives(self):
        return self._AppArchives

    @AppArchives.setter
    def AppArchives(self, AppArchives):
        self._AppArchives = AppArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AppType = params.get("AppType")
        self._DataEngine = params.get("DataEngine")
        self._AppFile = params.get("AppFile")
        self._RoleArn = params.get("RoleArn")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._MainClass = params.get("MainClass")
        self._AppConf = params.get("AppConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._AppJars = params.get("AppJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._AppFiles = params.get("AppFiles")
        self._CmdArgs = params.get("CmdArgs")
        self._MaxRetries = params.get("MaxRetries")
        self._DataSource = params.get("DataSource")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._AppArchives = params.get("AppArchives")
        self._SparkImage = params.get("SparkImage")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._SessionId = params.get("SessionId")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppResponse(AbstractModel):
    """CreateSparkApp response structure.

    """

    def __init__(self):
        r"""
        :param _SparkAppId: The unique ID of the application.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkAppId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SparkAppId = None
        self._RequestId = None

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SparkAppId = params.get("SparkAppId")
        self._RequestId = params.get("RequestId")


class CreateSparkAppTaskRequest(AbstractModel):
    """CreateSparkAppTask request structure.

    """

    def __init__(self):
        r"""
        :param _JobName: Spark job name
        :type JobName: str
        :param _CmdArgs: Command line parameters of the Spark job separated by space. They are generally used for periodic calls.
        :type CmdArgs: str
        """
        self._JobName = None
        self._CmdArgs = None

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        self._CmdArgs = params.get("CmdArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkAppTaskResponse(AbstractModel):
    """CreateSparkAppTask response structure.

    """

    def __init__(self):
        r"""
        :param _BatchId: Batch ID
        :type BatchId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BatchId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSparkSessionBatchSQLRequest(AbstractModel):
    """CreateSparkSessionBatchSQL request structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineName: The name of the engine for executing the Spark job.
        :type DataEngineName: str
        :param _ExecuteSQL: The SQL statement to execute.
        :type ExecuteSQL: str
        :param _DriverSize: The driver size. Valid values: `small` (default, 1 CU), `medium` (2 CUs), `large` (4 CUs), and `xlarge` (8 CUs).
        :type DriverSize: str
        :param _ExecutorSize: The executor size. Valid values: `small` (default, 1 CU), `medium` (2 CUs), `large` (4 CUs), and `xlarge` (8 CUs).
        :type ExecutorSize: str
        :param _ExecutorNumbers: The executor count, which defaults to 1.
        :type ExecutorNumbers: int
        :param _ExecutorMaxNumbers: The maximum executor count, which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the value of this parameter is the same as that of `ExecutorNumbers`.
        :type ExecutorMaxNumbers: int
        :param _TimeoutInSecond: The session timeout period in seconds. Default value: 3600
        :type TimeoutInSecond: int
        :param _SessionId: The unique ID of a session. If this parameter is specified, the task will be run using the specified session.
        :type SessionId: str
        :param _SessionName: The name of the session to create.
        :type SessionName: str
        :param _Arguments: Session configurations. `dlc.eni`, `dlc.role.arn`, `dlc.sql.set.config`, and user-defined configurations are supported.
        :type Arguments: list of KVPair
        """
        self._DataEngineName = None
        self._ExecuteSQL = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNumbers = None
        self._ExecutorMaxNumbers = None
        self._TimeoutInSecond = None
        self._SessionId = None
        self._SessionName = None
        self._Arguments = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def ExecuteSQL(self):
        return self._ExecuteSQL

    @ExecuteSQL.setter
    def ExecuteSQL(self, ExecuteSQL):
        self._ExecuteSQL = ExecuteSQL

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNumbers(self):
        return self._ExecutorNumbers

    @ExecutorNumbers.setter
    def ExecutorNumbers(self, ExecutorNumbers):
        self._ExecutorNumbers = ExecutorNumbers

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers

    @property
    def TimeoutInSecond(self):
        return self._TimeoutInSecond

    @TimeoutInSecond.setter
    def TimeoutInSecond(self, TimeoutInSecond):
        self._TimeoutInSecond = TimeoutInSecond

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SessionName(self):
        return self._SessionName

    @SessionName.setter
    def SessionName(self, SessionName):
        self._SessionName = SessionName

    @property
    def Arguments(self):
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._ExecuteSQL = params.get("ExecuteSQL")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNumbers = params.get("ExecutorNumbers")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        self._TimeoutInSecond = params.get("TimeoutInSecond")
        self._SessionId = params.get("SessionId")
        self._SessionName = params.get("SessionName")
        if params.get("Arguments") is not None:
            self._Arguments = []
            for item in params.get("Arguments"):
                obj = KVPair()
                obj._deserialize(item)
                self._Arguments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSparkSessionBatchSQLResponse(AbstractModel):
    """CreateSparkSessionBatchSQL response structure.

    """

    def __init__(self):
        r"""
        :param _BatchId: The unique identifier of a batch task.
        :type BatchId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask request structure.

    """

    def __init__(self):
        r"""
        :param _Task: Computing task. This parameter contains the task type and related configuration information.
        :type Task: :class:`tencentcloud.dlc.v20210125.models.Task`
        :param _DatabaseName: Database name. If there is a database name in the SQL statement, the database in the SQL statement will be used first; otherwise, the database specified by this parameter will be used (note: when submitting the database creation SQL statement, passed in an empty string for this field).
        :type DatabaseName: str
        :param _DatasourceConnectionName: Name of the default data source
        :type DatasourceConnectionName: str
        :param _DataEngineName: Data engine name. If this parameter is not specified, the task will be submitted to the default engine.
        :type DataEngineName: str
        """
        self._Task = None
        self._DatabaseName = None
        self._DatasourceConnectionName = None
        self._DataEngineName = None

    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._DatabaseName = params.get("DatabaseName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateTasksRequest(AbstractModel):
    """CreateTasks request structure.

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Database name. If there is a database name in the SQL statement, the database in the SQL statement will be used first; otherwise, the database specified by this parameter will be used (note: when submitting the database creation SQL statement, passed in an empty string for this field).
        :type DatabaseName: str
        :param _Tasks: SQL task information
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TasksInfo`
        :param _DatasourceConnectionName: Data source name. Default value: DataLakeCatalog.
        :type DatasourceConnectionName: str
        :param _DataEngineName: Compute engine name. If this parameter is not specified, the task will be submitted to the default engine.
        :type DataEngineName: str
        """
        self._DatabaseName = None
        self._Tasks = None
        self._DatasourceConnectionName = None
        self._DataEngineName = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        if params.get("Tasks") is not None:
            self._Tasks = TasksInfo()
            self._Tasks._deserialize(params.get("Tasks"))
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DataEngineName = params.get("DataEngineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTasksResponse(AbstractModel):
    """CreateTasks response structure.

    """

    def __init__(self):
        r"""
        :param _BatchId: ID of the current batch of submitted tasks
        :type BatchId: str
        :param _TaskIdSet: Collection of task IDs arranged in order of execution
        :type TaskIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BatchId = None
        self._TaskIdSet = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def TaskIdSet(self):
        return self._TaskIdSet

    @TaskIdSet.setter
    def TaskIdSet(self, TaskIdSet):
        self._TaskIdSet = TaskIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._TaskIdSet = params.get("TaskIdSet")
        self._RequestId = params.get("RequestId")


class CrontabResumeSuspendStrategy(AbstractModel):
    """Scheduled start and suspension information

    """

    def __init__(self):
        r"""
        :param _ResumeTime: The scheduled start time, such as 8:00 AM every Monday.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResumeTime: str
        :param _SuspendTime: The scheduled suspension time, such as 8:00 PM every Monday.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuspendTime: str
        :param _SuspendStrategy: The suspension setting. Valid values: `0` (suspension after task end, default) and `1` (force suspension).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuspendStrategy: int
        """
        self._ResumeTime = None
        self._SuspendTime = None
        self._SuspendStrategy = None

    @property
    def ResumeTime(self):
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime

    @property
    def SuspendTime(self):
        return self._SuspendTime

    @SuspendTime.setter
    def SuspendTime(self, SuspendTime):
        self._SuspendTime = SuspendTime

    @property
    def SuspendStrategy(self):
        return self._SuspendStrategy

    @SuspendStrategy.setter
    def SuspendStrategy(self, SuspendStrategy):
        self._SuspendStrategy = SuspendStrategy


    def _deserialize(self, params):
        self._ResumeTime = params.get("ResumeTime")
        self._SuspendTime = params.get("SuspendTime")
        self._SuspendStrategy = params.get("SuspendStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEngineConfigPair(AbstractModel):
    """Engine configurations

    """


class DataGovernPolicy(AbstractModel):
    """The data governance rules.

    """

    def __init__(self):
        r"""
        :param _RuleType: Governance rule type. Valid values: `Customize` (custom) and `Intelligence` (intelligent).
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _GovernEngine: The governance engine.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GovernEngine: str
        """
        self._RuleType = None
        self._GovernEngine = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def GovernEngine(self):
        return self._GovernEngine

    @GovernEngine.setter
    def GovernEngine(self, GovernEngine):
        self._GovernEngine = GovernEngine


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._GovernEngine = params.get("GovernEngine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSparkAppRequest(AbstractModel):
    """DeleteSparkApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppName: Spark application name
        :type AppName: str
        """
        self._AppName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSparkAppResponse(AbstractModel):
    """DeleteSparkApp response structure.

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


class DescribeEngineUsageInfoRequest(AbstractModel):
    """DescribeEngineUsageInfo request structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineId: The house ID.
        :type DataEngineId: str
        """
        self._DataEngineId = None

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId


    def _deserialize(self, params):
        self._DataEngineId = params.get("DataEngineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEngineUsageInfoResponse(AbstractModel):
    """DescribeEngineUsageInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total cluster spec.
        :type Total: int
        :param _Used: The used cluster spec.
        :type Used: int
        :param _Available: The available cluster spec.
        :type Available: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._Available = None
        self._RequestId = None

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

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Available = params.get("Available")
        self._RequestId = params.get("RequestId")


class DescribeForbiddenTableProRequest(AbstractModel):
    """DescribeForbiddenTablePro request structure.

    """


class DescribeForbiddenTableProResponse(AbstractModel):
    """DescribeForbiddenTablePro response structure.

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


class DescribeLakeFsDirSummaryRequest(AbstractModel):
    """DescribeLakeFsDirSummary request structure.

    """


class DescribeLakeFsDirSummaryResponse(AbstractModel):
    """DescribeLakeFsDirSummary response structure.

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


class DescribeLakeFsInfoRequest(AbstractModel):
    """DescribeLakeFsInfo request structure.

    """


class DescribeLakeFsInfoResponse(AbstractModel):
    """DescribeLakeFsInfo response structure.

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


class DescribeResultDownloadRequest(AbstractModel):
    """DescribeResultDownload request structure.

    """

    def __init__(self):
        r"""
        :param _DownloadId: The query task ID.
        :type DownloadId: str
        """
        self._DownloadId = None

    @property
    def DownloadId(self):
        return self._DownloadId

    @DownloadId.setter
    def DownloadId(self, DownloadId):
        self._DownloadId = DownloadId


    def _deserialize(self, params):
        self._DownloadId = params.get("DownloadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResultDownloadResponse(AbstractModel):
    """DescribeResultDownload response structure.

    """

    def __init__(self):
        r"""
        :param _Path: The file save path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _Status: The task status. Valid values: `init`, `queue`, `format`, `compress`, `success`, `timeout`, and `error`.
        :type Status: str
        :param _Reason: The task exception cause.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param _SecretId: The temporary secret ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretId: str
        :param _SecretKey: The temporary secret key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _Token: The temporary token.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Token: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Path = None
        self._Status = None
        self._Reason = None
        self._SecretId = None
        self._SecretKey = None
        self._Token = None
        self._RequestId = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppJobRequest(AbstractModel):
    """DescribeSparkAppJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Spark job ID. If it co-exists with `JobName`, `JobName` will become invalid.
        :type JobId: str
        :param _JobName: Spark job name
        :type JobName: str
        """
        self._JobId = None
        self._JobName = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppJobResponse(AbstractModel):
    """DescribeSparkAppJob response structure.

    """

    def __init__(self):
        r"""
        :param _Job: Spark job details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Job: :class:`tencentcloud.dlc.v20210125.models.SparkJobInfo`
        :param _IsExists: Whether the queried Spark job exists
        :type IsExists: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Job = None
        self._IsExists = None
        self._RequestId = None

    @property
    def Job(self):
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def IsExists(self):
        return self._IsExists

    @IsExists.setter
    def IsExists(self, IsExists):
        self._IsExists = IsExists

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = SparkJobInfo()
            self._Job._deserialize(params.get("Job"))
        self._IsExists = params.get("IsExists")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppJobsRequest(AbstractModel):
    """DescribeSparkAppJobs request structure.

    """

    def __init__(self):
        r"""
        :param _SortBy: The returned results are sorted by this field.
        :type SortBy: str
        :param _Sorting: Descending or ascending order, such as `desc`.
        :type Sorting: str
        :param _Filters: Filter by this parameter, which can be `spark-job-name`.
        :type Filters: list of Filter
        :param _StartTime: The update start time in the format of yyyy-mm-dd HH:MM:SS.
        :type StartTime: str
        :param _EndTime: The update end time in the format of yyyy-mm-dd HH:MM:SS.
        :type EndTime: str
        :param _Offset: The query list offset, which defaults to 0.
        :type Offset: int
        :param _Limit: The maximum number of queries allowed in the list, which defaults to 100.
        :type Limit: int
        """
        self._SortBy = None
        self._Sorting = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        


class DescribeSparkAppJobsResponse(AbstractModel):
    """DescribeSparkAppJobs response structure.

    """

    def __init__(self):
        r"""
        :param _SparkAppJobs: Detailed list of Spark jobs
        :type SparkAppJobs: list of SparkJobInfo
        :param _TotalCount: Total number of Spark jobs
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SparkAppJobs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SparkAppJobs(self):
        return self._SparkAppJobs

    @SparkAppJobs.setter
    def SparkAppJobs(self, SparkAppJobs):
        self._SparkAppJobs = SparkAppJobs

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
        if params.get("SparkAppJobs") is not None:
            self._SparkAppJobs = []
            for item in params.get("SparkAppJobs"):
                obj = SparkJobInfo()
                obj._deserialize(item)
                self._SparkAppJobs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSparkAppTasksRequest(AbstractModel):
    """DescribeSparkAppTasks request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Spark job ID
        :type JobId: str
        :param _Offset: Paginated query offset
        :type Offset: int
        :param _Limit: Paginated query limit
        :type Limit: int
        :param _TaskId: Execution instance ID
        :type TaskId: str
        :param _StartTime: Update start time
        :type StartTime: str
        :param _EndTime: Update end time
        :type EndTime: str
        :param _Filters: Filter by this parameter, which can be `task-state`.
        :type Filters: list of Filter
        """
        self._JobId = None
        self._Offset = None
        self._Limit = None
        self._TaskId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkAppTasksResponse(AbstractModel):
    """DescribeSparkAppTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: Task result (this field has been disused)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: :class:`tencentcloud.dlc.v20210125.models.TaskResponseInfo`
        :param _TotalCount: Total number of tasks
        :type TotalCount: int
        :param _SparkAppTasks: List of task results
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkAppTasks: list of TaskResponseInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._TotalCount = None
        self._SparkAppTasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SparkAppTasks(self):
        return self._SparkAppTasks

    @SparkAppTasks.setter
    def SparkAppTasks(self, SparkAppTasks):
        self._SparkAppTasks = SparkAppTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = TaskResponseInfo()
            self._Tasks._deserialize(params.get("Tasks"))
        self._TotalCount = params.get("TotalCount")
        if params.get("SparkAppTasks") is not None:
            self._SparkAppTasks = []
            for item in params.get("SparkAppTasks"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self._SparkAppTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSparkSessionBatchSqlLogRequest(AbstractModel):
    """DescribeSparkSessionBatchSqlLog request structure.

    """

    def __init__(self):
        r"""
        :param _BatchId: The unique ID of a Spark SQL job.
        :type BatchId: str
        """
        self._BatchId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSparkSessionBatchSqlLogResponse(AbstractModel):
    """DescribeSparkSessionBatchSqlLog response structure.

    """

    def __init__(self):
        r"""
        :param _State: The status. Valid values: `0` (initializing), `1` (successful), `2` (failed), `3` (canceled), and `4` (exception).
        :type State: int
        :param _LogSet: The log information list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSet: list of SparkSessionBatchLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._State = None
        self._LogSet = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        if params.get("LogSet") is not None:
            self._LogSet = []
            for item in params.get("LogSet"):
                obj = SparkSessionBatchLog()
                obj._deserialize(item)
                self._LogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID
        :type TaskId: str
        :param _NextToken: The pagination information returned by the last response. This parameter can be omitted for the first response, where the data will be returned from the beginning. The data with a volume set by the `MaxResults` field is returned each time.
        :type NextToken: str
        :param _MaxResults: Maximum number of returned rows. Value range: 0–1,000. Default value: 1,000.
        :type MaxResults: int
        """
        self._TaskId = None
        self._NextToken = None
        self._MaxResults = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult response structure.

    """

    def __init__(self):
        r"""
        :param _TaskInfo: The queried task information. If the returned value is empty, the task with the entered task ID does not exist. The task result will be returned only if the task status is `2` (succeeded).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskInfo: :class:`tencentcloud.dlc.v20210125.models.TaskResultInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self._TaskInfo = TaskResultInfo()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of returned results. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter. The following filters are supported, and the `Name` input parameter must be one of them. Up to 50 `task-id` values can be filtered, while up to 5 other parameters can be filtered in total.
task-id - String - (filter by task ID). `task-id` format: e386471f-139a-4e59-877f-50ece8135b99.
task-state - String - (filter exactly by task status). Valid values: `0` (initial), `1` (running), `2` (succeeded), `-1` (failed).
task-sql-keyword - String - (filter fuzzily by SQL statement keyword, such as `DROP TABLE`).
task-operator- string (filter by sub-UIN)
task-kind - string (filter by task type)
        :type Filters: list of Filter
        :param _SortBy: Sorting field. Valid values: `create-time` (default value), `update-time`.
        :type SortBy: str
        :param _Sorting: Sorting order. Valid values: `asc` (ascending order), `desc` (descending order). Default value: `asc`.
        :type Sorting: str
        :param _StartTime: Start time in the format of `yyyy-mm-dd HH:MM:SS`, which is the current time seven days ago by default.
        :type StartTime: str
        :param _EndTime: End time in the format of `yyyy-mm-dd HH:MM:SS`, which is the current time by default. The time span is (0, 30] days. Data in the last 45 days can be queried.
        :type EndTime: str
        :param _DataEngineName: Filter by compute resource name
        :type DataEngineName: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._SortBy = None
        self._Sorting = None
        self._StartTime = None
        self._EndTime = None
        self._DataEngineName = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Sorting(self):
        return self._Sorting

    @Sorting.setter
    def Sorting(self, Sorting):
        self._Sorting = Sorting

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
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortBy = params.get("SortBy")
        self._Sorting = params.get("Sorting")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DataEngineName = params.get("DataEngineName")
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
        :param _TaskList: List of task objects.
        :type TaskList: list of TaskResponseInfo
        :param _TotalCount: Total number of instances
        :type TotalCount: int
        :param _TasksOverview: The task overview.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TasksOverview: :class:`tencentcloud.dlc.v20210125.models.TasksOverview`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskList = None
        self._TotalCount = None
        self._TasksOverview = None
        self._RequestId = None

    @property
    def TaskList(self):
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TasksOverview(self):
        return self._TasksOverview

    @TasksOverview.setter
    def TasksOverview(self, TasksOverview):
        self._TasksOverview = TasksOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = TaskResponseInfo()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("TasksOverview") is not None:
            self._TasksOverview = TasksOverview()
            self._TasksOverview._deserialize(params.get("TasksOverview"))
        self._RequestId = params.get("RequestId")


class Execution(AbstractModel):
    """SQL statement objects

    """

    def __init__(self):
        r"""
        :param _SQL: The automatically generated SQL statements.
        :type SQL: str
        """
        self._SQL = None

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL


    def _deserialize(self, params):
        self._SQL = params.get("SQL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query list filter parameter

    """

    def __init__(self):
        r"""
        :param _Name: Attribute name. If more than one filter exists, the logical relationship between these filters is `OR`.
        :type Name: str
        :param _Values: Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCreateMangedTableSqlRequest(AbstractModel):
    """GenerateCreateMangedTableSql request structure.

    """

    def __init__(self):
        r"""
        :param _TableBaseInfo: The basic table information.
        :type TableBaseInfo: :class:`tencentcloud.dlc.v20210125.models.TableBaseInfo`
        :param _Columns: The table fields.
        :type Columns: list of TColumn
        :param _Partitions: The table partitions.
        :type Partitions: list of TPartition
        :param _Properties: The table properties.
        :type Properties: list of Property
        :param _UpsertKeys: The Upsert key for a v2 table (in Upsert mode).
        :type UpsertKeys: list of str
        """
        self._TableBaseInfo = None
        self._Columns = None
        self._Partitions = None
        self._Properties = None
        self._UpsertKeys = None

    @property
    def TableBaseInfo(self):
        return self._TableBaseInfo

    @TableBaseInfo.setter
    def TableBaseInfo(self, TableBaseInfo):
        self._TableBaseInfo = TableBaseInfo

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def UpsertKeys(self):
        return self._UpsertKeys

    @UpsertKeys.setter
    def UpsertKeys(self, UpsertKeys):
        self._UpsertKeys = UpsertKeys


    def _deserialize(self, params):
        if params.get("TableBaseInfo") is not None:
            self._TableBaseInfo = TableBaseInfo()
            self._TableBaseInfo._deserialize(params.get("TableBaseInfo"))
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = TPartition()
                obj._deserialize(item)
                self._Partitions.append(obj)
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._UpsertKeys = params.get("UpsertKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCreateMangedTableSqlResponse(AbstractModel):
    """GenerateCreateMangedTableSql response structure.

    """

    def __init__(self):
        r"""
        :param _Execution: The SQL statements for creating the managed internal table.
        :type Execution: :class:`tencentcloud.dlc.v20210125.models.Execution`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Execution = None
        self._RequestId = None

    @property
    def Execution(self):
        return self._Execution

    @Execution.setter
    def Execution(self, Execution):
        self._Execution = Execution

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Execution") is not None:
            self._Execution = Execution()
            self._Execution._deserialize(params.get("Execution"))
        self._RequestId = params.get("RequestId")


class KVPair(AbstractModel):
    """Configuration format

    """

    def __init__(self):
        r"""
        :param _Key: Configured key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Configured value
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class ModifyGovernEventRuleRequest(AbstractModel):
    """ModifyGovernEventRule request structure.

    """


class ModifyGovernEventRuleResponse(AbstractModel):
    """ModifyGovernEventRule response structure.

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


class ModifySparkAppBatchRequest(AbstractModel):
    """ModifySparkAppBatch request structure.

    """

    def __init__(self):
        r"""
        :param _SparkAppId: The list of the IDs of the Spark job tasks to be modified in batches.
        :type SparkAppId: list of str
        :param _DataEngine: The engine ID.
        :type DataEngine: str
        :param _AppDriverSize: The driver size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
        :type AppDriverSize: str
        :param _AppExecutorSize: The executor size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
        :type AppExecutorSize: str
        :param _AppExecutorNums: The executor count. The minimum value is 1 and the maximum value is less than the cluster specification.
        :type AppExecutorNums: int
        :param _AppExecutorMaxNumbers: The maximum executor count (in dynamic configuration scenarios). The minimum value is 1 and the maximum value is less than the cluster specification. If you set `ExecutorMaxNumbers` to a value smaller than that of `ExecutorNums`, the value of `ExecutorMaxNumbers` is automatically changed to that of `ExecutorNums`.
        :type AppExecutorMaxNumbers: int
        :param _IsInherit: Whether to inherit the task resource configuration from the cluster template. Valid values: `0` (default): No; `1`: Yes.
        :type IsInherit: int
        """
        self._SparkAppId = None
        self._DataEngine = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._AppExecutorMaxNumbers = None
        self._IsInherit = None

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._SparkAppId = params.get("SparkAppId")
        self._DataEngine = params.get("DataEngine")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppBatchResponse(AbstractModel):
    """ModifySparkAppBatch response structure.

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


class ModifySparkAppRequest(AbstractModel):
    """ModifySparkApp request structure.

    """

    def __init__(self):
        r"""
        :param _AppName: Spark application name
        :type AppName: str
        :param _AppType: 1: Spark JAR application; 2: Spark streaming application
        :type AppType: int
        :param _DataEngine: The data engine executing the Spark job
        :type DataEngine: str
        :param _AppFile: Execution entry of the Spark application
        :type AppFile: str
        :param _RoleArn: Execution role ID of the Spark job
        :type RoleArn: int
        :param _AppDriverSize: Driver resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppDriverSize: str
        :param _AppExecutorSize: Executor resource specification of the Spark job. Valid values: `small`, `medium`, `large`, `xlarge`.
        :type AppExecutorSize: str
        :param _AppExecutorNums: Number of Spark job executors
        :type AppExecutorNums: int
        :param _SparkAppId: Spark application ID
        :type SparkAppId: str
        :param _Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param _IsLocal: Whether it is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param _MainClass: Main class of the Spark JAR job during execution
        :type MainClass: str
        :param _AppConf: Spark configurations separated by line break
        :type AppConf: str
        :param _IsLocalJars: JAR resource dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalJars: str
        :param _AppJars: Dependency JAR packages of the Spark JAR job separated by comma
        :type AppJars: str
        :param _IsLocalFiles: File resource dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalFiles: str
        :param _AppFiles: Dependency resources of the Spark job separated by comma
        :type AppFiles: str
        :param _IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
        :type AppPythonFiles: str
        :param _CmdArgs: Command line parameters of the Spark job
        :type CmdArgs: str
        :param _MaxRetries: This parameter takes effect only for Spark flow tasks.
        :type MaxRetries: int
        :param _DataSource: Data source name
        :type DataSource: str
        :param _IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
        :type IsLocalArchives: str
        :param _AppArchives: Archives: Dependency resources
        :type AppArchives: str
        :param _SparkImage: The Spark image version.
        :type SparkImage: str
        :param _SparkImageVersion: The Spark image version name.
        :type SparkImageVersion: str
        :param _AppExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `AppExecutorNums`.
        :type AppExecutorMaxNumbers: int
        :param _SessionId: The associated Data Lake Compute query script.
        :type SessionId: str
        :param _IsInherit: Whether to inherit the task resource configuration from the cluster configuration template. Valid values: `0` (default): No; `1`: Yes.
        :type IsInherit: int
        """
        self._AppName = None
        self._AppType = None
        self._DataEngine = None
        self._AppFile = None
        self._RoleArn = None
        self._AppDriverSize = None
        self._AppExecutorSize = None
        self._AppExecutorNums = None
        self._SparkAppId = None
        self._Eni = None
        self._IsLocal = None
        self._MainClass = None
        self._AppConf = None
        self._IsLocalJars = None
        self._AppJars = None
        self._IsLocalFiles = None
        self._AppFiles = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._CmdArgs = None
        self._MaxRetries = None
        self._DataSource = None
        self._IsLocalArchives = None
        self._AppArchives = None
        self._SparkImage = None
        self._SparkImageVersion = None
        self._AppExecutorMaxNumbers = None
        self._SessionId = None
        self._IsInherit = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def AppFile(self):
        return self._AppFile

    @AppFile.setter
    def AppFile(self, AppFile):
        self._AppFile = AppFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def AppDriverSize(self):
        return self._AppDriverSize

    @AppDriverSize.setter
    def AppDriverSize(self, AppDriverSize):
        self._AppDriverSize = AppDriverSize

    @property
    def AppExecutorSize(self):
        return self._AppExecutorSize

    @AppExecutorSize.setter
    def AppExecutorSize(self, AppExecutorSize):
        self._AppExecutorSize = AppExecutorSize

    @property
    def AppExecutorNums(self):
        return self._AppExecutorNums

    @AppExecutorNums.setter
    def AppExecutorNums(self, AppExecutorNums):
        self._AppExecutorNums = AppExecutorNums

    @property
    def SparkAppId(self):
        return self._SparkAppId

    @SparkAppId.setter
    def SparkAppId(self, SparkAppId):
        self._SparkAppId = SparkAppId

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def AppConf(self):
        return self._AppConf

    @AppConf.setter
    def AppConf(self, AppConf):
        self._AppConf = AppConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def AppJars(self):
        return self._AppJars

    @AppJars.setter
    def AppJars(self, AppJars):
        self._AppJars = AppJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def AppFiles(self):
        return self._AppFiles

    @AppFiles.setter
    def AppFiles(self, AppFiles):
        self._AppFiles = AppFiles

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def MaxRetries(self):
        return self._MaxRetries

    @MaxRetries.setter
    def MaxRetries(self, MaxRetries):
        self._MaxRetries = MaxRetries

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def AppArchives(self):
        return self._AppArchives

    @AppArchives.setter
    def AppArchives(self, AppArchives):
        self._AppArchives = AppArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def AppExecutorMaxNumbers(self):
        return self._AppExecutorMaxNumbers

    @AppExecutorMaxNumbers.setter
    def AppExecutorMaxNumbers(self, AppExecutorMaxNumbers):
        self._AppExecutorMaxNumbers = AppExecutorMaxNumbers

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AppType = params.get("AppType")
        self._DataEngine = params.get("DataEngine")
        self._AppFile = params.get("AppFile")
        self._RoleArn = params.get("RoleArn")
        self._AppDriverSize = params.get("AppDriverSize")
        self._AppExecutorSize = params.get("AppExecutorSize")
        self._AppExecutorNums = params.get("AppExecutorNums")
        self._SparkAppId = params.get("SparkAppId")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._MainClass = params.get("MainClass")
        self._AppConf = params.get("AppConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._AppJars = params.get("AppJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._AppFiles = params.get("AppFiles")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._CmdArgs = params.get("CmdArgs")
        self._MaxRetries = params.get("MaxRetries")
        self._DataSource = params.get("DataSource")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._AppArchives = params.get("AppArchives")
        self._SparkImage = params.get("SparkImage")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._AppExecutorMaxNumbers = params.get("AppExecutorMaxNumbers")
        self._SessionId = params.get("SessionId")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySparkAppResponse(AbstractModel):
    """ModifySparkApp response structure.

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


class Policy(AbstractModel):
    """Permission objects

    """

    def __init__(self):
        r"""
        :param _Database: The name of the target database. `*` represents all databases in the current catalog. To grant admin permissions, it must be `*`; to grant data connection permissions, it must be null; to grant other permissions, it can be any database.
        :type Database: str
        :param _Catalog: The name of the target data source. To grant admin permission, it must be `*` (all resources at this level); to grant data source and database permissions, it must be `COSDataCatalog` or `*`; to grant table permissions, it can be a custom data source; if it is left empty, `DataLakeCatalog` is used. Note: To grant permissions on a custom data source, the permissions that can be managed in the Data Lake Compute console are subsets of the account permissions granted when you connect the data source to the console.
        :type Catalog: str
        :param _Table: The name of the target table. `*` represents all tables in the current database. To grant admin permissions, it must be `*`; to grant data connection and database permissions, it must be null; to grant other permissions, it can be any table.
        :type Table: str
        :param _Operation: The target permissions, which vary by permission level. Admin: `ALL` (default); data connection: `CREATE`; database: `ALL`, `CREATE`, `ALTER`, and `DROP`; table: `ALL`, `SELECT`, `INSERT`, `ALTER`, `DELETE`, `DROP`, and `UPDATE`. Note: For table permissions, if a data source other than `COSDataCatalog` is specified, only the `SELECT` permission can be granted here.
        :type Operation: str
        :param _PolicyType: The permission type. Valid values: `ADMIN`, `DATASOURCE`, `DATABASE`, `TABLE`, `VIEW`, `FUNCTION`, `COLUMN`, and `ENGINE`. Note: If it is left empty, `ADMIN` is used.
        :type PolicyType: str
        :param _Function: The name of the target function. `*` represents all functions in the current catalog. To grant admin permissions, it must be `*`; to grant data connection permissions, it must be null; to grant other permissions, it can be any function.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Function: str
        :param _View: The name of the target view. `*` represents all views in the current database. To grant admin permissions, it must be `*`; to grant data connection and database permissions, it must be null; to grant other permissions, it can be any view.
Note: This field may return null, indicating that no valid values can be obtained.
        :type View: str
        :param _Column: The name of the target column. `*` represents all columns. To grant admin permissions, it must be `*`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Column: str
        :param _DataEngine: The name of the target data engine. `*` represents all engines. To grant admin permissions, it must be `*`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngine: str
        :param _ReAuth: Whether the grantee is allowed to further grant the permissions. Valid values: `false` (default) and `true` (the grantee can grant permissions gained here to other sub-users).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReAuth: bool
        :param _Source: The permission source, which is not required when input parameters are passed in. Valid values: `USER` (from the user) and `WORKGROUP` (from one or more associated work groups).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Source: str
        :param _Mode: The grant mode, which is not required as an input parameter. Valid values: `COMMON` and `SENIOR`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        :param _Operator: The operator, which is not required as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operator: str
        :param _CreateTime: The permission policy creation time, which is not required as an input parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _SourceId: The ID of the work group, which applies only when the value of the `Source` field is `WORKGROUP`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceId: int
        :param _SourceName: The name of the work group, which applies only when the value of the `Source` field is `WORKGROUP`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceName: str
        :param _Id: The policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._Database = None
        self._Catalog = None
        self._Table = None
        self._Operation = None
        self._PolicyType = None
        self._Function = None
        self._View = None
        self._Column = None
        self._DataEngine = None
        self._ReAuth = None
        self._Source = None
        self._Mode = None
        self._Operator = None
        self._CreateTime = None
        self._SourceId = None
        self._SourceName = None
        self._Id = None

    @property
    def Database(self):
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Table(self):
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def View(self):
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Column(self):
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def ReAuth(self):
        return self._ReAuth

    @ReAuth.setter
    def ReAuth(self, ReAuth):
        self._ReAuth = ReAuth

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SourceId(self):
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Catalog = params.get("Catalog")
        self._Table = params.get("Table")
        self._Operation = params.get("Operation")
        self._PolicyType = params.get("PolicyType")
        self._Function = params.get("Function")
        self._View = params.get("View")
        self._Column = params.get("Column")
        self._DataEngine = params.get("DataEngine")
        self._ReAuth = params.get("ReAuth")
        self._Source = params.get("Source")
        self._Mode = params.get("Mode")
        self._Operator = params.get("Operator")
        self._CreateTime = params.get("CreateTime")
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrestoMonitorMetrics(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _LocalCacheHitRate: 
        :type LocalCacheHitRate: float
        :param _FragmentCacheHitRate: 
        :type FragmentCacheHitRate: float
        """
        self._LocalCacheHitRate = None
        self._FragmentCacheHitRate = None

    @property
    def LocalCacheHitRate(self):
        return self._LocalCacheHitRate

    @LocalCacheHitRate.setter
    def LocalCacheHitRate(self, LocalCacheHitRate):
        self._LocalCacheHitRate = LocalCacheHitRate

    @property
    def FragmentCacheHitRate(self):
        return self._FragmentCacheHitRate

    @FragmentCacheHitRate.setter
    def FragmentCacheHitRate(self, FragmentCacheHitRate):
        self._FragmentCacheHitRate = FragmentCacheHitRate


    def _deserialize(self, params):
        self._LocalCacheHitRate = params.get("LocalCacheHitRate")
        self._FragmentCacheHitRate = params.get("FragmentCacheHitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """Properties of database and table

    """

    def __init__(self):
        r"""
        :param _Key: The property key name.
        :type Key: str
        :param _Value: The property value.
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
        


class SQLTask(AbstractModel):
    """SQL query task

    """

    def __init__(self):
        r"""
        :param _SQL: Base64-encrypted SQL statement
        :type SQL: str
        :param _Config: Task configuration information
        :type Config: list of KVPair
        """
        self._SQL = None
        self._Config = None

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._SQL = params.get("SQL")
        if params.get("Config") is not None:
            self._Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self._Config.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionResourceTemplate(AbstractModel):
    """The session resource configuration template for a Spark cluster.

    """

    def __init__(self):
        r"""
        :param _DriverSize: The driver size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DriverSize: str
        :param _ExecutorSize: The executor size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorSize: str
        :param _ExecutorNums: The executor count. The minimum value is 1 and the maximum value is less than the cluster specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorNums: int
        :param _ExecutorMaxNumbers: The maximum executor count (in dynamic mode). The minimum value is 1 and the maximum value is less than the cluster specification. If you set `ExecutorMaxNumbers` to a value smaller than that of `ExecutorNums`, the value of `ExecutorMaxNumbers` is automatically changed to that of `ExecutorNums`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorMaxNumbers: int
        """
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNums = None
        self._ExecutorMaxNumbers = None

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNums(self):
        return self._ExecutorNums

    @ExecutorNums.setter
    def ExecutorNums(self, ExecutorNums):
        self._ExecutorNums = ExecutorNums

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers


    def _deserialize(self, params):
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNums = params.get("ExecutorNums")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkJobInfo(AbstractModel):
    """Spark job details

    """

    def __init__(self):
        r"""
        :param _JobId: Spark job ID
        :type JobId: str
        :param _JobName: Spark job name
        :type JobName: str
        :param _JobType: Spark job type. Valid values: `1` (batch job), `2` (streaming job).
        :type JobType: int
        :param _DataEngine: Engine name
        :type DataEngine: str
        :param _Eni: This field has been disused. Use the `Datasource` field instead.
        :type Eni: str
        :param _IsLocal: Whether the program package is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocal: str
        :param _JobFile: Program package path
        :type JobFile: str
        :param _RoleArn: Role ID
        :type RoleArn: int
        :param _MainClass: Main class of Spark job execution
        :type MainClass: str
        :param _CmdArgs: Command line parameters of the Spark job separated by space
        :type CmdArgs: str
        :param _JobConf: Native Spark configurations separated by line break
        :type JobConf: str
        :param _IsLocalJars: Whether the dependency JAR packages are uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocalJars: str
        :param _JobJars: Dependency JAR packages of the Spark job separated by comma
        :type JobJars: str
        :param _IsLocalFiles: Whether the dependency file is uploaded locally. Valid values: `cos`, `lakefs`.
        :type IsLocalFiles: str
        :param _JobFiles: Dependency files of the Spark job separated by comma
        :type JobFiles: str
        :param _JobDriverSize: Driver resource size of the Spark job
        :type JobDriverSize: str
        :param _JobExecutorSize: Executor resource size of the Spark job
        :type JobExecutorSize: str
        :param _JobExecutorNums: Number of Spark job executors
        :type JobExecutorNums: int
        :param _JobMaxAttempts: Maximum number of retries of the Spark flow task
        :type JobMaxAttempts: int
        :param _JobCreator: Spark job creator
        :type JobCreator: str
        :param _JobCreateTime: Spark job creation time
        :type JobCreateTime: int
        :param _JobUpdateTime: Spark job update time
        :type JobUpdateTime: int
        :param _CurrentTaskId: Last task ID of the Spark job
        :type CurrentTaskId: str
        :param _JobStatus: Last status of the Spark job
        :type JobStatus: int
        :param _StreamingStat: Spark streaming job statistics
Note: This field may return null, indicating that no valid values can be obtained.
        :type StreamingStat: :class:`tencentcloud.dlc.v20210125.models.StreamingStatistics`
        :param _DataSource: Data source name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSource: str
        :param _IsLocalPythonFiles: PySpark: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsLocalPythonFiles: str
        :param _AppPythonFiles: Note: This returned value has been disused.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppPythonFiles: str
        :param _IsLocalArchives: Archives: Dependency upload method. 1: cos; 2: lakefs (this method needs to be used in the console but cannot be called through APIs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsLocalArchives: str
        :param _JobArchives: Archives: Dependency resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobArchives: str
        :param _SparkImage: The Spark image version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkImage: str
        :param _JobPythonFiles: PySpark: Python dependency, which can be in .py, .zip, or .egg format. Multiple files should be separated by comma.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobPythonFiles: str
        :param _TaskNum: Number of tasks running or ready to run under the current job
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskNum: int
        :param _DataEngineStatus: Engine status. -100 (default value): unknown; -2–11: normal.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineStatus: int
        :param _JobExecutorMaxNumbers: The specified executor count (max), which defaults to 1. This parameter applies if the "Dynamic" mode is selected. If the "Dynamic" mode is not selected, the executor count is equal to `JobExecutorNums`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobExecutorMaxNumbers: int
        :param _SparkImageVersion: The image version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkImageVersion: str
        :param _SessionId: The ID of the associated Data Lake Compute query script.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionId: str
        :param _DataEngineClusterType: `spark_emr_livy` indicates to create an EMR cluster.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineClusterType: str
        :param _DataEngineImageVersion: `Spark 3.2-EMR` indicates to use the Spark 3.2 image.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineImageVersion: str
        :param _IsInherit: Whether the task resource configuration is inherited from the cluster template. Valid values: `0` (default): No; `1`: Yes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsInherit: int
        """
        self._JobId = None
        self._JobName = None
        self._JobType = None
        self._DataEngine = None
        self._Eni = None
        self._IsLocal = None
        self._JobFile = None
        self._RoleArn = None
        self._MainClass = None
        self._CmdArgs = None
        self._JobConf = None
        self._IsLocalJars = None
        self._JobJars = None
        self._IsLocalFiles = None
        self._JobFiles = None
        self._JobDriverSize = None
        self._JobExecutorSize = None
        self._JobExecutorNums = None
        self._JobMaxAttempts = None
        self._JobCreator = None
        self._JobCreateTime = None
        self._JobUpdateTime = None
        self._CurrentTaskId = None
        self._JobStatus = None
        self._StreamingStat = None
        self._DataSource = None
        self._IsLocalPythonFiles = None
        self._AppPythonFiles = None
        self._IsLocalArchives = None
        self._JobArchives = None
        self._SparkImage = None
        self._JobPythonFiles = None
        self._TaskNum = None
        self._DataEngineStatus = None
        self._JobExecutorMaxNumbers = None
        self._SparkImageVersion = None
        self._SessionId = None
        self._DataEngineClusterType = None
        self._DataEngineImageVersion = None
        self._IsInherit = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def DataEngine(self):
        return self._DataEngine

    @DataEngine.setter
    def DataEngine(self, DataEngine):
        self._DataEngine = DataEngine

    @property
    def Eni(self):
        return self._Eni

    @Eni.setter
    def Eni(self, Eni):
        self._Eni = Eni

    @property
    def IsLocal(self):
        return self._IsLocal

    @IsLocal.setter
    def IsLocal(self, IsLocal):
        self._IsLocal = IsLocal

    @property
    def JobFile(self):
        return self._JobFile

    @JobFile.setter
    def JobFile(self, JobFile):
        self._JobFile = JobFile

    @property
    def RoleArn(self):
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def MainClass(self):
        return self._MainClass

    @MainClass.setter
    def MainClass(self, MainClass):
        self._MainClass = MainClass

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def JobConf(self):
        return self._JobConf

    @JobConf.setter
    def JobConf(self, JobConf):
        self._JobConf = JobConf

    @property
    def IsLocalJars(self):
        return self._IsLocalJars

    @IsLocalJars.setter
    def IsLocalJars(self, IsLocalJars):
        self._IsLocalJars = IsLocalJars

    @property
    def JobJars(self):
        return self._JobJars

    @JobJars.setter
    def JobJars(self, JobJars):
        self._JobJars = JobJars

    @property
    def IsLocalFiles(self):
        return self._IsLocalFiles

    @IsLocalFiles.setter
    def IsLocalFiles(self, IsLocalFiles):
        self._IsLocalFiles = IsLocalFiles

    @property
    def JobFiles(self):
        return self._JobFiles

    @JobFiles.setter
    def JobFiles(self, JobFiles):
        self._JobFiles = JobFiles

    @property
    def JobDriverSize(self):
        return self._JobDriverSize

    @JobDriverSize.setter
    def JobDriverSize(self, JobDriverSize):
        self._JobDriverSize = JobDriverSize

    @property
    def JobExecutorSize(self):
        return self._JobExecutorSize

    @JobExecutorSize.setter
    def JobExecutorSize(self, JobExecutorSize):
        self._JobExecutorSize = JobExecutorSize

    @property
    def JobExecutorNums(self):
        return self._JobExecutorNums

    @JobExecutorNums.setter
    def JobExecutorNums(self, JobExecutorNums):
        self._JobExecutorNums = JobExecutorNums

    @property
    def JobMaxAttempts(self):
        return self._JobMaxAttempts

    @JobMaxAttempts.setter
    def JobMaxAttempts(self, JobMaxAttempts):
        self._JobMaxAttempts = JobMaxAttempts

    @property
    def JobCreator(self):
        return self._JobCreator

    @JobCreator.setter
    def JobCreator(self, JobCreator):
        self._JobCreator = JobCreator

    @property
    def JobCreateTime(self):
        return self._JobCreateTime

    @JobCreateTime.setter
    def JobCreateTime(self, JobCreateTime):
        self._JobCreateTime = JobCreateTime

    @property
    def JobUpdateTime(self):
        return self._JobUpdateTime

    @JobUpdateTime.setter
    def JobUpdateTime(self, JobUpdateTime):
        self._JobUpdateTime = JobUpdateTime

    @property
    def CurrentTaskId(self):
        return self._CurrentTaskId

    @CurrentTaskId.setter
    def CurrentTaskId(self, CurrentTaskId):
        self._CurrentTaskId = CurrentTaskId

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def StreamingStat(self):
        return self._StreamingStat

    @StreamingStat.setter
    def StreamingStat(self, StreamingStat):
        self._StreamingStat = StreamingStat

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IsLocalPythonFiles(self):
        return self._IsLocalPythonFiles

    @IsLocalPythonFiles.setter
    def IsLocalPythonFiles(self, IsLocalPythonFiles):
        self._IsLocalPythonFiles = IsLocalPythonFiles

    @property
    def AppPythonFiles(self):
        return self._AppPythonFiles

    @AppPythonFiles.setter
    def AppPythonFiles(self, AppPythonFiles):
        self._AppPythonFiles = AppPythonFiles

    @property
    def IsLocalArchives(self):
        return self._IsLocalArchives

    @IsLocalArchives.setter
    def IsLocalArchives(self, IsLocalArchives):
        self._IsLocalArchives = IsLocalArchives

    @property
    def JobArchives(self):
        return self._JobArchives

    @JobArchives.setter
    def JobArchives(self, JobArchives):
        self._JobArchives = JobArchives

    @property
    def SparkImage(self):
        return self._SparkImage

    @SparkImage.setter
    def SparkImage(self, SparkImage):
        self._SparkImage = SparkImage

    @property
    def JobPythonFiles(self):
        return self._JobPythonFiles

    @JobPythonFiles.setter
    def JobPythonFiles(self, JobPythonFiles):
        self._JobPythonFiles = JobPythonFiles

    @property
    def TaskNum(self):
        return self._TaskNum

    @TaskNum.setter
    def TaskNum(self, TaskNum):
        self._TaskNum = TaskNum

    @property
    def DataEngineStatus(self):
        return self._DataEngineStatus

    @DataEngineStatus.setter
    def DataEngineStatus(self, DataEngineStatus):
        self._DataEngineStatus = DataEngineStatus

    @property
    def JobExecutorMaxNumbers(self):
        return self._JobExecutorMaxNumbers

    @JobExecutorMaxNumbers.setter
    def JobExecutorMaxNumbers(self, JobExecutorMaxNumbers):
        self._JobExecutorMaxNumbers = JobExecutorMaxNumbers

    @property
    def SparkImageVersion(self):
        return self._SparkImageVersion

    @SparkImageVersion.setter
    def SparkImageVersion(self, SparkImageVersion):
        self._SparkImageVersion = SparkImageVersion

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def DataEngineClusterType(self):
        return self._DataEngineClusterType

    @DataEngineClusterType.setter
    def DataEngineClusterType(self, DataEngineClusterType):
        self._DataEngineClusterType = DataEngineClusterType

    @property
    def DataEngineImageVersion(self):
        return self._DataEngineImageVersion

    @DataEngineImageVersion.setter
    def DataEngineImageVersion(self, DataEngineImageVersion):
        self._DataEngineImageVersion = DataEngineImageVersion

    @property
    def IsInherit(self):
        return self._IsInherit

    @IsInherit.setter
    def IsInherit(self, IsInherit):
        self._IsInherit = IsInherit


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobType = params.get("JobType")
        self._DataEngine = params.get("DataEngine")
        self._Eni = params.get("Eni")
        self._IsLocal = params.get("IsLocal")
        self._JobFile = params.get("JobFile")
        self._RoleArn = params.get("RoleArn")
        self._MainClass = params.get("MainClass")
        self._CmdArgs = params.get("CmdArgs")
        self._JobConf = params.get("JobConf")
        self._IsLocalJars = params.get("IsLocalJars")
        self._JobJars = params.get("JobJars")
        self._IsLocalFiles = params.get("IsLocalFiles")
        self._JobFiles = params.get("JobFiles")
        self._JobDriverSize = params.get("JobDriverSize")
        self._JobExecutorSize = params.get("JobExecutorSize")
        self._JobExecutorNums = params.get("JobExecutorNums")
        self._JobMaxAttempts = params.get("JobMaxAttempts")
        self._JobCreator = params.get("JobCreator")
        self._JobCreateTime = params.get("JobCreateTime")
        self._JobUpdateTime = params.get("JobUpdateTime")
        self._CurrentTaskId = params.get("CurrentTaskId")
        self._JobStatus = params.get("JobStatus")
        if params.get("StreamingStat") is not None:
            self._StreamingStat = StreamingStatistics()
            self._StreamingStat._deserialize(params.get("StreamingStat"))
        self._DataSource = params.get("DataSource")
        self._IsLocalPythonFiles = params.get("IsLocalPythonFiles")
        self._AppPythonFiles = params.get("AppPythonFiles")
        self._IsLocalArchives = params.get("IsLocalArchives")
        self._JobArchives = params.get("JobArchives")
        self._SparkImage = params.get("SparkImage")
        self._JobPythonFiles = params.get("JobPythonFiles")
        self._TaskNum = params.get("TaskNum")
        self._DataEngineStatus = params.get("DataEngineStatus")
        self._JobExecutorMaxNumbers = params.get("JobExecutorMaxNumbers")
        self._SparkImageVersion = params.get("SparkImageVersion")
        self._SessionId = params.get("SessionId")
        self._DataEngineClusterType = params.get("DataEngineClusterType")
        self._DataEngineImageVersion = params.get("DataEngineImageVersion")
        self._IsInherit = params.get("IsInherit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkMonitorMetrics(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _ShuffleWriteBytesCos: 
        :type ShuffleWriteBytesCos: int
        :param _ShuffleWriteBytesTotal: 
        :type ShuffleWriteBytesTotal: int
        """
        self._ShuffleWriteBytesCos = None
        self._ShuffleWriteBytesTotal = None

    @property
    def ShuffleWriteBytesCos(self):
        return self._ShuffleWriteBytesCos

    @ShuffleWriteBytesCos.setter
    def ShuffleWriteBytesCos(self, ShuffleWriteBytesCos):
        self._ShuffleWriteBytesCos = ShuffleWriteBytesCos

    @property
    def ShuffleWriteBytesTotal(self):
        return self._ShuffleWriteBytesTotal

    @ShuffleWriteBytesTotal.setter
    def ShuffleWriteBytesTotal(self, ShuffleWriteBytesTotal):
        self._ShuffleWriteBytesTotal = ShuffleWriteBytesTotal


    def _deserialize(self, params):
        self._ShuffleWriteBytesCos = params.get("ShuffleWriteBytesCos")
        self._ShuffleWriteBytesTotal = params.get("ShuffleWriteBytesTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkSessionBatchLog(AbstractModel):
    """Running logs of a Spark SQL batch job

    """

    def __init__(self):
        r"""
        :param _Step: The log step. Valid values: `BEG`, `CS`, `DS`, `DSS`, `DSF`, `FINF`, `RTO`, `CANCEL`, `CT`, `DT`, `DTS`, `DTF`, `FINT`, and `EXCE`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Step: str
        :param _Time: Time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Time: str
        :param _Message: The log message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Operate: The operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operate: list of SparkSessionBatchLogOperate
        """
        self._Step = None
        self._Time = None
        self._Message = None
        self._Operate = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._Time = params.get("Time")
        self._Message = params.get("Message")
        if params.get("Operate") is not None:
            self._Operate = []
            for item in params.get("Operate"):
                obj = SparkSessionBatchLogOperate()
                obj._deserialize(item)
                self._Operate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SparkSessionBatchLogOperate(AbstractModel):
    """Operation information in the logs of a Spark SQL batch job

    """

    def __init__(self):
        r"""
        :param _Text: The operation message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Text: str
        :param _Operate: The operation type. Valid values: `COPY`, `LOG`, `UI`, `RESULT`, `List`, and `TAB`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operate: str
        :param _Supplement: Additional information, such as taskid, sessionid, and sparkui.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Supplement: list of KVPair
        """
        self._Text = None
        self._Operate = None
        self._Supplement = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def Supplement(self):
        return self._Supplement

    @Supplement.setter
    def Supplement(self, Supplement):
        self._Supplement = Supplement


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Operate = params.get("Operate")
        if params.get("Supplement") is not None:
            self._Supplement = []
            for item in params.get("Supplement"):
                obj = KVPair()
                obj._deserialize(item)
                self._Supplement.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamingStatistics(AbstractModel):
    """Statistics of the Spark flow task

    """

    def __init__(self):
        r"""
        :param _StartTime: Task start time
        :type StartTime: str
        :param _Receivers: Number of data receivers
        :type Receivers: int
        :param _NumActiveReceivers: Number of receivers in service
        :type NumActiveReceivers: int
        :param _NumInactiveReceivers: Number of inactive receivers
        :type NumInactiveReceivers: int
        :param _NumActiveBatches: Number of running batches
        :type NumActiveBatches: int
        :param _NumRetainedCompletedBatches: Number of batches to be processed
        :type NumRetainedCompletedBatches: int
        :param _NumTotalCompletedBatches: Number of completed batches
        :type NumTotalCompletedBatches: int
        :param _AverageInputRate: Average input speed
        :type AverageInputRate: float
        :param _AverageSchedulingDelay: Average queue time
        :type AverageSchedulingDelay: float
        :param _AverageProcessingTime: Average processing time
        :type AverageProcessingTime: float
        :param _AverageTotalDelay: Average latency
        :type AverageTotalDelay: float
        """
        self._StartTime = None
        self._Receivers = None
        self._NumActiveReceivers = None
        self._NumInactiveReceivers = None
        self._NumActiveBatches = None
        self._NumRetainedCompletedBatches = None
        self._NumTotalCompletedBatches = None
        self._AverageInputRate = None
        self._AverageSchedulingDelay = None
        self._AverageProcessingTime = None
        self._AverageTotalDelay = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def NumActiveReceivers(self):
        return self._NumActiveReceivers

    @NumActiveReceivers.setter
    def NumActiveReceivers(self, NumActiveReceivers):
        self._NumActiveReceivers = NumActiveReceivers

    @property
    def NumInactiveReceivers(self):
        return self._NumInactiveReceivers

    @NumInactiveReceivers.setter
    def NumInactiveReceivers(self, NumInactiveReceivers):
        self._NumInactiveReceivers = NumInactiveReceivers

    @property
    def NumActiveBatches(self):
        return self._NumActiveBatches

    @NumActiveBatches.setter
    def NumActiveBatches(self, NumActiveBatches):
        self._NumActiveBatches = NumActiveBatches

    @property
    def NumRetainedCompletedBatches(self):
        return self._NumRetainedCompletedBatches

    @NumRetainedCompletedBatches.setter
    def NumRetainedCompletedBatches(self, NumRetainedCompletedBatches):
        self._NumRetainedCompletedBatches = NumRetainedCompletedBatches

    @property
    def NumTotalCompletedBatches(self):
        return self._NumTotalCompletedBatches

    @NumTotalCompletedBatches.setter
    def NumTotalCompletedBatches(self, NumTotalCompletedBatches):
        self._NumTotalCompletedBatches = NumTotalCompletedBatches

    @property
    def AverageInputRate(self):
        return self._AverageInputRate

    @AverageInputRate.setter
    def AverageInputRate(self, AverageInputRate):
        self._AverageInputRate = AverageInputRate

    @property
    def AverageSchedulingDelay(self):
        return self._AverageSchedulingDelay

    @AverageSchedulingDelay.setter
    def AverageSchedulingDelay(self, AverageSchedulingDelay):
        self._AverageSchedulingDelay = AverageSchedulingDelay

    @property
    def AverageProcessingTime(self):
        return self._AverageProcessingTime

    @AverageProcessingTime.setter
    def AverageProcessingTime(self, AverageProcessingTime):
        self._AverageProcessingTime = AverageProcessingTime

    @property
    def AverageTotalDelay(self):
        return self._AverageTotalDelay

    @AverageTotalDelay.setter
    def AverageTotalDelay(self, AverageTotalDelay):
        self._AverageTotalDelay = AverageTotalDelay


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Receivers = params.get("Receivers")
        self._NumActiveReceivers = params.get("NumActiveReceivers")
        self._NumInactiveReceivers = params.get("NumInactiveReceivers")
        self._NumActiveBatches = params.get("NumActiveBatches")
        self._NumRetainedCompletedBatches = params.get("NumRetainedCompletedBatches")
        self._NumTotalCompletedBatches = params.get("NumTotalCompletedBatches")
        self._AverageInputRate = params.get("AverageInputRate")
        self._AverageSchedulingDelay = params.get("AverageSchedulingDelay")
        self._AverageProcessingTime = params.get("AverageProcessingTime")
        self._AverageTotalDelay = params.get("AverageTotalDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineRequest(AbstractModel):
    """SuspendResumeDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineName: The name of a virtual cluster.
        :type DataEngineName: str
        :param _Operate: The operation type: `suspend` or `resume`.
        :type Operate: str
        """
        self._DataEngineName = None
        self._Operate = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendResumeDataEngineResponse(AbstractModel):
    """SuspendResumeDataEngine response structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineName: The details of the virtual cluster.
        :type DataEngineName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataEngineName = None
        self._RequestId = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._RequestId = params.get("RequestId")


class SwitchDataEngineRequest(AbstractModel):
    """SwitchDataEngine request structure.

    """

    def __init__(self):
        r"""
        :param _DataEngineName: The name of the primary cluster.
        :type DataEngineName: str
        :param _StartStandbyCluster: Whether to start the standby cluster.
        :type StartStandbyCluster: bool
        """
        self._DataEngineName = None
        self._StartStandbyCluster = None

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def StartStandbyCluster(self):
        return self._StartStandbyCluster

    @StartStandbyCluster.setter
    def StartStandbyCluster(self, StartStandbyCluster):
        self._StartStandbyCluster = StartStandbyCluster


    def _deserialize(self, params):
        self._DataEngineName = params.get("DataEngineName")
        self._StartStandbyCluster = params.get("StartStandbyCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDataEngineResponse(AbstractModel):
    """SwitchDataEngine response structure.

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


class TColumn(AbstractModel):
    """Table field information

    """

    def __init__(self):
        r"""
        :param _Name: The field name.
        :type Name: str
        :param _Type: The field type.
        :type Type: str
        :param _Comment: The field description.
        :type Comment: str
        :param _Default: The default field value.
        :type Default: str
        :param _NotNull: Whether the field is not null.
        :type NotNull: bool
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Default = None
        self._NotNull = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def NotNull(self):
        return self._NotNull

    @NotNull.setter
    def NotNull(self, NotNull):
        self._NotNull = NotNull


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Default = params.get("Default")
        self._NotNull = params.get("NotNull")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TPartition(AbstractModel):
    """Table partition information

    """

    def __init__(self):
        r"""
        :param _Name: The field name.
        :type Name: str
        :param _Type: The field type.
        :type Type: str
        :param _Comment: The field description.
        :type Comment: str
        :param _PartitionType: The partition type.
        :type PartitionType: str
        :param _PartitionFormat: The partition format.
        :type PartitionFormat: str
        :param _PartitionDot: The separator count of the partition conversion policy.
        :type PartitionDot: int
        :param _Transform: The partition conversion policy.
        :type Transform: str
        :param _TransformArgs: The policy parameters.
        :type TransformArgs: list of str
        """
        self._Name = None
        self._Type = None
        self._Comment = None
        self._PartitionType = None
        self._PartitionFormat = None
        self._PartitionDot = None
        self._Transform = None
        self._TransformArgs = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def PartitionFormat(self):
        return self._PartitionFormat

    @PartitionFormat.setter
    def PartitionFormat(self, PartitionFormat):
        self._PartitionFormat = PartitionFormat

    @property
    def PartitionDot(self):
        return self._PartitionDot

    @PartitionDot.setter
    def PartitionDot(self, PartitionDot):
        self._PartitionDot = PartitionDot

    @property
    def Transform(self):
        return self._Transform

    @Transform.setter
    def Transform(self, Transform):
        self._Transform = Transform

    @property
    def TransformArgs(self):
        return self._TransformArgs

    @TransformArgs.setter
    def TransformArgs(self, TransformArgs):
        self._TransformArgs = TransformArgs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._PartitionType = params.get("PartitionType")
        self._PartitionFormat = params.get("PartitionFormat")
        self._PartitionDot = params.get("PartitionDot")
        self._Transform = params.get("Transform")
        self._TransformArgs = params.get("TransformArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableBaseInfo(AbstractModel):
    """Table configurations

    """

    def __init__(self):
        r"""
        :param _DatabaseName: The database name.
        :type DatabaseName: str
        :param _TableName: The table name.
        :type TableName: str
        :param _DatasourceConnectionName: The data source name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatasourceConnectionName: str
        :param _TableComment: The table remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableComment: str
        :param _Type: The specific type: `table` or `view`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _TableFormat: The data format type, such as `hive` and `iceberg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableFormat: str
        :param _UserAlias: The table creator name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAlias: str
        :param _UserSubUin: The table creator ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserSubUin: str
        :param _GovernPolicy: The data governance configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GovernPolicy: :class:`tencentcloud.dlc.v20210125.models.DataGovernPolicy`
        :param _DbGovernPolicyIsDisable: Whether database data governance is disabled. Valid values: `true` (disabled) and `false` (not disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbGovernPolicyIsDisable: str
        """
        self._DatabaseName = None
        self._TableName = None
        self._DatasourceConnectionName = None
        self._TableComment = None
        self._Type = None
        self._TableFormat = None
        self._UserAlias = None
        self._UserSubUin = None
        self._GovernPolicy = None
        self._DbGovernPolicyIsDisable = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def TableComment(self):
        return self._TableComment

    @TableComment.setter
    def TableComment(self, TableComment):
        self._TableComment = TableComment

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableFormat(self):
        return self._TableFormat

    @TableFormat.setter
    def TableFormat(self, TableFormat):
        self._TableFormat = TableFormat

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def UserSubUin(self):
        return self._UserSubUin

    @UserSubUin.setter
    def UserSubUin(self, UserSubUin):
        self._UserSubUin = UserSubUin

    @property
    def GovernPolicy(self):
        return self._GovernPolicy

    @GovernPolicy.setter
    def GovernPolicy(self, GovernPolicy):
        self._GovernPolicy = GovernPolicy

    @property
    def DbGovernPolicyIsDisable(self):
        return self._DbGovernPolicyIsDisable

    @DbGovernPolicyIsDisable.setter
    def DbGovernPolicyIsDisable(self, DbGovernPolicyIsDisable):
        self._DbGovernPolicyIsDisable = DbGovernPolicyIsDisable


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._TableComment = params.get("TableComment")
        self._Type = params.get("Type")
        self._TableFormat = params.get("TableFormat")
        self._UserAlias = params.get("UserAlias")
        self._UserSubUin = params.get("UserSubUin")
        if params.get("GovernPolicy") is not None:
            self._GovernPolicy = DataGovernPolicy()
            self._GovernPolicy._deserialize(params.get("GovernPolicy"))
        self._DbGovernPolicyIsDisable = params.get("DbGovernPolicyIsDisable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """Tag pair info

    """

    def __init__(self):
        r"""
        :param _TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class Task(AbstractModel):
    """Task type, such as SQL query.

    """

    def __init__(self):
        r"""
        :param _SQLTask: SQL query task
        :type SQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        :param _SparkSQLTask: Spark SQL query task
        :type SparkSQLTask: :class:`tencentcloud.dlc.v20210125.models.SQLTask`
        """
        self._SQLTask = None
        self._SparkSQLTask = None

    @property
    def SQLTask(self):
        return self._SQLTask

    @SQLTask.setter
    def SQLTask(self, SQLTask):
        self._SQLTask = SQLTask

    @property
    def SparkSQLTask(self):
        return self._SparkSQLTask

    @SparkSQLTask.setter
    def SparkSQLTask(self, SparkSQLTask):
        self._SparkSQLTask = SparkSQLTask


    def _deserialize(self, params):
        if params.get("SQLTask") is not None:
            self._SQLTask = SQLTask()
            self._SQLTask._deserialize(params.get("SQLTask"))
        if params.get("SparkSQLTask") is not None:
            self._SparkSQLTask = SQLTask()
            self._SparkSQLTask._deserialize(params.get("SparkSQLTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResponseInfo(AbstractModel):
    """The task instance.

    """

    def __init__(self):
        r"""
        :param _DatabaseName: Database name of the task
        :type DatabaseName: str
        :param _DataAmount: Data volume of the task
        :type DataAmount: int
        :param _Id: Task ID
        :type Id: str
        :param _UsedTime: The compute time in ms.
        :type UsedTime: int
        :param _OutputPath: Task output path
        :type OutputPath: str
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _State: Task status. Valid values: `0` (initial), `1` (executing), `2` (executed successfully), `-1` (failed to execute), `-3` (canceled).
        :type State: int
        :param _SQLType: SQL statement type of the task, such as DDL and DML.
        :type SQLType: str
        :param _SQL: SQL statement of the task
        :type SQL: str
        :param _ResultExpired: Whether the result has expired
        :type ResultExpired: bool
        :param _RowAffectInfo: Number of affected data rows
        :type RowAffectInfo: str
        :param _DataSet: Dataset of task results
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSet: str
        :param _Error: Failure information, such as `errorMessage`. This field has been disused.
        :type Error: str
        :param _Percentage: Task progress (%)
        :type Percentage: int
        :param _OutputMessage: Output information of task execution
        :type OutputMessage: str
        :param _TaskType: Type of the engine executing the SQL statement
        :type TaskType: str
        :param _ProgressDetail: Task progress details
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProgressDetail: str
        :param _UpdateTime: Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _DataEngineId: Compute resource ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineId: str
        :param _OperateUin: Sub-UIN that executes the SQL statement
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperateUin: str
        :param _DataEngineName: Compute resource name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataEngineName: str
        :param _InputType: Whether the import type is local import or COS
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputType: str
        :param _InputConf: Import configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputConf: str
        :param _DataNumber: Number of data entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataNumber: int
        :param _CanDownload: Whether the data can be downloaded
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanDownload: bool
        :param _UserAlias: User alias
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserAlias: str
        :param _SparkJobName: Spark application job name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobName: str
        :param _SparkJobId: Spark application job ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobId: str
        :param _SparkJobFile: JAR file of the Spark application entry
Note: This field may return null, indicating that no valid values can be obtained.
        :type SparkJobFile: str
        :param _UiUrl: Spark UI URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type UiUrl: str
        :param _TotalTime: The task time in ms.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalTime: int
        :param _CmdArgs: The program entry parameter for running a task under a Spark job.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CmdArgs: str
        :param _ImageVersion: The image version of the cluster.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageVersion: str
        :param _DriverSize: The driver size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DriverSize: str
        :param _ExecutorSize: The executor size.
Valid values for the standard resource type: `small`, `medium`, `large`, and `xlarge`.
Valid values for the memory resource type: `m.small`, `m.medium`, `m.large`, and `m.xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorSize: str
        :param _ExecutorNums: The executor count. The minimum value is 1 and the maximum value is less than the cluster specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorNums: int
        :param _ExecutorMaxNumbers: The maximum executor count (in dynamic mode). The minimum value is 1 and the maximum value is less than the cluster specification. If you set `ExecutorMaxNumbers` to a value smaller than that of `ExecutorNums`, the value of `ExecutorMaxNumbers` is automatically changed to that of `ExecutorNums`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutorMaxNumbers: int
        :param _CommonMetrics: 
        :type CommonMetrics: :class:`tencentcloud.dlc.v20210125.models.CommonMetrics`
        :param _SparkMonitorMetrics: 
        :type SparkMonitorMetrics: :class:`tencentcloud.dlc.v20210125.models.SparkMonitorMetrics`
        :param _PrestoMonitorMetrics: 
        :type PrestoMonitorMetrics: :class:`tencentcloud.dlc.v20210125.models.PrestoMonitorMetrics`
        """
        self._DatabaseName = None
        self._DataAmount = None
        self._Id = None
        self._UsedTime = None
        self._OutputPath = None
        self._CreateTime = None
        self._State = None
        self._SQLType = None
        self._SQL = None
        self._ResultExpired = None
        self._RowAffectInfo = None
        self._DataSet = None
        self._Error = None
        self._Percentage = None
        self._OutputMessage = None
        self._TaskType = None
        self._ProgressDetail = None
        self._UpdateTime = None
        self._DataEngineId = None
        self._OperateUin = None
        self._DataEngineName = None
        self._InputType = None
        self._InputConf = None
        self._DataNumber = None
        self._CanDownload = None
        self._UserAlias = None
        self._SparkJobName = None
        self._SparkJobId = None
        self._SparkJobFile = None
        self._UiUrl = None
        self._TotalTime = None
        self._CmdArgs = None
        self._ImageVersion = None
        self._DriverSize = None
        self._ExecutorSize = None
        self._ExecutorNums = None
        self._ExecutorMaxNumbers = None
        self._CommonMetrics = None
        self._SparkMonitorMetrics = None
        self._PrestoMonitorMetrics = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def DataAmount(self):
        return self._DataAmount

    @DataAmount.setter
    def DataAmount(self, DataAmount):
        self._DataAmount = DataAmount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def OutputPath(self):
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SQLType(self):
        return self._SQLType

    @SQLType.setter
    def SQLType(self, SQLType):
        self._SQLType = SQLType

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def ResultExpired(self):
        return self._ResultExpired

    @ResultExpired.setter
    def ResultExpired(self, ResultExpired):
        self._ResultExpired = ResultExpired

    @property
    def RowAffectInfo(self):
        return self._RowAffectInfo

    @RowAffectInfo.setter
    def RowAffectInfo(self, RowAffectInfo):
        self._RowAffectInfo = RowAffectInfo

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def OutputMessage(self):
        return self._OutputMessage

    @OutputMessage.setter
    def OutputMessage(self, OutputMessage):
        self._OutputMessage = OutputMessage

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ProgressDetail(self):
        return self._ProgressDetail

    @ProgressDetail.setter
    def ProgressDetail(self, ProgressDetail):
        self._ProgressDetail = ProgressDetail

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DataEngineId(self):
        return self._DataEngineId

    @DataEngineId.setter
    def DataEngineId(self, DataEngineId):
        self._DataEngineId = DataEngineId

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def DataEngineName(self):
        return self._DataEngineName

    @DataEngineName.setter
    def DataEngineName(self, DataEngineName):
        self._DataEngineName = DataEngineName

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputConf(self):
        return self._InputConf

    @InputConf.setter
    def InputConf(self, InputConf):
        self._InputConf = InputConf

    @property
    def DataNumber(self):
        return self._DataNumber

    @DataNumber.setter
    def DataNumber(self, DataNumber):
        self._DataNumber = DataNumber

    @property
    def CanDownload(self):
        return self._CanDownload

    @CanDownload.setter
    def CanDownload(self, CanDownload):
        self._CanDownload = CanDownload

    @property
    def UserAlias(self):
        return self._UserAlias

    @UserAlias.setter
    def UserAlias(self, UserAlias):
        self._UserAlias = UserAlias

    @property
    def SparkJobName(self):
        return self._SparkJobName

    @SparkJobName.setter
    def SparkJobName(self, SparkJobName):
        self._SparkJobName = SparkJobName

    @property
    def SparkJobId(self):
        return self._SparkJobId

    @SparkJobId.setter
    def SparkJobId(self, SparkJobId):
        self._SparkJobId = SparkJobId

    @property
    def SparkJobFile(self):
        return self._SparkJobFile

    @SparkJobFile.setter
    def SparkJobFile(self, SparkJobFile):
        self._SparkJobFile = SparkJobFile

    @property
    def UiUrl(self):
        return self._UiUrl

    @UiUrl.setter
    def UiUrl(self, UiUrl):
        self._UiUrl = UiUrl

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def CmdArgs(self):
        return self._CmdArgs

    @CmdArgs.setter
    def CmdArgs(self, CmdArgs):
        self._CmdArgs = CmdArgs

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def DriverSize(self):
        return self._DriverSize

    @DriverSize.setter
    def DriverSize(self, DriverSize):
        self._DriverSize = DriverSize

    @property
    def ExecutorSize(self):
        return self._ExecutorSize

    @ExecutorSize.setter
    def ExecutorSize(self, ExecutorSize):
        self._ExecutorSize = ExecutorSize

    @property
    def ExecutorNums(self):
        return self._ExecutorNums

    @ExecutorNums.setter
    def ExecutorNums(self, ExecutorNums):
        self._ExecutorNums = ExecutorNums

    @property
    def ExecutorMaxNumbers(self):
        return self._ExecutorMaxNumbers

    @ExecutorMaxNumbers.setter
    def ExecutorMaxNumbers(self, ExecutorMaxNumbers):
        self._ExecutorMaxNumbers = ExecutorMaxNumbers

    @property
    def CommonMetrics(self):
        return self._CommonMetrics

    @CommonMetrics.setter
    def CommonMetrics(self, CommonMetrics):
        self._CommonMetrics = CommonMetrics

    @property
    def SparkMonitorMetrics(self):
        return self._SparkMonitorMetrics

    @SparkMonitorMetrics.setter
    def SparkMonitorMetrics(self, SparkMonitorMetrics):
        self._SparkMonitorMetrics = SparkMonitorMetrics

    @property
    def PrestoMonitorMetrics(self):
        return self._PrestoMonitorMetrics

    @PrestoMonitorMetrics.setter
    def PrestoMonitorMetrics(self, PrestoMonitorMetrics):
        self._PrestoMonitorMetrics = PrestoMonitorMetrics


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._DataAmount = params.get("DataAmount")
        self._Id = params.get("Id")
        self._UsedTime = params.get("UsedTime")
        self._OutputPath = params.get("OutputPath")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._SQLType = params.get("SQLType")
        self._SQL = params.get("SQL")
        self._ResultExpired = params.get("ResultExpired")
        self._RowAffectInfo = params.get("RowAffectInfo")
        self._DataSet = params.get("DataSet")
        self._Error = params.get("Error")
        self._Percentage = params.get("Percentage")
        self._OutputMessage = params.get("OutputMessage")
        self._TaskType = params.get("TaskType")
        self._ProgressDetail = params.get("ProgressDetail")
        self._UpdateTime = params.get("UpdateTime")
        self._DataEngineId = params.get("DataEngineId")
        self._OperateUin = params.get("OperateUin")
        self._DataEngineName = params.get("DataEngineName")
        self._InputType = params.get("InputType")
        self._InputConf = params.get("InputConf")
        self._DataNumber = params.get("DataNumber")
        self._CanDownload = params.get("CanDownload")
        self._UserAlias = params.get("UserAlias")
        self._SparkJobName = params.get("SparkJobName")
        self._SparkJobId = params.get("SparkJobId")
        self._SparkJobFile = params.get("SparkJobFile")
        self._UiUrl = params.get("UiUrl")
        self._TotalTime = params.get("TotalTime")
        self._CmdArgs = params.get("CmdArgs")
        self._ImageVersion = params.get("ImageVersion")
        self._DriverSize = params.get("DriverSize")
        self._ExecutorSize = params.get("ExecutorSize")
        self._ExecutorNums = params.get("ExecutorNums")
        self._ExecutorMaxNumbers = params.get("ExecutorMaxNumbers")
        if params.get("CommonMetrics") is not None:
            self._CommonMetrics = CommonMetrics()
            self._CommonMetrics._deserialize(params.get("CommonMetrics"))
        if params.get("SparkMonitorMetrics") is not None:
            self._SparkMonitorMetrics = SparkMonitorMetrics()
            self._SparkMonitorMetrics._deserialize(params.get("SparkMonitorMetrics"))
        if params.get("PrestoMonitorMetrics") is not None:
            self._PrestoMonitorMetrics = PrestoMonitorMetrics()
            self._PrestoMonitorMetrics._deserialize(params.get("PrestoMonitorMetrics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResultInfo(AbstractModel):
    """The task result information.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID
        :type TaskId: str
        :param _DatasourceConnectionName: Name of the default selected data source when the current job is executed
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatasourceConnectionName: str
        :param _DatabaseName: Name of the default selected database when the current job is executed
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _SQL: The currently executed SQL statement. Each task contains one SQL statement.
        :type SQL: str
        :param _SQLType: Type of the executed task. Valid values: `DDL`, `DML`, `DQL`.
        :type SQLType: str
        :param _State: Current status of the task. `0`: initial; `1`: task running; `2`: task execution succeeded; `-1`: task execution failed; `-3`: task terminated manually by the user. The task execution result will be returned only if task execution succeeds.
        :type State: int
        :param _DataAmount: Amount of the data scanned in bytes
        :type DataAmount: int
        :param _UsedTime: The compute time in ms.
        :type UsedTime: int
        :param _OutputPath: Address of the COS bucket for storing the task result
        :type OutputPath: str
        :param _CreateTime: Task creation timestamp
        :type CreateTime: str
        :param _OutputMessage: Task execution information. `success` will be returned if the task succeeds; otherwise, the failure cause will be returned.
        :type OutputMessage: str
        :param _RowAffectInfo: Number of affected rows
        :type RowAffectInfo: str
        :param _ResultSchema: Schema information of the result
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultSchema: list of Column
        :param _ResultSet: Result information. After it is unescaped, each element of the outer array is a data row.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultSet: str
        :param _NextToken: Pagination information. If there is no more result data, `nextToken` will be empty.
        :type NextToken: str
        :param _Percentage: Task progress (%)
        :type Percentage: int
        :param _ProgressDetail: Task progress details
        :type ProgressDetail: str
        :param _DisplayFormat: Console display format. Valid values: `table`, `text`.
        :type DisplayFormat: str
        :param _TotalTime: The task time in ms.
        :type TotalTime: int
        """
        self._TaskId = None
        self._DatasourceConnectionName = None
        self._DatabaseName = None
        self._SQL = None
        self._SQLType = None
        self._State = None
        self._DataAmount = None
        self._UsedTime = None
        self._OutputPath = None
        self._CreateTime = None
        self._OutputMessage = None
        self._RowAffectInfo = None
        self._ResultSchema = None
        self._ResultSet = None
        self._NextToken = None
        self._Percentage = None
        self._ProgressDetail = None
        self._DisplayFormat = None
        self._TotalTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DatasourceConnectionName(self):
        return self._DatasourceConnectionName

    @DatasourceConnectionName.setter
    def DatasourceConnectionName(self, DatasourceConnectionName):
        self._DatasourceConnectionName = DatasourceConnectionName

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def SQLType(self):
        return self._SQLType

    @SQLType.setter
    def SQLType(self, SQLType):
        self._SQLType = SQLType

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DataAmount(self):
        return self._DataAmount

    @DataAmount.setter
    def DataAmount(self, DataAmount):
        self._DataAmount = DataAmount

    @property
    def UsedTime(self):
        return self._UsedTime

    @UsedTime.setter
    def UsedTime(self, UsedTime):
        self._UsedTime = UsedTime

    @property
    def OutputPath(self):
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def OutputMessage(self):
        return self._OutputMessage

    @OutputMessage.setter
    def OutputMessage(self, OutputMessage):
        self._OutputMessage = OutputMessage

    @property
    def RowAffectInfo(self):
        return self._RowAffectInfo

    @RowAffectInfo.setter
    def RowAffectInfo(self, RowAffectInfo):
        self._RowAffectInfo = RowAffectInfo

    @property
    def ResultSchema(self):
        return self._ResultSchema

    @ResultSchema.setter
    def ResultSchema(self, ResultSchema):
        self._ResultSchema = ResultSchema

    @property
    def ResultSet(self):
        return self._ResultSet

    @ResultSet.setter
    def ResultSet(self, ResultSet):
        self._ResultSet = ResultSet

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def ProgressDetail(self):
        return self._ProgressDetail

    @ProgressDetail.setter
    def ProgressDetail(self, ProgressDetail):
        self._ProgressDetail = ProgressDetail

    @property
    def DisplayFormat(self):
        return self._DisplayFormat

    @DisplayFormat.setter
    def DisplayFormat(self, DisplayFormat):
        self._DisplayFormat = DisplayFormat

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DatasourceConnectionName = params.get("DatasourceConnectionName")
        self._DatabaseName = params.get("DatabaseName")
        self._SQL = params.get("SQL")
        self._SQLType = params.get("SQLType")
        self._State = params.get("State")
        self._DataAmount = params.get("DataAmount")
        self._UsedTime = params.get("UsedTime")
        self._OutputPath = params.get("OutputPath")
        self._CreateTime = params.get("CreateTime")
        self._OutputMessage = params.get("OutputMessage")
        self._RowAffectInfo = params.get("RowAffectInfo")
        if params.get("ResultSchema") is not None:
            self._ResultSchema = []
            for item in params.get("ResultSchema"):
                obj = Column()
                obj._deserialize(item)
                self._ResultSchema.append(obj)
        self._ResultSet = params.get("ResultSet")
        self._NextToken = params.get("NextToken")
        self._Percentage = params.get("Percentage")
        self._ProgressDetail = params.get("ProgressDetail")
        self._DisplayFormat = params.get("DisplayFormat")
        self._TotalTime = params.get("TotalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksInfo(AbstractModel):
    """Collection of tasks executed sequentially in batches

    """

    def __init__(self):
        r"""
        :param _TaskType: Task type. Valid values: `SQLTask` (SQL query task), `SparkSQLTask` (Spark SQL query task).
        :type TaskType: str
        :param _FailureTolerance: Fault tolerance policy. `Proceed`: continues to execute subsequent tasks after the current task fails or is canceled. `Terminate`: terminates the execution of subsequent tasks after the current task fails or is canceled, and marks all subsequent tasks as canceled.
        :type FailureTolerance: str
        :param _SQL: Base64-encrypted SQL statements separated by ";". Up to 50 tasks can be submitted at a time, and they will be executed strictly in sequence.
        :type SQL: str
        :param _Config: Configuration information of the task. Currently, only `SparkSQLTask` tasks are supported.
        :type Config: list of KVPair
        :param _Params: User-defined parameters of the task
        :type Params: list of KVPair
        """
        self._TaskType = None
        self._FailureTolerance = None
        self._SQL = None
        self._Config = None
        self._Params = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def FailureTolerance(self):
        return self._FailureTolerance

    @FailureTolerance.setter
    def FailureTolerance(self, FailureTolerance):
        self._FailureTolerance = FailureTolerance

    @property
    def SQL(self):
        return self._SQL

    @SQL.setter
    def SQL(self, SQL):
        self._SQL = SQL

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._FailureTolerance = params.get("FailureTolerance")
        self._SQL = params.get("SQL")
        if params.get("Config") is not None:
            self._Config = []
            for item in params.get("Config"):
                obj = KVPair()
                obj._deserialize(item)
                self._Config.append(obj)
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = KVPair()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TasksOverview(AbstractModel):
    """The task overview.

    """

    def __init__(self):
        r"""
        :param _TaskQueuedCount: The number of tasks in queue.
        :type TaskQueuedCount: int
        :param _TaskInitCount: The number of initialized tasks.
        :type TaskInitCount: int
        :param _TaskRunningCount: The number of tasks in progress.
        :type TaskRunningCount: int
        :param _TotalTaskCount: The total number of tasks in this time range.
        :type TotalTaskCount: int
        """
        self._TaskQueuedCount = None
        self._TaskInitCount = None
        self._TaskRunningCount = None
        self._TotalTaskCount = None

    @property
    def TaskQueuedCount(self):
        return self._TaskQueuedCount

    @TaskQueuedCount.setter
    def TaskQueuedCount(self, TaskQueuedCount):
        self._TaskQueuedCount = TaskQueuedCount

    @property
    def TaskInitCount(self):
        return self._TaskInitCount

    @TaskInitCount.setter
    def TaskInitCount(self, TaskInitCount):
        self._TaskInitCount = TaskInitCount

    @property
    def TaskRunningCount(self):
        return self._TaskRunningCount

    @TaskRunningCount.setter
    def TaskRunningCount(self, TaskRunningCount):
        self._TaskRunningCount = TaskRunningCount

    @property
    def TotalTaskCount(self):
        return self._TotalTaskCount

    @TotalTaskCount.setter
    def TotalTaskCount(self, TotalTaskCount):
        self._TotalTaskCount = TotalTaskCount


    def _deserialize(self, params):
        self._TaskQueuedCount = params.get("TaskQueuedCount")
        self._TaskInitCount = params.get("TaskInitCount")
        self._TaskRunningCount = params.get("TaskRunningCount")
        self._TotalTaskCount = params.get("TotalTaskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRowFilterRequest(AbstractModel):
    """UpdateRowFilter request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: The ID of the row filter policy, which can be obtained using the `DescribeUserInfo` or `DescribeWorkGroupInfo` API.
        :type PolicyId: int
        :param _Policy: The new filter policy.
        :type Policy: :class:`tencentcloud.dlc.v20210125.models.Policy`
        """
        self._PolicyId = None
        self._Policy = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        if params.get("Policy") is not None:
            self._Policy = Policy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRowFilterResponse(AbstractModel):
    """UpdateRowFilter response structure.

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