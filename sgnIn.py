from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLineEdit,QVBoxLayout,
                             QWidget, QPushButton, QLabel,
                             QGridLayout, QCheckBox
                
                             )
from PyQt6.QtGui import QIcon

class NewWindow(QWidget):
    def __init__(self,) -> None:
        super().__init__()
        layout = QVBoxLayout()
        text = QLabel("Ro'xyatdan o'tdingiz!")
        layout.addWidget(text)
        self.setLayout(layout)
        

class MainWindow(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_widget = QWidget()
        
        self.email = QLineEdit()
        self.password = QLineEdit()
        
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.chec = QCheckBox('Bir oyga eslab qolish')
        self.eye = QPushButton()
        self.eye.setCheckable(True)
        self.eye.clicked.connect(self.hide_password)
        
        self.eye.setIcon(QIcon('eye.png'))
        
        self.sign_up = QPushButton("Sign up")
        self.sign_in = QPushButton("Sing in")
        
        
        self.main_layout.addWidget(self.email,0,0)
        self.main_layout.addWidget(self.password,1,0)
        self.main_layout.addWidget(self.eye,1,1)
        self.main_layout.addWidget(self.chec,2,0)
        self.main_layout.addWidget(self.sign_up,3,0)
        self.main_layout.addWidget(self.sign_in,4,0)
        self.sign_in.clicked.connect(self.signIn)

        
            
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
    def hide_password(self,chec):
        if chec:
            self.eye.setIcon(QIcon('eye_open.png'))
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
           
        else:
            self.eye.setIcon(QIcon('eye.png'))
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
           
            
            
    def signIn(self):
       self.sing = NewWindow()
       self.sing.show()
        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()