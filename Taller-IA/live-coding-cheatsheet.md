# Live Coding in a Blank Notebook

Ten simple things in Python and five in Markdown. Each one works in Jupyter or Colab with no installation. Type each into its own cell and run it with Shift + Enter.

## Ten Things in Python

### 1. A calculator

```python
2 + 3 * 4
```

### 2. Variables

```python
price = 25
quantity = 4
price * quantity
```

### 3. Text

```python
city = "Madrid"
f"Hola, {city}!"
```

### 4. A list of numbers

```python
temps = [12, 15, 19, 24, 30]
max(temps), min(temps), sum(temps) / len(temps)
```

### 5. A loop

```python
for t in temps:
    print(t, "degrees")
```

### 6. A decision

```python
for t in temps:
    if t > 20:
        print(t, "is warm")
    else:
        print(t, "is cool")
```

### 7. Your own function

```python
def grow(amount, rate, years):
    return amount * (1 + rate) ** years

grow(1000, 0.05, 10)
```

### 8. A random choice (pick a volunteer)

```python
import random
random.choice(["Ana", "Luis", "Marta", "Pablo"])
```

### 9. A table of data

```python
import pandas as pd

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "temp": temps
})
df
```

```python
df.describe()
```

### 10. A plot

```python
import matplotlib.pyplot as plt

plt.plot(df["month"], df["temp"], marker="o")
plt.title("Monthly temperature")
plt.ylabel("Degrees C")
plt.show()
```

## Five Things in Markdown

Change the cell type to Markdown (in Jupyter press M; in Colab click "+ Text"), type, then run the cell to see it rendered.

### 1. Headings

```markdown
# Title
## Section
### Subsection
```

### 2. Bold and italic

```markdown
This is **important** and this is *emphasised*.
```

### 3. Lists

```markdown
- Load the data
- Explore it
- Plot it

1. First step
2. Second step
```

### 4. Links and images

```markdown
[Universidad Europea](https://universidadeuropea.com)

![A chart](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Simple_linear_regression.svg/320px-Simple_linear_regression.svg.png)
```

### 5. Equations

```markdown
Inline: $E = mc^2$

On its own line:

$$ A = P(1 + r)^t $$
```

## Suggested demo order

Python 1 to 4 show that code is just a calculator with memory. Python 7 links to Markdown 5: write the formula in Markdown, then compute it in Python right below. End with Python 9 and 10 to show data becoming a picture in four lines.
