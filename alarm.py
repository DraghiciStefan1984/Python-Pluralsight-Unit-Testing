from sensor import Sensor

class Alarm:
	def __init__(self, sensor=None):
		self._low_pressure_limit=17
		self._high_pressure_limit=21
		self._sensor=sensor or Sensor()
		self._is_alarm_on=False
		
	def check(self):
		psi_pressure_value=self._sensor.sample_pressure()
		if psi_pressure_value<self._low_pressure_limit or self._high_pressure_limit<psi_pressure_value:
			self._is_alarm_on=True
			
	@property
	def is_alarm_on(self):
		return self._is_alarm_on