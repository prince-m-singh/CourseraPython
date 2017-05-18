text = "X-DSPAM-Confidence:    0.8475";
num=text.find(":")
print num
data=text[num+1:].strip()
print type(data)
print float(data)