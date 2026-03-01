from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QFileDialog,
    QLineEdit,
    QLabel,
    QHBoxLayout,
)

from pathlib import Path
import sys
from dataclasses import dataclass, field

@dataclass
class AppState():
    output_dir: Path | None= Path()
    files: list[Path] = field(default_factory = list)
    pass

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # window setting
        self.setWindowTitle("L-classification slip")
        self.resize(800,500)

        # state setting
        self.state: AppState = AppState()

        self._setup_input_file_selection_section()
        self._setup_output_dir_selection_section()

        self.output_dir: Path | None = None

        self._setup_layout()
        # ------------------------- I am a split line \(ow <) -------------------------


    def _setup_input_file_selection_section(self):
        # input part and layout item
        self.input_section = QWidget()
        input_layout = QVBoxLayout(self.input_section)

        # add button
        self.btn_add = QPushButton("Add files")
        self.btn_add.clicked.connect(self.add_files)
        # files list
        self.list_widget = QListWidget()

        # add to layout
        input_layout.addWidget(self.btn_add)
        input_layout.addWidget(self.list_widget)

    def _setup_output_dir_selection_section(self):
        # output directory row, and layout object
        self.output_section = QWidget()
        output_row = QHBoxLayout(self.output_section)

        # label
        output_label = QLabel("Output directory")

        # output edit line
        self.out_path_edit = QLineEdit()
        self.out_path_edit.setReadOnly(True)
        self.out_path_edit.setPlaceholderText("Not selected")
        
        # output button
        self.btn_pick_outdir = QPushButton("Select output directory...")
        self.btn_pick_outdir.clicked.connect(self.set_output_dir)

        output_row.addWidget(output_label)
        output_row.addWidget(self.out_path_edit,1)
        output_row.addWidget(self.btn_pick_outdir)

    def _setup_convert_btn(self):
        self.convert_btn = QPushButton("Convert to A4 file.")
        self.convert_btn.clicked.connect # todo
        pass

    def _setup_layout(self):
        # central widget and layout
        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        # previous setup layouts
        layout.addWidget(self.input_section)
        layout.addWidget(self.output_section)

    def convert_file(self):
        pass
        
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "select file",
            str(Path.home()),
            "All files (*)"
        )
        if not files:
            return
        for f in files:
            p = str(Path(f).resolve())
            self.list_widget.addItem(p)
            self.state.files.append(Path(f).resolve())
    
    def set_output_dir(self):
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select output directory",
        )
        if not dir_path:
            return
        self.output_dir = Path(dir_path).resolve()
        self.out_path_edit.setText(str(self.output_dir))
        self.state.output_dir = Path(dir_path).resolve()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
