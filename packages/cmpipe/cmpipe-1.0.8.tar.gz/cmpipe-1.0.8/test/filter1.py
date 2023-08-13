import time
from cmpipe import (OrderedStage, FilterStage, Pipeline, OrderedWorker, Stage)


def pass_thru(value):
    time.sleep(0.013)
    return value


class Pull(object):
    def __init__(self, pipe):
        self.pipe = pipe

    def __call__(self, task):
        for task, result in self.pipe.results():
            print('{0} {1}'.format(task, result))
        #    # if result:
        #    #     print('{0} {1}'.format(task, result[0]))


def main():
    s1 = FilterStage(
        (OrderedStage(pass_thru),),
        max_tasks=1,
        )
    p1 = Pipeline(s1)

    p2 = Pipeline(OrderedStage(Pull(p1)))
    p2.put(True)

    for number in range(10):
        p1.put(number)
        time.sleep(0.010)

    p1.put(None)
    p2.put(None)


if __name__ == '__main__':
    main()
