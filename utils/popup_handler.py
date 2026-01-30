def dismiss_popups(page):
    selectors = [
        "button.accept",
        ".modal-close",
        ".popup-close"
    ]

    for selector in selectors:
        try:
            if page.locator(selector).count() > 0:
                page.locator(selector).first.click()
        except:
            pass
