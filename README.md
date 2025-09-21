
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>🌟 Lumie World</h1>
  <p>
    Lumie World is a personalized AI-powered character interaction app. Users can chat with virtual characters, 
    build relationships, and experience immersive voice responses generated using Amazon Polly and text-to-speech services.
  </p>

  <h2>✨ Features</h2>
  <ul>
    <li>💬 <b>Character Chat</b> – Talk to your favorite characters.</li>
    <li>❤️ <b>Relationship System</b> – Relationship level grows the more you interact.</li>
    <li>🔊 <b>Voice Integration</b> – Characters respond with audio using <b>Amazon Polly</b> or <b>gTTS</b>.</li>
    <li>🗂 <b>Profiles</b> – Character settings stored in <code>lumie_profile.json</code>.</li>
    <li>🌐 <b>Streamlit UI</b> – Web interface for interaction.</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
├── LumieWorld(amazon).py   # Main application file
├── lumie_profile.json      # Character profile & personalization data
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
  <p>Then open the provided local URL in your browser to start interacting with characters.</p>



</body>
</html>
