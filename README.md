
# Bitcoin Price Change Alert Robot

## Overview

The Bitcoin Price Change Alert Robot is a Python application that monitors Bitcoin price fluctuations and provides audible alerts when certain thresholds are crossed. This tool helps users stay informed about significant price changes.

## Features

- Real-time monitoring of Bitcoin price.
- Audible alerts for price increase or decrease.
- Adjustable price thresholds.
- Console output for current price and thresholds.

## Requirements

- Python 3.11.6 or higher
- Required Python packages: pyttsx3, pygame, tkinter (for messagebox`), and `bitcoin_value (for the currency function)

## Installation

1. Clone the repository:
   ~~~bash
   git clone https://github.com/AisDisappeared/BTC-price-change-alert-robot-.git
   ~~~
2. Navigate to the project directory:
   ~~~bash
   cd BTC-price-change-alert-robot-
   ~~~
3. Install the required Python packages. Make sure to have the pygame and pyttsx3 libraries installed:
   ~~~bash
   pip install -r requirements.txt
   ~~~
   Additionally, ensure the bitcoin_value package is installed and accessible. If it's not available via pip, make sure the module is in your project directory or accessible from your Python environment.

4. Place up.mp3 and down.mp3 files in the same directory as the script for audio alerts.

## Usage

Run the application using:
~~~bash
python3 python-btc.py
~~~
The application will monitor the Bitcoin price and provide audible alerts through the up.mp3 and down.mp3 files when the price crosses the configured thresholds.

## Alerts

- Price Increase: If the price exceeds the high threshold, an audible alert will play using up.mp3, and the thresholds will increase by the specified amount.
- Price Decrease: If the price falls below the low threshold, an audible alert will play using down.mp3, and the thresholds will decrease by the specified amount.

## Contributing

If you wish to contribute to the project, please fork the repository, create a new branch for your changes, and submit a pull request. Ensure your code adheres to the project's style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [Aliseyfi0841@gmail.com](mailto:Aliseyfi0841@gmail.com).