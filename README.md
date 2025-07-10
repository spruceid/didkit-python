> [!IMPORTANT]
> As we do not use the DIDKit bindings internally anymore, we have decided to archive their respective repositories. If you are looking for alternatives, our Rust library [`ssi`](https://github.com/spruceid/ssi/) (on which DIDKit was built) is still in active deployment, and we have new mobile-focused libraries with [`sprucekit-mobile`](https://github.com/spruceid/sprucekit-mobile). And as always, you are welcome to fork our repositories.

[![PyPI version](https://badge.fury.io/py/didkit.svg)](https://badge.fury.io/py/didkit)

Check out the DIDKit documentation [here](https://spruceid.dev/docs/didkit/).

# DIDKit Python

DIDKit provides Verifiable Credential and Decentralized Identifier
functionality across different platforms. It was written primarily in Rust due
to Rust's expressive type system, memory safety, simple dependency web, and
suitability across different platforms including embedded systems. DIDKit
embeds the [`ssi`](https://github.com/spruceid/ssi) library, which contains the
core functionality.

## Installation and Usage

DIDKit is available [on PyPI](https://pypi.org/project/didkit/).

You can install it globally with:
```bash
$ pip install -U didkit
```

> `asyncio` is required, meaning you will need Python 3.7 or above.

## Build from Source

```bash
$ maturin build
```
> You can install `maturin` with `pip install maturin`.

Now the `wheel` should be in the [target directory](../../target/wheel).

### Custom Builds

To enable or disable certain features of DIDKit, or use different cryptography
backends, you will need edit the `Cargo.toml`.

## Development

When adding a function or changing the signature of an existing one, make sure
to reflect the changes in [the stub file](./didkit/pydidkit.pyi). This is
important for static analysis and IDE support. (This will be automated in the
future.)

## Test

```bash
poetry install
poetry run maturin develop
poetry run pytest
```

## Migration

### 0.2 to 0.3
Functions have kept the same signatures, but some have become asynchronous. You
will need to start using
[`asyncio`](https://docs.python.org/3/library/asyncio.html) if it is not already
the case.

## Maturity Disclaimer

Please note: this readme documents an early-stage open-source product ported
manually to python, and we are still incorporating feedback from our first
comprehensive third-party code audit. These artefacts are presented as
functional "betas" for experimentation and to show the direction of the
project (inviting proposals for changes of direction, even!). They are not,
 however, intended for transacting real-world business yet.
