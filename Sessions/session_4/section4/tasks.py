class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title: str = title
        self.description: str = description
        self.completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def is_completed(self) -> bool:
        return self.completed

    def __str__(self) -> str:
        status: str = "Completed" if self.completed else "Not Completed"
        return f"{self.title} - {self.description} ({status})"