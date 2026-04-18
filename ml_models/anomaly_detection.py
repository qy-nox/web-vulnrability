from statistics import mean


def score(values: list[float]) -> float:
    if not values:
        return 0.0
    baseline = mean(values)
    return round(abs(values[-1] - baseline), 4)
