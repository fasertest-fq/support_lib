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
        self.label = qw.QLabel()
        self.label.setText(name)
        self.input_f=qw.QLineEdit()
        
        
        self.layout = qw.QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_f)
        
        self.setLayout(self.layout)
        
    def return_info(self, text_type='str'):
        if text_type=='int':
            return {self.label.text(): int(self.input_f.text())}
        return {self.label.text(): self.input_f.text()}
        
class WLine(qw.QWidget):
    """
    multiple InputFields
    """

    def __init__(self, name_list:list):
        super().__init__()
        self.name_list=name_list
        
        self.layout=qw.QHBoxLayout()
        self.setLayout(self.layout)
        
        self.draw_Widgets()
        
    def draw_Widgets(self):
        for name in self.name_list:
            self.layout.addWidget(InputField(name))
            
    def get_info(self, text_type="str"):
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



        
#©created by fasertest-fq in 09.08.2025 17:38
