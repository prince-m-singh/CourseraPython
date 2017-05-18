str = 'X-DSPAM-Confidence: 0.8475'

atpos=str.find(': ')
print atpos
sppos=str.find('5',atpos)
print sppos
data=str[atpos+2:]
print float(data)
