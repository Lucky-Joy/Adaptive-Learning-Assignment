import streamlit as st
import time
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine
from ml_model import DifficultyModel

pg = PuzzleGenerator()
ae = AdaptiveEngine()
ml = DifficultyModel()

st.set_page_config(page_title="Math Adventures", layout="centered")

st.markdown("""
<style>
:root {
    --neu-bg: var(--secondary-background-color);
    --neu-light: rgba(255,255,255,0.6);
    --neu-dark: rgba(0,0,0,0.15);
}
.neu-box {
    padding: 22px;
    border-radius: 18px;
    background: var(--neu-bg);
    box-shadow:
        6px 6px 12px var(--neu-dark),
        -6px -6px 12px var(--neu-light);
    margin-bottom: 18px;
}
.title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 12px;
}
.label {
    font-size: 18px;
    font-weight: 500;
}
.question {
    font-size: 30px;
    font-weight: 600;
    text-align: center;
    margin-top: 14px;
}
</style>
""", unsafe_allow_html=True)

if "state" not in st.session_state:
    st.session_state.state = "start"
    st.session_state.tr = PerformanceTracker()
    st.session_state.q = None

st.markdown("<div class='title'>Math Adventures</div>", unsafe_allow_html=True)

if st.session_state.state == "start":
    st.session_state.name = st.text_input("Enter your name")
    st.session_state.lvl = st.selectbox(
        "Choose starting difficulty",
        ["Easy", "Medium", "Hard"]
    )
    if st.button("Start Session"):
        st.session_state.tr = PerformanceTracker()
        st.session_state.q = None
        st.session_state.state = "play"
        st.rerun()

elif st.session_state.state == "play":
    if st.session_state.q is None:
        (
            st.session_state.q,
            st.session_state.ans,
            st.session_state.op
        ) = pg.generate(st.session_state.lvl)
        st.session_state.start_t = time.time()
    st.markdown(f"""
    <div class="neu-box">
        <div class="label">Player: {st.session_state.name}</div>
        <div class="label">Difficulty: {st.session_state.lvl}</div>
        <div class="question">{st.session_state.q}</div>
    </div>
    """, unsafe_allow_html=True)
    u = st.number_input("Your Answer", step=1)
    if st.button("Submit"):
        ok = int(u) == st.session_state.ans
        st.session_state.tr.log(
            st.session_state.lvl,
            st.session_state.op,
            ok,
            st.session_state.start_t
        )
        acc, avg_t = st.session_state.tr.stats()
        idx = ["Easy", "Medium", "Hard"].index(st.session_state.lvl)
        if ml.predict_up(acc, avg_t, idx) > 0.7:
            st.session_state.lvl = ae.levels[min(2, idx + 1)]
        else:
            st.session_state.lvl = ae.decide(
                st.session_state.lvl, acc, avg_t
            )
        st.session_state.q = None
        st.rerun()
    if st.button("End Session"):
        st.session_state.state = "summary"
        st.rerun()

elif st.session_state.state == "summary":
    (
        total,
        acc,
        avg_t,
        strong,
        weak,
        unattempted,
        total_t
    ) = st.session_state.tr.summary()
    st.markdown("<div class='neu-box'>", unsafe_allow_html=True)
    st.subheader("Session Summary")
    st.write("Questions Attempted:", total)
    st.write("Accuracy:", round(acc * 100, 2), "%")
    st.write("Average time per question:", round(avg_t, 2), "seconds")
    st.write("Total session time:", round(total_t, 2), "seconds")
    if acc >= 0.8:
        st.success("You're doing great!")
    elif acc >= 0.5:
        st.warning("Good progress. Keep practising.")
    else:
        st.error("You need more practice. Don't give up!")
    mp = {
        "+": "addition",
        "-": "subtraction",
        "*": "multiplication",
        "/": "division"
    }
    if weak:
        topics = ", ".join(mp[o] for o in weak)
        st.info(f"You should practise **{topics}** more.")
    elif strong and unattempted:
        done = ", ".join(mp[o] for o in strong)
        todo = ", ".join(mp[o] for o in unattempted if o in mp)
        if todo:
            st.info(
                f"You're doing great with **{done}**. "
                f"Try **{todo}** next."
            )
    elif strong:
        done = ", ".join(mp[o] for o in strong)
        st.info(f"Excellent work with **{done}**!")
    if st.button("Start New Session"):
        st.session_state.state = "start"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)