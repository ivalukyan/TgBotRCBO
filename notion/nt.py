"""
Notion
"""

import requests

from env import NOTION_TOKEN, NOTION_DATABASE_ID, NOTION_URL
from datetime import datetime, timezone

# Authorization
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
    "Authorization": NOTION_TOKEN

}


async def create_page(data: dict):
    """
    Create database
    """
    create_url = f"{NOTION_URL}/pages"
    payload = {"parent": {"database_id": NOTION_DATABASE_ID}, "properties": data}
    result = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)

    await result


async def get_pages(num_pages=None):
    """
    Get info database
    """
    get_url = f"{NOTION_URL}/databases/{NOTION_DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(get_url, json=payload, headers=headers)

    get_data = response.json()

    results = get_data["results"]
    while get_data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": get_data["next_cursor"]}
        _url = f"{NOTION_URL}/databases/{NOTION_DATABASE_ID}/query"
        response = requests.post(_url, json=payload, headers=headers)
        _data = response.json()
        results.extend(_data["results"])

    await results


async def update_page(page_id: str, data: dict):
    """
    Update database
    """
    url = f"{NOTION_URL}/pages/{page_id}"
    payload = {"properties": data}
    result = requests.patch(url, json=payload, headers=headers)

    await result


async def delete_page(page_id: str):
    """
    Delete database
    """
    url = f"{NOTION_URL}/pages/{page_id}"

    payload = {"archived": True}

    result = requests.patch(url, json=payload, headers=headers)
    await result

# ============Обработка данных===================

# for page in pages:
#     page_id = page["id"]
#     props = page["properties"]
#     sub = props["Subjects"]["title"][0]["text"]["content"]
#     task = props["Tasks"]["rich_text"][0]["text"]["content"]
#     publish = props["Published"]["date"]["start"]
#     published = datetime.fromisoformat(publish).date().strftime("%d-%m-%Y")

#     date = f"Subject  - {sub}\nTask - {task}\nTime - {published}"
#     print(f"ID = {page_id}")
#     print(date)


# ------------CRUD-------------

# task = "Nuber 3"
# subject = "Physics"
# published_date = datetime.now().astimezone(timezone.utc).isoformat()
# data = {
#     "Subjects": {"title": [{"text": {"content": subject}}]},
#     "Tasks": {"rich_text": [{"text": {"content": task}}]},
#     "Published": {"date": {"start": published_date, "end": None}}
# }

# page_id = "fcdd6b6d-6197-4237-a72d-bd1889e80ce5"

# create_page(data)

# pages = get_pages()

# new_date = datetime(2023, 1, 15).astimezone(timezone.utc).isoformat()
# update_data = {"Published": {"date": {"start": new_date, "end": None}}}
# update_page(page_id, update_data)

# delete_page(page_id)
