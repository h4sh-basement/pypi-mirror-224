import argparse
from anadroid.Anadroid import AnaDroid
from anadroid.Config import set_general_config
from anadroid.Types import TESTING_FRAMEWORK, PROFILER, ANALYZER, INSTRUMENTER
from anadroid.application.AndroidProject import BUILD_TYPE
from anadroid.device.Device import set_device_conn
from anadroid.device.MockedDevice import MockedDevice
from anadroid.instrument.Types import INSTRUMENTATION_TYPE


def init_PyAnaDroid_from_args(args):
    return AnaDroid(arg1=args.diretory if (len(args.package_names) + len(args.application_packages) == 0) else args,
                    testing_framework=TESTING_FRAMEWORK(args.testingframework),
                    device=MockedDevice() if args.buildonly or args.justanalyze else None,
                    profiler=PROFILER(args.profiler),
                    build_type=BUILD_TYPE(args.buildtype),
                    instrumenter=INSTRUMENTER(args.instrumenter),
                    instrumentation_type=INSTRUMENTATION_TYPE(args.instrumentationtype),
                    analyzer=ANALYZER(args.analyzer),
                    tests_dir=args.tests_dir,
                    rebuild_apps=args.rebuild,
                    reinstrument=args.reinstrument,
                    recover_from_last_run=args.recover,
                    test_cmd=args.command,
                    load_projects=not args.run_only
                    )


def process_general_config(args_obj):
    n_times = args_obj.n_times if args_obj.n_times != 0 else 0
    if n_times != 0:
        set_general_config('tests', 'tests_per_app', n_times)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--testingframework", default=TESTING_FRAMEWORK.MONKEY.value, type=str,
                        help="testing framework to exercise app(s)", choices=[e.value for e in TESTING_FRAMEWORK])
    parser.add_argument("-p", "--profiler", default=PROFILER.MANAFA.value, type=str,
                        help="energy profiler", choices=[e.value for e in PROFILER])
    parser.add_argument("-b", "--buildtype", default=BUILD_TYPE.DEBUG.value, type=str,
                        help="app build type", choices=[e.value for e in BUILD_TYPE])
    parser.add_argument("-i", "--instrumenter", default=INSTRUMENTER.JINST.value, type=str,
                        help="Source code instrumenter", choices=[e.value for e in INSTRUMENTER])
    parser.add_argument("-it", "--instrumentationtype", default=INSTRUMENTATION_TYPE.ANNOTATION.value, type=str,
                        help="instrumentation type", choices=[e.value for e in INSTRUMENTATION_TYPE])
    parser.add_argument("-a", "--analyzer", default=ANALYZER.MANAFA_ANALYZER.value, type=str, help="results analyzer",
                        choices=[e.value for e in INSTRUMENTATION_TYPE])
    parser.add_argument("-d", "--diretory", default="demoProjects", type=str, help="app(s)' folder")
    parser.add_argument("-bo", "--buildonly", help="just build apps", action='store_true')
    parser.add_argument("-record", "--record", help="record test", action='store_true', default=False)
    parser.add_argument("-run", "--run_only", help="run only", action='store_true')
    #parser.add_argument("-rt", "--retry", help="retry build if previously failed", action='store_true')
    parser.add_argument("-rb", "--rebuild", help="rebuild apps", action='store_true')
    parser.add_argument("-ri", "--reinstrument", help="reinstrument app", action='store_true')
    parser.add_argument("-ja", "--justanalyze", help="just analyze apps", action='store_true')
    #parser.add_argument("-c", "--connection", help="connection to device", choices=["USB", "WIFI"], default="USB")
    parser.add_argument("-sc", "--setconnection", help="set connection to device and exit", choices=["USB", "WIFI"])
    parser.add_argument("-ds", "--device_serial", help="device serial id", type=int, default=None)
    parser.add_argument("-td", "--tests_dir", help="tests directory", type=str, default=None)
    parser.add_argument("-n", "--package_names", help="package(s) of already installed apps", nargs='+', default=[])
    parser.add_argument("-apk", "--application_packages", help="path of apk(s) to process", nargs='+', default=[])
    parser.add_argument("-rec", "--recover", help="recover progress of the previous run", action='store_true')
    parser.add_argument("-cmd", "--command", help="test command", type=str, default=None)
    parser.add_argument("-nt", "--n_times", help="times to repeat test (overrides config)", type=int, default=0)
    args = parser.parse_args()
    process_general_config(args)
    if args.setconnection:
        set_device_conn(args.setconnection, device_id=args.device_serial)
        exit(0)
    anadroid = init_PyAnaDroid_from_args(args)
    if args.buildonly:
        anadroid.just_build_apps()
    elif args.justanalyze:
        anadroid.just_analyze()
    elif args.record:
        anadroid.record_test(args.tests_dir)
    elif args.run_only:
        anadroid.exec_command()
    else:
        anadroid.default_workflow()


if __name__ == '__main__':
    main()