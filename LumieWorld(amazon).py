import streamlit as st
from gtts import gTTS
import os
import json
import time
import streamlit.components.v1 as components

# Pink/Purple LumieWorld Theme CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f8f4ff, #fff0f8);
        padding: 20px;
    }
    .stApp {
        background: linear-gradient(135deg, #f8f4ff, #fff0f8);
    }
    
    /* Full height sidebar */
    .css-1d391kg {
        background: #f8f9fa;
        height: 100vh;
        padding-top: 20px;
        border-right: 2px solid #e1bee7;
    }
    
    /* Help button in top right */
    .help-button {
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #e91e63, #f06292);
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 14px;
        cursor: pointer;
        z-index: 1000;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3);
        border: none;
    }
    
    /* Pink theme buttons */
    .stButton > button {
        background: linear-gradient(135deg, #e91e63, #f06292) !important;
        color: white !important;
        border: none;
        border-radius: 25px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: 600;
        margin: 8px 0;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #d81b60, #e91e63) !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.4);
    }
    
    /* Sidebar button text override */
    .css-1d391kg .stButton > button,
    .css-1d391kg .stButton > button *,
    .css-1d391kg button,
    .css-1d391kg button * {
        color: white !important;
        background: linear-gradient(135deg, #e91e63, #f06292) !important;
    }
    
    /* Universal button text force */
    .stButton button p,
    .stButton button span,
    .stButton button div {
        color: white !important;
    }
    
    /* Pink theme inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background-color: white;
        border: 2px solid #e1bee7;
        color: #333333 !important;
        border-radius: 12px;
        font-size: 16px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(233, 30, 99, 0.1);
    }
    
    .stSelectbox > div > div > div {
        color: #333333 !important;
    }
    
    /* Pink theme radio buttons */
    .stRadio > div {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        border: 2px solid #e1bee7;
        box-shadow: 0 2px 8px rgba(233, 30, 99, 0.1);
    }
    
    /* Pink theme multiselect */
    .stMultiSelect > div > div {
        background-color: white;
        border: 2px solid #e1bee7;
        color: #333333 !important;
        border-radius: 12px;
    }
    .stMultiSelect > div > div > div {
        color: #333333 !important;
    }
    
    /* Pink theme metrics */
    .stMetric {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #e1bee7;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1);
    }
    
    /* Pink theme tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        border: 2px solid #e1bee7;
        border-radius: 12px;
        padding: 15px 25px;
        font-size: 16px;
        font-weight: 600;
        color: #e91e63;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #e91e63, #f06292);
        color: white;
    }
    
    /* Pink theme headers */
    h1, h2, h3 {
        color: #333333;
        font-weight: 700;
    }
    
    /* Text colors */
    p, div, span, label {
        color: #666666 !important;
        font-size: 16px;
    }
    
    /* Override for sidebar */
    .css-1d391kg p,
    .css-1d391kg div,
    .css-1d391kg span,
    .css-1d391kg label {
        color: white !important;
    }
    
    /* Assessment card styling */
    .assessment-card {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        border: 3px solid #e1bee7;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.15);
        max-width: 600px;
    }
    
    /* MCQ and Fill in the blanks styling */
    .mcq-question, .fill-blank-sentence {
        font-size: 20px;
        font-weight: 600;
        color: #333333;
        margin: 20px 0;
        padding: 15px;
        background-color: white;
        border-radius: 12px;
        border-left: 5px solid #e91e63;
        box-shadow: 0 2px 8px rgba(233, 30, 99, 0.1);
    }
    
    .fill-blank-translation {
        font-size: 16px;
        color: #666666;
        font-style: italic;
        margin-bottom: 15px;
    }
    
    .correct-answer {
        font-size: 18px;
        font-weight: 600;
        color: #28a745;
        background-color: #d4edda;
        padding: 12px;
        border-radius: 12px;
        margin: 10px 0;
        border-left: 4px solid #28a745;
    }
    
    .wrong-answer {
        font-size: 18px;
        font-weight: 600;
        color: #dc3545;
        background-color: #f8d7da;
        padding: 12px;
        border-radius: 12px;
        margin: 10px 0;
        border-left: 4px solid #dc3545;
    }
    
    .points-earned {
        font-size: 20px;
        font-weight: bold;
        color: #e91e63;
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin: 20px 0;
        border: 3px solid #e91e63;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.2);
    }
    
    /* Sidebar styling */
    .css-1d391kg .stRadio > div {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .css-1d391kg .stRadio label {
        color: white !important;
        font-weight: 500;
    }
    
    .css-1d391kg h2 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Sidebar text elements */
    .css-1d391kg p,
    .css-1d391kg div,
    .css-1d391kg span,
    .css-1d391kg label {
        color: white !important;
    }
    
    /* Welcome header */
    .welcome-header {
        background: linear-gradient(135deg, #e91e63, #9c27b0);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.3);
    }
    
    /* Content cards */
    .exercise-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #e1bee7;
        margin: 20px 0;
        box-shadow: 0 6px 20px rgba(233, 30, 99, 0.1);
    }
    
    /* Success/Info messages */
    .stSuccess {
        background-color: #e8f5e8;
        border: 1px solid #4caf50;
        border-radius: 12px;
    }
    
    .stInfo {
        background-color: #fff3e0;
        border: 1px solid #e91e63;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="LumieWorld", page_icon="🌟", layout="wide")

# Help button in top right
st.markdown('<button class="help-button">🌟 Help</button>', unsafe_allow_html=True)

# Profile persistence functions
def save_profile_to_file():
    """Save user profile and progress to file"""
    profile_data = {
        'user_profile': st.session_state.user_profile,
        'progress': st.session_state.progress,
        'purchased_characters': st.session_state.purchased_characters,
        'character_conversations': st.session_state.character_conversations,
        'completed_levels': st.session_state.completed_levels,
        'current_level': st.session_state.current_level,
        'completed_exercises': st.session_state.completed_exercises,
        'character_relationships': st.session_state.character_relationships
    }
    try:
        with open('lumie_profile.json', 'w') as f:
            json.dump(profile_data, f)
    except Exception as e:
        st.error(f"Error saving profile: {e}")

def load_profile_from_file():
    """Load user profile and progress from file"""
    try:
        if os.path.exists('lumie_profile.json'):
            with open('lumie_profile.json', 'r') as f:
                profile_data = json.load(f)
                st.session_state.user_profile = profile_data.get('user_profile', st.session_state.user_profile)
                st.session_state.progress = profile_data.get('progress', st.session_state.progress)
                st.session_state.purchased_characters = profile_data.get('purchased_characters', ['Jake', 'Professor Anya', 'Kaito'])
                st.session_state.character_conversations = profile_data.get('character_conversations', {})
                st.session_state.completed_levels = profile_data.get('completed_levels', [])
                st.session_state.current_level = profile_data.get('current_level', 1)
                st.session_state.completed_exercises = profile_data.get('completed_exercises', {})
                st.session_state.character_relationships = profile_data.get('character_relationships', {})
            return True
    except Exception as e:
        st.error(f"Error loading profile: {e}")
    return False

# Initialize session state with enhanced progress tracking
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'native_lang': 'English',
        'target_lang': 'Spanish',
        'level': 'Beginner',
        'interests': ['Travel', 'Food'],
        'learning_style': 'Interactive',
        'study_time': '15-30 min',
        'personality': 'Extrovert',
        'goal': 'Basic conversation'
    }
if 'progress' not in st.session_state:
    st.session_state.progress = {
        'lessons_completed': 5, 
        'words_learned': 25, 
        'streak': 3,
        'total_points': 1000,
        'correct_answers': 0,
        'total_questions': 0,
        'difficulty_level': 1,  # 1=Easy, 2=Medium, 3=Hard
        'recent_scores': [],  # Track last 10 exercise scores
        'conversation_points': 0  # Points earned from AI conversations
    }
if 'fill_blank_questions' not in st.session_state:
    st.session_state.fill_blank_questions = []
if 'mcq_questions' not in st.session_state:
    st.session_state.mcq_questions = []
if 'show_answers' not in st.session_state:
    st.session_state.show_answers = False
if 'show_mcq_answers' not in st.session_state:
    st.session_state.show_mcq_answers = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'selected_companion' not in st.session_state:
    st.session_state.selected_companion = None
if 'character_conversations' not in st.session_state:
    st.session_state.character_conversations = {}
if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False
if 'completed_levels' not in st.session_state:
    st.session_state.completed_levels = []
if 'current_level' not in st.session_state:
    st.session_state.current_level = 1
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None
if 'show_learning' not in st.session_state:
    st.session_state.show_learning = False
if 'completed_exercises' not in st.session_state:
    st.session_state.completed_exercises = {}
if 'character_relationships' not in st.session_state:
    st.session_state.character_relationships = {
        'Jake': 70,
        'Professor Anya': 30,
        'Kaito': 2
    }
if 'show_checkpoint' not in st.session_state:
    st.session_state.show_checkpoint = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = None
if 'voice_input' not in st.session_state:
    st.session_state.voice_input = ""

# Load saved profile after all session state is initialized
load_profile_from_file()
if 'assessment_page' not in st.session_state:
    st.session_state.assessment_page = 1
if 'purchased_characters' not in st.session_state:
    st.session_state.purchased_characters = ['Jake', 'Professor Anya', 'Kaito']  # Default characters

def calculate_level_from_points(points):
    """Calculate user level based on total points"""
    if points < 100:
        return "Beginner"
    elif points < 500:
        return "Elementary"
    elif points < 1000:
        return "Intermediate"
    elif points < 2000:
        return "Upper-Intermediate"
    else:
        return "Advanced"

def get_difficulty_level():
    """Determine difficulty based on recent performance"""
    recent_scores = st.session_state.progress['recent_scores']
    if len(recent_scores) < 3:
        return 1  # Start with easy
    
    avg_score = sum(recent_scores[-5:]) / len(recent_scores[-5:])  # Last 5 scores
    
    if avg_score >= 0.8:  # 80% or higher
        return min(3, st.session_state.progress['difficulty_level'] + 1)
    elif avg_score < 0.5:  # Less than 50%
        return max(1, st.session_state.progress['difficulty_level'] - 1)
    else:
        return st.session_state.progress['difficulty_level']

def award_points(correct_count, total_count):
    """Award points based on performance and update progress"""
    base_points = 10
    difficulty_multiplier = st.session_state.progress['difficulty_level']
    accuracy_bonus = int((correct_count / total_count) * 20) if total_count > 0 else 0
    
    points_earned = (correct_count * base_points * difficulty_multiplier) + accuracy_bonus
    
    # Update progress
    st.session_state.progress['total_points'] += points_earned
    st.session_state.progress['correct_answers'] += correct_count
    st.session_state.progress['total_questions'] += total_count
    
    # Track recent performance
    score = correct_count / total_count if total_count > 0 else 0
    st.session_state.progress['recent_scores'].append(score)
    if len(st.session_state.progress['recent_scores']) > 10:
        st.session_state.progress['recent_scores'].pop(0)
    
    # Update difficulty level
    st.session_state.progress['difficulty_level'] = get_difficulty_level()
    
    # Update user level
    new_level = calculate_level_from_points(st.session_state.progress['total_points'])
    st.session_state.user_profile['level'] = new_level
    
    return points_earned

import boto3
from botocore.exceptions import ClientError
import asyncio
import websockets
import base64

# Removed complex @ Transcribe function - using browser speech recognition instead

def generate_ai_response(prompt):
    try:
        bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1',
            aws_access_key_id='AKIAV2BW3E4QWA2RI2VE',
            aws_secret_access_key='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'
        )

        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 4096,
                "temperature": 0.7
            }
        })
        
        response = bedrock.invoke_model(
            body=body,
            modelId='amazon.nova-pro-v1:0',
            accept='application/json',
            contentType='application/json'
        )
        
        response_body = json.loads(response.get('body').read())
        return response_body['output']['message']['content'][0]['text']
        
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I'm having trouble generating a response right now."

