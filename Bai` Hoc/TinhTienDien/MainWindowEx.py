from PyQt6 import QtWidgets, QtCore, QtGui

from MainWindow import Ui_MainWindow

class MainWindowEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center_window()

        # Set up Tab Order
        self.setTabOrder(self.lineEditOld, self.lineEditNew)
        self.setTabOrder(self.lineEditNew, self.lineEditSoHo)
        self.setTabOrder(self.lineEditSoHo, self.lineEditSokWh)
        self.setTabOrder(self.lineEditSokWh, self.pushButtonSHBT)

        # Connect signals to slots
        self.lineEditOld.textChanged.connect(self.update_kwh_usage)
        self.lineEditNew.textChanged.connect(self.update_kwh_usage)
        self.pushButtonSHBT.clicked.connect(self.calculate_shbt)
        self.pushButtonKinhDoanh.clicked.connect(self.calculate_kinh_doanh)
        self.pushButtonnSanXuat.clicked.connect(self.calculate_san_xuat)
        self.pushButton.clicked.connect(self.clear_fields)
        self.pushButtonThoat.clicked.connect(self.close)
        self.pushButtonHuongDan.clicked.connect(self.show_help)

    def center_window(self):
        """Center the main window on the screen."""
        frame_geometry = self.frameGeometry()
        center_point = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def get_input_values(self):
        """Helper function to get values from input fields."""
        try:
            A = int(self.lineEditOld.text())
            B = int(self.lineEditNew.text())
            C = float(self.lineEditSoHo.text())
            if A > B:
                self.label_7.setText("Lỗi: Chỉ số cũ lớn hơn chỉ số mới.")
                return None, None, None
            return A, B, C
        except ValueError:
            self.label_7.setText("Vui lòng nhập đúng định dạng số.")
            return None, None, None

    def update_kwh_usage(self):
        """Automatically update kWh usage when old or new index changes."""
        A = self.lineEditOld.text()
        B = self.lineEditNew.text()
        if A.isdigit() and B.isdigit():
            usage = int(B) - int(A)
            self.lineEditSokWh.setText(str(usage))
        else:
            self.lineEditSokWh.clear()

    def calculate_shbt(self):
        """Calculate the Ladder Cost of Living (SHBT) and display the result."""
        A, B, C = self.get_input_values()
        if A is not None and B is not None and C is not None:
            usage = B - A

            if usage <= 50 * C:
                result = usage * 1484
            elif usage <= 100 * C:
                result = (50 * C * 1484) + (usage - 50 * C) * 1533
            elif usage <= 200 * C:
                result = (50 * C * 1484) + (50 * C * 1533) + (usage - 100 * C) * 1786
            elif usage <= 300 * C:
                result = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + (usage - 200 * C) * 2242
            elif usage <= 400 * C:
                result = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + (100 * C * 2242) + (usage - 300 * C) * 2503
            else:
                result = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + (100 * C * 2242) + (100 * C * 2503) + (usage - 400 * C) * 2587

            self.label_7.setText(f"Tiền SHBT = {int(result)} (VND)")

    def calculate_kinh_doanh(self):
        """Calculate the Business Electricity Price and display the result."""
        A, B, _ = self.get_input_values()
        if A is not None and B is not None:
            usage = B - A
            result = usage * 2320
            self.label_7.setText(f"Tiền Kinh doanh = {int(result)} (VND)")

    def calculate_san_xuat(self):
        """Calculate the Production Electricity Price and display the result."""
        A, B, _ = self.get_input_values()
        if A is not None and B is not None:
            usage = B - A
            result = usage * 1518
            self.label_7.setText(f"Tiền Sản xuất = {int(result)} (VND)")

    def clear_fields(self):
        """Clear the information boxes on the interface and move the cursor to the old index box."""
        self.lineEditOld.clear()
        self.lineEditNew.clear()
        self.lineEditSoHo.clear()
        self.lineEditSokWh.clear()
        self.label_7.clear()
        self.lineEditOld.setFocus()

    def show_help(self):
        """Display a message with the student's name when 'Hướng dẫn' is clicked."""
        QtWidgets.QMessageBox.information(self, "Cảnh báo chúng mày", "Bố Chúng Mày đến rồi đây: Trần Đức Trung Kiên")

