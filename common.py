class Terpenoids(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:
        
            '6β, 14β-dihydroxyisopimara-8(9),15-diene' : '', 
                
        '''

        smiles = {
              '3-caren-5-one'                                      : 'CC1=CC(=O)C2C(C1)C2(C)C',
              '(3r,4r,6s)-3,6-Dihydroxy-1-menthene'                : 'CC1=C[C@@H]([C@H](C[C@@H]1O)C(C)C)O',
              '(1R,2S,4R)-p-menth-5-ene-1,2,8-triol'               : 'O[C@H]1[C@@H]([C@H](C=C)[C@H](O)C1)CO',
              'Oxyphyllenodiol B'                                  : 'CC(C)[C@H]1CCC(=O)C2=C1[C@@H]([C@](CC2)(C)O)O',
              'hedytriol'                                          : 'CC(C)(C)C1=CC(=C(C(=C1)O)O)C(C)(C)C',
              'kaemgalangol A'                                     : 'CC(C)(C)CCCC(C)(C)CCCC(C)(C)CCCC(C)(C)CCCC1=CC(=C(C(=C1)O)O)C(C)(C)C',
              '6β-hydroxypimara-8(14), 15-diene-1-one'             : 'O[C@@H]1[C@@H](C)C[C@@H]2[C@]1(CC[C@@H]3[C@H]2CC=C4[C@@]3(C)CCC(=C4)C(=O)C)C',
              'sandaracopimaradien-6β, 9α-diol-l-one'              : 'O=C[C@@]1(C)[C@H]2[C@@H](O)C[C@H]3[C@](O)(C)[C@]4(C)CC[C@@H]5[C@@]4(C)CC[C@@H](O)C(C)(C)[C@]35C2=C1',
              '(-)-Sandaracopimaradiene'                           : 'C[C@@]1(CC[C@H]2C(=C1)CC[C@@H]3[C@@]2(CCCC3(C)C)C)C=C',
              'sandaracopimaradiene-9α-ol'                         : 'CC(C)[C@]1(C)CC[C@@H](CC1)C(C)C2=CC(=C[C@@H](O)C2)C',
              'kaempulchraol l'                                    : 'C[C@@]1(CC[C@]2(C(=C1)C[C@H]([C@@H]3[C@@]2(CCCC3(C)C)C)O)OC)C=C',
              'kaempulchraol E'                                    : 'C[C@]12[C@H]3CC[C@@H](C=C3C[C@H]([C@@H]1C(CC[C@@H]2O)(C)C)O)C=C',
              '8(14),15-sandaracopimaradiene- 1a,9α-diol'          : 'CC1=C2[C@]([C@H]3[C@]4([C@@H]([C@H](C)C(C)(C)[C@H]4CC[C@@]3(C)C2)CC[C@H]1O)C)(C)C',
              'kaempulchraol L'                                    : 'C[C@@]1(CC[C@]2(C(=C1)C[C@H]([C@@H]3[C@@]2(CCCC3(C)C)C)O)OC)C=', # Mistake
              '2α-acetoxy sandaracopimaradien-1α-ol'               : 'CC(=O)OC1(C2[C@@]([C@@H]3[C@]4([C@H](C(C)=C)[C@@H]([C@H]4CC[C@]3(C)C2)CC[C@@H]1O)(C)C)C',
              '1,11-dihydroxypimara-8(14), 15-diene'               : 'CC1=CCCC2C(C1)CCC(C2)(O)C(C=C)C(CO)C',
              '6β, 14α-dihydroxyisopimara-8(9),15-diene'           : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@@H](O)C[C@@H](O)C4=C(C)[C@H](O)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              '6α, 14β-dihydroxyisopimara-8(9), 15-diene'          : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@H](O)C[C@H](O)[C@@]4(C)[C@H](O)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              '1α-hydroxy-14α-methoxyisopimara-8(9),15-diene'      : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@H](O)[C@H](OC)[C@@]4(C)[C@H](C)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              '1α,14α-dihydroxyisopimara-8(9),15-diene'            : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@H](O)[C@@H](O)[C@@]4(C)[C@H](C)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              'boesenberol l'                                      : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@H](C)[C@@H](O)[C@@]4(C)[C@H](C)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              'boesenberol J'                                      : 'CC(C)[C@]1(C)[C@@H]2CC=C3[C@H](C)[C@@H](O)[C@@]4(C)[C@H](C)C[C@@]4(C)[C@]3(C)CC[C@@H]2[C@@]1(C)C',
              '6β-acetoxysandaracopimaradiene-9α-ol'               : 'CC(=O)O[C@@]1(C)[C@H]2CC[C@](C)(O)C(C)(C)[C@@]2(C)[C@@H]3CC[C@@]4(C)[C@H](O)CC[C@]4(C)[C@@]3(C)CC1',
              '6β-acetoxysandaracopimaradiene-9α-ol-1-one'         : 'CC(=O)[C@@]1(C)[C@H]2CC[C@](C)(O)C(C)(C)[C@@]2(C)[C@@H]3CC[C@@]4(C)[C@H](O)CC[C@]4(C)[C@@]3(C)CC1',
              '6β-acetoxysandaracopimaradiene-1α,9α-diol'          : 'CC(=O)[C@]1(C)[C@@H]2CC[C@](C)(O)C(C)(C)[C@@]2(C)[C@@H]3CC[C@@]4(C)[C@@H](O)CC[C@]4(C)[C@@]3(C)CC1',
              '6β-acetoxy-1α-14α-dihydroxyisopimara-8(9),15-diene' : 'CC(=O)[C@]1(C)[C@@H]2CC[C@](C)(O)[C@@]3(C)[C@H](O)C[C@@]4(C)[C@H](O)C[C@@]4(C)[C@@]3(C)CC[C@@H]2[C@@]1(C)C',
         }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
class Polysaccharides(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:
            
    
        '''

        smiles = {'fucose' : 'C[C@H]1[C@H]([C@H]([C@@H](C(O1)O)O)O)O',
                  'arabinose' : 'C1[C@@H]([C@@H]([C@H](C(O1)O)O)O)O',
                  'xylose' : 'C1[C@H]([C@@H]([C@H](C(O1)O)O)O)O',
                  'rhamnose' : 'C[C@H]1[C@@H]([C@H]([C@H](C(O1)O)O)O)O',
                  'mannose' : 'C([C@@H]1[C@H]([C@@H]([C@@H](C(O1)O)O)O)O)O',
                  'galactose' : 'C([C@@H]1[C@H]([C@@H]([C@@H](C(O1)O)O)O)O)O',
                  'glucose' : 'C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O',
                  'glucuronic acid' : 'C1=CN(C(=O)NC1=O)[C@H]2[C@@H]([C@@H]([C@H](O2)COP(=O)(O)OP(=O)(O)O[C@@H]3[C@@H]([C@H]([C@@H]([C@H](O3)C(=O)O)O)O)O)O)O',
                  'galacturonic acid' : '[C@@H]1([C@H]([C@H](OC([C@@H]1O)O)C(=O)O)O)O'}

        
        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
class Phenolics(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:

            '4-methoxybenzyl-O-β-D-glucopyranoside': '',
            '1-O-4-carboxylphenyl-(6-O-4-hydroxybenzoyl)-β-D-glucopyranoside': '',            
        '''

        smiles = {'p-metho-xybenzoicacid' : 'COC1=CC=CC=C1C(=O)O.COC1=CC=CC=C1C(=O)O',
                  'p-hydroxybenzoic acid' : 'C1=CC(=CC=C1C(=O)O)O',
                  'vanillic acid' : 'COC1=C(C=CC(=C1)C(=O)O)O',
                  'methyl 3,4-dihydroxybenzoate' : 'COC(=O)C1=CC(=C(C=C1)O)O',
                  'methyl (2R,3S)-2,3-dihydroxy-3-(4-methoxyphenyl) propanoate' : 'COC1=CC=C(C=C1)[C@@H]([C@H](C(=O)OC)O)O',
                  'ethyl (2R,3S)-2,3-dihydroxy-3-(4-methoxyphenyl) propanocate' : 'CCOC(=O)[C@@H]([C@H](C1=CC=C(C=C1)OC)O)O',
                  'trans ethyl p-methoxycinnamate' : 'CCOC(=O)/C=C/C1=CC=C(C=C1)OC',
                  'ferulic acid' : 'COC1=C(C=CC(=C1)/C=C/C(=O)O)O',
                  'trans p-hydroxycinnamic acid' : 'C1=CC(=CC=C1/C=C/C(=O)O)O',
                  'trans p-methoxycinnamic acid' : 'COC1=CC=C(C=C1)/C=C/C(=O)O',
                  'trans ethyl cinnamate' : 'CCOC(=O)/C=C/C1=CC=CC=C1',
                  'cis ethyl p-methoxycinnamate' : 'CCOC(=O)/C=C\C1=CC=C(C=C1)OC',
                  '4-methoxy-benzyl (E)-3-(4-methoxyp-henyl) acrylate' : 'COC1=CC=C(C=C1)/C(=C\C(=O)OCC2=CC=CC=C2)/OC',
}

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
class Flavonoids(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:
                
        '''

        smiles = {'kaempferol' : 'C1=CC(=CC=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O',
                  'luteolin': 'C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O)O',
                  'kaempferide' : 'COC1=CC=C(C=C1)C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O'}

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
class FattyAcidsAndEsters(object):

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

        smarts = {

        }

        return smarts
    
class DyarilHeptanoids(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:    
            'hedycoropyran B' : '',            
        '''

        smiles = {'(3R,5S)-3,5-dihydroxy-1,7-bis(3,4- dihydroxyphenyl) heptane' : 'C1=CC(=C(C=C1CC[C@H](C[C@H](CCC2=CC(=C(C=C2)O)O)O)O)O)O',
                  '(1R,3R,5R)-1,5-epoxy-3-hydroxy-1-(3,4-dihydroxyphenyl)-7-(3,4-dihydroxypheny) heptane' : 'C(C[C@H](C[C@H](C[C@H](C1=CC=C(C(=C1)O)O)OO)O)O)C2=CC=C(C(=C2)O)O',
                  '(1R,3R,5R)-1,5-epoxy-3-hydroxy-1-(3,4-dihydroxyphenyl)-7-(4-hydroxyphenyl) heptane 3-O-p-D-glucopyranoside' : 'C1=C(C=CC(=C1)O)CC[C@H](C[C@H](C[C@H](C2=CC=C(C(=C2)O)O)O[Hg])O)O[67O]',
                  'phaeoheptanoxide' : 'CCCCCCC(=O)[O-]',
                  '1-(4-hydroxy-3-methoxyphenyl)-7-(4-hydroxyphenyl) heptane-1,2,3,5,6-pentanol' : 'COC1=CC(=CC=C1O)C(C(C(CC(C(CC2=CC=C(C=C2)O)O)O)O)O)O',
                  'kaempsulfonic acid A': 'OS(=O)(=O)[SH+]',
                  'kaempsulfonic acid A': '[Pb](=O)(=O)(O)S(=O)(=O)O'}

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
class CyclicDypeptides(object):

    def __init__(self):

        self.name = 'Thai Spices'

    @staticmethod
    def get_smiles():

        '''

        Missing:  
            'cyclo-(L-Val-L-Val)': '',
            'cyclo-(L-Ala-L-lle)': '',
            'cyclo-(L-Ala-L-Phe)': '',
            'cyclo-(L-Val-L-Ala)': '',
            'cyclo-(L-Leu-L-Tyr)': '',
            'cyclo-(L-Val-L-Tyr)': '',
            'cyclo-(L-Asp-OCH3-L-Phe)': '',
            'cyclo-(L-Tyr-L-lle)' : '',
            'cyclo-(L-Glu-OCH3-L-Phe)' : '',
        '''

        smiles = {'cyclo-(L-Val-L-Phe}' : 'CC(C)[C@H]1C(=O)N[C@H](C(=O)N1)CC2=CC=CC=C2',
                  'cyclo-(L-Val-L-Leu)' : 'CC(C)C[C@H]1C(=O)N[C@@H](C(=O)N1)C(C)C',
                  'cyclo-(L-Ala-L-Leu)' : 'C[C@H]1C(=O)N[C@H](C(=O)N1)CC(C)C',
                  'cyclo-(L-Phe-L-Tyr)' : 'C1=CC=C(C=C1)C[C@H]2C(=O)N[C@H](C(=O)N2)CC3=CC=C(C=C3)O',
                  'cyclo-(L-Pro-L-Tyr)' : 'C1C[C@H]2C(=O)N[C@H](C(=O)N2C1)CC3=CC=C(C=C3)O',
                  'cyclo-(L-Leu-L-Phe)' : 'CC(C)C[C@H]1C(=O)N[C@H](C(=O)N1)CC2=CC=CC=C2 ',
                  'cyclo-(L-Leu-L-lle)' : 'C1CCC(C1)[PbH]'

                    }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {

        }

        return smarts
    
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

        smarts = {
            
        }

        return smarts
    

