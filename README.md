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

※ 習題開發環境為 Microsoft Windows 系列 x64 作業系統與 Macbook macOS Monterey，並採用軟體 VS Code 為文字編輯器，Python 3.x。

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

## Chapter 04 -- 序列型別與迭代 ##

>- 型別與物件
>- 抽象型別
>- 元素存取
>- 迭代
>- 串列生成式（list comprehension）
>- 字串

## Chapter 05 -- 字典與集合 ##

>- 字典與集合的基礎
>- 相關抽象型別
>- 字典
>- 集合
>- 補充

## Chapter 06 -- 函式 ##

>- 函式基礎
>- 參數
>- 可視範圍與命名空間
>- 遞迴
>- 高階函式
>- 產生器（generator）
>- 補充

## Chapter 07 -- 檔案、文字、編碼、位元組資料 ##

>- 初探檔案
>- 型別 str、bytes、unicode
>- 文字檔案
>- 位元組（二進位）資料
>- 文字編碼系統

## Chapter 08 -- 其他容器型別 ##

>- 具名元組（named tuple）
>- 雙向佇列（deque）
>- 計數器（Counter）
>- 模組 heapq
>- ChainMap
>- 陣列（array）

## Chapter 09 -- 再談函式 ##

>- 再談遞迴
>- 裝飾器（decorator）
>- 函數式程式設計

## Chapter 10 -- 模組 ##

>- 基本概念
>- 匯入模組：import 與 from
>- 再次載入模組
>- 模組搜尋路徑
>- 套件
>- 第三方模組

## Chapter 11 -- 物件導向程式設計（OOP） ##

>- 概論
>- 類別（class）
>- 繼承
>- 多重繼承
>- 後設類別

## Chapter 12 -- 異常（exception） ##

>- 程式錯誤
>- 異常
>- 已內建的異常型別
>- 捕抓異常
>- 引發異常

## Chapter 13 -- 延伸學習 ##

>- 程式撰寫風格與實務作法
>- 命令列參數
>- 圖形介面
>- 執行外部程式
>- 動態執行
>- 並行處理
>- 其他
