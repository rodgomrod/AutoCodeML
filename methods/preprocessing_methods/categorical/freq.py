#!/usr/bin/env python
# -*- coding: utf-8 -*-

class freq(object):

    def __init__(self, file, separate):
        self.file = file
        self.separate = separate


    def transform(self):
        self.file.write('## Frequency Encoder Method ##\n\n')
        self.file.write('def freq_parser(x):\n'
                        '\ttry:\n'
                        '\t\treturn dict_freq[x]\n'
                        '\texcept:\n'
                        '\t\treturn len(dict_freq)\n\n')

        self.file.write('for col in categorical_cols:\n'
                        '\tcategories = X_fit[col].value_counts().index.tolist()\n'
                        '\tdict_freq = dict()\n'
                        '\tfor i, cat in enumerate(categories):\n'
                        '\t\tdict_freq[cat] = i\n\n'
                        '\tX_fit[col] = X_fit[col].apply(lambda x: freq_parser(x))\n'
                        '\tX_val[col] = X_val[col].apply(lambda x: freq_parser(x))\n')
        if self.separate:
            self.file.write('\tX_test[col] = X_test[col].apply(lambda x: freq_parser(x))\n')
        self.file.write('\n\n')
