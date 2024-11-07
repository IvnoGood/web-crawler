import uuid
uuids = {}
link = 'https://www.CornHub.website'


def Hash(uuids, link):
    gid = uuid.uuid4().hex
    print(gid)
    uuids[gid] = link
    print(uuids)


Hash(uuids, link)
