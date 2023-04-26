# 作者: ZengCheng
# 时间: 2022/9/19
import time

import pytest

from Python_PyTest.common.common_util import Commo_util


class Test_web(Commo_util):
    workage = 10

    @pytest.mark.modu2
    def test_web_04(self):
        print('测试微博1_第4个用例')

    @pytest.mark.skip(reason="无理由跳过")  # 无条件跳过该用例
    def test_web_05(self):
        print('测试微博1_第5个用例')
        # assert 1 == 2

    @pytest.mark.skipif(workage < 18,reason='工作经验少于10年跳过')  # 有条件跳过该用例
    def test_web_06(self):
        print('测试微博1_第6个用例')

    @pytest.mark.run(order=1)  # 改变默认的执行顺序
    @pytest.mark.modu1 # 分组模块
    def test_web_01(self):
        print('测试微博1_第1个用例')

    @pytest.mark.run(order=3)
    @pytest.mark.modu2
    def test_web_03(self):
        print('测试微博1_第3个用例')

    @pytest.mark.run(order=2)
    @pytest.mark.modu1
    def test_web_02(self):
        print('测试微博1_第2个用例')
