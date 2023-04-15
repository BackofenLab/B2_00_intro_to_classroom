import pytest


class CustomReport:
    def pytest_terminal_summary(self, terminalreporter):
        tr = terminalreporter
        passed_tests = {}
        failed_functions = set()

        for rep in tr.getreports(''):
            func_name = rep.nodeid.split("::")[1]
            if rep.passed:
                passed_tests[func_name] = passed_tests.get(func_name, 0) + 1
            elif rep.failed:
                failed_functions.add(func_name)
                if func_name in passed_tests:
                    del passed_tests[func_name]

        for func_name in passed_tests:
            tr.write_line(f"All tests passed for the function {func_name}", green=True)

        if failed_functions:
            for rep in tr.getreports(''):
                if rep.failed and rep.nodeid.split("::")[1] in failed_functions:
                    tr.write_line(f"Test failed for {rep.nodeid}", red=True)

                    for prop in rep.user_properties:
                        if prop[0] == "input_values":
                            tr.write_line(f"Input variables are: {prop[1]}", red=True)
                        if prop[0] == "expected_result":
                            tr.write_line(f"Expected answer: {prop[1]}", red=True)
                        if prop[0] == "actual_result":
                            tr.write_line(f"Your answer: {prop[1]}", red=True)

                    failed_functions.remove(rep.nodeid.split("::")[1])

        # Suppress the default summary output.
        terminalreporter.config.option.disable_test_summary = True


def pytest_configure(config):
    # Register the custom report by default, without checking for the --custom-report option
    config.pluginmanager.register(CustomReport(), "customreport")
