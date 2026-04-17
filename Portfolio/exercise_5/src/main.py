# main.py
from controllers.task_manager_controller import TaskManagerController
from ui.command_line_ui import CommandLineUI

# Entry point of the application
def main():
    # Separation of concerns: connect UI and controller
    controller = TaskManagerController()
    ui = CommandLineUI(controller)
    ui.run()

if __name__ == "__main__":
    main()

