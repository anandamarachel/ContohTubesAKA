# Fibonacci Algorithm Comparison (Iterative vs Recursive)

A Streamlit web app to empirically compare the runtime efficiency of iterative and recursive implementations of the Fibonacci algorithm.

## 📁 Project Structure
fibonacci-tubes/
├── fibonacci_app.py       # Main Streamlit application
├── requirements.txt       # Python dependencies
└── fibonacci.py           # CLI Testing

## ⚙️ Dependencies
- Python 3.8+
- streamlit
- matplotlib

Install them with:
pip install -r requirements.txt or
pip install streamlit matplotlib

## ▶️ Run Locally
streamlit run fibonacci_app.py or
python -m streamlit run fibonanci_app.py

Open your browser to: http://localhost:8501

## 📈 App Features
- Input integer n (recommended range: 0 to 35)
- Execute both iterative (O(n)) and naive recursive (O(2ⁿ)) versions
- Display:
  - Computed Fibonacci number F(n)
  - Execution time in microseconds (µs)
- Visualizations:
  - Bar chart: runtime comparison for the current n
  - Line plot: runtime vs n (for n = 5, 10, ..., 30) with logarithmic Y-axis

> ⚠️ Note: The recursive version becomes extremely slow for n > 35. The app enforces n ≤ 35 for stability.

## ☁️ Deploy to Streamlit Cloud
1. Push this code to a public GitHub repository
2. Go to https://streamlit.io/cloud
3. Click "New app"
   - Repository: your-username/fibonacci-tubes
   - Branch: main
   - Main file path: fibonacci_web_app.py
4. Click "Deploy"

Your app will be live at:
https://your-username-fibonacci-tubes.streamlit.app

## 📄 Report Compliance
This project fulfills all requirements from the AKA Tugas Besar (Semester Ganjil 2025/2026):
- ✅ One problem (Fibonacci — used here as a reference example only)
- ✅ One algorithm in two versions: iterative & recursive
- ✅ Web-based application (Streamlit)
- ✅ Empirical runtime analysis across multiple input sizes
- ✅ Theoretical complexity analysis (O(n) vs O(2ⁿ))

> 🚫 Reminder for students: Your group must choose a different, unique problem. Do not reuse Fibonacci.

## 📚 References
- Python time.perf_counter(): https://docs.python.org/3/library/time.html#time.perf_counter
- Streamlit: https://streamlit.io
- Cormen et al., Introduction to Algorithms (3rd ed.)
