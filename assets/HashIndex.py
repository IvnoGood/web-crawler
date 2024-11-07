import uuid


def HashIndex(uuids, link):
    gid = uuid.uuid4().hex
    print(gid)
    uuids[gid] = link
    print(uuids)
    return uuids
