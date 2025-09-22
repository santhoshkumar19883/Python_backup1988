import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_excel("your_data.xlsx")   # or pd.read_csv("your_data.csv")

# 2. User input
years_input = input("Enter Years (comma separated, e.g. 2024,2025): ")

years = [int(y.strip()) for y in years_input.split(",")]

customer = input("Enter Customer: ").strip().lower()

# 3. Weighted Average function
def weighted_avg(group):
    weights = group["Chicks Placed"]
    result = {}
    result["Chicks Placed"] = weights.sum()
    for col in group.columns:
        if col not in ["Customer", "Year", "Month", "Chicks Placed"]:
            result[col] = (group[col] * weights).sum() / weights.sum()
    return pd.Series(result)

# 4. Loop through selected years
for year in years:
    filtered_df = df[(df["Year"] == year) & (df["Customer"].str.lower() == customer)].copy()

    if not filtered_df.empty:
        # Weighted summary month by month
        summary = filtered_df.groupby("Month").apply(weighted_avg).reset_index()
        summary.insert(0, "Customer", customer)
        summary.insert(1, "Year", year)

        # Formatting
        summary["BW"] = summary["BW"].map(lambda x: f"{x:.1f}")
        summary["FCR"] = summary["FCR"].map(lambda x: f"{x:.3f}")
        summary["cFCR"] = summary["cFCR"].map(lambda x: f"{x:.3f}")

        for col in summary.columns:
            if col not in ["Customer", "Year", "Month", "BW", "FCR", "cFCR"]:
                try:
                    summary[col] = summary[col].astype(int)
                except:
                    pass

        # Sort months (calendar order)
        month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        summary["Month"] = pd.Categorical(summary["Month"], categories=month_order, ordered=True)
        summary = summary.sort_values("Month")

        # Show Table for this year
        fig, ax = plt.subplots(figsize=(12, 0.6 * len(summary)))
        ax.axis('off')
        table = ax.table(cellText=summary.values,
                         colLabels=summary.columns,
                         loc='center',
                         cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1.2, 1.2)

        plt.title(f"Performance of {customer.title()} - {year}", fontsize=12, pad=20)
        plt.show()
        # plt.savefig(f"{customer}_{year}_summary.png", bbox_inches="tight")

    else:
        print(f"No data found for {customer.title()} in {year}.")
