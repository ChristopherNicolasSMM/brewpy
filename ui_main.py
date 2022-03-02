# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 487)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"/*-----Header Table-----*/\n"
" QHeaderView::section\n"
" { \n"
" color:white; \n"
" background-color:#232326; \n"
" }\n"
" \n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #202020;\n"
"	color: #fff;\n"
"	selection-background-color: #ff732d; \n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ff732d;\n"
"	font-weight: bold;\n"
"	font-size: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel:disabled \n"
"{\n"
"	color: #4e4e4e;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: #252525;\n"
"	border: none;\n"
"	color: #ff732d;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar:disabled \n"
"{\n"
"	color: #4e4e4e;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: #424242;\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #424242;\n"
"    border: none;\n"
"    padding: 4px;\n"
"    padding-right: 0px;\n"
"	color: #fff;\n"
"	font-size: 11px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #ff732d;\n"
"    color: #000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"	background-color: #aaa;	\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
""
                        "QTabBar \n"
"{\n"
"	background-color: transparent;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"	border:none;\n"
"	left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"	font-weight: bold;\n"
"	padding-left: 15px; \n"
"	padding-right: 15px; \n"
"	height: 25px;\n"
"	width: 60px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	border: 1px solid #333; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"	color: #ff732d; \n"
"	font-weight: bold;\n"
"	border: 1px solid #1b1b1b;\n"
"	background-color: #1b1b1b;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"	background-color: #424242;\n"
"	border: 1px solid #414141;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar:tab:selected:disabled \n"
"{\n"
"	color: #4e4e4e;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"	color: #fff; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar:tab:!selected:disabled \n"
"{\n"
"	color: #4e4e4e;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color"
                        ": transparent;\n"
"	color: #ff732d;\n"
"	font-weight: bold;\n"
"	font-size: 10px;\n"
"	border: none;\n"
"	margin: 2px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: #ff732d;\n"
"	color: #000;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: #424242;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: #424242;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:disabled \n"
"{\n"
"	color: #4e4e4e;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDockWidget-----*/\n"
"QDockWidget\n"
"{\n"
"	color : #ff732d;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::title \n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #3a3a3a;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button\n"
""
                        "{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: #ff732d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: #ff732d;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeWidget\n"
"{\n"
"	show-decoration-selected: 0;\n"
"	selection-background-color: transparent; /* Used on Mac */\n"
"	selection-color: #fff; /* Used on Mac */\n"
"	background-color: #292929;\n"
"	border: 1px solid #3a3a3a;\n"
"	padding: 5px;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color: #000;\n"
"	background-color: #ff732d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"	background-color: #424242;\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:disabled\n"
"{\n"
"	backgroun"
                        "d-color: #656565;\n"
"	color: #333;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	color: black;\n"
"	font-weight: bold;\n"
"	background-color: #9d9d9d;\n"
"	border: 1px solid #3a3a3a;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover \n"
"{\n"
"	background-color: #bebebe;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"	color: #ff732d;\n"
"    border: 1px solid #3a3a3a;\n"
"	background-color: #1b1b1b;\n"
"    margin-top: 5.5ex;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::disabled\n"
"{\n"
"	color: #656"
                        "565;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title \n"
"{\n"
"	background-color: #1b1b1b;\n"
"	border: 1px solid #3a3a3a;\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top right 0px;\n"
"	border-radius: 0px;\n"
"    padding: 3px 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox \n"
"{\n"
"	background-color: #424242;\n"
"	border: 1px solid #3a3a3a;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:editable \n"
"{\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"	background-color: #424242;\n"
"    border-left-width:1px;\n"
"    border-left-color: #777777;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow \n"
"{\n"
"    image: url(://arrow-down.png);\n"
"	width:8px;\n"
"	height:8"
                        "px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on \n"
"{ \n"
"    top: 1px;\n"
"    left: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QListView\n"
"{\n"
"	background-color: #292929;\n"
"    border-left-style: solid; \n"
"	selection-background-color: #ff732d;\n"
"	selection-color: #000;\n"
"	color: #fff;\n"
"	padding: 10px;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"	font-size: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #00111d;\n"
"    border: 1px solid #ff732d;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #ff732d;\n"
"    border: 1px solid #ff732d;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #ff732d;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheck"
                        "Box::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox-----*/\n"
"QSpinBox \n"
"{\n"
"    border: 1px solid #3a3a3a;\n"
"	min-height: 20px;\n"
"	min-width: 30px;\n"
"    border-radius : 2px;\n"
"	color : #ff732d;\n"
"	font-weight: bold;\n"
"	font-size: 10px;\n"
"    background-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover \n"
"{\n"
"	background-color: #333;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button \n"
"{\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover \n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed \n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow \n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    he"
                        "ight: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button \n"
"{\n"
"	border-bottom-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover \n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed \n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow \n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{ \n"
"	border: 2px inset #424242; \n"
"	border-radius: 6px; \n"
"	background-color:  #323232;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover\n"
"{ \n"
"	border: 2px solid #ff732d; \n"
"	border-radius: 5px; \n"
""
                        "	background-color:  #323232;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{ \n"
