# streamlit_mbti_study_recommender.py
# A playful Streamlit app that recommends study methods based on MBTI type.
# Drop into a GitHub repo and deploy to Streamlit Cloud as `app.py`.

import streamlit as st
import time
import random

st.set_page_config(page_title="MBTI Study Buddy 📚✨", page_icon="🧠", layout="centered")

# --- Data: MBTI -> Recommendations (short, fun, emoji-rich) ---
MBTI_RECS = {
    "INTJ": {
        "emoji": "🧠",
        "title": "Strategic Solo Planner",
        "tips": [
            "Make a long-term study plan — break into milestones 🗺️",
            "Study alone in focused blocks (Pomodoro 25/5) ⏱️",
            "Use mind maps to connect concepts 🕸️",
            "Teach the concept to an imaginary audience 🎙️"
        ]
    },
    "INTP": {
        "emoji": "🔬",
        "title": "Curious Concept Hacker",
        "tips": [
            "Dive into the principles — ask ‘why’ repeatedly 🤔",
            "Build small experiments or mini-projects 🧩",
            "Keep a question notebook and chase answers 📓",
            "Pair reading with hands-on examples (practice>theory) ⚙️"
        ]
    },
    "ENTJ": {
        "emoji": "🚀",
        "title": "Goal-Driven Leader",
        "tips": [
            "Set measurable targets and schedules 📈",
            "Use group study to teach & lead discussions 🗣️",
            "Prioritize high-impact topics first 🔥",
            "Track progress with a visible checklist ✅"
        ]
    },
    "ENTP": {
        "emoji": "💡",
        "title": "Idea-Generating Challenger",
        "tips": [
            "Debate concepts with friends or online forums 🗨️",
            "Switch topics when interest dips (variety!) 🎨",
            "Prototype ideas quickly — learn by doing 🛠️",
            "Use flashcards for quick idea-refresh sessions ⚡"
        ]
    },
    "INFJ": {
        "emoji": "🌿",
        "title": "Meaningful Reflective Learner",
        "tips": [
            "Connect study topics to personal goals or values ❤️",
            "Create a calm, distraction-free ritual space 🕯️",
            "Summarize topics in personal metaphors or stories 📖",
            "Use spaced repetition for long-term retention 🔁"
        ]
    },
    "INFP": {
        "emoji": "🎨",
        "title": "Value-Driven Explorer",
        "tips": [
            "Turn study into a creative project (mind maps, doodles) ✍️",
            "Study when inspiration hits; small consistent sessions 🌤️",
            "Relate facts to real-life examples you care about 🌱",
            "Reward progress with tiny joys (snack, walk) 🍪"
        ]
    },
    "ENFJ": {
        "emoji": "🤝",
        "title": "Supportive Group Motivator",
        "tips": [
            "Organize study groups and lead recap sessions 📚",
            "Use role-play to act out scenarios or problems 🎭",
            "Give and request feedback — it helps retention 🔁",
            "Create collaborative goals and celebrate hits 🎉"
        ]
    },
    "ENFP": {
        "emoji": "✨",
        "title": "Enthusiastic Connector",
        "tips": [
            "Keep study sessions lively — switch formats often 🔄",
            "Use visuals, stories, and analogies to remember ✨",
            "Study with peers for energy and brainstorming 🤩",
            "Gamify tasks (points, timers, small rewards) 🕹️"
        ]
    },
    "ISTJ": {
        "emoji": "📏",
        "title": "Organized Reliability",
        "tips": [
            "Make a clear checklist and follow routines 🗂️",
            "Set dedicated study times and stick to them ⏰",
            "Use past papers and practice tests for mastery 📝",
            "Keep notes tidy — your future self will thank you 🙏"
        ]
    },
    "ISFJ": {
        "emoji": "🛡️",
        "title": "Steady Supporter",
        "tips": [
            "Study in comfortable, familiar spots 🛋️",
            "Break work into small, manageable tasks 📦",
            "Use repetition and summaries to lock knowledge 🔐",
            "Teach someone else — explaining helps remember 👩‍🏫"
        ]
    },
    "ESTJ": {
        "emoji": "🏛️",
        "title": "Practical Organizer",
        "tips": [
            "Plan study sessions with clear outcomes and deadlines 🗓️",
            "Prioritize based on exam weight / importance ⚖️",
            "Use checklists and timed drills to build speed ⏱️",
            "Review and correct mistakes immediately ✅"
        ]
    },
    "ESFJ": {
        "emoji": "💐",
        "title": "Helpful Harmonizer",
        "tips": [
            "Study with friends or in small groups for support 🤗",
            "Create study schedules that include breaks and rewards 🎀",
            "Use teaching as a tool — host mini-lessons 📣",
            "Organize notes clearly for review and sharing 📘"
        ]
    },
    "ISTP": {
        "emoji": "🧰",
        "title": "Hands-On Problem Solver",
        "tips": [
            "Learn by doing — labs, projects, practice problems 🔧",
            "Use short focused sessions and then move physically 🚴",
            "Apply concepts to real problems or gadgets 🧩",
            "Keep explanations concise and practical ✂️"
        ]
    },
    "ISFP": {
        "emoji": "🌸",
        "title": "Quiet Improviser",
        "tips": [
            "Use creative note-taking (colors, doodles) 🎨",
            "Study in short, pleasant bursts that respect your rhythm 💤",
            "Relate learning to sensory or emotional examples 🌈",
            "Keep a relaxed review routine — low pressure ✅"
        ]
    },
    "ESTP": {
        "emoji": "⚡",
        "title": "Action-Focused Challenger",
        "tips": [
            "Use competitive drills or timed quizzes 🏁",
            "Practice applying knowledge in real contexts ⚙️",
            "Keep sessions dynamic — change activities fast 🔁",
            "Use group challenges to keep motivation high 🙌"
        ]
    },
    "ESFP": {
        "emoji": "🎉",
        "title": "Playful Performer",
        "tips": [
            "Turn study into games, songs, or skits 🎶",
            "Study with friends and socialize with purpose 🥳",
            "Use visuals and physical activity to remember ✨",
            "Celebrate small wins with fun treats 🎈"
        ]
    }
}

