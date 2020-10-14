# callonce

## Usage

```python
from callonce import callonce


@callonce
def _return_true() -> bool:
    return True


def _call_return_true():
    return _return_true()


def _call_return_true_3times():
    return _return_true(times=3)


def test_call_once():
    assert _call_return_true() == True
    assert _call_return_true() == None


def test_call_3times():
    assert _call_return_true_3times() == True
    assert _call_return_true_3times() == True
    assert _call_return_true_3times() == True
    assert _call_return_true_3times() == None
```
