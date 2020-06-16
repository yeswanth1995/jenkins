#multiple inheritence
class A:
    def add(self):
        return 10


class B:
    def add(self):
        return 20


class C(A,B):
    pass


c1 = C()
print(c1.add())