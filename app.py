import streamlit as st
import time

st.set_page_config(page_title="Tower of Hanoi Visualizer", layout="centered")

st.header("🎮 Tower of Hanoi Algorithm Visualizer")
st.divider()

# About Algorithm (directly visible)
st.subheader("About the Algorithm")

st.write("""
The Tower of Hanoi is a classic recursive puzzle.

Rules:
• Only one disk can be moved at a time  
• A larger disk cannot be placed on a smaller disk  
• Move all disks from Tower A to Tower C using Tower B

The optimal number of moves required is:

Moves = 2ⁿ - 1
""")

st.divider()

# Disk input
n = st.text_input("Enter number of disks (3 - 6)", "3")

try:
    n = int(n)
except:
    st.warning("Please enter a valid number")
    st.stop()

if n < 3 or n > 6:
    st.warning("Enter a number between 3 and 6")
    st.stop()

# Fixed animation speed
speed = 2


# Hanoi logic
def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
    else:
        hanoi(n-1, source, auxiliary, target, moves)
        moves.append((source, target))
        hanoi(n-1, auxiliary, target, source, moves)


# Draw towers
def draw_towers(towers):

    html = """
    <style>

    .container{
        display:flex;
        justify-content:space-around;
        align-items:flex-end;
        height:350px;
        background:#111827;
        padding:20px;
        border-radius:12px;
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

    .base{
        position:absolute;
        bottom:-10px;
        width:120px;
        height:10px;
        background:white;
        border-radius:4px;
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
        font-weight:bold;
    }

    </style>
    """

    html += '<div class="container">'

    colors = ["#ff595e","#ffca3a","#8ac926","#1982c4","#6a4c93","#ff924c"]
    labels = ["A","B","C"]

    for i, tower in enumerate(towers):

        html += '<div class="tower">'
        html += '<div class="rod"></div>'
        html += '<div class="base"></div>'

        for disk in tower:
            width = 40 + disk*20
            color = colors[disk % len(colors)]

            html += f'<div class="disk" style="width:{width}px;background:{color}"></div>'

        html += f'<div class="label">Tower {labels[i]}</div>'
        html += '</div>'

    html += '</div>'

    st.markdown(html, unsafe_allow_html=True)


# Start simulation
if st.button("▶ Start Simulation"):

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

            st.info(f"Move {i+1} / {len(moves)} : Move disk {disk} from {src} → {dst}")

            draw_towers([
                towers["A"],
                towers["B"],
                towers["C"]
            ])

        time.sleep(speed)

    st.success("✅ Puzzle Solved!")

    # Reset button at bottom
    if st.button("🔄 Reset Puzzle"):
        st.rerun()

st.divider()
st.caption("Algorithm Visualizer Project | Built with Python + Streamlit")
