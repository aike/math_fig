math_fig
---

## 説明
Jupyter Notebookでの使用を想定した、簡易的な数学用の作図ライブラリ。  
importして利用することもできるが、サイズが小さいため直接埋め込んでポータブルなipynbファイルにすることも可能。

## 使用例


## API

### init()
描画領域の設定。一番最初に実行する。（必須）

| keyword argument | range               | default    | note           |
|:----------------:|:--------------------|:----------:|:--------------:|
|  max             | 正の整数            | 10         | 目盛りの最大値 |
|  origin          | center / leftbottom | leftbottom | 原点位置       |
|  aspect          | square / landscape  | square     | 縦横比         |
|  col             | 色名 / カラーコード | #444444    | 軸の色         |

### show()
描画実行。各種描画関数実行後、一番最後に実行する。（必須）

### vec(x, y, col)  
原点からの矢印描画

| argument | range               | note     |
|:--------:|:--------------------|:--------:|
|  x       | 実数                | x座標    |
|  y       | 実数                | y座標    |
|  col     | 色名 / カラーコード | 線の色   |

### vec2(x0, y0, x1, y1, col)  
２点間の矢印描画

| argument | range               | note      |
|:--------:|:--------------------|:---------:|
|  x0      | 実数                | 始点x座標 |
|  y0      | 実数                | 始点y座標 |
|  x1      | 実数                | 終点x座標 |
|  y1      | 実数                | 終点y座標 |
|  col     | 色名 / カラーコード | 線の色    |





## ライセンス
math_fig program is licensed under MIT License.  
Copyright 2024, aike (@aike1000)  
