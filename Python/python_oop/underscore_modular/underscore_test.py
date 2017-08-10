from underscore import Underscore

_ = Underscore()

print _.filter([1,2,3,4], lambda x: x % 2 == 0)