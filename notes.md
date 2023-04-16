# Unittest

only tests classes that inherit from `unittest.TestCase`, more explicit

# PyTest

Tests all the functions that start with test, and all Classes that start with Test, 
    additionally all unittest tests are supported as well.

# Discovery

The `test` folder should be a module for ease of testing and better path resolution

All files that start with `test`are discovered by both packages,
    with the `test_variant2` an additional parent folder and/or the pattern for tests may be specified.