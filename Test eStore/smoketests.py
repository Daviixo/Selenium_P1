from unittest import TestLoader, TestSuite
from assertions import AssertionsTest
from searchtests import SearchTests
from HtmlTestRunner import HTMLTestRunner

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_tests])

# Aquí generamos nuestros reportes. 
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
    }


runner = HTMLTestRunner(**kwargs)

runner.run(smoke_test) 