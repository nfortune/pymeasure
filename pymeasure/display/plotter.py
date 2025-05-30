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

import logging

import sys
import time

from .Qt import QtWidgets
from .windows import PlotterWindow
from ..thread import StoppableThread

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Plotter(StoppableThread):
    """ Plotter dynamically plots data from a file through the Results object.

    .. seealso::

        Tutorial :ref:`tutorial-plotterwindow`
            A tutorial and example on using the Plotter and PlotterWindow.
    """

    def __init__(self, results, refresh_time=0.1, linewidth=1):
        super().__init__()
        self.results = results
        self.refresh_time = refresh_time
        self.linewidth = linewidth

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        window = PlotterWindow(self, refresh_time=self.refresh_time, linewidth=self.linewidth)
        self.setup_plot(window.plot)
        app.aboutToQuit.connect(window.quit)
        window.show()
        app.exec()

    def setup_plot(self, plot):
        """
        This method does nothing by default, but can be overridden by the child
        class in order to set up custom options for the plot window, via its
        PlotItem_.

        :param plot: This window's PlotItem_ instance.

        .. _PlotItem: https://pyqtgraph.readthedocs.io/en/latest/graphicsItems/plotitem.html
        """
        pass

    def wait_for_close(self, check_time=0.1):
        while not self.should_stop():
            time.sleep(check_time)
