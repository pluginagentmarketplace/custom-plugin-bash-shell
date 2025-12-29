# Testing Guide

## Test Pyramid

```
         E2E (10%)
       Integration (20%)
      Unit Tests (70%)
```

## Jest Example
```javascript
test("adds 1 + 2", () => {
  expect(add(1, 2)).toBe(3);
});
```

## PyTest Example
```python
def test_add():
    assert add(1, 2) == 3
```
