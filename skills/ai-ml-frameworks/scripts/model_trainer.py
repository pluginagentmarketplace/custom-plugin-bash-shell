#!/usr/bin/env python3
"""Simple model training template."""
import torch
import torch.nn as nn

def train_step(model, data, optimizer):
    model.train()
    optimizer.zero_grad()
    output = model(data)
    loss = nn.CrossEntropyLoss()(output, data.labels)
    loss.backward()
    optimizer.step()
    return loss.item()

if __name__ == "__main__":
    print("Training template loaded")
