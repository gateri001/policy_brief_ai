import pandas as pd

def simulate():
    rows = [
        ("Citizens demand better healthcare access", "health"),
        ("Youth unemployment is rising", "jobs"),
        ("Security concerns in rural areas", "security"),
        ("Education reforms are welcomed", "education")
    ]
    df = pd.DataFrame(rows, columns=["feedback","theme"])
    df.to_csv("data/synthetic_feedback.csv", index=False)
    print("Saved data/synthetic_feedback.csv")

if __name__ == "__main__":
    simulate()
