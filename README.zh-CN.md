<h1 align="center">Flame Tracker</h1>

<p align="center">用于视频和图像序列中火焰及明亮物体定量追踪的 Python 桌面应用。</p>

<p align="center"><a href="README.md">English</a> | <strong>简体中文</strong></p>

<p align="center">
  <a href="https://github.com/Mercury1219/flameTracker/releases"><img alt="Release" src="https://img.shields.io/github/v/release/Mercury1219/flameTracker"></a>
  <a href="https://github.com/Mercury1219/flameTracker/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Mercury1219/flameTracker/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%20%7C%203.13-3776AB?logo=python&logoColor=white">
  <a href="https://github.com/Mercury1219/flameTracker/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Mercury1219/flameTracker"></a>
</p>

Flame Tracker 面向火灾科学研究，可逐帧编辑和分析视频或图像，并通过手动、亮度、RGB、HSV 和余烬追踪方法获得火焰位置、蔓延速率、宽度、高度及面积等参数。

本维护分支基于上游项目 [`combustionTools/flameTracker`](https://github.com/combustionTools/flameTracker)，改进了比例尺测量流程，并从 v1.5.0 起支持英文与简体中文界面的即时切换。

原作者：Luca Carmignani, PhD  
贡献者：Charles Scudiere, PhD  
联系邮箱：flameTrackerContact@gmail.com

## 安装与启动

需要 Python 3.11 或 3.13。克隆仓库后，在项目根目录执行：

```bash
python -m pip install -r requirements.txt
cd scripts
python flameTracker.py
```

Windows 用户也可以从本分支的 [Releases](https://github.com/Mercury1219/flameTracker/releases) 下载打包后的可执行文件，无需单独安装 Python。

## 中英文切换

在菜单栏选择 **Language > English** 或 **Language > 简体中文**。当前窗口和已打开的追踪面板会立即更新，语言选择也会在下次启动时保留。

语言切换只改变界面显示。追踪算法使用的内部选项、计算过程以及导出数据的稳定字段不会因语言变化而改变。

## 比例尺测量

1. 打开视频或图像序列；
2. 点击工具栏中的 **比例尺**，或选择 **测量 > 比例尺（像素/长度）**；
3. 在图像中点击已知长度的两个端点；
4. 输入实际长度并选择单位；
5. 点击确定，软件会把计算结果写入“比例尺 px/单位”字段。

## 追踪方法

- **手动追踪**：逐帧点击一个或多个目标点；
- **亮度追踪**：通过像素亮度阈值识别火焰；
- **RGB 追踪**：通过红、绿、蓝通道阈值识别火焰；
- **HSV 追踪**：通过色相、饱和度和明度阈值识别火焰；
- **余烬追踪**：提取余烬或颗粒的轨迹与速度。

完整操作说明参见上游 [Flame Tracker Wiki](https://github.com/combustionTools/flameTracker/wiki)。

## 许可证与引用

本项目采用 [GNU GPL v3](LICENSE) 许可证。

如在科研工作中使用，请引用：

L. Carmignani, *Flame Tracker: An image analysis program to measure flame characteristics*, SoftwareX, Vol. 15, 2021.
