# Python 程式設計入門（習題個人解答） #

[![issue](https://img.shields.io/github/discussions/z2x3c4v5bz/Learning--Py_intro)](https://github.com/z2x3c4v5bz/Learning--Py_intro/discussions)
[![forks](https://img.shields.io/github/forks/z2x3c4v5bz/Learning--Py_intro)](https://github.com/z2x3c4v5bz/Learning--Py_intro/network)
[![stars](https://img.shields.io/github/stars/z2x3c4v5bz/Learning--Py_intro)](https://github.com/z2x3c4v5bz/Learning--Py_intro/stargazers)
[![release](https://img.shields.io/github/release/z2x3c4v5bz/Learning--Py_intro/all)](https://github.com/z2x3c4v5bz/Learning--Py_intro/releases)
[![license](https://img.shields.io/github/license/z2x3c4v5bz/Learning--Py_intro)](https://github.com/z2x3c4v5bz/Learning--Py_intro/blob/master/LICENSE)

## Abstract ##

**Title:** Python 程式設計入門

**Auther:** 葉難

**Introduction:**

>- 完整收納 Python 2.x 與 3.x 版的所有知識
>- 從入門到進階技巧的完整 Python 教學
>- 循序漸進的範例與豐富的習題
>- 多種設計思路的全面提示
>- 各種延伸學習資源

![thumbnail](img/thumbnail.png)

※ 習題開發環境為 Python 3.x，作業系統使用 Microsoft Windows 7/10/11 x64 與 Apple macOS Monterey，並選擇軟體 VS Code 為文字編輯器。

※ 原諒我題目內不附圖示。

※ 請留意，文中數學公式在瀏覽器頁面中可能無法正確顯示。

※ 圖書封面、內容皆為版權作者、出版商所有，本站所刊內容僅供教育、學習使用。

## Table of Contents ##

- [Python 程式設計入門（習題個人解答）](#python-程式設計入門習題個人解答)
  - [Abstract](#abstract)
  - [Table of Contents](#table-of-contents)
  - [Chapter 01 -- 走入 Python 的世界](#chapter-01----走入-python-的世界)
  - [Chapter 02 -- 開始撰寫 Python 程式](#chapter-02----開始撰寫-python-程式)
  - [Chapter 03 -- 數值型別](#chapter-03----數值型別)
  - [Chapter 04 -- 序列型別與迭代](#chapter-04----序列型別與迭代)
  - [Chapter 05 -- 字典與集合](#chapter-05----字典與集合)
  - [Chapter 06 -- 函式](#chapter-06----函式)
  - [Chapter 07 -- 檔案、文字、編碼、位元組資料](#chapter-07----檔案文字編碼位元組資料)
  - [Chapter 08 -- 其他容器型別](#chapter-08----其他容器型別)
  - [Chapter 09 -- 再談函式](#chapter-09----再談函式)
  - [Chapter 10 -- 模組](#chapter-10----模組)
  - [Chapter 11 -- 物件導向程式設計（OOP）](#chapter-11----物件導向程式設計oop)
  - [Chapter 12 -- 異常（exception）](#chapter-12----異常exception)
  - [Chapter 13 -- 延伸學習](#chapter-13----延伸學習)

## Chapter 01 -- 走入 Python 的世界 ##

>- 電腦、軟體與程式語言
>- Python 簡介
>- 版本
>- Python 程式執行環境與實作
>- 安裝 Python 實作
>- Hello Python
>- 程式碼編輯器與 IDE

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 02 -- 開始撰寫 Python 程式 ##

>- 名稱、物件、型別、指派
>- 運算式
>- 述句
>- 函式
>- 模組
>- 原始程式檔
>- 常見錯誤
>- 補充

### [Question 02-01](ch02/ch02_01/ch02_01.py) ###

>閏年規則如下，西元年份可被 400 整除是閏年，或者，可被 4 整除但不能被 100 整除的年份也是閏年。例如 2000 與 2060 是閏年，1900 與 2057 不是閏年。請依此規則寫出 `if` 述句判斷某整數（西元年份）是否為閏年。

### [Question 02-02](ch02/ch02_02/ch02_02.py) ###

>分別用 `for` 與 `while` 述句印出九九乘法表。

### [Question 02-03](ch02/ch02_03/ch02_03.py) ###

>程式碼 2.9（ch02_score_plus.py）使用 `continue` 述句，請改寫，去掉 `continue` 述句，但仍保持相同的功能。

### [Question 02-04](ch02/ch02_04/ch02_04.py) ###

>請寫出攝氏溫度轉華氏溫度的函式，以及華氏轉攝氏的函式。

### [Question 02-05](ch02/ch02_05/ch02_05.py) ###

>請寫個函式，參數是三個數字，找出其中較大的兩個，並算出平方和回傳。例：參數 `2`、`3`、`4`，回傳 $3^2 + 4^2$。

### [Question 02-06](ch02/ch02_06/ch02_06.py) ###

>給兩個整數，求出最小公倍數。

### [Question 02-07](ch02/ch02_07/ch02_07.py) ###

>串列裡含有由小到大排列好的整數，數字可能重複，例如 `[0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]`，請撰寫函式找出重複最多次的整數，若重複次數相等則回傳值較小的，以此例而言，9 與 25 都重複 3 次，應回傳 `9`。

### [Question 02-08](ch02/ch02_08/ch02_08.py) ###

>給你兩個日期，請算出相差幾天。日期以串列表示，譬如 2014 年 11 月 12 日是 `[2014, 11, 12]`。

### [Question 02-09](ch02/ch02_09/ch02_09.py) ###

>$n$ 階乘（$n!$）等於「$1 × 2 × 3 × ... × (n - 1) × n$」。請撰寫函式，參數是 $n$，算出 $n!$ 的所有位數的和。譬如 $9!$ 是 362880，而 $3 + 6 + 2 + 8 + 8 + 0$ 等於 27。

### [Question 02-10](ch02/ch02_10/ch02_10.py) ###

>給定兩個串列，裡頭各有一些數字（整數），找出兩個串列都有的數字。

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 03 -- 數值型別 ##

>- 整數（int）與浮點數（float）
>- 範例：平方根
>- 布林
>- 物件、型別、方法
>- 複數（complex）
>- 轉型
>- 十進位數（Decimal）
>- 分數（Fraction）
>- 位元運算

### [Question 03-01](ch03/ch03_01/ch03_01.py) ###

>圓形面積是圓的半徑平方再乘上圓周率，請撰寫函式，傳入半徑，回傳圓面積。

### [Question 03-02](ch03/ch03_02/ch03_02.py) ###

>曾經有一款遊戲，其角色能力值的上下限是 0 到 255，現在想要將能力值上下限轉換為大眾熟悉的 0 到 100。請撰寫函式進行轉換，其中 200～255（良好）應該轉換到 85～100，0～130（差勁）應轉換到 0～60。

### [Question 03-03](ch03/ch03_03/ch03_03.py) ###

>當給定一個正整數時，把每個位數加起來，其和若可被 3 整除，則原數也可被 3 整除，同樣的原理可依此類推，直到最後得到的和可被 3 整除。譬如 37524，$3 + 7 + 5 + 2 + 4$ 等於 21，$2 + 1$ 等於 3，所以 21 可被 3 整除，所以 37524 也可被 3 整除。請撰寫函式，根據此法判斷參數是否可被 3 整除。

### [Question 03-04](ch03/ch03_04/ch03_04.py) ###

>考拉茲猜想（Collatz conjecture），又稱為奇偶歸一猜想；給定一正整數，若是偶數就除以 2，若是奇數就乘 3 再加 1，如下：
>
>$f(n) = \frac{n}{2}$ ，若 $n$ 是偶數
>
>$f(n) = 3n + 1$ ，若 $n$ 是奇數
>
>如此不斷重複，最終必得到 1。譬如給定 6 的話，將會依序得到 3、10、5、16、8、4、2、1。但這僅為猜想而已，尚無人可證明。請撰寫程式，驗證介於 1 到 10000 之間的正整數，都符合此猜想。

### [Question 03-05](ch03/ch03_05/ch03_05.py) ###

>若一個整數除了自己與 1 以外，不能被其他數整除，就稱為質數，例如 2、3、5、7、11。請撰寫函式，參數是個整數，回傳布林值代表它是不是質數。

### [Question 03-06](ch03/ch03_06/ch03_06.py) ###

>神秘的 1089。三位數的整數，百位數與個位數必須相差 2 以上，假定原數字是 ABC，反轉後得到 CBA，讓大的減去小的，得到 DEF，再反轉得到 FED，而相加後「DEF + FED」一定會等於 1089。譬如 $732 - 237$ 等於 495，$495 + 594$ 等於 1089；讀者可試試 654 與 123。請問是否所有符合條件的三位數整數，都會得到 1089。

### [Question 03-07](ch03/ch03_07/ch03_07.py) ###

>計算 $n$ 階乘（$n!$）時，當 $n$ 很大時計算量非常龐大，若情況許可，可使用斯特靈公式（Stirling's approximation）取得近似值，公式如下，請撰寫實作此公式的函式。
>
>$$n! \approx \sqrt{2 \pi n}(\frac{n}{e})^n$$

### [Question 03-08](ch03/ch03_08/ch03_08.py) ###

>三個正整數 a、b、c，若能符合下列公式，便可稱為卡達諾三數組（Cardano Triplet），譬如 2、1、5。當 $a + b + c \le 1000$ 時，共存在著 149 個卡達諾三數組，請找出來。
>
>$$\sqrt[3]{a + b \sqrt{c}} + \sqrt[3]{a - b \sqrt{c}} = 1$$

### [Question 03-09](ch03/ch03_09/ch03_09.py) ###

>「幾 A 幾 B 猜數字」規則如下，甲方在心中設想一個四位數的數字，位數不重複，由乙方來猜，甲方需回答「幾 A 幾 B」，A 代表位置正確的位數的個數，B 代表數字正確但位置不對的個數，舉例而言，若正確答案是 5234，那麼猜 5346 會得到 1A2B。請寫出函式，參數是正確答案與猜測，回傳 `tuple`，第 0 個元素代表 A、第一個元素代表 B。

### [Question 03-10](ch03/ch03_10/ch03_10.py) ###

>終極密碼戰遊戲的玩法如下，由電腦從 1 到 100 選出一個數字當作謎底，然後由使用者猜謎底，若沒猜中就縮減邊界（往較小的方向縮減），然後繼續猜。舉例而言，假設謎底是 23，而使用者猜 44 沒猜中，那麼邊界就從 1～100 縮減到 1～44，然後使用者再猜 12 沒猜中，邊界從 1～44 縮減到 12～44，直到猜中為止。請寫支程式，讓電腦隨機從 1 到 100 選出謎底，由你來猜，看看需要猜幾次。

### [Question 03-11](ch03/ch03_11/ch03_11.py) ###

>假定參數是兩個 32 位元整數 A 與 B，請判斷需要改變幾個位元，才能把整數 A 轉換成整數 B。範例：A 是 31（0b11111），B 是 14（0b1110），答案是 2。

### Question 03-12 ###

>假定整數有 32 位元，請把其中奇數位元與偶數位元互換，也就是說，第 0 個位元與第 1 個位元互換，第 2 個與第 3 個位元互換，依此類推，只能使用位元運算子，使用次數越少越好。

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 04 -- 序列型別與迭代 ##

>- 型別與物件
>- 抽象型別
>- 元素存取
>- 迭代
>- 串列生成式（list comprehension）
>- 字串

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 05 -- 字典與集合 ##

>- 字典與集合的基礎
>- 相關抽象型別
>- 字典
>- 集合
>- 補充

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 06 -- 函式 ##

>- 函式基礎
>- 參數
>- 可視範圍與命名空間
>- 遞迴
>- 高階函式
>- 產生器（generator）
>- 補充

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 07 -- 檔案、文字、編碼、位元組資料 ##

>- 初探檔案
>- 型別 str、bytes、unicode
>- 文字檔案
>- 位元組（二進位）資料
>- 文字編碼系統

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 08 -- 其他容器型別 ##

>- 具名元組（named tuple）
>- 雙向佇列（deque）
>- 計數器（Counter）
>- 模組 heapq
>- ChainMap
>- 陣列（array）

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 09 -- 再談函式 ##

>- 再談遞迴
>- 裝飾器（decorator）
>- 函數式程式設計

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 10 -- 模組 ##

>- 基本概念
>- 匯入模組：import 與 from
>- 再次載入模組
>- 模組搜尋路徑
>- 套件
>- 第三方模組

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 11 -- 物件導向程式設計（OOP） ##

>- 概論
>- 類別（class）
>- 繼承
>- 多重繼承
>- 後設類別

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 12 -- 異常（exception） ##

>- 程式錯誤
>- 異常
>- 已內建的異常型別
>- 捕抓異常
>- 引發異常

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)

## Chapter 13 -- 延伸學習 ##

>- 程式撰寫風格與實務作法
>- 命令列參數
>- 圖形介面
>- 執行外部程式
>- 動態執行
>- 並行處理
>- 其他

[![table_of_contents](https://img.shields.io/badge/%E5%9B%9E%E5%88%B0%E7%9B%AE%E9%8C%84-Top-blue)](#table-of-contents)
