import streamlit as st
from copy import deepcopy
from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

# Initialize the game state
if 'board' not in st.session_state:
    st.session_state.board = initial_state()

st.title("🤖 Tic-Tac-Toe AI (Minimax)")

board = st.session_state.board
current_player = player(board)

# Draw the board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = board[i][j]
        label = cell if cell else " "
        if not terminal(board) and cell is None:
            if cols[j].button(label, key=f"{i}-{j}"):
                # Human move
                board = result(board, (i, j))
                st.session_state.board = board

                # AI move
                if not terminal(board):
                    ai_move = minimax(board)
                    if ai_move:
                        board = result(board, ai_move)
                        st.session_state.board = board
                st.experimental_rerun()  # This is still safe here, only used after button click
        else:
            cols[j].markdown(f"### {label}")

# Show game result
if terminal(board):
    game_winner = winner(board)
    if game_winner:
        st.success(f"🏆 Game Over! Winner: {game_winner}")
    else:
        st.info("🤝 Game Over! It's a tie!")

# Restart game
if st.button("🔁 Restart Game"):
    st.session_state.board = initial_state()
    st.experimental_rerun()
