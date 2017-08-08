text=input("Enter a text: ")

q_keyboard="qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_keyboard="fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

translate_chart=str.maketrans(f_keyboard,q_keyboard)

print(text.translate(translate_chart))