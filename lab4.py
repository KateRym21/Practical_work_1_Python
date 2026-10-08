```python
import math


def calculate_circle_area(radius: float) -> float:
    return math.pi * (radius ** 2)
```

```python
import random


def generate_random_numbers(count: int = 5) -> list[int]:
    return [random.randint(1, 100) for _ in range(count)]
```

```python
from datetime import datetime


def get_current_formatted_time() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
```

```python
import json


def parse_and_serialize_json() -> str:
    data = {
        "course": "Python",
        "lab_number": 4,
        "status": "completed",
    }
    return json.dumps(data, indent=4)
```

```python
import os


def get_working_directory_info() -> str:
    return os.getcwd()
```

```python
import requests


def check_site_status(
    url: str = "https://peps.python.org/pep-0008/",
) -> int:
    response = requests.get(url, timeout=5)
    return response.status_code
```

```python
import numpy as np


def compute_array_mean() -> float:
    array = np.array([10, 20, 30, 40, 50])
    return float(np.mean(array))
```


```python
import pandas as pd


def create_simple_dataframe() -> str:
    data = {
        "Name": ["Alice", "Bob"],
        "Age": [22, 25],
    }
    df = pd.DataFrame(data)
    return str(df)
```


```python
import matplotlib.pyplot as plt


def generate_simple_plot() -> str:
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title("Sample Plot")

    filename = "plot.png"
    plt.savefig(filename)
    plt.close()

    return filename
```



```python
from PIL import Image


def create_blank_image() -> str:
    image = Image.new("RGB", (100, 100), color="blue")

    filename = "blue_square.png"
    image.save(filename)

    return filename
```


```python
from bs4 import BeautifulSoup


def extract_title_from_html(html_doc: str) -> str:
    soup = BeautifulSoup(html_doc, "html.parser")
    title_tag = soup.title

    return title_tag.string if title_tag else "No title found"
```

```python
from scipy import constants


def get_speed_of_light() -> float:
    return constants.c
```


```python
import sympy as sp


def solve_quadratic_equation() -> list:
    x = sp.Symbol("x")
    equation = sp.Eq(x**2 - 4, 0)

    return sp.solve(equation, x)
```


```python
from art import text2art


def render_ascii_art(text: str = "LAB 4") -> str:
    return text2art(text)
```


```python
from colorama import Fore, Style


def format_colored_text(text: str) -> str:
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
```


```python
from builtins.use_datetime import get_current_formatted_time
from builtins.use_json import parse_and_serialize_json
from builtins.use_math import calculate_circle_area
from builtins.use_os import get_working_directory_info
from builtins.use_random import generate_random_numbers

from external.use_art import render_ascii_art
from external.use_bs4 import extract_title_from_html
from external.use_colorama import format_colored_text
from external.use_matplotlib import generate_simple_plot
from external.use_numpy import compute_array_mean
from external.use_pandas import create_simple_dataframe
from external.use_pillow import create_blank_image
from external.use_requests import check_site_status
from external.use_scipy import get_speed_of_light
from external.use_sympy import solve_quadratic_equation


def main() -> None:
    """Main function demonstrating all imported libraries."""
    print("=== ВБУДОВАНІ БІБЛІОТЕКИ ===")

    print(f"Math (Circle Area r=5): {calculate_circle_area(5)}")
    print(f"Random Numbers: {generate_random_numbers()}")
    print(f"Current Time: {get_current_formatted_time()}")
    print(f"JSON Output:\n{parse_and_serialize_json()}")
    print(f"Working Dir: {get_working_directory_info()}\n")

    print("=== СТОРОННІ БІБЛІОТЕКИ ===")

    print(f"Requests (PEP 8 Status Code): {check_site_status()}")
    print(f"NumPy (Mean): {compute_array_mean()}")
    print(f"Pandas DataFrame:\n{create_simple_dataframe()}")
    print(f"Matplotlib Plot Saved: {generate_simple_plot()}")
    print(f"Pillow Image Saved: {create_blank_image()}")

    html_sample = (
        "<html><head><title>Test Page</title></head></html>"
    )
    print(
        f"BeautifulSoup Title: "
        f"{extract_title_from_html(html_sample)}"
    )

    print(f"SciPy Speed of Light: {get_speed_of_light()} m/s")
    print(
        "SymPy Roots of x^2 - 4 = 0: "
        f"{solve_quadratic_equation()}"
    )

    print("\nASCII Art Output:")
    print(render_ascii_art("PYTHON"))

    print(format_colored_text(
        "Усі 15 функцій успішно виконано!"
    ))


if __name__ == "__main__":
    main()
```

Lab4/
│
├── builtins/
│   ├── use_math.py
│   ├── use_random.py
│   ├── use_datetime.py
│   ├── use_json.py
│   └── use_os.py
│
├── external/
│   ├── use_requests.py
│   ├── use_numpy.py
│   ├── use_pandas.py
│   ├── use_matplotlib.py
│   ├── use_pillow.py
│   ├── use_bs4.py
│   ├── use_scipy.py
│   ├── use_sympy.py
│   ├── use_art.py
│   └── use_colorama.py
│
├── main.py
└── requirements.txt
