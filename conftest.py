from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import url

@pytest.fixture(scope="session")
def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    #context = browser.new_context(ignore_https_errors=True)
    context = browser.new_context(
    ignore_https_errors=True,
    record_video_dir="videos",
    record_video_size={"width": 1280, "height": 720}
)
    page = context.new_page()
    page.goto(url)
    page.wait_for_load_state("load")

    yield page
    video = page.video
    context.close()
    if video:
        print("Video saved at:", video.path())
    browser.close()
    p.stop()


#To Capture screenshort
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(pytest_html.extras.image(str(file_name)))

        report.extra = extra
