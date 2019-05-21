# build linear interpolaters for the 'standard' flight data fields.

import math
import numpy as np
from scipy import interpolate # strait up linear interpolation, nothing fancy

# helpful constants
d2r = math.pi / 180.0

class FlightInterpolate():
    def __init__(self, df):
        self.result = {}
        for column in df.columns:
            print(column)
            self.result[column] = interpolate.interp1d(df.index, df[column],
                                                       bounds_error=False,
                                                       fill_value=0.0)

    def interp(self, t):
        result = {}
        result['time'] = t
        for key in self.result:
            result[key] = self.result[key](t).item()
        return result