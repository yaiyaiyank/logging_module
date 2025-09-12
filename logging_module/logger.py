import datetime
import inspect
import tomllib
from logging import DEBUG, INFO, FileHandler, Formatter, StreamHandler, getLogger
from pathlib import Path

# 自作ライブラリ
from .setting import project_folder_path


class Log:
    def __init__(self, module_name: str | None = None, log_folder_path: Path | str | None = None):
        """ログ"""
        # ログを識別する名前
        if module_name is None:
            module_name = self._get_caller_name()

        log_folder_path = self._get_log_folder_path(log_folder_path)

        self._set_handlers(module_name, log_folder_path)

    def debug(self, text):
        self.logger.debug(text)

    def info(self, text):
        self.logger.info(text)

    def warning(self, text):
        self.logger.warning(text)

    def error(self, text):
        self.logger.error(text)

    def critical(self, text):
        self.logger.critical(text)

    def _set_handlers(self, module_name: str, log_folder_path: Path):
        self.logger = getLogger(module_name)

        # 重複防止
        if self.logger.hasHandlers():
            return
        # debug以上のログを記録
        self.logger.setLevel(DEBUG)
        # はんどらせってい
        self._set_file_handler(log_folder_path)
        self._set_stream_handler()

    def _set_file_handler(self, log_folder_path: Path):
        # 日付を
        date = datetime.date.today()
        log_file = log_folder_path / f"{date.year:04}" / f"{date.month:02}" / f"{date.day:02}.log"
        # フォルダ生成
        log_file.parent.mkdir(parents=True, exist_ok=True)

        # FileHandler
        handler = FileHandler(log_file, encoding="utf-8")
        handler.setLevel(INFO)
        handler.setFormatter(Formatter("%(asctime)s [%(levelname)s] - %(name)s - %(message)s"))
        self.logger.addHandler(handler)

    def _set_stream_handler(self) -> str:
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(Formatter("[%(levelname)s] - %(name)s - %(message)s"))
        self.logger.addHandler(handler)

    @staticmethod
    def _get_log_folder_path(log_folder_path: Path | str | None) -> Path:
        """ログのフォルダーを決定"""
        # 引数で指定されていたらそれ
        if not log_folder_path is None:
            return Path(log_folder_path)
        # tomlから引用
        with (project_folder_path / "config.toml").open("rb") as f:
            toml = tomllib.load(f)
        log_folder_path_str = toml["path"]["default_log_folder"]
        # tomlにも設定されていなかったら
        if log_folder_path_str == "":
            return project_folder_path / "log"
        # tomlに設定されていたらそれを使う
        return Path(log_folder_path_str)

    @staticmethod
    def _get_caller_name() -> str:
        """logの呼び出し名を決める。呼び出した位置に依存"""
        # スタックフレームを取得
        stack = inspect.stack()

        # 呼び出し元の情報を取得
        frame = stack[2]  # [0]はget_caller_name, [1]は__init__, [2]はその呼び出し元
        caller_frame = frame.frame
        code_object = caller_frame.f_code

        # クラスのイニシャライザか関数かを判定
        if "self" in caller_frame.f_locals:
            # selfがある場合はクラスのメソッド
            cls_name = caller_frame.f_locals["self"].__class__.__name__
            if code_object.co_name == "__init__":
                return f"Class: {cls_name}"
            return f"method: {cls_name}.{code_object.co_name}"
        elif code_object.co_name == "<module>":
            # selfがない場合は通常の関数
            return f"File: {Path(code_object.co_filename).name}"
        else:
            return f"Function: {code_object.co_name}"


if __name__ == "__main__":
    log = Log()
    log.info("にょわああ")