# --- Helper functions ---

def simulate_matching_animation():
    """Play a playful progress and then balloons"""
    placeholder = st.empty()
    progress = placeholder.progress(0)
    for i in range(0, 101, random.randint(8, 18)):
        progress.progress(i)
        time.sleep(0.06)
    placeholder.empty()
    st.balloons()


# --- UI ---
st.markdown("# MBTI Study Buddy \nFind your perfect study groove! 🎧📚")
st.markdown("---")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("Choose your MBTI type and get a playful, emoji-filled study plan tuned to how you learn best. ✨")
    mbti = st.selectbox("Pick your MBTI type:", options=sorted(MBTI_RECS.keys()))
    custom_note = st.text_area("Optional: Tell me a little about your study context (exam, project, schedule):", max_chars=200)
    if st.button("Find my study method! 🎯"):
        simulate_matching_animation()
        rec = MBTI_RECS.get(mbti)
        # Header card
        st.markdown(f"## {rec['emoji']} {rec['title']} — {mbti}")
        if custom_note:
            st.info(f"Context: {custom_note}")
        # Tips
        st.write("**Top study tips:**")
        for i, tip in enumerate(rec['tips'], start=1):
            st.markdown(f"{i}. {tip}")

        # Quick cheatsheet block
        st.write("---")
        st.subheader("Quick cheatsheet ⚡")
        cheats = {
            "Best time": random.choice(["Morning 🌅", "Afternoon ☀️", "Evening 🌙", "Depends on you — test both!"]),
            "Session length": random.choice(["25–30 min (Pomodoro)", "50–90 min deep focus", "2–3 short bursts with breaks"]),
            "Motivation boost": random.choice(["Study buddy", "Playlist", "Snacks + short walk"])
        }
        st.write(f"• **Best time:** {cheats['Best time']}")
        st.write(f"• **Session length:** {cheats['Session length']}")
        st.write(f"• **Motivation boost:** {cheats['Motivation boost']}")

        # Fun little confetti GIF (external) — if image fails it's non-blocking
        try:
            st.image('https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif', caption='Party! 🎉')
        except Exception:
            pass

with col2:
    st.markdown("### Quick MBTI map")
    # Show a short grid of types with emojis
    grid = ""
    for t, v in MBTI_RECS.items():
        grid += f"**{t}** {v['emoji']} — {v['title']}  \n"
    st.markdown(grid)

st.write("---")

# Footer: extra playful interactions
if st.button("Surprise me — random tip 🎲"):
    t = random.choice(list(MBTI_RECS.values()))
    st.success(f"Random pick: {t['emoji']} {t['title']} — try: {random.choice(t['tips'])}")
    st.snow()

st.write("Made with ❤️ for learners. Deploy this file as `app.py` on Streamlit Cloud.")

# End of file
