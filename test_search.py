# -*- coding: utf-8 -*-
from model.searchpar import SearchPar

def test_search_found_result(app):
    app.search(SearchPar.Param1())
    assert app.is_found()

def test_search_unfound_result(app):
    app.search(SearchPar.Param2())
    assert app.is_not_found()