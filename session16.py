import streamlit as st
import random

class SnakeAndLadder:
    def __init__(self):
        # Game board setup
        self.board_size = 100
        self.snakes = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }
        self.ladders = {
            1: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100
        }
        self.player_position = 0
        self.computer_position = 0


def roll_dice():
    return random.randint(1, 6)


def snake_and_ladder_game():
    st.title("🐍 Snake and Ladder Game")

    # Initialize game state
    if 'game' not in st.session_state or not hasattr(st.session_state.game, 'player_position'):
        st.session_state.game = SnakeAndLadder()
        st.session_state.game_over = False
        st.session_state.winner = None

    game = st.session_state.game

    # Game board visualization
    def create_board():
        board = []
        for i in range(10):
            row = []
            if i % 2 == 0:
                row = list(range(i * 10 + 1, (i + 1) * 10 + 1))
            else:
                row = list(range((i + 1) * 10, i * 10, -1))
            board.append(row)
        return board

    # Display board
    board = create_board()
    board_display = ""
    for row in board:
        board_display += " ".join(f"{num:3}" for num in row) + "\n"
    st.text(board_display)

    # Player and Computer positions
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🧑 Player Position: {game.player_position}")
    with col2:
        st.write(f"💻 Computer Position: {game.computer_position}")

    # Player's turn
    if st.button("Roll Dice"):
        # Player's move
        player_roll = roll_dice()
        st.write(f"You rolled: {player_roll}")

        new_player_pos = game.player_position + player_roll

        # Check for snakes and ladders
        if new_player_pos in game.snakes:
            game.player_position = game.snakes[new_player_pos]
            st.warning(f"Oops! Snake bite! Moved to {game.player_position}")
        elif new_player_pos in game.ladders:
            game.player_position = game.ladders[new_player_pos]
            st.success(f"Yay! Ladder climb! Moved to {game.player_position}")
        else:
            game.player_position = min(new_player_pos, 100)

        # Check if player won
        if game.player_position == 100:
            st.balloons()
            st.success("🎉 Congratulations! You won!")
            st.session_state.game_over = True
            st.session_state.winner = "Player"

        # Computer's move
        if not st.session_state.game_over:
            computer_roll = roll_dice()
            st.write(f"Computer rolled: {computer_roll}")

            new_computer_pos = game.computer_position + computer_roll

            # Check for snakes and ladders
            if new_computer_pos in game.snakes:
                game.computer_position = game.snakes[new_computer_pos]
                st.warning(f"Computer hit a snake! Moved to {game.computer_position}")
            elif new_computer_pos in game.ladders:
                game.computer_position = game.ladders[new_computer_pos]
                st.success(f"Computer climbed a ladder! Moved to {game.computer_position}")
            else:
                game.computer_position = min(new_computer_pos, 100)

            # Check if computer won
            if game.computer_position == 100:
                st.error("Computer won! Better luck next time.")
                st.session_state.game_over = True
                st.session_state.winner = "Computer"

    # Reset game button
    if st.button("Reset Game"):
        # Instead of experimental_rerun(), we'll directly reset the state
        st.session_state.game = SnakeAndLadder()
        st.session_state.game_over = False
        st.session_state.winner = None
        # Rerun is no longer needed as Streamlit will automatically refresh

    # Game statistics
    if st.session_state.game_over:
        st.header("Game Result")
        st.write(f"Winner: {st.session_state.winner}")


# Run the game
def main():
    snake_and_ladder_game()


if __name__ == "__main__":
    main()
