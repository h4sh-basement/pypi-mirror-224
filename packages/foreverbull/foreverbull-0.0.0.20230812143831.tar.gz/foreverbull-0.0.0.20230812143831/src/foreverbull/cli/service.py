import time

import typer
from rich.console import Console
from typing_extensions import Annotated

from foreverbull import broker

name = Annotated[str, typer.Argument(help="service name")]
image = Annotated[str, typer.Argument(help="service image")]

service = typer.Typer()

std = Console()
std_err = Console(stderr=True)


@service.command()
def create(name: name, image: image):
    service = broker.service.create(name, image)
    status = service["status"]
    std.log("Created successfully")
    for _ in range(50):
        service = broker.service.get(name)
        if service["status"] != status:
            status = service["status"]
            std.log("Status: ", status)
        if status == "READY":
            std.log("Service is ready")
            break
        time.sleep(0.5)
