import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set application title
st.title("Data Points Visualization Tool")

# Allow users to input x and y data points
x_input = st.text_input("Enter x data points (comma-separated)", "1, 2, 3, 4, 5")
y_input = st.text_input("Enter y data points (comma-separated)", "2, 4, 6, 8, 10")

try:
    # Convert input strings to numeric lists
    x_data = [float(i) for i in x_input.split(',')]
    y_data = [float(i) for i in y_input.split(',')]

    # Check if the lengths of x and y match
    if len(x_data) != len(y_data):
        st.error("The number of x and y data points must match!")
    else:
        # Convert data to a Pandas DataFrame for further processing
        data = pd.DataFrame({"x": x_data, "y": y_data})

        # Display the data table
        st.write("Entered Data Points:")
        st.dataframe(data)

        # Create a visualization plot
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, marker='o', linestyle='-', color='b', label='Connected Data Points')
        ax.set_title("Data Points Visualization")
        ax.set_xlabel("x values")
        ax.set_ylabel("y values")
        ax.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

except ValueError:
    st.error("Please ensure the x and y data points are valid numbers separated by commas!")
