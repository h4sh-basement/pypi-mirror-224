import pytest
import uuid
from sqlconstructor import SqlVals


def test_inline_one_element():
    assert (
        str(
            SqlVals(
                1,
            ).inline()
        )
        == '1'
    )


def test_inline_two_and_more_elements():
    _uuid = uuid.uuid4()
    assert (
        str(
            SqlVals(
                1,
                'phone',
                _uuid,
            ).inline()
        )
        == f"1, 'phone', '{_uuid}'"
    )


def test_inline_wrap_one_element():
    assert (
        str(
            SqlVals(
                1,
            ).inline().wrap()
        )
        == '(\n  1\n)'
    )


def test_inline_wrap_two_and_more_elements():
    _uuid = uuid.uuid4()
    assert (
        str(
            SqlVals(
                1,
                'phone',
                _uuid,
            ).inline().wrap()
        )
        == f"(\n  1, 'phone', '{_uuid}'\n)"
    )
