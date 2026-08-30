"""Runtime English/Simplified-Chinese localization for Flame Tracker.

The tracking code historically uses visible English combo-box values as
control values.  The localized widgets below keep those canonical English
values internally while translating only what the user sees.
"""

from __future__ import annotations

import os
import re
import weakref

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QAction as _QAction
from PyQt6.QtWidgets import (
    QCheckBox as _QCheckBox,
    QComboBox as _QComboBox,
    QFileDialog as _QFileDialog,
    QGroupBox as _QGroupBox,
    QLabel as _QLabel,
    QMessageBox as _QMessageBox,
    QPushButton as _QPushButton,
    QRadioButton as _QRadioButton,
    QMenu as _QMenu,
)


ENGLISH = "en"
CHINESE = "zh_CN"
_language = os.environ.get("FLAMETRACKER_LANGUAGE") or QSettings(
    "Mercury1219", "FlameTracker"
).value(
    "language", ENGLISH, type=str
)
if _language not in {ENGLISH, CHINESE}:
    _language = ENGLISH

_objects: "weakref.WeakSet[object]" = weakref.WeakSet()
_menus: "weakref.WeakKeyDictionary[object, str]" = weakref.WeakKeyDictionary()


ZH = {
    "&File": "文件(&F)", "&Measure": "测量(&M)", "&Tracking": "追踪(&T)",
    "&Show": "显示(&S)", "&Help": "帮助(&H)", "&Tracking options": "追踪选项(&T)",
    "Language": "语言", "English": "English", "Simplified Chinese": "简体中文",
    "Open video": "打开视频", "Open image(s)": "打开图像", "Save parameters": "保存参数",
    "Load parameters": "加载参数", "Export edited video": "导出编辑后的视频",
    "Scale (px/length)": "比例尺（像素/长度）", "Point coordinates": "点坐标",
    "Length": "长度", "Manual tracking": "手动追踪", "Luma tracking": "亮度追踪",
    "RGB tracking": "RGB 追踪", "HSV tracking": "HSV 追踪", "Ember tracking": "余烬追踪",
    "Show frame in new window": "在新窗口显示帧", "Reduced-size windows": "缩小窗口",
    "Scale": "比例尺", "Point": "坐标点", "Frame": "帧",
    "Preview box": "预览区", "Analysis box": "分析区", "Welcome to Flame Tracker!": "欢迎使用 Flame Tracker！",
    "(file name)": "（文件名）", "Width (px):": "宽度（px）：", "Height (px):": "高度（px）：",
    "Frame rate (fps):": "帧率（fps）：", "Frames #:": "帧数：", "Duration (s):": "时长（s）：",
    "Video parameters:": "视频参数：", "First frame:": "起始帧：", "Last frame:": "结束帧：",
    "Skip frames:": "跳过帧数：", "Scale px/len:": "比例尺 px/长度：", "Ref. point": "参考点",
    "Select ROI": "选择 ROI", "ROI, x:": "ROI，x：", "ROI, y:": "ROI，y：",
    "ROI, w:": "ROI，宽：", "ROI, h:": "ROI，高：", "Rotation (deg):": "旋转角度（°）：",
    "Brightness:": "亮度：", "Contrast:": "对比度：", "Grayscale": "灰度",
    "Correction lengths (mm):": "校正长度（mm）：", "Horizontal:": "水平：", "Vertical:": "垂直：",
    "Correct perspective": "透视校正", "Restore original": "恢复原始图像", "Frame:": "帧：",
    "Time:": "时间：", "Go to frame": "跳转到帧", "Go to time": "跳转到时间",
    "Select the analysis method from the menu Tracking > ... to activate this panel": "请从“追踪 > …”菜单选择分析方法以启用此面板",
    "Direction:": "方向：", "Left to right": "从左到右", "Right to left": "从右到左",
    "Flashing light (optional):": "闪光灯（可选）：", "Flashing light": "闪光灯",
    "Pick bright region": "选取明亮区域", "Adjust light thresholds": "调整亮度阈值",
    "Track every frame": "追踪每一帧", "Frames light on": "仅灯亮帧", "Frames light off": "仅灯灭帧",
    "Tracking pts #:": "追踪点数：", "Start tracking": "开始追踪", "Start Tracking": "开始追踪",
    "Save data": "保存数据", "Update graphs": "更新图表", "Absolute values": "绝对值",
    "Show tracking lines": "显示追踪线", "x axis:": "x 轴：", "y axis:": "y 轴：",
    "Time [s]": "时间 [s]", "Frame #": "帧号", "x coord.": "x 坐标",
    "x coord. [px]": "x 坐标 [px]", "y coord.": "y 坐标", "y coord. [px]": "y 坐标 [px]",
    "Spread rate, x": "x 方向蔓延速率", "Spread rate, y": "y 方向蔓延速率",
    "Threshold:": "阈值：", "Filter (px):": "颗粒过滤（px）：", "Edges (px):": "边缘点数（px）：",
    "Flame tracking:": "火焰追踪：", "Moving avg pts:": "移动平均点数：",
    "Position, x": "x 位置", "Position, x [px]": "x 位置 [px]", "Position, y": "y 位置",
    "Position, y [px]": "y 位置 [px]", "Flame width": "火焰宽度", "Flame height": "火焰高度",
    "Spread rate": "蔓延速率", "Flame area": "火焰面积", "Show filtered frame": "显示过滤后帧",
    "right edge": "右边缘", "left edge": "左边缘", "top edge": "上边缘", "bottom edge": "下边缘",
    "Ignore flashing light": "忽略闪光灯", "Show edge lines": "显示边缘线", "Show edges location": "显示边缘位置",
    "Export BW video": "导出黑白视频", "Export Luma video": "导出亮度视频", "Export RGB video": "导出 RGB 视频",
    "Connectivity (px)": "连通性（px）", "Red:": "红色：", "Green:": "绿色：", "Blue:": "蓝色：",
    "Hue:": "色相：", "Saturation:": "饱和度：", "Value:": "明度：", "Min:": "最小值：", "Max:": "最大值：",
    "Graph #1:": "图表 1：", "Graph #2:": "图表 2：", "Save RGB values": "保存 RGB 参数",
    "Load RGB values": "加载 RGB 参数", "Save HSV values": "保存 HSV 参数", "Load HSV values": "加载 HSV 参数",
    "Approx Diameter (len):": "估计直径（长度）：", "Max Travel Length (len):": "最大移动距离（长度）：",
    "Min Brightness:": "最低亮度：", "Min Tot Intensity:": "最低总强度：", "Frame Memory:": "帧记忆数：",
    "Animation": "动画", "Combined": "组合", "Trajectories": "轨迹", "Velocities": "速度",
    "Total Intensity Distribution": "总强度分布", "Tot Intensity (Area * px intensity)": "总强度（面积 × 像素强度）",
    "Number of embers": "余烬数量",
    "Output video analysis": "输出视频分析", "Video tracking overlay": "视频追踪叠加层",
    "Show:": "显示：", "Save Results": "保存结果", "Save": "保存", "Done": "完成", "Next": "下一步",
    "Save Par": "保存参数", "Load Par": "加载参数", "x (#1):": "x（点 1）：", "y (#1):": "y（点 1）：",
    "x (#2):": "x（点 2）：", "y (#2):": "y（点 2）：",
    "Measure scale": "测量比例尺", "Known length": "已知长度", "Known length:": "已知长度：",
    "Points selected: 0 / 2": "已选择点：0 / 2", "Select video format": "选择视频格式",
    "New frame rate (fps):": "新帧率（fps）：", "Video codec:": "视频编码器：", "Video format:": "视频格式：",
    "Open File": "打开文件", "Open Images": "打开图像", "Save edited video": "保存编辑后的视频",
    "Open parameters": "打开参数", "Save channel values": "保存通道参数", "Load channel values": "加载通道参数",
    "Save tracking data": "保存追踪数据", "Save Ember Parameters": "保存余烬参数", "Load Ember Parameters": "加载余烬参数",
    "Save Tracking Data": "保存追踪数据", "CSV Files (*.csv)": "CSV 文件 (*.csv)",
    "Missing unit scale": "缺少长度单位", "Please select a unit scale before starting tracking.": "开始追踪前请选择长度单位。",
    "Image successfully corrected": "图像校正成功", "Video read succesfully": "视频读取成功",
    "Image(s)read succesfully": "图像读取成功", "Parameters saved.": "参数已保存。",
    "Parameters loaded.": "参数已加载。", "Parameters loaded. Perspective correction detected and applied": "参数已加载，并检测和应用了透视校正",
    "Parameters not loaded correctly.": "参数未能正确加载。", "Measurement cancelled.": "测量已取消。",
    "Tracking completed": "追踪完成", "Tracking started, press (Esc) to quit.": "追踪已开始，按 Esc 退出。",
    "Flame not found in some frames": "部分帧中未找到火焰", "Data successfully saved.": "数据保存成功。",
    "Data succesfully saved.": "数据保存成功。", "Data not saved.": "数据未保存。",
    "Channel values saved.": "通道参数已保存。", "Channel values loaded.": "通道参数已加载。",
    "Ember parameters saved.": "余烬参数已保存。", "Ember parameters loaded.": "余烬参数已加载。",
    "No tracks found.": "未找到轨迹。", "No tracks found for this frame.": "当前帧未找到轨迹。",
    "No data to save. Run tracking first.": "没有可保存的数据，请先运行追踪。", "Run tracking first!": "请先运行追踪！",
    "Not enough colors for plotting.": "用于绘图的颜色数量不足。", "Error: the graphs could not be updated.": "错误：无法更新图表。",
    "Error: the video could not be opened": "错误：无法打开视频", "Error: the image(s) could not be opened": "错误：无法打开图像",
    "Error: Enter a valid video name": "错误：请输入有效的视频名称", "Clicks not specified (=1)": "未指定点击次数（已设为 1）",
    "Click on two points to measure their distance.": "请点击两个点以测量距离。",
    "Click the two endpoints of a known length in the image. A third click starts the selection again.": "请在图像中点击已知长度的两个端点；第三次点击将重新选择。",
    "The reference length and width need to be specified": "必须指定参考对象的长度和宽度",
    "The scale [px/len] has not been specified": "尚未指定比例尺 [px/长度]",
    "The click order is: 1) top right, 2) bottom right, 3) bottom left, 4) top left.": "点击顺序：1）右上，2）右下，3）左下，4）左上。",
    "1) top right, 2) bottom right, 3) bottom left, 4) top left": "1）右上，2）右下，3）左下，4）左上",
    "Before the tracking, click on \"Pick a bright region\" to select a small region visible only when the light is on.": "追踪前请点击“选取明亮区域”，选择一块仅在灯亮时可见的小区域。",
    "Pick a bright region first (click \"Pick a bright region\").": "请先点击“选取明亮区域”。",
    "Selected ROI appears empty on this frame.": "所选 ROI 在当前帧中似乎为空。",
    "No frames were detected, please check ROI size and light settings.": "未检测到任何帧，请检查 ROI 大小和灯光设置。",
    "Grayscale images not supported with this feature": "此功能不支持灰度图像",
    "Grayscale images are not supported for the RGB tracking method": "RGB 追踪方法不支持灰度图像",
    "Something went wrong and the scale was not measured.": "发生错误，未能测量比例尺。",
    "Something went wrong and the reference point was not measured.": "发生错误，未能测量参考点。",
    "Something went wrong and the length was not measured.": "发生错误，未能测量长度。",
    "Ops! Something went wrong!": "糟糕，发生了错误！", "Ops! Something went wrong.": "糟糕，发生了错误。",
    "Ops! Parameters were not saved.": "糟糕，参数未保存。", "Ops! Parameters were not loaded.": "糟糕，参数未加载。",
    "Ops! The values were not saved.": "糟糕，数值未保存。", "Light threshold adjustment canceled.": "已取消亮度阈值调整。",
    "Maximize unfiltered area. (S=Save, Q/Esc=Cancel)": "请最大化未过滤区域。（S=保存，Q/Esc=取消）",
    "Maximize unfiltered (white) area. (S=Save, Q/Esc=Cancel)": "请最大化未过滤的白色区域。（S=保存，Q/Esc=取消）",
    "Warning: Length unit not found. Once the Scale is determined, \"len\" will have that unit.": "警告：未找到长度单位。确定比例尺后，“长度”将采用该单位。",
}


