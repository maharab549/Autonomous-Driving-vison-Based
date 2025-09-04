<div align="center" style="position: relative;">
<h1 style="align;center">AUTONOMOUS-DRIVING-VISON-BASED</h1>
<p align="center">
	<img src="https://img.shields.io/github/license/maharab549/Autonomous-Driving-vison-Based?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/maharab549/Autonomous-Driving-vison-Based?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/maharab549/Autonomous-Driving-vison-Based?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/maharab549/Autonomous-Driving-vison-Based?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>This project implements a vision-based autonomous driving system on a Jetson Nano (ROS1, Ubuntu 18.04). The car uses computer vision (OpenCV + YOLOv5) for real-time perception and intelligent behavior control.
<h1>Tech Stack</h1>
#Hardware: Jetson Nano (4GB), USB Camera
#Software: ROS1 (Melodic), OpenCV with CUDA, YOLOv5 (TensorRT optimized)
#Programming: Python</code>

---

## 👾 Features

<code> Road Following: Detects and follows yellow lane borders using OpenCV + YOLOv5.
Traffic Sign Detection: Recognizes signs (green light, turn left/right, warning) with YOLOv5.
Behavior Control:
Green light → move forward
Turn left/right signs → lane change & turning
Warning signs → stop safely
Progressive Danger Detection: Adaptive responses based on detected obstacles/signals.
ROS1 Integration: Modular nodes for perception, decision, and control. </code>
## 📁 Project Structure

```sh
└── Autonomous-Driving-vison-Based/
    ├── CMakeLists.txt
    ├── package.xml
    └── scripts
        ├── .idea
        ├── 2025
        ├── 202_yolo
        ├── 320_yolo
        ├── __pycache__
        ├── ai_yolov5.py
        ├── bin_hsv.py
        ├── direct_fix.py
        ├── direct_fix_code.py
        ├── fix_findcontours.sh
        ├── hsv.py
        ├── hsv2.py
        ├── hsv_green.py
        ├── hsv_red.py
        ├── large_yolo
        ├── main.py
        ├── new_main.py
        ├── opencv_line.py
        ├── rgb.py
        ├── servo_pd.py
        ├── shuju
        ├── small_yolo
        ├── test.py
        ├── yolov5
        └── yolov5_det_trt.py
```


