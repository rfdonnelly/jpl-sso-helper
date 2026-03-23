from playwright.sync_api import sync_playwright

import sys
import yaml

def main():
    url = sys.argv[1]

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(viewport={"width": 500, "height": 700})
        page = context.new_page()
        page.goto(url)
        page.wait_for_url(url)
        print(yaml.dump(context.cookies()))

if __name__ == "__main__":
    main()
