# loggingモジュール

自分のエコシステム用(役立ちそう ∧ 機密情報なし なのでパブリックでご開帳)

今は中身がないので公式リリースを待てろ...

# install

・Python

標準ライブラリのみで完結！依存なし逆転なし

# うさげ

使いたいディレクトリ(使い方からしてモジュール一覧みたいなディレクトリ)で

```bash
git clone https://github.com/yaiyaiyank/logging_module
```

Pythonで

```python
from logging_module import Log # importまでのfrom句は環境によって違うよ。最終的にlogging_module/__init__.pyのLogをimportすればおｋ

log = Log()

log.info("うおｗ")

log.error("おお")

```

以上