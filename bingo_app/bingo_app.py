import streamlit as st
import random

st.set_page_config(page_title="Bingo Game", layout="centered")

# Setup session state
if 'numbers' not in st.session_state:
    nums = random.sample(range(1, 26), 25)  # Random 1–25
    st.session_state.numbers = nums
    st.session_state.marked = [False] * 25
    st.session_state.completed_lines = set()

# Function to check completed lines
def check_lines():
    grid = st.session_state.marked
    completed = set()

    for i in range(5):
        if all(grid[i*5 + j] for j in range(5)):
            completed.add(f"row-{i}")
        if all(grid[j*5 + i] for j in range(5)):
            completed.add(f"col-{i}")

    if all(grid[i*6] for i in range(5)):
        completed.add("diag-main")
    if all(grid[(i+1)*4] for i in range(5)):
        completed.add("diag-anti")

    return completed

# Display BINGO header
cols_header = st.columns(5)
for i, letter in enumerate("BINGO"):
    cols_header[i].markdown(f"### {letter}")

# Display 5x5 bingo grid
for row in range(5):
    cols = st.columns(5)
    for col in range(5):
        idx = row * 5 + col
        if st.session_state.marked[idx]:
            cols[col].button("❌", key=f"btn-{idx}", disabled=True)
        else:
            if cols[col].button(str(st.session_state.numbers[idx]), key=f"btn-{idx}"):
                st.session_state.marked[idx] = True
                st.session_state.completed_lines = check_lines()

lines = st.session_state.completed_lines
if len(lines) >= 5:
    st.success("🎉 BINGO! You completed 5 lines!")
elif len(lines) > 0:
    st.info(f"✔️ You have completed {len(lines)} line(s)")

# Reset
if st.button("🔁 Restart Game"):
    nums = random.sample(range(1, 26), 25)
    st.session_state.numbers = nums
    st.session_state.marked = [False] * 25
    st.session_state.completed_lines = set()
