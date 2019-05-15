from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QDialog
import functions
import multiprocessing
import sys
import time

multiprocessing.cpu_count()

app = QtWidgets.QApplication(sys.argv)

class MainWIndow(QtWidgets.QMainWindow,QLCDNumber,QDialog):

    def __init__(self,parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.status.text()
        self.setWindowTitle("TEZOS password finder")
        self.ui.StartButton.clicked.connect(self.start_Button_click)

    def start_Button_click(self):
        self.thread = CalcThread()
        self.thread.start()

class CalcThread(QThread):

    def run(self):
        start = self.on_StartButton_click()


    def on_StartButton_click(self):

        pwd_list = []

        while 1:

            found_it = "False"
            L = V = W = X = Y = Z = E = 0
            window.ui.status.setText("creating potential passwords...")

            lsalt_lst = functions.saltmixer(window.ui.lsalt_char.text(), window.ui.lsalt_number.text(),window.ui.lsalt_null.isChecked(),
                                            window.ui.lsalt_char_multible.isChecked())
            esalt_lst = functions.saltmixer(window.ui.esalt_char.text(), window.ui.esalt_number.text(),window.ui.esalt_null.isChecked(),
                                            window.ui.esalt_char_multible.isChecked())
            vsalt_lst = functions.saltmixer(window.ui.vsalt_char.text(), window.ui.vsalt_number.text(),window.ui.vsalt_null.isChecked(),
                                            window.ui.vsalt_char_multible.isChecked())

            if window.ui.comp1_noclue.isChecked() == False:
                comp1_list = window.ui.comp1_input.toPlainText().split()
            else:
                comp1_list = functions.comp_create(window.ui.comp1_char_set.toPlainText(),window.ui.comp1_capitalize_first.isChecked(),
                                                    window.ui.comp1_capitalize_each.isChecked(),window.ui.comp1_capitalize_all.isChecked(),window.ui.comp1_min_char.text(),
                                                    window.ui.comp1_max_char.text(),window.ui.comp1_repeat_char.text())

            if window.ui.comp2_noclue.isChecked() == False:
                comp2_list = window.ui.comp2_input.toPlainText().split()
            else:
                comp2_list = functions.comp_create(window.ui.comp2_char_set.toPlainText(),window.ui.comp2_capitalize_first.isChecked(),
                                                    window.ui.comp2_capitalize_each.isChecked(),window.ui.comp2_capitalize_all.isChecked(),window.ui.comp2_min_char.text(),
                                                    window.ui.comp2_max_char.text(),window.ui.comp2_repeat_char.text())

            comp3_list = window.ui.comp3_input.toPlainText().split()
            comp4_list = window.ui.comp4_input.toPlainText().split()

            email = window.ui.email_input.toPlainText()
            mnemonic = bytes((window.ui.mnemonic_input.toPlainText()),"utf8")
            address = window.ui.address_input.toPlainText()

            max_char_num = int(window.ui.max_char_number.text())
            min_char_num = int(window.ui.min_char_number.text())

            if window.ui.lsalt_char.text() != "":
                L = 1
            if window.ui.vsalt_char.text() != "":
                Z = 1
            if window.ui.esalt_char.text() != "":
                E = 1
            if comp1_list != []:
                comp1_act = True
                V = 1
            if comp2_list != []:
                comp2_act = True
                W = 1
            if comp3_list != []:
                comp3_act = True
                X = 1
            if comp4_list != []:
                comp4_act = True
                Y = 1

            window.ui.lcdNumber.display(functions.pwd_len(lsalt_lst,esalt_lst,vsalt_lst,comp1_list,comp2_list,comp3_list,comp4_list,window,W,X,Y,Z))

            if Z == 1:
                sequ = functions.sequenzerwithvsalt(L, V, W, X, Y, Z, E)

            elif Z == 0:
                sequ = functions.sequenzernovsalt(L, V, W, X, Y, E)

            candidate_count = 0
            candidate_used = 0

            for subset in sequ:
                sequ_list = list(subset)

                for n, i in enumerate(sequ_list):
                    if i == "L":
                        sequ_list[n] = lsalt_lst
                    if i == "V":
                        sequ_list[n] = comp1_list
                    if i == "W":
                        sequ_list[n] = comp2_list
                    if i == "X":
                        sequ_list[n] = comp3_list
                    if i == "Y":
                        sequ_list[n] = comp4_list
                    if i == "Z":
                        sequ_list[n] = vsalt_lst
                    if i == "E":
                        sequ_list[n] = esalt_lst

                received = functions.component_mixer(sequ_list, min_char_num, max_char_num, candidate_count,candidate_used,window,pwd_list)
                candidate_count = received[0]
                candidate_used = received[1]
                pwd_list = received[2]


            window.ui.lcdNumber_used.display(candidate_used)
            window.ui.status.setText("checking potential passwords...")

            start = time.time()
            cpu_use = (multiprocessing.cpu_count())-1
            conn1, conn2 = multiprocessing.Pipe()
            pool = multiprocessing.Pool(cpu_use)
            password = ""

            p = pool.starmap(functions.check, [(password,email, mnemonic, address) for password in pwd_list], chunksize=1000)

            end = time.time()
            print(f'Time to complete: {end - start:.12f}s\n')

            for x in p:
                found_it = x[0]
                password = x[1]

                if found_it == "True":
                    window.ui.status.setText('Your Password is - "' + password + '"')
                    break

            if found_it == "True":
                pool.close()
                pool.join()
                break

            print(candidate_used)
            window.ui.status.setText('Sorry nothing found!')
            pool.close()
            pool.join()
            break

if __name__ == '__main__':
    multiprocessing.freeze_support()
    window = MainWIndow()
    window.show()
    sys.exit(app.exec_())



