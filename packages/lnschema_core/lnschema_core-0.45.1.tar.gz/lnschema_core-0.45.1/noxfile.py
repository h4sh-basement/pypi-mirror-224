import nox
from laminci.nox import login_testuser1, run_pre_commit, run_pytest  # noqa

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session
def test(session: nox.Session) -> None:
    session.run(*"pip install -e .[dev]".split())
    login_testuser1(session)
    run_pytest(session, coverage=False)
