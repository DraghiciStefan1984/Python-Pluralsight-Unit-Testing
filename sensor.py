import random

class Sensor:
	_OFFSET=16
	
	def sample_pressure(self):
		pressure_value=self.sample_pressure()
		return Sensor._OFFSET+pressure_value
		
	@staticmethod
	def sample_actual_pressure():
		pressure_value=6*random.random()*random.random()
		return pressure_value