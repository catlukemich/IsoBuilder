class PickResults:
    def __init__(self):
        self.objects = []

    def addObject(self, object):
        self.objects.append(object)

    def removeObject(self, object):
        self.objects.remove(object)

    def hasObjectOfClass(self, obj_class):
        for own_object in self.objects:
            if isinstance(own_object, obj_class):
                return True
        return False

    def getObjectOfClass(self, obj_class):
        for own_object in self.objects:
            if isinstance(own_object, obj_class):
                return own_object
        return None

    def reverse(self):
        self.objects.reverse()

    def __str__(self):
        ret = ""
        for object in self.objects:
            ret += str(object)
        return ret
