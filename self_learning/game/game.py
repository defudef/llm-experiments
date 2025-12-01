class Game:
  bulbs: list[bool] = []
  changes: list[int] = []
  target: list[int] = []
  
  def __init__(self, bulbs: list[bool], changes: list[bool]):
    self.bulbs = bulbs
    self.changes = changes
    self.target = self._calculate_target()

  def print_bulbs(self, values: list[bool]):
    print(''.join('o' if b else '*' for b in values))

  def _calculate_target(self):
    target = []

    for c in self.changes:
      target.append(self.bulbs[c])

    return target

  def print_board(self):
    self.print_bulbs(self.bulbs)

  def print_target(self):
    self.print_bulbs(self._calculate_target())

  def print_goal(self):
    goal: list[str] = []

    # Print changes as a, b, c, d, etc.
    for c in self.changes:
      goal.append(f"{chr(ord('a') + c)}")

    print(''.join(goal))

  