import time
from cmpipe import (OrderedStage, FilterStage, Pipeline)


def echo(value):
    print(value)
    time.sleep(0.013)
    return value


def main():
    stage = FilterStage((OrderedStage(echo),), max_tasks=2)
    pipe = Pipeline(stage)
    for number in range(12):
        pipe.put(number)
        time.sleep(0.010)

    pipe.put(None)


if __name__ == '__main__':
    main()
