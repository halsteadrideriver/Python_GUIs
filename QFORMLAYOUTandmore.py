import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello app")
        form = qtw.QFormLayout()
        self.setLayout(form)
        #adding contents to the layout
        label_1 = qtw.QLabel("This is form layout")
        label_1.setFont(qtg.QFont('Helvetica',18))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        
        # adding rows in the layout
        form.addRow(label_1)
        form.addRow("First name", f_name)
        form.addRow("Last name", l_name)
        form.addRow(qtw.QPushButton("Press me",clicked = lambda:Press_it()))
        
        
        self.show()
        def Press_it():
            label_1.setText(f'Yo clicked,{f_name.text()} {l_name.text()}')
        
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()