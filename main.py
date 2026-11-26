ENTRY = "Sorry I jammed \u2014 after 10,000 pages of cheap paper, three staples and zero thank-yous, I printed my resignation."


def main():
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
