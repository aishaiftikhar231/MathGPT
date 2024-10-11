import streamlit as st
from utils.plotting import plot_function
from utils.solver import solve_math_expression
from utils.file_handler import handle_file_upload
from utils.llm import generate_response
from math_symbols import MATH_SYMBOLS
from streamlit_drawable_canvas import st_canvas
# app.py
from utils.file_handler import read_sample_input
import streamlit as st




def main():
    st.title("Math Solver App")

    mode = st.sidebar.selectbox("Choose Mode", ["Calculator", "Whiteboard", "Document Upload", "Math Symbols"])

    if mode == "Calculator":
        expression = st.text_input("Enter a math expression:")
        if st.button("Solve"):
            result = solve_math_expression(expression)
            st.write(f"Result: {result}")
            plot_graph = st.checkbox("Plot the function")
            if plot_graph:
                fig = plot_function(expression)
                if fig:
                    st.pyplot(fig)

    elif mode == "Whiteboard":
        st.write("Draw your math equation here:")
        
        # Create a canvas for drawing
        canvas_result = st_canvas(
            stroke_width=3,
            stroke_color="black",
            background_color="white",
            width=700,
            height=300,
            drawing_mode="freedraw",
            key="canvas",
        )

        if st.button("Solve Drawn Equation"):
            # Here we would need to implement a way to recognize drawn content
            # For demonstration, we will just display the drawn content as a placeholder
            st.image(canvas_result.image_data)
            st.write("This functionality is not yet implemented.")  # Replace with actual processing logic

    elif mode == "Document Upload":
        uploaded_file = st.file_uploader("Upload a .txt, .pdf, or .docx file", type=["txt", "pdf", "docx"])
        if uploaded_file is not None:
            content = handle_file_upload(uploaded_file)
            st.text_area("File Content", content, height=300)

    elif mode == "Math Symbols":
        st.write("Available Math Symbols:")
        for category, symbols in MATH_SYMBOLS.items():
            st.subheader(category)
            st.write(", ".join(symbols))
# Use the function to read the sample input
sample_input_content = read_sample_input()

# Display the content in your Streamlit app
st.title("Math Problem Solver")
st.subheader("Sample Input from File:")
st.text(sample_input_content)
if __name__ == "__main__":
    main()
