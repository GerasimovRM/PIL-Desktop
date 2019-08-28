from collections import OrderedDict
import inspect
import sys
import os

from PIL import Image

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QFileDialog, qApp
from PyQt5.QtWidgets import QMessageBox, QErrorMessage, QTableWidgetItem, QDialog
from PyQt5.QtGui import QPixmap, QImage, QDesktopServices, QCloseEvent
from PyQt5.QtCore import QUrl, QDir, Qt

from ui_PIL import Ui_PILDesktop
from ui_PIL_dialog import Ui_Dialog


sys.path.append(os.getcwd() + "\\Filters")


class PILDesktop(QMainWindow, Ui_PILDesktop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag_save = False
        self.flag_open = False
        self.filename = None
        self.func_dict = dict()
        self.basic_name = self.windowTitle()
        self.dialog_filter = None
        self.image_stack = []

        self.init_graphics_view()
        self.init_buttons()
        self.init_menu()
        self.init_table_widget()
        self.init_filters()

    def init_graphics_view(self):
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)

    def init_buttons(self):
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_save_as.clicked.connect(self.save_as)
        self.pushButton_reset.clicked.connect(self.clear_filters)
        self.pushButton_right.clicked.connect(lambda: self.graphicsView.rotate(90))
        self.pushButton_left.clicked.connect(lambda: self.graphicsView.rotate(-90))
        self.pushButton_zoom_plus.clicked.connect(lambda: self.graphicsView.scale(1.1, 1.1))
        self.pushButton_zoom_minus.clicked.connect(lambda: self.graphicsView.scale(0.9, 0.9))
        self.pushButton_change_parameters.clicked.connect(self.change_parameters)

        self.pushButton_redo.hide()
        self.pushButton_undo.hide()

    def init_menu(self):
        self.actionOpen.triggered.connect(self.open)
        self.actionExit.triggered.connect(self.exit)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionDefault_size.triggered.connect(self.graphicsView.resetTransform)
        self.actionZoom_plus.triggered.connect(lambda: self.graphicsView.scale(1.1, 1.1))
        self.actionZoom_minus.triggered.connect(lambda: self.graphicsView.scale(0.9, 0.9))

        url_help = QUrl("mailto:?to=gerasimov@yandexlyceum.ru&subject=PIL Desktop question")
        self.actionHelp.triggered.connect(lambda: QDesktopServices.openUrl(url_help))

    def init_table_widget(self):
        self.tableWidget.itemClicked.connect(self.table_click)

    def init_filters(self):
        # print(self.tableWidget)
        directory = QDir("Filters")
        for elem in directory.entryList()[2:]:
            if not elem.startswith("__") and elem.endswith(".py"):
                elem = elem[:-3]
                try:
                    func_filter = getattr(__import__(elem, fromlist=[elem]), elem)
                except AttributeError:
                    continue

                args = inspect.getfullargspec(func_filter).args[1:]
                defaults = inspect.getfullargspec(func_filter).defaults
                if defaults is not None and args:
                    self.func_dict[elem] = OrderedDict()
                    for arg, value in zip(args, defaults):
                        self.func_dict[elem][arg] = value

                self.tableWidget.insertRow(self.tableWidget.rowCount())
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(elem))

        self.update_args_filters()

    def update_args_filters(self):
        for i in range(self.tableWidget.rowCount()):
            txt = self.tableWidget.item(i, 0).text()
            try:
                args_str = "; ".join([f"{arg}={value}" for arg, value in self.func_dict[txt].items()])
                self.tableWidget.setItem(i, 1, QTableWidgetItem(args_str))
            except KeyError:
                pass

    def update_args_filter(self, row: int):
        txt = self.tableWidget.item(row, 0).text()
        args_str = "; ".join([f"{arg}={value}" for arg, value in self.func_dict[txt].items()])
        self.tableWidget.setItem(row, 1, QTableWidgetItem(args_str))

    def open(self):
        if not self.flag_open:
            self.graphicsView.viewport().update()
            self.graphicsView.scene().clear()

        self.filename = QFileDialog.getOpenFileName(filter="Image files (*.jpg *.png)\nAny files (*)")[0]
        self.setWindowTitle(self.basic_name + self.filename)
        image = QImage(self.filename)
        item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        self.graphicsView.scene().addItem(item)
        self.graphicsView.show()

        self.flag_open = True

    def save(self):
        if self.flag_open:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Save dialog")
            msg_box.setInformativeText("Do you want to rewrite this file?")
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Save)
            answer = msg_box.exec()
            if answer == QMessageBox.Save:
                item = self.graphicsView.scene().items()[0]
                image = item.pixmap().toImage()
                image.save(self.filename)
                self.flag_save = False
                if self.windowTitle().endswith(' *'):
                    self.setWindowTitle(self.windowTitle()[:-2])
            return answer
        else:
            QErrorMessage(self).showMessage("You don't open the file")

    def save_as(self):
        if self.flag_open:
            self.filename = QFileDialog.getSaveFileName(filter="Image files (*.jpg *.png )\nAny files (*)")[0]
            self.setWindowTitle(self.basic_name + self.filename)
            item = self.graphicsView.scene().items()[0]
            image = item.pixmap().toImage()
            image.save(self.filename)
            self.flag_save = False
            if self.windowTitle().endswith(' *'):
                self.setWindowTitle(self.windowTitle()[:-2])
        else:
            QErrorMessage(self).showMessage("You don't open the file")

    def exit(self):
        if self.flag_save:
            msg_box = QMessageBox()
            msg_box.setInformativeText("Do you want to save your changes?")
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Save)
            answer = msg_box.exec()
            if answer == QMessageBox.Save:
                self.save()
            elif answer == QMessageBox.Cancel:
                # Don't close app if user change is <Cancel>
                return
        qApp.exit()

    def table_click(self, item: QTableWidgetItem):
        if self.flag_open:
            item = self.tableWidget.item(item.row(), 0)
            txt = item.text()
            try:
                func_filter = getattr(__import__(txt, fromlist=[txt]), txt)
            except ModuleNotFoundError:
                QErrorMessage(self).showMessage("Module is crushed!")
                return
            self.use_filter(func_filter)

    def change_parameters(self):
        try:
            item = self.tableWidget.item(self.tableWidget.selectedItems()[0].row(), 0)
        except IndexError:
            QErrorMessage(self).showMessage("Filter is not selected")
            return
        txt = item.text()
        try:
            self.dialog_filter = getattr(__import__(txt, fromlist=[txt]), txt)
        except ModuleNotFoundError:
            QErrorMessage(self).showMessage("Module is not found")
            return
        dialog = Dialog(self)
        if dialog.exec():
            for i in range(dialog.tableWidget.rowCount()):
                arg = dialog.tableWidget.item(i, 0).text()
                value = dialog.tableWidget.item(i, 1).text()
                if value != self.func_dict[self.dialog_filter.__name__][arg]:
                    type_value = type(self.func_dict[self.dialog_filter.__name__][arg])
                    self.func_dict[self.dialog_filter.__name__][arg] = type_value(value)
            self.update_args_filters()
        self.use_filter(self.dialog_filter)

    def use_filter(self, func):
        if self.flag_open:
            pil_image = Image.open(self.filename)
            try:
                try:
                    args = map(lambda x: x[1], list(self.func_dict[func.__name__].items()))
                    pil_image = func(pil_image, *args)
                except KeyError:
                    pil_image = func(pil_image)
            except:
                QErrorMessage(self).showMessage("Bad filter!")
                return

            # ***************** переделать через буфер *****************
            # PIL.Image.Image -> QImage
            pil_image.save("PIL_tmp.jpg")
            image = QImage("PIL_tmp.jpg")
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))

            self.graphicsView.scene().items().clear()
            self.graphicsView.scene().addItem(item)
            self.graphicsView.show()

            if not self.windowTitle().endswith(' *'):
                self.setWindowTitle(self.windowTitle() + ' *')

            self.flag_save = True

    def clear_filters(self):
        image = QImage(self.filename)
        item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        self.graphicsView.scene().addItem(item)
        self.graphicsView.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.flag_save:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Exit dialog")
            msg_box.setInformativeText("Want to save?")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            answer = msg_box.exec()
            if answer == QMessageBox.Yes:
                answer_save = self.save()
                if answer_save == QMessageBox.Save:
                    event.accept()
                else:
                    event.ignore()
            elif answer == QMessageBox.No:
                event.accept()
            else:
                event.ignore()


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, *args):
        super().__init__(*args)
        self.setupUi(self)

        self.parent = args[0]
        self.func = None

        self.init_table_widget()
        self.init_parameters()
        self.init_buttons()

    def init_buttons(self):
        self.pushCancel.clicked.connect(self.close)
        self.pushOk.clicked.connect(self.accept)

    def init_table_widget(self):
        self.parent: PILDesktop
        self.func = self.parent.dialog_filter

    def init_parameters(self):
        self.parent: PILDesktop
        try:
            tmp = self.parent.func_dict[self.func.__name__].items()
        except KeyError:
            return
        for arg, value in tmp:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            item = QTableWidgetItem(arg)
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, item)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(value)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    wnd = PILDesktop()
    wnd.show()
    sys.exit(app.exec())
