---
name: ai-ml-tools
description: AI/ML tools, frameworks, and platforms. Learn TensorFlow, PyTorch, scikit-learn, and build machine learning applications.
---

# AI/ML Tools & Frameworks Skill

Master machine learning libraries and frameworks for building intelligent systems.

## Quick Start

### The ML Development Process

```
1. Problem Definition
    ↓
2. Data Collection & Exploration
    ↓
3. Data Preprocessing
    ↓
4. Feature Engineering
    ↓
5. Model Selection
    ↓
6. Model Training
    ↓
7. Evaluation & Tuning
    ↓
8. Deployment
    ↓
9. Monitoring
```

### Common ML Libraries

#### scikit-learn (Classic ML)
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
```

#### TensorFlow/Keras (Deep Learning)
```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

#### PyTorch (Flexible Deep Learning)
```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
```

## Core ML Concepts

### Data Preparation

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Scale features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode categorical variables
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X_categorical)
```

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 80-20 split
    random_state=42     # Reproducibility
)
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)  # 5-fold cross-validation
print(f"Mean score: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### Feature Engineering

```python
# Create new features
df['age_squared'] = df['age'] ** 2
df['salary_per_age'] = df['salary'] / df['age']

# Feature selection
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

## Model Types & When to Use

### Supervised Learning

**Regression** (predict continuous values)
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```
Use for: house prices, stock prices, temperature

**Classification** (predict categories)
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
```
Use for: email spam, disease diagnosis, sentiment

### Unsupervised Learning

**Clustering** (group similar items)
```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
```
Use for: customer segmentation, image compression

**Dimensionality Reduction** (reduce features)
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
```
Use for: visualization, removing redundancy

### Deep Learning Models

**CNN** (Convolutional Neural Networks)
- Image classification, object detection
- Built-in spatial feature extraction

**RNN/LSTM** (Recurrent Neural Networks)
- Time series, text sequences
- Remembers previous data

**Transformers**
- NLP, sequence-to-sequence
- Attention mechanisms

**Graph Neural Networks**
- Graph data, recommendations
- Node relationships

## Popular Frameworks

### TensorFlow/Keras
```
Pros:
- Production-ready
- Scalable (distributed training)
- Large ecosystem
- TensorFlow Lite for mobile

Cons:
- Steeper learning curve
- More verbose code
```

### PyTorch
```
Pros:
- Pythonic, intuitive
- Excellent documentation
- Research-friendly
- Dynamic computation graphs

Cons:
- Smaller ecosystem (improving)
- Less mobile support
```

### scikit-learn
```
Pros:
- Simple, consistent API
- Comprehensive algorithms
- Good for classic ML
- Fast for small datasets

Cons:
- Not for deep learning
- Limited to single machine
```

## Evaluation Metrics

### Classification

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
```

### Regression

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)  # 1.0 is perfect
```

## Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
```

## Working with LLMs

### OpenAI API
```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are helpful"},
        {"role": "user", "content": "Explain machine learning"}
    ]
)

print(response['choices'][0]['message']['content'])
```

### LangChain
```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a paragraph about {topic}"
)
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(topic="machine learning")
```

## Model Deployment

### Serving Models
```python
# Flask
from flask import Flask, request
from sklearn.externals import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return {'prediction': prediction[0].tolist()}
```

### Model Serving Platforms
- **TensorFlow Serving** - Production inference
- **Seldon** - Kubernetes native
- **KServe** - On Kubernetes
- **BentoML** - Model packaging
- **MLflow** - Model registry and serving

## MLOps Tools

### Experiment Tracking
```python
import mlflow

mlflow.start_run()
mlflow.log_param("n_estimators", 100)
mlflow.log_metric("accuracy", 0.95)
mlflow.log_model(model, "model")
mlflow.end_run()
```

### Data Versioning
```bash
# DVC
dvc add data/
dvc push
git add data.dvc
```

### Pipeline Orchestration
- **Airflow** - Workflow DAGs
- **Kubeflow** - Kubernetes pipelines
- **Prefect** - Modern orchestration

## Learning Path

### Phase 1: Fundamentals (2-4 weeks)
- Python for data science
- NumPy, Pandas basics
- Data visualization (Matplotlib, Seaborn)
- scikit-learn fundamentals
- Simple projects

### Phase 2: Intermediate (4-8 weeks)
- Deeper scikit-learn
- Feature engineering
- Model evaluation
- Cross-validation
- Real datasets

### Phase 3: Deep Learning (4-8 weeks)
- Neural network basics
- TensorFlow/PyTorch
- CNNs, RNNs
- Transfer learning
- Computer vision or NLP

### Phase 4: Advanced (ongoing)
- Advanced architectures
- Distributed training
- MLOps and production
- Specialized domains

## Common Challenges & Solutions

### Overfitting
- Use regularization (L1/L2)
- Increase training data
- Reduce model complexity
- Use early stopping
- Increase dropout

### Class Imbalance
- Use weighted loss
- Over/under-sampling
- SMOTE (Synthetic Minority)
- Adjust decision threshold
- Different metrics (F1, AUC-ROC)

### Data Quality
- Handle missing values
- Detect outliers
- Remove duplicates
- Normalize/scale features
- Feature engineering

## Resources

- **Courses**: Fast.ai, Coursera ML Specialization
- **Documentation**: TensorFlow.org, PyTorch.org
- **Practice**: Kaggle competitions
- **Books**: "Hands-On ML" by Aurélien Géron
- **Communities**: Reddit r/MachineLearning, Discord servers

## Next Steps

After mastering ML tools:
- Learn **advanced architectures** (Vision Transformers, BERT)
- Study **MLOps at scale**
- Explore **LLM fine-tuning**
- Master **reinforcement learning**
- Build **production systems**
