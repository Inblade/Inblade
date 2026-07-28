# -*- coding: utf-8 -*-
import html

ascii_art = open('ascii.txt').read().splitlines()

TOTAL = 66   # chars per info kv-line

def kv(k, v): return ('kv', k, v)
def header(t): return ('hdr', t, None)
def blank():   return ('blank', None, None)

lines = [
    ('title', 'danylo', 'github'),
    ('rule', None, None),
    kv('- OS', 'Linux, macOS'),
    kv('- Uptime', '7+ years in DevOps / SRE'),
    kv('- Host', 'Gdansk, Poland'),
    kv('- Kernel', 'Senior DevOps / SRE Engineer'),
    kv('- Shell', 'bash, python, go'),
    blank(),
    kv('- Languages.Programming', 'Python, Go, Bash, SQL'),
    kv('- Languages.Orchestration', 'Kubernetes, Docker, Helm'),
    kv('- Languages.GitOps', 'ArgoCD, GitLab CI/CD, Terraform, Ansible'),
    kv('- Languages.Observability', 'Prometheus, Grafana, Alertmanager, ELK'),
    kv('- Languages.Cloud', 'GCP (GKE), AWS, Gcore, Bare-Metal'),
    kv('- Languages.Real', 'English, Ukrainian, Polish'),
    blank(),
    kv('- Projects.Work', 'Monitoring platform from scratch on GKE'),
    kv('- Projects.Go', 'K8s Operator (kube-reaper), exporters'),
    kv('- Projects.GPU', 'NVIDIA A100/H200 node pools for AI/ML'),
    kv('- Hobbies', 'Game servers, ARK modding, AI tools'),
    blank(),
    header('Contact'),
    kv('- Email', 'dkocheto@gmail.com'),
    kv('- LinkedIn', 'linkedin.com/in/dkocheto'),
    kv('- GitHub', 'github.com/Inblade'),
    blank(),
    header('GitHub Stats'),
    kv('- Uptime', 'since Jan 2016'),
    kv('- Repos', '50 | SLO: 99.98% uptime, 0 rage-quits'),
]

themes = {
    'dark': dict(bg='#0d1117', border='#30363d', art='#768390',
                 key='#ffa657', dots='#484f58', val='#c9d1d9',
                 user='#7ee787', at='#c9d1d9', host='#79c0ff',
                 hdr='#7ee787', rule='#484f58'),
    'light': dict(bg='#ffffff', border='#d0d7de', art='#8c959f',
                  key='#e36209', dots='#d0d7de', val='#24292f',
                  user='#1a7f37', at='#24292f', host='#0969da',
                  hdr='#1a7f37', rule='#d0d7de'),
}

FS, LH, CW = 12, 17, 7.2          # info font / line height / char width
AFS, ALH, ACW = 10.5, 15.4, 6.3   # art
PAD, ART_X, INFO_X, W = 26, 26, 372, 900

def esc(s): return html.escape(s, quote=False)

def build(theme):
    c = themes[theme]
    art_h, info_h = len(ascii_art) * ALH, len(lines) * LH
    H = int(max(art_h, info_h) + PAD * 2)
    art_y = PAD + (H - 2 * PAD - art_h) / 2 + AFS
    info_y = PAD + (H - 2 * PAD - info_h) / 2 + FS

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'SFMono-Regular\',Consolas,\'Liberation Mono\',Menlo,monospace">',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{c["bg"]}" stroke="{c["border"]}"/>']

    y = art_y
    for row in ascii_art:
        if row:
            tl = len(row) * ACW
            out.append(f'<text xml:space="preserve" x="{ART_X}" y="{y:.1f}" font-size="{AFS}" fill="{c["art"]}" textLength="{tl:.1f}" lengthAdjust="spacingAndGlyphs">{esc(row)}</text>')
        y += ALH

    y = info_y
    for kind, a, b in lines:
        if kind == 'blank':
            y += LH; continue
        if kind == 'title':
            n = len(a) + 1 + len(b)
            out.append(f'<text xml:space="preserve" x="{INFO_X}" y="{y:.1f}" font-size="{FS}" font-weight="bold" textLength="{n*CW:.1f}" lengthAdjust="spacingAndGlyphs"><tspan fill="{c["user"]}">{a}</tspan><tspan fill="{c["at"]}" font-weight="normal">@</tspan><tspan fill="{c["host"]}">{b}</tspan></text>')
        elif kind == 'rule':
            n = 13
            out.append(f'<text xml:space="preserve" x="{INFO_X}" y="{y:.1f}" font-size="{FS}" fill="{c["rule"]}" textLength="{n*CW:.1f}" lengthAdjust="spacingAndGlyphs">{"-"*n}</text>')
        elif kind == 'hdr':
            n = 2 + len(a)
            out.append(f'<text xml:space="preserve" x="{INFO_X}" y="{y:.1f}" font-size="{FS}" textLength="{n*CW:.1f}" lengthAdjust="spacingAndGlyphs"><tspan fill="{c["rule"]}">— </tspan><tspan fill="{c["hdr"]}" font-weight="bold">{esc(a)}</tspan></text>')
        else:
            key, val = a, b
            ndots = max(TOTAL - len(key) - 2 - len(val) - 1, 2)
            n = len(key) + 2 + ndots + 1 + len(val)
            out.append(f'<text xml:space="preserve" x="{INFO_X}" y="{y:.1f}" font-size="{FS}" textLength="{n*CW:.1f}" lengthAdjust="spacingAndGlyphs"><tspan fill="{c["key"]}">{esc(key)}</tspan><tspan fill="{c["val"]}">: </tspan><tspan fill="{c["dots"]}">{"."*ndots}</tspan><tspan fill="{c["val"]}"> {esc(val)}</tspan></text>')
        y += LH

    out.append('</svg>')
    open(f'profile-{theme}.svg', 'w').write('\n'.join(out))
    print(theme, 'H =', H)

build('dark'); build('light')
