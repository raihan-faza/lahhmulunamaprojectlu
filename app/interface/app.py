from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Input, Static


class Lahh(App):
    messages = []
    TITLE = "Guiless chatapp, yep yap yip"
    SUB_TITLE = "don't ask me how to exit the app"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(
            key="delete",
            action="delete",
            description="Delete the thing",
        ),
        Binding(
            key="j",
            action="down",
            description="Scroll down",
        ),
        Binding(
            key="k",
            action="up",
            description="Scroll up",
        ),
    ]
    CSS = """
    #message-display{
        height:15fr;
    }

    #input-bar{
        height:1fr;
        margin-bottom:1;
    }
    """

    def on_mount(self):
        self.theme = "gruvbox"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Main Content", id="message-display")
        yield Input(placeholder="Type here...", id="input-bar")
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""

        # Add the new message to the message list
        self.messages.append(event.value.strip())

        # Render only the latest state of the message list
        self.query_one("#message-display", Static).update(f"{self.messages}")

        # Clear the input bar
        event.input.value = ""
