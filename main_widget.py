from copy import deepcopy
import time
from pathlib import Path
from dataclasses import dataclass, field

import numpy as np

from PySide6.QtCore import (
    Slot,
    Signal,
    QTimer
)

from PySide6.QtWidgets import (
    QWidget,
    QFileDialog,
)

from ui_main_widget import Ui_Form




class MainWidget(QWidget, Ui_Form):


    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._p1 = self.plotWidget.plot()
        self._p1.setPen((255, 0, 0))
        self._p2 = self.plotWidget.plot()
        self._p2.setPen((150, 0, 0))
        self.plotWidget.setXRange(0, 1)
        self.plotWidget.setYRange(0, 2000)

        self._timer = QTimer()
        self._interval = 10
        self._time = 0
        self._x = []
        self._y = []
        self._x_old = []
        self._y_old = []

        self._plots = []
        self._plots_old = []
        self._create_curves()
        self._connect_signals()
        self._window_size = 1000 / self._interval
        self._ts = None
        
    def _create_curves(self):
        colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255)
        ]
        for c in colors:
            p = self.plotWidget.plot()
            p.setPen(c)
            self._plots.append(p)
            
            p_old = self.plotWidget.plot()
            p_old.setPen(c + (100,))
            self._plots_old.append(p_old)

            self._x.append([])
            self._x_old.append([])
            self._y.append([])
            self._y_old.append([])
        

    def _connect_signals(self):
        self.pushButtonStart.clicked.connect(
            self._start_plotting
        )
        self._timer.timeout.connect(self._plot_data)

    def _plot_data(self):
        if self._time > 1000:
        # if self._time % (self._interval * self._window_size) == 0:
            ts = time.perf_counter()
            # for i, p in enumerate(self._plots):
            #     p.setData(x=self._x[i], y=self._y[i])

            print(ts - self._ts)
            self._ts = ts
            # x = deepcopy(self._x)
            # for i, row in enumerate(x):
            #     self._x_old[i] = [
            #         el + self._interval*self._window_size / 1000 for
            #         el in row
            #     ]
            self._x_old = deepcopy(self._x)
            self._y_old = deepcopy(self._y)
            self._x = []
            self._y = []
            for p_old, x_old, y_old in zip(
                self._plots_old,
                self._x_old,
                self._y_old
            ):
                p_old.setData(x=x_old, y=y_old)
                self._x.append([])
                self._y.append([])
            self._time = 0
        for i, p in enumerate(self._plots):
            self._x[i].append(self._time / 1000)
            # self._y[i].append(np.random.randint(i*10, (i+1)*10, size=1)[0])
            self._y[i].append(np.random.randint(1500, 1800, size=1)[0])
            p.setData(x=self._x[i], y=self._y[i])
        self._time += self._interval

    def _plot_data_test(self):
        if self._time > 1000:
            ts = time.perf_counter()
            print(ts - self._ts)
            self._ts = ts
            self._time = 0
        self._time += self._interval

    # def _instant_plot_data(self):
    #     if self._time % (self._interval * self._window_size) == 0:
    #         ts = time.perf_counter()
    #         print(ts - self._ts)
    #         self._ts = ts
    #     for i, p in enumerate(self._plots):
        
    #     self._time += self._interval


    def _start_plotting(self):
        print('Plotting has been started!')
        self._ts = time.perf_counter()
        self._timer.start(self._interval)
        # x = np.arange(5)
        # y = np.random.normal(size=(3, 5))
        # pw = self.plotWidget
        # pw.clear()
        # for i in range(3):
        #     self.plotWidget.plot(x, y[i], pen=(i,3))

    

