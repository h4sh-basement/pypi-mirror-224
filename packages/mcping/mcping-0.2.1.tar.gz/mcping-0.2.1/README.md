# mcping [![Build Badge]](https://gitlab.com/MysteryBlokHed/mcping/-/pipelines) [![Docs Badge]](https://mcping.readthedocs.io/en/latest/) [![License Badge]](#license)

Get statuses from Minecraft servers.

## Difference between this and mcstatus

This package uses some classes and functions from [mcstatus].

The primary goal of this package is to simply get the raw status without doing any other parsing.
Although mcstatus does provide a `raw` property to get the raw response,
there is no straightforward way to _only_ get this response.
This results in time wasted doing processing that isn't needed for some applications.

A side effect of this is that there isn't any guarantee that the status response
will have all of the keys that it should, meaning you'll need to do some validation
before assuming that keys are present, or that they're the types you think.  
In the situation that led me to make this package, this is completely fine.

## Docs

Documentation is available at <https://mcping.readthedocs.io>.

## Installation

If you want to use the library, install with `pip`:

```sh
pip install mcping
```

If you only want the CLI, `pipx` is recommended:

```sh
pipx install mcping
```

## Use

### Library

```python
import mcping

# Synchronous
mcping.status('127.0.0.1')

# Asynchronous
async def main():
    await mcping.async_status('127.0.0.1')
```

### CLI

The package also includes a CLI to get server statuses.
It can be run from a cloned repo using the `cli.py` file:

```sh
python3 cli.py example.com
python3 cli.py example.com:25565
```

If the library is installed, the `mcping` script should also be installed and available globally:

```sh
mcping example.com
mcping example.com:25565
```

## License

This project is licensed under either of

- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or
  <http://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or
  <http://opensource.org/licenses/MIT>)

at your option.

Some code in `mcping/__init__.py` is modified from the [mcstatus] project's code,
licensed under the Apache License, Version 2.0.

[build badge]: https://img.shields.io/gitlab/pipeline-status/MysteryBlokHed/mcping
[docs badge]: https://img.shields.io/readthedocs/mcping
[license badge]: https://img.shields.io/badge/license-MIT%20or%20Apache--2.0-green
[mcstatus]: https://github.com/py-mine/mcstatus
