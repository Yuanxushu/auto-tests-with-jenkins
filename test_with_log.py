#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import logging
from logger import logger, err_logger
from utils import assert_failure

import pytest


def test_data(caplog):
    data = [1, 2, 3, 4, 5]
    check_data(data)
    logger.info("here: " + caplog.text)


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@assert_failure
def check_data(data):
    failures = []
    for i in data:
        if i % 2 == 0:
            err_logger.error("Fail: %s Not odd" % i)
            failures.append("Fail: %s Not odd" % i)
        else:
            logger.info("Pass: %s" % i)
    return failures
