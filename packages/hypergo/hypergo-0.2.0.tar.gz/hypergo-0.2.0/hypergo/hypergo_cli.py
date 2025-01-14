import datetime
import json
import os
import sys

from colors import color

from hypergo.config import ConfigType
from hypergo.graph import graph as hypergraph
from hypergo.local_storage import LocalStorage
from hypergo.stdio_connection import StdioConnection
from hypergo.version import get_version


class HypergoCli:
    @property
    def prompt(self) -> str:
        return f"{color('hypergo', fg='#33ff33')} {color('∵', fg='#33ff33')} "

    @property
    def intro(self) -> str:
        def format_date(sec: float) -> str:
            return datetime.datetime.fromtimestamp(sec).strftime("%b %d %Y, %H:%M:%S.%f")[:-3]

        def get_version_path() -> str:
            return os.path.dirname(os.path.abspath(__file__)) + "/version.py"

        version: str = get_version()
        timestamp: str = format_date(os.path.getmtime(get_version_path()))
        intro: str = f"hypergo {version} ({timestamp})\nType help or ? to list commands."
        return str(color(intro, fg="#ffffff"))

    def stdio(self, ref: str, *args: str) -> int:
        try:
            with open(ref, "r", encoding="utf-8") as file:
                config: ConfigType = json.load(file)

            if not sys.stdin.isatty():
                stdin_data = sys.stdin.read().strip()
                if stdin_data:
                    args = (stdin_data,) + args
            else:
                raise BrokenPipeError("No input message piped in through stdin")

            connection = StdioConnection()
            connection.consume(args[0], config, LocalStorage())

        except Exception as err:
            print(f"*** {err}")
            raise err

        return 0

    def graph(self, *args: str) -> int:
        hypergraph(list(args))
        return 0
