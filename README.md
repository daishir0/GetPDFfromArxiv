# GetPDFfromArxiv

## Overview
GetPDFfromArxiv is a simple Python script designed to help researchers and enthusiasts download academic papers in PDF format from ArXiv. Given a search keyword, the script fetches relevant PDFs and ensures they contain the keyword within their text.

## Installation
1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone this repository or download the `GetPDFfromArxiv.py` script.
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To use the script, run the following command in your terminal or command prompt:
```sh
python GetPDFfromArxiv.py <search_keyword>
```
Replace `<search_keyword>` with the keyword you want to search for.

## Notes
- The script saves downloaded PDFs in a folder named `pdfs` in the current working directory.
- If the keyword is not found in the text of a PDF, the file is saved with a prefix "NG_" to indicate that it did not pass the filter.
- Make sure you have internet connectivity and access to ArXiv's website.
- Use responsibly to avoid overwhelming ArXiv's servers.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# GetPDFfromArxiv

## 概要
GetPDFfromArxivは、検索キーワードに基づいてArXivから学術論文のPDFをダウンロードするためのシンプルなPythonスクリプトです。指定されたキーワードを含む関連するPDFをフェッチし、そのテキスト内にキーワードが含まれていることを確認します。

## インストール方法
1. システムにPython 3.6以降がインストールされていることを確認してください。
2. このリポジトリをクローンするか、`GetPDFfromArxiv.py`スクリプトをダウンロードしてください。
3. 必要な依存関係をインストールしてください：
   ```sh
   pip install -r requirements.txt
   ```

## 使い方
スクリプトを使用するには、ターミナルまたはコマンドプロンプトで以下のコマンドを実行してください：
```sh
python GetPDFfromArxiv.py <検索キーワード>
```
`<検索キーワード>`を検索したいキーワードに置き換えてください。

## 注意点
- スクリプトはダウンロードしたPDFを現在の作業ディレクトリ内の`pdfs`フォルダに保存します。
- キーワードがPDFテキスト内に見つからない場合、ファイルはフィルタを通過しなかったことを示すために"NG_"というプレフィックスで保存されます。
- インターネット接続とArXivのウェブサイトへのアクセスが必要です。
- ArXivのサーバを過負荷にしないように責任を持って使用してください。

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています - 詳細は[LICENSE](LICENSE)ファイルをご覧ください。
