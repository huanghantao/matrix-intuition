"""测试共用设施。

通过环境变量 IMPL 选择被测实现：

    IMPL=matrixlab   （默认）跑你自己写的代码 —— 一开始全是 TODO，会红
    IMPL=reference           跑参考答案 —— 应该全绿

用法示例（测试文件里）：

    def test_add(mod):
        vec2d = mod("vec2d")
        assert vec2d.add([1, 2], [3, 4]) == [4, 6]
"""

import importlib
import os

import pytest

IMPL = os.environ.get("IMPL", "matrixlab")


@pytest.fixture
def mod():
    """返回一个"按模块名取实现"的小工具。"""

    def _mod(name: str):
        return importlib.import_module(f"{IMPL}.{name}")

    return _mod
