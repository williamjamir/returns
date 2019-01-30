# -*- coding: utf-8 -*-

import pytest

from dry_monads.either import Left, Right
from dry_monads.primitives.exceptions import UnwrapFailedError


def test_unwrap_success():
    """Ensures that unwrap works for Right monad."""
    assert Right(5).unwrap() == 5


def test_unwrap_failure():
    """Ensures that unwrap works for Left monad."""
    with pytest.raises(UnwrapFailedError):
        assert Left(5).unwrap()