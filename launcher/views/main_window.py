from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from launcher.services.library import load_games

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Launcher")
        self.resize(960, 600)

        central = QWidget(self)
        layout = QHBoxLayout(central)

        self.list = QListWidget()
        self.detail = QLabel("Chọn 1 game ở danh sách bên trái")
        self.detail.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.play_btn = QPushButton("Play")

        left = QVBoxLayout()
        left.addWidget(QLabel("Library"))
        left.addWidget(self.list)

        right = QVBoxLayout()
        right.addWidget(QLabel("Details"))
        right.addWidget(self.detail, 1)
        right.addWidget(self.play_btn, 0, Qt.AlignRight)

        layout.addLayout(left, 1)
        layout.addLayout(right, 2)
        self.setCentralWidget(central)

        self._bind()

    def _bind(self):
        self.games = load_games()
        for g in self.games:
            self.list.addItem(g.name)
        self.list.currentRowChanged.connect(self._on_select)
        self.play_btn.clicked.connect(self._on_play)

    def _on_select(self, idx: int):
        if idx < 0 or idx >= len(self.games): return
        g = self.games[idx]
        txt = f"Name: {g.name}\nPlatform: {g.platform}\nTags: {', '.join(g.tags) or '—'}\nExe: {g.exe_path or '—'}\nWorkDir: {g.work_dir or '—'}\nArgs: {g.args or '—'}"
        self.detail.setText(txt)

    def _on_play(self):
        # sẽ triển khai ở Bước 10 (Windows: chạy .exe thật; Mac: mô phỏng)
        self.statusBar().showMessage("Play clicked (not implemented yet)", 2500)
