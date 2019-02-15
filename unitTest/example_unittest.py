import unittest
from unittest import mock
from example_function import function1, function2

class ExampleTest(unittest.TestCase):
    def test_function2(self):
        # 錯誤比對 =>會跳 AssertionError: 50 != 49
        # self.assertEqual(function2(5),49)
        # 正確比對 => 不輸出任何東西
        self.assertEqual(function2(5),50)

    # 可以用在多重引用的環節
    @mock.patch('example_function.function1')
    def With_mock_test_function2(self, mock_function1):

        # 將 function1 的回傳值指定為 0 ，目的是讓單元測試時可以將 function 1 及 function 2 分離
        mock_function1.return_value = 0 

        # self.assertEqual(function2(5),26)

        self.assertEqual(function2(5),25)
        

if __name__ == '__main__':
    newTest = ExampleTest()
    newTest.test_function2()
    newTest.With_mock_test_function2()