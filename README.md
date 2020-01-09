# nararei

# Name

supercar_CNN フェラーリとランボルギーニを判別するコマンドラインアプリ
Tensorflowを用いてフェラーリとランボルギーニの画像を学習させ判別するプログラム

# 使用した物
使用した言語、ライブラリは以下の物である
*Anacondaに入っているAnaconda Prompt
* Python3.7.3
* Tensorflow2.0.0
*numpy 1.16.2
*pillow 6.2.1
*sys

# 各ライブラリのインストール方法

```bash
pip install tensorflow
```
```bash
pip install pip install numpy
```
```bash
pip install pillow
```

```bash
pip install sys
```
# 画像データの準備
まずフェラーリとランボルギーニの画像を用意する。
ferrariディレクトリにフェラーリの画像
lamborghiniディレクトリにランボルギーニの画像を
用意する。

#画像を数値データに変換
次に画像データをコンピュータが読み込み安いようにnumpy形式に変換するためgenerate_data224.py
を実行させる。
コマンドラインを開きsupercar_CNNディレクトリまで移動し
```bash
python generate_data224.py
```
を実行させる。
その際.npy形式のファイルが保存される。これを学習の際に使用する。

#学習
今度は画像データを学習させる。先ほど作成した.npy形式のファイルをvgg_16transfer.pyに読み込ませ
学習させる。

コマンドラインを開きsupercar_CNNディレクトリまで移動し
```bash
python vgg_16transfer.py
```
を実行させる。
実行後.h5ファイルが作成される。これは学習した際の学習データが入っているファイルである。
このファイルを使用しコマンドラインを用い検証を行う。

# 画像の検証
先程作成された.h5ファイルをpredict.pyにセットさせる。
コマンドラインを開きsupercar_CNNディレクトリまで移動し
```bash
python predict.py 読み込ませたい画像の名前
```

# 作成者

* 奈良岡 伶

# 参考文献
[画像判定AIアプリ開発・パート1]TensorFlow・Python・Flaskで作る画像判定AIアプリ開発入門
https://www.udemy.com/course/tensorflow-advanced/

[画像判定AIアプリ開発・パート2】Django・TensorFlow・転移学習による高精度AI アプリ開発
https://www.udemy.com/course/django-ai-app/


