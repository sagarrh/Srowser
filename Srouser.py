from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class webbrowser(QMainWindow):
    def __init__(self):

        self.window=QWidget()
        self.window.setWindowTitle("Sagarweb Browser")


        self.layout=QVBoxLayout()
        self.horizontal=QHBoxLayout()

        self.url_bar=QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn=QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn=QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn=QPushButton(">")
        self.forward_btn.setMinimumHeight(30)


        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)



        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        self.window.setLayout(self.layout) 
        self.window.show()
    
    def navigate(self,url):
        if not url.startswith('http') or not any(url.endswith(ext) for ext in domain_extensions):
            url='https://www.google.com/search?q='+url
            self.url_bar.setText(url)
            
        self.browser.setUrl(QUrl(url))

domain_extensions = [
    ".com", ".org", ".net", ".edu", ".gov", ".mil", ".biz", ".info", 
    ".mobi", ".name", ".pro", ".coop", ".aero", ".jobs", ".museum", 
    ".travel", ".asia", ".cat", ".tel",".app",".me",".xyz"
]
app=QApplication([])

window=webbrowser()
app.exec_()





