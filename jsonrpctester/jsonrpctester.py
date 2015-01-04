import sys

from PySide import QtCore
from PySide import QtGui
from json_syntax_highlighter import JSONSyntaxHighlighter
from ui_jsonrpctester import Ui_MainWindow

class JsonRpcTester(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(JsonRpcTester, self).__init__(parent)

        #build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #set syntax highlighters
        self.syntax_params = JSONSyntaxHighlighter(self.ui.textEditParameters)
        self.syntax_result = JSONSyntaxHighlighter(self.ui.textEditResult)

        #connect signals
        self.ui.pushButtonSend.clicked.connect(self.send)

    @QtCore.Slot()
    def send(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    jsonrpctester = JsonRpcTester()
    jsonrpctester.show()
    sys.exit(app.exec_())
