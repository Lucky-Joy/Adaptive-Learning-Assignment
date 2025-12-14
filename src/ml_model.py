class DifficultyModel:
    def predict_up(self, acc, t, lvl):
        s = 0.6 * acc - 0.1 * t + 0.2 * lvl
        return max(0, min(1, s))