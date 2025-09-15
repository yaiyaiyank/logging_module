from pathlib import Path
from funcs import execute_cmd, get_top_modules_path_for_current_name
import argparse

TOP_MODULES_NAME = "yai"


def init_env():
    # venvを作ったりしてくれる
    execute_cmd("uv sync")

    # 開発用にトップモジュールのパスを通す (pthってなんかAIのモデルのファイルみたいだね)
    pth_file = Path().cwd() / ".venv" / "Lib" / "site-packages" / "mymodules.pth"
    mymodules_path = get_top_modules_path_for_current_name(TOP_MODULES_NAME)
    if not mymodules_path is None:
        pth_file.write_text(mymodules_path.__str__(), encoding="utf-8")

    # 依存ライブラリがあったらインストール
    requirement_txt = Path().cwd() / "requirement.txt"
    if requirement_txt.exists():
        execute_cmd("uv add -r requirements.txt -U")

    # config.tomlに書き込む初期設定があったら記入
    config_toml_path = Path().cwd() / "config.toml"
    if not mymodules_path is None:
        default_log_path = mymodules_path / "logs"
    else:
        default_log_path = Path.cwd() / "logs"
    if not config_toml_path.exists():
        config_toml_path.write_text(f"[path]\ndefault_log_folder = '{default_log_path}'", encoding="utf-8")


def update_env():
    # 依存ライブラリの最新をインストール
    requirement_txt = Path().cwd() / "requirement.txt"
    if requirement_txt.exists():
        execute_cmd("uv add -r requirements.txt -U")

    # リポジトリを最新へ
    execute_cmd("git pull --rebase")


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--env", type=str, default="init")
args = parser.parse_args()

if args.env == "init":
    init_env()
if args.env == "update":
    update_env()
