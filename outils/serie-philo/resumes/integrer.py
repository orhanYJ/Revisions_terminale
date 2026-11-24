"""Intègre les résumés écrits des épisodes (resumes/<notion>.json) dans philo/index.html, sous le lecteur des séries.

Rejouable : remplace le style, les données RESUMES_SERIE et le composant SerieResume entre les marqueurs
resumes-serie:debut / resumes-serie:fin, et branche SerieResume dans SerieView s'il n'y est pas.
Format d'un épisode : {"intro", "parties": [{"t", "p": [...], "cit": [{"t", "a"}]}], "reperes": [...], "retenir": [...]}
(*italique* pour les titres d'œuvres). Contrôle : chaque épisode de SERIES publié a son résumé.
Usage : python3 outils/serie-philo/resumes/integrer.py, puis monter le cache de philo/sw.js.
"""
import json, os, re, sys
ICI = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ICI, "..", "..", "..", "philo", "index.html")
NOTIONS = ["liberte", "devoir", "bonheur", "conscience", "etat"]

CSS = r'''  .sr{scroll-margin-top:70px;margin:40px 0 10px;border:1px solid var(--rule);border-radius:14px;background:var(--paper);padding:26px 28px 22px}
  .sr-k{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--saffron-deep)}
  .sr-h{font-family:'Spectral',serif;font-weight:600;font-size:25px;line-height:1.2;margin:6px 0 12px;color:var(--ink)}
  .sr-in{font-family:'Spectral',serif;font-size:17.5px;line-height:1.55;color:var(--ink-soft);margin:0 0 6px}
  .sr-som{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 4px}
  .sr-som button{font:inherit;font-size:12.5px;padding:5px 11px;border:1px solid var(--rule);border-radius:20px;background:var(--card-2);color:var(--ink-soft);cursor:pointer}
  .sr-som button:hover{border-color:var(--saffron);color:var(--ink)}
  .sr-p{margin-top:24px;scroll-margin-top:80px}
  .sr-pt{display:flex;gap:11px;align-items:baseline;font-family:'Spectral',serif;font-weight:600;font-size:19px;color:var(--ink);margin:0 0 8px}
  .sr-pt .n{flex:none;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:500;color:var(--saffron-deep)}
  .sr ul{margin:0;padding:0 0 0 20px}
  .sr li{font-size:15px;line-height:1.6;color:var(--ink);margin:0 0 7px}
  .sr li::marker{color:var(--saffron)}
  .sr-c{margin:10px 0 4px;padding:11px 16px;border-left:3px solid var(--saffron);background:var(--ivory-2);border-radius:0 6px 6px 0}
  .sr-c .t{font-family:'Spectral',serif;font-style:italic;font-size:16px;line-height:1.5;color:var(--ink)}
  .sr-c .a{font-size:12.5px;color:var(--ink-soft);margin-top:4px}
  .sr-rep{margin-top:24px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
  .sr-rep .k{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);margin-right:4px}
  .sr-rep span.r{font-size:13px;padding:4px 10px;border-radius:20px;border:1px solid var(--rule);background:var(--card-2);color:var(--ink)}
  .sr-ret{margin-top:24px;padding:16px 20px;border:1px solid rgba(var(--saffron-rgb),.45);background:rgba(var(--saffron-rgb),.08);border-radius:10px}
  .sr-ret .k{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--saffron-deep);margin-bottom:8px}
  .sr-ret li{margin-bottom:5px}
  .sr-bas{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:22px}
  .sr-bas button{font:inherit;font-size:13.5px;padding:8px 14px;border:1px solid var(--rule);border-radius:8px;background:var(--card-2);color:var(--ink);cursor:pointer}
  .sr-bas button:hover{border-color:var(--saffron)}
  @media(max-width:760px){.sr{padding:20px 16px 18px;margin-top:30px}.sr-h{font-size:21px}.sr-in{font-size:16.5px}.sr li{font-size:14.5px}.sr-c .t{font-size:15px}.sr ul{padding-left:18px}}
  @media print{.sr{border:0;padding:0}.sr-som,.sr-bas{display:none}}
'''
COMP = r'''const srTxt=s=>{const o=[];String(s).split(/(\*[^*]+\*)/).forEach((x,i)=>{if(/^\*[^*]+\*$/.test(x))o.push(React.createElement("em",{key:i},x.slice(1,-1)));else if(x)o.push(x);});return o;};
function SerieResume({S,cur,choisir}){const R=RESUMES_SERIE[cur.code];if(!R)return null;
 const dispo=S.episodes.filter(e=>e.code),i=dispo.findIndex(e=>e.code===cur.code),prec=dispo[i-1],suiv=dispo[i+1];
 const aller=k=>{const el=document.getElementById("sr-"+cur.code+"-"+k);if(el)el.scrollIntoView({behavior:"smooth",block:"start"});};
 return React.createElement("section",{className:"sr",id:"sr-"+cur.code},
  React.createElement("div",{className:"sr-k"},"Résumé écrit · épisode "+cur.num),
  React.createElement("h2",{className:"sr-h"},cur.titre),
  React.createElement("p",{className:"sr-in"},srTxt(R.intro)),
  R.parties.length>2?React.createElement("div",{className:"sr-som"},R.parties.map((p,k)=>React.createElement("button",{key:k,onClick:()=>aller(k)},(k+1)+". ",srTxt(p.t)))):null,
  R.parties.map((p,k)=>React.createElement("div",{key:k,className:"sr-p",id:"sr-"+cur.code+"-"+k},
   React.createElement("h3",{className:"sr-pt"},React.createElement("span",{className:"n"},String(k+1).padStart(2,"0")),srTxt(p.t)),
   React.createElement("ul",null,p.p.map((x,j)=>React.createElement("li",{key:j},srTxt(x)))),
   (p.cit||[]).map((c,j)=>React.createElement("blockquote",{key:"c"+j,className:"sr-c"},React.createElement("div",{className:"t"},"« "+c.t+" »"),React.createElement("div",{className:"a"},srTxt(c.a)))))),
  R.reperes&&R.reperes.length?React.createElement("div",{className:"sr-rep"},React.createElement("span",{className:"k"},"Repères"),R.reperes.map((r,k)=>React.createElement("span",{key:k,className:"r"},r))):null,
  R.retenir&&R.retenir.length?React.createElement("div",{className:"sr-ret"},React.createElement("div",{className:"k"},"À retenir"),React.createElement("ul",null,R.retenir.map((x,k)=>React.createElement("li",{key:k},srTxt(x))))):null,
  React.createElement("div",{className:"sr-bas"},
   prec?React.createElement("button",{onClick:()=>choisir(prec.code,1)},"← Épisode "+prec.num):React.createElement("span"),
   suiv?React.createElement("button",{onClick:()=>choisir(suiv.code,1)},"Épisode "+suiv.num+" →"):null));}
'''

