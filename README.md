# Monte Carlo Stock Price Simulation

## Local
```bash
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python montecarlo.py
```

## Docker (headless)
```bash
docker build -t montecarlo-sim .
docker run --rm -e HEADLESS=1 -v "${PWD}:/app" montecarlo-sim
```
