from PySide import QtCore, QtGui


class JSONSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        """ Constructor
        """
        super(JSONSyntaxHighlighter, self).__init__(parent)

        self.symbol_format = QtGui.QTextCharFormat()
        self.symbol_format.setForeground(QtCore.Qt.red)
        self.symbol_format.setFontWeight(QtGui.QFont.Bold)

        self.name_format = QtGui.QTextCharFormat()
        self.name_format.setForeground(QtCore.Qt.blue)
        self.name_format.setFontWeight(QtGui.QFont.Bold)
        self.name_format.setFontItalic(True)

        self.value_format = QtGui.QTextCharFormat()
        self.value_format.setForeground(QtCore.Qt.darkGreen)

    def highlightBlock(self, text):
        """ Highlight a block of code using the rules outlined in the Constructor
        """
        expression = QtCore.QRegExp("(\\{|\\}|\\[|\\]|\\:|\\,)")
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length, self.symbol_format)
            index = expression.indexIn(text, index + length)

        text.replace("\\\"", "  ")

        expression = QtCore.QRegExp("\".*\" *\\:")
        expression.setMinimal(True)
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length - 1, self.name_format)
            index =expression.indexIn(text, index + length)

        expression = QtCore.QRegExp("\\: *\".*\"")
        expression.setMinimal(True)
        index = expression.indexIn(text)
        while index >= 0:
            length = expression.matchedLength()
            self.setFormat(index, length - 1, self.value_format)
            index = expression.indexIn(text, index + length)
