# SushidAuto（スシドート）
タイピングゲーム「寿司打」自動化プログラム

**注意**: プログラムの利用は自己責任でお願いします。

## 概要
SushidAuto はOCRでゲーム内の文字を記録し、文字列に変換します。Pyautoguiはその名の通りGUIを自動化、すなわち表示された文字を入力します。

## 準備
お持ちのデバイスにPython3がインストールされている必要があります。

次に、以下のPythonモジュールをインストールしてください:
* PIL:  `pip install pillow`
* PyOCR: `pip install pyocr`
* cv2: `pip install opencv-python`
* PyAutoGui: `pip install pyautogui` (macOS・Linuxは `pip3` Linuxの方は[こちら](https://pyautogui.readthedocs.io/en/latest/install.html)も参照)
* Tesseract-OCR
    * **Windows**: インストーラをこちらからダウンロードし、
    https://github.com/UB-Mannheim/tesseract/wiki
    "C:\Program Files\Tesseract-OCR" をPATHに追加してください。
    * **macOS**: `brew install tesseract` でインストール
    * **Ubuntu**: `sudo apt install tesseract-ocr` でインストール

| OS           | サポートされている解像度  　| 難易度         |
|--------------|-------------------------|--------------------|
| macOS (beta) | 2560×1600               | お手軽、お勧め、高級 |
| Windows      | 2560×1600               | お手軽、高級       |
|              | 2560×1440               | お手軽、お勧め、高級 |
|              | 1920×1080               | お手軽、お勧め、高級 |

## 実行方法
以下のコマンドで実行できます:

`python main.py`


## 修正予定のバグなど:
* macOSにてゲーム開始のクリックがされない
* macOSで実行速度が遅い
* 一部の難易度・解像度では間違った範囲から文字を読み取ってしまう