import pytest


class CustomReport:
    def pytest_terminal_summary(self, terminalreporter):
        tr = terminalreporter
        tests_passed = 0
        failed_tests = []

        for rep in tr.getreports(''):
            if rep.passed:
                tests_passed += 1
            elif rep.failed:
                failed_tests.append(rep)

        if tests_passed > 0:
            tr.write_line(f"All tests passed for {tests_passed} functions.", green=True)

        if failed_tests:
            for rep in failed_tests[:1]:
                tr.write_line(f"Test failed for {rep.nodeid}", red=True)

                for prop in rep.user_properties:
                    if prop[0] == "input_values":
                        tr.write_line(f"Input variables are: {prop[1]}", red=True)
                    if prop[0] == "expected_result":
                        tr.write_line(f"Expected answer: {prop[1]}", red=True)
                    if prop[0] == "actual_result":
                        tr.write_line(f"Your answer: {prop[1]}", red=True)

        # Suppress the default summary output.
        terminalreporter.config.option.disable_test_summary = True


def pytest_configure(config):
    if config.getoption("--custom-report"):
        config.pluginmanager.register(CustomReport(), "customreport")


def pytest_addoption(parser):
    parser.addoption(
        "--custom-report",
        action="store_true",
        default=True,
        help="Use custom report format",
    )
