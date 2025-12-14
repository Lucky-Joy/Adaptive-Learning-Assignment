import time
from collections import defaultdict
class PerformanceTracker:
    def __init__(self):
        self.logs = []
    def log(self, lvl, op, correct, start_t):
        self.logs.append({
            "difficulty": lvl,
            "operation": op,
            "correct": int(correct),
            "time": time.time() - start_t
        })
    def stats(self, n=5):
        data = self.logs[-n:]
        if not data:
            return 0, 0
        acc = sum(x["correct"] for x in data) / len(data)
        avg_t = sum(x["time"] for x in data) / len(data)
        return acc, avg_t
    def summary(self):
        total = len(self.logs)
        if total == 0:
            return 0, 0, 0, [], [], [], 0
        acc = sum(x["correct"] for x in self.logs) / total
        avg_t = sum(x["time"] for x in self.logs) / total
        total_t = sum(x["time"] for x in self.logs)
        op_stats = defaultdict(list)
        for x in self.logs:
            op_stats[x["operation"]].append(x["correct"])
        strong = []
        weak = []
        attempted = set(op_stats.keys())
        all_ops = {"+", "-", "*", "/"}
        for op, vals in op_stats.items():
            if len(vals) >= 2:
                a = sum(vals) / len(vals)
                if a >= 0.8:
                    strong.append(op)
                elif a < 0.6:
                    weak.append(op)
        unattempted = list(all_ops - attempted)
        return total, acc, avg_t, strong, weak, unattempted, total_t