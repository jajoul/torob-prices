# torob-prices

[![PyPI version](https://badge.fury.io/py/torob-prices.svg)](https://badge.fury.io/py/torob-prices)

A simple web scraper to find the lowest price of a product on the Torob website.

## Description

`torob-prices` is a command-line tool that allows you to quickly find the prices of a product on [Torob](https://torob.com/), a popular price comparison website in Iran. You can either get a list of all the prices found or just the minimum price.

## Installation

```bash
pip install torob-prices
```

## Usage

Run the script from your terminal:

```bash
torob-prices "your product name"
```

For example:

```bash
torob-prices "iphone 15 pro max"
```

### Options

*   `--min`: Only display the minimum price.
*   `--base_url`: Override the default search URL (`https://torob.com/search/`).

#### Example with options:

```bash
torob-prices "samsung s23 ultra" --min
```

## Contributing

Contributions are welcome! Please see the [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
