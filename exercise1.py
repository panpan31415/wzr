# # exercise1:
#  print 9*9 table
#  ## create a function to print nine-nine-table
#  the results should look like this:
#  ```
#     1*1=1
#     2*1=2 2*2=4
#     3*1=3 3*2=6 3*3=9
#     4*1=4 4*2=8 4*3=12 4*4=16
#     5*1=5 5*2=10 5*3=15 5*4=20 5*5=25
#     6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36
#     7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49
#     8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64
#     9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81
#  ```
#  hint:
#  - use nested while loop

def nine_nine_table():
    # write your code here
    for i in range(9):  # each line
        l = ""  # string for each line
        for j in range(i+1):
            l += (str(i+1)+'*'+str(j+1)+'='+str(i*j+i+j+1)+' ')
        print(l)


nine_nine_table()
