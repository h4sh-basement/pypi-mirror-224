import math
import re
from datetime import datetime
from enum import Enum, unique
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from data_aggregator_sdk.constants.enums import SignalModulation, DownlinkTaskType
from data_aggregator_sdk.integration_message import IntegrationV0MessageMeta, IntegrationV0MessageMetaBSChannelProtocol, \
    IntegrationV0MessageMetaBSHttp
from pydantic import BaseModel, Extra, validator

from data_gateway_sdk.errors import DataGatewayBSProtocolParsingError
from data_gateway_sdk.protocols.nero_bs_packet.nero_bs_packet import NeroBsPacket


def hex_is_valid(value: str, hex_length: int = 0) -> bool:
    if hex_length == 0:
        if len(value) % 2 == 0 and re.fullmatch("^#?([A-Fa-f0-9]+)$", value):
            return True
        return False
    else:
        if re.fullmatch("^#?([A-Fa-f0-9]{" + str(hex_length * 2) + "})$", value):
            return True
        return False


class DataNbfi(BaseModel):
    mac: int
    f_ask: bool
    iterator: int
    multi: bool
    system: bool
    payload: str

    @validator('mac')
    def validate_mac(cls, value: int) -> int:
        if 0 <= value < math.pow(2, 32):
            return value
        else:
            raise ValueError(f'Mac must be in range (1, 2^32-1). {value} was given')

    @validator('iterator')
    def validate_iterator(cls, value: int) -> int:
        if 0 <= value < math.pow(2, 32):
            return value
        else:
            raise ValueError(f'Iterator must be in range (0, 2^32-1). {value} was given')

    @validator('payload')
    def validate_payload(cls, value: str) -> str:
        if hex_is_valid(value, 8):
            return value
        else:
            raise ValueError(f'Payload is not a valid HEX. {value} was given')


class DataUnbp(BaseModel):
    mac: int
    ack: bool
    iterator: int
    payload: str

    @validator('mac')
    def validate_mac(cls, value: int) -> int:
        if 0 <= value < math.pow(2, 32):
            return value
        else:
            raise ValueError(f'Mac must be in range (1, 2^32-1). {value} was given')

    @validator('iterator')
    def validate_iterator(cls, value: int) -> int:
        if 0 <= value < math.pow(2, 32):
            return value
        else:
            raise ValueError(f'Iterator must be in range (0, 2^32-1). {value} was given')

    @validator('payload')
    def validate_payload(cls, value: str) -> str:
        if hex_is_valid(value, 4) or hex_is_valid(value, 16) or hex_is_valid(value, 24):  # noqa: E501
            return value
        else:
            raise ValueError(f'Payload is not a valid HEX. {value} was given')


class SdrInfo(BaseModel):
    freq: int
    freq_channel: int
    sdr: int
    baud_rate: int
    rssi: int
    snr: int

    class Config:
        extra = Extra.allow

    @validator('freq')
    def validate_freq(cls, value: int) -> int:
        if value >= 0:
            return value
        else:
            raise ValueError(f'Freq must be more than 0. {value} was given')

    @validator('freq_channel', 'baud_rate')
    def validate_baud_rate(cls, value: int) -> int:
        if value >= 0:
            return value
        else:
            raise ValueError(f'Freq cannot be less than 0. {value} was given')


@unique
class DevicePackageNetworkTypeEnum(Enum):
    downlink = 'downlink'
    uplink = 'uplink'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


@unique
class DevicePackageProtocolTypeEnum(Enum):
    none = 'none'
    nbfi = 'nbfi'
    unbp = 'unbp'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


