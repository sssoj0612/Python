class Service:
    secret = "영구는 배꼽이 두 개다."
    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print ("%s님 %s + %s = %s입니다." % (self.name, a, b, result))