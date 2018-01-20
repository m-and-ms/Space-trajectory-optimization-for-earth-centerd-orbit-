import numpy as np
def get_from_GUI(free,BCS):
    subset_of_free=[1000000, 10000000, 100000000]
    fvv = [a for a in free if a not in subset_of_free]
    num=len(fvv)
    num1=len(free)
    fvn0=np.zeros(num1)
    for l in range(num1):
        if free[l]== 1000000:
            fvn0[l]=l
        else:
            fvn0[l]=0
    dummy=[0, 1000]
    fvn=[a for a in fvn0 if a not in dummy]
    subset_of_Bcs=[1000000, 10000000, 100000000]
    BCsv = [a for a in BCS if a not in subset_of_Bcs]
    num2=len(BCS)
    BCsn0 = np.zeros(num2)
    for l in range(num2):
        if BCS[l]== 1000000:
            BCsn0[l]=l
        else:
            BCsn0[l]=0
    BCSn = [a for a in BCsn0 if a not in dummy]
    return fvn, fvv, BCSn, BCsv






