from autograding_scripts.config import load_settings


def test_load_settings(tmp_path, monkeypatch):
    monkeypatch.setenv('INPUT_DIR', str(tmp_path))
    settings = load_settings()
    assert settings.input_dir.exists()
    assert 'default' in settings.rubric_definitions
