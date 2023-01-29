from ipaddress import IPv4Address
from typing import Union


class Device:
    ip_address: IPv4Address
    device_id: str

    def __init__(self, ip_address: Union[IPv4Address, str], device_id: str):
        if len(device_id) > 80:
            raise TypeError("Device ID too long (max: 80 characters)")

        self.ip_address = (
            ip_address
            if isinstance(ip_address, IPv4Address)
            else IPv4Address(ip_address)
        )
        self.device_id = device_id

    def as_dict(self):
        data = self.__dict__.copy()
        data["ip_address"] = str(self.ip_address)
        return data
