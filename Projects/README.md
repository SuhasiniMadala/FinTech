# 🏀 NBA Quant: Player Volatility & Risk Engine

A "teeny-tiny" quantitative tool that treats NBA player performance as a financial time-series. This project applies hedge fund risk-distribution models to live basketball data to find a statistical "edge."

## 🧪 The Quant Logic
In finance, we look for **"Alpha"** (an edge). This engine moves beyond basic PPG averages to analyze:

* **FCS (Frequency Consistency Score):** Derived from the **Coefficient of Variation** ($CV = \sigma / \mu$). It scores how "reliable" a player is. A high FCS indicates a "Blue Chip" asset; a low FCS indicates a high-volatility "Growth" asset.
* **Threshold Probability:** Uses historical distributions to calculate the exact statistical likelihood of a player hitting a specific **Over/Under** line.
* **Contextual Alpha (Home/Away Splits):** Analyzes the variance in performance based on environment, identifying "Road Warriors" vs. "Home Court Heroes."



## 🚀 Tech Stack
* **Data:** `nba_api` (Live JSON fetching from NBA.com)
* **Analysis:** `pandas`, `numpy`
* **Visualization:** `seaborn`, `matplotlib` (Kernel Density Estimation plots)

## 📈 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