@unique
class DModEnum(Enum):
    DBPSK = 'DBPSK'
    FSK = 'FSK'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DevicePackage(BaseModel):
    footprint: Optional[str] = None
    dt: datetime
    raw: str
    data_nbfi: Optional[DataNbfi]
    data_unbp: Optional[DataUnbp]
    sdr_info: Optional[SdrInfo]
    type: DevicePackageNetworkTypeEnum
    protocol: DevicePackageProtocolTypeEnum
    message_id: Optional[int] = None

    @property
    def payload_bytes(self) -> bytes:
        if self.protocol is DevicePackageProtocolTypeEnum.unbp:
            assert self.data_unbp
            return bytes.fromhex(self.data_unbp.payload)
        if self.protocol is DevicePackageProtocolTypeEnum.nbfi:
            assert self.data_nbfi
            return bytes.fromhex(self.data_nbfi.payload)
        raise NotImplementedError(f'not implemented for protocol "{self.type.name}"')

    @property
    def mac(self) -> int:
        if self.protocol is DevicePackageProtocolTypeEnum.unbp:
            assert self.data_unbp
            return self.data_unbp.mac
        if self.protocol is DevicePackageProtocolTypeEnum.nbfi:
            assert self.data_nbfi
            return self.data_nbfi.mac
        raise NotImplementedError(f'not implemented for protocol "{self.type.name}"')

    class Config:
        extra = Extra.allow

    @validator('raw')
    def validate_payload(cls, value: str) -> str:
        if hex_is_valid(value):
            return value
        else:
            raise ValueError('Payload is not a valid HEX')

    @validator('protocol', pre=True)
    def validate_protocol(cls, value: Union[str, DevicePackageProtocolTypeEnum], values: Dict[str, Any]) -> DevicePackageProtocolTypeEnum:
        if value == DevicePackageProtocolTypeEnum.unbp.value or value is DevicePackageProtocolTypeEnum.unbp:
            if values.get("data_nbfi", None) is not None:
                raise ValueError(f'data_nbfi for protocol "{value}" must be None. "{type(values.get("data_nbfi", None)).__name__}" was given')
            if not isinstance(values.get('data_unbp', None), (dict, DataUnbp)):
                raise ValueError(f'data_unbp for protocol "{value}" must be dict. "{type(values.get("data_unbp", None)).__name__}" was given')
            if isinstance(value, str):
                return DevicePackageProtocolTypeEnum(value)
            return value
        if value == DevicePackageProtocolTypeEnum.nbfi.value or value is DevicePackageProtocolTypeEnum.nbfi:
            if values.get("data_unbp", None) is not None:
                raise ValueError(f'data_unbp for protocol "{value}" must be None. "{type(values.get("data_unbp", None)).__name__}" was given')
            if not isinstance(values.get('data_nbfi', None), (dict, DataNbfi)):
                raise ValueError(f'data_nbfi for protocol "{value}" must be dict. "{type(values.get("data_nbfi", None)).__name__}" was given')
            if isinstance(value, str):
                return DevicePackageProtocolTypeEnum(value)
            return value
        raise ValueError(f'Invalid protocol. "{value}" was given')


class BaseStationEnvironmentInfo(BaseModel):
    dt: datetime
    spectrum: List[float]
    sdr: int
    freq_carrier: float
    freq_delta: float


class BaseStationInfoGeo(BaseModel):
    dt: datetime
    longitude: float = 0.0
    latitude: float = 0.0
    actual: bool


class SdrConfigData(BaseModel):
    enable: bool
    dds_freq: int
    dmod: DModEnum
    baud_rate: int
    unions: int

    @validator('dmod', pre=True)
    def validate_dmod(cls, value: Union[DModEnum, str]) -> DModEnum:
        return DModEnum(re.compile(r'[^a-zA-Z0-9_-]').sub('', value).upper()) if isinstance(value, str) else value


class SdrConfig(BaseModel):
    freq: int
    sdr: List[SdrConfigData]


class BaseStationInfo(BaseModel):
    geo: BaseStationInfoGeo
    uptime_s: int
    sdr_config: Optional[SdrConfig]

    @validator('uptime_s')
    def validate_mac(cls, value: int) -> int:
        if value >= 0:
            return value
        else:
            raise ValueError('Uptime_s cannot be less than 0')

    # TODO: check uptime_s >= 0


class BaseStationAdditionalInfo(BaseModel):
    id: int  # SERIAL NUMBER
    version: Optional[str]
    # TODO: it's was just example additional info
    # any: str


@unique
class BaseStationLogsTypeEnum(Enum):
    emerg = 'emerg'
    alert = 'alert'
    critical = 'critical'
    error = 'error'
    warning = 'warning'
    notice = 'notice'
    debug = 'debug'
    info = 'info'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


