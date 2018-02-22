# base56
human-readable binary encoding

## This project
base56 is a side project for a side project.
Its primary use is to implement base56 encoding for
[bitshuffle](https://github.com/charlesdaniels/bitshuffle/issues/3).

## Base56
base56 is a variant of [base58](https://en.wikipedia.org/wiki/Base58)
omitting the characters '1' and 'o' to avoid confusion.
Its purpose is to make it easy to both type and copy/paste encoded data.

## Technical details
### Specification
base56 translates the binary values from 0-55 to their counterpart
in the following alphabet:
`23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz`

### Version number conventions

base56 loosely follows [Semantic Versioning](https://semver.org).
The following suffixes are used:

- No suffix - stable release
- `-git` - from the base56 git repository; unstable
- `-RCX` - `X`th release candidate for the relevant version; testing
