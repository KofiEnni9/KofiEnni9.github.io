"""Builds projects/<slug>/index.html from the fragments in _build/pages/.

Each project page = shared header + facts list + the fragment body + prev/next links.
Run from the repo root:  python3 _build/build.py
Jekyll skips folders that start with an underscore, so _build/ is never published.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAGS = Path(__file__).resolve().parent / "pages"

PAGES = [
    dict(
        slug="oream",
        title="OREAM: end-to-end off-road planning from camera and LiDAR",
        short="OREAM end-to-end planner",
        kicker="Research, MSU Center for Advanced Vehicular Systems",
        lede="A planner that looks at one camera frame and one LiDAR sweep and proposes where an off-road vehicle should drive for the next few seconds, trained only on the paths a human actually drove.",
        facts=[
            ("Role", "Lead developer: data pipeline, model, training and evaluation"),
            ("When", "2026, ongoing"),
            ("Stack", "PyTorch, CUDA, TransFuser, NumPy, OpenCV, rosbags, scikit-learn"),
            ("Status", "Paper in preparation for SPIE. Code is private until publication."),
        ],
    ),
    dict(
        slug="trunk-diameter",
        title="Measuring tree trunks from a single LiDAR scan",
        short="Trunk diameter from LiDAR",
        kicker="Research, MSU Center for Advanced Vehicular Systems",
        lede="A C++17 pipeline that finds tree trunks in an off-road point cloud from a Clearpath Warthog and estimates each trunk's diameter at breast height.",
        facts=[
            ("Role", "Sole developer"),
            ("When", "2026"),
            ("Stack", "C++17, PCL, Eigen, GLM, NATURE elevation grid"),
            ("Code", '<a href="https://github.com/KofiEnni9/nature-stack/tree/master/src/Diameter_Proj">nature-stack/src/Diameter_Proj</a>'),
        ],
    ),
    dict(
        slug="lidar-segmentation",
        title="Semantic segmentation of off-road LiDAR",
        short="Off-road LiDAR segmentation",
        kicker="Research, MSU Center for Advanced Vehicular Systems",
        lede="Teaching a network to label every LiDAR return on a trail as grass, shrubs, foliage, smooth trail, rough trail or obstacle, so a planner can tell what it is allowed to drive over.",
        facts=[
            ("Role", "Labelled data, adapted the training code, trained and evaluated the models"),
            ("When", "2024 to 2025"),
            ("Stack", "PyTorch, MMDetection3D, FRNet, Point Transformer V3, SPVCNN, MATLAB Lidar Labeler"),
            ("Result", "0.65 mIoU over 7 classes on held-out scans, 0.94 IoU on high vegetation"),
        ],
    ),
    dict(
        slug="busybox",
        title="BusyBox: a benchmark for affordance generalization",
        short="BusyBox at Microsoft Research",
        kicker="Research internship, Microsoft Research",
        lede="A physical board of switches, sliders, buttons and dials that can be rearranged into many different-looking devices, built to test whether vision-language-action policies really understand the controls they manipulate.",
        facts=[
            ("Role", "Robotics research intern: data-collection automation and robot operation"),
            ("When", "August 2025"),
            ("Paper", 'Fortier, Adamson, Hellebrekers, LaScala, <span class="me">Ennin</span>, Murray, Kolobov, Mullins. <a href="https://arxiv.org/abs/2602.05441">arXiv:2602.05441</a>. Accepted at CoRL.'),
            ("Robots", "Mobile ALOHA (bimanual), with π₀.₅ and GR00T-N1.6 baselines"),
        ],
    ),
    dict(
        slug="teleoperation",
        title="Marionette Live: driving a robot arm with your own arm",
        short="Vision-based teleoperation",
        kicker="HackGT 13, Georgia Tech, team of three",
        lede="Stand in front of a webcam, strike a pose, and an SO-101 arm copies your arm in real time. No leader arm, no markers, no calibration rig.",
        facts=[
            ("Role", "Team member. I set up the one-arm teleop kit in the repo and worked on the tracking-loss safety behaviour"),
            ("When", "September 2026"),
            ("Stack", "MediaPipe (browser), JavaScript, Three.js twin, Python bridge, Feetech STS3215 servos, TimescaleDB"),
            ("Code", '<a href="https://github.com/Im-ma/Teleoperation-Arm">Im-ma/Teleoperation-Arm</a>'),
        ],
    ),
    dict(
        slug="salo",
        title="SALO: a PDF reader that reads along with you",
        short="SALO reading assistant",
        kicker="Personal project",
        lede="A desktop PDF reader that summarises the page you are on as you scroll and answers questions about everything you have open, citing the right document.",
        facts=[
            ("Role", "Sole developer, front end and back end"),
            ("When", "2025"),
            ("Stack", "Electron, React, Redux, pdf.js, Tailwind, FastAPI, Pinecone, BM25, Claude tool use, Firebase"),
            ("Code", '<a href="https://github.com/KofiEnni9/salo-readingtool">KofiEnni9/salo-readingtool</a>'),
        ],
    ),
    dict(
        slug="danso",
        title="Danso: an adaptive study partner for Ghana's NSMQ",
        short="Danso study platform",
        kicker="Personal project",
        lede="A study platform for Ghana's National Science and Maths Quiz that retrieves real past questions, explains them with an open language model, and adapts which contests it quizzes you on as you improve.",
        facts=[
            ("Role", "Builder of the retrieval, model serving and bandit"),
            ("When", "2024"),
            ("Stack", "sentence-transformers, FAISS, Mistral-7B-Instruct (4-bit), FastAPI, Streamlit, LinUCB"),
            ("Code", '<a href="https://github.com/KofiEnni9/Danso">KofiEnni9/Danso</a>'),
        ],
    ),
    dict(
        slug="building-classifier",
        title="Recognising campus buildings from a photo",
        short="Campus building classifier",
        kicker="MSU AI Club Campus Vision Challenge, 1st place",
        lede="A ResNet-50 fine-tuned to tell ten Mississippi State buildings apart from phone photos, reaching 99.45% validation accuracy on Colab compute.",
        facts=[
            ("Team", "Team se7en: Kofi A. Ennin and Sandys Ayuumah"),
            ("When", "2024"),
            ("Stack", "PyTorch, torchvision, scikit-learn, Google Colab"),
            ("Code", '<a href="https://github.com/KofiEnni9/buildingclassification">KofiEnni9/buildingclassification</a>'),
        ],
    ),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{short} | Kofi A. Ennin</title>
<meta name="description" content="{lede_attr}">
<meta property="og:title" content="{title_attr}">
<meta property="og:description" content="{lede_attr}">
<link rel="icon" href="../../assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=JetBrains+Mono:wght@400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/site.css">
<script src="../../assets/site.js"></script>
</head>
<body>
<div class="wrap">
<header class="topbar">
  <a class="home" href="../../">Kofi A. Ennin</a>
  <nav aria-label="Site"><a href="../../#work">All work</a><a href="../../cv.pdf">CV</a></nav>
</header>

<article class="proj">
<header class="proj-head">
  <p class="kicker">{kicker}</p>
  <h1>{title}</h1>
  <p class="lede">{lede}</p>
  <dl class="facts">
{facts}
  </dl>
</header>

{body}

<nav class="pager" aria-label="More projects">
{prev}
{next}
</nav>
</article>

<footer>
  <span>Kofi A. Ennin, Starkville, Mississippi</span>
  <button class="theme-toggle" id="theme" type="button">Switch to dark</button>
</footer>
</div>
</body>
</html>
"""


def main():
    for i, p in enumerate(PAGES):
        body = (FRAGS / f"{p['slug']}.html").read_text()
        facts = "\n".join(f"    <dt>{k}</dt><dd>{v}</dd>" for k, v in p["facts"])
        prev_p = PAGES[i - 1] if i > 0 else None
        next_p = PAGES[i + 1] if i + 1 < len(PAGES) else None
        prev = (f'  <a class="prev" href="../{prev_p["slug"]}/"><span>Previous</span><strong>{prev_p["short"]}</strong></a>'
                if prev_p else '  <a class="prev" href="../../#work"><span>Back to</span><strong>All work</strong></a>')
        nxt = (f'  <a class="next" href="../{next_p["slug"]}/"><span>Next</span><strong>{next_p["short"]}</strong></a>'
               if next_p else '  <a class="next" href="../../#work"><span>Back to</span><strong>All work</strong></a>')
        html = TEMPLATE.format(
            short=escape(p["short"]), title=escape(p["title"]), kicker=escape(p["kicker"]),
            lede=escape(p["lede"]), lede_attr=escape(p["lede"], quote=True), title_attr=escape(p["title"], quote=True),
            facts=facts, body=body.strip(), prev=prev, next=nxt,
        )
        out = ROOT / "projects" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
