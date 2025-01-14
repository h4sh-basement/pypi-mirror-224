import itertools

import pyqtgraph as pg
from bec_lib.core.logger import bec_logger
from PyQt5.QtCore import pyqtProperty, pyqtSlot

from bec_widgets.bec_dispatcher import bec_dispatcher

logger = bec_logger.logger


pg.setConfigOptions(background="w", foreground="k", antialias=True)
COLORS = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a"]


class BECScanPlot(pg.GraphicsView):
    def __init__(self, parent=None, background="default"):
        super().__init__(parent, background)
        bec_dispatcher.connect(self)

        self.view = pg.PlotItem()
        self.setCentralItem(self.view)

        self._x_channel = ""
        self._y_channel_list = []

        self.scan_curves = {}
        self.dap_curves = {}

    @pyqtSlot(dict, dict)
    def on_new_scan(self, _scan_segment, _metadata):
        for plot_curve in {**self.scan_curves, **self.dap_curves}.values():
            plot_curve.setData(x=[], y=[])

    @pyqtSlot(dict, dict)
    def on_scan_segment(self, scan_segment, _metadata):
        if not self.x_channel:
            return

        data = scan_segment["data"]

        if self.x_channel not in data:
            logger.warning(f"Unknown channel `{self.x_channel}` for X data in {self.objectName()}")
            return

        x_new = data[self.x_channel][self.x_channel]["value"]
        for chan, plot_curve in self.scan_curves.items():
            if not chan:
                continue

            if chan not in data:
                logger.warning(f"Unknown channel `{chan}` for Y data in {self.objectName()}")
                continue

            y_new = data[chan][chan]["value"]
            x, y = plot_curve.getData()  # TODO: is it a good approach?
            if x is None:
                x = []
            if y is None:
                y = []

            plot_curve.setData(x=[*x, x_new], y=[*y, y_new])

    @pyqtSlot(dict, dict)
    def redraw_dap(self, data, _metadata):
        for chan, plot_curve in self.dap_curves.items():
            if not chan:
                continue

            if chan not in data:
                logger.warning(f"Unknown channel `{chan}` for DAP data in {self.objectName()}")
                continue

            x_new = data[chan]["x"]
            y_new = data[chan]["y"]

            plot_curve.setData(x=x_new, y=y_new)

    @pyqtProperty("QStringList")
    def y_channel_list(self):
        return self._y_channel_list

    @y_channel_list.setter
    def y_channel_list(self, new_list):
        # TODO: do we want to care about dap/not dap here?
        chan_removed = [chan for chan in self._y_channel_list if chan not in new_list]
        if chan_removed and chan_removed[0].startswith("dap."):
            chan_removed = chan_removed[0].partition("dap.")[-1]
            bec_dispatcher.disconnect_dap_slot(self.redraw_dap, chan_removed)

        self._y_channel_list = new_list

        # Prepare plot for a potentially different list of y channels
        self.view.clear()

        self.view.addLegend()
        colors = itertools.cycle(COLORS)

        for y_chan in new_list:
            if y_chan.startswith("dap."):
                y_chan = y_chan.partition("dap.")[-1]
                curves = self.dap_curves
                bec_dispatcher.connect_dap_slot(self.redraw_dap, y_chan)
            else:
                curves = self.scan_curves

            curves[y_chan] = self.view.plot(
                x=[], y=[], pen=pg.mkPen(color=next(colors), width=2), name=y_chan
            )

        if len(new_list) == 1:
            self.view.setLabel("left", new_list[0])

    @pyqtProperty(str)
    def x_channel(self):
        return self._x_channel

    @x_channel.setter
    def x_channel(self, new_val):
        self._x_channel = new_val
        self.view.setLabel("bottom", new_val)


if __name__ == "__main__":
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    plot = BECScanPlot()
    plot.x_channel = "samx"
    plot.y_channel_list = ["bpm3y", "bpm6y"]

    plot.show()

    sys.exit(app.exec_())
