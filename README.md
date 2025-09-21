<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🌟 Lumie World – Your AI Learning Companion</h1>
  <p>
    Lumie World is an <b>AI-powered learning companion app</b> that makes language practice fun and engaging. 
    Users can <b>chat with characters</b>, <b>progress through learning roadmaps</b>, and <b>earn rewards</b> 
    while improving their skills. The app combines <b>gamification</b>, <b>personalization</b>, and 
    <b>AI-driven conversations</b> to provide a unique, interactive learning experience.
  </p>

  <h2>✨ Key Features</h2>
  <ul>
    <li>📝 <b>Profile Assessment</b> – Users answer questions about their language level, interests, and personality to personalize their journey.</li>
    <li>📚 <b>City Roadmap</b> – Structured learning pathway where topics are generated based on user level (e.g., alphabets for beginners, advanced topics later).</li>
    <li>💬 <b>Character Chat</b> – Practice conversations with AI characters that adapt to the user’s learning style.</li>
    <li>❤️ <b>Relationship System</b> – The more you chat with a character, the stronger your relationship grows.</li>
    <li>🏆 <b>Leaderboard</b> – Compete with friends by earning points through learning and interactions.</li>
    <li>🛒 <b>Lumie Store</b> – Earn “Lumie Dollars” and redeem them for characters and other rewards.</li>
    <li>🔊 <b>Voice Integration</b> – Learn through listening and speaking with characters powered by <b>Amazon Polly</b> and <b>gTTS</b>.</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
├── LumieWorld(amazon).py   # Main application file
├── lumie_profile.json      # User profile & personalization data
├── requirements.txt        # Python dependencies
├── polly_audio.mp3         # Generated speech output (Amazon Polly)
├── temp_audio.mp3          # Temporary audio storage
└── README.md               # Project documentation
  </pre>

  <h2>⚙️ Installation</h2>
  <ol>
    <li>
      Clone this repository:
      <pre><code>git clone https://github.com/your-username/Lumie-World.git
cd Lumie-World</code></pre>
    </li>
    <li>
      Create and activate a virtual environment (recommended):
      <pre><code>python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows</code></pre>
    </li>
    <li>
      Install dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <h2>📦 Dependencies</h2>
  <p>The app requires the following Python libraries (from <code>requirements.txt</code>):</p>
  <ul>
    <li><code>streamlit</code> – Web app framework for the UI</li>
    <li><code>gtts</code> – Google Text-to-Speech for audio generation</li>
    <li><code>boto3</code> – AWS SDK for Python (Amazon Polly integration)</li>
    <li><code>botocore</code> – Core dependency for AWS services</li>
  </ul>

  <h2>🔑 AWS Configuration</h2>
  <p>To use <b>Amazon Polly</b>, configure your AWS credentials:</p>
  <pre><code>aws configure</code></pre>
  <p>Provide your <b>AWS Access Key</b>, <b>Secret Key</b>, and <b>region</b>.</p>

  <h2>🚀 Usage</h2>
  <p>Run the app with Streamlit:</p>
  <pre><code>streamlit run LumieWorld(amazon).py</code></pre>
  <p>Then open the provided local URL in your browser to start your AI learning journey.</p>

 

</body>
</html>
