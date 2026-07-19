import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    # 1. Build Single HTML book first
    print("Building Single HTML book containing all chapters...")
    os.system("jupyter-book build . --builder singlehtml")

    # Path to the build single HTML index
    html_path = os.path.abspath("_build/html/index.html")
    pdf_path = os.path.abspath("book/book.pdf")

    if not os.path.exists(html_path):
        print(f"Error: Single HTML build not found at {html_path}.")
        return

    # Ensure output directory for PDF exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    print("Launching browser with Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"Loading single HTML book: {html_path}")
        await page.goto(f"file://{html_path}", wait_until="networkidle")

        # Wait for MathJax and scripts to load fully
        print("Waiting for formulas and math assets to render...")
        await asyncio.sleep(6)

        # Print all sections to PDF
        print("Generating complete book PDF (this may take a few seconds)...")
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
        )
        
        await browser.close()
        print(f"Success! Full PDF saved to: {pdf_path}")

        # Re-build normal HTML so the website has separate pages
        print("Restoring standard HTML pages for web view...")
        os.system("jupyter-book build .")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
