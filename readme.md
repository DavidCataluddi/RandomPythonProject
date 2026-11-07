# Quotes Scraper 🐍🕷️

A lightweight Python web scraper built with **Requests** and **BeautifulSoup** to extract quotes, authors, and associated tags from [Quotes to Scrape](https://quotes.toscrape.com/).

---

## 📌 Features

- **Automated HTTP Requests:** Retrieves HTML content directly from the target site.
- **HTML Parsing:** Parses structure using `BeautifulSoup` to locate relevant data blocks easily.
- **Structured Output:** Formats each entry with:
  - 💬 **Quote Text**
  - 👤 **Author Name**
  - 🏷️ **Associated Tags**

---

## 🛠️ Prerequisites & Installation

Ensure you have Python 3.x installed on your system.

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/your-username/quotes-scraper.git
   cd quotes-scraper
   ```

2. **Install required packages:**
   ```bash
   pip install requests beautifulsoup4
   ```

---

## 🚀 Usage

Run the script directly from your terminal:

```bash
python main.py
```

---

## 📋 Output Example

When executed, the console output will look similar to this:

```text
Connexion réussie !

Citation : “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Auteur : Albert Einstein
Tags : change, deep-thoughts, thinking, world
----------------------------------------
Citation : “It is our choices, Harry, that show what we truly are, far more than our abilities.”
Auteur : J.K. Rowling
Tags : abilities, choices
----------------------------------------
```

---

## 🎯 Future Enhancements

- [ ] Add pagination support to scrape all pages.
- [ ] Export scraped data to `.csv` or `.json` files.
- [ ] Implement command-line arguments to filter by author or tag.