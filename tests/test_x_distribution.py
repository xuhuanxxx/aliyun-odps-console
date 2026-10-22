from maxc_cli.utils import current_cli_entry_point, distribution_cli_text
from maxc_cli.bearer_auth import BearerAuthConfig
from maxc_cli.agent_platforms import INVOCATIONS


def test_x_command_does_not_inherit_official_launcher(monkeypatch):
    monkeypatch.setattr('sys.argv', ['/opt/homebrew/bin/maxcx'])
    monkeypatch.setenv('MAXC_CLI_NAME', 'aliyun maxc')
    assert current_cli_entry_point() == 'maxcx'
    assert distribution_cli_text('Run maxc job wait JOB') == 'Run maxcx job wait JOB'
    assert BearerAuthConfig().cli == 'aliyunx'
    assert BearerAuthConfig(cli='/custom/aliyun').cli == '/custom/aliyun'
    assert INVOCATIONS['maxcx']['cli'] == 'maxcx'


def test_upstream_command_keeps_existing_default(monkeypatch):
    monkeypatch.setattr('sys.argv', ['maxc'])
    monkeypatch.delenv('MAXC_CLI_NAME', raising=False)
    assert current_cli_entry_point() == 'maxc'
    assert BearerAuthConfig().cli == 'aliyun'
