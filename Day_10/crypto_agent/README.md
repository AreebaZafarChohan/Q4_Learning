# 🤖 CryptoDataAgent

A simple OpenAI Agent powered by Gemini API that fetches **live market prices** of cryptocurrencies using the **Binance API**.

---

## 🚀 Goal

Get the current market rate of any crypto symbol like `BTCUSDT`, `ETHUSDT`, etc.

---

## 📁 Create a project in uv
```bash
uv init crypto_agent
cd crypto_agent
uv venv
.venv\Scripts\activate
```

## ✔ Create virtual environment and activate it
 
```bash
uv venv
.venv\Scripts\activate
```

## 📦 Requirements

Install the required libraries:

```bash
pip install openai-agents requests python-dotenv
```

## 📁 Project Structure

- ├── .git
- ├── .env # Contains GEMINI_API_KEY
- ├── .venv (folder)
- ├── .gitignore
- ├── .python-version
- ├── main.py # Main agent logic
- ├── pyproject.toml
- ├── README.md # Project documentation
- └── uv.lock

---

## 🔐 .env File

Create a `.env` file in your root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🧠 How It Works

- Uses `requests` to fetch live data from [Binance Ticker API](https://api.binance.com/api/v3/ticker/price).
- Defines a tool `get_crypto_price(symbol: str)` with `@function_tool`.
- Creates an agent `CryptoDataAgent` with instructions to use the tool.
- Uses `Runner.run_sync()` to process queries like:

  > “What’s the price of BTCUSDT?”

- Returns real-time market data.

---

## ▶️ Run the Agent

```bash
python crypto_agent.py
```

## 🖥️ Expected Output

```text
Calling Crypto Data Agent

The current price of BTCUSDT is 103694.80000000 USDT.
```

## 🛠️ Tech Stack / Built With

- 🧠 **OpenAI Agents SDK**
- ⚡ **Gemini Flash 2.0**
- 💹 **Binance API**
- 🐍 **Python 3.10+**
- 🚀 **uv** (Fast Python package manager)

---

## 📌 Notes

- Ensure **internet connection** is active.
- Make sure your **Gemini API key** is set in the `.env` file.
- Ensure your **Gemini free-tier quota** is not exceeded.
- Run using a compatible **Python version (>= 3.10)**.

---

## ✨ Future Ideas

- Add support for **multiple coins** in one query (e.g., BTC, ETH, DOGE).
- Build a modern **frontend using Streamlit or Next.js**.
- Log and analyze **historical price data** in a database or CSV.

---

## 📄 License

This project is licensed under the **MIT License**.


---

**Made with ❤️ by Areeba Zafar**
