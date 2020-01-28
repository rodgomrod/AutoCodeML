#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .ft_selection_methods.correlation import *
from .ft_selection_methods.permutation import *

# TODO others feature selection methods like chi2, etc.

class feature_selection(permutation_importance, feature_correlation):

    def __init__(self, file, how_ft_sel):

        self.file = file
        self.how_ft_sel = how_ft_sel

        permutation_importance.__init__(self, file=self.file)
        feature_correlation.__init__(self, file=self.file)


    def method_finder(self, how):
        if how == 'permutation':
            permutation_importance.select(self)
        elif how == 'correlation':
            feature_selection.select(self)
        else:
            raise ValueError(
                '{} is not in the how_ft_sel list: ["permutation", "correlation"]'.format(how))


    def select_ft_method(self):

        if type(self.how_ft_sel) == list:
            for ft_met in self.how_ft_sel:
                self.method_finder(ft_met)
        else:
            self.method_finder(self.how_ft_sel)


