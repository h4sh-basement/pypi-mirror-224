# Copyright 2023 Rapyuta Robotics
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import click
from click_help_colors import HelpColorsCommand

from riocli.config import new_client
from riocli.constants import Colors, Symbols
from riocli.static_route.util import name_to_guid
from riocli.utils.spinner import with_spinner


@click.command(
    'delete',
    cls=HelpColorsCommand,
    help_headers_color=Colors.YELLOW,
    help_options_color=Colors.GREEN,
)
@click.option('--force', '-f', is_flag=True, default=False, help='Skip confirmation')
@click.argument('static-route', type=str)
@name_to_guid
@with_spinner(text="Deleting static route...")
def delete_static_route(
        static_route: str,
        static_route_guid: str,
        force: bool,
        spinner=None,
) -> None:
    """
    Deletes a static route
    """
    with spinner.hidden():
        if not force:
            click.confirm(
                'Deleting static route {} ({})'.format(
                    static_route, static_route_guid), abort=True)

    try:
        client = new_client()
        client.delete_static_route(static_route_guid)
        spinner.text = click.style(
            'Static Route deleted successfully ', fg=Colors.GREEN)
        spinner.green.ok(Symbols.SUCCESS)
    except Exception as e:
        spinner.text = click.style('Failed to delete static route: {}'.format(e), fg=Colors.RED)
        spinner.red.fail(Symbols.ERROR)
        raise SystemExit(1)