def create_audio_polly(text, voice_id="Joanna"):
    try:
        polly = boto3.client(
            'polly',
            region_name='us-east-1',
            aws_access_key_id='AKIAV2BW3E4QWA2RI2VE',
            aws_secret_access_key='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'
        )
        
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            Engine='neural'
        )
        
        with open('polly_audio.mp3', 'wb') as f:
            f.write(response['AudioStream'].read())
        
        return 'polly_audio.mp3'
        
    except Exception as e:
        st.error(f"Polly error: {e}")
        return None

def create_audio(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save("temp_audio.mp3")
    return "temp_audio.mp3"

def format_chat_message(text):
    """Format chat message to properly display languages on separate lines"""
    # Remove any HTML entities
    import html
    text = html.unescape(text)
    
    # Split by lines and process
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Remove any remaining HTML tags
            import re
            line = re.sub(r'<[^>]+>', '', line)
            formatted_lines.append(line)
    
    return '<br><br>'.join(formatted_lines)  # Use HTML line breaks with spacing

def extract_target_language_text(text, target_lang):
    """Extract only target language text from AI response"""
    lines = text.split('\n')
    target_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('(') and not line.endswith(')') and not line.lower().startswith('translation'):
            # Skip lines that look like English translations
            if target_lang.lower() == 'spanish' and any(word in line.lower() for word in ['hello', 'how are you', 'what did you do', 'today', 'nice to meet']):
                continue
            target_lines.append(line)
    return ' '.join(target_lines)

def get_relationship_level(character_name):
    """Get relationship level and status for a character"""
    level = st.session_state.character_relationships.get(character_name, 0)
    if level < 5:
        return level, "Stranger"
    elif level < 15:
        return level, "Acquaintance"
    elif level < 30:
        return level, "Friend"
    elif level < 50:
        return level, "Close Friend"
    elif level < 70:
        return level, "Best Friend"
    else:
        return level, "Soulmate"

def increase_relationship(character_name):
    """Increase relationship level by 1 for each message"""
    if character_name not in st.session_state.character_relationships:
        st.session_state.character_relationships[character_name] = 0
    st.session_state.character_relationships[character_name] = min(100, st.session_state.character_relationships[character_name] + 1)



# Full-height Sidebar Navigation
with st.sidebar:
    # Main Menu Header
    st.markdown("""
    <div style='margin-bottom: 30px; padding: 20px 0;'>
        <h2 style='color: #ffffff; margin: 0; font-size: 24px; font-weight: 700;'>Main Menu</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Navigation buttons with icons
    nav_options = [
        ("🏠 Home", "🏠", "Home"),
        ("🗺️ City Roadmap", "☁️", "City Roadmap"), 
        ("👥 Characters", "📋", "Characters"),
        ("🛒 Lumie Shop", "⚙️", "Lumie Shop"),
        ("👤 Profile", "⚙️", "Profile")
    ]
    
    # Override page selection if coming from roadmap
    if st.session_state.current_page == "🎯 Checkpoint Assessment":
        page = "🎯 Checkpoint Assessment"
    elif st.session_state.current_page == "🗺️ City Roadmap":
        page = "🗺️ City Roadmap"
        st.session_state.current_page = None
    else:
        selected_idx = 0
        for i, (full_name, icon, display_name) in enumerate(nav_options):
            is_selected = st.session_state.get('selected_nav', 0) == i
            
            if st.button(f"{icon}   {display_name}", key=f"nav_{i}"):
                st.session_state.selected_nav = i
                page = full_name
                selected_idx = i
            
        if 'selected_nav' not in st.session_state:
            st.session_state.selected_nav = 0
            page = nav_options[0][0]
        else:
            page = nav_options[st.session_state.selected_nav][0]
        
        # Clear learning state when navigating to different pages
        if st.session_state.show_learning and page != "🗺️ City Roadmap":
            st.session_state.show_learning = False
            st.session_state.selected_topic = None
    
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
    
    # Quick Stats section
    st.markdown("<h3 style='color: #ffffff; font-size: 18px; margin-bottom: 15px; font-weight: 700;'>📊 Quick Stats</h3>", unsafe_allow_html=True)
    
    stats_html = f"""
    <div style='color: #ffffff; font-size: 14px; line-height: 1.8; font-weight: 600;'>
        <div style='margin-bottom: 8px;'><strong>Level:</strong> {st.session_state.user_profile.get('level', st.session_state.user_profile.get('speaking_level', 'Beginner'))}</div>
        <div style='margin-bottom: 8px;'><strong>Learning:</strong> {st.session_state.user_profile['target_lang']}</div>
        <div style='margin-bottom: 8px;'><strong>Points:</strong> {st.session_state.progress['total_points']}</div>
        <div style='margin-bottom: 8px;'><strong>Streak:</strong> {st.session_state.progress['streak']} days</div>
    </div>
    """
    st.markdown(stats_html, unsafe_allow_html=True)

profile = st.session_state.user_profile

# HOME PAGE
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("logo.jpg", width=400)
        except:
            st.markdown("<div style='text-align: center; font-size: 48px; margin: 20px 0;'>🌟 LumieWorld 🌟</div>", unsafe_allow_html=True)
    st.markdown('<div class="welcome-header"><h1 style="color: #ffffff;">Welcome to Your Personalized Language Learning Journey!</h1></div>', unsafe_allow_html=True)
    
    # Enhanced progress metrics
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    
    with col1:
        st.metric("🎯 Level", profile.get('level', profile.get('speaking_level', 'Beginner')))
    with col2:
        st.metric("🏆 Points", st.session_state.progress['total_points'])
    with col3:
        st.metric("📚 Lessons", st.session_state.progress['lessons_completed'])
    with col4:
        st.metric("✅ Accuracy", f"{int((st.session_state.progress['correct_answers'] / max(1, st.session_state.progress['total_questions'])) * 100)}%")
    with col5:
        st.metric("🔥 Streak", f"{st.session_state.progress['streak']} days")
    
    st.markdown("---")
    
    st.markdown("### 🏆 Leaderboard")
    
    # Help section for new users
    with st.expander("💡 New to the leaderboard? Learn how to earn points!", expanded=False):
        st.markdown("""
        **How to climb the leaderboard:**
        - 🗣️ **Chat with characters** - Earn 10-50 points per conversation
        - 📚 **Complete lessons** - Get 25-100 points per lesson
        - 🎯 **Pass checkpoints** - Earn bonus 200 points
        - 🔥 **Maintain streaks** - Daily bonus points
        - ✅ **High accuracy** - Bonus points for correct answers
        
        **Tip:** Start with character conversations in the Chat section - they're fun and give you quick points to get on the board!
        """)
        
        if st.button("🚀 Start Chatting to Earn Points", use_container_width=True):
            st.session_state.selected_nav = 2  # Characters page index
            st.rerun()
    
    st.markdown("---")
    
    # Create leaderboard data
    leaderboard_data = [
        {"name": "You", "points": st.session_state.progress['total_points'], "conversations": len(st.session_state.character_conversations), "is_user": True},
        {"name": "Emma Rodriguez", "points": 1250, "conversations": 45, "is_user": False},
        {"name": "Alex Chen", "points": 1180, "conversations": 38, "is_user": False},
        {"name": "Sofia Martinez", "points": 950, "conversations": 32, "is_user": False},
        {"name": "David Kim", "points": 890, "conversations": 28, "is_user": False},
        {"name": "Maya Patel", "points": 820, "conversations": 25, "is_user": False}
    ]
    
    # Sort by points
    leaderboard_data.sort(key=lambda x: x['points'], reverse=True)
    
    # Display leaderboard
    for i, player in enumerate(leaderboard_data):
        rank = i + 1
        if rank == 1:
            medal = "🥇"
        elif rank == 2:
            medal = "🥈"
        elif rank == 3:
            medal = "🥉"
        else:
            medal = f"#{rank}"
        
        bg_color = "linear-gradient(135deg, #e91e63, #f06292)" if player['is_user'] else "white"
        text_color = "white" if player['is_user'] else "#333333"
        border_color = "#e91e63" if player['is_user'] else "#e1bee7"
        
        st.markdown(f"""
        <div style='background: {bg_color}; 
                    color: {text_color}; 
                    padding: 15px 20px; 
                    border-radius: 12px; 
                    margin: 8px 0; 
                    border: 2px solid {border_color};
                    display: flex; 
                    justify-content: space-between; 
                    align-items: center;
                    box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1);'>
            <div style='display: flex; align-items: center; gap: 15px;'>
                <span style='font-size: 24px; font-weight: bold;'>{medal}</span>
                <span style='font-size: 18px; font-weight: 600;'>{player['name']}</span>
            </div>
            <div style='text-align: right;'>
                <div style='font-size: 20px; font-weight: bold;'>{player['points']} pts</div>
                <div style='font-size: 14px; opacity: 0.8;'>{player['conversations']} conversations</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# CITY ROADMAP PAGE
elif page == "🗺️ City Roadmap" and not st.session_state.show_learning:
    st.markdown("## 🗺️ City Roadmap")
    st.markdown("<div style='text-align: center; margin: 20px 0;'><h3 style='color: #e91e63;'>District Alpha: Everyday Conversations</h3><p>Master essential phrases, greetings, and basic interactions. Build your foundational vocabulary and confidence.</p></div>", unsafe_allow_html=True)
    
    # Define levels
    levels = [
        {"id": 1, "name": "Alphabets", "type": "subtopic", "desc": "Learn the alphabet and pronunciation"},
        {"id": 2, "name": "Numbers", "type": "subtopic", "desc": "Master numbers 1-100 and counting"},
        {"id": 3, "name": "Grammar", "type": "subtopic", "desc": "Basic grammar rules and sentence structure"},
        {"id": 4, "name": "Adjectives", "type": "subtopic", "desc": "Descriptive words and their usage"},
        {"id": 5, "name": "Checkpoint", "type": "checkpoint", "desc": "Test your knowledge of all previous topics", "reward": {"points": 200, "character": "Maria"}}
    ]
    
    # Create map layout
    
    
    # Display levels in a path-like layout
    for i, level in enumerate(levels):
        is_completed = level['id'] in st.session_state.completed_levels
        is_current = level['id'] == st.session_state.current_level
        is_locked = level['id'] > st.session_state.current_level
        
        # Determine colors and status
        if is_completed:
            color = "#4CAF50"  # Green
            icon = "✓"
            status = "Completed"
        elif is_current:
            color = "#e91e63" if level['type'] == 'checkpoint' else "#4CAF50"  # Pink for checkpoint, green for current
            icon = str(level['id'])
            status = "Available"
        else:
            color = "#CCCCCC"  # Gray
            icon = "🔒"
            status = "Locked"
        
        # Create level button
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Level circle
            circle_size = "80px" if level['type'] == 'checkpoint' else "60px"
            st.markdown(f"""
            <div style='text-align: center; margin: 20px 0;'>
                <div style='width: {circle_size}; height: {circle_size}; border-radius: 50%; background: {color}; color: white; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: 0 auto; cursor: pointer; box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3);'>
                    {icon}
                </div>
                <h4 style='color: #333; margin: 10px 0 5px 0;'>{level['name']}</h4>
                <p style='color: #666; font-size: 14px; margin: 0;'>{level['desc']}</p>
                <p style='color: {color}; font-size: 12px; margin: 5px 0;'>{status}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Level button
            if not is_locked:
                button_text = 'Start' if not is_completed else 'Redo'
                if st.button(f"{button_text} {level['name']}", key=f"level_{level['id']}", use_container_width=True):
                    if level['type'] == 'checkpoint':
                        # Navigate to checkpoint assessment page
                        st.session_state.current_page = "🎯 Checkpoint Assessment"
                        st.rerun()
                    else:
                        # Redirect to learning page with specific topic
                        st.session_state.selected_topic = level['name']
                        st.session_state.show_learning = True
                        st.rerun()
            else:
                st.button(f"🔒 {level['name']}", disabled=True, use_container_width=True)
        
        # Add connecting line (except for last level)
        if i < len(levels) - 1:
            st.markdown("<div style='text-align: center; color: #CCCCCC; font-size: 20px; margin: 10px 0;'>↓</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Progress summary
    completed_count = len(st.session_state.completed_levels)
    total_count = len(levels)
    progress_percent = (completed_count / total_count) * 100
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #e91e63, #f06292); color: white; padding: 20px; border-radius: 15px; margin: 20px 0; text-align: center;'>
        <h3>Your Progress</h3>
        <p>{completed_count}/{total_count} levels completed ({progress_percent:.0f}%)</p>
        <div style='background: rgba(255,255,255,0.3); border-radius: 10px; height: 10px; margin: 10px 0;'>
            <div style='background: white; height: 10px; border-radius: 10px; width: {progress_percent}%;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# LEARNING PAGE (when show_learning is True)
if st.session_state.show_learning:
    # Back to roadmap button
    if st.button("← Back to City Roadmap"):
        st.session_state.show_learning = False
        st.session_state.selected_topic = None
        st.rerun()
    
    st.markdown(f"## 📚 Learn {profile['target_lang']} - {st.session_state.selected_topic}")
    
    # Show current difficulty level
    difficulty_names = {1: "Easy", 2: "Medium", 3: "Hard"}
    st.info(f"Current Difficulty: {difficulty_names[st.session_state.progress['difficulty_level']]} | Points: {st.session_state.progress['total_points']}")
    
    theory_tab, practical_tab = st.tabs(["📖 Theory", "🎯 Practical"])
    
    with theory_tab:
        st.markdown("### 📖 Choose Your Learning Topic")
        
        col1, col2 = st.columns([1, 3], gap="large")
        
        with col1:
            topics = [
                "Colors", "Numbers", "Basic Nouns", "Verbs", "Adjectives", 
                "Family Members", "Body Parts", "Food & Drinks", "Animals", 
                "Weather", "Time & Dates", "Greetings", "Directions"
            ]
            # Use selected topic from roadmap or allow manual selection
            if st.session_state.selected_topic:
                selected_topic = st.session_state.selected_topic
                st.info(f"Learning: {selected_topic}")
            else:
                selected_topic = st.selectbox("Select Topic:", topics)
            
            if st.button("📚 Load Theory Content"):
                with col2:
                    difficulty_level = st.session_state.progress['difficulty_level']
                    complexity = ["basic", "intermediate", "advanced"][difficulty_level - 1]
                    
                    prompt = f"""
                    Create {complexity} level {profile['target_lang']} theory content for "{selected_topic}".
                    User speaks {profile['native_lang']}.
                    Learning style: {profile['learning_style']}
                    Difficulty: {complexity}
                    
                    Include:
                    1. Introduction to the topic
                    2. {"5-8" if difficulty_level == 1 else "10-15" if difficulty_level == 2 else "15-20"} key words/phrases with pronunciation guide
                    3. Grammar rules if applicable
                    4. Example sentences with translations
                    5. Cultural notes
                    6. Memory tips
                    
                    Make it detailed and educational for self-study.
                    Separate the native and target language in separate paragraphs or separate lines.
                    """
                    
                    with st.spinner("Loading theory content..."):
                        theory_content = generate_ai_response(prompt)
                        st.write(theory_content)
                        
                        try:
                            audio_file = create_audio(theory_content)
                            if audio_file and os.path.exists(audio_file):
                                st.audio(audio_file)
                        except Exception as e:
                            st.info("Audio generation temporarily unavailable")
    
    with practical_tab:
        st.markdown("### 🎯 Practice Exercises")
        
        # Show checkpoint assessment if selected topic is Checkpoint
        if st.session_state.selected_topic == "Checkpoint":
            # Redirect to checkpoint page
            st.session_state.show_learning = False
            st.session_state.show_checkpoint = True
            st.rerun()
        else:
            exercise_type = st.selectbox("Choose Exercise Type:", 
                                       ["Multiple Choice Quiz", "Fill in the Blanks", "Image Description", "Translation Practice"])
        
        if exercise_type == "Multiple Choice Quiz":
            
            st.markdown("#### 📝 Multiple Choice Quiz")
            
            if st.button("Generate Quiz"):
                # Reset answers display and clear previous questions
                st.session_state.show_mcq_answers = False
                st.session_state.mcq_questions = []
                
                difficulty_level = st.session_state.progress['difficulty_level']
                complexity_desc = {
                    1: "basic vocabulary and simple grammar",
                    2: "intermediate vocabulary and grammar structures", 
                    3: "advanced vocabulary, complex grammar, and cultural nuances"
                }
                
                prompt = f"""
                Create exactly 5 multiple choice questions in {profile['target_lang']} for a {profile['level']} learner.
                Focus specifically on the topic: {selected_topic}
                User speaks {profile['native_lang']}.
                Difficulty: {complexity_desc[difficulty_level]}
                
                For each question, provide:
                1. The question text
                2. Four options (A, B, C, D)
                3. The correct answer letter
                
                Format EXACTLY like this:
                1. [Question text]
                A) [option]
                B) [option]
                C) [option]
                D) [option]
                Correct: [letter]
                
                2. [Question text]
                A) [option]
                B) [option]
                C) [option]
                D) [option]
                Correct: [letter]
                
                Continue for all 5 questions.
                Focus on {selected_topic} and {complexity_desc[difficulty_level]}.
                Mix vocabulary, grammar, and comprehension questions related to {selected_topic}.
                """
                
                quiz_content = generate_ai_response(prompt)
                
                # Parse the content to extract questions, options, and answers
                lines = quiz_content.split('\n')
                questions = []
                current_question = ""
                current_options = []
                current_answer = ""
                
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith(('A)', 'B)', 'C)', 'D)', 'Correct:')):
                        if current_question and current_options and current_answer:
                            questions.append({
                                'question': current_question,
                                'options': current_options.copy(),
                                'correct': current_answer
                            })
                            current_options = []
                        current_question = line
                    elif line.startswith(('A)', 'B)', 'C)', 'D)')):
                        current_options.append(line)
                    elif line.startswith('Correct:'):
                        current_answer = line.replace('Correct:', '').strip()
                
                # Add the last question
                if current_question and current_options and current_answer:
                    questions.append({
                        'question': current_question,
                        'options': current_options.copy(),
                        'correct': current_answer
                    })
                
                # Store questions in session state
                st.session_state.mcq_questions = questions
            
            # Display questions if they exist
            if st.session_state.mcq_questions:
                st.markdown("### Choose the correct answer:")
                
                user_answers = []
                for i, q in enumerate(st.session_state.mcq_questions[:5]):
                    st.markdown(f'<div class="mcq-question">{q["question"]}</div>', unsafe_allow_html=True)
                    
                    # Create radio button options
                    options = q["options"]
                    selected_option = st.radio(
                        f"Question {i+1}:",
                        options,
                        key=f"mcq_{i}",
                        label_visibility="collapsed"
                    )
                    user_answers.append(selected_option)
                    
                    # Show correct/wrong answer if answers are being displayed
                    if st.session_state.show_mcq_answers:
                        selected_letter = selected_option[0] if selected_option else ""
                        correct_letter = q["correct"]
                        
                        if selected_letter == correct_letter:
                            st.markdown(f'<div class="correct-answer">✅ Correct! Answer: {correct_letter}) {selected_option[3:]}</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="wrong-answer">❌ Your answer: {selected_letter})</div>', unsafe_allow_html=True)
                            # Find correct option text
                            correct_option = next((opt for opt in options if opt.startswith(correct_letter)), "")
                            st.markdown(f'<div class="correct-answer">✅ Correct Answer: {correct_option}</div>', unsafe_allow_html=True)
                    
                    st.markdown("---")
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Check All Answers"):
                        # Calculate correct answers
                        correct_count = 0
                        for i, q in enumerate(st.session_state.mcq_questions[:5]):
                            if i < len(user_answers) and user_answers[i]:
                                selected_letter = user_answers[i][0]
                                if selected_letter == q["correct"]:
                                    correct_count += 1
                        
                        # Award points based on performance
                        points_earned = award_points(correct_count, 5)
                        
                        # Mark exercise as completed
                        if selected_topic not in st.session_state.completed_exercises:
                            st.session_state.completed_exercises[selected_topic] = []
                        if "MCQ" not in st.session_state.completed_exercises[selected_topic]:
                            st.session_state.completed_exercises[selected_topic].append("MCQ")
                        save_profile_to_file()
                        
                        st.session_state.show_mcq_answers = True
                        st.markdown(f'<div class="points-earned">🏆 You got {correct_count}/5 correct! +{points_earned} points earned!</div>', unsafe_allow_html=True)
                        
                        if correct_count >= 4:
                            st.balloons()
                            st.success("Excellent work! 🌟")
                        elif correct_count >= 3:
                            st.success("Good job! Keep practicing! 👍")
                        else:
                            st.info("Keep trying! Practice makes perfect! 💪")
                        
                        st.rerun()  # Refresh to show answers
                
                with col2:
                    completed_count = len(st.session_state.completed_exercises.get(selected_topic, []))
                    if st.button("✨ Complete Topic"):
                        if completed_count >= 2:
                            # Complete the level
                            current_level_id = None
                            levels = [
                                {"id": 1, "name": "Alphabets"},
                                {"id": 2, "name": "Numbers"},
                                {"id": 3, "name": "Grammar"},
                                {"id": 4, "name": "Adjectives"},
                                {"id": 5, "name": "Checkpoint"}
                            ]
                            for level in levels:
                                if level["name"] == selected_topic:
                                    current_level_id = level["id"]
                                    break
                            
                            if current_level_id and current_level_id not in st.session_state.completed_levels:
                                st.session_state.completed_levels.append(current_level_id)
                                st.session_state.current_level = min(5, current_level_id + 1)
                                st.session_state.progress['total_points'] += 50
                                save_profile_to_file()
                                st.success(f"Level {current_level_id} completed! +50 points earned!")
                                st.balloons()
                            
                            # Return to roadmap
                            st.session_state.show_learning = False
                            st.session_state.selected_topic = None
                            st.rerun()
                        else:
                            st.warning(f"Complete at least 2 exercise types first! ({completed_count}/2 completed)")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif exercise_type == "Fill in the Blanks":

            st.markdown("#### ✏️ Fill in the Blanks")
            
            if st.button("Generate Exercise"):
                # Reset answers display and clear previous questions
                st.session_state.show_answers = False
                st.session_state.fill_blank_questions = []
                
                difficulty_level = st.session_state.progress['difficulty_level']
                complexity_desc = {
                    1: "simple vocabulary and basic sentence structures",
                    2: "intermediate vocabulary and more complex grammar",
                    3: "advanced vocabulary, complex grammar, and idiomatic expressions"
                }
                
                prompt = f"""
                Create exactly 5 fill-in-the-blank sentences in {profile['target_lang']}.
                Focus specifically on the topic: {selected_topic}
                User speaks {profile['native_lang']}.
                Level: {profile['level']}
                Difficulty: {complexity_desc[difficulty_level]}
                
                For each sentence, provide:
                1. The sentence with ONE blank (_____)
                2. The translation in {profile['native_lang']}
                3. The correct answer (the word that goes in the blank)
                
                Format EXACTLY like this:
                1. [Sentence with _____ for missing word]
                Translation: [translation]
                Answer: [correct word]
                
                2. [Sentence with _____ for missing word]
                Translation: [translation]
                Answer: [correct word]
                
                Continue for all 5 sentences.
                Focus on {selected_topic} and {complexity_desc[difficulty_level]}.
                """
                
                exercise_content = generate_ai_response(prompt)
                
                # Parse the content to extract sentences, translations, and answers
                lines = exercise_content.split('\n')
                questions = []
                current_sentence = ""
                current_translation = ""
                current_answer = ""
                
                for line in lines:
                    line = line.strip()
                    if line and '_____' in line and not line.startswith('Translation:') and not line.startswith('Answer:'):
                        current_sentence = line
                    elif line.startswith('Translation:'):
                        current_translation = line.replace('Translation:', '').strip()
                    elif line.startswith('Answer:'):
                        current_answer = line.replace('Answer:', '').strip()
                        if current_sentence and current_translation and current_answer:
                            questions.append({
                                'sentence': current_sentence,
                                'translation': current_translation,
                                'answer': current_answer
                            })
                            current_sentence = ""
                            current_translation = ""
                            current_answer = ""
                
                # Store questions in session state
                st.session_state.fill_blank_questions = questions
            
            # Display questions if they exist
            if st.session_state.fill_blank_questions:
                st.markdown("### Complete the sentences:")
                
                answers = []
                for i, q in enumerate(st.session_state.fill_blank_questions[:5]):
                    st.markdown(f'<div class="fill-blank-sentence">{q["sentence"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="fill-blank-translation">Translation: {q["translation"]}</div>', unsafe_allow_html=True)
                    
                    answer = st.text_input(f"Your answer for question {i+1}:", key=f"answer_{i}", placeholder="Type your answer here...")
                    answers.append(answer)
                    
                    # Show correct/wrong answer if answers are being displayed
                    if st.session_state.show_answers:
                        user_answer = answer.strip().lower()
                        correct_answer = q["answer"].strip().lower()
                        
                        if user_answer == correct_answer:
                            st.markdown(f'<div class="correct-answer">✅ Correct! Answer: {q["answer"]}</div>', unsafe_allow_html=True)
                        elif user_answer:
                            st.markdown(f'<div class="wrong-answer">❌ Your answer: {answer}</div>', unsafe_allow_html=True)
                            st.markdown(f'<div class="correct-answer">✅ Correct Answer: {q["answer"]}</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="correct-answer">✅ Correct Answer: {q["answer"]}</div>', unsafe_allow_html=True)
                    
                    st.markdown("---")
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Check All Answers"):
                        filled_answers = [a for a in answers if a.strip()]
                        if len(filled_answers) >= 3:
                            # Calculate correct answers
                            correct_count = 0
                            for i, q in enumerate(st.session_state.fill_blank_questions[:5]):
                                if i < len(answers) and answers[i].strip().lower() == q["answer"].strip().lower():
                                    correct_count += 1
                            
                            # Award points based on performance
                            points_earned = award_points(correct_count, 5)
                            
                            # Mark exercise as completed
                            if selected_topic not in st.session_state.completed_exercises:
                                st.session_state.completed_exercises[selected_topic] = []
                            if "Fill Blanks" not in st.session_state.completed_exercises[selected_topic]:
                                st.session_state.completed_exercises[selected_topic].append("Fill Blanks")
                            save_profile_to_file()
                            
                            st.session_state.show_answers = True
                            st.markdown(f'<div class="points-earned">🏆 You got {correct_count}/5 correct! +{points_earned} points earned!</div>', unsafe_allow_html=True)
                            
                            if correct_count >= 4:
                                st.balloons()
                                st.success("Excellent work! 🌟")
                            elif correct_count >= 3:
                                st.success("Good job! Keep practicing! 👍")
                            else:
                                st.info("Keep trying! Practice makes perfect! 💪")
                            
                            st.rerun()  # Refresh to show answers
                        else:
                            st.info("Try to answer at least 3 questions before checking!")
                
                with col2:
                    completed_count = len(st.session_state.completed_exercises.get(selected_topic, []))
                    if st.button("✨ Complete Topic", key="complete_fill"):
                        if completed_count >= 2:
                            # Complete the level
                            current_level_id = None
                            levels = [
                                {"id": 1, "name": "Alphabets"},
                                {"id": 2, "name": "Numbers"},
                                {"id": 3, "name": "Grammar"},
                                {"id": 4, "name": "Adjectives"},
                                {"id": 5, "name": "Checkpoint"}
                            ]
                            for level in levels:
                                if level["name"] == selected_topic:
                                    current_level_id = level["id"]
                                    break
                            
                            if current_level_id and current_level_id not in st.session_state.completed_levels:
                                st.session_state.completed_levels.append(current_level_id)
                                st.session_state.current_level = min(5, current_level_id + 1)
                                st.session_state.progress['total_points'] += 50
                                save_profile_to_file()
                                st.success(f"Level {current_level_id} completed! +50 points earned!")
                                st.balloons()
                            
                            # Return to roadmap
                            st.session_state.show_learning = False
                            st.session_state.selected_topic = None
                            st.rerun()
                        else:
                            st.warning(f"Complete at least 2 exercise types first! ({completed_count}/2 completed)")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif exercise_type == "Image Description":
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.markdown(f"#### 🖼️ Image Description Exercise - {selected_topic}")
            
            # Topic-specific images
            topic_images = {
                "Alphabets": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=300",
                "Numbers": "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=300", 
                "Grammar": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=300",
                "Adjectives": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300"
            }
            image_url = topic_images.get(selected_topic, "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=300")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.image(image_url, caption=f"Describe this image using {selected_topic}", width=300)
            
            with col2:
                st.markdown(f"**Describe this image in {profile['target_lang']} focusing on {selected_topic}:**")
                description = st.text_area("Your description:", height=150)
                
                if st.button("Get AI Feedback") and description:
                    prompt = f"""
                    The user is learning {profile['target_lang']} at {profile['level']} level.
                    They are focusing on the topic: {selected_topic}
                    They described an image in {profile['target_lang']} as: "{description}"
                    
                    Please provide helpful feedback specifically related to {selected_topic}:
                    1. What they did well
                    2. Any grammar or vocabulary corrections needed
                    3. Suggestions for better expressions related to {selected_topic}
                    4. A model description they can learn from
                    
                    Be encouraging and educational. Focus on helping them improve their use of {selected_topic}.
                    """
                    
                    feedback = generate_ai_response(prompt)
                    st.write("**AI Feedback:**")
                    st.write(feedback)
            
            st.markdown('</div>', unsafe_allow_html=True)

# CHECKPOINT ASSESSMENT PAGE
elif page == "🎯 Checkpoint Assessment":
    
    st.markdown("## 🎯 Checkpoint Assessment")
    st.info("Complete this comprehensive test covering all previous topics: Alphabets, Numbers, Grammar, and Adjectives")
    st.warning("You need to score at least 7/10 (70%) to pass and unlock rewards!")
    
    if st.button("Start Checkpoint Assessment", use_container_width=True):
        # Generate comprehensive checkpoint quiz
        st.session_state.show_mcq_answers = False
        st.session_state.mcq_questions = []
        
        difficulty_level = st.session_state.progress['difficulty_level']
        complexity_desc = {
            1: "basic vocabulary and simple grammar",
            2: "intermediate vocabulary and grammar structures", 
            3: "advanced vocabulary, complex grammar, and cultural nuances"
        }
        
        prompt = f"""
        Create exactly 10 comprehensive multiple choice questions in {profile['target_lang']} for a {profile['level']} learner.
        This is a CHECKPOINT ASSESSMENT covering ALL these topics: Alphabets, Numbers, Grammar, and Adjectives
        User speaks {profile['native_lang']}.
        Difficulty: {complexity_desc[difficulty_level]}
        
        Create 2-3 questions for each topic:
        - Alphabets: pronunciation, letter recognition, alphabetical order
        - Numbers: counting, number words, basic math
        - Grammar: sentence structure, verb forms, basic rules
        - Adjectives: descriptive words, comparisons, usage
        
        For each question, provide:
        1. The question text
        2. Four options (A, B, C, D)
        3. The correct answer letter
        
        Format EXACTLY like this:
        1. [Question text]
        A) [option]
        B) [option]
        C) [option]
        D) [option]
        Correct: [letter]
        
        Continue for all 10 questions.
        Mix all four topics throughout the assessment.
        """
        
        quiz_content = generate_ai_response(prompt)
        
        # Parse the content to extract questions, options, and answers
        lines = quiz_content.split('\n')
        questions = []
        current_question = ""
        current_options = []
        current_answer = ""
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith(('A)', 'B)', 'C)', 'D)', 'Correct:')):
                if current_question and current_options and current_answer:
                    questions.append({
                        'question': current_question,
                        'options': current_options.copy(),
                        'correct': current_answer
                    })
                    current_options = []
                current_question = line
            elif line.startswith(('A)', 'B)', 'C)', 'D)')):
                current_options.append(line)
            elif line.startswith('Correct:'):
                current_answer = line.replace('Correct:', '').strip()
        
        # Add the last question
        if current_question and current_options and current_answer:
            questions.append({
                'question': current_question,
                'options': current_options.copy(),
                'correct': current_answer
            })
        
        # Store questions in session state
        st.session_state.mcq_questions = questions
        st.rerun()
    
    # Display checkpoint assessment if questions exist
    if st.session_state.mcq_questions:
        st.markdown("### 🎯 Answer all 10 questions:")
        
        user_answers = []
        for i, q in enumerate(st.session_state.mcq_questions[:10]):
            st.markdown(f'<div class="mcq-question">{i+1}. {q["question"]}</div>', unsafe_allow_html=True)
            
            # Create radio button options
            options = q["options"]
            selected_option = st.radio(
                f"Question {i+1}:",
                options,
                key=f"checkpoint_{i}",
                label_visibility="collapsed"
            )
            user_answers.append(selected_option)
            
            # Show correct/wrong answer if answers are being displayed
            if st.session_state.show_mcq_answers:
                selected_letter = selected_option[0] if selected_option else ""
                correct_letter = q["correct"]
                
                if selected_letter == correct_letter:
                    st.markdown(f'<div class="correct-answer">✅ Correct! Answer: {correct_letter}) {selected_option[3:]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="wrong-answer">❌ Your answer: {selected_letter})</div>', unsafe_allow_html=True)
                    # Find correct option text
                    correct_option = next((opt for opt in options if opt.startswith(correct_letter)), "")
                    st.markdown(f'<div class="correct-answer">✅ Correct Answer: {correct_option}</div>', unsafe_allow_html=True)
            
            st.markdown("---")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Check Answers", use_container_width=True):
                st.session_state.show_mcq_answers = True
                st.rerun()
        
        with col2:
            if st.button("Submit Assessment", use_container_width=True):
                # Calculate correct answers
                correct_count = 0
                for i, q in enumerate(st.session_state.mcq_questions[:10]):
                    if i < len(user_answers) and user_answers[i]:
                        selected_letter = user_answers[i][0]
                        if selected_letter == q["correct"]:
                            correct_count += 1
                
                # Award points and rewards based on performance
                if correct_count >= 7:  # 70% pass rate
                    points_earned = 200
                    st.session_state.progress['total_points'] += points_earned
                    
                    # Award Maria character
                    if "Maria" not in st.session_state.purchased_characters:
                        st.session_state.purchased_characters.append("Maria")
                        st.session_state.character_relationships["Maria"] = 0
                    
                    # Complete the checkpoint level
                    if 5 not in st.session_state.completed_levels:
                        st.session_state.completed_levels.append(5)
                        st.session_state.current_level = 6
                    
                    save_profile_to_file()
                    
                    st.session_state.show_mcq_answers = True
                    st.balloons()
                    st.success(f"🎉 Checkpoint Passed! You got {correct_count}/10 correct!")
                    st.success(f"🏆 Rewards: +{points_earned} Lumie Dollars + Maria character unlocked!")
                    
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("Redo Assessment"):
                            st.session_state.mcq_questions = []
                            st.session_state.show_mcq_answers = False
                            # Keep current_page set to maintain sidebar
                            st.rerun()
                    with col2:
                        if st.button("Back to Roadmap"):
                            st.session_state.current_page = "🗺️ City Roadmap"
                            st.session_state.mcq_questions = []
                            st.session_state.show_mcq_answers = False
                            st.rerun()
                else:
                    st.session_state.show_mcq_answers = True
                    st.error(f"❌ Checkpoint Failed. You got {correct_count}/10 correct. You need at least 7/10 to pass.")
                    st.info("Review the topics and try again!")
                    
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("Try Again"):
                            st.session_state.mcq_questions = []
                            st.session_state.show_mcq_answers = False
                            # Keep current_page set to maintain sidebar
                            st.rerun()
                    with col2:
                        if st.button("Back to Roadmap"):
                            st.session_state.current_page = "🗺️ City Roadmap"
                            st.session_state.mcq_questions = []
                            st.session_state.show_mcq_answers = False
                            st.rerun()

# CHARACTERS PAGE
elif page == "👥 Characters" and not st.session_state.show_chat:
    st.markdown("<div style='text-align: center; margin: 50px 0;'><h1 style='color: #e91e63; font-size: 48px;'>Your Learning Companions</h1></div>", unsafe_allow_html=True)
    
    # Get owned characters
    owned_characters = st.session_state.purchased_characters
    
    if not owned_characters:
        st.markdown("<div style='text-align: center; margin: 50px 0;'><h2>No Characters Unlocked</h2><p>Visit the Lumie Shop to unlock your first character!</p></div>", unsafe_allow_html=True)
        if st.button("🛒 Go to Lumie Shop", use_container_width=True):
            st.switch_page("🛒 Lumie Shop")
    else:
        companions = [
            {"name": "Jake", "title": "The Barista", "desc": "Jake is your go-to for casual chats over coffee. He teaches you conversational Spanish with a smile and a warm latte.", "emoji": "☕", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face"},
            {"name": "Professor Anya", "title": "The Historian", "desc": "Professor Anya unravels the rich history of French culture and language. Engage in thought-provoking discussions and refine your academic French.", "emoji": "📚", "image": "https://images.unsplash.com/photo-1494790108755-2616c27b1e2d?w=300&h=300&fit=crop&crop=face"},
            {"name": "Kaito", "title": "The Chef", "desc": "Kaito brings the world of Japanese cuisine to life. Learn essential phrases for cooking, dining, and navigating Japanese food culture with authentic recipes and stories.", "emoji": "🍣", "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=300&fit=crop&crop=face"},
            {"name": "Maria", "title": "The Artist", "desc": "Maria brings creativity to language learning through art and culture. Perfect for learning Spanish through creative expression.", "emoji": "🎨", "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&h=300&fit=crop&crop=face"},
            {"name": "Hans", "title": "The Engineer", "desc": "Hans makes German learning systematic and logical. Great for technical vocabulary and precise grammar.", "emoji": "🔧", "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&h=300&fit=crop&crop=face"},
            {"name": "Sophie", "title": "The Fashion Designer", "desc": "Sophie teaches French through the lens of fashion and elegance. Perfect for cultural immersion.", "emoji": "👗", "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&h=300&fit=crop&crop=face"}
        ]
        
        # Filter to show only owned characters
        owned_companion_data = [c for c in companions if c['name'] in owned_characters]
        
        # Display owned characters in a grid
        for i in range(0, len(owned_companion_data), 3):
            cols = st.columns(3, gap="large")
            for j, companion in enumerate(owned_companion_data[i:i+3]):
                with cols[j]:
                    st.markdown(f"""
                    <div style='background: white; padding: 30px; border-radius: 20px; text-align: center; box-shadow: 0 8px 25px rgba(233, 30, 99, 0.15); margin: 20px 0;'>
                        <img src='{companion['image']}' style='width: 120px; height: 120px; border-radius: 50%; margin-bottom: 20px; object-fit: cover;'>
                        <h3 style='color: #333; margin-bottom: 10px;'>{companion['name']} {companion['emoji']}</h3>
                        <p style='color: #e91e63; font-weight: 600; margin-bottom: 15px;'>{companion['title']}</p>
                        <p style='color: #666; font-size: 14px; line-height: 1.5; margin-bottom: 25px;'>{companion['desc']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("Chat Now", key=f"chat_{companion['name']}"):
                        st.session_state.selected_companion = companion
                        # Load character-specific conversation
                        if companion['name'] in st.session_state.character_conversations:
                            st.session_state.chat_history = st.session_state.character_conversations[companion['name']]
                            st.session_state.conversation_started = True
                        else:
                            st.session_state.chat_history = []
                            st.session_state.conversation_started = False
                        # Switch to chat view
                        st.session_state.show_chat = True
                        st.rerun()

# CHAT PAGE (when show_chat is True)
if st.session_state.show_chat and st.session_state.selected_companion:
    # Show chat interface
    companion = st.session_state.selected_companion
    
    # Back button
    if st.button("← Back to Characters"):
        st.session_state.show_chat = False
        st.rerun()
    
    # Header with companion info and relationship bar
    relationship_level, relationship_status = get_relationship_level(companion['name'])
    
    st.markdown(f"""
    <div style='display: flex; align-items: center; margin-bottom: 20px;'>
        <img src='{companion.get('image', '')}' style='width: 60px; height: 60px; border-radius: 50%; margin-right: 20px; object-fit: cover;'>
        <div style='flex: 1;'>
            <h2 style='color: #333; margin: 0;'>{companion['name']} {companion['emoji']}</h2>
            <p style='color: #e91e63; margin: 0;'>{companion['title']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Relationship bar
    st.markdown(f"""
    <div style='margin-bottom: 20px;'>
        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;'>
            <span style='font-weight: 600; color: #333;'>Relationship: {relationship_status}</span>
            <span style='font-size: 14px; color: #666;'>{relationship_level}%</span>
        </div>
        <div style='background: #f0f0f0; border-radius: 10px; height: 8px;'>
            <div style='background: linear-gradient(135deg, #e91e63, #f06292); height: 8px; border-radius: 10px; width: {relationship_level}%;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize conversation if not started
    if not st.session_state.conversation_started:
        relationship_level, relationship_status = get_relationship_level(companion['name'])
        
        greeting_prompt = f"""
        You are {companion['name']}, {companion['title']}. Send a SHORT greeting message like WhatsApp (1-2 sentences).
        The user is learning {profile['target_lang']} and speaks {profile['native_lang']}.
        Their level is {profile['level']}.
        
        Your relationship with the user is: {relationship_status} ({relationship_level}%)
        Adjust your tone and familiarity based on this relationship level:
        - Stranger (0-4%): Formal, polite, distant
        - Acquaintance (5-14%): Friendly but reserved
        - Friend (15-29%): Warm, casual, supportive
        - Close Friend (30-49%): Very friendly, personal topics
        - Best Friend (50-69%): Intimate, caring, playful
        - Soulmate (70-100%): Deeply connected, romantic undertones
        
        Format your greeting EXACTLY like this:
        
        {profile['target_lang']}: [your greeting in target language]
        English: [translation in English]
        
        Do NOT include any HTML tags, div tags, or special formatting. Just plain text.
        """
        
        greeting = generate_ai_response(greeting_prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": greeting})
        st.session_state.conversation_started = True
    
    # Reset clear_input flag after rerun
    if st.session_state.clear_input:
        st.session_state.clear_input = False
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat history as individual bubbles
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                # User message - pink bubble on right
                st.markdown(f"""
                <div style='display: flex; justify-content: flex-end; margin: 10px 0;'>
                    <div style='background: linear-gradient(135deg, #ff69b4, #ff1493); color: white; padding: 12px 18px; border-radius: 18px; max-width: 70%; font-size: 14px; word-wrap: break-word;'>
                        {message['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # AI message - gray bubble on left with proper formatting
                formatted_content = format_chat_message(message['content'])
                st.markdown(f"""
                <div style='display: flex; justify-content: flex-start; margin: 10px 0;'>
                    <div style='background: #f0f0f0; color: #333; padding: 12px 18px; border-radius: 18px; max-width: 70%; font-size: 14px; word-wrap: break-word; line-height: 1.5;'>
                        {formatted_content}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add audio player for AI messages
                try:
                    character_voices = {
                        'Jake': 'Matthew',
                        'Professor Anya': 'Amy', 
                        'Kaito': 'Takumi',
                        'Maria': 'Lupe',
                        'Hans': 'Hans',
                        'Sophie': 'Celine'
                    }
                    voice_id = character_voices.get(companion['name'], 'Joanna')
                    audio_file = create_audio_polly(message['content'], voice_id)
                    if audio_file and os.path.exists(audio_file):
                        st.audio(audio_file)
                except Exception as e:
                    # Fallback to regular TTS if Polly fails
                    try:
                        audio_file = create_audio(message['content'])
                        if audio_file and os.path.exists(audio_file):
                            st.audio(audio_file)
                    except:
                        pass  # Skip audio if both fail
    
    # Input area at bottom
    st.markdown("---")
    
    # Voice recording component using browser speech recognition
    audio_html = f"""
    <div style="margin-bottom: 10px;">
        <button id="voiceBtn" onclick="toggleVoice()" style="background: linear-gradient(135deg, #e91e63, #f06292); color: white; border: none; border-radius: 25px; padding: 10px 20px; cursor: pointer;">🎤 Voice Input</button>
        <span id="status" style="margin-left: 10px; color: #666;"></span>
    </div>
    <script>
        let recognition;
        let isListening = false;
        
        if ('webkitSpeechRecognition' in window) {{
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            
            recognition.onstart = function() {{
                isListening = true;
                document.getElementById('voiceBtn').textContent = '⏹️ Stop Listening';
                document.getElementById('status').textContent = 'Listening...';
            }};
            
            recognition.onresult = function(event) {{
                const transcript = event.results[0][0].transcript;
                document.getElementById('status').textContent = 'Sending: ' + transcript;
                
                // Find and fill the input, then click send
                setTimeout(() => {{
                    const textInputs = window.parent.document.querySelectorAll('input[type="text"]');
                    const sendButtons = window.parent.document.querySelectorAll('button');
                    
                    // Fill the last text input (should be chat input)
                    if (textInputs.length > 0) {{
                        const chatInput = textInputs[textInputs.length - 1];
                        chatInput.value = transcript;
                        chatInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
                        chatInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        
                        // Find and click Send button
                        sendButtons.forEach(btn => {{
                            if (btn.textContent.includes('Send')) {{
                                setTimeout(() => btn.click(), 500);
                            }}
                        }});
                    }}
                }}, 200);
            }};
            
            recognition.onend = function() {{
                isListening = false;
                document.getElementById('voiceBtn').textContent = '🎤 Voice Input';
            }};
            
            recognition.onerror = function(event) {{
                document.getElementById('status').textContent = 'Error: ' + event.error;
                isListening = false;
                document.getElementById('voiceBtn').textContent = '🎤 Voice Input';
            }};
        }} else {{
            document.getElementById('status').textContent = 'Speech recognition not supported';
        }}
        
        function toggleVoice() {{
            if (!recognition) return;
            
            if (!isListening) {{
                recognition.start();
            }} else {{
                recognition.stop();
            }}
        }}
    </script>
    """
    
    components.html(audio_html, height=60)
    
    col1, col2 = st.columns([5, 1])
    
    # Check for voice input
    if st.session_state.voice_input:
        current_input = st.session_state.voice_input
        st.session_state.voice_input = ""  # Clear after use
    else:
        current_input = "" if st.session_state.clear_input else st.session_state.get('chat_input', '')
    
    with col1:
        user_input = st.text_input(
            "Message", 
            placeholder="Type your message here or use voice recording above...", 
            value=current_input,
            label_visibility="collapsed",
            key="chat_input"
        )
    
    with col2:
        send_button = st.button("Send", use_container_width=True)
    
    # Handle message sending
    if send_button and user_input.strip():
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        
        # Increase relationship level
        increase_relationship(companion['name'])
        relationship_level, relationship_status = get_relationship_level(companion['name'])
        
        # Generate AI response - keep it short like WhatsApp
        response_prompt = f"""
        You are {companion['name']}, {companion['title']}. Keep responses short and conversational like WhatsApp messages.
        The user is learning {profile['target_lang']} and speaks {profile['native_lang']}.
        Their level is {profile['level']}.
        
        Your relationship with the user is: {relationship_status} ({relationship_level}%)
        Adjust your tone and familiarity based on this relationship level:
        - Stranger (0-4%): Formal, polite, distant
        - Acquaintance (5-14%): Friendly but reserved
        - Friend (15-29%): Warm, casual, supportive
        - Close Friend (30-49%): Very friendly, personal topics
        - Best Friend (50-69%): Intimate, caring, playful
        - Soulmate (70-100%): Deeply connected, romantic undertones
        
        User just said: "{user_input}"
        
        Respond with a SHORT message (1-2 sentences max) as {companion['name']}:
        1. Stay in character
        2. Keep it conversational and brief
        3. Match the relationship level in your tone
        4. Format your response EXACTLY like this:
        
        {profile['target_lang']}: [your message in target language]
        English: [translation in English]
        
        Do NOT include any HTML tags, div tags, or special formatting. Just plain text.
        """
        
        ai_response = generate_ai_response(response_prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        
        # Generate audio for AI response using Polly with character-specific voice
        try:
            character_voices = {
                'Jake': 'Matthew',
                'Professor Anya': 'Amy', 
                'Kaito': 'Takumi',
                'Maria': 'Lupe',
                'Hans': 'Hans',
                'Sophie': 'Celine'
            }
            voice_id = character_voices.get(companion['name'], 'Joanna')
            audio_file = create_audio_polly(ai_response, voice_id)
            if audio_file and os.path.exists(audio_file):
                st.audio(audio_file, autoplay=True)
        except Exception as e:
            # Fallback to regular TTS if Polly fails
            try:
                audio_file = create_audio(ai_response)
                if audio_file and os.path.exists(audio_file):
                    st.audio(audio_file, autoplay=True)
            except:
                pass  # Skip audio if both fail
        
        # Save conversation for this character
        st.session_state.character_conversations[companion['name']] = st.session_state.chat_history
        save_profile_to_file()
        
        # Clear input and rerun
        st.session_state.clear_input = True
        st.rerun()
    




# LUMIE SHOP PAGE
elif page == "🛒 Lumie Shop":
    st.markdown("## 🛒 Lumie Shop")
    
    # Balance display
    st.markdown(f"<div style='text-align: center; background: linear-gradient(135deg, #e91e63, #f06292); color: white; padding: 20px; border-radius: 15px; margin: 20px 0;'><h2>Your Balance: {st.session_state.progress['total_points']} Lumie Dollars</h2></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("### 👥 Character Store")
        
        # Available characters for purchase
        purchasable_characters = [
            {"name": "Maria", "title": "The Artist", "cost": 150, "desc": "Learn Spanish through art and creativity", "emoji": "🎨", "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&h=300&fit=crop&crop=face"},
            {"name": "Hans", "title": "The Engineer", "cost": 200, "desc": "Master German with systematic precision", "emoji": "🔧", "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&h=300&fit=crop&crop=face"},
            {"name": "Sophie", "title": "The Fashion Designer", "cost": 250, "desc": "Learn French through fashion and elegance", "emoji": "👗", "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&h=300&fit=crop&crop=face"},
            {"name": "Chen", "title": "The Tech Guru", "cost": 300, "desc": "Learn Chinese through technology and innovation", "emoji": "💻", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face"},
            {"name": "Isabella", "title": "The Travel Blogger", "cost": 180, "desc": "Explore Italian through travel stories", "emoji": "✈️", "image": "https://images.unsplash.com/photo-1494790108755-2616c27b1e2d?w=300&h=300&fit=crop&crop=face"}
        ]
        
        for character in purchasable_characters:
            is_purchased = character['name'] in st.session_state.purchased_characters
            
            col_img, col_info, col_btn = st.columns([1, 2, 1])
            
            with col_img:
                st.markdown(f"<img src='{character['image']}' style='width: 80px; height: 80px; border-radius: 50%; object-fit: cover;'>", unsafe_allow_html=True)
            
            with col_info:
                st.markdown(f"**{character['name']} {character['emoji']}**")
                st.markdown(f"*{character['title']}*")
                st.markdown(f"{character['desc']}")
            
            with col_btn:
                if is_purchased:
                    st.success("✓ Owned")
                else:
                    if st.button(f"{character['cost']} LD", key=f"buy_{character['name']}"):
                        if st.session_state.progress['total_points'] >= character['cost']:
                            st.session_state.progress['total_points'] -= character['cost']
                            st.session_state.purchased_characters.append(character['name'])
                            st.session_state.character_relationships[character['name']] = 0
                            save_profile_to_file()
                            st.success(f"Purchased {character['name']}! Check Characters page.")
                            st.rerun()
                        else:
                            st.error("Not enough Lumie Dollars!")
            
            st.markdown("---")
    
    with col2:
        st.markdown("### 🏆 How to Earn")
        st.info("🗺️ Complete chapters: +50-100 LD")
        st.info("🎯 Finish levels: +20-50 LD")
        st.info("📚 Complete exercises: +10-30 LD")
        st.info("🔥 Daily streak: +5 LD")
        
        st.markdown("### 👥 Your Characters")
        if st.session_state.purchased_characters:
            for char in st.session_state.purchased_characters:
                st.success(f"✓ {char}")
        else:
            st.info("No purchased characters yet")

# OLD ASSESSMENT PAGE (TO BE REMOVED)
elif page == "🎯 Assessment":
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown('<div class="assessment-card">', unsafe_allow_html=True)
        st.markdown("# Welcome to LumieWorld!")
        st.markdown("✨ To personalize your journey, tell us about your skills, personality, and goals!")

        with st.form("assessment_form"):
            st.markdown("### 🌐 Your Language Profile")

            target_lang = st.selectbox("Select the language you’re learning", 
                                     ["Spanish", "French", "German", "Italian", "Portuguese", "Chinese", "Japanese", "Korean"])

            speaking_level = st.radio("Speaking Level", 
                                    ["Beginner", "Intermediate", "Advanced", "Native"],
                                    horizontal=True)

            reading_level = st.radio("Reading Level", 
                                   ["Beginner", "Intermediate", "Advanced", "Native"],
                                   horizontal=True)

            st.markdown("### 👤 About You")

            age = st.text_input("Age", placeholder="e.g., 25")
            institution = st.text_input("Current School/Institution", placeholder="e.g., University of California")

            st.markdown("### 🎯 Goals & Motivation")

            goal = st.selectbox("Why are you learning this language?", 
                                ["Travel ✈️", "Career 💼", "Education 🎓", "Culture & Hobbies 🎶", "Family/Relationships ❤️", "Other"])

            time_commitment = st.radio("How much time do you plan to study weekly?", 
                                       ["< 1 hr", "1-3 hrs", "3-5 hrs", "5+ hrs"],
                                       horizontal=True)

            st.markdown("### 🧠 Your Learning Style & Personality")

            learning_style = st.radio("What’s your preferred learning style?", 
                                     ["Structured & step-by-step 📘", "Interactive & conversational 💬", "Playful with games 🎮", "Immersive with real content 🎥"],
                                     horizontal=False)

            personality = st.radio("Your personality when learning?", 
                                  ["Quiet & reflective 🤔", "Curious & questioning 🔍", "Energetic & social 🎉"],
                                  horizontal=True)

            st.markdown("### 🌟 Preferences")

            struggles = st.multiselect("What do you struggle with most?", 
                                       ["Speaking", "Listening", "Grammar", "Vocabulary", "Confidence"],
                                       default=["Speaking"])

            interests = st.text_area("What topics excite you most? (e.g., food, movies, technology, music)", 
                                   height=80)

            if st.form_submit_button("✨ Save My Profile"):
                st.session_state.user_profile = {
                    'native_lang': 'English',
                    'target_lang': target_lang,
                    'speaking_level': speaking_level,
                    'reading_level': reading_level,
                    'age': age,
                    'institution': institution,
                    'goal': goal,
                    'time_commitment': time_commitment,
                    'learning_style': learning_style,
                    'personality': personality,
                    'struggles': struggles,
                    'interests': interests.split(",") if interests else ["General"]
                }
                st.success("✅ Assessment completed! Your profile has been updated.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f8f4ff, #fff0f8); border-radius: 20px; margin-top: 100px;'>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: #e91e63; font-size: 48px;'>🌍📚🌟</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: #666; font-size: 18px; margin-top: 20px;'>Truly Personalized Learning<br>Made Just for You</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# PROFILE PAGE
elif page == "👤 Profile":
    st.markdown("## 👤 Your Profile")
    
    tab1, tab2 = st.tabs(["📋 Profile Info", "🔄 Re-Assessment"])
    
    with tab1:
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("### 📋 Language Information")
            st.write(f"**Native Language:** {profile['native_lang']}")
            st.write(f"**Target Language:** {profile['target_lang']}")
            st.write(f"**Current Level:** {profile.get('level', profile.get('speaking_level', 'Beginner'))}")
            st.write(f"**Learning Goal:** {profile.get('goal', 'Not specified')}")
            
            st.markdown("### 🏆 Achievement Stats")
            st.write(f"**Total Points:** {st.session_state.progress['total_points']}")
            st.write(f"**Questions Answered:** {st.session_state.progress['total_questions']}")
            st.write(f"**Accuracy Rate:** {int((st.session_state.progress['correct_answers'] / max(1, st.session_state.progress['total_questions'])) * 100)}%")
        
        with col2:
            st.markdown("### 🎯 Learning Preferences")
            st.write(f"**Interests:** {', '.join(profile.get('interests', ['Not specified']))}")
            st.write(f"**Learning Style:** {profile.get('learning_style', 'Not specified')}")
            st.write(f"**Study Time:** {profile.get('study_time', profile.get('time_commitment', 'Not specified'))}")
            st.write(f"**Personality:** {profile.get('personality', 'Not specified')}")
            
            st.markdown("### 📊 Progress Details")
            st.write(f"**Current Difficulty:** Level {st.session_state.progress['difficulty_level']}")
            st.write(f"**Lessons Completed:** {st.session_state.progress['lessons_completed']}")
            st.write(f"**Learning Streak:** {st.session_state.progress['streak']} days")
        
        st.markdown("---")
        if st.button("💾 Save Profile"):
            save_profile_to_file()
            st.success("Profile saved successfully!")
    
    with tab2:
        st.markdown("<div style='text-align: center; margin: 30px 0;'><h2 style='color: #e91e63;'>Re-Assessment</h2><p>Reevaluate your language level and preferences</p></div>", unsafe_allow_html=True)
        
        # Progress indicator
        progress_width = (st.session_state.assessment_page / 3) * 100
        st.markdown(f"""
        <div style='background: #f0f0f0; border-radius: 10px; margin: 20px 0;'>
            <div style='background: linear-gradient(135deg, #e91e63, #f06292); height: 8px; border-radius: 10px; width: {progress_width}%;'></div>
        </div>
        <p style='text-align: center; color: #666;'>Step {st.session_state.assessment_page} of 3</p>
        """, unsafe_allow_html=True)
        
        if st.session_state.assessment_page == 1:
            col1, col2 = st.columns([1, 1], gap="large")
            with col1:
                st.markdown('<div class="assessment-card">', unsafe_allow_html=True)
                st.markdown("### 🌍 Language Profile")
                target_lang = st.selectbox("Select the language you're learning", ["Spanish", "French", "German", "Italian", "Portuguese", "Chinese", "Japanese", "Korean"])
                speaking_level = st.radio("Speaking Level", ["Beginner", "Intermediate", "Advanced", "Native"], horizontal=True)
                reading_level = st.radio("Reading Level", ["Beginner", "Intermediate", "Advanced", "Native"], horizontal=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f8f4ff, #fff0f8); border-radius: 20px;'>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #e91e63; font-size: 48px;'>🌍📚</div>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #666; font-size: 18px; margin-top: 20px;'>Update your<br>language background</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col3:
                if st.button("Next →", use_container_width=True):
                    if 'temp_assessment' not in st.session_state:
                        st.session_state.temp_assessment = {}
                    st.session_state.temp_assessment.update({'target_lang': target_lang, 'speaking_level': speaking_level, 'reading_level': reading_level})
                    st.session_state.assessment_page = 2
                    st.rerun()
        
        elif st.session_state.assessment_page == 2:
            col1, col2 = st.columns([1, 1], gap="large")
            with col1:
                st.markdown('<div class="assessment-card">', unsafe_allow_html=True)
                st.markdown("### 👤 About You")
                age = st.text_input("Age", placeholder="e.g., 25")
                institution = st.text_input("Current School/Institution", placeholder="e.g., University of California")
                st.markdown("### 🎯 Goals & Motivation")
                goal = st.selectbox("Why are you learning this language?", ["Travel ✈️", "Career 💼", "Education 🎓", "Culture & Hobbies 🎶", "Family/Relationships ❤️", "Other"])
                time_commitment = st.radio("How much time do you plan to study weekly?", ["< 1 hr", "1-3 hrs", "3-5 hrs", "5+ hrs"], horizontal=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f8f4ff, #fff0f8); border-radius: 20px;'>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #e91e63; font-size: 48px;'>🎯💼</div>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #666; font-size: 18px; margin-top: 20px;'>Update your goals<br>and motivation</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.assessment_page = 1
                    st.rerun()
            with col3:
                if st.button("Next →", use_container_width=True):
                    st.session_state.temp_assessment.update({'age': age, 'institution': institution, 'goal': goal, 'time_commitment': time_commitment})
                    st.session_state.assessment_page = 3
                    st.rerun()
        
        elif st.session_state.assessment_page == 3:
            col1, col2 = st.columns([1, 1], gap="large")
            with col1:
                st.markdown('<div class="assessment-card">', unsafe_allow_html=True)
                st.markdown("### 🧠 Learning Style & Personality")
                learning_style = st.radio("What's your preferred learning style?", ["Structured & step-by-step 📘", "Interactive & conversational 💬", "Playful with games 🎮", "Immersive with real content 🎥"], horizontal=False)
                personality = st.radio("Your personality when learning?", ["Quiet & reflective 🤔", "Curious & questioning 🔍", "Energetic & social 🎉"], horizontal=True)
                st.markdown("### 🌟 Preferences")
                struggles = st.multiselect("What do you struggle with most?", ["Speaking", "Listening", "Grammar", "Vocabulary", "Confidence"], default=["Speaking"])
                interests = st.text_area("What topics excite you most? (e.g., food, movies, technology, music)", height=80)
                st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown("<div style='height: 400px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f8f4ff, #fff0f8); border-radius: 20px;'>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #e91e63; font-size: 48px;'>🧠✨</div>", unsafe_allow_html=True)
                st.markdown("<div style='text-align: center; color: #666; font-size: 18px; margin-top: 20px;'>Update your learning<br>preferences</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.assessment_page = 2
                    st.rerun()
            with col3:
                if st.button("✨ Update Profile", use_container_width=True):
                    st.session_state.temp_assessment.update({'learning_style': learning_style, 'personality': personality, 'struggles': struggles, 'interests': interests.split(",") if interests else ["General"]})
                    st.session_state.user_profile.update({'native_lang': 'English', **st.session_state.temp_assessment})
                    st.session_state.assessment_page = 1
                    del st.session_state.temp_assessment
                    save_profile_to_file()
                    st.success("✅ Profile updated and saved successfully!")
                    st.balloons()

# SETTINGS PAGE
elif page == "⚙️ Settings":
    st.markdown("## ⚙️ Settings")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 🔄 Account Actions")
        if st.button("🗑️ Reset Progress"):
            st.session_state.progress = {
                'lessons_completed': 0, 
                'words_learned': 0, 
                'streak': 0,
                'total_points': 0,
                'correct_answers': 0,
                'total_questions': 0,
                'difficulty_level': 1,
                'recent_scores': []
            }
            st.success("Progress reset!")
        
        if st.button("🔄 Reset to Default Profile"):
            st.session_state.user_profile = {
                'native_lang': 'English',
                'target_lang': 'Spanish',
                'level': 'Beginner',
                'interests': ['Travel', 'Food'],
                'learning_style': 'Interactive',
                'study_time': '15-30 min',
                'personality': 'Extrovert',
                'goal': 'Basic conversation'
            }
            st.success("Profile reset to defaults!")
        
        if st.button("🗨️ Clear Chat History"):
            st.session_state.chat_history = []
            st.session_state.conversation_started = False
            st.session_state.selected_companion = None
            st.success("Chat history cleared!")
    
    with col2:
        st.markdown("### 🎨 Preferences")
        st.info("Theme: Orange & White (Active)")
        st.info("Language: English")
        st.info("Notifications: Enabled")
        
        st.markdown("### 📈 Difficulty System")
        st.info(f"Current Level: {st.session_state.progress['difficulty_level']}/3")
        st.write("System automatically adjusts based on your performance!")

# Auto-save profile on any page change or interaction
save_profile_to_file()