import random
class PuzzleGenerator:
    def __init__(self):
        self.levels = {
            "Easy": (["+","-"], 1, 10),
            "Medium": (["+","-","*"], 1, 25),
            "Hard": (["+","-","*","/"], 1, 100)
        }
    def generate(self, lvl):
        ops, lo, hi = self.levels[lvl]
        a = random.randint(lo, hi)
        b = random.randint(lo, hi)
        op = random.choice(ops)
        if op == "/":
            b = random.randint(1, hi)
            a = a * b
        q = f"{a} {op} {b}"
        ans = int(eval(q))
        return q, ans, op