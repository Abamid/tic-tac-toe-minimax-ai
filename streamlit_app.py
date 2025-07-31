import streamlit as st
from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = initial_state()
if 'last_move' not in st.session_state:
    st.session_state.last_move = None

st.title("🤖 Tic-Tac-Toe AI (Minimax)")

board = st.session_state.board
game_over = terminal(board)

# Show the board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = board[i][j]
        label = cell if cell else " "
        key = f"{i}-{j}"

        if not game_over and cell is None:
            if cols[j].button(label, key=key):
                # Human move
                st.session_state.board = result(board, (i, j))
                board = st.session_state.board

                # AI move
                if not terminal(board):
                    ai_move = minimax(board)
                    if ai_move:
                        st.session_state.board = result(board, ai_move)
        else:
            cols[j].markdown(f"### {label}")

# Show game status
if terminal(st.session_state.board):
    win = winner(st.session_state.board)
    if win:
        st.success(f"🏆 Game Over! Winner: {win}")
    else:
        st.info("🤝 Game Over! It's a tie!")

# Restart button
if st.button("🔁 Restart Game"):
    st.session_state.board = initial_state()
