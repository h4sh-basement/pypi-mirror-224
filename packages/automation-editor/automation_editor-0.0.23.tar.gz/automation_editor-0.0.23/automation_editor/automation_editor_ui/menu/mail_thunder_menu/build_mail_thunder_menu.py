from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
import sys
import webbrowser

from PySide6.QtGui import QAction

from automation_editor.extend.process_executor.mail_thunder.mail_thunder_process import call_mail_thunder


def set_mail_thunder_menu(ui_we_want_to_set: AutomationEditor):
    """
    Build menu include LoadDensity feature.
    :param ui_we_want_to_set: main window to add menu.
    :return: None
    """
    ui_we_want_to_set.mail_thunder_menu = ui_we_want_to_set.menu.addMenu("MailThunder")
    ui_we_want_to_set.mail_thunder_run_menu = ui_we_want_to_set.mail_thunder_menu.addMenu("Run")
    # Run MailThunder
    ui_we_want_to_set.run_mail_thunder_action = QAction("Run MailThunder")
    ui_we_want_to_set.run_mail_thunder_action.triggered.connect(
        lambda: call_mail_thunder(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.mail_thunder_run_menu.addAction(
        ui_we_want_to_set.run_mail_thunder_action
    )
    # Help menu
    ui_we_want_to_set.mail_thunder_help_menu = ui_we_want_to_set.mail_thunder_menu.addMenu("HELP")
    # Open Github
    ui_we_want_to_set.open_mail_thunder_github_action = QAction("Open MailThunder GitHub")
    ui_we_want_to_set.open_mail_thunder_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Integration-Automation/MailThunder"
        )
    )
    ui_we_want_to_set.mail_thunder_help_menu.addAction(
        ui_we_want_to_set.open_mail_thunder_github_action
    )
    ui_we_want_to_set.mail_thunder_project_menu = ui_we_want_to_set.mail_thunder_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_mail_thunder_project_action = QAction("Create MailThunder Project")
    ui_we_want_to_set.create_mail_thunder_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.mail_thunder_project_menu.addAction(
        ui_we_want_to_set.create_mail_thunder_project_action
    )


def open_web_browser(url: str) -> None:
    webbrowser.open(url=url)


def create_project() -> None:
    try:
        import je_mail_thunder
        package = je_mail_thunder
        if package is not None:
            package.create_project_dir()
    except ImportError as error:
        print(repr(error), file=sys.stderr)
