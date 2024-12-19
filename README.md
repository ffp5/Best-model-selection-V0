# Best Model Selection V0

This repository contains scripts and notebooks for evaluating the performance of different machine learning models based on their predictions. The evaluation process involves loading JSON files from zip archives, combining the data into a DataFrame, and creating a pivot table to compare model performances.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Scripts and Notebooks](#scripts-and-notebooks)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Best-model-selection-V0.git
    cd Best-model-selection-V0
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Scripts

1. **Generate DataFrame**: Run the `gen_df.py` script to load JSON files from zip archives and create a combined DataFrame.
    ```sh
    python gen_df.py
    ```

2. **Evaluate Models**: Use the Jupyter notebook `selector.ipynb` to evaluate model performances and find the top models for a given input question.

### Notebook

1. Launch Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

2. Open and run the `selector.ipynb` notebook to evaluate model performances and find similar questions.

## Project Structure

```
Best-model-selection-V0/
├── eval_results/                # Directory containing zip files with evaluation results
├── venv/                        # Virtual environment directory
├── gen_df.py                    # Script to generate DataFrame from JSON files
├── selector.ipynb               # Jupyter notebook for model evaluation
├── requirements.txt             # List of required packages
└── README.md                    # Project README file
```

## Scripts and Notebooks

### `gen_df.py`

This script loads JSON files from zip archives, combines the data into a single DataFrame, and creates a pivot table to compare model performances.

### `selector.ipynb`

This Jupyter notebook evaluates the performance of different models based on their predictions. It processes JSON files from zip archives, combines the data into a DataFrame, and creates a pivot table to compare model performances. The notebook also computes embeddings for questions and finds the top 20 most similar questions for a given input question.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.