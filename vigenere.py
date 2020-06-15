alphabets = "abcdefghijklmnopqrstuvwxyz"
def encrypt(p, k):
    c = ""
    kpos = [] # return the index of characters ex: if k='d' then kpos= 3
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i] #find the number or index of the character and perform the shift with the key

      if pos > 25:
          pos = pos-26               # check you exceed the limit
      c += alphabets[pos].capitalize()
      i +=1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      p += alphabets[pos].lower()
      i +=1
    return p



p = "сryptography"

k = "key"
k = k.strip()  # remove the white spaces from both sides
c = encrypt(p, k)
print("The cipher text is: ", c)
p = decrypt(c, k)
print("The plain text is: ", p)
