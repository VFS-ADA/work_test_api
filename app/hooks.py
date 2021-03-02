def pre_get_all(resource, request, lookup):
    if "_id" in lookup:
        print("PRE GET ITEM ALL", resource, request, lookup)
    else:
        print("PRE GET ALL", resource, request, lookup)


def pre_post_all(resource, request):
    print("PRE POST ALL", resource, request)


def pre_put_all(resource, request, lookup):
    print("PRE PUT ALL", resource, request, lookup)


def pre_patch_all(resource, request, lookup):
    print("PRE PATCH ALL", resource, request, lookup)


def pre_delete_all(resource, request, lookup):
    print("PRE DELETE ALL", resource, request, lookup)
