from PySide6.QtWidgets import QMainWindow, QTabWidget, QMenu, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QAction, QKeySequence
from PySide6.QtCore import Slot
from .graph_editor import GraphEditor
from ..ir import Model, OnnxImport, OnnxExport
import os
import onnx
import onnx.checker


class MainWindow(QMainWindow):
    def __init__(self, irm: Model | None, path: str | None, parent=None):
        super().__init__(parent)
        self._imp = OnnxImport()
        self._exp = OnnxExport()

        self.setWindowIcon(QIcon(":/img/appicon.ico"))
        self.resize(800, 600)
        self.initActions()

        self._path = ''
        self.openFile(irm, path)

    def add_graph_tab(self, graph_editor, name: str = None):
        self.tab_widget.addTab(
            graph_editor, graph_editor.name if name is None else name)

    def initActions(self):
        def addMenu(name: str, menu: QMenu = None):
            if menu is None:
                return self.menuBar().addMenu(name)
            else:
                return menu.addMenu(name)

        def addAction(menu: QMenu, name: str, fn):
            act = QAction(self)
            act.setText(name)
            act.triggered.connect(fn)
            menu.addAction(act)
            return act
        # File
        menu = addMenu('File')
        act = addAction(menu, "Open File", self.fileOpenSlot)
        act.setStatusTip("Open an exist onnx file")
        act.setShortcut(QKeySequence('Ctrl+o'))
        act = addAction(menu, "Save", self.fileSaveSlot)
        act.setStatusTip("Save this onnx file")
        act.setShortcut(QKeySequence('Ctrl+s'))
        act = addAction(menu, "Save as", self.fileSaveAsSlot)
        act.setStatusTip("Save this onnx file as new file")
        act.setShortcut(QKeySequence('Ctrl+e'))

    def openFile(self, irm: Model | None, path: str | None):
        if path is None:
            path = ''
            self._path = path
        elif irm is None:
            m = onnx.load(path)
            try:
                onnx.checker.check_model(m)
            except Exception as e:
                QMessageBox.warning(self, "onnx checker error", str(e))
            irm = self._imp(path)
        if not path.startswith('(') and len(path) > 0:
            path = '(' + path + ')'
        self.setWindowTitle('OnnxEditor' + path)
        if irm is None:
            irm = Model()
        self._irm = irm
        self._ge = GraphEditor(irm.graph)
        self.setCentralWidget(self._ge)

    @Slot()
    def fileOpenSlot(self):
        path = QFileDialog.getOpenFileName(
            self, "open onnx file", "/", '*.onnx')
        if path is None or len(path[0]) == 0:
            return
        else:
            self.openFile(None, path[0])

    @Slot()
    def fileSaveSlot(self):
        if len(self._path) == 0:
            self.fileSaveAsSlot()
        else:
            m = self._exp(self._irm, self._path)
            try:
                onnx.checker.check_model(m)
            except Exception as e:
                QMessageBox.warning(self, "onnx checker error", str(e))

    @Slot()
    def fileSaveAsSlot(self):
        if len(self._path) == 0:
            self._path = "/"
        else:
            self._path = os.path.dirname(self._path)
        path = QFileDialog.getSaveFileName(
            self, "save onnx file", self._path, '*.onnx')
        if path is None or len(path[0]) == 0:
            return
        else:
            m = self._exp(self._irm, path[0])
            try:
                onnx.checker.check_model(m)
            except Exception as e:
                QMessageBox.warning(self, "onnx checker error", str(e))