def language() -> str:
    return _language


def tr(text: str) -> str:
    if not isinstance(text, str) or _language == ENGLISH:
        return text
    if text in ZH:
        return ZH[text]
    match = re.fullmatch(r"Points selected: (\d+) / 2", text)
    if match:
        return f"已选择点：{match.group(1)} / 2"
    match = re.fullmatch(r"Scale in px/(.+) successfully measured", text)
    if match:
        return f"比例尺测量成功：px/{match.group(1)}"
    match = re.fullmatch(r"Scale px/(.+):", text)
    if match:
        return f"比例尺 px/{match.group(1)}："
    match = re.fullmatch(r"MT, frame #: (\d+)", text)
    if match:
        return f"手动追踪，帧号：{match.group(1)}"
    if text.startswith("Manual Tracking allows"):
        return "手动追踪允许您逐帧点击火焰位置。可设置每帧追踪点数、闪光灯帧过滤以及结果坐标与蔓延速率的导出。\n\n详细说明：https://github.com/combustionTools/flameTracker/wiki/3.-Manual-tracking"
    if text.startswith("Luma Tracking allows"):
        return "亮度追踪根据 ROI 中每个像素的亮度自动识别火焰，并计算位置、尺寸、面积和蔓延速率。\n\n详细说明：https://github.com/combustionTools/flameTracker/wiki/4.-Luma-Tracking"
    if text.startswith("RGB Tracking allows"):
        return "RGB 追踪根据 ROI 中红、绿、蓝通道的阈值自动识别火焰区域。\n\n详细说明：https://github.com/combustionTools/flameTracker/wiki/5.-Color-Tracking"
    if text.startswith("HSV Tracking allows"):
        return "HSV 追踪根据 ROI 中色相、饱和度和明度阈值自动识别火焰区域。可配合颗粒过滤与闪光灯过滤使用。"
    if text.startswith("Ember Tracking allows"):
        return "余烬追踪用于识别余烬或颗粒，并测量其速度和运动轨迹。"
    if text.startswith("Flame Tracker is an image analysis program"):
        return "Flame Tracker 是用于检测和追踪图像或视频中火焰（或发光物体）的图像分析软件。\n\n说明文档：https://github.com/combustionTools/flameTracker/wiki\n\n联系邮箱：flametrackercontact@gmail.com"
    return text


