# loggingモジュール

自分のエコシステム用(役立ちそう ∧ 機密情報なし なのでパブリックで公開)

# install

・Python3.13

標準ライブラリのみで完結！

# usage

使いたいディレクトリ(使い方からしてモジュール一覧みたいなディレクトリ)で

```bash
git clone https://github.com/yaiyaiyank/logging_module
```

config.tomlのdefault_log_folderにログを格納するディレクトリのパスを指定(指定しなければこのディレクトリ下のlogsとする)

Pythonで

```python
from logging_module import Log # from句は環境によって違うよ。最終的にlogging_module/__init__.pyのLogをimportすればおｋ

log = Log()

log.info("うおｗ")

log.error("おお")

```

ちなみに、FileHandlerはINFO以上、StreamHandlerはDEBUG以上です。引数で調整できるようにするかもしれないし、しれないかもしれない。