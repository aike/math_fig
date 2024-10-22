math_fig
---

## 説明
Jupyter Notebookでの使用を想定した、簡易的な数学用の作図ライブラリ。  
importして利用することもできるが、サイズが小さいため直接埋め込んでポータブルなipynbファイルにすることも可能。

## 使用例


## API

+ init()
描画領域の設定  
| keyword argument | range               | default    | note          |
|:----------------:|:--------------------|:----------:|:-------------:|
|  max             | 正の整数             | 10         | 目盛りの最大値 |
|  origin          | center / leftbottom | leftbottom | 原点位置       |
|  aspect          | square / landscape  | square     | 縦横比        |
|  col             | 色名 / カラーコード   | #444444    | 軸の色        |

+ vec(x, y, col)
原点からの矢印描画  
| argument | range              | note     |
|:--------:|:-------------------|:---------:|
|  x       | 実数               | x座標     |
|  y       | 実数               | y座標     |
|  col     | 色名 / カラーコード | 線の色     |



## ライセンス
math_fig program is licensed under MIT License.  
Copyright 2024, aike (@aike1000)  
