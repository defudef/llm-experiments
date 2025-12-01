from os import path
from dotenv import load_dotenv

import asyncio

from self_learning.game.game import Game

load_dotenv()

# Resolve paths relative to this script's directory
SCRIPT_DIR = path.dirname(path.abspath(__file__))
MEMORY_DIR = path.join(SCRIPT_DIR, "memory")

async def main():
  # Check if notes.md exists. If not. Add empty file at memory/notes.md
  notes_path = path.join(MEMORY_DIR, "notes.md")
  if not path.exists(notes_path):
    with open(notes_path, "w") as f:
      f.write("")

  # Check if algorithm.py exists. If not. Add empty file at memory/algorithm.py
  algorithm_path = path.join(MEMORY_DIR, "algorithm.py")
  if not path.exists(algorithm_path):
    with open(algorithm_path, "w") as f:
      f.write("")

  game = Game([True, False, True, False], [3, 1, 0, 2])
  game.print_board()
  game.print_goal()
  game.print_target()

if __name__ == "__main__":
  asyncio.run(main())
