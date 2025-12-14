# 🧮 Math Adventures — Adaptive Learning Prototype

**Math Adventures** is a minimal AI-powered adaptive learning prototype designed to help children (ages 5–10) practise basic mathematics through personalised difficulty adjustment and meaningful feedback.

The system dynamically adapts problem difficulty based on learner performance, tracks accuracy and response time, and provides end-of-session insights to guide further learning.
The focus of the project is on **adaptive logic and learning intelligence**, not on complex UI or heavy machine learning.

---

## Key Features

* **Dynamic Puzzle Generation**

  * Supports addition, subtraction, multiplication, and division
  * Problems are generated based on difficulty level (Easy, Medium, Hard)

* **Performance Tracking**

  * Tracks correctness per question
  * Measures response time per question
  * Maintains session-level statistics

* **Adaptive Difficulty Engine**

  * Automatically increases difficulty when the learner performs well
  * Reduces difficulty when the learner struggles
  * Uses a combination of rule-based logic and ML-inspired scoring

* **Intelligent Feedback System**

  * Distinguishes between:

    * Strong topics
    * Weak topics
    * Unattempted topics
  * Provides:

    * Encouraging feedback for mastered topics
    * Targeted practice suggestions for weak areas
    * Exploration prompts for unattempted operations

* **Session Summary**

  * Total questions attempted
  * Accuracy percentage
  * Average time per question
  * Total session time
  * Recommended next learning direction

* **Clean, Minimal UI**

  * Subtle neumorphic design for better readability
  * Works in both light and dark modes
  * UI remains secondary to learning logic

---

## Adaptive Learning Logic

### Difficulty Adjustment

Difficulty is adjusted after each question using recent performance:

* **Increase difficulty** when:

  * Accuracy is high
  * Response time is consistently low

* **Decrease difficulty** when:

  * Accuracy drops significantly

* **Maintain difficulty** otherwise

A lightweight scoring function inspired by ML decision-making is used to smooth transitions and avoid abrupt difficulty jumps.

---

### Topic-Level Feedback Logic

For each mathematical operation (`+`, `-`, `*`, `/`), the system classifies learner performance into three states:

* **Strong**

  * At least 2 attempts
  * Accuracy ≥ 80%

* **Weak**

  * At least 2 attempts
  * Accuracy < 60%

* **Unattempted**

  * No attempts yet

Feedback follows a clear priority:

1. Suggest practising weak topics (if any)
2. Encourage exploring unattempted topics when current topics are strong
3. Provide positive reinforcement when performance is consistently strong

This avoids misleading feedback and ensures recommendations are evidence-based.

---

## Project Structure

```
math-adventures/
├─ requirements.txt
└─ src/
   ├─ main.py              # Application flow and UI
   ├─ puzzle_generator.py  # Math puzzle generation logic
   ├─ tracker.py           # Performance tracking and analysis
   ├─ adaptive_engine.py   # Rule-based difficulty adjustment
   └─ ml_model.py          # ML-inspired difficulty scoring
```

---

## Running the Project

### Requirements

* Python 3.9+
* Streamlit

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run src/main.py
```

---

## Design Philosophy

* **Simplicity over complexity**
  The system prioritises clarity and interpretability over heavy machine learning.

* **Interaction-first learning**
  Adaptation is driven by real-time user interaction rather than pre-trained datasets.

* **Explainable decisions**
  All difficulty and feedback decisions are rule-based or score-based and easy to reason about.

* **Extensible architecture**
  The current design can be extended to other subjects or enhanced with real user data in the future.

---

## Possible Extensions

* Persist session data for long-term learner profiling
* Train a real ML model using collected interaction data
* Add adaptive time limits per difficulty
* Extend beyond math to other learning domains

---

## Conclusion

Math Adventures demonstrates how adaptive learning systems can be built using simple, interpretable logic while still delivering personalised and meaningful learning experiences. The project focuses on *how learners improve*, not just *whether answers are correct*, making it a strong foundation for scalable educational technology.

---

Just tell me.
