# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QTimer, QObject, SIGNAL, QSize
from PyQt4.QtGui import QFont
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

class UptimeDisplayApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(True)
        self.setAspectRatioMode(Plasma.Square)
        self.uptime = ''
        self.update_timer = QTimer()
        self.update_timer.start(60000) #60s
        QObject.connect(self.update_timer, SIGNAL("timeout()"), self.constantUpdate)
        self.readUptime()

    def sizeHint(self):
        return QSize(400, 400)

    def readUptime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = int(uptime_seconds / 3600)
            uptime_minutes = int((uptime_seconds - (uptime_hours * 3600)) / 60)

            self.uptime = "%dh\n%dm" % (uptime_hours, uptime_minutes)

    def constantUpdate(self):
        self.readUptime()
        self.update()

    def paintInterface(self, painter, option, rect):
        painter.save()
        painter.setPen(Qt.black)
        painter.setFont(QFont('Decorative', 8))
        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, str(self.uptime))
        painter.restore()


def CreateApplet(parent):
    return UptimeDisplayApplet(parent)
