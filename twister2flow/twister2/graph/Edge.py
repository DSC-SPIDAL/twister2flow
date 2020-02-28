class Edge(object):

    def __init__(self, name, parent, child):
        self.__name = name
        self.__parent = parent
        self.__child = child

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @parent.deleter
    def parent(self):
        del self.__parent

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, child):
        self.__child = child

    @child.deleter
    def child(self):
        del self.__child
