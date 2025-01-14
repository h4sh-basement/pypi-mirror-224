import numpy as np
import pandas as pd
import datetime

from pluma.stream import Stream, StreamType
from pluma.io.harp import load_harp_stream, _HARP_T0

from pluma.stream.siconversion import SiUnitConversion

from pluma.sync import ClockRefId

from pluma.export.streams import export_stream_to_csv, resample_stream_harp


class HarpStream(Stream):
	"""_summary_

	Args:
		Stream (_type_): _description_
	"""
	def __init__(self,
              eventcode: int,
              data: pd.DataFrame = pd.DataFrame(
                  columns=['Seconds', 'Value']),
              si_conversion: SiUnitConversion = SiUnitConversion(),
              clockreferenceid: ClockRefId = ClockRefId.HARP,
              **kw):
		super(HarpStream, self).__init__(data=data, **kw)
		self.eventcode = eventcode
		self.streamtype = StreamType.HARP
		self.si_conversion = si_conversion
		self.clockreferencering.reference = clockreferenceid

		if self.autoload:
			self.load()

		if self.si_conversion.attempt_conversion:
			self.convert_to_si()

	def convert_to_si(self, data=None):
		"""Method to convert data to SI units
		"""
		if data is None:  # Default to the instance's data if None is provided
			self.data = self.si_conversion.convert_to_si(self.data)
			self.si_conversion.is_si = True
		else:  # if some other data source is provided
			return self.si_conversion.convert_to_si(data)

	def load(self):
		self.data = load_harp_stream(self.eventcode,
                               root=self.rootfolder)
		self.si_conversion.is_si = False

	def __str__(self):
		return (f'Harp stream from device \
		{self.device}, stream {self.streamlabel}({self.eventcode})')

	@staticmethod
	def to_seconds(index):
		# Converts an harp referred timedelta to seconds (double)
		return (index - np.datetime64(_HARP_T0)) / np.timedelta64(1, 's')

	@staticmethod
	def from_seconds(index):
		# Converts seconds (double) back to a harp referenced timedelta
		return (_HARP_T0 + pd.to_timedelta(index, 's')).values

	def export_to_csv(self, root_path, **kwargs):
		export_stream_to_csv(self, root_path, **kwargs)

	def resample(self,
	      sampling_dt: datetime.timedelta,
		  **kwargs) -> pd.DataFrame:
		return resample_stream_harp(self, sampling_dt, **kwargs)