"	border: 2px inset #424242; \n"
"	border-radius: 5px; \n"
"	background-color: #ff732d; \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 2px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar \n"
"{\n"
"	color: #ff732d;\n"
"	font-weight: bold;\n"
"	background-color: #252525;\n"
"\n"
"}\n"
"\n"
"\n"
"QStatusBar::item \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSizeGrip-----*/\n"
"QSizeGrip \n"
"{\n"
"	background-color: image(\"./ressources/sizegrip.png\"); /*To replace*/\n"
"\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 10)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QSize(0, 0))
        self.menu.setMaximumSize(QSize(200, 16777215))
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 32))
        self.frame.setMaximumSize(QSize(16777215, 32))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 191, 21))

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.principal_pgtool = QWidget()
        self.principal_pgtool.setObjectName(u"principal_pgtool")
        self.principal_pgtool.setGeometry(QRect(0, 0, 106, 354))
        self.verticalLayout_4 = QVBoxLayout(self.principal_pgtool)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.inicio_btn = QPushButton(self.principal_pgtool)
        self.inicio_btn.setObjectName(u"inicio_btn")
        self.inicio_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/novos_icones/casa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inicio_btn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.inicio_btn)

        self.cadastros_btn = QPushButton(self.principal_pgtool)
        self.cadastros_btn.setObjectName(u"cadastros_btn")
        self.cadastros_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.cadastros_btn)

        self.insumos_btn = QPushButton(self.principal_pgtool)
        self.insumos_btn.setObjectName(u"insumos_btn")
        self.insumos_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/novos_icones/salgadinhos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insumos_btn.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.insumos_btn)

        self.receitas_btn = QPushButton(self.principal_pgtool)
        self.receitas_btn.setObjectName(u"receitas_btn")
        self.receitas_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/novos_icones/cerveja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.receitas_btn.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.receitas_btn)

        self.parametros_btn = QPushButton(self.principal_pgtool)
        self.parametros_btn.setObjectName(u"parametros_btn")
        self.parametros_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/novos_icones/controles.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parametros_btn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.parametros_btn)

        self.painel_btn = QPushButton(self.principal_pgtool)
        self.painel_btn.setObjectName(u"painel_btn")
        self.painel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/novos_icones/cerveja (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.painel_btn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.painel_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.principal_pgtool, u"Menu Principal")
        self.opcoes_pgtool = QWidget()
        self.opcoes_pgtool.setObjectName(u"opcoes_pgtool")
        self.opcoes_pgtool.setGeometry(QRect(0, 0, 93, 354))
        self.verticalLayout_20 = QVBoxLayout(self.opcoes_pgtool)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.contato_btn = QPushButton(self.opcoes_pgtool)
        self.contato_btn.setObjectName(u"contato_btn")
        self.contato_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/novos_icones/comercial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contato_btn.setIcon(icon5)

        self.verticalLayout_20.addWidget(self.contato_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.opcoes_pgtool, u"Suporte")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.menu)

        self.principal = QFrame(self.centralwidget)
        self.principal.setObjectName(u"principal")
        self.principal.setFrameShape(QFrame.StyledPanel)
        self.principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.principal)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.principal)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(32, 32))
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggle_btn = QPushButton(self.header)
        self.toggle_btn.setObjectName(u"toggle_btn")
        self.toggle_btn.setMinimumSize(QSize(32, 34))
        self.toggle_btn.setMaximumSize(QSize(32, 32))
        self.toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_btn.setLayoutDirection(Qt.LeftToRight)
        self.toggle_btn.setAutoFillBackground(False)
        self.toggle_btn.setStyleSheet(u"QPushButton{aling:left;}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_btn.setIcon(icon6)
        self.toggle_btn.setIconSize(QSize(24, 24))
        self.toggle_btn.setCheckable(False)
        self.toggle_btn.setAutoDefault(False)
        self.toggle_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.toggle_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.atualizar_btn = QPushButton(self.header)
        self.atualizar_btn.setObjectName(u"atualizar_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/novos_icones/repetir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atualizar_btn.setIcon(icon7)
        self.atualizar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.atualizar_btn)

        self.save_btn = QPushButton(self.header)
        self.save_btn.setObjectName(u"save_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/novos_icones/salve-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon8)
        self.save_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.save_btn)

        self.exit_btn = QPushButton(self.header)
        self.exit_btn.setObjectName(u"exit_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/novos_icones/saida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon9)
        self.exit_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.exit_btn)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.principal)
        self.body.setObjectName(u"body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.body)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.paginacao = QStackedWidget(self.body)
        self.paginacao.setObjectName(u"paginacao")
        self.inicio_pg = QWidget()
        self.inicio_pg.setObjectName(u"inicio_pg")
        self.verticalLayout_15 = QVBoxLayout(self.inicio_pg)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.inicio_pg)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"image: url(:/icons/imgs/logo1.png);")

        self.verticalLayout_15.addWidget(self.label_4)

        self.paginacao.addWidget(self.inicio_pg)
        self.suporte_pg = QWidget()
        self.suporte_pg.setObjectName(u"suporte_pg")
        self.verticalLayout_16 = QVBoxLayout(self.suporte_pg)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.suporte_pg)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.suporte_pg)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"image: url(:/icons/imgs/ajude o desenvolvedor.png);")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_7 = QLabel(self.suporte_pg)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_4)

        self.paginacao.addWidget(self.suporte_pg)
        self.painel_pg = QWidget()
        self.painel_pg.setObjectName(u"painel_pg")
        self.tipo_adjunto_cb_8 = QComboBox(self.painel_pg)
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.addItem("")
        self.tipo_adjunto_cb_8.setObjectName(u"tipo_adjunto_cb_8")
        self.tipo_adjunto_cb_8.setGeometry(QRect(10, 50, 381, 23))
        self.tipo_adjunto_cb_8.setMinimumSize(QSize(100, 0))
        self.label_106 = QLabel(self.painel_pg)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(10, 12, 381, 32))
        self.label_107 = QLabel(self.painel_pg)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(420, 12, 211, 32))
        self.tipo_adjunto_cb_9 = QComboBox(self.painel_pg)
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.addItem("")
        self.tipo_adjunto_cb_9.setObjectName(u"tipo_adjunto_cb_9")
        self.tipo_adjunto_cb_9.setGeometry(QRect(420, 50, 211, 23))
        self.tipo_adjunto_cb_9.setMinimumSize(QSize(100, 0))
        self.descricao_adjunto_tbx_40 = QLineEdit(self.painel_pg)
        self.descricao_adjunto_tbx_40.setObjectName(u"descricao_adjunto_tbx_40")
        self.descricao_adjunto_tbx_40.setGeometry(QRect(650, 40, 151, 29))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.descricao_adjunto_tbx_40.setFont(font)
        self.label_108 = QLabel(self.painel_pg)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(650, 10, 151, 32))
        self.graphicsView = QGraphicsView(self.painel_pg)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 120, 401, 81))
        self.graphicsView_2 = QGraphicsView(self.painel_pg)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(420, 120, 401, 81))
        self.label_111 = QLabel(self.painel_pg)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(10, 90, 401, 32))
        self.label_112 = QLabel(self.painel_pg)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(420, 87, 401, 32))
        self.groupBox_7 = QGroupBox(self.painel_pg)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 310, 381, 80))
        self.label_70 = QLabel(self.groupBox_7)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 60, 101, 16))
        self.label_71 = QLabel(self.groupBox_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(110, 60, 151, 16))
        self.label_72 = QLabel(self.groupBox_7)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(260, 60, 121, 16))
        self.pushButton_7 = QPushButton(self.groupBox_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(17, 30, 30, 31))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/novos_icones/status_ligado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(32, 32))
        self.pushButton_8 = QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(140, 30, 30, 31))
        self.pushButton_8.setIcon(icon10)
        self.pushButton_8.setIconSize(QSize(32, 32))
        self.pushButton_9 = QPushButton(self.groupBox_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(290, 30, 30, 31))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/novos_icones/status_desligado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon11)
        self.pushButton_9.setIconSize(QSize(32, 32))
        self.pushButton_5 = QPushButton(self.painel_pg)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(410, 320, 291, 71))
        self.pushButton_5.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_6 = QPushButton(self.painel_pg)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(710, 320, 101, 71))
        self.pushButton_6.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"background-color: rgb(0, 188, 0);")
        self.paginacao.addWidget(self.painel_pg)
        self.parametros_pg = QWidget()
        self.parametros_pg.setObjectName(u"parametros_pg")
        self.paginacao.addWidget(self.parametros_pg)
        self.receitas_pg = QWidget()
        self.receitas_pg.setObjectName(u"receitas_pg")
        self.verticalLayout_5 = QVBoxLayout(self.receitas_pg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.receita_tbw = QTabWidget(self.receitas_pg)
        self.receita_tbw.setObjectName(u"receita_tbw")
        self.basico_receita_aba = QWidget()
        self.basico_receita_aba.setObjectName(u"basico_receita_aba")
        self.gridLayout_5 = QGridLayout(self.basico_receita_aba)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_58 = QLabel(self.basico_receita_aba)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_5.addWidget(self.label_58, 0, 0, 1, 3)

        self.label_59 = QLabel(self.basico_receita_aba)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_5.addWidget(self.label_59, 0, 3, 1, 5)

        self.label_60 = QLabel(self.basico_receita_aba)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_5.addWidget(self.label_60, 0, 8, 1, 1)

        self.descricao_adjunto_tbx_2 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_2.setObjectName(u"descricao_adjunto_tbx_2")
        self.descricao_adjunto_tbx_2.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_2, 1, 0, 1, 3)

        self.descricao_adjunto_tbx_3 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_3.setObjectName(u"descricao_adjunto_tbx_3")
        self.descricao_adjunto_tbx_3.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_3, 1, 3, 1, 5)

        self.descricao_adjunto_tbx_4 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_4.setObjectName(u"descricao_adjunto_tbx_4")
        self.descricao_adjunto_tbx_4.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_4, 1, 8, 1, 1)

        self.label_61 = QLabel(self.basico_receita_aba)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_5.addWidget(self.label_61, 2, 0, 1, 1)

        self.label_62 = QLabel(self.basico_receita_aba)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_5.addWidget(self.label_62, 2, 1, 1, 2)

        self.label_63 = QLabel(self.basico_receita_aba)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_5.addWidget(self.label_63, 2, 3, 1, 2)

        self.label_64 = QLabel(self.basico_receita_aba)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_5.addWidget(self.label_64, 2, 5, 1, 2)

        self.label_84 = QLabel(self.basico_receita_aba)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_5.addWidget(self.label_84, 2, 7, 1, 2)

        self.tipo_adjunto_cb_3 = QComboBox(self.basico_receita_aba)
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.addItem("")
        self.tipo_adjunto_cb_3.setObjectName(u"tipo_adjunto_cb_3")
        self.tipo_adjunto_cb_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.tipo_adjunto_cb_3, 3, 0, 1, 1)

        self.tipo_adjunto_cb_4 = QComboBox(self.basico_receita_aba)
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.addItem("")
        self.tipo_adjunto_cb_4.setObjectName(u"tipo_adjunto_cb_4")
        self.tipo_adjunto_cb_4.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.tipo_adjunto_cb_4, 3, 1, 1, 2)

        self.dateEdit = QDateEdit(self.basico_receita_aba)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.dateEdit, 3, 3, 1, 2)

        self.timeEdit = QTimeEdit(self.basico_receita_aba)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.timeEdit, 3, 5, 1, 2)

        self.descricao_adjunto_tbx_21 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_21.setObjectName(u"descricao_adjunto_tbx_21")
        self.descricao_adjunto_tbx_21.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_21, 3, 7, 1, 2)

        self.label_65 = QLabel(self.basico_receita_aba)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_5.addWidget(self.label_65, 4, 0, 1, 1)

        self.label_66 = QLabel(self.basico_receita_aba)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_5.addWidget(self.label_66, 4, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.basico_receita_aba)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setMinimumSize(QSize(380, 78))
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_67 = QLabel(self.groupBox_5)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_6.addWidget(self.label_67, 0, 0, 1, 1)

        self.label_85 = QLabel(self.groupBox_5)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_6.addWidget(self.label_85, 0, 1, 1, 1)

        self.label_86 = QLabel(self.groupBox_5)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_6.addWidget(self.label_86, 0, 2, 1, 1)

        self.descricao_adjunto_tbx_11 = QLineEdit(self.groupBox_5)
        self.descricao_adjunto_tbx_11.setObjectName(u"descricao_adjunto_tbx_11")
        self.descricao_adjunto_tbx_11.setMinimumSize(QSize(0, 30))
        self.descricao_adjunto_tbx_11.setFont(font)

        self.gridLayout_6.addWidget(self.descricao_adjunto_tbx_11, 1, 0, 1, 1)

        self.descricao_adjunto_tbx_22 = QLineEdit(self.groupBox_5)
        self.descricao_adjunto_tbx_22.setObjectName(u"descricao_adjunto_tbx_22")
        self.descricao_adjunto_tbx_22.setMinimumSize(QSize(0, 30))
        self.descricao_adjunto_tbx_22.setFont(font)

        self.gridLayout_6.addWidget(self.descricao_adjunto_tbx_22, 1, 1, 1, 1)

        self.descricao_adjunto_tbx_23 = QLineEdit(self.groupBox_5)
        self.descricao_adjunto_tbx_23.setObjectName(u"descricao_adjunto_tbx_23")
        self.descricao_adjunto_tbx_23.setMinimumSize(QSize(0, 30))
        self.descricao_adjunto_tbx_23.setFont(font)

        self.gridLayout_6.addWidget(self.descricao_adjunto_tbx_23, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 4, 2, 2, 6)

        self.label_68 = QLabel(self.basico_receita_aba)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_5.addWidget(self.label_68, 4, 8, 1, 1)

        self.descricao_adjunto_tbx_9 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_9.setObjectName(u"descricao_adjunto_tbx_9")
        self.descricao_adjunto_tbx_9.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_9, 5, 0, 1, 1)

        self.descricao_adjunto_tbx_10 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_10.setObjectName(u"descricao_adjunto_tbx_10")
        self.descricao_adjunto_tbx_10.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_10, 5, 1, 1, 1)

        self.textEdit = QTextEdit(self.basico_receita_aba)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_5.addWidget(self.textEdit, 5, 8, 5, 1)

        self.label_93 = QLabel(self.basico_receita_aba)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_5.addWidget(self.label_93, 6, 0, 1, 1)

        self.label_90 = QLabel(self.basico_receita_aba)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_5.addWidget(self.label_90, 6, 1, 1, 1)

        self.label_92 = QLabel(self.basico_receita_aba)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_5.addWidget(self.label_92, 6, 2, 1, 2)

        self.label_89 = QLabel(self.basico_receita_aba)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_5.addWidget(self.label_89, 6, 4, 1, 2)

        self.label_91 = QLabel(self.basico_receita_aba)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_5.addWidget(self.label_91, 6, 6, 1, 2)

        self.descricao_adjunto_tbx_29 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_29.setObjectName(u"descricao_adjunto_tbx_29")
        self.descricao_adjunto_tbx_29.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_29, 7, 0, 1, 1)

        self.descricao_adjunto_tbx_25 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_25.setObjectName(u"descricao_adjunto_tbx_25")
        self.descricao_adjunto_tbx_25.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_25, 7, 1, 1, 1)

        self.descricao_adjunto_tbx_28 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_28.setObjectName(u"descricao_adjunto_tbx_28")
        self.descricao_adjunto_tbx_28.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_28, 7, 2, 1, 2)

        self.descricao_adjunto_tbx_30 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_30.setObjectName(u"descricao_adjunto_tbx_30")
        self.descricao_adjunto_tbx_30.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_30, 7, 4, 1, 2)

        self.descricao_adjunto_tbx_26 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_26.setObjectName(u"descricao_adjunto_tbx_26")
        self.descricao_adjunto_tbx_26.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_26, 7, 6, 1, 2)

        self.label_96 = QLabel(self.basico_receita_aba)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_5.addWidget(self.label_96, 8, 0, 1, 1)

        self.label_97 = QLabel(self.basico_receita_aba)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_5.addWidget(self.label_97, 8, 1, 1, 1)

        self.label_95 = QLabel(self.basico_receita_aba)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_5.addWidget(self.label_95, 8, 2, 1, 2)

        self.label_98 = QLabel(self.basico_receita_aba)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_5.addWidget(self.label_98, 8, 4, 1, 2)

        self.label_94 = QLabel(self.basico_receita_aba)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_5.addWidget(self.label_94, 8, 6, 1, 2)

        self.descricao_adjunto_tbx_31 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_31.setObjectName(u"descricao_adjunto_tbx_31")
        self.descricao_adjunto_tbx_31.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_31, 9, 0, 1, 1)

        self.descricao_adjunto_tbx_34 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_34.setObjectName(u"descricao_adjunto_tbx_34")
        self.descricao_adjunto_tbx_34.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_34, 9, 1, 1, 1)

        self.descricao_adjunto_tbx_32 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_32.setObjectName(u"descricao_adjunto_tbx_32")
        self.descricao_adjunto_tbx_32.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_32, 9, 2, 1, 2)

        self.descricao_adjunto_tbx_33 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_33.setObjectName(u"descricao_adjunto_tbx_33")
        self.descricao_adjunto_tbx_33.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_33, 9, 4, 1, 2)

        self.descricao_adjunto_tbx_27 = QLineEdit(self.basico_receita_aba)
        self.descricao_adjunto_tbx_27.setObjectName(u"descricao_adjunto_tbx_27")
        self.descricao_adjunto_tbx_27.setFont(font)

        self.gridLayout_5.addWidget(self.descricao_adjunto_tbx_27, 9, 6, 1, 2)

        self.receita_tbw.addTab(self.basico_receita_aba, "")
        self.parametros_receita_aba = QWidget()
        self.parametros_receita_aba.setObjectName(u"parametros_receita_aba")
        self.gridLayout_8 = QGridLayout(self.parametros_receita_aba)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_6 = QGroupBox(self.parametros_receita_aba)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_3 = QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/novos_icones/mais.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon12)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_3, 0, 5, 2, 1)

        self.label_57 = QLabel(self.groupBox_6)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_7.addWidget(self.label_57, 1, 3, 1, 1)

        self.tableWidget_2 = QTableWidget(self.groupBox_6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_7.addWidget(self.tableWidget_2, 2, 0, 1, 6)

        self.label_69 = QLabel(self.groupBox_6)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_7.addWidget(self.label_69, 0, 2, 1, 2)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/novos_icones/erro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon13)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_4, 0, 0, 2, 1)

        self.timeEdit_3 = QTimeEdit(self.groupBox_6)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.timeEdit_3, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_6, 0, 0, 5, 1)

        self.label_99 = QLabel(self.parametros_receita_aba)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_8.addWidget(self.label_99, 0, 1, 1, 2)

        self.label_101 = QLabel(self.parametros_receita_aba)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_8.addWidget(self.label_101, 0, 3, 1, 3)

        self.tipo_adjunto_cb_5 = QComboBox(self.parametros_receita_aba)
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.addItem("")
        self.tipo_adjunto_cb_5.setObjectName(u"tipo_adjunto_cb_5")
        self.tipo_adjunto_cb_5.setMinimumSize(QSize(100, 0))

        self.gridLayout_8.addWidget(self.tipo_adjunto_cb_5, 1, 1, 1, 2)

        self.tipo_adjunto_cb_6 = QComboBox(self.parametros_receita_aba)
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.addItem("")
        self.tipo_adjunto_cb_6.setObjectName(u"tipo_adjunto_cb_6")
        self.tipo_adjunto_cb_6.setMinimumSize(QSize(100, 0))

        self.gridLayout_8.addWidget(self.tipo_adjunto_cb_6, 1, 3, 1, 3)

        self.label_102 = QLabel(self.parametros_receita_aba)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_8.addWidget(self.label_102, 2, 1, 1, 1)

        self.label_100 = QLabel(self.parametros_receita_aba)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_8.addWidget(self.label_100, 2, 2, 1, 2)

        self.label_103 = QLabel(self.parametros_receita_aba)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_8.addWidget(self.label_103, 2, 4, 1, 1)

        self.label_104 = QLabel(self.parametros_receita_aba)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_8.addWidget(self.label_104, 2, 5, 1, 1)

        self.tipo_adjunto_cb_7 = QComboBox(self.parametros_receita_aba)
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.addItem("")
        self.tipo_adjunto_cb_7.setObjectName(u"tipo_adjunto_cb_7")
        self.tipo_adjunto_cb_7.setMinimumSize(QSize(100, 0))

        self.gridLayout_8.addWidget(self.tipo_adjunto_cb_7, 3, 1, 1, 1)

        self.descricao_adjunto_tbx_36 = QLineEdit(self.parametros_receita_aba)
        self.descricao_adjunto_tbx_36.setObjectName(u"descricao_adjunto_tbx_36")
        self.descricao_adjunto_tbx_36.setFont(font)

        self.gridLayout_8.addWidget(self.descricao_adjunto_tbx_36, 3, 2, 1, 2)

        self.descricao_adjunto_tbx_37 = QLineEdit(self.parametros_receita_aba)
        self.descricao_adjunto_tbx_37.setObjectName(u"descricao_adjunto_tbx_37")
        self.descricao_adjunto_tbx_37.setFont(font)

        self.gridLayout_8.addWidget(self.descricao_adjunto_tbx_37, 3, 4, 1, 1)

        self.descricao_adjunto_tbx_38 = QLineEdit(self.parametros_receita_aba)
        self.descricao_adjunto_tbx_38.setObjectName(u"descricao_adjunto_tbx_38")
        self.descricao_adjunto_tbx_38.setFont(font)

        self.gridLayout_8.addWidget(self.descricao_adjunto_tbx_38, 3, 5, 1, 1)

        self.label_105 = QLabel(self.parametros_receita_aba)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_8.addWidget(self.label_105, 4, 1, 1, 2)

        self.textEdit_2 = QTextEdit(self.parametros_receita_aba)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_8.addWidget(self.textEdit_2, 5, 1, 1, 5)

        self.receita_tbw.addTab(self.parametros_receita_aba, "")
        self.ingredientes_receita_aba = QWidget()
        self.ingredientes_receita_aba.setObjectName(u"ingredientes_receita_aba")
        self.horizontalLayout_6 = QHBoxLayout(self.ingredientes_receita_aba)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.ingredientes_receita_aba)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_7 = QFrame(self.ingredientes_receita_aba)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_21.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_21.addWidget(self.pushButton_2)

        self.verticalSpacer_4 = QSpacerItem(20, 252, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.receita_tbw.addTab(self.ingredientes_receita_aba, "")
        self.analise_receita_aba = QWidget()
        self.analise_receita_aba.setObjectName(u"analise_receita_aba")
        self.receita_tbw.addTab(self.analise_receita_aba, "")

        self.verticalLayout_5.addWidget(self.receita_tbw)

        self.paginacao.addWidget(self.receitas_pg)
        self.cadastros_pg = QWidget()
        self.cadastros_pg.setObjectName(u"cadastros_pg")
        self.verticalLayout_17 = QVBoxLayout(self.cadastros_pg)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cadastro_tabw = QTabWidget(self.cadastros_pg)
        self.cadastro_tabw.setObjectName(u"cadastro_tabw")
        self.cadastro_tabw.setEnabled(True)
        self.malte_aba = QWidget()
        self.malte_aba.setObjectName(u"malte_aba")
        self.gridLayout = QGridLayout(self.malte_aba)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.malte_aba)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 4)

        self.label_9 = QLabel(self.malte_aba)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 2)

        self.label_10 = QLabel(self.malte_aba)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 6, 1, 1)

        self.descricao_malte_tbx = QLineEdit(self.malte_aba)
        self.descricao_malte_tbx.setObjectName(u"descricao_malte_tbx")
        self.descricao_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.descricao_malte_tbx, 1, 0, 1, 4)

        self.origem_malte_tbx = QLineEdit(self.malte_aba)
        self.origem_malte_tbx.setObjectName(u"origem_malte_tbx")
        self.origem_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.origem_malte_tbx, 1, 4, 1, 2)

        self.fabricante_malte_tbx = QLineEdit(self.malte_aba)
        self.fabricante_malte_tbx.setObjectName(u"fabricante_malte_tbx")
        self.fabricante_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.fabricante_malte_tbx, 1, 6, 1, 1)

        self.label_12 = QLabel(self.malte_aba)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 2)

        self.label_11 = QLabel(self.malte_aba)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        self.label_13 = QLabel(self.malte_aba)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 3, 1, 2)

        self.label_14 = QLabel(self.malte_aba)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 5, 1, 1)

        self.label_19 = QLabel(self.malte_aba)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 2, 6, 1, 1)

        self.tipo_malte_cb = QComboBox(self.malte_aba)
        self.tipo_malte_cb.addItem("")
        self.tipo_malte_cb.addItem("")
        self.tipo_malte_cb.setObjectName(u"tipo_malte_cb")

        self.gridLayout.addWidget(self.tipo_malte_cb, 3, 0, 1, 2)

        self.qntmax_malte_tbx = QLineEdit(self.malte_aba)
        self.qntmax_malte_tbx.setObjectName(u"qntmax_malte_tbx")
        self.qntmax_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.qntmax_malte_tbx, 3, 2, 1, 1)

        self.cor_malte_tbx = QLineEdit(self.malte_aba)
        self.cor_malte_tbx.setObjectName(u"cor_malte_tbx")
        self.cor_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.cor_malte_tbx, 3, 3, 1, 2)

        self.preco_malte_tbx = QLineEdit(self.malte_aba)
        self.preco_malte_tbx.setObjectName(u"preco_malte_tbx")
        self.preco_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.preco_malte_tbx, 3, 5, 1, 1)

        self.extibulkg_malte_tbx = QLineEdit(self.malte_aba)
        self.extibulkg_malte_tbx.setObjectName(u"extibulkg_malte_tbx")
        self.extibulkg_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.extibulkg_malte_tbx, 3, 6, 1, 1)

        self.label_15 = QLabel(self.malte_aba)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_16 = QLabel(self.malte_aba)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 1, 1, 2)

        self.label_17 = QLabel(self.malte_aba)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 4, 4, 1, 2)

        self.label_18 = QLabel(self.malte_aba)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 4, 6, 1, 1)

        self.potencial_sg_malte_tbx = QLineEdit(self.malte_aba)
        self.potencial_sg_malte_tbx.setObjectName(u"potencial_sg_malte_tbx")
        self.potencial_sg_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.potencial_sg_malte_tbx, 5, 0, 1, 1)

        self.aproveitamento_malte_tbx = QLineEdit(self.malte_aba)
        self.aproveitamento_malte_tbx.setObjectName(u"aproveitamento_malte_tbx")
        self.aproveitamento_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.aproveitamento_malte_tbx, 5, 1, 1, 3)

        self.poder_diastatico_malte_tbx = QLineEdit(self.malte_aba)
        self.poder_diastatico_malte_tbx.setObjectName(u"poder_diastatico_malte_tbx")
        self.poder_diastatico_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.poder_diastatico_malte_tbx, 5, 4, 1, 2)

        self.proteina_malte_tbx = QLineEdit(self.malte_aba)
        self.proteina_malte_tbx.setObjectName(u"proteina_malte_tbx")
        self.proteina_malte_tbx.setFont(font)

        self.gridLayout.addWidget(self.proteina_malte_tbx, 5, 6, 1, 1)

        self.label_20 = QLabel(self.malte_aba)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 6, 0, 1, 3)

        self.groupBox = QGroupBox(self.malte_aba)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.usar_mostura_malte_cbx = QCheckBox(self.groupBox)
        self.usar_mostura_malte_cbx.setObjectName(u"usar_mostura_malte_cbx")

        self.verticalLayout_18.addWidget(self.usar_mostura_malte_cbx)

        self.usar_fervura_malte_cbx = QCheckBox(self.groupBox)
        self.usar_fervura_malte_cbx.setObjectName(u"usar_fervura_malte_cbx")

        self.verticalLayout_18.addWidget(self.usar_fervura_malte_cbx)

        self.nao_fermentavel_malte_cbx = QCheckBox(self.groupBox)
        self.nao_fermentavel_malte_cbx.setObjectName(u"nao_fermentavel_malte_cbx")

        self.verticalLayout_18.addWidget(self.nao_fermentavel_malte_cbx)


        self.gridLayout.addWidget(self.groupBox, 6, 6, 2, 1)

        self.observacoes_malte_tbx = QTextEdit(self.malte_aba)
        self.observacoes_malte_tbx.setObjectName(u"observacoes_malte_tbx")

        self.gridLayout.addWidget(self.observacoes_malte_tbx, 7, 0, 1, 6)

        self.cadastro_tabw.addTab(self.malte_aba, "")
        self.adjunto_aba = QWidget()
        self.adjunto_aba.setObjectName(u"adjunto_aba")
        self.gridLayout_3 = QGridLayout(self.adjunto_aba)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_34 = QLabel(self.adjunto_aba)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_3.addWidget(self.label_34, 0, 0, 1, 3)

        self.label_36 = QLabel(self.adjunto_aba)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_3.addWidget(self.label_36, 0, 3, 1, 1)

        self.label_35 = QLabel(self.adjunto_aba)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_3.addWidget(self.label_35, 0, 4, 1, 1)

        self.descricao_adjunto_tbx = QLineEdit(self.adjunto_aba)
        self.descricao_adjunto_tbx.setObjectName(u"descricao_adjunto_tbx")
        self.descricao_adjunto_tbx.setFont(font)

        self.gridLayout_3.addWidget(self.descricao_adjunto_tbx, 1, 0, 1, 3)

        self.tipo_adjunto_cb = QComboBox(self.adjunto_aba)
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.addItem("")
        self.tipo_adjunto_cb.setObjectName(u"tipo_adjunto_cb")
        self.tipo_adjunto_cb.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.tipo_adjunto_cb, 1, 3, 1, 1)

        self.fabricante_adjunto_tbx = QLineEdit(self.adjunto_aba)
        self.fabricante_adjunto_tbx.setObjectName(u"fabricante_adjunto_tbx")
        self.fabricante_adjunto_tbx.setFont(font)

        self.gridLayout_3.addWidget(self.fabricante_adjunto_tbx, 1, 4, 1, 1)

        self.label_37 = QLabel(self.adjunto_aba)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_3.addWidget(self.label_37, 2, 0, 1, 1)

        self.label_33 = QLabel(self.adjunto_aba)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 2, 1, 1, 1)

        self.label_38 = QLabel(self.adjunto_aba)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_3.addWidget(self.label_38, 2, 2, 1, 2)

        self.maximo_por_litro_adjunto_tbx = QLineEdit(self.adjunto_aba)
        self.maximo_por_litro_adjunto_tbx.setObjectName(u"maximo_por_litro_adjunto_tbx")
        self.maximo_por_litro_adjunto_tbx.setFont(font)

        self.gridLayout_3.addWidget(self.maximo_por_litro_adjunto_tbx, 3, 0, 1, 1)

        self.preco_adjunto_tbx = QLineEdit(self.adjunto_aba)
        self.preco_adjunto_tbx.setObjectName(u"preco_adjunto_tbx")
        self.preco_adjunto_tbx.setFont(font)

        self.gridLayout_3.addWidget(self.preco_adjunto_tbx, 3, 1, 1, 1)

        self.indicacao_breve_adjunto_tbx = QLineEdit(self.adjunto_aba)
        self.indicacao_breve_adjunto_tbx.setObjectName(u"indicacao_breve_adjunto_tbx")
        self.indicacao_breve_adjunto_tbx.setFont(font)

        self.gridLayout_3.addWidget(self.indicacao_breve_adjunto_tbx, 3, 2, 1, 3)

        self.label_32 = QLabel(self.adjunto_aba)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 4, 0, 1, 2)

        self.observacoes_adjunto_tbx = QTextEdit(self.adjunto_aba)
        self.observacoes_adjunto_tbx.setObjectName(u"observacoes_adjunto_tbx")

        self.gridLayout_3.addWidget(self.observacoes_adjunto_tbx, 5, 0, 1, 5)

        self.cadastro_tabw.addTab(self.adjunto_aba, "")
        self.levedura_aba = QWidget()
        self.levedura_aba.setObjectName(u"levedura_aba")
        self.gridLayout_4 = QGridLayout(self.levedura_aba)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_39 = QLabel(self.levedura_aba)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 0, 0, 1, 3)

        self.label_44 = QLabel(self.levedura_aba)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_4.addWidget(self.label_44, 0, 3, 1, 1)

        self.label_40 = QLabel(self.levedura_aba)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 0, 4, 1, 2)

        self.label_43 = QLabel(self.levedura_aba)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_4.addWidget(self.label_43, 0, 6, 1, 1)

        self.descricao_levedura_tbx = QLineEdit(self.levedura_aba)
        self.descricao_levedura_tbx.setObjectName(u"descricao_levedura_tbx")
        self.descricao_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.descricao_levedura_tbx, 1, 0, 1, 3)

        self.sigla_levedura_tbx = QLineEdit(self.levedura_aba)
        self.sigla_levedura_tbx.setObjectName(u"sigla_levedura_tbx")
        self.sigla_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.sigla_levedura_tbx, 1, 3, 1, 1)

        self.laboratorio_levedura_tbx = QLineEdit(self.levedura_aba)
        self.laboratorio_levedura_tbx.setObjectName(u"laboratorio_levedura_tbx")
        self.laboratorio_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.laboratorio_levedura_tbx, 1, 4, 1, 2)

        self.preco_levedura_tbx = QLineEdit(self.levedura_aba)
        self.preco_levedura_tbx.setObjectName(u"preco_levedura_tbx")
        self.preco_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.preco_levedura_tbx, 1, 6, 1, 1)

        self.label_42 = QLabel(self.levedura_aba)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_4.addWidget(self.label_42, 2, 0, 1, 1)

        self.label_45 = QLabel(self.levedura_aba)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_4.addWidget(self.label_45, 2, 1, 1, 1)

        self.label_46 = QLabel(self.levedura_aba)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_4.addWidget(self.label_46, 2, 2, 1, 3)

        self.label_47 = QLabel(self.levedura_aba)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_4.addWidget(self.label_47, 2, 5, 1, 1)

        self.label_52 = QLabel(self.levedura_aba)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_4.addWidget(self.label_52, 2, 6, 1, 1)

        self.formato_levedura_cb = QComboBox(self.levedura_aba)
        self.formato_levedura_cb.addItem("")
        self.formato_levedura_cb.addItem("")
        self.formato_levedura_cb.setObjectName(u"formato_levedura_cb")

        self.gridLayout_4.addWidget(self.formato_levedura_cb, 3, 0, 1, 1)

        self.floculacao_levedura_cb = QComboBox(self.levedura_aba)
        self.floculacao_levedura_cb.addItem("")
        self.floculacao_levedura_cb.addItem("")
        self.floculacao_levedura_cb.addItem("")
        self.floculacao_levedura_cb.setObjectName(u"floculacao_levedura_cb")

        self.gridLayout_4.addWidget(self.floculacao_levedura_cb, 3, 1, 1, 1)

        self.viabilidade_levedura_tbx = QLineEdit(self.levedura_aba)
        self.viabilidade_levedura_tbx.setObjectName(u"viabilidade_levedura_tbx")
        self.viabilidade_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.viabilidade_levedura_tbx, 3, 2, 1, 3)

        self.gramas_unidade_levedura_tbx = QLineEdit(self.levedura_aba)
        self.gramas_unidade_levedura_tbx.setObjectName(u"gramas_unidade_levedura_tbx")
        self.gramas_unidade_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.gramas_unidade_levedura_tbx, 3, 5, 1, 1)

        self.celulas_por_pacote_levedura_tbx = QLineEdit(self.levedura_aba)
        self.celulas_por_pacote_levedura_tbx.setObjectName(u"celulas_por_pacote_levedura_tbx")
        self.celulas_por_pacote_levedura_tbx.setFont(font)

        self.gridLayout_4.addWidget(self.celulas_por_pacote_levedura_tbx, 3, 6, 1, 1)

        self.groupBox_4 = QGroupBox(self.levedura_aba)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(280, 100))
        self.atenuacao_maxima_levedura_tbx = QLineEdit(self.groupBox_4)
        self.atenuacao_maxima_levedura_tbx.setObjectName(u"atenuacao_maxima_levedura_tbx")
        self.atenuacao_maxima_levedura_tbx.setGeometry(QRect(10, 60, 101, 29))
        self.atenuacao_maxima_levedura_tbx.setFont(font)
        self.label_48 = QLabel(self.groupBox_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 32, 91, 22))
        self.label_49 = QLabel(self.groupBox_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(142, 30, 71, 22))
        self.atenuacao_minima_levedura_tbx = QLineEdit(self.groupBox_4)
        self.atenuacao_minima_levedura_tbx.setObjectName(u"atenuacao_minima_levedura_tbx")
        self.atenuacao_minima_levedura_tbx.setGeometry(QRect(142, 58, 101, 29))
        self.atenuacao_minima_levedura_tbx.setFont(font)
        self.label_53 = QLabel(self.groupBox_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(114, 55, 21, 41))
        self.label_55 = QLabel(self.groupBox_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(247, 55, 21, 41))

        self.gridLayout_4.addWidget(self.groupBox_4, 4, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.levedura_aba)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(240, 100))
        self.label_50 = QLabel(self.groupBox_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 30, 71, 22))
        self.temperatura_maxima_levedura_tbx = QLineEdit(self.groupBox_3)
        self.temperatura_maxima_levedura_tbx.setObjectName(u"temperatura_maxima_levedura_tbx")
        self.temperatura_maxima_levedura_tbx.setGeometry(QRect(10, 58, 81, 29))
        self.temperatura_maxima_levedura_tbx.setFont(font)
        self.label_51 = QLabel(self.groupBox_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(128, 30, 71, 22))
        self.temperatura_minima_levedura_tbx = QLineEdit(self.groupBox_3)
        self.temperatura_minima_levedura_tbx.setObjectName(u"temperatura_minima_levedura_tbx")
        self.temperatura_minima_levedura_tbx.setGeometry(QRect(128, 58, 81, 29))
        self.temperatura_minima_levedura_tbx.setFont(font)
        self.label_54 = QLabel(self.groupBox_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(94, 55, 21, 41))
        self.label_56 = QLabel(self.groupBox_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(213, 55, 21, 41))

        self.gridLayout_4.addWidget(self.groupBox_3, 4, 2, 1, 4)

        self.groupBox_2 = QGroupBox(self.levedura_aba)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(80, 100))
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.ale_levedura_cbx = QCheckBox(self.groupBox_2)
        self.ale_levedura_cbx.setObjectName(u"ale_levedura_cbx")

        self.verticalLayout_19.addWidget(self.ale_levedura_cbx)

        self.lager_levedura_cbx = QCheckBox(self.groupBox_2)
        self.lager_levedura_cbx.setObjectName(u"lager_levedura_cbx")

        self.verticalLayout_19.addWidget(self.lager_levedura_cbx)


        self.gridLayout_4.addWidget(self.groupBox_2, 4, 6, 1, 1)

        self.label_41 = QLabel(self.levedura_aba)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_4.addWidget(self.label_41, 5, 0, 1, 2)

        self.observacoes_levedura_tbx = QTextEdit(self.levedura_aba)
        self.observacoes_levedura_tbx.setObjectName(u"observacoes_levedura_tbx")

        self.gridLayout_4.addWidget(self.observacoes_levedura_tbx, 6, 0, 1, 7)

        self.cadastro_tabw.addTab(self.levedura_aba, "")
        self.lupulo_aba = QWidget()
        self.lupulo_aba.setObjectName(u"lupulo_aba")
        self.gridLayout_2 = QGridLayout(self.lupulo_aba)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.observacoes_lupulo_tbx = QTextEdit(self.lupulo_aba)
        self.observacoes_lupulo_tbx.setObjectName(u"observacoes_lupulo_tbx")

        self.gridLayout_2.addWidget(self.observacoes_lupulo_tbx, 5, 0, 1, 9)

        self.label_21 = QLabel(self.lupulo_aba)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 0, 7, 1, 2)

        self.label_30 = QLabel(self.lupulo_aba)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 3, 5, 1, 1)

        self.origem_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.origem_lupulo_tbx.setObjectName(u"origem_lupulo_tbx")
        self.origem_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.origem_lupulo_tbx, 1, 4, 1, 3)

        self.fabricante_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.fabricante_lupulo_tbx.setObjectName(u"fabricante_lupulo_tbx")
        self.fabricante_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.fabricante_lupulo_tbx, 1, 7, 1, 2)

        self.label_27 = QLabel(self.lupulo_aba)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 2, 1, 1, 1)

        self.acido_beta_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.acido_beta_lupulo_tbx.setObjectName(u"acido_beta_lupulo_tbx")
        self.acido_beta_lupulo_tbx.setMaximumSize(QSize(100, 16777215))
        self.acido_beta_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.acido_beta_lupulo_tbx, 3, 8, 1, 1)

        self.preco_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.preco_lupulo_tbx.setObjectName(u"preco_lupulo_tbx")
        self.preco_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.preco_lupulo_tbx, 3, 3, 1, 2)

        self.label_28 = QLabel(self.lupulo_aba)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 2, 6, 1, 1)

        self.label_25 = QLabel(self.lupulo_aba)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 0, 4, 1, 3)

        self.descricao_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.descricao_lupulo_tbx.setObjectName(u"descricao_lupulo_tbx")
        self.descricao_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.descricao_lupulo_tbx, 1, 0, 1, 4)

        self.tipo_lupulo_tbx = QComboBox(self.lupulo_aba)
        self.tipo_lupulo_tbx.addItem("")
        self.tipo_lupulo_tbx.addItem("")
        self.tipo_lupulo_tbx.addItem("")
        self.tipo_lupulo_tbx.setObjectName(u"tipo_lupulo_tbx")
        self.tipo_lupulo_tbx.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.tipo_lupulo_tbx, 3, 0, 1, 1)

        self.formato_lupulo_tbx = QComboBox(self.lupulo_aba)
        self.formato_lupulo_tbx.addItem("")
        self.formato_lupulo_tbx.addItem("")
        self.formato_lupulo_tbx.addItem("")
        self.formato_lupulo_tbx.addItem("")
        self.formato_lupulo_tbx.setObjectName(u"formato_lupulo_tbx")
        self.formato_lupulo_tbx.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.formato_lupulo_tbx, 3, 1, 1, 1)

        self.label_23 = QLabel(self.lupulo_aba)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 4, 0, 1, 2)

        self.label_22 = QLabel(self.lupulo_aba)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 2, 3, 1, 2)

        self.label_29 = QLabel(self.lupulo_aba)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 2, 8, 1, 1)

        self.acido_alfa_lupulo_tbx = QLineEdit(self.lupulo_aba)
        self.acido_alfa_lupulo_tbx.setObjectName(u"acido_alfa_lupulo_tbx")
        self.acido_alfa_lupulo_tbx.setMaximumSize(QSize(100, 16777215))
        self.acido_alfa_lupulo_tbx.setFont(font)

        self.gridLayout_2.addWidget(self.acido_alfa_lupulo_tbx, 3, 6, 1, 2)

        self.label_26 = QLabel(self.lupulo_aba)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_24 = QLabel(self.lupulo_aba)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 4)

        self.label_31 = QLabel(self.lupulo_aba)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 3, 2, 1, 1)

        self.cadastro_tabw.addTab(self.lupulo_aba, "")

        self.verticalLayout_17.addWidget(self.cadastro_tabw)

        self.paginacao.addWidget(self.cadastros_pg)
        self.insumos_pg = QWidget()
        self.insumos_pg.setObjectName(u"insumos_pg")
        self.verticalLayout_7 = QVBoxLayout(self.insumos_pg)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.insumos_pg)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(30, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pesquisar_insumo_tbx = QLineEdit(self.frame_3)
        self.pesquisar_insumo_tbx.setObjectName(u"pesquisar_insumo_tbx")
        self.pesquisar_insumo_tbx.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_2.addWidget(self.pesquisar_insumo_tbx)

        self.pesquisar_insumo_btn = QPushButton(self.frame_3)
        self.pesquisar_insumo_btn.setObjectName(u"pesquisar_insumo_btn")
        self.pesquisar_insumo_btn.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_2.addWidget(self.pesquisar_insumo_btn)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.insumos_pg)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.insumos_tbw = QTabWidget(self.frame_5)
        self.insumos_tbw.setObjectName(u"insumos_tbw")
        self.view_malte_tab = QWidget()
        self.view_malte_tab.setObjectName(u"view_malte_tab")
        self.verticalLayout_11 = QVBoxLayout(self.view_malte_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.malte_tb = QTableWidget(self.view_malte_tab)
        if (self.malte_tb.columnCount() < 16):
            self.malte_tb.setColumnCount(16)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(11, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(12, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(13, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(14, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.malte_tb.setHorizontalHeaderItem(15, __qtablewidgetitem23)
        self.malte_tb.setObjectName(u"malte_tb")
        self.malte_tb.setStyleSheet(u"")
        self.malte_tb.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.malte_tb.setDragEnabled(False)
        self.malte_tb.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_11.addWidget(self.malte_tb)

        self.insumos_tbw.addTab(self.view_malte_tab, "")
        self.view_lupulo_tab = QWidget()
        self.view_lupulo_tab.setObjectName(u"view_lupulo_tab")
        self.verticalLayout_12 = QVBoxLayout(self.view_lupulo_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lupulo_tb = QTableWidget(self.view_lupulo_tab)
        if (self.lupulo_tb.columnCount() < 9):
            self.lupulo_tb.setColumnCount(9)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.lupulo_tb.setHorizontalHeaderItem(8, __qtablewidgetitem32)
        self.lupulo_tb.setObjectName(u"lupulo_tb")

        self.verticalLayout_12.addWidget(self.lupulo_tb)

        self.insumos_tbw.addTab(self.view_lupulo_tab, "")
        self.view_levedura_tab = QWidget()
        self.view_levedura_tab.setObjectName(u"view_levedura_tab")
        self.verticalLayout_13 = QVBoxLayout(self.view_levedura_tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.levedura_tb = QTableWidget(self.view_levedura_tab)
        if (self.levedura_tb.columnCount() < 13):
            self.levedura_tb.setColumnCount(13)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(7, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(8, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(9, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(10, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(11, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.levedura_tb.setHorizontalHeaderItem(12, __qtablewidgetitem45)
        self.levedura_tb.setObjectName(u"levedura_tb")

        self.verticalLayout_13.addWidget(self.levedura_tb)

        self.insumos_tbw.addTab(self.view_levedura_tab, "")
        self.view_adjunto_tab = QWidget()
        self.view_adjunto_tab.setObjectName(u"view_adjunto_tab")
        self.verticalLayout_14 = QVBoxLayout(self.view_adjunto_tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.adjunto_tb = QTableWidget(self.view_adjunto_tab)
        if (self.adjunto_tb.columnCount() < 7):
            self.adjunto_tb.setColumnCount(7)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.adjunto_tb.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        self.adjunto_tb.setObjectName(u"adjunto_tb")

        self.verticalLayout_14.addWidget(self.adjunto_tb)

        self.insumos_tbw.addTab(self.view_adjunto_tab, "")

        self.verticalLayout_10.addWidget(self.insumos_tbw)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2)

        self.exportar_insumo_btn = QPushButton(self.frame_6)
        self.exportar_insumo_btn.setObjectName(u"exportar_insumo_btn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/novos_icones/computacao-em-nuvem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportar_insumo_btn.setIcon(icon14)

        self.verticalLayout_9.addWidget(self.exportar_insumo_btn)

        self.importar_insumo_btn = QPushButton(self.frame_6)
        self.importar_insumo_btn.setObjectName(u"importar_insumo_btn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/novos_icones/computacao-em-nuvem (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.importar_insumo_btn.setIcon(icon15)

        self.verticalLayout_9.addWidget(self.importar_insumo_btn)

        self.criar_receita_insumo_btn = QPushButton(self.frame_6)
        self.criar_receita_insumo_btn.setObjectName(u"criar_receita_insumo_btn")
        self.criar_receita_insumo_btn.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.criar_receita_insumo_btn)

        self.editar_insumo_btn = QPushButton(self.frame_6)
        self.editar_insumo_btn.setObjectName(u"editar_insumo_btn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/novos_icones/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editar_insumo_btn.setIcon(icon16)
        self.editar_insumo_btn.setAutoExclusive(False)

        self.verticalLayout_9.addWidget(self.editar_insumo_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 169, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.paginacao.addWidget(self.insumos_pg)

        self.verticalLayout_6.addWidget(self.paginacao)


        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.principal)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(24, 24))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.paginacao.setCurrentIndex(6)
        self.receita_tbw.setCurrentIndex(0)
        self.cadastro_tabw.setCurrentIndex(1)
        self.insumos_tbw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">DevBrew</span></p></body></html>", None))
        self.inicio_btn.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.cadastros_btn.setText(QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.insumos_btn.setText(QCoreApplication.translate("MainWindow", u" Insumos", None))
        self.receitas_btn.setText(QCoreApplication.translate("MainWindow", u"Receitas", None))
        self.parametros_btn.setText(QCoreApplication.translate("MainWindow", u"Parametros", None))
        self.painel_btn.setText(QCoreApplication.translate("MainWindow", u"Painel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.principal_pgtool), QCoreApplication.translate("MainWindow", u"Menu Principal", None))
        self.contato_btn.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.opcoes_pgtool), QCoreApplication.translate("MainWindow", u"Suporte", None))
        self.toggle_btn.setText("")
        self.atualizar_btn.setText("")
        self.save_btn.setText("")
        self.exit_btn.setText("")
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ca610b;\">Este sofware \u00e9 gratu\u00edto!</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:400; color:#ca610b;\">Ajude o desenvolvedor com uma doa\u00e7\u00e3o,</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:400; color:#ca610b;\">assim o sistema pode continuar a evoluir.</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ca610b;\">Nome: </span><span style=\" font-size:16pt; font-style:italic; color:#ca610b;\">Christopher Nicolas Mauricio</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ca610b;\">Chave PIX: 434.127.878-92</span><br/></p><p align=\"center\"><span style=\" font-size:12pt; color:#ca610b;\">Caso necessite de suporte entre em contato pelo email:</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#13bdb2;\">christopher.nicolas.mauricio@gmail.com</span></p></body></html>", None))
        self.tipo_adjunto_cb_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_8.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_8.setPlaceholderText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Receita</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Conex\u00e3o com o Hardware</span></p></body></html>", None))
        self.tipo_adjunto_cb_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_9.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_9.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_9.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_9.setPlaceholderText("")
        self.descricao_adjunto_tbx_40.setPlaceholderText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">IP Raspberry</span></p></body></html>", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Observa\u00e7\u00e3o hist\u00f3rico real mostura</span></p></body></html>", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Observa\u00e7\u00e3o hist\u00f3rico real fervura</span></p></body></html>", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Exibi\u00e7\u00e3o de status operacional", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"  Bomba", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Resistencia Mostura", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Resistencia Fervura", None))
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Parada de emergencia", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Nome</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Cervejeiro</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Vers\u00e3o</span></p></body></html>", None))
        self.descricao_adjunto_tbx_2.setPlaceholderText("")
        self.descricao_adjunto_tbx_3.setPlaceholderText("")
        self.descricao_adjunto_tbx_4.setPlaceholderText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tipo Receita</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Data Cria\u00e7\u00e3o</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tempo Fervura</span></p></body></html>", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Volume Lote (L)</span></p></body></html>", None))
        self.tipo_adjunto_cb_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_3.setPlaceholderText("")
        self.tipo_adjunto_cb_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_4.setPlaceholderText("")
        self.descricao_adjunto_tbx_21.setPlaceholderText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">(V) Pr\u00e9 Fervura</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">(V) P\u00f3s Fervura</span></p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Calculo de Eficiencia", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Mostura</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Volume</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Total</span></p></body></html>", None))
        self.descricao_adjunto_tbx_11.setPlaceholderText("")
        self.descricao_adjunto_tbx_22.setPlaceholderText("")
        self.descricao_adjunto_tbx_23.setPlaceholderText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Anota\u00e7\u00f5es Breve</span></p></body></html>", None))
        self.descricao_adjunto_tbx_9.setPlaceholderText("")
        self.descricao_adjunto_tbx_10.setPlaceholderText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo OG</span></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo FG</span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo IBU</span></p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo ABV</span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Estilo SRM</span></p></body></html>", None))
        self.descricao_adjunto_tbx_29.setPlaceholderText("")
        self.descricao_adjunto_tbx_25.setPlaceholderText("")
        self.descricao_adjunto_tbx_28.setPlaceholderText("")
        self.descricao_adjunto_tbx_30.setPlaceholderText("")
        self.descricao_adjunto_tbx_26.setPlaceholderText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Real OG</span></p></body></html>", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Real FG</span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Real IBU</span></p></body></html>", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Real ABV</span></p></body></html>", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Real SRM</span></p></body></html>", None))
        self.descricao_adjunto_tbx_31.setPlaceholderText("")
        self.descricao_adjunto_tbx_34.setPlaceholderText("")
        self.descricao_adjunto_tbx_32.setPlaceholderText("")
        self.descricao_adjunto_tbx_33.setPlaceholderText("")
        self.descricao_adjunto_tbx_27.setPlaceholderText("")
        self.receita_tbw.setTabText(self.receita_tbw.indexOf(self.basico_receita_aba), QCoreApplication.translate("MainWindow", u"Basico", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Rampas Mostura", None))
        self.pushButton_3.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tempo</span></p></body></html>", None))
        self.pushButton_4.setText("")
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Perfil Mostura</span></p></body></html>", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Perfil Fermenta\u00e7\u00e3o</span></p></body></html>", None))
        self.tipo_adjunto_cb_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_5.setPlaceholderText("")
        self.tipo_adjunto_cb_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_6.setPlaceholderText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Carbonata\u00e7\u00e3o</span></p></body></html>", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">(t) Gr\u00e3os</span></p></body></html>", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">(t) Lupulos</span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tx. Amargor</span></p></body></html>", None))
        self.tipo_adjunto_cb_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb_7.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb_7.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb_7.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb_7.setPlaceholderText("")
        self.descricao_adjunto_tbx_36.setPlaceholderText("")
        self.descricao_adjunto_tbx_37.setPlaceholderText("")
        self.descricao_adjunto_tbx_38.setPlaceholderText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Perfil Mostura</span></p></body></html>", None))
        self.receita_tbw.setTabText(self.receita_tbw.indexOf(self.parametros_receita_aba), QCoreApplication.translate("MainWindow", u"Parametros", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ordem", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"IBU%", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"M\u00e9trica", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Momento", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.receita_tbw.setTabText(self.receita_tbw.indexOf(self.ingredientes_receita_aba), QCoreApplication.translate("MainWindow", u"Ingredientes", None))
        self.receita_tbw.setTabText(self.receita_tbw.indexOf(self.analise_receita_aba), QCoreApplication.translate("MainWindow", u"Analise", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Nome ou descri\u00e7\u00e3o</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Origem</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Fabricante</span></p></body></html>", None))
        self.descricao_malte_tbx.setPlaceholderText("")
        self.origem_malte_tbx.setPlaceholderText("")
        self.fabricante_malte_tbx.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tipo</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Quant. Max%</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Cor SRM</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Pre\u00e7o Kg</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Ext. IBU L/Kg</span></p></body></html>", None))
        self.tipo_malte_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Extrato", None))
        self.tipo_malte_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Gr\u00e3o", None))

        self.tipo_malte_cb.setPlaceholderText("")
        self.qntmax_malte_tbx.setPlaceholderText("")
        self.cor_malte_tbx.setPlaceholderText("")
        self.preco_malte_tbx.setPlaceholderText("")
        self.extibulkg_malte_tbx.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Potencial SG</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Aproveitamento</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">P. Diast\u00e1tico</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Prote\u00edna</span></p></body></html>", None))
        self.potencial_sg_malte_tbx.setPlaceholderText("")
        self.aproveitamento_malte_tbx.setPlaceholderText("")
        self.poder_diastatico_malte_tbx.setPlaceholderText("")
        self.proteina_malte_tbx.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Anota\u00e7\u00f5es e observa\u00e7\u00f5es</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de uso", None))
        self.usar_mostura_malte_cbx.setText(QCoreApplication.translate("MainWindow", u"Usar na mostura", None))
        self.usar_fervura_malte_cbx.setText(QCoreApplication.translate("MainWindow", u"Usar na fervura", None))
        self.nao_fermentavel_malte_cbx.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Ferment\u00e1vel", None))
        self.observacoes_malte_tbx.setPlaceholderText("")
        self.cadastro_tabw.setTabText(self.cadastro_tabw.indexOf(self.malte_aba), QCoreApplication.translate("MainWindow", u"Malte", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Nome ou descri\u00e7\u00e3o</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tipo</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Fabricante</span></p></body></html>", None))
        self.descricao_adjunto_tbx.setPlaceholderText("")
        self.tipo_adjunto_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Aroma", None))
        self.tipo_adjunto_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Bebida alc\u00f3lica", None))
        self.tipo_adjunto_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Dul\u00e7or", None))
        self.tipo_adjunto_cb.setItemText(3, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.tipo_adjunto_cb.setItemText(4, QCoreApplication.translate("MainWindow", u"Infus\u00e3o", None))
        self.tipo_adjunto_cb.setItemText(5, QCoreApplication.translate("MainWindow", u"Suco", None))

        self.tipo_adjunto_cb.setPlaceholderText("")
        self.fabricante_adjunto_tbx.setPlaceholderText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">M\u00e1ximo por litro (g)</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Pre\u00e7o Kg</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Indica\u00e7\u00e3o breve</span></p></body></html>", None))
        self.maximo_por_litro_adjunto_tbx.setPlaceholderText("")
        self.preco_adjunto_tbx.setPlaceholderText("")
        self.indicacao_breve_adjunto_tbx.setPlaceholderText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Anota\u00e7\u00f5es e observa\u00e7\u00f5es</span></p></body></html>", None))
        self.observacoes_adjunto_tbx.setPlaceholderText("")
        self.cadastro_tabw.setTabText(self.cadastro_tabw.indexOf(self.adjunto_aba), QCoreApplication.translate("MainWindow", u"Adjunto", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Nome</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Sigla</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Laborat\u00f3rio</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Pre\u00e7o Un.</span></p></body></html>", None))
        self.descricao_levedura_tbx.setPlaceholderText("")
        self.sigla_levedura_tbx.setPlaceholderText("")
        self.laboratorio_levedura_tbx.setPlaceholderText("")
        self.preco_levedura_tbx.setPlaceholderText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Formato</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Flocula\u00e7\u00e3o</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Viabilidade %</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Gramas Un.</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">C. Pacote</span></p></body></html>", None))
        self.formato_levedura_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Liquido", None))
        self.formato_levedura_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Seco", None))

        self.formato_levedura_cb.setPlaceholderText("")
        self.floculacao_levedura_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.floculacao_levedura_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.floculacao_levedura_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Alta", None))

        self.floculacao_levedura_cb.setPlaceholderText("")
        self.viabilidade_levedura_tbx.setPlaceholderText("")
        self.gramas_unidade_levedura_tbx.setPlaceholderText("")
        self.celulas_por_pacote_levedura_tbx.setPlaceholderText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Atenua\u00e7\u00e3o", None))
        self.atenuacao_maxima_levedura_tbx.setPlaceholderText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">M\u00e1ximo</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Min\u00edmo</span></p></body></html>", None))
        self.atenuacao_minima_levedura_tbx.setPlaceholderText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">%</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">%</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">M\u00e1xima</span></p></body></html>", None))
        self.temperatura_maxima_levedura_tbx.setPlaceholderText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Min\u00edma</span></p></body></html>", None))
        self.temperatura_minima_levedura_tbx.setPlaceholderText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C\u00ba</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">C\u00ba</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Familia", None))
        self.ale_levedura_cbx.setText(QCoreApplication.translate("MainWindow", u"Ale", None))
        self.lager_levedura_cbx.setText(QCoreApplication.translate("MainWindow", u"Lager", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Anota\u00e7\u00f5es e observa\u00e7\u00f5es</span></p></body></html>", None))
        self.observacoes_levedura_tbx.setPlaceholderText("")
        self.cadastro_tabw.setTabText(self.cadastro_tabw.indexOf(self.levedura_aba), QCoreApplication.translate("MainWindow", u"Levedura", None))
        self.observacoes_lupulo_tbx.setPlaceholderText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Fabricante</span></p></body></html>", None))
        self.label_30.setText("")
        self.origem_lupulo_tbx.setPlaceholderText("")
        self.fabricante_lupulo_tbx.setPlaceholderText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Formato</span></p></body></html>", None))
        self.acido_beta_lupulo_tbx.setPlaceholderText("")
        self.preco_lupulo_tbx.setPlaceholderText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">A.Alfa %</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Origem</span></p></body></html>", None))
        self.descricao_lupulo_tbx.setPlaceholderText("")
        self.tipo_lupulo_tbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Ambos", None))
        self.tipo_lupulo_tbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Amargor", None))
        self.tipo_lupulo_tbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Aroma", None))

        self.tipo_lupulo_tbx.setPlaceholderText("")
        self.formato_lupulo_tbx.setItemText(0, QCoreApplication.translate("MainWindow", u"Extrato", None))
        self.formato_lupulo_tbx.setItemText(1, QCoreApplication.translate("MainWindow", u"Ch\u00e1", None))
        self.formato_lupulo_tbx.setItemText(2, QCoreApplication.translate("MainWindow", u"Flor", None))
        self.formato_lupulo_tbx.setItemText(3, QCoreApplication.translate("MainWindow", u"Pelet", None))

        self.formato_lupulo_tbx.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Anota\u00e7\u00f5es e observa\u00e7\u00f5es</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Pre\u00e7o Kg</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">A.Beta %</span></p></body></html>", None))
        self.acido_alfa_lupulo_tbx.setPlaceholderText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Tipo</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#d6d6d6;\">Nome ou descri\u00e7\u00e3o</span></p></body></html>", None))
        self.label_31.setText("")
        self.cadastro_tabw.setTabText(self.cadastro_tabw.indexOf(self.lupulo_aba), QCoreApplication.translate("MainWindow", u"Lup\u00falo", None))
        self.pesquisar_insumo_btn.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_3.setText("")
        ___qtablewidgetitem8 = self.malte_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem9 = self.malte_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Origem", None));
        ___qtablewidgetitem10 = self.malte_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem11 = self.malte_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem12 = self.malte_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Qnt. Max %", None));
        ___qtablewidgetitem13 = self.malte_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cor SRM", None));
        ___qtablewidgetitem14 = self.malte_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem15 = self.malte_tb.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Ext.IBU %", None));
        ___qtablewidgetitem16 = self.malte_tb.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Poten.SG %", None));
        ___qtablewidgetitem17 = self.malte_tb.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Diastatico", None));
        ___qtablewidgetitem18 = self.malte_tb.horizontalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Prote\u00edna %", None));
        ___qtablewidgetitem19 = self.malte_tb.horizontalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Aproveitamento %", None));
        ___qtablewidgetitem20 = self.malte_tb.horizontalHeaderItem(12)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Mostura", None));
        ___qtablewidgetitem21 = self.malte_tb.horizontalHeaderItem(13)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Fervura", None));
        ___qtablewidgetitem22 = self.malte_tb.horizontalHeaderItem(14)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Ferment\u00e1vel", None));
        ___qtablewidgetitem23 = self.malte_tb.horizontalHeaderItem(15)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.insumos_tbw.setTabText(self.insumos_tbw.indexOf(self.view_malte_tab), QCoreApplication.translate("MainWindow", u"Malte", None))
        ___qtablewidgetitem24 = self.lupulo_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem25 = self.lupulo_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Origem", None));
        ___qtablewidgetitem26 = self.lupulo_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem27 = self.lupulo_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem28 = self.lupulo_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Formato", None));
        ___qtablewidgetitem29 = self.lupulo_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Alfa A %", None));
        ___qtablewidgetitem30 = self.lupulo_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Beta A. %", None));
        ___qtablewidgetitem31 = self.lupulo_tb.horizontalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem32 = self.lupulo_tb.horizontalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.insumos_tbw.setTabText(self.insumos_tbw.indexOf(self.view_lupulo_tab), QCoreApplication.translate("MainWindow", u"L\u00fapulo", None))
        ___qtablewidgetitem33 = self.levedura_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem34 = self.levedura_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Sigla", None));
        ___qtablewidgetitem35 = self.levedura_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Laborat\u00f3rio", None));
        ___qtablewidgetitem36 = self.levedura_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem37 = self.levedura_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Formato", None));
        ___qtablewidgetitem38 = self.levedura_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Flocula\u00e7\u00e3o %", None));
        ___qtablewidgetitem39 = self.levedura_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Viabilidade %", None));
        ___qtablewidgetitem40 = self.levedura_tb.horizontalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"(g) pacote", None));
        ___qtablewidgetitem41 = self.levedura_tb.horizontalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Celulas (b-uni)", None));
        ___qtablewidgetitem42 = self.levedura_tb.horizontalHeaderItem(9)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Atenua\u00e7\u00e3o %", None));
        ___qtablewidgetitem43 = self.levedura_tb.horizontalHeaderItem(10)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Temperatura %", None));
        ___qtablewidgetitem44 = self.levedura_tb.horizontalHeaderItem(11)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Fam\u00edlia", None));
        ___qtablewidgetitem45 = self.levedura_tb.horizontalHeaderItem(12)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.insumos_tbw.setTabText(self.insumos_tbw.indexOf(self.view_levedura_tab), QCoreApplication.translate("MainWindow", u"Levedura", None))
        ___qtablewidgetitem46 = self.adjunto_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem47 = self.adjunto_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem48 = self.adjunto_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem49 = self.adjunto_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Max. Litro", None));
        ___qtablewidgetitem50 = self.adjunto_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem51 = self.adjunto_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Indica\u00e7\u00e3o Breve", None));
        ___qtablewidgetitem52 = self.adjunto_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.insumos_tbw.setTabText(self.insumos_tbw.indexOf(self.view_adjunto_tab), QCoreApplication.translate("MainWindow", u"Adjunto", None))
        self.label_2.setText("")
        self.exportar_insumo_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.importar_insumo_btn.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.criar_receita_insumo_btn.setText(QCoreApplication.translate("MainWindow", u"Criar Receita", None))
        self.editar_insumo_btn.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
    # retranslateUi

