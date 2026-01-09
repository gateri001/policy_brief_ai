import pandas as pd

def generate_brief():
    df = pd.read_csv("data/synthetic_feedback.csv")
    summary = []
    for _, row in df.iterrows():
        summary.append(f"- Theme: {row['theme'].capitalize()} | Citizen voice: {row['feedback']}")
    brief = "Policy Brief:\n" + "\n".join(summary)
    with open("apps/rl/artifacts/brief.txt","w") as f:
        f.write(brief)
    print(brief)

if __name__ == "__main__":
    generate_brief()
