from pyqtgraph import AxisItem
from datetime import date


class DateAxis(AxisItem):
    def tickStrings(self, values, scale, spacing):
        """
        Overload function to format dates from ordinals to months/days
        """
        return [
            date.fromordinal(int(value)).strftime('%b %d') for value in values
                ]
