# 3 言語のページを書き出す： python3 build/build.py
# 文言は strings.py、形は template.html。index.html / ja/index.html / fr/index.html は生成物なので直接直さない。
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from strings import S

BASE = "https://maeken313.github.io/"
LANGS = [("en", "", "EN"), ("ja", "ja/", "日本語"), ("fr", "fr/", "FR")]

JA_CSS = """  :root{--sans:"Inter Tight","Noto Sans JP",system-ui,sans-serif; --serif:"Instrument Serif","Zen Old Mincho",serif}
  body{font-size:16px;line-height:1.85;letter-spacing:.02em;word-break:auto-phrase}
  .hero h1{font-family:"Zen Old Mincho",serif;font-weight:600;font-size:clamp(36px,5.4vw,68px);line-height:1.3;letter-spacing:.02em;max-width:none}
  .hero h1 em{font-style:normal}
  .head h2,.abh,footer h2{font-family:"Zen Old Mincho",serif;font-weight:600;letter-spacing:.02em;line-height:1.35}
  .head h2,.abh{font-size:clamp(26px,3.2vw,38px)} footer h2{font-size:clamp(28px,4vw,48px)}
  .mono{text-transform:none;letter-spacing:.04em}
  .notes li,.steps p,.about p{line-break:strict}"""
FR_CSS = """  .hero h1{max-width:17ch}"""


def switcher(cur, prefix):
    out = []
    for code, path, label in LANGS:
        href = prefix + (path or "./") if path else (prefix or "./")
        cur_attr = ' aria-current="page"' if code == cur else ""
        out.append(f'<a href="{href}" hreflang="{code}" lang="{code}"{cur_attr}>{label}</a>')
    return '<div class="lang" aria-label="Language">' + "".join(out) + "</div>"


def build():
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{BASE}{p}">' for c, p, _ in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    for code, path, _ in LANGS:
        prefix = "../" if path else ""
        v = {k: d[code] for k, d in S.items()}
        note = v.pop("w1_note")
        v.update(
            P=prefix,
            alternates=alternates + f'\n<link rel="canonical" href="{BASE}{path}">',
            switcher=switcher(code, prefix),
            extra_fonts="&family=Zen+Old+Mincho:wght@600&family=Noto+Sans+JP:wght@400;500;700" if code == "ja" else "",
            lang_css=JA_CSS if code == "ja" else FR_CSS if code == "fr" else "",
            w1_note_html=f'<p class="vnote">{note}</p>' if note else "",
        )
        html = re.sub(r"\{\{(\w+)\}\}", lambda m: v[m.group(1)], tpl)
        left = re.findall(r"\{\{\w+\}\}", html)
        assert not left, left
        out = os.path.join(ROOT, path, "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(html)
        print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    build()
