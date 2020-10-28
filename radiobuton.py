import sys
from PyQt5.QtWidgets import  QWidget ,QApplication, QRadioButton,QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazisi = QLabel("Hangi dili daha çok seviyorsunuz ? ")
        #bu bizim radio yazımız
        self.java = QRadioButton("JAVA")
        self.python = QRadioButton("PYTHON")
        self.php = QRadioButton("PHP")
        self.ccc = QRadioButton("C")


        self.yazi_alani  = QLabel("")

        self.buton = QPushButton("GÖNDER")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)
        v_box.addWidget(self.ccc)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.ccc.isChecked(),self.yazi_alani))
        self.setWindowTitle("Radio Buton")
        self.show()
    def click(self,pyhton,java,php,ccc,yazi_alani):
        if pyhton:
            yazi_alani.setText("PYTHON")
        if java:
            yazi_alani.setText("JAVA")
        if php:
            yazi_alani.setText("PHP")
        if ccc:
            yazi_alani.setText("C programlama dili ")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())



#radio button bir çok seçenek sunulup bunlardan bir tanesini seçmen demek
