#!/usr/bin/env python

import numpy as np
theta=1
epoch=3

class perceptron(object) :
    def __init__(self, no_inputs, learning_rate=0.2) :
        self.learning_rate=learning_rate
        self.weights=np.zeros(no_inputs+1)
    
    def predict(self, inputs) :
        return (np.dot(inputs, self.weights[1:])+self.weights[0])

    def train(self, training_inputs, t, weights) :
        for inputs, label in zip(training_inputs, t) :
            net_in=self.predict(inputs)
            if net_in>theta :
                y_out=1
            elif net_in < -theta:
                y_out = -1
            else:
                y_out = 0
            if y_out!=label :
                self.weights[1:]+=self.learning_rate*label*inputs
                self.weights[0]+=self.learning_rate*label
            print(inputs, net_in, label, y_out, self.weights)
    
training_inputs=np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
t=np.array([1,1,1,-1])
perceptron=perceptron(2)
for i in range(epoch):
    print("Epoch",i)
    print("X1 X2","Net"," T"," Y", "B Weights")
    weights = perceptron.weights
    print("Initial Weights",weights)
    perceptron.train(training_inputs, t,weights)