def remplacer(html, avant_ancre, bloc, deb, fin):
    if deb in html:
        a = html.index(deb)
        b = html.index(fin, a) + len(fin)
        return html[:a] + bloc + html[b:]
    assert html.count(avant_ancre) == 1, avant_ancre
    i = html.index(avant_ancre)
    return html[:i] + bloc + html[i:]

def main():
    data = {}
    for n in NOTIONS:
        data.update(json.load(open(os.path.join(ICI, n + ".json"), encoding="utf-8")))
    html = open(PAGE, encoding="utf-8").read()
    codes = re.findall(r'\{code:"([a-z]+-\d)"', html[html.index("const SERIES=["):html.index("const serieDe=")])
    manque = [c for c in codes if c not in data]
    assert not manque, "épisodes sans résumé : %s" % manque
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    assert "</" not in js and " " not in js
    html = remplacer(html, "\n  .method-step{", "\n  /* resumes-serie:debut */\n" + CSS + "  /* resumes-serie:fin */",
                     "\n  /* resumes-serie:debut */", "/* resumes-serie:fin */")
    html = remplacer(html, "const serieDe=", "/* resumes-serie:debut */\nconst RESUMES_SERIE=" + js + ";\n" + COMP + "/* resumes-serie:fin */\n",
                     "/* resumes-serie:debut */\nconst RESUMES_SERIE=", "/* resumes-serie:fin */\n")
    branche = ',\n  React.createElement(SerieResume,{S,cur,choisir:(c,r)=>{setEp(c);if(r){const v=()=>{const el=document.getElementById("sr-"+c);if(el)el.scrollIntoView({block:"start",behavior:"instant"});};setTimeout(v,60);setTimeout(v,600);}else window.scrollTo(0,0);}})'
    html = re.sub(r',\n  React\.createElement\(SerieResume,\{S,cur,choisir:.*?\}\}\)\);\}', ');}', html, count=1)
    if "React.createElement(SerieResume," not in html:
        fin_eps = 'React.createElement("div",{className:"r"},e.r)))));}'
        assert html.count(fin_eps) == 1
        html = html.replace(fin_eps, 'React.createElement("div",{className:"r"},e.r))))' + branche + ');}')
    open(PAGE, "w", encoding="utf-8").write(html)
    print(len(data), "résumés intégrés,", len(js.encode()) // 1024, "Ko")

if __name__ == "__main__":
    main()
