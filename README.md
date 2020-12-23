# DailyProgress 概要
簡単に勉強時間をプログレスバー化し、画像で取得してくれる(すぐにアップ出来る！！)

* 1日によるので、最大は24時間です(10時間, 10時間ってしたら凄い人間になっちゃう)
* 自動的に画像化までしてくれます
* 出力画像は実行ファイルと一緒の場所に出力されます
* 最大文字数は10文字です、それ以上は途中で切られます

![](https://github.com/anko191/DailyProgress/blob/main/imgs/ex2.png)

* 出力された画像

![](https://github.com/anko191/DailyProgress/blob/main/imgs/12_24.png)

余計な余白はあるけどまぁ...(　   'ω')

# 実行方法

## EXEファイルバージョン
exeファイルversionを用意しています。<br>
ファイルサイズは11MBで、環境構築を必要とせず実行することで出力することができます。<br>
起動まで5秒くらいかかりますpyinstallerの仕様だと思います...<br>

- [ ] また、<span style="color: red; ">Windows Defenderに不明なファイルとして検出される場合があります</span>

対処法は分かりません((

- [x] Download [https://github.com/anko191/DailyProgress/raw/main/progressbar.exe](https://github.com/anko191/DailyProgress/raw/main/progressbar.exe)



## Pythonファイルバージョン

###  必要なモジュール
```
python 3.8 (このバージョンじゃなくてもいいと思います)
pip install tkinter (元から入ってるかも)
pip install pillow
```

* 実行方法として
```
git clone https://github.com/anko191/DailyProgress.git
```
をした後、ターミナルで
```
\> cd DailyProgress
\DailyProgress> python progressbar.py
```
を実行する！

# これからの改善(するかもしれないしないかも）

誰かtkinterのtext-align centerを知っていたら教えてください<br>
あと余計な余白が無いようにしたい...あんまり行数が多いと下が凄くながくなるかも
