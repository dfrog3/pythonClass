print("Hello, today I will be calculating your required chocolate dosage.")
print("Please enter your weight.")
Oweight = float(input())
# gets original weight value
print("Thank you, Now please enter your height.")
Oheight = float(input())
# gets original hight value
print("Thank you, Now please enter your age.")
Oage = float(input())
# gets original age value
print("Your dosage is now being calculated...")
mBMR = 0
fBMR = 0
fweight = Oweight * 4.35
mweight = Oweight * 6.2
fheight = Oheight * 4.7
mheight = Oheight * 12.7
fage = Oage * 4.7
mage = Oage * 6.76
# does the bits of the formula that were in () and seperates them by sex 

mBMR = (66 + mheight + mweight) - mage
fBMR = (655.1 + fheight + fweight) - fage
#evaluates the BMR formula
MBMR = mBMR // 241
FBMR = fBMR// 241
mBMRr = (mBMR / 241) - MBMR
fBMRr = (fBMR / 241) - FBMR
mBMR = mBMR / 241
fBMR = fBMR / 241
# sets variables for rounding the chocolate bar number up up

if mBMRr != 0:
    finalM = (mBMR - mBMRr) + 1
else:
    finalM = mBMR
if fBMRr != 0:
    finalF = (fBMR - fBMRr) + 1
else:
    finalF = fBMR
    # controls the rounding process and prevents rounding up if the calories are divided evenly by 241
print("Your required chocolate dosage is as follows:\nMales need to eat " + str(finalM) + " or at least " + str(mBMR) + " chocolate bars a day. \nFemales need to eat " + str(finalF) + " or at least " + str(fBMR) + " chocolate bars a day.")
#gives final answer

