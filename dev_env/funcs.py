import subprocess
from subprocess import CompletedProcess
from pathlib import Path


def execute_cmd(command, console_display=True) -> CompletedProcess:
    if console_display:
        # コンソールに文字を出す
        result = subprocess.run(
            command, shell=True, text=True, encoding="utf8", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    else:
        # コンソールに文字を出さない
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf8")
    return result


def get_top_modules_path_for_current_name(dir_name: str) -> Path | None:
    """トップモジュールが含まれるパスを返す"""
    search_path = Path().cwd()
    for _ in range(20):
        search_path = search_path.parent
        top_modules_path = search_path / "yai"
        if top_modules_path.exists():
            print(f"トップモジュールが見つかりました。パス: {top_modules_path}")
            return search_path
    else:
        return None
