import streamlit as st

st.set_page_config(page_title="Cube Builder", page_icon="🟦", layout="wide")

st.title("🟦 Cube Builder (Streamlit Version)")
st.write("Move around and place cubes!")

# Initialize state
if "player_pos" not in st.session_state:
    st.session_state.player_pos = [0, 0, 0]  # x, y, z
if "cubes" not in st.session_state:
    st.session_state.cubes = []

# Controls
col1, col2, col3 = st.columns(3)
if col1.button("⬅️ Left (A)"):
    st.session_state.player_pos[0] -= 1
if col2.button("⬆️ Forward (W)"):
    st.session_state.player_pos[2] += 1
if col3.button("➡️ Right (D)"):
    st.session_state.player_pos[0] += 1

if st.button("⬇️ Backward (S)"):
    st.session_state.player_pos[2] -= 1

# Place cube
if st.button("🟦 Place Cube (Left Click)"):
    cube_pos = [st.session_state.player_pos[0],
                1,
                st.session_state.player_pos[2] + 2]
    st.session_state.cubes.append(cube_pos)

# Show player position
st.subheader("📍 Player Position")
st.json({"x": st.session_state.player_pos[0],
         "y": st.session_state.player_pos[1],
         "z": st.session_state.player_pos[2]})

# Show placed cubes
st.subheader("🟦 Placed Cubes")
if st.session_state.cubes:
    st.write("Cubes at positions:")
    st.json(st.session_state.cubes)
else:
    st.write("No cubes placed yet.")

# (Optional) 3D visualization with Plotly
import plotly.graph_objects as go

fig = go.Figure()

# Add player
fig.add_trace(go.Scatter3d(
    x=[st.session_state.player_pos[0]],
    y=[st.session_state.player_pos[1]],
    z=[st.session_state.player_pos[2]],
    mode='markers',
    marker=dict(size=8, color='red'),
    name="Player"
))

# Add cubes
if st.session_state.cubes:
    for cube in st.session_state.cubes:
        fig.add_trace(go.Scatter3d(
            x=[cube[0]], y=[cube[1]], z=[cube[2]],
            mode='markers',
            marker=dict(size=6, color='blue'),
            name="Cube"
        ))

fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=10, range=[-10, 10]),
        yaxis=dict(nticks=5, range=[0, 5]),
        zaxis=dict(nticks=10, range=[-10, 10]),
    ),
    margin=dict(r=0, l=0, b=0, t=0)
)

st.plotly_chart(fig, use_container_width=True)
