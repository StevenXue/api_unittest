# -*- coding: utf-8 -*-  
"""  
  @desc:  
  @author: StevenXue 
  @date: 2018/10/31
"""
import unittest
from HTMLTestRunner import HTMLTestRunner
from URL_request import url_request_for_get_method


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_new(a, b):
    return float(a) / b


class TestMathFunc(unittest.TestCase):
    """
    Demo for template
    """

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))
        self.assertNotEqual(3, add(2.2313312233, 212321321321321323))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def test_url_request(self):
        """
        TEST URL request
        :return:
        """
        url = "http://localhost:3080/resource_manager/get_device_brands"
        for num in range(0, 100):
            querystring = {"page": "1", "limit": "10", "device_type_ID": num}
            response = url_request_for_get_method(url, querystring)
            if response.get("message") == "failed":
                self.fail("message == failed")
            else:
                if isinstance(response.get("response"), list):
                    print("success!")
                else:
                    self.fail("fail")

    def test_url_get_user(self):
        """
        用户查询

        :return:
        """
        keyword = None
        is_security = [0, 1]
        user_type = [0, 1, 2, 3, 4, 5, 10]
        print(keyword, is_security, user_type)


if __name__ == "__main__":
    """
    1.在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是 S。
    从上面也可以看出，测试的执行跟方法的顺序没有关系，test_divide写在了第4个，但是却是第2个执行的。
    
    2.每个测试方法均以 test 开头，否则是不被unittest识别的。
    
    3.在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，
    默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果，
    
    """
    # unittest.main(1)
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"),
    #          TestMathFunc("test_divide")]
    # suite.addTests(tests)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 直接用addTest方法添加单个TestCase
    # suite.addTest(TestMathFunc("test_multi"))

    # 用addTests + TestLoader
    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    with open('Report/HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)
