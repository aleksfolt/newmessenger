import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QSplitter, QListWidget, QListWidgetItem, \
    QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor


class Client:
    def __init__(self, host, port, name):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.name = name

    def send_message(self, message):
        self.sock.sendall(bytes(message, 'utf-8'))

    def receive_message(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message.startswith('[') and message.endswith(']'):
                    self.name = message[1:-1]
                else:
                    print(message)
            except Exception as e:
                print('[ERROR]', e)
                self.sock.close()
                break


class MainWindow(QMainWindow):

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.messages = {}
        self.initUI()

    def initUI(self):
        # Создание списка чатов
        self.chatList = QListWidget(self)
        self.chatList.addItem(QListWidgetItem('Chat 1'))
        self.chatList.addItem(QListWidgetItem('Chat 2'))
        self.chatList.currentItemChanged.connect(self.changeChat)

        # Создание виджета чата
        self.chat = QTextEdit(self)
        self.chat.setReadOnly(False)  # сделать виджет чата редактируемым
        self.chat.setLineWrapMode(QTextEdit.NoWrap)

        # Создание виджета ввода текста
        self.input = QTextEdit(self)
        self.input.setFixedHeight(50)
        self.input.setLineWrapMode(QTextEdit.NoWrap)  # сделать виджет ввода текста многострочным

        # Создание кнопки отправки сообщения
        sendAction = QAction('Send', self)
        sendAction.setShortcut('Ctrl+Return')
        sendAction.triggered.connect(self.sendMessage)

        # Добавление кнопки отправки сообщения в меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(sendAction)

        # Создание QSplitter для разделения окна на две части
        splitter = QSplitter(Qt.Horizontal, self)
        splitter.addWidget(self.chatList)
        splitter.addWidget(self.chat)

        # Создание QVBoxLayout для расположения виджета ввода текста под QSplitter
        vbox = QVBoxLayout()
        vbox.addWidget(splitter)
        vbox.addWidget(self.input)

        # Создание главного QHBoxLayout для добавления VBox и выравнивания по вертикали
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.setAlignment(Qt.AlignTop)

        # Создание QWidget для установки в качестве центрального виджета
        centralWidget = QWidget(self)
        centralWidget.setLayout(hbox)
        self.setCentralWidget(centralWidget)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Messenger')
        self.show()

    def changeChat(self, current, previous):
        current_chat = class MainWindow(QMainWindow):

            def __init__(self, client):
                super().__init__()
                self.client = client
                self.messages = {}
                self.current_chat = None
                self.initUI()

            def initUI(self):
                # Создание списка чатов
                self.chatList = QListWidget(self)
                self.chatList.addItem(QListWidgetItem('Chat 1'))
                self.chatList.addItem(QListWidgetItem('Chat 2'))
                self.chatList.currentItemChanged.connect(self.changeChat)

                # Создание виджета чата
                self.chat = QTextEdit(self)
                self.chat.setReadOnly(False)  # сделать виджет чата редактируемым
                self.chat.setLineWrapMode(QTextEdit.NoWrap)

                # Создание виджета ввода текста
                self.input = QTextEdit(self)
                self.input.setFixedHeight(50)
                self.input.setLineWrapMode(QTextEdit.NoWrap)  # сделать виджет ввода текста многострочным

                # Создание кнопки отправки сообщения
                sendAction = QAction('Send', self)
                sendAction.setShortcut('Ctrl+Return')
                sendAction.triggered.connect(self.sendMessage)

                # Добавление кнопки отправки сообщения в меню
                menubar = self.menuBar()
                fileMenu = menubar.addMenu('&File')
                fileMenu.addAction(sendAction)

                # Создание QSplitter для разделения окна на две части
                splitter = QSplitter(Qt.Horizontal, self)
                splitter.addWidget(self.chatList)
                splitter.addWidget(self.chat)

                # Создание QVBoxLayout для расположения виджета ввода текста под QSplitter
                vbox = QVBoxLayout()
                vbox.addWidget(splitter)
                vbox.addWidget(self.input)

                # Создание главного QHBoxLayout для добавления VBox и выравнивания по вертикали
                hbox = QHBoxLayout()
                hbox.addLayout(vbox)
                hbox.setAlignment(Qt.AlignTop)

                # Создание QWidget для установки в качестве центрального виджета
                centralWidget = QWidget(self)
                centralWidget.setLayout(hbox)
                self.setCentralWidget(centralWidget)

                self.setGeometry(300, 300, 500, 500)
                self.setWindowTitle('Messenger')
                self.show()

            def changeChat(self, current, previous):
                self.current_chat = current.text()
                if self.current_chat not in self.messages:
                    self.messages[self.current_chat] = []
                self.displayMessages()

            def displayMessages(self):
                self.chat.clear()
                for message in self.messages[self.current_chat]:
                    self.chat.append(message)

            def sendMessage(self):
                message = self.input.toPlainText().strip()
                if message:
                    self.client.send_message(f"{self.current_chat}: {self.client.name}: {message}")
                    self.messages[self.current_chat].append(f"{self.client.name}: {message}")
                    self.input.clear()
                    self.displayMessages()
                    self.current_chat = current.text()
                    if self.current_chat not in self.messages:
                        self.messages[self.current_chat] = ''

                    self.chat.setPlainText(self.messages[self.current_chat])

                def sendMessage(self):
                    message = self.input.toPlainText()
                    self.input.clear()
                    if message:
                        full_message = f'[{self.current_chat}] {self.client.name}: {message}\n'
                        self.client.send_message(full_message)

                def receiveMessage(self, message):
                    chat_name = message.split(']')[0][1:]
                    if chat_name not in self.messages:
                        self.messages[chat_name] = ''
                    self.messages[chat_name] += message
                    if chat_name == self.current_chat:
                        self.chat.setPlainText(self.messages[chat_name])

                def startClient(self):
                    thread = threading.Thread(target=self.client.receive_message)
                    thread.daemon = True
                    thread.start()

                def closeEvent(self, event):
                    self.client.send_message('exit')
                    self.client.sock.close()
                    event.accept()

if name == 'main':
app = QApplication(sys.argv)
client = Client('localhost', 8000, 'User')
window = MainWindow(client)
window.startClient()
sys.exit(app.exec_())



