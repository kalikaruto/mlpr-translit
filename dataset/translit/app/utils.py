from enum import Enum
from pydantic import BaseModel


class Lang(str, Enum):
    as_ = "as"
    bn  = "bn"
    brx = "brx"
    gu  = "gu"
    hi  = "hi"
    kn  = "kn"
    ks  = "ks"
    gom = "gom"
    mai = "mai"
    ml  = "ml"
    mni = "mni"
    mr  = "mr"
    ne  = "ne"
    or_ = "or"
    pa  = "pa"
    sa  = "sa"
    sd  = "sd"
    si  = "si"
    ta  = "ta"
    te  = "te"
    ur  = "ur"


class SrcLang(str, Enum):
    roman = "roman"
    indic = "indic"


class Input(BaseModel):
    text: str


LANG_INFO = [
    {"code": "as", "label": "Assamese - অসমীয়া"},
    {"code": "bn", "label": "Bangla - বাংলা"},
    {"code": "brx", "label": "Boro - बड़ो"},
    {"code": "gu", "label": "Gujarati - ગુજરાતી"},
    {"code": "hi", "label": "Hindi - हिंदी"},
    {"code": "kn", "label": "Kannada - ಕನ್ನಡ"},
    {"code": "ks", "label": "Kashmiri - كٲشُر"},
    {"code": "gom", "label": "Konkani Goan - कोंकणी"},
    {"code": "mai", "label": "Maithili - मैथिली"},
    {"code": "ml", "label": "Malayalam - മലയാളം"},
    {"code": "mni", "label": "Manipuri - ꯃꯤꯇꯩꯂꯣꯟ"},
    {"code": "mr", "label": "Marathi - मराठी"},
    {"code": "ne", "label": "Nepali - नेपाली"},
    {"code": "or", "label": "Oriya - ଓଡ଼ିଆ"},
    {"code": "pa", "label": "Panjabi - ਪੰਜਾਬੀ"},
    {"code": "sa", "label": "Sanskrit - संस्कृतम्"},
    {"code": "sd", "label": "Sindhi - سنڌي"},
    {"code": "si", "label": "Sinhala - සිංහල"},
    {"code": "ta", "label": "Tamil - தமிழ்"},
    {"code": "te", "label": "Telugu - తెలుగు"},
    {"code": "ur", "label": "Urdu - اُردُو"},
]

SRC_SCRIPT_TYPES_INFO = [
    {"code": "roman", "label": "Roman - English"},
    {"code": "indic", "label": "Indic - Indic"},
]

