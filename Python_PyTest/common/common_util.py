# 作者: ZengCheng
# 时间: 2022/9/29

class Commo_util:

    def setup_class(self):
        print('每个类之前执行一次')

    def teardown_class(self):
        print('每个类之后执行一次')

    def setup(self):
        print('每个用例之前执行一次')

    def teardown(self):
        print('每个用例之后执行一次')
