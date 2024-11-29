import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 标题
st.title("Simple X-Y Plotting App")

# 说明
st.write("This app allows you to input X and Y values to plot a graph!")

# 用户输入 X 和 Y 数据
x_values = st.text_input("Enter X values (comma-separated):", "1, 2, 3, 4, 5")
y_values = st.text_input("Enter Y values (comma-separated):", "1, 4, 9, 16, 25")

# 图表类型选择
plot_type = st.radio("Select plot type:", ["Line Plot", "Scatter Plot"])

# 按钮触发绘图
if st.button("Plot Graph"):
    try:
        # 转换输入为数组
        x = np.array([float(i.strip()) for i in x_values.split(",")])
        y = np.array([float(i.strip()) for i in y_values.split(",")])

        # 检查 x 和 y 长度
        if len(x) != len(y):
            st.error("X and Y must have the same number of values!")
        else:
            # 创建图形
            fig, ax = plt.subplots()
            if plot_type == "Line Plot":
                ax.plot(x, y, marker="o", label="Line Plot")
            elif plot_type == "Scatter Plot":
                ax.scatter(x, y, color="red", label="Scatter Plot")

            ax.set_title("X-Y Plot")
            ax.set_xlabel("X values")
            ax.set_ylabel("Y values")
            ax.legend()

            # 显示图形
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")
