def difference(*args) -> int | float:
    if args:
        lowest = min(args)
        highest = max(args)
        res = round(highest - lowest, 1)
        print(res)
        return res
    else:
        return 0


if __name__ == "__main__":
    assert difference(1, 2, 3) == 2
    assert difference(5, -5) == 10
    assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    assert difference() == 0
    print('OK')
