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


class CreateInput(AbstractModel):
    """Configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _InputName: Input name, which can contain 1 to 32 letters, digits, and underscores.
        :type InputName: str
        :param _Protocol: Input protocol. Valid values: `SRT`, `RTP`, `RTMP`
        :type Protocol: str
        :param _Description: Input description. Length: [0, 255].
        :type Description: str
        :param _AllowIpList: Allowlist of input IPs in CIDR format.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: RTP configuration information of input.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _FailOver: Input failover. Valid values: `OPEN`, `CLOSE` (default)
        :type FailOver: str
        """
        self._InputName = None
        self._Protocol = None
        self._Description = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._FailOver = None

    @property
    def InputName(self):
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver


    def _deserialize(self, params):
        self._InputName = params.get("InputName")
        self._Protocol = params.get("Protocol")
        self._Description = params.get("Description")
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTPSettings(AbstractModel):
    """RTP configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _FEC: Default value: none. Valid values: ['none'].
        :type FEC: str
        :param _IdleTimeout: Idle timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputSRTSettings(AbstractModel):
    """SRT configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _Mode: The SRT mode. Valid values: LISTENER (default), CALLER.
        :type Mode: str
        :param _StreamId: Stream ID, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param _Latency: Latency in ms. Default value: 0. Value range: [0, 3000].
        :type Latency: int
        :param _RecvLatency: Receive latency in ms. Default value: 120. Value range: [0, 3000].
        :type RecvLatency: int
        :param _PeerLatency: Peer latency in ms. Default value: 0. Value range: [0, 3000].
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key, which is empty by default, indicating not to encrypt. Only ASCII codes can be filled. Length: [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: Key length. Default value: 0. Valid values: 0, 16, 24, 32.
        :type PbKeyLen: int
        :param _SourceAddresses: The SRT peer address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type SourceAddresses: list of SRTSourceAddressReq
        """
        self._Mode = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._SourceAddresses = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressReq()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfo(AbstractModel):
    """The information of the output to create.

    """

    def __init__(self):
        r"""
        :param _OutputName: The output name.
        :type OutputName: str
        :param _Description: Description of the output.
        :type Description: str
        :param _Protocol: The output protocol. Valid values: SRT, RTP, RTMP, RTMP_PULL.
        :type Protocol: str
        :param _OutputRegion: The output region.
        :type OutputRegion: str
        :param _SRTSettings: The SRT configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTMPSettings: The RTMP configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _RTPSettings: The RTP configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _AllowIpList: The IP allowlist. The address must be in CIDR format, such as `0.0.0.0/0`.
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If it is left empty, there is no restriction on clients’ IP addresses.
        :type AllowIpList: list of str
        """
        self._OutputName = None
        self._Description = None
        self._Protocol = None
        self._OutputRegion = None
        self._SRTSettings = None
        self._RTMPSettings = None
        self._RTPSettings = None
        self._AllowIpList = None

    @property
    def OutputName(self):
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputRegion(self):
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTMPSettings(self):
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList


    def _deserialize(self, params):
        self._OutputName = params.get("OutputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        self._OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateOutputSrtSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = CreateOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateOutputInfoRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfoRTPSettings(AbstractModel):
    """The RTP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRTPSettingsDestinations
        :param _FEC: This parameter must be set to `none`.
        :type FEC: str
        :param _IdleTimeout: The timeout period (ms).
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRTPSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTMPSettings(AbstractModel):
    """The RTMP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param _ChunkSize: The RTMP chunk size. Value range: [4096, 40960].
        :type ChunkSize: int
        """
        self._Destinations = None
        self._ChunkSize = None

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def ChunkSize(self):
        return self._ChunkSize

    @ChunkSize.setter
    def ChunkSize(self, ChunkSize):
        self._ChunkSize = ChunkSize


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRtmpSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._ChunkSize = params.get("ChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTPSettingsDestinations(AbstractModel):
    """The RTP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Ip: The relay destination IP.
        :type Ip: str
        :param _Port: The relay destination port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    """The RTMP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Url: The relay URL. Format: `rtmp://domain/live`.
        :type Url: str
        :param _StreamKey: The `StreamKey` for relay. Format: `stream?key=value`.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettings(AbstractModel):
    """The SRT configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type Destinations: list of CreateOutputSrtSettingsDestinations
        :param _StreamId: The stream ID for relay, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param _Latency: The total latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type Latency: int
        :param _RecvLatency: The receive latency (ms) of SRT relay. Value range: [0, 3000]. Default: 120.
        :type RecvLatency: int
        :param _PeerLatency: The peer-to-peer latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type PeerLatency: int
        :param _PeerIdleTimeout: The timeout period (ms) for the SRT relay peer. Value range: [1000, 10000]. Default: 5000.
        :type PeerIdleTimeout: int
        :param _Passphrase: The encryption key for SRT relay, which is empty by default, indicating not to encrypt. Only ASCII codes are allowed. Length: [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: The key length for SRT relay. Valid values: 0 (default), 16, 24, 32.
        :type PbKeyLen: int
        :param _Mode: The SRT mode. Valid values: LISTENER, CALLER (default).
        :type Mode: str
        """
        self._Destinations = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._Mode = None

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputSrtSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettingsDestinations(AbstractModel):
    """The SRT destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Ip: The output IP.
        :type Ip: str
        :param _Port: The output port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowRequest(AbstractModel):
    """CreateStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowName: Flow name
        :type FlowName: str
        :param _MaxBandwidth: Maximum bandwidth in bps. Valid values: `10000000`, `20000000`, `50000000`
        :type MaxBandwidth: int
        :param _InputGroup: Flow input group
        :type InputGroup: list of CreateInput
        """
        self._FlowName = None
        self._MaxBandwidth = None
        self._InputGroup = None

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self._InputGroup = []
            for item in params.get("InputGroup"):
                obj = CreateInput()
                obj._deserialize(item)
                self._InputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowResponse(AbstractModel):
    """CreateStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Information of the created flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkOutputInfoRequest(AbstractModel):
    """CreateStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Output: The output configuration of the flow.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self._Output = CreateOutputInfo()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkOutputInfoResponse(AbstractModel):
    """CreateStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The information of the created output.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DeleteStreamLinkFlowRequest(AbstractModel):
    """DeleteStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkFlowResponse(AbstractModel):
    """DeleteStreamLinkFlow response structure.

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


class DeleteStreamLinkOutputRequest(AbstractModel):
    """DeleteStreamLinkOutput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        :param _OutputId: Output ID
        :type OutputId: str
        """
        self._FlowId = None
        self._OutputId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def OutputId(self):
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._OutputId = params.get("OutputId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkOutputResponse(AbstractModel):
    """DeleteStreamLinkOutput response structure.

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


class DescribeFlow(AbstractModel):
    """Configuration information of the queried flow.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID.
        :type FlowId: str
        :param _FlowName: Flow name.
        :type FlowName: str
        :param _State: Flow status. Valid values: `IDLE`, `RUNNING`
        :type State: str
        :param _MaxBandwidth: Maximum bandwidth value.
        :type MaxBandwidth: int
        :param _InputGroup: Input group.
        :type InputGroup: list of DescribeInput
        :param _OutputGroup: Output group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputGroup: list of DescribeOutput
        """
        self._FlowId = None
        self._FlowName = None
        self._State = None
        self._MaxBandwidth = None
        self._InputGroup = None
        self._OutputGroup = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup

    @property
    def OutputGroup(self):
        return self._OutputGroup

    @OutputGroup.setter
    def OutputGroup(self, OutputGroup):
        self._OutputGroup = OutputGroup


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._State = params.get("State")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self._InputGroup = []
            for item in params.get("InputGroup"):
                obj = DescribeInput()
                obj._deserialize(item)
                self._InputGroup.append(obj)
        if params.get("OutputGroup") is not None:
            self._OutputGroup = []
            for item in params.get("OutputGroup"):
                obj = DescribeOutput()
                obj._deserialize(item)
                self._OutputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInput(AbstractModel):
    """Configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _InputId: Input ID.
        :type InputId: str
        :param _InputName: Input name.
        :type InputName: str
        :param _Description: Input description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Protocol: Input protocol.
        :type Protocol: str
        :param _InputAddressList: Input address list.
        :type InputAddressList: list of InputAddress
        :param _AllowIpList: Input IP allowlist.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        :param _RTPSettings: RTP configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        :param _InputRegion: Input region.
        :type InputRegion: str
        :param _RTMPSettings: RTMP configuration information of an input
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        :param _FailOver: Input failover
Note: this field may return `null`, indicating that no valid value was found.
        :type FailOver: str
        """
        self._InputId = None
        self._InputName = None
        self._Description = None
        self._Protocol = None
        self._InputAddressList = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._InputRegion = None
        self._RTMPSettings = None
        self._FailOver = None

    @property
    def InputId(self):
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InputAddressList(self):
        return self._InputAddressList

    @InputAddressList.setter
    def InputAddressList(self, InputAddressList):
        self._InputAddressList = InputAddressList

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def InputRegion(self):
        return self._InputRegion

    @InputRegion.setter
    def InputRegion(self, InputRegion):
        self._InputRegion = InputRegion

    @property
    def RTMPSettings(self):
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver


    def _deserialize(self, params):
        self._InputId = params.get("InputId")
        self._InputName = params.get("InputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("InputAddressList") is not None:
            self._InputAddressList = []
            for item in params.get("InputAddressList"):
                obj = InputAddress()
                obj._deserialize(item)
                self._InputAddressList.append(obj)
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = DescribeInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = DescribeInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._InputRegion = params.get("InputRegion")
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = DescribeInputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        self._FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPSettings(AbstractModel):
    """RTMP configuration information of the queried input

    """

    def __init__(self):
        r"""
        :param _AppName: Path for RTMP stream pushing
Note: this field may return `null`, indicating that no valid value was found.
        :type AppName: str
        :param _StreamKey: StreamKey for RTMP stream pushing
Format of an RTMP stream pushing URL: rtmp://IP address:1935/AppName/StreamKey
        :type StreamKey: str
        """
        self._AppName = None
        self._StreamKey = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamKey(self):
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTPSettings(AbstractModel):
    """RTP configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _FEC: Whether it is FEC.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputSRTSettings(AbstractModel):
    """SRT configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _StreamId: Stream ID.
        :type StreamId: str
        :param _Latency: Latency.
        :type Latency: int
        :param _RecvLatency: Receive latency.
        :type RecvLatency: int
        :param _PeerLatency: Peer latency.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer idle timeout period.
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key.
        :type Passphrase: str
        :param _PbKeyLen: Key length.
        :type PbKeyLen: int
        :param _SourceAddresses: The SRT peer address.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of SRTSourceAddressResp
        """
        self._Mode = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._SourceAddresses = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressResp()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutput(AbstractModel):
    """Configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _OutputId: Output ID.
        :type OutputId: str
        :param _OutputName: Output name.
        :type OutputName: str
        :param _OutputType: Output type.
        :type OutputType: str
        :param _Description: Output description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Protocol: Output protocol.
        :type Protocol: str
        :param _OutputAddressList: Output destination address information list.
        :type OutputAddressList: list of OutputAddress
        :param _OutputRegion: Output region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputRegion: str
        :param _SRTSettings: SRT configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        :param _RTPSettings: RTP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        :param _RTMPSettings: RTMP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        :param _RTMPPullSettings: RTMP pull configuration of the output
Note: This field may return `null`, indicating that no valid value was found.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        :param _AllowIpList: CIDR allowlist
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If this parameter is left empty, there is no restriction on clients’ IP addresses.
Note: This field may return `null`, indicating that no valid value was found.
        :type AllowIpList: list of str
        """
        self._OutputId = None
        self._OutputName = None
        self._OutputType = None
        self._Description = None
        self._Protocol = None
        self._OutputAddressList = None
        self._OutputRegion = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._RTMPSettings = None
        self._RTMPPullSettings = None
        self._AllowIpList = None

    @property
    def OutputId(self):
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def OutputType(self):
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputAddressList(self):
        return self._OutputAddressList

    @OutputAddressList.setter
    def OutputAddressList(self, OutputAddressList):
        self._OutputAddressList = OutputAddressList

    @property
    def OutputRegion(self):
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTMPPullSettings(self):
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList


    def _deserialize(self, params):
        self._OutputId = params.get("OutputId")
        self._OutputName = params.get("OutputName")
        self._OutputType = params.get("OutputType")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("OutputAddressList") is not None:
            self._OutputAddressList = []
            for item in params.get("OutputAddressList"):
                obj = OutputAddress()
                obj._deserialize(item)
                self._OutputAddressList.append(obj)
        self._OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = DescribeOutputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = DescribeOutputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = DescribeOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTMPPullSettings") is not None:
            self._RTMPPullSettings = DescribeOutputRTMPPullSettings()
            self._RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        self._AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullServerUrl(AbstractModel):
    """RTMP pull URL of the output

    """

    def __init__(self):
        r"""
        :param _TcUrl: `tcUrl` of the RTMP pull URL
        :type TcUrl: str
        :param _StreamKey: Stream key of the RTMP pull URL
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._TcUrl = params.get("TcUrl")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullSettings(AbstractModel):
    """RTMP pull configuration of the output

    """

    def __init__(self):
        r"""
        :param _ServerUrls: List of pull URLs
Note: This field may return `null`, indicating that no valid value was found.
        :type ServerUrls: list of DescribeOutputRTMPPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        return self._ServerUrls

    @ServerUrls.setter
    def ServerUrls(self, ServerUrls):
        self._ServerUrls = ServerUrls


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self._ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTMPPullServerUrl()
                obj._deserialize(item)
                self._ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPSettings(AbstractModel):
    """RTMP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        :param _ChunkSize: Chunk size.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChunkSize: int
        :param _Destinations: Destination address information list of RTMP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTMPAddressDestination
        """
        self._IdleTimeout = None
        self._ChunkSize = None
        self._Destinations = None

    @property
    def IdleTimeout(self):
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ChunkSize(self):
        return self._ChunkSize

    @ChunkSize.setter
    def ChunkSize(self, ChunkSize):
        self._ChunkSize = ChunkSize

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations


    def _deserialize(self, params):
        self._IdleTimeout = params.get("IdleTimeout")
        self._ChunkSize = params.get("ChunkSize")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = RTMPAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTPSettings(AbstractModel):
    """RTP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _Destinations: Destination address information list of RTP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTPAddressDestination
        :param _FEC: Whether it is FEC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = RTPAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputSRTSettings(AbstractModel):
    """SRT configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _Destinations: A list of the destination addresses for relay. This parameter is valid if `Mode` is `CALLER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Destinations: list of SRTAddressDestination
        :param _StreamId: Stream ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamId: str
        :param _Latency: Latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Latency: int
        :param _RecvLatency: Receive latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecvLatency: int
        :param _PeerLatency: Peer latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerIdleTimeout: int
        :param _Passphrase: Encryption key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Passphrase: str
        :param _PbKeyLen: Encryption key length.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PbKeyLen: int
        :param _Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _SourceAddresses: The server’s listen address, which is valid if `Mode` is `LISTENER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of OutputSRTSourceAddressResp
        """
        self._Destinations = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._Mode = None
        self._SourceAddresses = None

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SourceAddresses(self):
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = SRTAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        self._Mode = params.get("Mode")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = OutputSRTSourceAddressResp()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsRequest(AbstractModel):
    """DescribeStreamLinkFlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: list of str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: list of str
        :param _PageSize: The page size. Value range: [1, 1000]. Default: 100.
        :type PageSize: int
        :param _SortType: Whether to sort the records by timestamp in descending or ascending order. Valid values: desc (default), asc.
        :type SortType: str
        :param _PageNum: The page number. Value range: [1, 1000]. Default: 1.
        :type PageNum: int
        """
        self._FlowId = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Pipeline = None
        self._PageSize = None
        self._SortType = None
        self._PageNum = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortType(self):
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Pipeline = params.get("Pipeline")
        self._PageSize = params.get("PageSize")
        self._SortType = params.get("SortType")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsResponse(AbstractModel):
    """DescribeStreamLinkFlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the logs.
        :type Infos: list of FlowLogInfo
        :param _PageNum: The current page number.
        :type PageNum: int
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _TotalNum: The total number of records.
        :type TotalNum: int
        :param _TotalPage: The total number of pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowLogInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowMediaStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowMediaStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the media data.
        :type Infos: list of FlowMediaInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowMediaInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRealtimeStatusRequest(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _InputIds: The IDs of the inputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type InputIds: list of str
        :param _OutputIds: The IDs of the outputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type OutputIds: list of str
        """
        self._FlowId = None
        self._InputIds = None
        self._OutputIds = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InputIds(self):
        return self._InputIds

    @InputIds.setter
    def InputIds(self, InputIds):
        self._InputIds = InputIds

    @property
    def OutputIds(self):
        return self._OutputIds

    @OutputIds.setter
    def OutputIds(self, OutputIds):
        self._OutputIds = OutputIds


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InputIds = params.get("InputIds")
        self._OutputIds = params.get("OutputIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowRealtimeStatusResponse(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds) of the query.
        :type Timestamp: int
        :param _Datas: A list of the real-time data.
        :type Datas: list of FlowRealtimeStatusItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Timestamp = None
        self._Datas = None
        self._RequestId = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Datas(self):
        return self._Datas

    @Datas.setter
    def Datas(self, Datas):
        self._Datas = Datas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("Datas") is not None:
            self._Datas = []
            for item in params.get("Datas"):
                obj = FlowRealtimeStatusItem()
                obj._deserialize(item)
                self._Datas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRequest(AbstractModel):
    """DescribeStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowResponse(AbstractModel):
    """DescribeStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Configuration information of a flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowSRTStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

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
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowSRTStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the SRT streaming performance data.
        :type Infos: list of FlowSRTInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowSRTInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the media data.
        :type Infos: list of FlowStatisticsArray
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowStatisticsArray()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowsRequest(AbstractModel):
    """DescribeStreamLinkFlows request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Number of the current page. Default value: `1`
        :type PageNum: int
        :param _PageSize: Number of entries per page. Default value: `10`
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowsResponse(AbstractModel):
    """DescribeStreamLinkFlows response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of the configuration information of the flows
        :type Infos: list of DescribeFlow
        :param _PageNum: Number of the current page
        :type PageNum: int
        :param _PageSize: Number of entries per page
        :type PageSize: int
        :param _TotalNum: Total number of entries
        :type TotalNum: int
        :param _TotalPage: Total number of pages
        :type TotalPage: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DescribeFlow()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkRegionsRequest(AbstractModel):
    """DescribeStreamLinkRegions request structure.

    """


class DescribeStreamLinkRegionsResponse(AbstractModel):
    """DescribeStreamLinkRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Info: StreamLink region information
        :type Info: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = StreamLinkRegionInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class FlowAudio(AbstractModel):
    """The audio data of the flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowLogInfo(AbstractModel):
    """The logs of a flow.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _Type: Whether it is an input or output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Protocol: The protocol.
        :type Protocol: str
        :param _EventCode: The event code.
        :type EventCode: str
        :param _EventMessage: The event information.
        :type EventMessage: str
        :param _RemoteIp: The peer IP.
        :type RemoteIp: str
        :param _RemotePort: The peer port.
        :type RemotePort: str
        :param _Pipeline: Whether it is a primary or backup pipeline. Valid values: 0 (primary), 1 (backup).
        :type Pipeline: str
        :param _InputOutputName: The input or output name.
        :type InputOutputName: str
        """
        self._Timestamp = None
        self._Type = None
        self._InputOutputId = None
        self._Protocol = None
        self._EventCode = None
        self._EventMessage = None
        self._RemoteIp = None
        self._RemotePort = None
        self._Pipeline = None
        self._InputOutputName = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def EventCode(self):
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventMessage(self):
        return self._EventMessage

    @EventMessage.setter
    def EventMessage(self, EventMessage):
        self._EventMessage = EventMessage

    @property
    def RemoteIp(self):
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp

    @property
    def RemotePort(self):
        return self._RemotePort

    @RemotePort.setter
    def RemotePort(self, RemotePort):
        self._RemotePort = RemotePort

    @property
    def Pipeline(self):
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def InputOutputName(self):
        return self._InputOutputName

    @InputOutputName.setter
    def InputOutputName(self, InputOutputName):
        self._InputOutputName = InputOutputName


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Protocol = params.get("Protocol")
        self._EventCode = params.get("EventCode")
        self._EventMessage = params.get("EventMessage")
        self._RemoteIp = params.get("RemoteIp")
        self._RemotePort = params.get("RemotePort")
        self._Pipeline = params.get("Pipeline")
        self._InputOutputName = params.get("InputOutputName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaAudio(AbstractModel):
    """The audio data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaInfo(AbstractModel):
    """The media data of a flow.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _Network: The total bandwidth.
        :type Network: int
        :param _Video: The video data of the flow.
        :type Video: list of FlowMediaVideo
        :param _Audio: The audio data of the flow.
        :type Audio: list of FlowMediaAudio
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        :param _ClientIp: The client IP.
        :type ClientIp: str
        """
        self._Timestamp = None
        self._Network = None
        self._Video = None
        self._Audio = None
        self._SessionId = None
        self._ClientIp = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Network = params.get("Network")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = FlowMediaVideo()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = FlowMediaAudio()
                obj._deserialize(item)
                self._Audio.append(obj)
        self._SessionId = params.get("SessionId")
        self._ClientIp = params.get("ClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaVideo(AbstractModel):
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The video PID.
        :type Pid: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusCommon(AbstractModel):
    """The common real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param _State: The connection status. Valid values: Connected, Waiting, Idle.
        :type State: str
        :param _Mode: The connection mode. Valid values: Listener, Caller.
        :type Mode: str
        :param _ConnectedTime: The connected time.
        :type ConnectedTime: int
        :param _Bitrate: The real-time bitrate (bps).
        :type Bitrate: int
        :param _Reconnections: The number of retries.
        :type Reconnections: int
        """
        self._State = None
        self._Mode = None
        self._ConnectedTime = None
        self._Bitrate = None
        self._Reconnections = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ConnectedTime(self):
        return self._ConnectedTime

    @ConnectedTime.setter
    def ConnectedTime(self, ConnectedTime):
        self._ConnectedTime = ConnectedTime

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Reconnections(self):
        return self._Reconnections

    @Reconnections.setter
    def Reconnections(self, Reconnections):
        self._Reconnections = Reconnections


    def _deserialize(self, params):
        self._State = params.get("State")
        self._Mode = params.get("Mode")
        self._ConnectedTime = params.get("ConnectedTime")
        self._Bitrate = params.get("Bitrate")
        self._Reconnections = params.get("Reconnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusItem(AbstractModel):
    """The real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param _Type: Whether it is an input or output. Valid values: Input, Output.
        :type Type: str
        :param _InputId: The input ID, which is not empty if `Type` is `Input`.
        :type InputId: str
        :param _OutputId: The output ID, which is not empty if `Type` is `Output`.
        :type OutputId: str
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Protocol: The protocol used. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param _CommonStatus: The common status information.
        :type CommonStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        :param _SRTStatus: This parameter is returned if `Protocol` is `SRT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SRTStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        :param _RTMPStatus: This parameter is returned if `Protocol` is `RTMP`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RTMPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        :param _ConnectServerIP: The server IP.
        :type ConnectServerIP: str
        :param _RTPStatus: This parameter is returned if the RTP protocol is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RTPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTP`
        """
        self._Type = None
        self._InputId = None
        self._OutputId = None
        self._FlowId = None
        self._Protocol = None
        self._CommonStatus = None
        self._SRTStatus = None
        self._RTMPStatus = None
        self._ConnectServerIP = None
        self._RTPStatus = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputId(self):
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def OutputId(self):
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CommonStatus(self):
        return self._CommonStatus

    @CommonStatus.setter
    def CommonStatus(self, CommonStatus):
        self._CommonStatus = CommonStatus

    @property
    def SRTStatus(self):
        return self._SRTStatus

    @SRTStatus.setter
    def SRTStatus(self, SRTStatus):
        self._SRTStatus = SRTStatus

    @property
    def RTMPStatus(self):
        return self._RTMPStatus

    @RTMPStatus.setter
    def RTMPStatus(self, RTMPStatus):
        self._RTMPStatus = RTMPStatus

    @property
    def ConnectServerIP(self):
        return self._ConnectServerIP

    @ConnectServerIP.setter
    def ConnectServerIP(self, ConnectServerIP):
        self._ConnectServerIP = ConnectServerIP

    @property
    def RTPStatus(self):
        return self._RTPStatus

    @RTPStatus.setter
    def RTPStatus(self, RTPStatus):
        self._RTPStatus = RTPStatus


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InputId = params.get("InputId")
        self._OutputId = params.get("OutputId")
        self._FlowId = params.get("FlowId")
        self._Protocol = params.get("Protocol")
        if params.get("CommonStatus") is not None:
            self._CommonStatus = FlowRealtimeStatusCommon()
            self._CommonStatus._deserialize(params.get("CommonStatus"))
        if params.get("SRTStatus") is not None:
            self._SRTStatus = FlowRealtimeStatusSRT()
            self._SRTStatus._deserialize(params.get("SRTStatus"))
        if params.get("RTMPStatus") is not None:
            self._RTMPStatus = FlowRealtimeStatusRTMP()
            self._RTMPStatus._deserialize(params.get("RTMPStatus"))
        self._ConnectServerIP = params.get("ConnectServerIP")
        if params.get("RTPStatus") is not None:
            self._RTPStatus = FlowRealtimeStatusRTP()
            self._RTPStatus._deserialize(params.get("RTPStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTMP(AbstractModel):
    """The real-time RTMP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _VideoFPS: The video frame rate.
        :type VideoFPS: int
        :param _AudioFPS: The audio frame rate.
        :type AudioFPS: int
        """
        self._VideoFPS = None
        self._AudioFPS = None

    @property
    def VideoFPS(self):
        return self._VideoFPS

    @VideoFPS.setter
    def VideoFPS(self, VideoFPS):
        self._VideoFPS = VideoFPS

    @property
    def AudioFPS(self):
        return self._AudioFPS

    @AudioFPS.setter
    def AudioFPS(self, AudioFPS):
        self._AudioFPS = AudioFPS


    def _deserialize(self, params):
        self._VideoFPS = params.get("VideoFPS")
        self._AudioFPS = params.get("AudioFPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTP(AbstractModel):
    """The real-time RTP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _Packets: The number of packets transmitted.
        :type Packets: int
        """
        self._Packets = None

    @property
    def Packets(self):
        return self._Packets

    @Packets.setter
    def Packets(self, Packets):
        self._Packets = Packets


    def _deserialize(self, params):
        self._Packets = params.get("Packets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusSRT(AbstractModel):
    """The real-time SRT streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _Latency: The latency (ms).
        :type Latency: int
        :param _RTT: RTT (ms).
        :type RTT: int
        :param _Packets: The number of packets sent or received.
        :type Packets: int
        :param _PacketLossRate: The packet loss rate.
        :type PacketLossRate: float
        :param _RetransmitRate: The retransmission rate.
        :type RetransmitRate: float
        :param _DroppedPackets: The number of packets dropped.
        :type DroppedPackets: int
        :param _Encryption: Whether to encrypt the stream. Valid values: On, Off.
        :type Encryption: str
        """
        self._Latency = None
        self._RTT = None
        self._Packets = None
        self._PacketLossRate = None
        self._RetransmitRate = None
        self._DroppedPackets = None
        self._Encryption = None

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RTT(self):
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def Packets(self):
        return self._Packets

    @Packets.setter
    def Packets(self, Packets):
        self._Packets = Packets

    @property
    def PacketLossRate(self):
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def RetransmitRate(self):
        return self._RetransmitRate

    @RetransmitRate.setter
    def RetransmitRate(self, RetransmitRate):
        self._RetransmitRate = RetransmitRate

    @property
    def DroppedPackets(self):
        return self._DroppedPackets

    @DroppedPackets.setter
    def DroppedPackets(self, DroppedPackets):
        self._DroppedPackets = DroppedPackets

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Latency = params.get("Latency")
        self._RTT = params.get("RTT")
        self._Packets = params.get("Packets")
        self._PacketLossRate = params.get("PacketLossRate")
        self._RetransmitRate = params.get("RetransmitRate")
        self._DroppedPackets = params.get("DroppedPackets")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowSRTInfo(AbstractModel):
    """The SRT streaming performance data.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _SendPacketLossRate: The packet loss rate for sending.
        :type SendPacketLossRate: int
        :param _SendRetransmissionRate: The retry rate for sending.
        :type SendRetransmissionRate: int
        :param _RecvPacketLossRate: The packet loss rate for receiving.
        :type RecvPacketLossRate: int
        :param _RecvRetransmissionRate: The retry rate for receiving.
        :type RecvRetransmissionRate: int
        :param _RTT: The peer RTT.
        :type RTT: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        :param _SendPacketDropNumber: The number of dropped packets for sending.
        :type SendPacketDropNumber: int
        :param _RecvPacketDropNumber: The number of dropped packets for receiving.
        :type RecvPacketDropNumber: int
        """
        self._Timestamp = None
        self._SendPacketLossRate = None
        self._SendRetransmissionRate = None
        self._RecvPacketLossRate = None
        self._RecvRetransmissionRate = None
        self._RTT = None
        self._SessionId = None
        self._SendPacketDropNumber = None
        self._RecvPacketDropNumber = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SendPacketLossRate(self):
        return self._SendPacketLossRate

    @SendPacketLossRate.setter
    def SendPacketLossRate(self, SendPacketLossRate):
        self._SendPacketLossRate = SendPacketLossRate

    @property
    def SendRetransmissionRate(self):
        return self._SendRetransmissionRate

    @SendRetransmissionRate.setter
    def SendRetransmissionRate(self, SendRetransmissionRate):
        self._SendRetransmissionRate = SendRetransmissionRate

    @property
    def RecvPacketLossRate(self):
        return self._RecvPacketLossRate

    @RecvPacketLossRate.setter
    def RecvPacketLossRate(self, RecvPacketLossRate):
        self._RecvPacketLossRate = RecvPacketLossRate

    @property
    def RecvRetransmissionRate(self):
        return self._RecvRetransmissionRate

    @RecvRetransmissionRate.setter
    def RecvRetransmissionRate(self, RecvRetransmissionRate):
        self._RecvRetransmissionRate = RecvRetransmissionRate

    @property
    def RTT(self):
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SendPacketDropNumber(self):
        return self._SendPacketDropNumber

    @SendPacketDropNumber.setter
    def SendPacketDropNumber(self, SendPacketDropNumber):
        self._SendPacketDropNumber = SendPacketDropNumber

    @property
    def RecvPacketDropNumber(self):
        return self._RecvPacketDropNumber

    @RecvPacketDropNumber.setter
    def RecvPacketDropNumber(self, RecvPacketDropNumber):
        self._RecvPacketDropNumber = RecvPacketDropNumber


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._SendPacketLossRate = params.get("SendPacketLossRate")
        self._SendRetransmissionRate = params.get("SendRetransmissionRate")
        self._RecvPacketLossRate = params.get("RecvPacketLossRate")
        self._RecvRetransmissionRate = params.get("RecvRetransmissionRate")
        self._RTT = params.get("RTT")
        self._SessionId = params.get("SessionId")
        self._SendPacketDropNumber = params.get("SendPacketDropNumber")
        self._RecvPacketDropNumber = params.get("RecvPacketDropNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatistics(AbstractModel):
    """The flow statistics.

    """

    def __init__(self):
        r"""
        :param _SessionId: The session ID.
        :type SessionId: str
        :param _ClientIp: The peer IP.
        :type ClientIp: str
        :param _Network: The total bandwidth.
        :type Network: int
        :param _Video: The video data.
        :type Video: list of FlowVideo
        :param _Audio: The audio data.
        :type Audio: list of FlowAudio
        """
        self._SessionId = None
        self._ClientIp = None
        self._Network = None
        self._Video = None
        self._Audio = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Network(self):
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._ClientIp = params.get("ClientIp")
        self._Network = params.get("Network")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = FlowVideo()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = FlowAudio()
                obj._deserialize(item)
                self._Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatisticsArray(AbstractModel):
    """A list of the flow statistics.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp.
        :type Timestamp: int
        :param _FlowStatistics: The statistics of all the sessions.
        :type FlowStatistics: list of FlowStatistics
        """
        self._Timestamp = None
        self._FlowStatistics = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FlowStatistics(self):
        return self._FlowStatistics

    @FlowStatistics.setter
    def FlowStatistics(self, FlowStatistics):
        self._FlowStatistics = FlowStatistics


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("FlowStatistics") is not None:
            self._FlowStatistics = []
            for item in params.get("FlowStatistics"):
                obj = FlowStatistics()
                obj._deserialize(item)
                self._FlowStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowVideo(AbstractModel):
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAddress(AbstractModel):
    """Input address information.

    """

    def __init__(self):
        r"""
        :param _Ip: Input address IP.
        :type Ip: str
        :param _Port: Input address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInput(AbstractModel):
    """The new input configuration.

    """

    def __init__(self):
        r"""
        :param _InputId: The input ID.
        :type InputId: str
        :param _InputName: The input name.
        :type InputName: str
        :param _Description: The description of the input.
        :type Description: str
        :param _AllowIpList: The IP addresses (CIDR) allowed to push streams.
        :type AllowIpList: list of str
        :param _SRTSettings: The SRT configuration information.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: The RTP configuration information.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _Protocol: The input protocol. Valid values: SRT, RTP, RTMP.
If there is an RTP input, the output must be RTP.
If there is an RTMP input, the output must be SRT or RTMP.
If there is an SRT input, the output must be SRT.
        :type Protocol: str
        :param _FailOver: Whether to enable input failover. Valid values: OPEN, CLOSE.
        :type FailOver: str
        """
        self._InputId = None
        self._InputName = None
        self._Description = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._Protocol = None
        self._FailOver = None

    @property
    def InputId(self):
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FailOver(self):
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver


    def _deserialize(self, params):
        self._InputId = params.get("InputId")
        self._InputName = params.get("InputName")
        self._Description = params.get("Description")
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._Protocol = params.get("Protocol")
        self._FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOutputInfo(AbstractModel):
    """The new output configuration.

    """

    def __init__(self):
        r"""
        :param _OutputId: The ID of the output to modify.
        :type OutputId: str
        :param _OutputName: The output name.
        :type OutputName: str
        :param _Description: The description of the output.
        :type Description: str
        :param _Protocol: The output protocol. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param _SRTSettings: The SRT relay configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTPSettings: The RTP relay configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _RTMPSettings: The RTMP relay configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _AllowIpList: The IP allowlist. The address must be in CIDR format, such as `0.0.0.0/0`.
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If it is left empty, there is no restriction on clients’ IP addresses.
        :type AllowIpList: list of str
        """
        self._OutputId = None
        self._OutputName = None
        self._Description = None
        self._Protocol = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._RTMPSettings = None
        self._AllowIpList = None

    @property
    def OutputId(self):
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SRTSettings(self):
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def AllowIpList(self):
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList


    def _deserialize(self, params):
        self._OutputId = params.get("OutputId")
        self._OutputName = params.get("OutputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateOutputSrtSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateOutputInfoRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = CreateOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        self._AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowRequest(AbstractModel):
    """ModifyStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        :param _FlowName: Name of the flow to modify
        :type FlowName: str
        """
        self._FlowId = None
        self._FlowName = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowResponse(AbstractModel):
    """ModifyStreamLinkFlow response structure.

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


class ModifyStreamLinkInputRequest(AbstractModel):
    """ModifyStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Input: The input information to modify.
        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        self._FlowId = None
        self._Input = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Input") is not None:
            self._Input = ModifyInput()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkInputResponse(AbstractModel):
    """ModifyStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The input information after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = DescribeInput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class ModifyStreamLinkOutputInfoRequest(AbstractModel):
    """ModifyStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Output: The output configuration to modify.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self._Output = ModifyOutputInfo()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkOutputInfoResponse(AbstractModel):
    """ModifyStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The output configuration after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

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
        if params.get("Info") is not None:
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class OutputAddress(AbstractModel):
    """Output destination address.

    """

    def __init__(self):
        r"""
        :param _Ip: Output destination IP.
        :type Ip: str
        """
        self._Ip = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputSRTSourceAddressResp(AbstractModel):
    """The listen address for an SRT output.

    """

    def __init__(self):
        r"""
        :param _Ip: The listen IP.
        :type Ip: str
        :param _Port: The listen port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPAddressDestination(AbstractModel):
    """Destination address information of RTMP push.

    """

    def __init__(self):
        r"""
        :param _Url: Destination URL of RTMP push in the format of 'rtmp://domain/live'.
        :type Url: str
        :param _StreamKey: Destination `StreamKey` of RTMP push in the format of 'streamid?key=value'.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTPAddressDestination(AbstractModel):
    """Destination address information of RTP push.

    """

    def __init__(self):
        r"""
        :param _Ip: Push destination address IP.
        :type Ip: str
        :param _Port: Push destination address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _Name: Region name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTAddressDestination(AbstractModel):
    """Push destination address information.

    """

    def __init__(self):
        r"""
        :param _Ip: Destination address IP.
        :type Ip: str
        :param _Port: Destination address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressReq(AbstractModel):
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param _Ip: The peer IP.
        :type Ip: str
        :param _Port: The peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressResp(AbstractModel):
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param _Ip: The peer IP.
        :type Ip: str
        :param _Port: The peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowRequest(AbstractModel):
    """StartStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowResponse(AbstractModel):
    """StartStreamLinkFlow response structure.

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


class StopStreamLinkFlowRequest(AbstractModel):
    """StopStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLinkFlowResponse(AbstractModel):
    """StopStreamLinkFlow response structure.

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


class StreamLinkRegionInfo(AbstractModel):
    """StreamLink region information

    """

    def __init__(self):
        r"""
        :param _Regions: List of StreamLink regions
        :type Regions: list of RegionInfo
        """
        self._Regions = None

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        