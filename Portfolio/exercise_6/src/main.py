from controllers.task_manager_controller import TaskManagerController
from ui.command_line_ui import CommandLineUI

def main() -> None:
    """Main entry point for the application."""
    # Create the controller and UI
    controller = TaskManagerController()
    ui = CommandLineUI(controller)
    
    # Run the application
    ui.run()

if __name__ == "__main__":
    main()
