#!/usr/bin/env python

class mpmodel :
    threshold=0
    w1=0
    w2=0
    w1_val=[-1,1]
    w2_val=[-1,1]
    threshold_val=[-2,-1,0,1,2]

    def __init__(self, input_mat) :
        self.input_mat=input_mat
    
    def neuron_activate(self, x1, x2) :
        output=self.w1*x1+self.w2*x2
        if output>=self.threshold :
            return 1
        else :
            return 0
    
    def compare_target(self, x1, x2, target) :
        if self.neuron_activate(x1, x2)==target :
            return True
        else :
            return False

    def check_combination(self) :
        valid=True
        for (x1,x2,y) in self.input_mat :
            if not self.compare_target(x1,x2,y) :
                valid=False
        return valid

    def iterate(self) :
        for w1 in self.w1_val :
            self.w1=w1
            for w2 in self.w2_val :
                self.w2=w2
                for threshold in self.threshold_val :
                    self.threshold=threshold
                    if self.check_combination() :
                        return True
        return False

AND_Mat=[[-1,-1,0],[-1,1,0],[1,-1,0],[1,1,1]]
OR_Mat=[[-1,-1,0],[-1,1,1],[1,-1,1],[1,1,1]]
NAND_Mat=[[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,0]]
XOR_Mat=[[-1,-1,0],[-1,1,1],[1,-1,1],[1,1,0]]

def neuron_cal(mp) :
    if mp.iterate() :
        print("Weights are : ",mp.w1," ",mp.w2)
        print("Threshold is ",mp.threshold)
    else :
        print("Not linearly seperable.")

print("++ AND Gate ++")
mp_AND = mpmodel(AND_Mat)
neuron_cal(mp_AND)

print("++ OR Gate ++")
mp_OR = mpmodel(OR_Mat)
neuron_cal(mp_OR)

print("++ NAND Gate ++")
mp_NAND = mpmodel(NAND_Mat)
neuron_cal(mp_NAND)

print("++ XOR Gate ++")
mp_XOR = mpmodel(XOR_Mat)
neuron_cal(mp_XOR)