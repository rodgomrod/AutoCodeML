#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .preprocessing_methods.categorical.freq import *
from .preprocessing_methods.categorical.label import *
from .preprocessing_methods.categorical.onehot import *
from .preprocessing_methods.numerical.maxabs import *
from .preprocessing_methods.numerical.minmax import *
from .preprocessing_methods.numerical.scale import *
from .preprocessing_methods.numerical.standard import *

class prepro(freq, label, onehot, maxabs, minmax, scale, standard):

    def __init__(self, file, separate, how_cat, how_num):
        self.file = file
        self.separate = separate
        self.how_cat = how_cat
        self.how_num = how_num

        # Categorical functions
        freq.__init__(self, file=self.file, separate=self.separate)
        label.__init__(self, file=self.file, separate=self.separate)
        onehot.__init__(self, file=self.file, separate=self.separate)

        # Numerical functions
        maxabs.__init__(self, file=self.file, separate=self.separate)
        minmax.__init__(self, file=self.file, separate=self.separate)
        scale.__init__(self, file=self.file, separate=self.separate)
        standard.__init__(self, file=self.file, separate=self.separate)


    def transform(self):

        if self.how_cat == 'freq':
            freq.transform(self)
        elif self.how_cat == 'label':
            label.transform(self)
        elif self.how_cat == 'onehot':
            onehot.transform(self)
        else:
            raise ValueError('{} is not in the how_cat list: ["freq", "label", "onehot"]'.format(self.how_cat))

        if self.how_num == 'maxabs':
            maxabs.transform(self)
        elif self.how_num == 'minmax':
            minmax.transform(self)
        elif self.how_num == 'scale':
            scale.transform(self)
        elif self.how_num == 'standard':
            standard.transform(self)
        else:
            raise ValueError('{} is not in the how_num list: ["maxabs", "minmax", "scale", "standard"]'.format(self.how_num))


