# 📱 Social Media Marketing Portfolio

A full-stack portfolio website built with Flask (Python) + HTML/CSS/JS.
Supports YouTube, Vimeo, TikTok, Instagram, and local video file embeds.

---

## 🚀 Quick Start (PyCharm)

1. **Open the `portfolio` folder** as your project in PyCharm.

2. **Install dependencies** — open the PyCharm terminal and run:
   ```
   pip install flask
   ```

3. **Run the app:**
   ```
   python app.py
   ```

4. **Open your browser** to: http://127.0.0.1:5000

---

## ✏️ Customizing Content

All editable content is at the top of **`app.py`**:

- `PROFILE` — name, bio, email, social links
- `PROJECTS` — portfolio items with video embeds
- `SKILLS` — skill names and percentages

### Adding Videos

**YouTube:**
```python
"video_type": "youtube",
"video_id": "dQw4w9WgXcQ",   # the part after ?v= in the URL
```

**Vimeo:**
```python
"video_type": "vimeo",
"video_id": "123456789",     # numbers in the Vimeo URL
```

**Local video file:**
1. Go to http://127.0.0.1:5000/upload and upload your .mp4 file
2. Copy the filename shown after uploading
```python
"video_type": "local_file",
"video_src": "my_video.mp4",
```

**TikTok:**
On TikTok → Share → Embed → copy the `<blockquote>` HTML
```python
"video_type": "tiktok",
"tiktok_embed": """<blockquote class="tiktok-embed" ...>...</blockquote>""",
```

**Instagram:**
On Instagram → ··· → Embed → copy the embed HTML
```python
"video_type": "instagram",
"instagram_embed": """<blockquote class="instagram-media" ...>...</blockquote>""",
```

### Adding a Profile Photo
1. Put your photo in `static/images/` (e.g. `static/images/photo.jpg`)
2. Open `templates/index.html`, find the `about-photo` section (~line 105)
3. Comment out the placeholder div and uncomment the `<img>` tag
4. Update the filename in the `src` attribute

---

## 🌐 Deploying for Free (So Anyone Can Visit)

### Option 1: Render (Recommended)
1. Push this folder to a GitHub repo
2. Go to https://render.com → New → Web Service
3. Connect your GitHub repo
4. Set: Build Command = `pip install -r requirements.txt`
5. Set: Start Command = `gunicorn app:app`
6. Deploy! You'll get a free `.onrender.com` URL

Install gunicorn first: `pip install gunicorn` and add to requirements.txt

### Option 2: Railway
1. Push to GitHub
2. Go to https://railway.app → New Project → Deploy from GitHub

---

## 📁 Project Structure

```
portfolio/
├── app.py                  ← Main Flask app (edit this!)
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html          ← Main portfolio page
│   └── upload.html         ← Admin video upload page
├── static/
│   ├── css/style.css       ← All styling
│   ├── js/main.js          ← Animations & interactions
│   └── images/             ← Put profile photo here
└── uploads/                ← Local video files go here (auto-created)
```
