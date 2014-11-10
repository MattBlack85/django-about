#!/usr/bin/env python
import os
import sys


def run_tests():
    import django
    from django.conf import global_settings
    from django.conf import settings

    sys.path.append(os.path.abspath(__file__))
    os.environ.update({'DJANGO_SETTINGS_MODULE': 'djabout_settings'})

    if hasattr(django, 'setup'):
        django.setup()
        from django.test.simple import DjangoTestSuiteRunner
        test_runner = DjangoTestSuiteRunner(verbosity=1)
        return test_runner.run_tests([
            'djabout',
        ])


def main():
    failures = run_tests()
    sys.exit(failures)

if __name__ == '__main__':
    main()
