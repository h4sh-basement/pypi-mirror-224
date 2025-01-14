import argparse, asyncio, queue, sqlite3, threading
from pathlib import Path

from xklb import db, usage, utils
from xklb.utils import log

"""
My understanding of aiohttp is stolen
from ashish01's excellent https://github.com/ashish01/hn-data-dumps/blob/main/hn_async2.py

MIT License

Copyright (c) 2020 ashish01, Jacob Chapman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def parse_args(prog, usage) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog, usage)
    parser.add_argument("--oldest", action="store_true")

    parser.add_argument("--verbose", "-v", action="count", default=0)
    parser.add_argument("--db", "-db", help=argparse.SUPPRESS)

    parser.add_argument("database")
    args = parser.parse_args()

    if args.db:
        args.database = args.db
    Path(args.database).touch()
    args.db = db.connect(args)
    log.info(utils.dict_filter_bool(args.__dict__))

    return args


def get(url):
    import requests

    r = requests.get(url, timeout=120)
    return r.json()


def db_worker(args, input_queue):
    conn = sqlite3.connect(args.database, isolation_level=None)
    db_conn = db.connect(args, conn)
    while True:
        r = input_queue.get()
        if r is None:
            break

        hn_type, data = r
        log.info("Saving %s %s", hn_type, data["id"])
        db_conn["hn_" + hn_type].insert(data, pk="id", alter=True)  # type: ignore


async def get_hn_item(session, db_queue, sem, hn_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{hn_id}.json"
    try:
        async with session.get(url) as response:
            data = await response.json()
            hn_type = data.pop("type")
            data["path"] = data.pop("url", None)
            data["author"] = data.pop("by", None)
            data["is_dead"] = data.pop("dead", None)
            data["is_deleted"] = data.pop("deleted", None)
            data["time_created"] = data.pop("time", None)
            data = utils.dict_filter_bool(data)
            log.debug("Saving %s", data)
            db_queue.put((hn_type, data))
    finally:
        sem.release()


async def run(args, db_queue):
    import aiohttp

    N = 80
    sem = asyncio.Semaphore(N)

    async with aiohttp.ClientSession() as session:
        hn_ids = range(args.oldest_id + 1, args.latest_id)
        if not args.oldest:
            hn_ids = reversed(hn_ids)

        background_tasks = set()
        for hn_id in hn_ids:
            log.debug("Getting item %s", hn_id)
            await sem.acquire()
            task = asyncio.create_task(get_hn_item(session, db_queue, sem, hn_id))
            background_tasks.add(task)
            task.add_done_callback(background_tasks.discard)

        for _i in range(N):
            await sem.acquire()


def hacker_news_add() -> None:
    args = parse_args(prog="library hnadd", usage=usage.hnadd)
    try:
        import aiohttp
    except ModuleNotFoundError:
        log.error("aiohttp is required for hn_extract. Install with pip install aiohttp or pip install xklb[deluxe]")
        raise

    args.db.enable_wal()

    max_item_id = get("https://hacker-news.firebaseio.com/v0/maxitem.json")
    tables = args.db.table_names()
    r = list(
        args.db.query(
            f"""
        WITH t AS (
            SELECT id AS latest_id,
                LAG (id, 1) OVER (ORDER BY id) AS oldest_id,
                id - (LAG (id, 1) OVER (ORDER BY id)) AS diff
            FROM (
                {'SELECT id FROM hn_story' if 'hn_story' in tables else 'SELECT 1 as id'}
                {'UNION ALL SELECT id FROM hn_comment' if 'hn_comment' in tables else ''}
                {'UNION ALL SELECT id FROM hn_job' if 'hn_job' in tables else ''}
                {'UNION ALL SELECT id FROM hn_poll' if 'hn_poll' in tables else ''}
                {'UNION ALL SELECT id FROM hn_pollopt' if 'hn_pollopt' in tables else ''}
                {'UNION ALL SELECT ' + str(max_item_id)}
            )
            --WHERE id > 33212696
        )
        SELECT * FROM t
        WHERE diff > 1
        ORDER BY diff DESC
        """,
        ),
    )
    if len(r) == 0:
        raise SystemExit(128)

    for gap in r:
        args.latest_id = gap["latest_id"]
        args.oldest_id = gap["oldest_id"]

        log.info("Fetching %s items (%s to %s)", args.latest_id - args.oldest_id, args.oldest_id, args.latest_id)

        db_queue = queue.Queue()
        db_thread = threading.Thread(target=db_worker, args=(args, db_queue))
        db_thread.start()

        asyncio.get_event_loop().run_until_complete(run(args, db_queue))
        db_queue.put(None)
        db_thread.join()

        log.info("Imported %s rows", gap["diff"])


if __name__ == "__main__":
    hacker_news_add()
