import uuid

def Hash(uuids, link):
    gid = uuid.uuid4().hex
    print(gid)
    uuids[gid] = link
    print(uuids)
    return uuids
