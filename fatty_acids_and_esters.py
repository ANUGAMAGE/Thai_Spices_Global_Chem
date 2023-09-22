#!/usr/bin/env python3
#
# GlobalChem - Thai Spices
#
# -----------------------------------

class ThaiSpices(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing :
            
        '''
        smiles = {'stearic acid' : 'CCCCCCCCCCCCCCCCCC(=O)O',
                  'dec-5-enoic acid' : 'CCCCC=CCCCC(=O)O',
                  '2-tetradecenoic acid' : 'CCCCCCCCCCC/C=C/C(=O)O',
                  'linolenic acid' : 'CC/C=C\C/C=C\C/C=C\CCCCCCCC(=O)O',
                  'linoleic acid' : 'CCCCC/C=C\C/C=C\CCCCCCCC(=O)O',
                  'ethyl icosanoate' : 'CCCCCCCCCCCCCCCCCCCC(=O)OCC',
                  'monopalmitin' : 'CCCCCCCCCCCCCCCC(=O)OCC(CO)O',
                  'trimethyl citrate' : 'COC(=O)CC(CC(=O)OC)(C(=O)OC)O',
                  '1,5-dimethyl citrate' : 'COC(=O)CC(CC(=O)OC)(C(=O)[O-])O',
                  '5,6-dimethyl citrate' : 'CC1=C(C)C(=O)[O-]',
                  '3-carboxyethyl-3-hydroxyglutaric acid 1,5-dimethyl ester' : 'C[As](CCC(=O)O)(O)O'}

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {}

        return smarts