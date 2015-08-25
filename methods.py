class Obj(object):
    def __init__(self):
        pass

    def m(self, *args):
        return self, args

    @classmethod
    def cm(*args):
        return args

    @staticmethod
    def sm(*args):
        return args


o = Obj()
print "method:", o.m()
print "class method:", o.cm()
print "static method:", Obj.sm()
