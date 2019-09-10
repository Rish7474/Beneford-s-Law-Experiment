#Benford's Law Expirement
import xlrd
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
loc = ("WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES.xlsx")  
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name("ESTIMATES")
count_arr = [0]*9

for c in range(43,305): #Countries' population estimates cover rows 44 to 306 on the excel sheet
    cell_str = str(sheet.cell(c,74))
    first_digit = int(cell_str[7])#7th char = 1st digit since nums from excel are formatted like this -> Number:#####
    #Checks if the 1st digit is from one country only and records the occurence in count_arr
    if str(sheet.cell(c,5)) == "text:'Country'":
        count_arr[first_digit-1]+=1
for c in range(len(count_arr)):
    print("Proportion of",c+1,"as the 1st digit:",count_arr[c]/232)
y_pos = np.arange(len(count_arr))
plt.bar(y_pos, count_arr, align='center', alpha=0.5)
plt.xticks(y_pos, count_arr)
plt.ylabel("Proporation of 1st Digit")
plt.title("Proporation of 1st Digit in Estimated Countries' Populations")
plt.show()
