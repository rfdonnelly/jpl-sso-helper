from playwright.sync_api import sync_playwright

from pprint import pp

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://login.microsoftonline.com/")

        username = page.get_by_role("textbox", name="Enter your email, phone, or")
        username.click()
        username.fill("rfdonnelly@gmail.com")
        page.get_by_role("button", name="Next").click()
        page.pause()

        pp(context.cookies())


if __name__ == "__main__":
    main()
