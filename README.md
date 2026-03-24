<div align="center">
  <h1>🛡️ Sonic Shroud: The Audio-Stegano Vault 🔐</h1>
  
  <p>
    <img src="https://img.shields.io/badge/Security-AES--256--CBC-green?style=for-the-badge&logo=github-actions" alt="Security">
    <img src="https://img.shields.io/badge/Steganography-LSB-blue?style=for-the-badge" alt="Stegano">
    <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
  </p>
</div>

<hr />

<h3>🌟 Project Overview</h3>
<p><b>Sonic Shroud</b> is a high-security credential management system. It eliminates the "Master Password" vulnerability by hiding your encryption keys inside innocent-looking <code>.wav</code> audio files using <b>Least Significant Bit (LSB)</b> Steganography.</p>

<hr />

<h3>🏗️ Technical Architecture</h3>
<table width="100%">
  <thead>
    <tr style="background-color: #21262d;">
      <th align="left">Component</th>
      <th align="left">Technology</th>
      <th align="left">Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Steganography</b></td>
      <td>LSB Encoding</td>
      <td>Conceals bits inside audio PCM samples</td>
    </tr>
    <tr>
      <td><b>Cryptography</b></td>
      <td>AES-256 (CBC)</td>
      <td>Military-grade encryption for secrets</td>
    </tr>
    <tr>
      <td><b>KDF</b></td>
      <td>PBKDF2</td>
      <td>Derives keys from audio-hidden data</td>
    </tr>
    <tr>
      <td><b>Storage</b></td>
      <td>SQLite3</td>
      <td>Hardened local database</td>
    </tr>
  </tbody>
</table>

<hr />

<h3>🚀 Advanced Security Features</h3>
<ul>
  <li><b>🎧 Acoustic Authentication:</b> Your master key is a sound file.</li>
  <li><b>🔄 Master Key Rotation:</b> Securely migrate vault to a new audio file.</li>
  <li><b>🛡️ Integrity Protection:</b> Detection for audio tampering.</li>
  <li><b>🤖 CI/CD Integration:</b> Automated testing via GitHub Actions.</li>
</ul>

<hr />

<h3>🛠️ Installation & Setup</h3>
<p>Follow these steps to deploy the vault:</p>

<pre><code># 1. Clone the Vault
git clone https://github.com/ZUNATIC/SonicShroud.git
cd SonicShroud

# 2. Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt</code></pre>

<hr />

<h3>📖 User Operations Guide</h3>
<table width="100%">
  <thead>
    <tr style="background-color: #21262d;">
      <th align="left">Option</th>
      <th align="left">Action</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>[1]</b></td>
      <td>Forge Key</td>
      <td>Embed secret string into a .wav file.</td>
    </tr>
    <tr>
      <td><b>[2]</b></td>
      <td>Inject Data</td>
      <td>Encrypt and lock new passwords into vault.</td>
    </tr>
    <tr>
      <td><b>[3]</b></td>
      <td>Unlock Vault</td>
      <td>Decrypt secrets using the Shadow Key.</td>
    </tr>
    <tr>
      <td><b>[4]</b></td>
      <td>Migration</td>
      <td>Rotate/Change your audio keys.</td>
    </tr>
  </tbody>
</table>

<hr />

<h3>🧪 Automated Security Validation</h3>
<p>To ensure the encryption and steganography engines are functioning perfectly, run the internal validation suite:</p>
<pre><code>pytest test_core.py</code></pre>

<hr />

<h3>👤 Developed By</h3>
<ul>
  <li><b>Name:</b> Umae Habiba (Zunatic)</li>
</ul>

<hr />

<div align="center">
  <p>Distributed under the <b>MIT License</b>.</p>
</div>
