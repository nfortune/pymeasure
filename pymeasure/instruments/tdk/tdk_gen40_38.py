#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2025 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# =============================================================================
# Libraries / modules
# =============================================================================

from .tdk_base import TDK_Lambda_Base


# =============================================================================
# Instrument file
# =============================================================================


class TDK_Gen40_38(TDK_Lambda_Base):
    """
    Represents the TDK Lambda Genesys 40-38 DC power supply. Class inherits
    commands from the TDK_Lambda_Base parent class and utilizes dynamic
    properties adjust valid values on various properties.

    .. code-block:: python

        psu = TDK_Gen40_38("COM3", 6)       # COM port and daisy-chain address
        psu.remote = "REM"                  # PSU in remote mode
        psu.output_enabled = True           # Turn on output
        psu.ramp_to_current(2.0)            # Ramp to 2.0 A of current
        print(psu.current)                  # Measure actual PSU current
        print(psu.voltage)                  # Measure actual PSU voltage
        psu.shutdown()                      # Run shutdown command

    The initialization of a TDK instrument requires the current address
    of the TDK power supply. The default address for the TDK Lambda is 6.

    :param adapter: VISAAdapter instance
    :param name: Instrument name. Default is "TDK Lambda Gen40-38"
    :param address: Serial port daisy chain number. Default is 6.
    """

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Dynamic values - Overrides base class validator values
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    voltage_values = [0, 40]
    current_values = [0, 38]
    over_voltage_values = [2, 44]
    under_voltage_values = [0, 38]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Initializer
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, adapter, name="TDK Lambda Gen40-38", address=6,
                 **kwargs):
        super().__init__(
            adapter,
            name,
            address,
            **kwargs
        )
