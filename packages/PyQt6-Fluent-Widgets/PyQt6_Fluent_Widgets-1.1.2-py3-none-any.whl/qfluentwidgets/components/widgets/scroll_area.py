# coding:utf-8
from PyQt6.QtCore import QEasingCurve, Qt
from PyQt6.QtWidgets import QScrollArea

from ...common.smooth_scroll import SmoothScroll, SmoothMode
from .scroll_bar import SmoothScrollBar, SmoothScrollDelegate


class ScrollArea(QScrollArea):
    """ Smooth scroll area """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scrollDelagate = SmoothScrollDelegate(self)


class SingleDirectionScrollArea(QScrollArea):
    """ Single direction scroll area"""

    def __init__(self, parent=None, orient=Qt.Orientation.Vertical):
        """
        Parameters
        ----------
        parent: QWidget
            parent widget

        orient: Orientation
            scroll orientation
        """
        super().__init__(parent)
        self.smoothScroll = SmoothScroll(self, orient)
        self.vScrollBar = SmoothScrollBar(Qt.Orientation.Vertical, self)
        self.hScrollBar = SmoothScrollBar(Qt.Orientation.Horizontal, self)

    def setVerticalScrollBarPolicy(self, policy):
        super().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.vScrollBar.setForceHidden(policy == Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def setHorizontalScrollBarPolicy(self, policy):
        super().setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.hScrollBar.setForceHidden(policy == Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def setSmoothMode(self, mode):
        """ set smooth mode

        Parameters
        ----------
        mode: SmoothMode
            smooth scroll mode
        """
        self.smoothScroll.setSmoothMode(mode)

    def wheelEvent(self, e):
        self.smoothScroll.wheelEvent(e)
        e.setAccepted(True)


class SmoothScrollArea(QScrollArea):
    """ Smooth scroll area """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delegate = SmoothScrollDelegate(self, True)

    def setScrollAnimation(self, orient, duration, easing=QEasingCurve.Type.OutCubic):
        """ set scroll animation

        Parameters
        ----------
        orient: Orient
            scroll orientation

        duration: int
            scroll duration

        easing: QEasingCurve
            animation type
        """
        bar = self.delegate.hScrollBar if orient == Qt.Orientation.Horizontal else self.delegate.vScrollBar
        bar.setScrollAnimation(duration, easing)

