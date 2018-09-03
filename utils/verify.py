from utils.logs import log


class Verify(object):

    @staticmethod
    def greater_than(expected, actual, message_on_fail):
        try:
            assert expected > actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error("{}: {}".format(err_type, message_on_fail))
            log.debug("{0} should be greater {1}".format(expected, actual))
            raise err

    @staticmethod
    def equals(expected, actual, message_on_fail):
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error("{}: {}".format(err_type, message_on_fail))
            log.debug("\n\texpected: {}  \n\tactual:   {}".format(expected, actual))
            raise err

    @staticmethod
    def not_equals(expected, actual, message_on_fail):
        try:
            assert expected is not actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error("{}: {}".format(err_type, message_on_fail))
            log.debug("{} should not be equal to {}".format(expected, actual))
            raise err

    @staticmethod
    def true(condition, message_on_fail):
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error("{}: {}".format(err_type, message_on_fail))
            raise err

    @staticmethod
    def false(condition, message_on_fail):
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error("{}: {}".format(err_type, message_on_fail))
            raise err

    @staticmethod
    def each(expected, actual, message_on_fail):
        """
        Compare two lists.
        Order of the lists can be different.
        Raise AssertionError if at least one mismatch was found between two lists.
        :param expected: list with expected values
        :param actual: list with actual values
        """
        result = set(actual) & set(expected)
        if len(expected) != len(result):
            raise AssertionError(message_on_fail)

    @staticmethod
    def contains(expected, actual, message_on_fail):
        try:
            assert expected in actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.debug("\n\texpected: {} value contains actual:   {}".format(expected, actual))
            log.error("{}: {}".format(err_type, message_on_fail))
            raise err
