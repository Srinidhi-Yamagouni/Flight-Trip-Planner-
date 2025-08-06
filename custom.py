def comp1(tuple1, tuple2):
    return tuple1[0] < tuple2[0]

def comp2(tuple1, tuple2):
    if tuple1[0] == tuple2[0]:
        return tuple1[1] < tuple2[1]
    else:
        return tuple1[0] < tuple2[0]