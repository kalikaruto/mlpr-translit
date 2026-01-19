import requests
from pathlib import Path

BACKEND_URL = "http://localhost:8000/transliterate/sentence"
DATA_DIR = Path("data")
EN_DIR = DATA_DIR / "english"

LANG_INFO = [
    {"code": "as", "label": "assamese"},
    {"code": "bn", "label": "bangla"},
    {"code": "brx", "label": "boro"},
    {"code": "gu", "label": "gujarati"},
    {"code": "hi", "label": "hindi"},
    {"code": "kn", "label": "kannada"},
    {"code": "ks", "label": "kashmiri"},
    {"code": "gom", "label": "konkani_goan"},
    {"code": "mai", "label": "maithili"},
    {"code": "ml", "label": "malayalam"},
    {"code": "mni", "label": "manipuri"},
    {"code": "mr", "label": "marathi"},
    {"code": "ne", "label": "nepali"},
    {"code": "or", "label": "oriya"},
    {"code": "pa", "label": "panjabi"},
    {"code": "sa", "label": "sanskrit"},
    {"code": "sd", "label": "sindhi"},
    {"code": "si", "label": "sinhala"},
    {"code": "ta", "label": "tamil"},
    {"code": "te", "label": "telugu"},
    {"code": "ur", "label": "urdu"},
]

CODE_TO_LABEL = {x["code"]: x["label"] for x in LANG_INFO}


def transliterate_sentence(text: str) -> dict:
    r = requests.post(
        BACKEND_URL,
        json={"text": text},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["output"]  # dict: lang_code -> text


def process_file(txt_file: Path):
    lines = txt_file.read_text(encoding="utf-8").splitlines()

    # prepare output buffers per language
    buffers = {label: [] for label in CODE_TO_LABEL.values()}

    for line in lines:
        if not line.strip():
            for buf in buffers.values():
                buf.append("")
            continue

        out_map = transliterate_sentence(line)

        for code, label in CODE_TO_LABEL.items():
            buffers[label].append(out_map.get(code, ""))

    # write outputs
    for label, out_lines in buffers.items():
        out_dir = DATA_DIR / label
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / txt_file.name
        out_path.write_text("\n".join(out_lines), encoding="utf-8")


def main():
    if not EN_DIR.exists():
        raise RuntimeError("data/english directory not found")

    for txt_file in sorted(EN_DIR.glob("*.txt")):
        process_file(txt_file)


if __name__ == "__main__":
    main()

