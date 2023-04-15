import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--custom-report",
        action="store_true",
        default=True,
        help="Use custom report format",
    )

def pytest_configure(config):
    if config.getoption("--custom-report"):
        config.pluginmanager.register(CustomReport(), "customreport")

class CustomReport:

    def pytest_terminal_summary(self, terminalreporter):
        tr = terminalreporter
        passed_tests = tr.stats.get("passed", [])
        failed_tests = tr.stats.get("failed", [])

        for test in passed_tests:
            tr.write("\033[32mAll tests passed\033[0m for {}\n".format(test.nodeid))

        for test in failed_tests:
            tr.write("\033[31mTest failed\033[0m for {}\n".format(test.nodeid))
            input_vars = test._report.sections[0][1]
            tr.write("  Input variables are: {}\n".format(input_vars))
            error_message = test._report.longrepr.reprtraceback.reprentries[-1].reprfileloc.message
            tr.write("  {}\n".format(error_message))
