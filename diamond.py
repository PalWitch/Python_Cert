# Schritt 1
class HardwareUnit:
    def __init__(self, serial_number, **kwargs):
        super().__init__(**kwargs)
        self.serial_number = serial_number

    def status(self):
        return f"{self.__class__.__name__}(serial={self.serial_number})"


class NetworkDevice(HardwareUnit):
    def __init__(self, ip_address, **kwargs):
        super().__init__(**kwargs)
        self.ip_address = ip_address

    def status(self):
        return f"{super().status()}, ip={self.ip_address}"


class MeasuringDevice(HardwareUnit):
    def __init__(self, unit, **kwargs):
        super().__init__(**kwargs)
        self.unit = unit

    def status(self):
        return f"{super().status()}, unit={self.unit}"


class SmartTemperatureSensor(NetworkDevice, MeasuringDevice):
    def __init__(self, serial_number, ip_address, unit, temperature):
        super().__init__(
            serial_number=serial_number,
            ip_address=ip_address,
            unit=unit
        )
        self.temperature = temperature

    def status(self):
        return f"{super().status()}, temperature={self.temperature}"


sensor = SmartTemperatureSensor(
    serial_number="SN-1001",
    ip_address="192.168.0.10",
    unit="C",
    temperature=22.5
)

print(sensor.__dict__)
print(SmartTemperatureSensor.__mro__)
print(sensor.status())

# Schritt 2

class JsonMixin:
    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if hasattr(value, "to_dict"):
                result[key] = value.to_dict()
            elif hasattr(value, "__dict__"):
                result[key] = value.__dict__.copy()
            else:
                result[key] = value
        return result


class DiagnosticMixin:
    def diagnostic_report(self):
        return {
            "class": self.__class__.__name__,
            "mro": [cls.__name__ for cls in self.__class__.__mro__],
            "status": self.status()
        }


class HardwareUnit:
    def __init__(self, serial_number, **kwargs):
        super().__init__(**kwargs)
        self.serial_number = serial_number

    def status(self):
        return f"{self.__class__.__name__}(serial={self.serial_number})"


class NetworkDevice(HardwareUnit):
    def __init__(self, ip_address, **kwargs):
        super().__init__(**kwargs)
        self.ip_address = ip_address

    def status(self):
        return f"{super().status()}, ip={self.ip_address}"


class MeasuringDevice(HardwareUnit):
    def __init__(self, unit, **kwargs):
        super().__init__(**kwargs)
        self.unit = unit

    def status(self):
        return f"{super().status()}, unit={self.unit}"


class Battery:
    def __init__(self, level):
        self.level = level

    def is_low(self):
        return self.level < 20


class AlertChannel:
    def send(self, message):
        return f"ALERT: {message}"


class SmartTemperatureSensor(JsonMixin, DiagnosticMixin, NetworkDevice, MeasuringDevice):
    def __init__(self, serial_number, ip_address, unit, temperature, battery, alert_channel):
        super().__init__(
            serial_number=serial_number,
            ip_address=ip_address,
            unit=unit
        )
        self.temperature = temperature
        self.battery = battery
        self.alert_channel = alert_channel

    def status(self):
        return f"{super().status()}, temperature={self.temperature}"

    def check_battery_and_alert(self):
        if self.battery.is_low():
            return self.alert_channel.send(
                f"Batterie niedrig bei Sensor {self.serial_number}: {self.battery.level}%"
            )
        return "Batterie okay"


battery = Battery(level=15)
channel = AlertChannel()

sensor = SmartTemperatureSensor(
    serial_number="SN-1002",
    ip_address="192.168.0.20",
    unit="C",
    temperature=21.8,
    battery=battery,
    alert_channel=channel
)

print(sensor.to_dict())
print(sensor.diagnostic_report())
print(sensor.check_battery_and_alert())
print(SmartTemperatureSensor.__mro__)