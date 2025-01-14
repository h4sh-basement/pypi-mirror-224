# coding:utf-8
from typing import Union

from PyQt6.QtCore import Qt, pyqtSignal, QRectF, QDate, QPoint, pyqtProperty
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication

from ...common.style_sheet import FluentStyleSheet
from ...common.icon import FluentIcon as FIF
from .calendar_view import CalendarView


class CalendarPicker(QPushButton):
    """ Calendar picker """

    dateChanged = pyqtSignal(QDate)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._date = QDate()
        self._dateFormat = 'yyyy/M/d'

        self.view = CalendarView(self.window())
        self.view.hide()

        self.setText(self.tr('Pick a date'))
        FluentStyleSheet.CALENDAR_PICKER.apply(self)

        self.clicked.connect(self._showCalendarView)
        self.view.dateChanged.connect(self._onDateChanged)

    def getDate(self):
        return self._date

    def setDate(self, date: QDate):
        """ set the selected date """
        self._onDateChanged(date)
        self.view.setDate(date)

    def getDateFormat(self):
        return self._dateFormat

    def setDateFormat(self, format: Union[Qt.DateFormat, str]):
        self._dateFormat = format
        if self.date.isValid():
            self.setText(self.date.toString(self.dateFormat))

    def _showCalendarView(self):
        x = int(self.width()/2 - self.view.sizeHint().width()/2)
        y = self.height()
        self.view.exec(self.mapToGlobal(QPoint(x, y)))

    def _onDateChanged(self, date: QDate):
        self._date = QDate(date)
        self.setText(date.toString(self.dateFormat))
        self.setProperty('hasDate', True)
        self.setStyle(QApplication.style())
        self.update()

        self.dateChanged.emit(date)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        if not self.property('hasDate'):
            painter.setOpacity(0.6)

        w = 12
        rect = QRectF(self.width() - 23, self.height()/2 - w/2, w, w)
        FIF.CALENDAR.render(painter, rect)

    date = pyqtProperty(QDate, getDate, setDate)
    dateFormat = pyqtProperty(Qt.DateFormat, getDateFormat, setDateFormat)
