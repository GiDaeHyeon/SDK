import typer
from rich import print

from tasks import (
    env_manager,
    mongo_manager
)

LOGO_ = """
    ____  __  __   _____ ____  __ __    ______            __
   / __ \/ / / /  / ___// __ \/ //_/   /_  __/___  ____  / /
  / / / / /_/ /   \__ \/ / / / ,<       / / / __ \/ __ \/ / 
 / /_/ / __  /   ___/ / /_/ / /| |     / / / /_/ / /_/ / /  
/_____/_/ /_/   /____/_____/_/ |_|    /_/  \____/\____/_/   
                                                            
"""
app = typer.Typer()


if __name__ == "__main__":
    print(LOGO_)
    app.add_typer(env_manager.app, name="dot_manager")
    app()
