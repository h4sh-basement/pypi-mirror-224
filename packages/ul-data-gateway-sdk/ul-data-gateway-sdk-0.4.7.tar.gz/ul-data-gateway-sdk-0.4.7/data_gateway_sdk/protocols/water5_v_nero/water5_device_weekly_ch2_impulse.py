from decimal import Decimal
from typing import Dict, List, Any
from datetime import datetime, tzinfo
from data_aggregator_sdk.integration_message import IntegrationV0MessageConsumption, IntegrationV0MessageData, \
    IntegrationV0MessageCurrentBatteryLevel, CounterType, ResourceType

from data_gateway_sdk.utils.buf_ref import BufRef
from data_gateway_sdk.utils.packet import Packet


# PACKET (64 bits)   water5_device_weekly_ch2_impulse
#
# RESULT int:        14051230837399099771
# RESULT bin:  MSB   1100001100000000000000000000000000000000001100000001100101111011   LSB
# RESULT hex:  LE    7b 19 30 00 00 00 00 c3
#
#
# name           type  size  value(int)                                                        data(bits)
# -------------------------------------------------------------------------------------------------------
# pack_id        u8       8         123                                                          01111011
# value          u27     27       12313                               000000000000011000000011001
# UNUSED         -       21           0          000000000000000000000
# battery_fract  u7       7          67   1000011
# battery_int    u1       1           1  1


class Water5DeviceWeeklyCh2ImpulseData(Packet):
    value: int
    battery_int: int
    battery_fract: int

    def serialize(self) -> bytes:
        data = self
        result = 0
        size = 0
        result |= ((123) & (2 ** (8) - 1)) << size
        size += 8
        assert isinstance(data.value, int)
        val_tmp1 = data.value
        val_mod_tmp2 = val_tmp1 % 134217727
        result |= ((val_mod_tmp2 if val_mod_tmp2 else (val_tmp1 if not val_tmp1 else 134217727)
                    ) & (2 ** (27) - 1)) << size
        size += 27
        result |= ((0) & (2 ** (21) - 1)) << size
        size += 21
        assert isinstance(data.battery_fract, int)
        assert 0 <= data.battery_fract <= 127
        result |= ((data.battery_fract) & (2 ** (7) - 1)) << size
        size += 7
        assert isinstance(data.battery_int, int)
        assert 2 <= data.battery_int <= 3
        result |= (((data.battery_int + -2)) & (2 ** (1) - 1)) << size
        size += 1
        return result.to_bytes(8, "little")

    @classmethod
    def parse(cls, buf: BufRef) -> 'Water5DeviceWeeklyCh2ImpulseData':
        result__el_tmp3: Dict[str, Any] = dict()
        if 123 != buf.shift(8):
            raise ValueError("pack_id: buffer doesn't match value")
        result__el_tmp3["value"] = buf.shift(27) + 0
        buf.shift(21)
        result__el_tmp3["battery_fract"] = buf.shift(7) + 0
        result__el_tmp3["battery_int"] = buf.shift(1) + 2
        result = Water5DeviceWeeklyCh2ImpulseData(**result__el_tmp3)
        return result

    def to_integration_data(self, received_at: datetime, device_tz: tzinfo, **kwargs: Any) -> List[IntegrationV0MessageData]:
        return [
            IntegrationV0MessageData(
                dt=received_at,
                battery=[
                    IntegrationV0MessageCurrentBatteryLevel(voltage=self.battery_int + self.battery_fract / 100),
                ],
                consumption=[
                    IntegrationV0MessageConsumption(
                        counter_type=CounterType.COMMON,
                        resource_type=ResourceType.COMMON,
                        channel=2,
                        value=Decimal(self.value),
                        overloading_value=Decimal(134217727),
                    ),
                    # : List[IntegrationV0MessageConsumption]
                ],
            ),
        ]
