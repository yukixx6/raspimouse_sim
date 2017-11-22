# raspimouse_sim 

[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=indigo-devel)](https://travis-ci.org/rt-net/raspimouse_sim)

Gaezbo上でシミュレートできるRaspberry Pi MouseのROSパッケージ一式です。

チュートリアルと詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。

## 動作環境

以下の環境を前提として動作確認しています。

* Ubuntu
  * Ubuntu Trusty 14.04
* ROS
  * ROS Indigo
* Gazebo
  * Gazebo 2.x
* ROS Package
  * [raspimouse_ros](https://github.com/ryuichiueda/raspimouse_ros)
  * ros-indigo-desktop-full
  * ros-indigo-gazebo-ros-control
  * ros-indigo-ros-controllers

## インストール方法
ターミナルを開き、以下のコマンドを実行してください。

```
bash -exv -c "$(curl -sSfL https://git.io/raspimouse-sim-installer)"
```

## スクリーンショット
### サンプル迷路での動作例
![](./docs/images/raspimouse_samplemaze.png)

### URG付きモデルでの動作例
![](./docs/images/raspimouse_urg.png)

## ライセンス

このリポジトリはMITライセンスに基づいて公開されています。
MITライセンスについては[LICENSE]( ./LICENSE )を確認してください。

### 引用または参考にしたリポジトリ

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