def set_language(value: str) -> None:
    global _language
    if value not in {ENGLISH, CHINESE}:
        raise ValueError(f"Unsupported language: {value}")
    _language = value
    QSettings("Mercury1219", "FlameTracker").setValue("language", value)
    for obj in list(_objects):
        method = getattr(obj, "_retranslate", None)
        if method:
            method()
    for menu, source in list(_menus.items()):
        menu.setTitle(tr(source))


def add_menu(parent, source: str):
    """Add a menu whose title participates in live language switching."""
    menu = _QMenu(tr(source), parent)
    parent.addMenu(menu)
    _menus[menu] = source
    return menu


def _source_text(args):
    for index, value in enumerate(args):
        if isinstance(value, str):
            return index, value
    return None, None


class _TextMixin:
    def _init_translation(self, args):
        index, source = _source_text(args)
        self._i18n_source = source
        _objects.add(self)
        if index is not None:
            args = list(args)
            args[index] = tr(source)
        return args

    def setText(self, text):
        self._i18n_source = text
        return super().setText(tr(text))

    def _retranslate(self):
        if self._i18n_source is not None:
            super().setText(tr(self._i18n_source))


class QLabel(_TextMixin, _QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)

    def text(self):
        # Labels are also used as stable CSV field identifiers in legacy code.
        if self._i18n_source is not None:
            return self._i18n_source
        return super().text()


