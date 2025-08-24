import PyQt6.QtWidgets as qw

class WarningWindow(qw.QWidget):
    def __init__(self, e):
        super().__init__()
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Warning')
        self._label = qw.QLabel()
        self._label.setText(e)
        
        self._button = qw.QPushButton(' Ok ', self)
        self._button.clicked.connect(self.close)
        
        self._layout = qw.QVBoxLayout()
        self._layout.addWidget(self._label)
        self._layout.addWidget(self._button)
        
        self.setLayout(self._layout)
        
        
        
#©created by fasertest-fq in 24.08.2025 19:36
