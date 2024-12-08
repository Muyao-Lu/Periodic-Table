import periodictable

class LanthanidesPortal:
    symbol = ""
    name = "Lanthanides"
    number = "57-71"

class ActinidesPortal:
    symbol = ""
    name = "Actinides"
    number = "89-103"

class Legend:
    number = ""
    name = ""

class HydrogenLegend(Legend):
    symbol = "Hydrogen"
    max_word_length = 8

class AlkaliMetalLegend(Legend):
    symbol = "Alkali\n Metals"
    max_word_length = 6

class AlkalineEarthMetalLegend(Legend):
    symbol = "Alkaline\n Earth\n Metals"
    max_word_length = 8

class TransitionMetalLegend(Legend):
    symbol = "Transition\n Metals"
    max_word_length = 10

class OtherMetalLegend(Legend):
    symbol = "Other\n Metals"
    max_word_length = 6

class MetalloidLegend(Legend):
    symbol = "Metalloids"
    max_word_length = 10

class NonMetalLegend(Legend):
    symbol = "Non \n Metals"
    max_word_length = 6

class HalogenLegend(Legend):
    symbol = "Halogens"
    max_word_length = 8

class NobelGasesLegend(Legend):
    symbol = "Non \n Metals"
    max_word_length = 6

class LanthanidesLegend(Legend):
    symbol = "Lanthanides"
    max_word_length = 11

class ActinidesLegend(Legend):
    symbol = "Actinides"
    max_word_length = 9

families = [{1: periodictable.H, 4: HydrogenLegend},  # Hydrogen
            {5: AlkaliMetalLegend, 19: periodictable.Li, 37: periodictable.Na, 55: periodictable.K, 73: periodictable.Rb, 91: periodictable.Cs, 109: periodictable.Fr},  #Alkali metals
            {6: AlkalineEarthMetalLegend, 20: periodictable.Be, 38: periodictable.Mg, 56: periodictable.Ca, 74: periodictable.Sr, 92: periodictable.Ba, 110: periodictable.Ra},  # Alkaline Earth Metals
            {7: TransitionMetalLegend, 57: periodictable.Sc, 58: periodictable.Ti, 59: periodictable.V, 60: periodictable.Cr, 61: periodictable.Mn, 62: periodictable.Fe, 63: periodictable.Co, 64: periodictable.Ni, 65: periodictable.Cu, 66: periodictable.Zn, 75: periodictable.Y, 76: periodictable.Zr, 77: periodictable.Nb, 78: periodictable.Mo, 79: periodictable.Tc, 80: periodictable.Ru, 81: periodictable.Rh, 82: periodictable.Pd, 83: periodictable.Ag, 84: periodictable.Cd
             , 94: periodictable.Hf, 95: periodictable.Ta, 96: periodictable.W, 97: periodictable.Re, 98: periodictable.Os, 99: periodictable.Ir, 100: periodictable.Pt, 101: periodictable.Au, 102: periodictable.Hg, 112: periodictable.Rf, 113: periodictable.Db, 114: periodictable.Sg, 115: periodictable.Bh, 116: periodictable.Hs, 117: periodictable.Mt, 118: periodictable.Ds, 119: periodictable.Rg, 120: periodictable.Cn},  # Transition Metals
            {8: OtherMetalLegend, 49: periodictable.Al, 67: periodictable.Ga, 85: periodictable.In, 86: periodictable.Sn, 103: periodictable.Tl, 104: periodictable.Pb, 105: periodictable.Bi, 121: periodictable.Nh, 122: periodictable.Fl, 123: periodictable.Mc, 124: periodictable.Lv},  # Basic Metal ?
            {9: MetalloidLegend, 31: periodictable.B, 50: periodictable.Si, 68: periodictable.Ge, 69: periodictable.As, 87: periodictable.Sb, 88: periodictable.Te, 106: periodictable.Po},  # Metalloid
            {10: NonMetalLegend, 32: periodictable.C, 33: periodictable.N, 34: periodictable.O, 51: periodictable.P, 52: periodictable.S, 70: periodictable.Se},  # Nonmetal
            {11: HalogenLegend, 35: periodictable.F, 53: periodictable.Cl, 71: periodictable.Br, 89: periodictable.I, 107: periodictable.At, 125: periodictable.Ts},  # Halogens
            {12: NobelGasesLegend, 18: periodictable.He, 36: periodictable.Ne, 54: periodictable.Ar, 72: periodictable.Kr, 90: periodictable.Xe, 108: periodictable.Rn, 126: periodictable.Og},  # Nobel Gasses
            {13: LanthanidesLegend, 93: LanthanidesPortal, 129: periodictable.La, 130: periodictable.Ce, 131: periodictable.Pr, 132: periodictable.Nd, 133: periodictable.Pm, 134: periodictable.Sm, 135: periodictable.Eu, 136: periodictable.Gd, 137: periodictable.Tb, 138: periodictable.Dy, 139: periodictable.Ho, 140: periodictable.Er, 141: periodictable.Tm, 142: periodictable.Yb, 143: periodictable.Lu},  #Lanthanides
            {14: ActinidesLegend, 111: ActinidesPortal, 147: periodictable.Ac, 148: periodictable.Th, 149: periodictable.Pa, 150: periodictable.U, 151: periodictable.Np, 152: periodictable.Pu, 153: periodictable.Am, 154: periodictable.Cm, 155: periodictable.Bk, 156: periodictable.Cf, 157: periodictable.Es, 158: periodictable.Fm, 159: periodictable.Md, 160: periodictable.No, 161: periodictable.Lr}] # Actinides
