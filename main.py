import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow 
from sudoku import Sudoku


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew_Game.triggered.connect(self.new_game)
        self.ui.actionMy_Game_Help.triggered.connect(self.help)
        self.ui.actionOpen_file.triggered.connect(self.open_file)
        self.ui.actionAbout_my_Game.triggered.connect(self.about)
        self.ui.actionExit.triggered.connect(self.exit)
        self.array=[[None for i in range (9)] for j in range(9)]
        self.new_game()
    
    

    def new_game(self):
        puzzle = Sudoku(3 ,seed=random.randrange(1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                New_cell=QLineEdit()
                self.ui.gridLayout.addWidget(New_cell , i ,j)
                if puzzle.board[i][j] !=None:
                    New_cell.setText(str(puzzle.board[i][j]))
                    New_cell.setReadOnly(True)
                New_cell.textChanged.connect(partial(self.validation , i ,j))
                self.array[i][j]=New_cell

    def open_file(self):
        file_path=QFileDialog.getOpenFileName(self,"Open file...")[0]
        f=open(file_path, "r")
        big_text=f.read()
        rows=big_text.split("/n")
        puzzle_board=[[None for i in range(9)] for j in range(9)]
        for i in range (len(rows)):
            cells=rows[i].split(" ")
            for j in range (len(cells)):
                puzzle_board[i][j]=int(cells[j])

    def help(self):
            msg_box=QMessageBox()
            msg_box.setText("For playing you should enter a number between 1 and 9")
            msg_box.exec_()
    
    def about(self):
        msg_box=QMessageBox()
        msg_box.setText("This project is my first sodoku Game,it writen with python and designed with Qt")
        msg_box.exec_()

    def validation(self,i , j , text):
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.array[i][j].setText("")
            
    def exit(self):
        msg_box=QMessageBox()
        msg_box.setText("Do you want to Exit?")
        msg_box.exec_()
        exit(0)




if __name__ == "__main__":
    app=QApplication(sys.argv)

    main_window=MainWindow()
    main_window.show()
    app.exec_()