import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    # 1. Build Single HTML book first
    print("Building Single HTML book containing all chapters...")
    os.system("jupyter-book build . --builder singlehtml")

    # Path to the build single HTML index
    html_path = os.path.abspath("_build/singlehtml/index.html")
    pdf_path = os.path.abspath("book/Math-For-Data-Science.pdf")

    if not os.path.exists(html_path):
        print(f"Error: Single HTML build not found at {html_path}.")
        return

    # Ensure output directory for PDF exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    print("Launching browser with Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Set viewport to A4 width (210mm ≈ 794px at 96dpi) for accurate rendering
        page = await browser.new_page(viewport={"width": 794, "height": 1123})

        print(f"Loading single HTML book: {html_path}")
        await page.goto(f"file://{html_path}", wait_until="networkidle")

        # Inject comprehensive print CSS to fix layout for PDF
        print("Injecting print styles and formatting title to MATH FOR DATA SCIENCE...")
        await page.add_style_tag(content="""
            /* ===== PAGE SETUP ===== */
            @page {
                size: A4;
                margin: 18mm 15mm 18mm 15mm;
            }

            /* ===== GLOBAL RESET FOR PRINT ===== */
            * {
                box-sizing: border-box !important;
            }
            body {
                background: #ffffff !important;
                color: #1a1a1a !important;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
                font-size: 11pt !important;
                line-height: 1.6 !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
            }

            /* ===== HIDE ALL WEB-ONLY ELEMENTS ===== */
            .bd-sidebar,
            .bd-sidebar-primary,
            .bd-sidebar-secondary,
            .bd-toc,
            .bd-header,
            .bd-header-article,
            .bd-footer,
            .topbar,
            .prev-next-area,
            #site-navigation,
            .headerlink,
            .search-button,
            .theme-switch-button,
            .navbar,
            nav,
            footer,
            .footer,
            .bd-footer-article,
            .bd-footer-content,
            #pst-back-to-top,
            .pst-breadcrumbs,
            .bd-header-announcement {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
                overflow: hidden !important;
            }

            /* ===== BREAK THE CSS GRID LAYOUT ===== */
            /* Jupyter Book uses CSS grid with sidebar columns. Force single column. */
            .bd-page-width {
                max-width: 100% !important;
                width: 100% !important;
            }
            .bd-container {
                display: block !important;
                max-width: 100% !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .bd-container .row,
            .bd-main .container-xl {
                display: block !important;
                max-width: 100% !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .bd-main {
                display: block !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                grid-template-columns: 1fr !important;
            }
            .bd-content {
                display: block !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .bd-article-container {
                display: block !important;
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .bd-article {
                width: 100% !important;
                max-width: 100% !important;
                padding: 0 !important;
            }
            main, article {
                width: 100% !important;
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                box-shadow: none !important;
            }
            /* Container overrides */
            .container, .container-fluid, .container-lg, .container-xl {
                max-width: 100% !important;
                width: 100% !important;
                padding-left: 0 !important;
                padding-right: 0 !important;
                margin: 0 !important;
            }

            /* ===== SPHINX-DESIGN GRID CARDS (fix overlap) ===== */
            .sd-row {
                display: flex !important;
                flex-wrap: wrap !important;
                gap: 12px !important;
                margin: 15px 0 !important;
            }
            .sd-col,
            .sd-col-4, .sd-col-6, .sd-col-8, .sd-col-12,
            [class*="sd-col-xs-"], [class*="sd-col-sm-"],
            [class*="sd-col-md-"], [class*="sd-col-lg-"] {
                flex: 1 1 45% !important;
                max-width: 48% !important;
                min-width: 200px !important;
                width: auto !important;
            }
            .sd-card {
                border: 1px solid #e2e8f0 !important;
                border-radius: 8px !important;
                padding: 12px !important;
                margin-bottom: 10px !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                overflow: visible !important;
                background: #ffffff !important;
            }

            /* ===== COVER PAGE ===== */
            .book-cover-container {
                height: auto !important;
                min-height: 85vh !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-items: center !important;
                border-radius: 0 !important;
                margin: 0 -15mm !important;
                padding: 60px 40px !important;
                border: none !important;
                box-shadow: none !important;
                page-break-after: always !important;
                break-after: page !important;
            }
            .book-cover-title {
                font-size: 3.2rem !important;
                font-weight: 900 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.05em !important;
                /* For print, use solid color since gradients may not render */
                color: #4f46e5 !important;
                -webkit-text-fill-color: #4f46e5 !important;
            }
            .book-cover-subtitle {
                font-size: 1.3rem !important;
                color: #64748b !important;
            }
            .book-cover-author {
                font-size: 1.1rem !important;
                color: #2563eb !important;
            }

            /* ===== PAGE BREAK RULES ===== */
            h1 {
                page-break-before: always !important;
                break-before: page !important;
                margin-top: 0 !important;
                padding-top: 10px !important;
            }
            /* Don't break before the very first h1 (cover) */
            article > section:first-child > h1:first-child,
            .bd-article > section:first-child > h1:first-child {
                page-break-before: avoid !important;
                break-before: avoid !important;
            }
            h2, h3 {
                page-break-after: avoid !important;
                break-after: avoid !important;
            }
            pre, code, table, figure, img, .sd-card {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }

            /* ===== IMAGES ===== */
            img {
                max-width: 100% !important;
                height: auto !important;
            }

            /* ===== CODE BLOCKS ===== */
            pre {
                white-space: pre-wrap !important;
                word-wrap: break-word !important;
                overflow: visible !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 6px !important;
                padding: 10px !important;
                font-size: 9pt !important;
                background: #f8fafc !important;
            }

            /* ===== TABLES ===== */
            table {
                width: 100% !important;
                border-collapse: collapse !important;
                font-size: 10pt !important;
            }
            th, td {
                border: 1px solid #cbd5e1 !important;
                padding: 6px 10px !important;
            }

            /* ===== SUPPORT / DONATION SECTION ===== */
            /* Hide the donation section in PDF — not relevant for offline reading */
            [style*="display: flex"][style*="justify-content: center"] {
                display: none !important;
            }

            /* ===== MATH (MathJax) ===== */
            .MathJax, .MathJax_Display, mjx-container {
                overflow: visible !important;
                page-break-inside: avoid !important;
            }
        """)

        # Wait for MathJax formulas and images to render fully
        print("Waiting for formulas and math assets to render...")
        await asyncio.sleep(5)

        # Print all sections to PDF
        print("Generating complete book PDF (A4 Format)...")
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"}
        )
        
        await browser.close()
        print(f"Success! Full PDF saved to: {pdf_path}")

        # Re-build normal HTML so the website has separate pages
        print("Restoring standard HTML pages for web view...")
        os.system("jupyter-book build .")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
