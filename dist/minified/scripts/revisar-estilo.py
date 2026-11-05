"""
Validador de estilo editorial e integridade curricular de O Último Curso (Memória de Trabalho).
Verifica:
1. Ausência de emojis, travessões, meia-riscas, hífen solto, exclamações, clichês de IA e o termo proibido "Civic Tech".
2. Integridade do arquivo `data/curriculum.json` (3 ciclos, 20 módulos, soma de horas e existência de cada `markdownPath` em `trilhas/`).
"""
import json
import re
import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
CURRICULUM_JSON = ROOT_DIR / "data" / "curriculum.json"
TRAVESSAO = re.compile(r"[\u2014\u2013]")
HIFEN_SOLTO = re.compile(r"[\wÀ-ú,] - [\wÀ-ú]")
EMOJI = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U0000FE0F"
    "]+"
)
FORMULA = [
    re.compile(r"\bnão (?:é|era|foi|está) (?:sobre|só|apenas)\b[^.!?\n]{0,90}?[,;:]\s*(?:é|era|foi|mas)\b", re.I),
    re.compile(r"\bnão se trata de\b", re.I),
    re.compile(r"\bmais do que [^.!?\n]{1,60}, (?:é|era|foi)\b", re.I),
]
CLICHES = [
    "vale ressaltar",
    "vale destacar",
    "é importante destacar",
    "é importante ressaltar",
    "no fim do dia",
    "em suma",
    "mergulhar",
    "mergulho",
    "navegar por",
    "desvendar",
    "potencializar",
    "alavancar",
    "divisor de águas",
    "civic tech",
    "civic-tech",
]
def revisar_arquivo(caminho: Path) -> list[tuple[int, str]]:
    erros: list[tuple[int, str]] = []
    texto = caminho.read_text(encoding="utf-8")
    for n, linha in enumerate(texto.splitlines(), 1):
        if "<!-- estilo: ok -->" in linha:
            continue
        sem_url = re.sub(r"\]\([^)]*\)|https?://\S+", "]", linha)
        if TRAVESSAO.search(sem_url):
            erros.append((n, "travessão ou meia-risca"))
        if HIFEN_SOLTO.search(sem_url):
            erros.append((n, "hífen solto usado como travessão"))
        if EMOJI.search(sem_url):
            erros.append((n, "emoji encontrado"))
        for padrao in FORMULA:
            if padrao.search(sem_url):
                erros.append((n, "fórmula de correção dramática"))
                break
        if caminho.name not in {"ESTILO.md", "AGENTS.md"}:
            baixa = sem_url.lower()
            for cliche in CLICHES:
                if cliche in baixa:
                    erros.append((n, f"termo ou clichê proibido: '{cliche}'"))
    return erros
def revisar_curriculo() -> list[str]:
    erros: list[str] = []
    if not CURRICULUM_JSON.exists():
        return ["data/curriculum.json não encontrado"]
    data = json.loads(CURRICULUM_JSON.read_text(encoding="utf-8"))
    ciclos = data.get("cycles", [])
    if len(ciclos) != 3:
        erros.append(f"esperados 3 ciclos, encontrados {len(ciclos)}")
    modulos = [m for c in ciclos for m in c.get("modules", [])]
    if len(modulos) != 20:
        erros.append(f"esperados 20 módulos, encontrados {len(modulos)}")
    soma_horas = sum(m.get("estimatedHours", 0) for m in modulos)
    total_declarado = data.get("metadata", {}).get("totalHours", 0)
    if soma_horas != total_declarado:
        erros.append(f"soma das horas dos módulos ({soma_horas}h) difere de totalHours ({total_declarado}h)")
    for m in modulos:
        md_rel = m.get("markdownPath", "")
        if not md_rel or not (ROOT_DIR / md_rel).exists():
            erros.append(f"módulo {m.get('code')} aponta para arquivo inexistente: {md_rel}")
    return erros
def main() -> int:
    skip_dirs = {".git", "dist", "viewer", "scripts", "__pycache__", ".venv"}
    arquivos = [
        p
        for p in sorted(ROOT_DIR.rglob("*"))
        if p.is_file()
        and not p.name.startswith(".")
        and not any(part in skip_dirs for part in p.relative_to(ROOT_DIR).parts)
        and p.suffix in {".md", ".json"}
    ]
    total_erros = 0
    for arq in arquivos:
        erros = revisar_arquivo(arq)
        total_erros += len(erros)
        rel = arq.relative_to(ROOT_DIR)
        if erros:
            print(f"{rel}: {len(erros)} erro(s)")
            for n, msg in erros:
                print(f"  erro linha {n}: {msg}")
    erros_curr = revisar_curriculo()
    total_erros += len(erros_curr)
    for msg in erros_curr:
        print(f"data/curriculum.json: erro estrutural: {msg}")
    if total_erros == 0:
        print(f"OK: {len(arquivos)} arquivos e 20 módulos conferidos sem erros de estilo ou estrutura.")
        return 0
    return 1
if __name__ == "__main__":
    sys.exit(main())