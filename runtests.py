import unittest

def main()->int:
    test_loader = unittest.defaultTestLoader
    test_runner = unittest.TextTestRunner()
    test_suite = test_loader.discover('test')
    test_runner.run(test_suite)
    return 0

if __name__ == '__main__':
    exit(main())