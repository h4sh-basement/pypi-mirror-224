from rich.console import Console
from rich.table import Table
from rich import box
from typing import Union, Any
import click
from .client import HomeClient
from .scanner import Scanner

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def get_version():
    from pkg_resources import get_distribution
    return get_distribution("xhac").version


def print_version(context: click.Context, param: Union[click.Option, click.Parameter], value: bool) -> Any:
    """Print the version of mbed-tools."""
    if not value or context.resilient_parsing:
        return
    click.echo(get_version())
    context.exit()


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Display versions.",
)
def cli() -> None:
    """The MXCHIP Home Access Client Tool."""
    pass


@click.command()
def scan() -> None:
    """Scan for MXCHIP Home Access Server on local network.

    Example:

        $ xhac scan
    """
    scanner = Scanner()
    click.echo("Scanning for servers ...")
    scanner.scan()

    if len(scanner.servers) == 0:
        click.echo("No server found")
        return

    table = Table(title="Servers", box=box.ROUNDED)
    table.add_column("Name")
    table.add_column("Model")
    table.add_column("MAC")
    table.add_column("Host")
    for index, server in enumerate(scanner.servers):
        table.add_row(server.name, server.model, server.mac, f"{server.ip}:{server.port}")
    console = Console()
    console.print(table)


@click.command()
@click.argument("host", type=click.STRING)
@click.argument("mac", type=click.STRING)
@click.argument("password", type=click.STRING)
def info(host: str, mac: str, password: str) -> None:
    """Connect to MXCHIP Home Access Server and load Home model.

    Arguments:

        HOST : Format <IP>:<Port>, 192.168.31.66:52348.

        USERNAME: Username of the server.

        PASSWORD: Password of the server.

    Example:

        $ xhac info 192.168.31.66:52348 SGW2052 mxchip123
    """

    ip, port = host.split(":")

    click.echo(f"Connecting to {ip}:{port} ...")
    client = HomeClient(ip, int(port), mac, password)

    if not client.connect():
        click.echo("Failed to connect")
        return

    console = Console()

    table = Table(title="Scenes", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    for scene in client.home_db["scenes"]:
        table.add_row(f"{scene['sid']}", scene["name"])
    console.print(table)

    table = Table(title="Rooms", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    for zone in client.home_db["zones"]:
        table.add_row(f"{zone['zid']}", zone["name"])
    console.print(table)

    def FindZone(zid):
        for zone in client.home_db["zones"]:
            if zone["zid"] == zid:
                return zone["name"]
        return "Unknown"

    table = Table(title="Devices", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Room")
    for device in client.home_db["devices"]:
        table.add_row(f"{device['did']}", device["name"],
                      FindZone(device["zid"]))
    console.print(table)


def main():
    cli.add_command(scan, "scan")
    cli.add_command(info, "info")
    cli()


if __name__ == "__main__":
    main()
