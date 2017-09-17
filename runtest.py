import unittest

#定义测试case路径'
dir='./case/'

#匹配测试文件
discover=unittest.defaultTestLoader.discover(dir,pattern="test.py")

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)