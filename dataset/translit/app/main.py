from fastapi import FastAPI
import torch, argparse

from utils import (
    Input,
    LANG_INFO,
    SRC_SCRIPT_TYPES_INFO,
)

from ai4bharat.transliteration import XlitEngine


# required for ai4bharat checkpoints
torch.serialization.add_safe_globals([argparse.Namespace])

app = FastAPI(title="Indic Transliteration API")

# cache engines per (src, lang)

ENGINE = XlitEngine(
        beam_width=10,
        rescore=False,
        src_script_type="roman",
    )

def get_engine():
    return ENGINE


@app.post("/transliterate/sentence")
async def transliterate_sentence(data: Input):
    engine = get_engine()
    output = engine.translit_sentence(
        data.text,
    )

    return {
        "input": data.text,
        "output": output,
    }


@app.get("/lang/list")
async def list_langs():
    return {
        "lang_codes": LANG_INFO,
        "src_script_types": SRC_SCRIPT_TYPES_INFO,
    }

