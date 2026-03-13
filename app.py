import streamlit as st
import time

st.set_page_config(page_title="Tower of Hanoi Visualizer", layout="centered")

st.title("🎮 Tower of Hanoi Visualizer")

# Select number of disks
n = st.slider("Select number of disks", 3, 6, 3)

# Speed control
speed = st.slider("Animation Speed (seconds)", 0.5, 5.0, 2.0)

# Function to generate moves
def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
    else:
        hanoi(n-1, source, auxiliary, target, moves)
        moves.append((source, target))
        hanoi(n-1, auxiliary, target, source, moves)

# Function to draw towers
def draw_towers(towers):
    html = """
    <style>
    .container{
        display:flex;
        justify-content:space-around;
        align-items:flex-end;
        height:350px;
        background:#0e1117;
        padding:20px;
        border-radius:10px;
    }

    .tower{
        width:150px;
        height:300px;
        position:relative;
        display:flex;
        flex-direction:column-reverse;
        align-items:center;
    }

    .rod{
        position:absolute;
        bottom:0;
        width:6px;
        height:260px;
        background:white;
        z-index:1;
    }

    .disk{
        height:25px;
        margin:4px;
        border-radius:6px;
        z-index:2;
    }

    .label{
        color:white;
        margin-top:5px;
        text-align:center;
    }
    </style>
    """

    html += '<div class="container">'

    colors = ["#ff595e","#ffca3a","#8ac926","#1982c4","#6a4c93","#ff924c"]
    labels = ["A","B","C"]

    for i, tower in enumerate(towers):
        html += '<div class="tower">'
        html += '<div class="rod"></div>'

        for disk in tower:
            width = 40 + disk*20
            color = colors[disk % len(colors)]
            html += f'<div class="disk" style="width:{width}px;background:{color}"></div>'

        html += f'<div class="label">Tower {labels[i]}</div>'
        html += '</div>'

    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)

# Solve button
if st.button("▶ Solve Tower of Hanoi"):

    moves = []
    hanoi(n,"A","C","B",moves)

    towers = {
        "A": list(range(n,0,-1)),
        "B": [],
        "C": []
    }

    placeholder = st.empty()

    for i,(src,dst) in enumerate(moves):

        disk = towers[src].pop()
        towers[dst].append(disk)

        with placeholder.container():
            st.subheader(f"Step {i+1}: Move disk from {src} → {dst}")
            draw_towers([towers["A"], towers["B"], towers["C"]])

        time.sleep(speed)

    st.success("✅ Puzzle Solved!")