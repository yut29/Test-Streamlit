import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 设置应用标题
st.title("数据点可视化工具")

# 中文解释：让用户输入 x 和 y 数据点
# 创建两个文本输入框，分别用于输入 x 和 y 数据
x_input = st.text_input("输入 x 数据点（用逗号分隔）", "1, 2, 3, 4, 5")
y_input = st.text_input("输入 y 数据点（用逗号分隔）", "2, 4, 6, 8, 10")

try:
    # 将输入的字符串转换为数值列表
    x_data = [float(i) for i in x_input.split(',')]
    y_data = [float(i) for i in y_input.split(',')]

    # 检查数据长度是否匹配
    if len(x_data) != len(y_data):
        st.error("x 和 y 的数据点数量必须相同！")
    else:
        # 数据转换为 Pandas DataFrame，方便进一步处理
        data = pd.DataFrame({"x": x_data, "y": y_data})

        # 显示数据表格
        st.write("输入的数据点：")
        st.dataframe(data)

        # 创建可视化图表
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, marker='o', linestyle='-', color='b', label='数据点连接')
        ax.set_title("数据点可视化")
        ax.set_xlabel("x 值")
        ax.set_ylabel("y 值")
        ax.legend()

        # 在 Streamlit 中显示图表
        st.pyplot(fig)

except ValueError:
    st.error("请确保输入的 x 和 y 数据点是用逗号分隔的有效数字！")
