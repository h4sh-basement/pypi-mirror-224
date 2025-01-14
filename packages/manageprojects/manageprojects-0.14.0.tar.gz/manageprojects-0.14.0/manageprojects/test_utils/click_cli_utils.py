from unittest.mock import patch

import click
import rich_click
from bx_py_utils.path import assert_is_file
from bx_py_utils.test_utils.context_managers import MassContextManager
from cli_base.cli_tools.subprocess_utils import verbose_check_output
from click.testing import CliRunner, Result


TERMINAL_WIDTH = 100


def subprocess_cli(*, cli_bin, args, exit_on_error=True):
    assert_is_file(cli_bin)
    return verbose_check_output(
        cli_bin,
        *args,
        cwd=cli_bin.parent,
        extra_env=dict(TERMINAL_WIDTH=str(TERMINAL_WIDTH)),
        exit_on_error=exit_on_error,
    )


class ForceRichTerminalWidth(MassContextManager):
    mocks = (
        patch.object(rich_click.rich_click, 'MAX_WIDTH', TERMINAL_WIDTH),
        patch.object(rich_click.rich_click, 'FORCE_TERMINAL', False),
    )


class ClickInvokeCliException(Exception):
    def __init__(self, result: Result):
        self.result = result


def invoke_click(cli, *args, expected_stderr='', expected_exit_code=0, strip=True, **kwargs):
    assert isinstance(cli, click.Command)

    args = tuple([str(arg) for arg in args])  # e.g.: Path() -> str

    with ForceRichTerminalWidth():
        runner = CliRunner(mix_stderr=False)
        result: Result = runner.invoke(cli=cli, args=args, **kwargs, color=False)

    if result.exception:
        raise ClickInvokeCliException(result) from result.exception

    stdout = result.stdout
    stderr = result.stderr
    assert stderr == expected_stderr, f'{stderr!r} is not {expected_stderr!r}'
    assert (
        result.exit_code == expected_exit_code
    ), f'Exit code {result.exit_code} is not {expected_exit_code}\n{stdout}\n{stderr}'

    if strip:
        stdout = '\n'.join(line.rstrip() for line in stdout.splitlines())
        stdout = stdout.strip()
    return stdout
