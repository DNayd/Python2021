class Sequence:

  def __init__(self, name, seq):
    self.name = name
    self.seq = seq
    def name ( self ) :
      return self.name
    def seq ( self ) :
      return self.seq
    def length (self) :
      length=len(seq)
      return length

class DNA(Sequence):
  name='DNA'
  alphabet=['A','C','G','T']

  def __init__(self,seq,):
    super().__init__(Sequence,seq)

  def statistic(self):
    for i in range(0,4):
      stat = self.seq.count(self.alphabet[i])
      print(alphabet[i],' - ',stat)

  def Mol(self):
    m = 347 * self.seq.count(self.alphabet[0]) +\
    320.2 * self.seq.count(self.alphabet[1]) +\
    363.2 * self.seq.count(self.alphabet[2]) +\
    323.2 * self.seq.count(self.alphabet[3])
    print('Молекулярная масса - ',round(m,2))

  def complementary(self):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_seq = ''
    for i in self.seq:
      comp_seq += comp[i]
    return comp_seq
    print('Комплементарная последовательность - ', comp_seq)
    
  def Transcription(self):
    tran = []
    for i in range(0, len(self.seq)):
      if self.seq[i] == 'A':
        tran.append('U')
      elif self.seq[i] == 'T':
        tran.append('A')
      elif self.seq[i] == 'G':
        tran.append('C')
      elif self.seq[i] == 'C':
        tran.append('G')
      print('Транскрипция - ', tran)


class RNA(Sequence):
  name = 'RNA'
  alphabet = ['A', 'C', 'G', 'U']
  def __init__(self,seq,):
    super().__init__(Sequence,seq)
  def statistic(self):
    for i in range(0,4):
      stat = self.seq.count(alphabet[i])
    print(alphabet[i],' - ',stat)

  def Mol(self):
    m = 347 * self.seq.count(self.alphabet[0]) + 324.2 * self.seq.count(self.alphabet[1]) + 363.2 * self.seq.count(self.alphabet[2]) + 323.2 * self.seq.count(self.alphabet[3])
    print('Молекулярная масса - ', round(m,2))

  def Translation(self):
    d = {'UUU': 'F', 'UUC': 'F','UUA':'L','UUG':'L','CUU':'L',
             'CUC': 'L','CUA':'L',  'CUG':'L', 'AUU':'I','AUC':'I',
             'AUA': 'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
             'UCU': 'S','UCA': 'S','UCC': 'S','UCG': 'S','CCU': 'P','CCC': 'P',
             'CCA': 'P','CCG': 'P','ACU': 'T','ACC': 'T','ACA': 'T','ACG': 'T',
             'GCU': 'A','GCC': 'A','GCA': 'A','GCG': 'A', 'UAU': 'Y','UAC': 'Y',
             'CAU': 'H','CAC': 'H','CAA': 'Q','CAG': 'Q','AAU': 'N', 'AAC': 'N',
             'AAA': 'K','AAG': 'K','GAU': 'D','GAC': 'D','GAA': 'E','GAG': 'E',
             'UGU': 'C','UGC': 'C','UGG': 'W','CGU': 'R','CGC': 'R','CGA': 'R',
             'CGG': 'R','AGU': 'S','AGC': 'S','AGA': 'R','AGG': 'R','GGU': 'G',
             'GGC': 'G','GGA': 'G','GGG': 'G','UAA': 'STOP','UAG': 'STOP',
             'UGA': 'STOP'}
    protein = []
    start = 0
    for i in range(len(self.seq)):
      if (self.seq[i:i + 3] == "AUG"):
      start = i
      for j in range(start, len(self.seq) - 2, 3):
        amin = d[self.seq[j:j + 3]]
        if (cods == "STOP"):
          break
        else:
          protein.append(amin)
    print('Белковая последовательность  - ', protein)

class Protein(Sequence):
  name = 'Protein'
  alphabet = ['A', 'R', 'N', 'D', 'V', 'H', 'G', 'Q', 'E', 'I', 'L',
  'K', 'M', 'P', 'S', 'Y', 'T', 'W', 'F', 'C']

  def __init__(self,seq,):
    super().__init__(Sequence,seq)

  def statistic(self):
    for i in range(0,20):
      stat = self.seq.count(alphabet[i])
      print(alphabet[i],' - ',stat)

  def Mol(self):
    m = 75 * self.seq.count(self.alphabet[0]) + 89 * self.seq.count(self.alphabet[1]) +\
    117.2 * self.seq.count(self.alphabet[2]) + 131.2 * self.seq.count(self.alphabet[3]) +\
    131.2 * self.seq.count(self.alphabet[4]) + 149.2 * self.seq.count(self.alphabet[5]) +\
    115.1 * self.seq.count(self.alphabet[6]) + 165.2 * self.seq.count(self.alphabet[7]) +\
    204.2 * self.seq.count(self.alphabet[8]) + 105.9 * self.seq.count(self.alphabet[9]) +\
    119 * self.seq.count(self.alphabet[10]) + 132 * self.seq.count(self.alphabet[11]) +\
    146 * self.seq.count(self.alphabet[12]) + 181.2 * self.seq.count(self.alphabet[13]) +\
    121.2 * self.seq.count(self.alphabet[14]) + 146.2 * self.seq.count(self.alphabet[15]) +\
    174.2 * self.seq.count(self.alphabet[16]) + 155.2 * self.seq.count(self.alphabet[17]) +\
    131 * self.seq.count(self.alphabet[18]) + 147 * self.seq.count(self.alphabet[19])
    print('Молекулярная масса - ', round(m,2))
