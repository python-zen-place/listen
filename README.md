# listen

![license:MIT](https://img.shields.io/github/license/python-zen-place/listen) ![Python Version: 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)

>  命令行音乐源聚合搜索工具

由于版权分立，我们要找的歌可能在不同平台。一个个平台去找？太麻烦！
现在，你可以使用一个命令在多个平台搜索你的音乐。

## 搜索源

- [x] 网易云音乐
- [x] QQ音乐
- [x] 酷狗音乐
- [x] Apple Music
- [ ] 千千音乐

## 安装 
> Windows需确保拥有管理员权限

克隆本项目

`git clone https://github.com/python-zen-place/listen.git`

打开目录

`cd listen`

使用pip安装

`pip install .`

## 使用

直接使用

`python -m listen 我也喜欢你的女朋友`

作为模块使用

```python
import listen

data = listen.search.netease_music_search('我也喜欢你的女朋友')

```

## TODO

- [x] 编写setup.py
- [ ] 千千音乐搜索源
- [ ] 提供歌曲访问链接

## 感谢

listen的诞生离不开他们:

- [Netease API](https://music.jeeas.cn/)