shells = {1: [1], 2: [2], 3: [2, 1], 4: [2, 2], 5: [2, 3], 6: [2, 4], 7: [2, 5], 8: [2, 6], 9: [2, 7], 10: [2, 8],
          11: [2, 8, 1], 12: [2, 8, 2], 13: [2, 8, 3], 14: [2, 8, 4], 15: [2, 8, 5], 16: [2, 8, 6], 17: [2, 8, 7],
          18: [2, 8, 8], 19: [2, 8, 8, 1], 20: [2, 8, 8, 2], 21: [2, 8, 9, 2], 22: [2, 8, 10, 2], 23: [2, 8, 11, 2],
          24: [2, 8, 13, 1], 25: [2, 8, 13, 2], 26: [2, 8, 14, 2], 27: [2, 8, 15, 2], 28: [2, 8, 16, 2], 29: [2, 8, 18, 1],
          30: [2, 8, 18, 2], 31: [2, 8, 18, 3], 32: [2, 8, 18, 4], 33: [2, 8, 18, 5], 34: [2, 8, 18, 6], 35: [2, 8, 18, 7],
          36: [2, 8, 18, 8], 37: [2, 8, 18, 8, 1], 38: [2, 8, 18, 8, 2], 39: [2, 8, 18, 9, 2], 40: [2, 8, 18, 10, 2], 41: [2, 8, 18, 12, 1],
          42: [2, 8, 18, 13, 1], 43: [2, 8, 18, 14, 1], 44: [2, 8, 18, 15, 1], 45: [2, 8, 18, 16, 1], 46: [2, 8, 18, 18],
          47: [2, 8, 18, 18, 1], 48: [2, 8, 18, 18, 2], 49: [2, 8, 18, 18, 3], 50: [2, 8, 18, 18, 4], 51: [2, 8, 18, 18, 5],
          52: [2, 8, 18, 18, 6], 53: [2, 8, 18, 18, 7], 54: [2, 8, 18, 18, 8], 55: [2, 8, 18, 18, 8, 1], 56: [2, 8, 18, 18, 8, 2],
          57: [2, 8, 18, 18, 9, 2], 58: [2, 8, 18, 19, 9, 2], 59: [2, 8, 18, 21, 8, 2], 60: [2, 8, 18, 22, 8, 2], 61: [2, 8, 18, 23, 8, 2],
          62: [2, 8, 18, 24, 8, 2], 63: [2, 8, 18, 25, 8, 2], 64: [2, 8, 18, 25, 9, 2], 65: [2, 8, 18, 27, 8, 2], 66: [2, 8, 18, 28, 8, 2],
          67: [2, 8, 18, 29, 8, 2], 68: [2, 8, 18, 30, 8, 2], 69: [2, 8, 18, 31, 8, 2], 70: [2, 8, 18, 32, 8, 2], 71: [2, 8, 18, 32, 9, 2],
          72: [2, 8, 18, 32, 10, 2], 73: [2, 8, 18, 32, 11, 2], 74: [2, 8, 18, 32, 12, 2], 75: [2, 8, 18, 32, 13, 2], 76: [2, 8, 18, 32, 14, 2],
          77: [2, 8, 18, 32, 15, 2], 78: [2, 8, 18, 32, 17, 1], 79: [2, 8, 18, 32, 18, 1], 80: [2, 8, 18, 32, 18, 2], 81: [2, 8, 18, 32, 18, 3],
          82: [2, 8, 18, 32, 18, 4], 83: [2, 8, 18, 32, 18, 5], 84: [2, 8, 18, 32, 18, 6], 85: [2, 8, 18, 32, 18, 7], 86: [2, 8, 18, 32, 18, 8],
          87: [2, 8, 18, 32, 18, 8, 1], 88: [2, 8, 18, 32, 18, 8, 2], 89: [2, 8, 18, 32, 18, 9, 2], 90: [2, 8, 18, 32, 18, 10, 2],
          91: [2, 8, 18, 32, 20, 9, 2], 92: [2, 8, 18, 32, 21, 9, 2], 93: [2, 8, 18, 32, 22, 9, 2], 94: [2, 8, 18, 32, 24, 8, 2],
          95: [2, 8, 18, 32, 25, 8, 2], 96: [2, 8, 18, 32, 25, 9, 2], 97: [2, 8, 18, 32, 27, 8, 2], 98: [2, 8, 18, 32, 28, 8, 2],
          99: [2, 8, 18, 32, 29, 8, 2], 100: [2, 8, 18, 32, 30, 8, 2], 101: [2, 8, 18, 32, 31, 8, 2], 102: [2, 8, 18, 32, 32, 8, 2],
          103: [2, 8, 18, 32, 32, 9, 2], 104: [2, 8, 18, 32, 32, 10, 2], 105: [2, 8, 18, 32, 32, 11, 2], 106: [2, 8, 18, 32, 32, 12, 2],
          107: [2, 8, 18, 32, 32, 13, 2], 108: [2, 8, 18, 32, 32, 14, 2], 109: [2, 8, 18, 32, 32, 15, 2], 110: [2, 8, 18, 32, 32, 17, 1],
          111: [2, 8, 18, 32, 32, 17, 2], 112: [2, 8, 18, 32, 32, 18, 2], 113: [2, 8, 18, 32, 32, 18, 3], 114: [2, 8, 18, 32, 32, 18, 4],
          115: [2, 8, 18, 32, 32, 18, 5], 116: [2, 8, 18, 32, 32, 18, 6], 117: [2, 8, 18, 32, 32, 18, 7], 118: [2, 8, 18, 32, 32, 18, 8]}
colors = ["#eeeeee", "#e81416", "#ffa500", "#faeb36", "#79c314", "40E0D0", "#487de7", "#4b369d", "#70369d", "#B78C11", "#848482"]
group_names = ["Hydrogen", "Alkali Metals", "Alkaline Earth Metals", "Transition Metals", "Other Metals", "Metalloids", "Nonmetals", "Halogens", "Nobel Gases", "Lanthanides", "Actinides"]