# https://wikidocs.net/21935

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QMainWindow, QAction, qApp, QGridLayout, \
    QLabel, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QMessageBox, QTableWidgetItem, QTableView, QTableWidget, \
    QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate, Qt

class MyApp(QMainWindow):

    # 생성자
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    # 가운데 이동 함수
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 테이블 데이터 입력 함수
    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

    # Buy 이벤트 설정
    def buyEvent(self, event):
        reply = QMessageBox.question(self, '구매확인', '구매를 확정하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 테이블
    def bookmark(self):
        # 우측 그리드 - 장바구니 내역 테이블
        bookmark = QTableWidget(self)

        # 우측 그리드 - 장바구니 내역 테이블 - 데이터가져오기

        # 우측 그리드 - 장바구니 내역 테이블 - 테이블 크기 설정
        bookmark.setColumnCount(4)
        bookmark.setRowCount(2)

        bookmark.setHorizontalHeaderLabels(["제품", "상품명", "가격", "제조사"])
        bookmark.horizontalHeaderItem(0).setToolTip("코드...")

        # 우측 그리드 - 장바구니 내역 테이블 - 데이터 입력
        bookmark.setItem(0, 0, QTableWidgetItem("(0,0)"))
        bookmark.setItem(0, 1, QTableWidgetItem("(0,1)"))
        bookmark.setItem(1, 0, QTableWidgetItem("(1,0)"))
        bookmark.setItem(1, 1, QTableWidgetItem("(1,1)"))

        # 컬럼 길이 조정 https://wikidocs.net/36794
        bookmark.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        return bookmark

    # 클릭이벤트 - action method
    def cccc(self):
        print("d")

    def initUI(self):
        # 제목
        self.setWindowTitle('My Kiosk')

        # 메뉴바 설정
        # 나가기
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바 표시(상단)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 화면 레이아웃 조정
        # 절대적 배치
        # label1 = QLabel('Label1', self)
        # label1.move(20, 20)
        # label2 = QLabel('Label2', self)
        # label2.move(20, 60)
        #
        # btn1 = QPushButton('Button1', self)
        # btn1.move(80, 13)
        # btn2 = QPushButton('Button2', self)
        # btn2.move(80, 53)

        # 그리드 레이아웃 ( 옵션 : addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0) )
        widget = QWidget(self)

        grid = QGridLayout(widget)

        # 좌측 그리드
        y = 0
        x = 0
        grid.addWidget(QLabel('상품'), y, 0, 1, 2)
        grid.addWidget(QLabel("d"), 1, 0, 1, 2)


        grid.addWidget(QPushButton("구매 초기화"), y+5, 0, 1, 2) # 장바구니 초기화 버튼

        # 우측 그리드 (세로 0~4층
        grid.addWidget(QLabel('장바구니'), y, 2, 1, 3)
        grid.addWidget(QPushButton("내역 확인"), y, 4, 1, 1)  # 구매 내역 확인 버튼
        grid.addWidget(self.bookmark(), y+1, 2, y+4, 3) # 장바구니 내역 테이블
        grid.addWidget(QPushButton("구매 완료"), y+5, 2, 1, 3) # 구매 버튼
        grid.addWidget(QLabel('합계 : '), y+6, 3, 1, -1)  # 합계 표시


        # 그리드 중앙 배치
        self.setCentralWidget(widget)

        # 상태바 현재시각 표시
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # # 종료 버튼 구성
        # btn = QPushButton('종료', self)
        # btn.move(700, 700)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        # ICON 설정
        self.setWindowIcon(QIcon('web.png'))

        # 창 설정
        self.setGeometry(0, 0, 700, 700)
        self.center() # 가운데로 이동

        # 창 띄우기
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())