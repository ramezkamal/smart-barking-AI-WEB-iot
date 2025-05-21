import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette, QFontDatabase  # إضافة QFontDatabase

# تكوين الألوان الرئيسية
PRIMARY_COLOR = "#2E86C1"
SECONDARY_COLOR = "#3498DB"
ACCENT_COLOR = "#45B39D"
DANGER_COLOR = "#E74C3C"
SUCCESS_COLOR = "#28B463"

class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # تصميم الخلفية
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2C3E50, stop:1 #4CA1AF)"
        palette.setColor(QPalette.Window, QColor(44, 62, 80))
        self.setPalette(palette)

        # التخطيط الرئيسي
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        # عنوان التطبيق
        title = QLabel("🅿️ نظام إدارة المواقف الذكي")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setStyleSheet(f"color: {PRIMARY_COLOR};")
        layout.addWidget(title)

        # حاوية النموذج (تصميم كرت)
        form_container = QWidget()
        form_container.setStyleSheet(f"""
            background: white;
            border-radius: 15px;
            padding: 30px;
        """)
        form_layout = QVBoxLayout()

        # حقل اسم المستخدم
        self.username = QLineEdit()
        self.username.setPlaceholderText(" اسم المستخدم 📝")
        self.username.setStyleSheet(f"""
            padding: 10px;
            border: 2px solid {PRIMARY_COLOR};
            border-radius: 8px;
            font-size: 16px;
        """)
        form_layout.addWidget(self.username)

        # حقل كلمة المرور
        self.password = QLineEdit()
        self.password.setPlaceholderText(" كلمة المرور 🔒")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(f"""
            padding: 10px;
            border: 2px solid {PRIMARY_COLOR};
            border-radius: 8px;
            font-size: 16px;
            margin-top: 15px;
        """)
        form_layout.addWidget(self.password)

        # زر تسجيل الدخول
        login_btn = QPushButton("تسجيل الدخول 🔑")
        login_btn.setStyleSheet(f"""
            QPushButton {{
                background: {PRIMARY_COLOR};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
                margin-top: 20px;
            }}
            QPushButton:hover {{
                background: {SECONDARY_COLOR};
            }}
        """)
        login_btn.clicked.connect(self.check_login)
        form_layout.addWidget(login_btn)

        form_container.setLayout(form_layout)
        layout.addWidget(form_container)
        self.setLayout(layout)

    def check_login(self):
        if self.username.text() == "admin" and self.password.text() == "1234":
            self.stacked_widget.setCurrentIndex(1)
        else:
            QMessageBox.critical(self, "שגיאה ❌", "بيانات الدخول غير صحيحة! 🚫")

class ParkingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # تصميم الخلفية
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2C3E50, stop:1 #3498DB)"
        palette.setColor(QPalette.Window, QColor(44, 62, 80))
        self.setPalette(palette)

        # التخطيط الرئيسي
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # عنوان النافذة
        header = QLabel("📊 حالة المواقف الحالية")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet(f"color: {ACCENT_COLOR}; padding: 20px;")
        layout.addWidget(header)

        # شبكة المواقف
        grid_layout = QHBoxLayout()
        grid_layout.setSpacing(20)

        # إنشاء 4 مواقف مع تصميم حديث
        self.spots = []
        for i in range(4):
            spot = QLabel(f"""
                <div style='text-align: center;'>
                    <span style='font-size: 24px;'>🅿️ موقف {i+1}</span><br>
                    <span style='font-size: 40px;'>?</span>
                </div>
            """)
            spot.setStyleSheet(f"""
                background: white;
                border-radius: 15px;
                padding: 30px;
                min-width: 200px;
                min-height: 200px;
            """)
            self.spots.append(spot)
            grid_layout.addWidget(spot)

        layout.addLayout(grid_layout)

        # إضافة تذييل الصفحة
        footer = QLabel("© 2024 نظام إدارة المواقف | جميع الحقوق محفوظة 🛠️")
        footer.setStyleSheet(f"color: {ACCENT_COLOR}; padding: 20px;")
        layout.addWidget(footer)

        self.setLayout(layout)

        # محاكاة تحديث البيانات (لأغراض الاختبار)
        self.timer = QTimer()
        self.timer.timeout.connect(self.simulate_data)
        self.timer.start(2000)

    def simulate_data(self):
        # محاكاة قراءة البيانات (0 = فارغ، 1 = ممتلئ)
        import random
        states = [random.choice([0,1]) for _ in range(4)]
        
        for i, state in enumerate(states):
            if state == 0:
                self.spots[i].setText(f"""
                    <div style='text-align: center;'>
                        <span style='font-size: 24px; color: {SUCCESS_COLOR};'>✅ متاح</span><br>
                        <span style='font-size: 40px;'>🅿️</span>
                    </div>
                """)
            else:
                self.spots[i].setText(f"""
                    <div style='text-align: center;'>
                        <span style='font-size: 24px; color: {DANGER_COLOR};'>❌ ممتلئ</span><br>
                        <span style='font-size: 40px;'>🚗</span>
                    </div>
                """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("نظام إدارة المواقف الذكي 🅿️")
        self.setGeometry(100, 100, 1000, 600)

        # إنشاء الـ Stacked Widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # إضافة النوافذ
        self.login_window = LoginWindow(self.stacked_widget)
        self.parking_window = ParkingWindow()
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.parking_window)

        # تطبيق أنماط عامة
        self.setStyleSheet(f"""
            QLabel {{
                color: white;
            }}
            QPushButton {{
                font-weight: bold;
            }}
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # إذا كان لديك ملفات الخطوط، يمكنك إزالة التعليق عن السطرين التاليين
    # QFontDatabase.addApplicationFont("ds-digital.ttf")
    # QFontDatabase.addApplicationFont("arial.ttf")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())