@unique
class BsDownlinkCommandNameEnum(Enum):
    sync_downlink_tasks = "sync_downlink_tasks"
    add_downlink_task = "add_downlink_task"
    delete_downlink_task = "delete_downlink_task"
    get_active_downlink_task_ids = "get_active_downlink_task_ids"

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DataAddDownlinkTaskResponseInvalidTasks(BaseModel):
    id: UUID
    reason: str


class DataAddDownlinkTaskResponse(BaseModel):
    accepted_ids: List[UUID]
    already_exist_ids: List[UUID]
    invalid: List[DataAddDownlinkTaskResponseInvalidTasks]


class DataDeleteDownlinkTaskResponse(BaseModel):
    deleted_ids: List[UUID]


class DataGetActiveDownlinkTaskIDSResponse(BaseModel):
    active_ids: List[UUID]


class BsDownlinkTaskExecutionsSignalParams(BaseModel):
    freq: int
    power: int
    baudrate: int
    modulation: SignalModulation


class BsDownlinkTaskExecutionsDataUnbpMessage(BaseModel):
    ...


class BsDownlinkTaskExecutionsDataTimeSync(BaseModel):
    dt: datetime


class BaseStationLogs(BaseModel):
    type: BaseStationLogsTypeEnum
    mdl: Optional[str]
    dt: datetime
    text: str

    @validator('mdl', 'text')
    def validate_mac(cls, value: str) -> str:
        return value.strip()

    # TODO: strip content of mdl
    # TODO: strip content of text


class BsDownlinkCommandRequests(BaseModel):
    command: BsDownlinkCommandNameEnum


class BsDownlinkCommandResponse(BaseModel):
    dt: datetime
    id: UUID
    status_ok: bool
    command: BsDownlinkCommandNameEnum
    data_add_downlink_task: Optional[DataAddDownlinkTaskResponse] = None
    data_delete_downlink_tasks: Optional[DataDeleteDownlinkTaskResponse] = None
    data_get_active_downlink_task_ids: Optional[DataGetActiveDownlinkTaskIDSResponse] = None


class BsDownlinkTaskExecutions(BaseModel):
    task_id: UUID
    execution_start_dt: datetime
    execution_end_dt: datetime
    status_ok: bool
    status_message: str
    mac: int
    signal_params: Optional[BsDownlinkTaskExecutionsSignalParams] = None
    type: DownlinkTaskType
    data_unbp_message: Optional[BsDownlinkTaskExecutionsDataUnbpMessage] = None
    data_time_sync: Optional[BsDownlinkTaskExecutionsDataTimeSync] = None


class HttpV0NeroBsPacket(NeroBsPacket):
    data: List[DevicePackage]
    base_station_environment_info: Optional[List[BaseStationEnvironmentInfo]] = None
    base_station_info: BaseStationInfo
    base_station_additional_info: BaseStationAdditionalInfo
    base_station_logs: Optional[List[BaseStationLogs]] = None
    command_requests: Optional[List[BsDownlinkCommandRequests]] = None
    commands_responses: Optional[List[BsDownlinkCommandResponse]] = None
    downlink_task_executions: Optional[List[BsDownlinkTaskExecutions]] = None

    def to_integration_meta(self, *, bs_id: UUID, packet: DevicePackage, **kwargs: Any) -> IntegrationV0MessageMeta:  # type: ignore
        assert packet.sdr_info is not None
        return IntegrationV0MessageMeta(
            bs_http=IntegrationV0MessageMetaBSHttp(
                freq=packet.sdr_info.freq,
                freq_channel=packet.sdr_info.freq_channel,
                sdr=packet.sdr_info.sdr,
                baud_rate=packet.sdr_info.baud_rate,
                rssi=packet.sdr_info.rssi,
                snr=packet.sdr_info.snr,
                mac=packet.mac,
                station_id=bs_id,
                station_serial_number=self.base_station_additional_info.id,
                dt_detected=packet.dt,
                dt_published=packet.dt,
                channel_protocol=IntegrationV0MessageMetaBSChannelProtocol(packet.protocol.value),
            ),
        )

    @classmethod
    def parse(cls, data: Dict[str, Any], **kwargs: Any) -> 'HttpV0NeroBsPacket':
        try:
            return HttpV0NeroBsPacket(
                **data,
            )
        except Exception as e:  # noqa: B902
            raise DataGatewayBSProtocolParsingError('invalid payload', e)
