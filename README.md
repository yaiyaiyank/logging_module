# loggingモジュール

自分のエコシステム用につくったログ記録モジュール
役立ちそう ∧ 機密情報なし なのでパブリックで公開

# install
・uv
・Python3.13以上推奨(モジュールとして利用時のPythonの環境)

Pyhtonスクリプト自体は標準ライブラリのみで完結するのでモジュール利用時は依存を気にしなくてok

# usage

### start

使いたいディレクトリ(使い方からしてモジュール一覧みたいなディレクトリ)(日本語やスペースなどが含まれていると後でエラーを吐くので注意)で

```bash
git clone https://github.com/yaiyaiyank/logging_module
```

を実行。

logging_moduleディレクトリ内のinit_env.batを実行。これによってconfig.tomlなどが生成される。(※この時、日本語やスペースなどが含まれているとエラーを吐くはず)

config.tomlのdefault_log_folderにログを格納するディレクトリのパスを指定(デフォルトでこのディレクトリ下のlogsとなっている。)

### update

logging_moduleディレクトリ内のupdate_env.batを実行。

```python
from logging_module import Log # from句は環境によって違うよ。最終的にlogging_module/__init__.pyのLogをimportすればおｋ

log = Log()

log.info("うおｗ")

log.error("おお")

```

ちなみに、FileHandlerはINFO以上、StreamHandlerはDEBUG以上です。引数で調整できるようにするかもしれないし、しれないかもしれない。