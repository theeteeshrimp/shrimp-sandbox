#!/usr/bin/env python3
"""
🦐 Shrimp Guesser 9000
A totally over-engineered number guessing game with shrimp energy
"""

import random
import sys
from datetime import datetime


class ShrimpGame:
    """The main game class - shrimp style!"""
    
    SHRIMP_EMOJIS = ["🦐", "🍤", "🦞", "🦀", "🐙", "🦑"]
    
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        self.guesses = []
        self.start_time = None
        
    def print_header(self):
        """Print that fancy header"""
        print("\n" + "=" * 50)
        print("🦐  SHRIMP GUESSER 9000  🦐")
        print("=" * 50)
        print("\nI'm thinking of a number between 1 and 100...")
        print(f"You have {self.max_attempts} attempts! Don't disappoint the shrimp.")
        print()
        
    def get_hint(self, guess):
        """Give the player a hint"""
        diff = abs(guess - self.number)
        if diff == 0:
            return "🎉 CORRECT!"
        elif diff <= 5:
            return "🔥 SUPER HOT! You're SO close!"
        elif diff <= 10:
            return "🌡️ Getting warm!"
        elif diff <= 20:
            return "❄️ Cold... but not frozen"
        else:
            return "🧊 FREEZING! Try something way different"
            
    def get_emoji_rating(self):
        """Rate their performance with shrimp"""
        if self.attempts <= 3:
            return "🦐🦐🦐 LEGENDARY SHRIMP!"
        elif self.attempts <= 6:
            return "🦐🦐 Solid shrimp!"
        elif self.attempts <= 9:
            return "🦐 Adequate shrimp..."
        else:
            return "🍤 Cooked shrimp (barely made it)"
            
    def play(self):
        """Main game loop"""
        self.start_time = datetime.now()
        self.print_header()
        
        while self.attempts < self.max_attempts:
            remaining = self.max_attempts - self.attempts
            print(f"\n[{remaining} attempts left] Your guess: ", end="")
            
            try:
                guess = input().strip()
                
                # Easter eggs!
                if guess.lower() in ["quit", "exit", "q"]:
                    print("\n🦐 The shrimp is disappointed. Goodbye!")
                    return
                elif guess.lower() == "hint":
                    print(f"💡 The number is {self.number % 2 == 0 and 'even' or 'odd'}")
                    continue
                elif guess.lower() == "shrimp":
                    print(f"🦐 {random.choice(self.SHRIMP_EMOJIS)} Shrimp mode activated!")
                    continue
                    
                guess = int(guess)
                
                if guess < 1 or guess > 100:
                    print("🚨 Hey! That's not between 1 and 100! Try again.")
                    continue
                    
                if guess in self.guesses:
                    print("🤔 You already guessed that! Pay attention!")
                    continue
                    
                self.guesses.append(guess)
                self.attempts += 1
                
                hint = self.get_hint(guess)
                print(hint)
                
                if guess == self.number:
                    self.victory()
                    return
                    
            except ValueError:
                print("🚨 That's not a number! Type 'quit' to exit.")
                continue
                
        # Game over
        self.game_over()
        
    def victory(self):
        """They won!"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        rating = self.get_emoji_rating()
        
        print("\n" + "=" * 50)
        print("🎉 VICTORY! YOU FOUND THE NUMBER! 🎉")
        print(f"Number: {self.number}")
        print(f"Attempts: {self.attempts}")
        print(f"Time: {elapsed:.1f} seconds")
        print(f"Rating: {rating}")
        print("=" * 50)
        
    def game_over(self):
        """They lost :("""
        print("\n" + "=" * 50)
        print("🍤 GAME OVER 🍤")
        print(f"The number was: {self.number}")
        print("Better luck next time, shrimp friend!")
        print("=" * 50)


def main():
    """Entry point"""
    print("🦐 Welcome to Shrimp Guesser 9000!")
    print("Commands: 'quit' to exit, 'hint' for a clue, 'shrimp' for vibes")
    
    while True:
        game = ShrimpGame()
        game.play()
        
        print("\nPlay again? (y/n): ", end="")
        if input().strip().lower() not in ["y", "yes", "yeah", "yep"]:
            print("\n🦐 Thanks for playing! Stay shrimpy!")
            break


if __name__ == "__main__":
    main()
