import os
import sys
from pathlib import Path

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')

from PyQt6.QtCore import QPoint, QTimer, Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import (
    QApplication,
    QDialogButtonBox,
    QFileDialog,
    QLineEdit,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / 'scripts'
sys.path.insert(0, str(SCRIPTS_DIR))

import flameTracker as ft


def test_version_comes_from_version_file():
    expected = f"v{(PROJECT_ROOT / 'VERSION').read_text(encoding='utf-8').strip()}"
    assert ft.loadVersion() == expected


def test_scale_dialog_measures_known_length(monkeypatch):
    app = QApplication.instance() or QApplication([])
    window = ft.FlameTrackerWindow()
    example_video = (PROJECT_ROOT / 'examples' / 'example.mp4').as_posix()
    monkeypatch.setattr(
        QFileDialog,
        'getOpenFileName',
        staticmethod(lambda *args, **kwargs: (example_video, '')),
    )
    window.openVideo_clicked()
    assert window.frameNumber == 0

    def complete_dialog():
        dialog = app.activeModalWidget()
        assert dialog is not None
        image = dialog.findChild(ft.ScaleImageLabel)
        assert image is not None
        length = next(
            widget
            for widget in dialog.findChildren(QLineEdit)
            if widget.placeholderText() == 'Known length'
        )
        QTest.mouseClick(
            image,
            Qt.MouseButton.LeftButton,
            pos=QPoint(20, 20),
        )
        QTest.mouseClick(
            image,
            Qt.MouseButton.LeftButton,
            pos=QPoint(120, 20),
        )
        length.setText('10')
        buttons = dialog.findChild(QDialogButtonBox)
        ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        assert ok_button.isEnabled()
        ok_button.click()

    QTimer.singleShot(100, complete_dialog)
    window.measureScaleBtn_clicked(False)

    assert float(window.scaleIn.text()) > 0
    assert window.unitScale == 'mm'
    window.close()
