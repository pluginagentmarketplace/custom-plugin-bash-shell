# ML Frameworks Guide

## PyTorch vs TensorFlow

| Aspect | PyTorch | TensorFlow |
|--------|---------|------------|
| Dynamic graphs | Yes | TF 2.0+ |
| Debugging | Easier | Harder |
| Production | TorchServe | TF Serving |

## Quick Start

```python
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```