### 📂 Project Index
<details open>
	<summary><b><code>AUTONOMOUS-DRIVING-VISON-BASED/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/CMakeLists.txt'>CMakeLists.txt</a></b></td>
				<td><code>❯</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5_det_trt.py'>yolov5_det_trt.py</a></b></td>
				<td><code>❯ REPLACE-M</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/hsv_red.py'>hsv_red.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/direct_fix.py'>direct_fix.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/hsv2.py'>hsv2.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/ai_yolov5.py'>ai_yolov5.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/new_main.py'>new_main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/opencv_line.py'>opencv_line.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/main.py'>main.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/bin_hsv.py'>bin_hsv.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/hsv.py'>hsv.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/servo_pd.py'>servo_pd.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/fix_findcontours.sh'>fix_findcontours.sh</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/direct_fix_code.py'>direct_fix_code.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/test.py'>test.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/rgb.py'>rgb.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/hsv_green.py'>hsv_green.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>large_yolo</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/large.engine'>large.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/large.wts'>large.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5-cls.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5-cls.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.13.0</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/3.13.0/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/large_yolo/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>yolov5</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/best.wts'>best.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/gen_wts.py'>gen_wts.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/yolov5_det'>yolov5_det</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/best.engine'>best.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>3.13.0</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CUDA.bin'>CMakeDetermineCompilerABI_CUDA.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CMakeCUDACompiler.cmake'>CMakeCUDACompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCUDA</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/CMakeCUDACompilerId.cu'>CMakeCUDACompilerId.cu</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
											<details>
												<summary><b>tmp</b></summary>
												<blockquote>
													<table>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/a_dlink.reg.c'>a_dlink.reg.c</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.fatbin.c'>CMakeCUDACompilerId.fatbin.c</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/a_dlink.fatbin'>a_dlink.fatbin</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cpp1.ii'>CMakeCUDACompilerId.cpp1.ii</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.module_id'>CMakeCUDACompilerId.module_id</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/a_dlink.sm_30.cubin'>a_dlink.sm_30.cubin</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.ptx'>CMakeCUDACompilerId.ptx</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cudafe1.stub.c'>CMakeCUDACompilerId.cudafe1.stub.c</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.fatbin'>CMakeCUDACompilerId.fatbin</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cpp4.ii'>CMakeCUDACompilerId.cpp4.ii</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cudafe1.c'>CMakeCUDACompilerId.cudafe1.c</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/a_dlink.fatbin.c'>a_dlink.fatbin.c</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.sm_30.cubin'>CMakeCUDACompilerId.sm_30.cubin</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cudafe1.gpu'>CMakeCUDACompilerId.cudafe1.gpu</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													<tr>
														<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/3.13.0/CompilerIdCUDA/tmp/CMakeCUDACompilerId.cudafe1.cpp'>CMakeCUDACompilerId.cudafe1.cpp</a></b></td>
														<td><code>❯ REPLACE-ME</code></td>
													</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>yolov5_det.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/CUDA.includecache'>CUDA.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/yolov5_det.dir/dlink.txt'>dlink.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/CUDA.includecache'>CUDA.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/yolov5/CMakeFiles/myplugins.dir/dlink.txt'>dlink.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>shuju</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/best.wts'>best.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/best.engine'>best.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.10.2</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/3.10.2/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.Debug.cmake'>myplugins_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.depend'>myplugins_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.cmake.pre-gen'>myplugins_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/shuju/CMakeFiles/myplugins.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>small_yolo</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/small.engine'>small.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/small.wts'>small.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5-cls.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5-cls.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.13.0</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/3.13.0/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/small_yolo/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>320_yolo</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/320.engine'>320.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/320.wts'>320.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5-cls.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5-cls.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.13.0</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/3.13.0/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/320_yolo/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>202_yolo</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5-cls.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5-cls.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.13.0</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/3.13.0/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/202_yolo/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>2025</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/best.wts'>best.wts</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/cmake_install.cmake'>cmake_install.cmake</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/yolov5'>yolov5</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/Makefile'>Makefile</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeCache.txt'>CMakeCache.txt</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/best.engine'>best.engine</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>CMakeFiles</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/feature_tests.cxx'>feature_tests.cxx</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/progress.marks'>progress.marks</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/CMakeDirectoryInformation.cmake'>CMakeDirectoryInformation.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/TargetDirectories.txt'>TargetDirectories.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/feature_tests.bin'>feature_tests.bin</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/feature_tests.c'>feature_tests.c</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/Makefile2'>Makefile2</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/Makefile.cmake'>Makefile.cmake</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/CMakeRuleHashes.txt'>CMakeRuleHashes.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/cmake.check_cache'>cmake.check_cache</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>yolov5.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.Debug.cmake'>yolov5_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.cmake.pre-gen'>yolov5_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o.depend'>yolov5_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>3.10.2</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CMakeCXXCompiler.cmake'>CMakeCXXCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CMakeDetermineCompilerABI_C.bin'>CMakeDetermineCompilerABI_C.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CMakeDetermineCompilerABI_CXX.bin'>CMakeDetermineCompilerABI_CXX.bin</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CMakeCCompiler.cmake'>CMakeCCompiler.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CMakeSystem.cmake'>CMakeSystem.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
									<details>
										<summary><b>CompilerIdC</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CompilerIdC/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CompilerIdC/CMakeCCompilerId.c'>CMakeCCompilerId.c</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>CompilerIdCXX</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CompilerIdCXX/CMakeCXXCompilerId.cpp'>CMakeCXXCompilerId.cpp</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/3.10.2/CompilerIdCXX/a.out'>a.out</a></b></td>
												<td><code>❯ REPLACE-ME</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>myplugins.dir</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.Debug.cmake'>myplugins_generated_yololayer.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/DependInfo.cmake'>DependInfo.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.Debug.cmake'>myplugins_generated_preprocess.cu.o.Debug.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.depend'>myplugins_generated_yololayer.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/link.txt'>link.txt</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/depend.internal'>depend.internal</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/progress.make'>progress.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/build.make'>build.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/cmake_clean.cmake'>cmake_clean.cmake</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_yololayer.cu.o.cmake.pre-gen'>myplugins_generated_yololayer.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.depend'>myplugins_generated_preprocess.cu.o.depend</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/flags.make'>flags.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/myplugins_generated_preprocess.cu.o.cmake.pre-gen'>myplugins_generated_preprocess.cu.o.cmake.pre-gen</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/depend.make'>depend.make</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/master/scripts/2025/CMakeFiles/myplugins.dir/CXX.includecache'>CXX.includecache</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Autonomous-Driving-vison-Based, ensure your runtime environment meets the following requirements:

- **Programming Language:** CMake
- **Package Manager:** Cmake


### ⚙️ Installation

Install Autonomous-Driving-vison-Based using one of the following methods:

**Build from source:**

1. Clone the Autonomous-Driving-vison-Based repository:
```sh
❯ git clone https://github.com/maharab549/Autonomous-Driving-vison-Based
```

2. Navigate to the project directory:
```sh
❯ cd Autonomous-Driving-vison-Based
```

3. Install the project dependencies:


**Using `cmake`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```




### 🤖 Usage
Run Autonomous-Driving-vison-Based using the following command:
**Using `cmake`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


### 🧪 Testing
Run the test suite using the following command:
**Using `cmake`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: Change you yolov5 traffic sign model directrory Code line: 800
- [ ] **`Task 2`**: Change your lane segmentation model directrory Code line: 801

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/maharab549/Autonomous-Driving-vison-Based/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/maharab549/Autonomous-Driving-vison-Based/issues)**: Submit bugs found or log feature requests for the `Autonomous-Driving-vison-Based` project.
- **💡 [Submit Pull Requests](https://github.com/maharab549/Autonomous-Driving-vison-Based/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/maharab549/Autonomous-Driving-vison-Based
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/maharab549/Autonomous-Driving-vison-Based/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=maharab549/Autonomous-Driving-vison-Based">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT](https://opensource.org/license/mit) License. For more details, refer to the [MIT](https://opensource.org/license/mit) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
