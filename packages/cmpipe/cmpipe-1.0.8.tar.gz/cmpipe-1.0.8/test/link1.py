from cmpipe import (OrderedStage as OStage, Pipeline)


def magnify(value):
    return value*10


def main():
    p1 = Pipeline(
        OStage(magnify).link(
            OStage(magnify).link(
                OStage(magnify).link(
                    OStage(magnify)
                    )
                )
            )
        )
    for val in list(range(10)) + [None]:
        p1.put(val)

    for result in p1.results():
        print(result)


if __name__ == '__main__':
    main()
