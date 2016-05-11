# -*- coding: utf-8 -*-

class SearchPar(object):

    def __init__(self, param=""):
        self.param = param

    @classmethod
    def Param1(cls):
        return cls(param=u'брюки')

    @classmethod
    def Param2(cls):
        return cls(param="111")