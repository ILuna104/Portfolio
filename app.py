"""
====================================================
  SOCIAL MEDIA MARKETING PORTFOLIO — Flask Backend
====================================================
Run this file to start the website locally.

SETUP INSTRUCTIONS (PyCharm):
1. Open this entire 'portfolio' folder as your project in PyCharm
2. Open the terminal in PyCharm and run:
       pip install flask
3. Then run:
       python app.py
4. Open your browser to:  http://127.0.0.1:5000

TO DEPLOY FOR FREE (so anyone can visit the site):
- Push this folder to GitHub, then deploy on:
  * https://render.com  (free tier, recommended)
  * https://railway.app (free tier)
  * https://fly.io      (free tier)
====================================================
"""

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import json

app = Flask(__name__)

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
try:
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
except Exception:
    UPLOAD_FOLDER = "/tmp/uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"mp4", "mov", "avi", "webm", "mkv"}

# ---------------------------------------------------------------------------
# ★  PORTFOLIO DATA  ★
# Edit this section to update your GF's info and projects.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Isleny Luna",
    "title": "Social Media Marketing Strategist",
    "tagline": "Crafting scroll-stopping content that converts.",
    "bio": (
        "I'm a marketing student specializing in social media strategy and "
        "content creation. I help brands find their voice, grow their audience, "
        "and turn followers into customers. From short-form video to full "
        "campaign strategy — I make brands unforgettable."
    ),
    "email": "Islenyluna104@gmail.com",
    "instagram": "https://instagram.com/i10luna",
    "tiktok": "https://tiktok.com/@iluna.10",
}

# ---------------------------------------------------------------------------
# ★  PROJECTS / VIDEO PORTFOLIO  ★
#
# Each project can have ONE of these video types:
#
#   "local_file"   → A video file you upload via the /upload page.
#                    Set "video_src" to the filename, e.g. "mybrand_reel.mp4"
#
#   "youtube"      → A YouTube video.
#                    Set "video_id" to the YouTube video ID
#                    (the part after ?v= in the URL, e.g. "dQw4w9WgXcQ")
#
#   "tiktok"       → A TikTok embed.
#                    Set "tiktok_embed" to the full embed HTML from TikTok's
#                    share menu → Embed → copy the <blockquote> block.
#
#   "instagram"    → An Instagram reel/post embed.
#                    Set "instagram_embed" to the full embed HTML from
#                    Instagram's share → Embed option.
#
#   "vimeo"        → A Vimeo video.
#                    Set "video_id" to the Vimeo video ID (numbers in the URL).
# ---------------------------------------------------------------------------

PROJECTS = [
    {
        "id": 1,
        "title": "Brand Campaign — [FXBG Iron]",
        "client": "FXBG Iron",       # ← CHANGE THIS
        "category": "Brand Strategy",
        "tags": ["Instagram Reels", "Brand Identity", "Launch"],
        "description": (
            "Developed and executed a full social media launch campaign "
            "achieving 5K impressions in the first week. Strategy included "
            "short-form video, influencer coordination, and paid social."
        ),
        "results": "5K impressions · 500 new followers · 8% engagement rate",
        # ─── VIDEO EMBED ────────────────────────────────────────────────────
        # TYPE: youtube
        # Replace the video_id below with the YouTube video ID.
        # Example URL: https://www.youtube.com/watch?v=ABC123xyz
        #              video_id would be "ABC123xyz"
        "video_type": "instagram",
        "instagram_embed": """<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/DRDCdlzgDtQ/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/DRDCdlzgDtQ/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/DRDCdlzgDtQ/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by FXBG Iron Gym (@fxbgiron)</a></p></div></blockquote>
        <script async src="//www.instagram.com/embed.js"></script>""",   # ← CHANGE THIS
        # ────────────────────────────────────────────────────────────────────
        "thumbnail": "",   # optional: filename of a thumbnail image in /static/images/
    },
    {
        "id": 2,
        "title": "Brand Campaign — [FXBG Iron]",
        "client": "FXBG Iron",  # ← CHANGE THIS
        "category": "Brand Strategy",
        "tags": ["Instagram Reels", "Brand Identity", "Launch"],
        "description": (
            "Developed and executed a full social media launch campaign "
            "achieving 5K impressions in the first week. Strategy included "
            "short-form video, influencer coordination, and paid social."
        ),
        "results": "5K impressions · 500 new followers · 8% engagement rate",
        # ─── VIDEO EMBED ────────────────────────────────────────────────────
        # TYPE: youtube
        # Replace the video_id below with the YouTube video ID.
        # Example URL: https://www.youtube.com/watch?v=ABC123xyz
        #              video_id would be "ABC123xyz"
        "video_type": "instagram",
        "instagram_embed": """<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/DQPGR39gKQM/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/DQPGR39gKQM/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/DQPGR39gKQM/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by FXBG Iron Gym (@fxbgiron)</a></p></div></blockquote>
            <script async src="//www.instagram.com/embed.js"></script>""",  # ← CHANGE THIS
        # ────────────────────────────────────────────────────────────────────
        "thumbnail": "",  # optional: filename of a thumbnail image in /static/images/
    },

]

SKILLS = [
    {"name": "Instagram & TikTok Strategy", "level": 95},
    {"name": "Short-Form Video Production", "level": 90},
    {"name": "Content Calendar Planning", "level": 92},
    {"name": "Paid Social (Meta Ads)", "level": 80},
    {"name": "Analytics & Reporting", "level": 85},
    {"name": "Influencer Coordination", "level": 78},
    {"name": "Brand Voice & Copywriting", "level": 88},
    {"name": "Adobe Premiere / CapCut", "level": 82},
]

# ---------------------------------------------------------------------------
# ROUTES
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS,
        skills=SKILLS,
    )


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return redirect(url_for("index"))
    return render_template("project.html", project=project, profile=PROFILE)


# ─── VIDEO UPLOAD ROUTE ──────────────────────────────────────────────────────
# Visit /upload in your browser to upload local video files.
# Uploaded files are saved to the /uploads folder.
# After uploading, copy the filename into PROJECTS above under video_src.
# ─────────────────────────────────────────────────────────────────────────────

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload():
    message = None
    uploaded_name = None
    if request.method == "POST":
        if "video" not in request.files:
            message = "No file selected."
        else:
            file = request.files["video"]
            if file.filename == "":
                message = "No file selected."
            elif not allowed_file(file.filename):
                message = f"File type not allowed. Use: {', '.join(ALLOWED_EXTENSIONS)}"
            else:
                from werkzeug.utils import secure_filename
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                uploaded_name = filename
                message = f"✅ Uploaded successfully! Add '{filename}' as video_src in app.py."
    # List existing uploads
    existing = os.listdir(UPLOAD_FOLDER)
    return render_template("upload.html", message=message, uploaded_name=uploaded_name,
                           existing=existing, profile=PROFILE)


@app.route("/uploads/<filename>")
def serve_upload(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ─── CONTACT FORM ────────────────────────────────────────────────────────────
# Currently logs to console. To send real emails, add Flask-Mail or use
# a service like Formspree (https://formspree.io) — free tier available.
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")
    # TODO: replace print with email sending logic
    print(f"\n📬 New Contact Message\nFrom: {name} <{email}>\n{message}\n")
    return render_template("index.html", profile=PROFILE, projects=PROJECTS,
                           skills=SKILLS, contact_success=True)


if __name__ == "__main__":
    # Debug mode is ON for local development — turn off before deploying!
    app.run(debug=True, port=5000)
