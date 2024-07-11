
class Range:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val


    def intersects(self, other):
        intersection = self.intersection(other)
        if intersection != None:
            return True
        else:
            return False

    def intersection(self, other):
        res_min = max(self.min_val, other.min_val)
        res_max = min(self.max_val, other.max_val)
        if res_min < res_max:
            return Range(res_min, res_max)
        else:
            return None


    def contains(self, value):
        return value > self.min_val and value < self.max_val

if __name__ == "__main__":
    r1 = Range(0,10)
    r2 = Range(11,20)
    r3 = Range(5,11)

    print(r1.intersects(r2))
    print(r1.intersects(r3))
    print(r2.intersects(r3))
