# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CCTVui_V2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 714)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 10, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 8, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_17)
        self.label_7.setMinimumSize(QtCore.QSize(0, 15))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.verticalLayout_5.addWidget(self.frame_17)
        self.logtextedit = QtWidgets.QPlainTextEdit(self.frame_16)
        self.logtextedit.setReadOnly(True)
        self.logtextedit.setObjectName("logtextedit")
        self.verticalLayout_5.addWidget(self.logtextedit)
        self.gridLayout_6.addWidget(self.frame_16, 4, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.portnum = QtWidgets.QLineEdit(self.frame)
        self.portnum.setMinimumSize(QtCore.QSize(150, 0))
        self.portnum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.portnum.setObjectName("portnum")
        self.horizontalLayout.addWidget(self.portnum)
        self.listen_btn = QtWidgets.QPushButton(self.frame)
        self.listen_btn.setObjectName("listen_btn")
        self.horizontalLayout.addWidget(self.listen_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 2)
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.currentframe = QtWidgets.QFrame(self.frame_18)
        self.currentframe.setFrameShape(QtWidgets.QFrame.Box)
        self.currentframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentframe.setObjectName("currentframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.currentframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.currentframe)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currentlabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.currentlabel.setFont(font)
        self.currentlabel.setObjectName("currentlabel")
        self.horizontalLayout_3.addWidget(self.currentlabel)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.currentframe)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.current_voltage_1 = QtWidgets.QLabel(self.frame_5)
        self.current_voltage_1.setMinimumSize(QtCore.QSize(50, 0))
        self.current_voltage_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.current_voltage_1.setText("")
        self.current_voltage_1.setAlignment(QtCore.Qt.AlignCenter)
        self.current_voltage_1.setObjectName("current_voltage_1")
        self.gridLayout.addWidget(self.current_voltage_1, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMinimumSize(QtCore.QSize(30, 0))
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.current_current_1 = QtWidgets.QLabel(self.frame_5)
        self.current_current_1.setMinimumSize(QtCore.QSize(50, 0))
        self.current_current_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.current_current_1.setText("")
        self.current_current_1.setAlignment(QtCore.Qt.AlignCenter)
        self.current_current_1.setObjectName("current_current_1")
        self.gridLayout.addWidget(self.current_current_1, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(30, 0))
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setMinimumSize(QtCore.QSize(30, 0))
        self.label_11.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.current_voltage_2 = QtWidgets.QLabel(self.frame_6)
        self.current_voltage_2.setMinimumSize(QtCore.QSize(50, 0))
        self.current_voltage_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.current_voltage_2.setText("")
        self.current_voltage_2.setAlignment(QtCore.Qt.AlignCenter)
        self.current_voltage_2.setObjectName("current_voltage_2")
        self.gridLayout_2.addWidget(self.current_voltage_2, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)
        self.current_current_2 = QtWidgets.QLabel(self.frame_6)
        self.current_current_2.setMinimumSize(QtCore.QSize(50, 0))
        self.current_current_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.current_current_2.setText("")
        self.current_current_2.setAlignment(QtCore.Qt.AlignCenter)
        self.current_current_2.setObjectName("current_current_2")
        self.gridLayout_2.addWidget(self.current_current_2, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setMinimumSize(QtCore.QSize(30, 0))
        self.label_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.frame_6)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.gridLayout_7.addWidget(self.currentframe, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_18)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.batterylabel = QtWidgets.QLabel(self.frame_8)
        self.batterylabel.setMinimumSize(QtCore.QSize(0, 0))
        self.batterylabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.batterylabel.setFont(font)
        self.batterylabel.setObjectName("batterylabel")
        self.horizontalLayout_4.addWidget(self.batterylabel)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_18 = QtWidgets.QLabel(self.frame_9)
        self.label_18.setMinimumSize(QtCore.QSize(30, 0))
        self.label_18.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.battery_voltage = QtWidgets.QLabel(self.frame_9)
        self.battery_voltage.setMinimumSize(QtCore.QSize(50, 0))
        self.battery_voltage.setMaximumSize(QtCore.QSize(50, 20))
        self.battery_voltage.setText("")
        self.battery_voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_voltage.setObjectName("battery_voltage")
        self.gridLayout_3.addWidget(self.battery_voltage, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_9)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_9)
        self.label_12.setMinimumSize(QtCore.QSize(60, 0))
        self.label_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.charge_current = QtWidgets.QLabel(self.frame_9)
        self.charge_current.setMinimumSize(QtCore.QSize(50, 20))
        self.charge_current.setMaximumSize(QtCore.QSize(50, 20))
        self.charge_current.setText("")
        self.charge_current.setAlignment(QtCore.Qt.AlignCenter)
        self.charge_current.setObjectName("charge_current")
        self.gridLayout_3.addWidget(self.charge_current, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_9)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_9)
        self.gridLayout_7.addWidget(self.frame_7, 1, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_18)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infolabel = QtWidgets.QLabel(self.frame_14)
        self.infolabel.setMinimumSize(QtCore.QSize(0, 15))
        self.infolabel.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infolabel.setFont(font)
        self.infolabel.setObjectName("infolabel")
        self.horizontalLayout_2.addWidget(self.infolabel)
        self.verticalLayout_4.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_36 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1)
        self.receive_time = QtWidgets.QLabel(self.frame_15)
        self.receive_time.setMinimumSize(QtCore.QSize(110, 0))
        self.receive_time.setText("")
        self.receive_time.setAlignment(QtCore.Qt.AlignCenter)
        self.receive_time.setObjectName("receive_time")
        self.gridLayout_5.addWidget(self.receive_time, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.gridLayout_7.addWidget(self.frame_13, 3, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_18)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sensorlabel = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sensorlabel.setFont(font)
        self.sensorlabel.setObjectName("sensorlabel")
        self.horizontalLayout_5.addWidget(self.sensorlabel)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_25 = QtWidgets.QLabel(self.frame_12)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_12)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 1, 2, 1, 1)
        self.sensor_solar = QtWidgets.QLabel(self.frame_12)
        self.sensor_solar.setText("")
        self.sensor_solar.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_solar.setObjectName("sensor_solar")
        self.gridLayout_4.addWidget(self.sensor_solar, 0, 1, 1, 1)
        self.sensor_temp = QtWidgets.QLabel(self.frame_12)
        self.sensor_temp.setText("")
        self.sensor_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_temp.setObjectName("sensor_temp")
        self.gridLayout_4.addWidget(self.sensor_temp, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_12)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_12)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.gridLayout_7.addWidget(self.frame_10, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_18, 4, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.status_alarm = QtWidgets.QLabel(self.frame_2)
        self.status_alarm.setMinimumSize(QtCore.QSize(10, 10))
        self.status_alarm.setMaximumSize(QtCore.QSize(10, 10))
        self.status_alarm.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.status_alarm.setText("")
        self.status_alarm.setObjectName("status_alarm")
        self.horizontalLayout_6.addWidget(self.status_alarm)
        self.statuslabel = QtWidgets.QLabel(self.frame_2)
        self.statuslabel.setObjectName("statuslabel")
        self.horizontalLayout_6.addWidget(self.statuslabel)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)
        self.autosave = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.autosave.setFont(font)
        self.autosave.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.autosave.setCheckable(True)
        self.autosave.setChecked(True)
        self.autosave.setObjectName("autosave")
        self.gridLayout_6.addWidget(self.autosave, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CCTV 모니터링"))
        self.label_2.setText(_translate("MainWindow", "(주)이음아이씨티 CCTV모니터링 V1.1_220307"))
        self.label_7.setText(_translate("MainWindow", "로그"))
        self.label.setText(_translate("MainWindow", "PORT"))
        self.listen_btn.setText(_translate("MainWindow", "Listen"))
        self.close_btn.setText(_translate("MainWindow", "Close"))
        self.currentlabel.setText(_translate("MainWindow", "소비전류"))
        self.label_3.setText(_translate("MainWindow", "CH 1"))
        self.label_9.setText(_translate("MainWindow", "V"))
        self.label_5.setText(_translate("MainWindow", "전압"))
        self.label_10.setText(_translate("MainWindow", "A"))
        self.label_6.setText(_translate("MainWindow", "전류"))
        self.label_11.setText(_translate("MainWindow", "전압"))
        self.label_13.setText(_translate("MainWindow", "V"))
        self.label_14.setText(_translate("MainWindow", "전류"))
        self.label_16.setText(_translate("MainWindow", "A"))
        self.label_4.setText(_translate("MainWindow", "CH 2"))
        self.batterylabel.setText(_translate("MainWindow", "배터리"))
        self.label_18.setText(_translate("MainWindow", "전압"))
        self.label_20.setText(_translate("MainWindow", "V"))
        self.label_12.setText(_translate("MainWindow", "충전전류"))
        self.label_17.setText(_translate("MainWindow", "A"))
        self.infolabel.setText(_translate("MainWindow", "정보"))
        self.label_36.setText(_translate("MainWindow", "수신시간"))
        self.sensorlabel.setText(_translate("MainWindow", "환경센서"))
        self.label_25.setText(_translate("MainWindow", "온도"))
        self.label_26.setText(_translate("MainWindow", "˚C"))
        self.label_29.setText(_translate("MainWindow", "일사량"))
        self.statuslabel.setText(_translate("MainWindow", "포트 닫힘"))
        self.autosave.setText(_translate("MainWindow", "데이터 자동저장"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
