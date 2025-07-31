import streamlit as st
from copy import deepcopy
from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

# Initialize the game state
if 'board' not in st.session_state:
    st.session_state.board = initial_state()

st.title("Tic-Tac-Toe AI (Minimax)")

board = st.session_state.board
current_player = player(board)

# Show board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = board[i][j]
        label = cell if cell else " "
        if not terminal(board) and (i, j) in actions(board) and cell is None:
            if cols[j].button(label, key=f"{i}-{j}"):
                board = result(board, (i, j))
                st.session_state.board = board
                # AI's turn (O)
                if not terminal(board):
                    ai_move = minimax(board)
                    if ai_move:
                        board = result(board, ai_move)
                        st.session_state.board = board
                st.experimental_rerun()
        else:
            cols[j].markdown(f"### {label}")

# Show result
if terminal(board):
    win = winner(board)
    if win:
        st.success(f"Game Over! Winner: {win}")
    else:
        st.info("Game Over! It's a Tie 🤝")

# Restart
if st.button("Restart Game"):
    st.session_state.board = initial_state()
    st.experimental_rerun()
