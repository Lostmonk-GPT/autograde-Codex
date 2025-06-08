import importlib

MODULES = [
    'autograding_scripts.ocr_processor',
    'autograding_scripts.symbol_corrector',
    'autograding_scripts.gpt_formatter',
    'autograding_scripts.pdf_generator',
    'autograding_scripts.config',
]

def test_imports():
    for mod in MODULES:
        importlib.import_module(mod)
