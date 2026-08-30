import os
import sys
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtGui import QAction as QtAction
from PyQt6.QtWidgets import QApplication, QGroupBox, QLabel, QPushButton


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import flameTracker as ft


def test_language_switch_updates_live_ui_and_preserves_control_values():
    app = QApplication.instance() or QApplication([])
    ft.set_language(ft.ENGLISH)
    window = ft.FlameTrackerWindow()
    manual_action = next(
        action
        for action in window.trackingGroup.actions()
        if action.text() == "Manual tracking"
    )
    manual_action.trigger()

    preview_box = next(
        box for box in window.findChildren(QGroupBox) if box.title() == "Preview box"
    )
    assert window.directionBox.currentText() == "Left to right"
    assert window.directionBox.itemText(0) == "Left to right"

    window.languageChinese.trigger()

    assert preview_box.title() == "预览区"
    assert window.roiOneTxt.text() == "ROI, x:"
    assert QLabel.text(window.roiOneTxt) == "ROI，x："
    assert manual_action.text() == "Manual tracking"
    assert QtAction.text(manual_action) == "手动追踪"
    assert window.directionBox.currentText() == "Left to right"
    assert window.directionBox.itemText(0) == "从左到右"
    assert any(
        button.text() == "开始追踪"
        for button in window.findChildren(QPushButton)
    )

    window.languageEnglish.trigger()
    assert preview_box.title() == "Preview box"
    assert window.directionBox.itemText(0) == "Left to right"
    window.close()


def test_every_tracking_panel_constructs_in_both_languages():
    app = QApplication.instance() or QApplication([])
    for language in (ft.ENGLISH, ft.CHINESE):
        ft.set_language(language)
        window = ft.FlameTrackerWindow()
        for action in window.trackingGroup.actions():
            action.trigger()
            app.processEvents()
            assert window.trackingMethod == action.text()
        window.close()
    ft.set_language(ft.ENGLISH)
