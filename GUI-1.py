import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi app") # Creating a title name.
        self.setLayout(qtw.QVBoxLayout()) #Creating a vertical box layout.
        my_label = qtw.QLabel("Hellow world") # Creating a label .
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)
        '''#Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)'''
        '''
        #Create a combo box
        my_combo = qtw.QComboBox(self,editable = True,insertPolicy = qtw.QComboBox.InsertAtTop)
        my_combo.addItem("Halstead")
        my_combo.addItem("Anderson")
        my_combo.addItem("Powell")
        my_combo.addItem("Antony")
        my_combo.addItem("Jessy")
        my_combo.addItems(["One","Two","Three"]) # To add more items together using list .
        my_combo.insertItem(5,"Joshua") # inset one item inbetween.
        my_combo.insertItems(6,["Joana","Maggie","Immu"])
        self.layout().addWidget(my_combo)'''
        
        '''
        #Create a spin box which is numeric control as in labview.
        my_spin = qtw.QSpinBox(self,value = 0 , maximum = 5000 , minimum = 0 ,singleStep = 1, prefix = "#",suffix = "!!!")
        #my_spin = qtw.QDoubleSpinBox(self,value = 0 , maximum = 5000 , minimum = 0 , singleStep = 1.1, prefix = "#",suffix = "!!!")
        self.layout().addWidget(my_spin)'''
        
        #Create a text box
        my_text = qtw.QTextEdit(self,lineWrapMode = qtw.QTextEdit.FixedColumnWidth,lineWrapColumnOrWidth = 50,placeholderText = 'Hello' , readOnly = False)
        self.layout().addWidget(my_text)
        #Create a button
        my_button = qtw.QPushButton("Press Me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()# To show the app
        def press_it():
            ''' For my_entry entry box
            my_label.setText(f'Hello {my_entry.text()}') # Create a text
            my_entry.setText("")'''
            '''my_label.setText(f'Your Choice is {my_combo.currentText()}')  # for combo box '''
            '''my_label.setText(f'Your Choice is {my_spin.value()}')  # for spin box.'''
            my_label.setText(f'Your Choice is {my_text.toPlainText()}')
            
        
app = qtw.QApplication([])
mw = MainWindow()

app.exec_() 