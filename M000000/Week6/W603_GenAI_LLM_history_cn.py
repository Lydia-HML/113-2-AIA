import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 指定字型檔案路徑
font_path = "fonts/chinese_font.ttf"  # 修改為你的字型路徑

def plot_llm_timeline():
    # 年份 (X 軸)
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

    # 重要事件或模型 (與 years 對應)
    # 可依實際需求增加或調整描述
    events = [
        "Transformer 論文 (Attention Is All You Need)",
        "BERT / GPT-1 等模型誕生",
        "GPT-2 / XLNet / Megatron-LM",
        "GPT-3 (175B 參數), T5 等",
        "大型多語言模型 / Switch Transformer 等",
        "ChatGPT爆紅 / 微調及指令調整 (Instruction Tuning)",
        "Google Bard / Meta LLaMA / Baidu ERNIE Bot 競爭",
        "模型垂直領域深耕 (金融、醫療...)\n檢索增強式生成更成熟",
        "安全性 / 隱私 / 可解釋性成關鍵\n巨量模型與專用模型並進"
    ]

    # 為了簡化，我們在 Y 軸使用相同值，僅在文字上標示事件
    y_values = [1] * len(years)

    plt.figure(figsize=(10, 6))  # 可依需要調整尺寸
    custom_font = fm.FontProperties(fname=font_path, size=12)  # 設定字型大小
    plt.text(0.5, 0.5, "測試中文字",  fontsize=20, ha="center", va="center")
    plt.title("中文測試", fontproperties=custom_font)

    # 繪製散點表示年份
    plt.scatter(years, y_values)

    # 在散點上方加上對應事件文字
    for i, year in enumerate(years):
        plt.text(year, 1.02, "(" + str(year) + ") " + events[i],
                 rotation=45,  # 文字旋轉角度，可視需求調整
                 fontproperties=custom_font,
                 ha='left', va='bottom', fontsize=10)




    # 設定 X 軸範圍讓圖表更美觀
    plt.xlim(min(years) - 0.5, max(years) + 3)
    plt.ylim(0.95, 1.2)

    plt.title("大型語言模型發展脈絡 (2017～2025)")
    plt.xlabel("年份", fontproperties=custom_font, fontsize=10)
    plt.yticks([])  # 隱藏 Y 軸刻度，因為這裡只有時間軸意義
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_llm_timeline()


