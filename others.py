#!/usr/bin/env python3
#
# GlobalChem - Thai Spices
#
# -----------------------------------

class Unclassified(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:

            'L-p Giu-L-Leu-OCH3' : '',
            'β-sitosterol' : '',
            'β-daucosterol' : '',          
                
        '''

        smiles = {'benzoic acid' : 'C1=CC=C(C=C1)C(=O)O',
                  'phenylmethanol' : 'C1=CC=C(C=C1)CO',
                  'dibutyl phthalate' : 'CCCCOC(=O)C1=CC=CC=C1C(=O)OCCCC',
                  'pyroglutamyl-phenylalanine methyl ester' : 'C1=CC=C(C=C1)[Al](CO[As](C2=CC=CC=C2)N)N',
                  'pyrogiutamyl-tyrosine methyl ester' : 'CC[As](COC)[Ge](C)(C)N',
                  'furan-2-carboxylc acid' : 'C1=COC(=C1)C(=O)O.C1=COC(=C1)C(=O)O',


                  }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {}

        return smarts
