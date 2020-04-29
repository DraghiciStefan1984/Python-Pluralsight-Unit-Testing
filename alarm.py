from sensor import Sensor

class Alarm:
    def __init__(self, sensor=None):
        self._low_pressure_treshold=17
        self._high_pressure_treshold=21
        self._sensor=sensor or Sensor()
        self._is_alarm_on=False

    def check(self):
        psi_pressure_value=self._sensor.sample_pressure()
        if psi_pressure_value<self._low_pressure_treshold or self._high_pressure_treshold<psi_pressure_value:
            self._is_alarm_on=True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on