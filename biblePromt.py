# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biblePromt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel,QModelIndex, Qt, QItemSelectionModel
from PyQt5.QtGui import QFont
import json
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 613)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("ex) 창 1 2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_search_clicked)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 50, 341, 131))
        self.listView.setObjectName("listView")
        self.listView.clicked.connect(self.on_item_clicked)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 470, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 450, 71, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 180, 341, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 470, 231, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_show_clicked)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 500, 160, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_prev_clicked)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 500, 161, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.on_next_clicked)

        self.window = None
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def read(self):
        file_path = 'merged_.json'
        with open(file_path, 'r', encoding='cp949') as file:
            data = json.load(file)
            for key in data.keys():
                try:
                    int(key.split(":")[1])
                except:
                    print(key)

            return data
    def setBibleContext(self, bible):
        self.bibleContents = bible

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "검색"))
        self.label.setText(_translate("Dialog", "출력 모니터"))
        self.pushButton_2.setText(_translate("Dialog", "모니터에 출력하기"))
        self.pushButton_3.setText(_translate("Dialog", "이전 구절"))
        self.pushButton_4.setText(_translate("Dialog", "다음 구절"))

    def on_search_clicked(self):
        txt =self.lineEdit.text().split()
        if len(txt)>2:
            new_dict = self.search_json(txt[0]+txt[1]+":"+txt[2])
            self.addToList(new_dict)
        elif len(txt)>1:
            new_dict = self.search_json(txt[0] + txt[1])
            self.addToList(new_dict)
        elif len(txt) == 1:
            new_dict = self.search_json(txt[0])
            self.addToList(new_dict)



    def on_item_clicked(self,index):
        item_text = index.data(Qt.DisplayRole)
        self.plainTextEdit.setPlainText(self.bibleContents[item_text])
        print(f'클릭된 아이템: {item_text}')

    def addToList(self, bibleJson):
        if len(bibleJson)>0:
            self.listModel = QStringListModel()
            self.listModel.setStringList(bibleJson.keys())
            self.listView.setModel(self.listModel)

    def get_display_info(self,app):
        # 모든 활성화된 스크린 정보 가져오기
        screens = app.screens()

        display_info = []

        for i, screen in enumerate(screens):
            screen_info = {
                'Screen': i + 1,
                'Geometry': screen.geometry(),
                'Available Geometry': screen.availableGeometry(),
                'Physical Size': screen.physicalSize(),
                'Logical DPI': screen.logicalDotsPerInch(),
                'Physical DPI': screen.physicalDotsPerInch(),
            }
            display_info.append(screen_info)

        return display_info

    def set_display_info(self,screens):
        self.comboBox.addItems(screens)
    def on_show_clicked(self):
        screen_index = self.comboBox.currentIndex()
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry(screen_index)
        selected_indexes = self.listView.selectedIndexes()
        if selected_indexes:
            title = selected_indexes[0].data()
            if self.window != None :
                self.window.close()
            self.window = FullScreenWindow(self, screen_index=screen_index, title=title, content=self.plainTextEdit.toPlainText())
            self.window.setGeometry(screen_geometry)
            self.window.showFullScreen()

    def on_prev_clicked(self):
        current_index = self.listView.currentIndex()
        previous_index = current_index.siblingAtColumn(0).siblingAtRow(current_index.row() - 1)

        if previous_index.isValid():
            # 이전 인덱스 선택
            self.listView.selectionModel().clearSelection()
            self.listView.selectionModel().setCurrentIndex(previous_index, QItemSelectionModel.Select)
            self.on_item_clicked(previous_index)
            if self.window != None :
                self.window.updateContent(previous_index.data(), self.bibleContents[previous_index.data()])

    def on_next_clicked(self):
        current_index = self.listView.currentIndex()
        next_index = current_index.siblingAtColumn(0).siblingAtRow(current_index.row() + 1)

        if next_index.isValid():
            # 이전 인덱스 선택
            self.listView.selectionModel().clearSelection()
            self.listView.selectionModel().setCurrentIndex(next_index, QItemSelectionModel.Select)
            self.on_item_clicked(next_index)
            if self.window != None:
                self.window.updateContent(next_index.data(), self.bibleContents[next_index.data()])


    def search_json(self, keyword):
        new_dict = {}
        for key in self.bibleContents.keys():
            if keyword in key:
                new_dict[key] = self.bibleContents[key]
        return new_dict

class FullScreenWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, screen_index=0,title="", content=""):
        super(FullScreenWindow, self).__init__()
        self.parent = parent
        self.screen_index = screen_index
        self.initUI(title, content)
    def initUI(self,title,content):
        self.setWindowTitle('Full Screen Presentation')
        self.setStyleSheet('background-color: black;')
        # QLabel을 사용하여 전체 화면에 텍스트를 표시
        self.setMaximumSize(1920, 1080)
        self.titleLbl =QtWidgets.QLabel(title, self)
        font = QFont()
        font.setPointSize(50)
        self.titleLbl.setFont(font)
        self.titleLbl.setStyleSheet('color:white; margin-bottom: 15px;')
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.contentLbl = QtWidgets.QLabel(content, self)
        font = QFont()
        font.setPointSize(30)
        self.contentLbl.setFont(font)
        self.contentLbl.setStyleSheet('color:white;margin-top: 5px; margin-left:20px; margin-right:20px;')
        self.contentLbl.setWordWrap(True)
        label_ratio = 0.8
        self.contentLbl.setAlignment(Qt.AlignCenter)

        # QVBoxLayout을 사용하여 위젯들을 배치
        layout = QtWidgets.QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.titleLbl)
        layout.addWidget(self.contentLbl)
        layout.addStretch()

        # QVBoxLayout의 margin 없애기

        # QWidget을 사용하여 위젯들을 감싸고, 윈도우의 중앙에 위치시킴
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)
        # QLabel을 전체 화면으로 표시

    def updateContent(self, title, content):
        self.titleLbl.setText(title)
        self.contentLbl.setText(content)


    def keyPressEvent(self, event):
        # ESC 키를 눌렀을 때 윈도우를 닫음
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, a0):
        self.parent.window = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    bible = ui.read()
    ui.setBibleContext(bible)
    ui.addToList(bible)
    screens = ui.get_display_info(app)
    print(screens)
    screen_numbers = []
    for i in range(len(screens)):
        screen_numbers.append('Screen' + str(i+1))
    ui.set_display_info(screen_numbers)

    Dialog.show()
    sys.exit(app.exec_())