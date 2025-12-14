class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]
    def decide(self, cur, acc, avg_t):
        i = self.levels.index(cur)
        if acc >= 0.8 and avg_t < 4 and i < 2:
            return self.levels[i + 1]
        if acc <= 0.4 and i > 0:
            return self.levels[i - 1]
        return cur