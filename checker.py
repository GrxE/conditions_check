def conditions_check(checks, exception_cls=RuntimeError):
    """Checks the dict *checks* if every key=condition is True.

    If not, the value=msg is raised with exception_cls

    :param exception_cls: Exception to raise if condition fails
    :param checks: a dict { condition that we expect to be ok, message if not fullfilled , ... }
    :return: None, raises exception_cls if contition fails
    """

    try:
        msg = checks[False]
        # logger.log(logging.DEBUG, msg)
        raise exception_cls(msg)
    except KeyError:
        # No condition was False
        pass
