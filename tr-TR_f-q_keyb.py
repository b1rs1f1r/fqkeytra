metin=input("Bir metin girin: ")

q_klavye="qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye="fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

çeviri_tablosu=str.maketrans(f_klavye,q_klavye)

print(metin.translate(çeviri_tablosu))