class QPushButton(_TextMixin, _QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)


class QCheckBox(_TextMixin, _QCheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)


class QRadioButton(_TextMixin, _QRadioButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)


class QGroupBox(_TextMixin, _QGroupBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)

    def setTitle(self, text):
        self._i18n_source = text
        return super().setTitle(tr(text))

    def _retranslate(self):
        if self._i18n_source is not None:
            super().setTitle(tr(self._i18n_source))


class QAction(_TextMixin, _QAction):
    def __init__(self, *args, **kwargs):
        super().__init__(*self._init_translation(args), **kwargs)

    def text(self):
        # Analysis code uses action text as a stable method identifier.
        if self._i18n_source is not None:
            return self._i18n_source
        return super().text()


class QComboBox(_QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._i18n_sources = []
        _objects.add(self)

    def addItem(self, *args, **kwargs):
        index, source = _source_text(args)
        cooked = list(args)
        if index is not None:
            cooked[index] = tr(source)
        super().addItem(*cooked, **kwargs)
        self._i18n_sources.append(source)

    def addItems(self, texts):
        for text in texts:
            self.addItem(text)

    def insertItem(self, item_index, *args, **kwargs):
        index, source = _source_text(args)
        cooked = list(args)
        if index is not None:
            cooked[index] = tr(source)
        super().insertItem(item_index, *cooked, **kwargs)
        self._i18n_sources.insert(item_index, source)

    def clear(self):
        super().clear()
        self._i18n_sources.clear()

    def currentText(self):
        index = self.currentIndex()
        if 0 <= index < len(self._i18n_sources) and self._i18n_sources[index] is not None:
            return self._i18n_sources[index]
        return super().currentText()

    def setCurrentText(self, text):
        if text in self._i18n_sources:
            self.setCurrentIndex(self._i18n_sources.index(text))
        else:
            super().setCurrentText(tr(text))

    def _retranslate(self):
        for index, source in enumerate(self._i18n_sources):
            if source is not None:
                self.setItemText(index, tr(source))


class QMessageBox(_QMessageBox):
    def setText(self, text):
        return super().setText(tr(text))

    def setInformativeText(self, text):
        return super().setInformativeText(tr(text))

    def setWindowTitle(self, text):
        return super().setWindowTitle(tr(text))

    @staticmethod
    def warning(parent, title, text, *args, **kwargs):
        return _QMessageBox.warning(parent, tr(title), tr(text), *args, **kwargs)

    @staticmethod
    def critical(parent, title, text, *args, **kwargs):
        return _QMessageBox.critical(parent, tr(title), tr(text), *args, **kwargs)

    @staticmethod
    def information(parent, title, text, *args, **kwargs):
        return _QMessageBox.information(parent, tr(title), tr(text), *args, **kwargs)


class QFileDialog(_QFileDialog):
    @staticmethod
    def getOpenFileName(parent=None, caption="", directory="", filter="", *args, **kwargs):
        return _QFileDialog.getOpenFileName(parent, tr(caption), directory, tr(filter), *args, **kwargs)

    @staticmethod
    def getOpenFileNames(parent=None, caption="", directory="", filter="", *args, **kwargs):
        return _QFileDialog.getOpenFileNames(parent, tr(caption), directory, tr(filter), *args, **kwargs)

    @staticmethod
    def getSaveFileName(parent=None, caption="", directory="", filter="", *args, **kwargs):
        return _QFileDialog.getSaveFileName(parent, tr(caption), directory, tr(filter), *args, **kwargs)

    @staticmethod
    def getExistingDirectory(parent=None, caption="", directory="", *args, **kwargs):
        return _QFileDialog.getExistingDirectory(parent, tr(caption), directory, *args, **kwargs)


RawQAction = _QAction
