# 作者: ZengCheng
# 时间: 2022/9/19
import pytest

if __name__ == '__main__':
    # -分组模块执行用例
    # pytest.main(['-m', 'modu1 or modu2'])

    # -根据测试用例的部分字符串指定测试用例
    # pytest.main(['-vs','-k','func'])

    # -出现两个用例失败就停止
    # pytest.main(['-vs','--maxfail=2'])

    # -表示只有有一个用例失败报错，就停止测试
    # pytest.main(['-vs','-x'])

    # -失败用例重跑
    # pytest.main(['-vs', './web_PyTest/test_web_01.py', '--reruns=2'])

    # -多线程
    # pytest.main(['-vs', './web_PyTest/test_web_01.py', '-n=2'])

    # -指定目录
    pytest.main(['-vs', './web_PyTest'])

    # -指定目录指定py文件
    # pytest.main(['-vs', './web_PyTest/test_interface_01.py'])

    # -指定目录指定py文件中的指定函数
    # pytest.main(['-vs', './web_PyTest/test_interface_01.py::test_func_01'])

    # -指定目录指定py文件中的指定类中指定方法
    # pytest.main(['-vs', './web_PyTest/test_interface_01.py::Test_interface_01::test_interface_01'])

    # -显示输出调试信息
    # pytest.main(['-s')

    # -显示更详细的信息
    # pytest.main(['-v')