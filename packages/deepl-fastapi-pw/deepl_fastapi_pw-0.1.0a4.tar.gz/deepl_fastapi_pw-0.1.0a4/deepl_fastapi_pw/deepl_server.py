"""
Run fastapi server pw.

deepl_scraper_pw.deel_tr is sync

python -c "from deepl_fastapi_pw import deepl_server;
import nest_asyncio; nest_asyncio.apply(); deepl_server.run_uvicorn()"
python -c "from deepl_fastapi_pw import deepl_server; deepl_server.run_uvicorn()"

greenlet.error: cannot switch to a different thread
"""
# pylint: disable=invalid-name, duplicate-code, no-name-in-module, broad-except, line-too-long
# import nest_asyncio

# import sys
# import asyncio
import os
from signal import SIG_DFL, SIGINT, signal
from typing import Optional

import nest_asyncio

# import portalocker
import uvicorn
from fastapi import FastAPI, Query
from get_pwbrowser_sync.get_pwbrowser_sync import get_pwbrowser_sync

# import logzero
from logzero import logger
from pydantic import BaseModel

from deepl_fastapi_pw import __version__

# from deepl_scraper_pw.deepl_tr import deepl_tr
from deepl_fastapi_pw.deepl_tr import deepl_tr

# lazy loading LOOP, wait for run_uvicorn to start first
# import lazy_import
# get_ppbrowser = lazy_import.lazy_module(get_ppbrowser)

port = 8001
nest_asyncio.apply()  # need this for the whole thing to work


def get_page():
    """Get a page."""
    try:
        browser = get_pwbrowser_sync()
    except Exception as exc:
        logger.error(exc)
        raise
    try:
        page = browser.new_page()
    except Exception as exc:
        logger.error(exc)
        raise

    url = r"https://www.deepl.com/translator"
    try:
        page.goto(url, timeout=16 * 1000)
    except Exception as exc:
        logger.error(exc)
        raise

    return page


# PAGE = get_page()

descr = f"""Post -d '\u007b"text": "this is a test", "to_lang": "zh" \u007d'

    to http://127.0.0.1:{port}/text/
    """


class Text(BaseModel):  # pylint: disable=too-few-public-methods
    """Define Text model."""

    text: str
    from_lang: Optional[str] = None
    to_lang: Optional[str] = None
    description: Optional[str] = descr


app = FastAPI(
    title="deepl-fastapi-pw",
    version=__version__,
)


@app.post("/text/")
def post_text(q: Text):
    """
    Post -d '\u007b"text": "this is a test", "to_lang": "zh" \u007d'.

    to http://127.0.0.1:{port}/text/
    """
    text = q.text
    to_lang = q.to_lang
    from_lang = q.from_lang
    logger.debug("text: %s", text)

    # _ = sent_corr(text1, text2)
    try:
        _ = deepl_tr(
            text,
            from_lang,
            to_lang,
            # page=PAGE,
        )
    except Exception as exc:
        logger.exception(exc)
        _ = {"error": True, "message": str(exc)}

    return {"q": q, "result": _}


@app.get("/text/")
def get_text(
    q: Optional[str] = Query(
        None,
        max_length=1500,
        min_length=1,
        title="text to translate",
        description=(
            "max. 5000 chars, paragraphs will be preserved. "
            "multiple translations may be provided for short phrases."
        ),
    ),
    from_lang: Optional[str] = None,
    to_lang: Optional[str] = "zh",
):
    r"""
    Get text.

    http://127.0.0.1:{port}/text/?q=abc&to_lang=zh

    Does not seem work, 'playwright\_impl\_sync_base.py... cannot switch to a different thread' TODO
    """
    result = {
        "q": q,
        "from_lang": from_lang,
        "to_lang": to_lang,
        "trtext": "",
        "translation": "",
    }
    try:
        trtext = deepl_tr(
            q,
            from_lang,
            to_lang,
            # page=PAGE,
        )
    except Exception as exc:
        logger.exception(exc)
        trtext = str(exc)

    result.update({"trtext": trtext})
    result.update({"translation": trtext})

    logger.debug("result: %s", result)

    return result


def run_uvicorn():
    """
    Run uvicor.

    Must be run from a different file, e.g., run_uvicorn.py
    """
    uvicorn.run(
        # app="deepl_fastapi.deepl_server:app",
        app=app,  # this should work with python -m deepl_fastapi.deepl_server
        # still "attached to a different loop" error
        host="0.0.0.0",
        # port=8000,
        port=port,
        # debug=True,
        # reload=True,
        # workers=2,
        # loop="asyncio",  # default "auto"
        # loop="uvloop",  # posix (linux and mac) only
    )


def main():
    """Start run_uvicorn."""


if __name__ == "__main__":
    logger.info("pid: %s", os.getpid())

    signal(SIGINT, SIG_DFL)
    print("ctrl-C to interrupt")

    # uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.run("app.app:app",host='0.0.0.0', port=4557, reload=True, debug=True, workers=3)

    # uvicorn deepl_fastapi.deepl_server:app --reload
    # works with nest_asyncio

    run_uvicorn()
