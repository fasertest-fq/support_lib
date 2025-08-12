#support templates for easy create pyqt5 gui interface.

import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qgi
import PyQt5.QtCore as qc


class InputField(qw.QWidget):
    """
    textline with description for input information.
    """

    def __init__(self, name:str):
        super().__init__()
        self._label = qw.QLabel()
        self._label.setText(name)
        self._input_f=qw.QLineEdit()
        
        
        self._layout = qw.QHBoxLayout()
        self._layout.addWidget(self._label)
        self._layout.addWidget(self._input_f)
        
        self.setLayout(self._layout)
        
    def return_info(self, text_type='str') -> dict:
        if text_type=='int':
            return {self._label.text(): int(self._input_f.text())}
        return {self._label.text(): self._input_f.text()}
        
class WLine(qw.QWidget):
    """
    multiple InputFields
    """

    def __init__(self, name_list:list):
        super().__init__()
        self._name_list=name_list
        
        self._layout=qw.QHBoxLayout()
        self.setLayout(self._layout)
        
        self.draw_Widgets()
        
    def draw_Widgets(self):
        for name in self._name_list:
            self._layout.addWidget(InputField(name))
            
    def get_info(self, text_type="str") -> dict:
        #for get information by textline
        widget_arr=self.findChildren(InputField)
        return_dict={}
        for widget_one in widget_arr:
            try:
                temp_dict=widget_one.return_info(text_type)
                return_dict.update(temp_dict)
            except:
                pass
        return return_dict


class FileLine(qw.QWidget):
    """
    For open/save file/directory. 
    """

    def __init__(self, name:str, mode:str):
        super().__init__()
        
        self._name=name
        self._mode=mode
        self.filename=None
        self.directory=None
        
        self._label=qw.QLabel()
        self._label.setText(name)
        self._textline=qw.QLineEdit()
        self._button=qw.QPushButton('Выбрать', self) 
        self._button.clicked.connect(self.file_function)
        
        self._layout=qw.QGridLayout()
        self._layout.addWidget(self._label, 0, 0, 1, 2)
        self._layout.addWidget(self._textline, 1, 0, 1, 2)
        self._layout.addWidget(self._button, 1, 2, 1, 1)
        
        self.setLayout(self._layout)
        
    def file_function(self):
        if self._mode=='openFile':
            self.filename, _ = qw.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
            self._textline.insert(self.filename)
            return self.filename
        elif self._mode=='openDir':
            self.directory = qw.QFileDialog.getExistingDirectory(self, "Select Directory")
            self._textline.insert(self.directory)
            return self.directory
        elif self._mode=='saveFile':
            self.filename, _ = qw.QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)")
            self._textline.insert(self.filename)
            return self.filename
        return None
        
    def get_info(self) -> dict:
        if self._mode=='openFile' or self._mode=='saveFile':
            return {self._mode: self.filename}
        elif self._mode=='openDir':
            return {self._mode: self.directory}
        return {"Error": None}
            
        
        
        
        
        
#©created by fasertest-fq in 12.08.2025 22:22
