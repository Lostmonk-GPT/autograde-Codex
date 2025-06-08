from autograding_scripts.gpt_formatter import format_prompt, parse_gpt_response
from autograding_scripts.config import load_settings


def test_prompt_and_parse():
    settings = load_settings()
    prompt = format_prompt('x=1', settings.rubric, settings.rubric_definitions)
    assert '=== COPY TO GPT ===' in prompt
    data = parse_gpt_response('{"score": 5, "comments": "ok"}')
    assert data['score'] == 5
