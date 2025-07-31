import streamlit as st
from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

# Initialize the game state
if 'board' not in st.session_state:
    st.session_state.board = initial_state()

st.title("🤖 Tic-Tac-Toe AI (Minimax)")

board = st.session_state.board
game_over = terminal(board)
current_player = player(board)

# UI to draw the board and handle player move
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell = board[i][j]
        label = cell if cell else " "
        key = f"{i}-{j}"

        if not game_over and cell is None:
            if cols[j].button(label, key=key):
                # Player move
                st.session_state.board = result(board, (i, j))

                # AI move if game not over
                if not terminal(st.session_state.board):
                    ai_move = minimax(st.session_state.board)
                    if ai_move:
                        st.session_state.board = result(st.session_state.board, ai_move)

                st.experimental_rerun()  # Safe here, inside the button block
        else:
            cols[j].markdown(f"### {label}")

# Show result
if terminal(st.session_state.board):
    win = winner(st.session_state.board)
    if win:
        st.success(f"🏆 Game Over! Winner: {win}")
    else:
        st.info("🤝 Game Over! It's a tie!")

# Restart button
if st.button("🔁 Restart Game"):
    st.session_state.board = initial_state()
    st.experimental_rerun()
