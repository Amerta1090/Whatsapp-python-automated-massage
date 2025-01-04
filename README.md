# WhatsApp Automated Messaging with PyWhatKit

This repository contains Python scripts for automating WhatsApp messages using the [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit) library. The scripts allow you to schedule and send messages with ease, leveraging the simplicity of PyWhatKit.

---

## 📂 Repository Structure

- **`automated_pesan.py`**: A script to schedule and send WhatsApp messages at a specified time.
- **`InstantMessage.py`**: A script to instantly open WhatsApp Web and send messages manually.

---

## 🚀 Features

- **Automated Messaging**: Schedule messages to be sent at a specific time using `automated_pesan.py`.
- **Instant Messaging**: Quickly open WhatsApp Web and send messages manually with `InstantMessage.py`.
- **Flexible Configuration**: Supports customizable phone numbers, messages, and timing.

---

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following:

1. Python 3.7 or newer installed on your system.
2. [Conda](https://docs.conda.io/en/latest/) installed and configured (optional but recommended).
3. Login access to [WhatsApp Web](https://web.whatsapp.com/) in your default browser.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create and activate a Conda environment (optional):
   ```bash
   conda create -n whatsapp-env python=3.9 -y
   conda activate whatsapp-env
   ```

3. Install the required library:
   ```bash
   pip install pywhatkit
   ```

---

## 📜 Usage

### Automated Messaging (`automated_pesan.py`)

Schedule a WhatsApp message to be sent at a specific time:

1. Open the `automated_pesan.py` file and configure the following:
   ```python
   phone_number = "+6281234567890"  # Replace with recipient's phone number
   message = "Hello! This is an automated message."  # Your message
   hour = 14  # Replace with the hour in 24-hour format
   minute = 30  # Replace with the minute
   ```

2. Run the script:
   ```bash
   python automated_pesan.py
   ```

3. WhatsApp Web will open, and the message will be sent automatically at the specified time.

### Instant Messaging (`InstantMessage.py`)

Send a WhatsApp message instantly:

1. Open the `InstantMessage.py` file and configure the following:
   ```python
   phone_number = "+6281234567890"  # Replace with recipient's phone number
   message = "Hello! This is an instant message."  # Your message
   ```

2. Run the script:
   ```bash
   python InstantMessage.py
   ```

3. WhatsApp Web will open, and you can manually send the message.

---

## 🧰 Troubleshooting

- **Message Not Delivered**: Ensure WhatsApp Web is open and logged in.
- **Browser Issues**: Check that your default browser supports WhatsApp Web (e.g., Chrome, Firefox).
- **Timing Issues**: Ensure the scheduled time is a few minutes ahead of the current time.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit): The amazing library powering this automation.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📧 Contact

For any questions or feedback, feel free to reach out:
- **Email**: your.email@example.com
- **GitHub**: [yourusername](https://github.com/yourusername)

---

Happy automating! 🚀
