import parsers

_SLTBENCH_CPPMAIN = '''
#include <sltbench/Bench.h>
SLTBENCH_MAIN();
'''

_GOOGLEBENCH_CPPMAIN = '''
#include <benchmark/benchmark.h>
BENCHMARK_MAIN();
'''

SLTBENCH = 'sltbench'
GOOGLEBENCH = 'googlebench'
ALL = [SLTBENCH, GOOGLEBENCH]


class BackendSLTBench:

    def __init__(self, install_path):
        self.install_path = install_path
        self.static_lib_name = 'sltbench_static'
        self.required_static_libs = []
        self.maincpp_code = _SLTBENCH_CPPMAIN
        self.option_json_reporter = '--reporter=json'
        self.result_parser = parsers.PerfResultsParserSLTBench()

class BackendGooglebench:

    def __init__(self, install_path):
        self.install_path = install_path
        self.static_lib_name = 'benchmark'
        self.required_static_libs = ['pthread']
        self.maincpp_code = _GOOGLEBENCH_CPPMAIN
        self.option_json_reporter = '--benchmark_format=json'
        self.result_parser = parsers.PerfResultsParserGoogleBench()
