import ipaddress

import pytest

from getnet.services.utils import Device


class TestDevice:
    def test_invalid_device_id(self):
        with pytest.raises(TypeError):
            Device("127.0.0.1", "A" * 81)

    def test_invalid_ipaddress(self):
        with pytest.raises(ipaddress.AddressValueError):
            Device("127.0.0.300", "ABC")

    def test_get_as_dict(self):
        object = Device("127.0.0.3", "ABC")
        assert {"ip_address": "127.0.0.3", "device_id": "ABC"} == object.as_dict()
