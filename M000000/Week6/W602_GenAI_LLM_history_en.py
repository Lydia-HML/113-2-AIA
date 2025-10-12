import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def plot_llm_timeline():

    # Define the years (X-axis)
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]

    # Define major LLM events corresponding to each year
    # You can modify or add more events as needed
    events = [
        "Transformer Paper (Attention Is All You Need)",
        "BERT / GPT-1 Models Introduced",
        "GPT-2 / XLNet / Megatron-LM Released",
        "GPT-3 (175B Parameters), T5 Model Released",
        "Large Multilingual Models / Switch Transformer",
        "ChatGPT Becomes Popular / Instruction Tuning Advances",
        "Google Bard / Meta LLaMA / Baidu ERNIE Bot Competition",
        "Industry-Specific Models (Finance, Healthcare, etc.)\nAdvancements in Retrieval-Augmented Generation",
        "Security, Privacy, Explainability Become Key Issues\nGrowth of Both Large and Specialized Models",
        "What's Next in 2026?",
        "What's Next in 2027?",
    ]

    # Y-axis values (all set to 1 for a horizontal timeline)
    y_values = [1] * len(years)

    # Create a new figure with specified size
    plt.figure(figsize=(10, 6))  # Adjust size as needed

    # # Load the custom Chinese font for correct text rendering
    # custom_font = fm.FontProperties(fname=font_path, size=12)
    #
    # # Example text to test Chinese font rendering
    # plt.text(0.5, 0.5, "測試中文字", fontsize=20, ha="center", va="center")
    # plt.title("中文測試", fontproperties=custom_font)

    # Plot scatter points to mark the years
    plt.scatter(years, y_values)

    # Add text annotations above each point in the timeline
    for i, year in enumerate(years):
        plt.text(year, 1.02, "(" + str(year) + ") " + events[i],  # Format: (Year) Event
                 rotation=45,  # Rotate text to prevent overlapping
                 ha='left', va='bottom', fontsize=10)

    # Set the X-axis range for better visualization
    plt.xlim(min(years) - 0.5, max(years) + 3)
    plt.ylim(0.95, 1.2)

    # Add title and labels
    plt.title("The development of LLM (2017～2025)")
    plt.xlabel("Year", fontsize=10)

    # Hide Y-axis labels as they are not needed for a timeline
    plt.yticks([])

    # Adjust layout to prevent text from being cut off
    plt.tight_layout()

    # Display the plot
    plt.show()

# Execute the function when the script is run
if __name__ == "__main__":
    plot_llm_timeline()