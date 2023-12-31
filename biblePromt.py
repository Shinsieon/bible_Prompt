# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biblePromt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QItemSelectionModel
from PyQt5.QtGui import QFont
import json
class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 450)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 260, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("ex) 창 1 2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 70, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_search_clicked)
        self.listView = QtWidgets.QListWidget(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 50, 150, 131))
        self.listView.setObjectName("listView")
        self.listView.clicked.connect(self.on_item_clicked)

        self.moveToFavButton = QtWidgets.QPushButton(Dialog)
        self.moveToFavButton.setGeometry(QtCore.QRect(160, 100, 40, 30))
        self.moveToFavButton.setObjectName("moveToFav")
        self.moveToFavButton.clicked.connect(self.on_move_clicked)

        self.favView = QtWidgets.QListWidget(Dialog)
        self.favView.setGeometry(QtCore.QRect(200, 50, 150, 130))
        self.favView.setObjectName("favoriteView")
        self.favView.clicked.connect(self.on_fav_item_clicked)
        self.favView.doubleClicked.connect(self.on_fav_item_double_clicked)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 340, 260, 20))
        self.comboBox.setObjectName("comboBox")
        self.showLbl = QtWidgets.QLabel(Dialog)
        self.showLbl.setGeometry(QtCore.QRect(10, 340, 70, 20))
        self.showLbl.setObjectName("label")
        self.bibleContentEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.bibleContentEdit.setGeometry(QtCore.QRect(10, 180, 340, 100))
        self.bibleContentEdit.setObjectName("bibleContentEdit")

        self.sizeLbl = QtWidgets.QLabel(Dialog)
        self.sizeLbl.setGeometry(QtCore.QRect(10, 365, 50, 20))
        self.sizeLbl.setText("화면 크기")

        self.widthSize = QtWidgets.QLineEdit(Dialog)
        self.widthSize.setText("1920")
        self.widthSize.setGeometry(QtCore.QRect(90, 365, 40, 20))

        self.heightSize = QtWidgets.QLineEdit(Dialog)
        self.heightSize.setText("1080")
        self.heightSize.setGeometry(QtCore.QRect(140, 365, 40, 20))

        self.fullCheck = QtWidgets.QCheckBox(Dialog)
        self.fullCheck.setText("전체")
        self.fullCheck.setGeometry(QtCore.QRect(185, 365, 50, 20))

        self.fontLbl = QtWidgets.QLabel(Dialog)
        self.fontLbl.setGeometry(QtCore.QRect(240, 365, 50, 20))
        self.fontLbl.setText("글씨 크기")

        self.fontSize = QtWidgets.QLineEdit(Dialog)
        self.fontSize.setGeometry(QtCore.QRect(300, 365, 50, 20))
        self.fontSize.setText("50")


        self.showButton = QtWidgets.QPushButton(Dialog)
        self.showButton.setGeometry(QtCore.QRect(10, 390, 340, 30))
        self.showButton.setObjectName("showButton")
        self.showButton.clicked.connect(self.on_show_clicked)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 300, 170, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_prev_clicked)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 300, 170, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.on_next_clicked)

        self.publisher = QtWidgets.QLabel(Dialog)
        self.publisher.setGeometry(QtCore.QRect(10, 420, 340, 30))
        self.publisher.setText("개발자 연락처 : coolguysiun@naver.com")

        self.window = None
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def read(self):
        file_path = 'bible.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    def setBibleContext(self, bible):
        self.bibleContents = bible

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "성경말씀 프롬프트"))
        self.pushButton.setText(_translate("Dialog", "검색"))
        self.showLbl.setText(_translate("Dialog", "출력 모니터"))
        self.showButton.setText(_translate("Dialog", "모니터에 출력하기"))
        self.pushButton_3.setText(_translate("Dialog", "이전 구절"))
        self.pushButton_4.setText(_translate("Dialog", "다음 구절"))
        self.moveToFavButton.setText(_translate("Dialog", "즐찾"))

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
        else :
            new_dict = self.addToList(self.bibleContents)



    def on_item_clicked(self,index):
        item_text = index.data(Qt.DisplayRole)
        self.bibleContentEdit.setPlainText(self.bibleContents[item_text])

    def on_fav_item_clicked(self, index):
        item_text = index.data(Qt.DisplayRole)
        self.bibleContentEdit.setPlainText(self.bibleContents[item_text])
        find_index = 0
        for index in range(self.listView.count()):
            item = self.listView.item(index)
            if item.text() == item_text:
                find_index = index
                break

        self.listView.setCurrentRow(find_index)

    def on_fav_item_double_clicked(self, index):
        selected_item = self.favView.currentItem()

        if selected_item is not None:
            # 아이템 제거
            row = self.favView.row(selected_item)
            self.favView.takeItem(row)
    def on_move_clicked(self):
        current_index = self.listView.currentIndex()
        item_text = current_index.data()
        list_item = QtWidgets.QListWidgetItem(current_index.data())

        for index in range(self.favView.count()):
            item = self.favView.item(index)
            if item.text() == item_text:
                return

        self.favView.addItem(list_item)

    def addToList(self, bibleJson):
        self.listView.clear()
        if len(bibleJson)>0:
            for i in bibleJson:
                item = QtWidgets.QListWidgetItem(i)
                self.listView.addItem(item)

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
                self.window.updateContent(title, self.bibleContentEdit.toPlainText())
            else:
                self.window = FullScreenWindow(self, self.widthSize.text(), self.heightSize.text(), self.fontSize.text(), screen_index=screen_index, title=title, content=self.bibleContentEdit.toPlainText())
                self.window.setGeometry(screen_geometry)
                if self.fullCheck.isChecked():
                    self.window.showFullScreen()
                else :
                    self.window.show()

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
    def __init__(self, parent, width, height, fontSize, screen_index=0,title="", content=""):
        super(FullScreenWindow, self).__init__()
        self.parent = parent
        self.screen_index = screen_index
        self.initUI(width, height, fontSize, title, content)
    def initUI(self,width, height, fontSize, title,content):
        self.setWindowTitle('Full Screen Presentation')
        self.setStyleSheet('background-color: black;')
        # QLabel을 사용하여 전체 화면에 텍스트를 표시
        self.setMaximumSize(int(width), int(height))
        self.titleLbl =QtWidgets.QLabel(title, self)
        font = QFont()
        font.setPointSize(int(fontSize))
        self.titleLbl.setFont(font)
        self.titleLbl.setStyleSheet('color:white; margin-bottom: 15px;')
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.contentLbl = QtWidgets.QLabel(content, self)
        font = QFont()
        font.setPointSize(int(int(fontSize) * 0.6))
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

        elif event.key() == Qt.Key_Left:
            self.parent.on_prev_clicked()
        elif event.key() == Qt.Key_Right:
            self.parent.on_next_clicked()

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
    screen_numbers = []
    for i in range(len(screens)):
        screen_numbers.append('Screen' + str(i+1))
    ui.set_display_info(screen_numbers)

    Dialog.show()
    sys.exit(app.exec_())
