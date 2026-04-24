import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QTimer, Qt, QPoint
from PyQt5.QtGui import QPixmap

class Fish(QLabel):
    def __init__(self):
        super().__init__()
        # 画像の読み込み（fish.pngを用意してください）
        self.pixmap = QPixmap("fish.png").scaled(100, 100, Qt.KeepAspectRatio)
        self.setPixmap(self.pixmap)
        
        # ウィンドウ設定：枠なし、背景透明、常に最前面、クリック透過
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 初期位置と速度
        self.pos = QPoint(random.randint(100, 500), random.randint(100, 500))
        self.speed = QPoint(random.choice([-2, 2]), random.choice([-2, 2]))
        self.move(self.pos)
        self.show()

        # タイマーでアニメーション実行
        self.timer = QTimer()
        self.timer.timeout.connect(self.swim)
        self.timer.start(20)

    def swim(self):
        screen = QApplication.primaryScreen().geometry()
        self.pos += self.speed
        
        # 画面端での跳ね返り判定
        if self.pos.x() <= 0 or self.pos.x() >= screen.width() - self.width():
            self.speed.setX(-self.speed.x())
        if self.pos.y() <= 0 or self.pos.y() >= screen.height() - self.height():
            self.speed.setY(-self.speed.y())
            
        self.move(self.pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fish_list = [Fish() for _ in range(1)] # 3匹泳がせる
    sys.exit(app.exec_())

    