# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import deviantart
import datetime
from gallery_dl import exception


__tests__ = (
{
    "#url"     : "https://www.deviantart.com/shimoda7",
    "#category": ("", "deviantart", "user"),
    "#class"   : deviantart.DeviantartUserExtractor,
    "#urls"    : "https://www.deviantart.com/shimoda7/gallery",
},

{
    "#url"     : "https://www.deviantart.com/shimoda7",
    "#category": ("", "deviantart", "user"),
    "#class"   : deviantart.DeviantartUserExtractor,
    "#options" : {"include": "all"},
    "#urls"    : (
        "https://www.deviantart.com/shimoda7/avatar",
        "https://www.deviantart.com/shimoda7/banner",
        "https://www.deviantart.com/shimoda7/gallery",
        "https://www.deviantart.com/shimoda7/gallery/scraps",
        "https://www.deviantart.com/shimoda7/posts",
        "https://www.deviantart.com/shimoda7/posts/statuses",
        "https://www.deviantart.com/shimoda7/favourites",
    ),
},

{
    "#url"     : "https://shimoda7.deviantart.com/",
    "#category": ("", "deviantart", "user"),
    "#class"   : deviantart.DeviantartUserExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
    "#pattern" : r"https://(images-)?wixmp-[^.]+\.wixmp\.com/f/.+/.+\.(jpg|png)\?token=.+",
    "#count"   : ">= 38",

    "allows_comments" : bool,
    "author"          : {
        "type"    : "regular",
        "usericon": str,
        "userid"  : "9AE51FC7-0278-806C-3FFF-F4961ABF9E2B",
        "username": "shimoda7",
    },
    "category_path"   : str,
    "content"         : {
        "filesize"    : int,
        "height"      : int,
        "src"         : str,
        "transparency": bool,
        "width"       : int,
    },
    "da_category"     : str,
    "date"            : datetime.datetime,
    "deviationid"     : str,
    "?download_filesize": int,
    "extension"       : str,
    "index"           : int,
    "is_deleted"      : bool,
    "is_downloadable" : bool,
    "is_favourited"   : bool,
    "is_mature"       : bool,
    "preview"         : {
        "height"      : int,
        "src"         : str,
        "transparency": bool,
        "width"       : int,
    },
    "published_time"  : int,
    "stats"           : {
        "comments"  : int,
        "favourites": int,
    },
    "target"          : dict,
    "thumbs"          : list,
    "title"           : str,
    "url"             : r"re:https://www.deviantart.com/shimoda7/art/[^/]+-\d+",
    "username"        : "shimoda7",
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/",
    "#comment" : "range/skip (#4557)",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
    "#options" : {"original": False},
    "#pattern" : r"https://images-wixmp-[0-9a-f]+\.wixmp\.com/f/0e474835-ec35-4937-b647-b6830ed58bd1/d2idul-6158ded2-37ac-413d-802e-0689f0f020ad\.jpg\?token=[\w.]+",
    "#range"   : "38-",
    "#count"   : 1,
},

{
    "#url"     : "https://www.deviantart.com/AlloyRabbit/gallery",
    "#comment" : "deactivated account",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://www.deviantart.com/Shydude/gallery",
    "#comment" : "deactivated account",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://www.deviantart.com/zapor666/gallery",
    "#comment" : "deactivated account",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://www.deviantart.com/yakuzafc/gallery",
    "#comment" : "group",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
    "#pattern" : r"https://www.deviantart.com/yakuzafc/gallery/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}/",
    "#count"   : ">= 15",
},

{
    "#url"      : "https://www.deviantart.com/yakuzafc/gallery",
    "#comment"  : "'group': 'skip' (#4630)",
    "#category" : ("", "deviantart", "gallery"),
    "#class"    : deviantart.DeviantartGalleryExtractor,
    "#options"  : {"group": "skip"},
    "#exception": exception.StopExtraction,
    "#count"    : 0,
},

{
    "#url"     : "https://www.deviantart.com/justatest235723/gallery",
    "#comment" : "'folders' option (#276)",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
    "#options" : {
        "metadata": 1,
        "folders" : 1,
        "original": 0,
    },
    "#count"   : 3,

    "description": str,
    "folders"    : list,
    "is_watching": bool,
    "license"    : str,
    "tags"       : list,
},

{
    "#url"     : "https://www.deviantart.com/shimoda8/gallery/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
    "#exception": exception.NotFoundError,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/all",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/?catpath=/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/gallery/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/gallery/all/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/gallery/?catpath=/",
    "#category": ("", "deviantart", "gallery"),
    "#class"   : deviantart.DeviantartGalleryExtractor,
},

{
    "#url"     : "https://deviantart.com/shimoda7/avatar",
    "#category": ("", "deviantart", "avatar"),
    "#class"   : deviantart.DeviantartAvatarExtractor,
    "#urls"        : "https://a.deviantart.net/avatars-big/s/h/shimoda7.jpg?4",
    "#sha1_content": "abf2cc79b842315f2e54bfdd93bf794a0f612b6f",

    "author"         : {
        "type"    : "regular",
        "usericon": "https://a.deviantart.net/avatars/s/h/shimoda7.jpg?4",
        "userid"  : "9AE51FC7-0278-806C-3FFF-F4961ABF9E2B",
        "username": "shimoda7",
    },
    "content"        : {
        "src": "https://a.deviantart.net/avatars-big/s/h/shimoda7.jpg?4"
    },
    "da_category"    : "avatar",
    "date"           : "dt:1970-01-01 00:00:00",
    "extension"      : "jpg",
    "filename"       : "avatar_by_shimoda7-d4",
    "index"          : 4,
    "index_base36"   : "4",
    "is_deleted"     : False,
    "is_downloadable": False,
    "is_original"    : True,
    "published_time" : 0,
    "target"         : {
        "extension": "jpg",
        "filename" : "avatar_by_shimoda7-d4",
        "src"      : "https://a.deviantart.net/avatars-big/s/h/shimoda7.jpg?4"
    },
    "title"          : "avatar",
    "username"       : "shimoda7",
},

{
    "#url"     : "https://deviantart.com/shimoda7/avatar",
    "#comment" : "'formats' option",
    "#category": ("", "deviantart", "avatar"),
    "#class"   : deviantart.DeviantartAvatarExtractor,
    "#archive" : False,
    "#options" : {"formats": ["original.jpg", "big.jpg", "big.png", "big.gif"]},
    "#urls"    : (
        "https://a.deviantart.net/avatars-original/s/h/shimoda7.jpg?4",
        "https://a.deviantart.net/avatars-big/s/h/shimoda7.jpg?4",
        "https://a.deviantart.net/avatars-big/s/h/shimoda7.png?4",
        "https://a.deviantart.net/avatars-big/s/h/shimoda7.gif?4",
    ),
},

{
    "#url"     : "https://deviantart.com/gdldev/banner",
    "#category": ("", "deviantart", "background"),
    "#class"   : deviantart.DeviantartBackgroundExtractor,
    "#pattern"     : r"https://wixmp-\w+\.wixmp\.com/f/b042e0ae-a7ff-420b-a41a-b35503427360/dgntyqc-3deebb65-04b4-4085-992a-aa0c0e7e225d\.png\?token=ey[\w.-]+$",
    "#sha1_content": "980eaa76ce515f1b6bef60dfadf26a5bbe9c583f",

    "allows_comments"  : True,
    "author"           : {
        "type"    : "regular",
        "usericon": "https://a.deviantart.net/avatars/g/d/gdldev.jpg?2",
        "userid"  : "1A12BA26-33C2-AA0A-7678-0B6DFBA7AC8E",
        "username": "gdldev"
    },
    "category_path"    : "",
    "content"          : {
        "filename"    : "banner_by_gdldev_dgntyqc.png",
        "filesize"    : 84510,
        "height"      : 4000,
        "src"         : r"re:https://wixmp-\w+\.wixmp\.com/f/b042e0ae-a7ff-420b-a41a-b35503427360/dgntyqc-3deebb65-04b4-4085-992a-aa0c0e7e225d\.png\?token=ey[\w.-]+$",
        "transparency": False,
        "width"       : 6400
    },
    "da_category"      : "Uncategorized",
    "date"             : "dt:2024-01-02 21:16:06",
    "deviationid"      : "8C8D6B28-766A-DE21-7F7D-CE055C3BD50A",
    "download_filesize": 84510,
    "extension"        : "png",
    "filename"         : "banner_by_gdldev-dgntyqc",
    "index"            : 1007488020,
    "index_base36"     : "gntyqc",
    "is_blocked"       : False,
    "is_deleted"       : False,
    "is_downloadable"  : True,
    "is_favourited"    : False,
    "is_mature"        : False,
    "is_original"      : True,
    "is_published"     : False,
    "preview"          : dict,
    "printid"          : None,
    "published_time"   : 1704230166,
    "stats"            : {
        "comments"  : 0,
        "favourites": 0,
    },
    "target"           : dict,
    "thumbs"           : list,
    "title"            : "Banner",
    "url"              : "https://sta.sh/0198jippkeys",
    "username"         : "gdldev",
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/722019/Miscellaneous",
    "#comment" : "user",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
    "#options" : {"original": False},
    "#count"   : 5,
},

{
    "#url"     : "https://www.deviantart.com/yakuzafc/gallery/37412168/Crafts",
    "#comment" : "group",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
    "#options" : {"original": False},
    "#count"   : ">= 4",
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/B38E3C6A-2029-6B45-757B-3C8D3422AD1A/misc",
    "#comment" : "uuid",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
    "#options" : {"original": False},
    "#count"   : 5,
},

{
    "#url"     : "https://www.deviantart.com/justatest235723/gallery/69302698/-test-b-c-d-e-f-",
    "#comment" : "name starts with '_', special characters (#1451)",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
    "#options" : {"original": False},
    "#count"   : 1,
},

{
    "#url"     : "https://shimoda7.deviantart.com/gallery/722019/Miscellaneous",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
},

{
    "#url"     : "https://yakuzafc.deviantart.com/gallery/37412168/Crafts",
    "#category": ("", "deviantart", "folder"),
    "#class"   : deviantart.DeviantartFolderExtractor,
},

{
    "#url"     : "https://sta.sh/022c83odnaxc",
    "#category": ("", "deviantart", "stash"),
    "#class"   : deviantart.DeviantartStashExtractor,
    "#pattern"     : r"https://wixmp-[^.]+\.wixmp\.com/f/.+/.+\.png\?token=.+",
    "#count"       : 1,
    "#sha1_content": "057eb2f2861f6c8a96876b13cca1a4b7a408c11f",
},

{
    "#url"     : "https://sta.sh/21jf51j7pzl2",
    "#comment" : "multiple stash items",
    "#category": ("", "deviantart", "stash"),
    "#class"   : deviantart.DeviantartStashExtractor,
    "#options" : {"original": False},
    "#count"   : 4,
},

{
    "#url"     : "https://sta.sh/024t4coz16mi",
    "#comment" : "downloadable, but no 'content' field (#307)",
    "#category": ("", "deviantart", "stash"),
    "#class"   : deviantart.DeviantartStashExtractor,
    "#pattern" : r"https://wixmp-[^.]+\.wixmp\.com/f/.+/.+\.rar\?token=.+",
    "#count"   : 1,
},

{
    "#url"     : "https://sta.sh/215twi387vfj",
    "#comment" : "mixed folders and images (#659)",
    "#category": ("", "deviantart", "stash"),
    "#class"   : deviantart.DeviantartStashExtractor,
    "#options" : {"original": False},
    "#count"   : 4,
},

{
    "#url"     : "https://sta.sh/abcdefghijkl",
    "#category": ("", "deviantart", "stash"),
    "#class"   : deviantart.DeviantartStashExtractor,
    "#count"   : 0,
},

{
    "#url"     : "https://www.deviantart.com/h3813067/favourites/",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
    "#options" : {
        "metadata": True,
        "flat"    : False,
    },
    "#count"   : 1,
},

{
    "#url"     : "https://www.deviantart.com/h3813067/favourites/",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
    "#sha1_content": "6a7c74dc823ebbd457bdd9b3c2838a6ee728091e",
},

{
    "#url"     : "https://www.deviantart.com/h3813067/favourites/all",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
},

{
    "#url"     : "https://www.deviantart.com/h3813067/favourites/?catpath=/",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
},

{
    "#url"     : "https://h3813067.deviantart.com/favourites/",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
},

{
    "#url"     : "https://h3813067.deviantart.com/favourites/all",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
},

{
    "#url"     : "https://h3813067.deviantart.com/favourites/?catpath=/",
    "#category": ("", "deviantart", "favorite"),
    "#class"   : deviantart.DeviantartFavoriteExtractor,
},

{
    "#url"     : "https://www.deviantart.com/pencilshadings/favourites/70595441/3D-Favorites",
    "#category": ("", "deviantart", "collection"),
    "#class"   : deviantart.DeviantartCollectionExtractor,
    "#options" : {"original": False},
    "#count"   : ">= 15",
},

{
    "#url"     : "https://www.deviantart.com/pencilshadings/favourites/F050486B-CB62-3C66-87FB-1105A7F6379F/3D Favorites",
    "#category": ("", "deviantart", "collection"),
    "#class"   : deviantart.DeviantartCollectionExtractor,
    "#options" : {"original": False},
    "#count"   : ">= 15",
},

{
    "#url"     : "https://pencilshadings.deviantart.com/favourites/70595441/3D-Favorites",
    "#category": ("", "deviantart", "collection"),
    "#class"   : deviantart.DeviantartCollectionExtractor,
},

{
    "#url"     : "https://www.deviantart.com/angrywhitewanker/posts/journals/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
    "#sha1_url": "38db2a0d3a587a7e0f9dba7ff7d274610ebefe44",
},

{
    "#url"     : "https://www.deviantart.com/angrywhitewanker/posts/journals/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
    "#options" : {"journals": "text"},
    "#sha1_url": "b2a8e74d275664b1a4acee0fca0a6fd33298571e",
},

{
    "#url"     : "https://www.deviantart.com/angrywhitewanker/posts/journals/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
    "#options" : {"journals": "none"},
    "#count"   : 0,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/posts/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/journal/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/journal/?catpath=/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/journal/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/journal/?catpath=/",
    "#category": ("", "deviantart", "journal"),
    "#class"   : deviantart.DeviantartJournalExtractor,
},

{
    "#url"     : "https://www.deviantart.com/t1na/posts/statuses",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#count"   : 0,
},

{
    "#url"     : "https://www.deviantart.com/justgalym/posts/statuses",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#count"   : 4,
    "#sha1_url": "bf4c44c0c60ff2648a880f4c3723464ad3e7d074",
},

{
    "#url"     : "https://www.deviantart.com/justgalym/posts/statuses",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#options" : {"journals": "none"},
    "#pattern" : r"https://images-wixmp-\w+\.wixmp\.com/f/[^/]+/[^.]+\.jpg\?token=",
    "#count"   : 1,
},

{
    "#url"     : "https://www.deviantart.com/vanillaghosties/posts/statuses",
    "#comment" : "shared sta.sh item",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#options" : {
        "journals": "none",
        "original": False,
    },
    "#range"   : "5-",
    "#count"   : 1,

    "index"       : int,
    "index_base36": r"re:^[0-9a-z]+$",
    "url"         : r"re:^https://sta.sh",
},

{
    "#url"     : "https://www.deviantart.com/AndrejSKalin/posts/statuses",
    "#comment" : "'deleted' deviations in 'items'",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#options" : {
        "journals"    : "none",
        "original"    : 0,
        "image-filter": "deviationid[:8] == '147C8B03'",
    },
    "#count"   : 2,
    "#archive" : False,

    "deviationid": "147C8B03-7D34-AE93-9241-FA3C6DBBC655",
},

{
    "#url"     : "https://www.deviantart.com/justgalym/posts/statuses",
    "#category": ("", "deviantart", "status"),
    "#class"   : deviantart.DeviantartStatusExtractor,
    "#options" : {"journals": "text"},
    "#sha1_url": "c8744f7f733a3029116607b826321233c5ca452d",
},

{
    "#url"     : "https://www.deviantart.com/?order=popular-all-time",
    "#category": ("", "deviantart", "popular"),
    "#class"   : deviantart.DeviantartPopularExtractor,
    "#options" : {"original": False},
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://www.deviantart.com/popular-24-hours/?q=tree+house",
    "#category": ("", "deviantart", "popular"),
    "#class"   : deviantart.DeviantartPopularExtractor,
    "#options" : {"original": False},
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://www.deviantart.com/artisan/popular-all-time/?q=tree",
    "#category": ("", "deviantart", "popular"),
    "#class"   : deviantart.DeviantartPopularExtractor,
},

{
    "#url"     : "https://www.deviantart.com/tag/nature",
    "#category": ("", "deviantart", "tag"),
    "#class"   : deviantart.DeviantartTagExtractor,
    "#options" : {"original": False},
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://www.deviantart.com/watch/deviations",
    "#category": ("", "deviantart", "watch"),
    "#class"   : deviantart.DeviantartWatchExtractor,
},

{
    "#url"     : "https://www.deviantart.com/notifications/watch",
    "#category": ("", "deviantart", "watch"),
    "#class"   : deviantart.DeviantartWatchExtractor,
},

{
    "#url"     : "https://www.deviantart.com/watch/posts",
    "#category": ("", "deviantart", "watch-posts"),
    "#class"   : deviantart.DeviantartWatchPostsExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/art/For-the-sake-10073852",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#options"     : {"original": 0},
    "#sha1_content": "6a7c74dc823ebbd457bdd9b3c2838a6ee728091e",
},

{
    "#url"     : "https://www.deviantart.com/zzz/art/zzz-1234567890",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#exception": exception.NotFoundError,
},

{
    "#url"     : "https://www.deviantart.com/myria-moon/art/Aime-Moi-261986576",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#options" : {"comments": True},
    "#pattern" : r"https://wixmp-[^.]+\.wixmp\.com/f/.+/.+\.jpg\?token=.+",

    "comments": "len:44",
},

{
    "#url"     : "https://www.deviantart.com/justatest235723/art/Blue-811519058",
    "#comment" : "nested comments (#4653)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#options" : {
        "original": False,
        "comments": True,
    },

    "comments": "len:20",
},

{
    "#url"     : "https://www.deviantart.com/citizenfresh/art/Hverarond-789295466",
    "#comment" : "wixmp URL rewrite /intermediary/",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#urls"    : "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/4deb0f1a-cdef-444e-b194-c8d6b3f7e933/dd1xca2-7f835e62-6fd3-4b99-92c7-2bfd4e1b296f.jpg",

    "is_downloadable": False,
    "is_original"    : False,
},

{
    "#url"     : "https://www.deviantart.com/skatergators/art/COM-Moni-781571783",
    "#comment" : "GIF (#242)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#pattern" : r"https://wixmp-\w+\.wixmp\.com/f/03fd2413-efe9-4e5c-8734-2b72605b3fbb/dcxbsnb-1bbf0b38-42af-4070-8878-f30961955bec\.gif\?token=ey...",
},

{
    "#url"     : "https://www.deviantart.com/yuumei/art/Flash-Comic-214724929",
    "#comment" : "Flash animation with GIF preview (#1731)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#pattern" : r"https://wixmp-[^.]+\.wixmp\.com/f/.+/.+\.swf\?token=.+",

    "filename" : "flash_comic_tutorial_by_yuumei-d3juatd",
    "extension": "swf",
},

{
    "#url"     : "https://www.deviantart.com/uotapo/art/INANAKI-Memo-590297498",
    "#comment" : "sta.sh URLs from description (#302)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#options" : {
        "extra"   : 1,
        "original": 0,
    },
    "#pattern" : deviantart.DeviantartStashExtractor.pattern,
    "#range"   : "2-",
    "#count"   : 4,
},

{
    "#url"     : "https://www.deviantart.com/cimar-wildehopps/art/Honorary-Vixen-859809305",
    "#comment" : "sta.sh URL from deviation['text_content']['body']['features']",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#options" : {"extra": 1},
    "#pattern" : r"""text:<!DOCTYPE html>
|(?:https?://)?sta\.sh/([a-z0-9]+)""",
    "#count"   : 2,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/journal/ARTility-583755752",
    "#comment" : "journal",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#pattern" : """text:<!DOCTYPE html>
""",
    "#sha1_url": "d34b2c9f873423e665a1b8ced20fcb75951694a3",
},

{
    "#url"     : "https://www.deviantart.com/gliitchlord/art/brashstrokes-812942668",
    "#comment" : "journal-like post with isJournal == False (#419)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#pattern" : """text:<!DOCTYPE html>
""",
    "#sha1_url": "e2e0044bd255304412179b6118536dbd9bb3bb0e",
},

{
    "#url"     : "https://deviantart.com/view/904858796/",
    "#comment" : "/view/ URLs",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#sha1_content": "8770ec40ad1c1d60f6b602b16301d124f612948f",
},

{
    "#url"     : "http://www.deviantart.com/view/890672057",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#sha1_content": "1497e13d925caeb13a250cd666b779a640209236",
},

{
    "#url"     : "https://www.deviantart.com/view/706871727",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#sha1_content": "3f62ae0c2fca2294ac28e41888ea06bb37c22c65",
},

{
    "#url"     : "https://www.deviantart.com/view/1",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#exception": exception.NotFoundError,
},

{
    "#url"     : "https://www.deviantart.com/deviation/817215762",
    "#comment" : "/deviation/ (#3558)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://fav.me/ddijrpu",
    "#comment" : "fav.me (#3558)",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#count"   : 1,
},

{
    "#url"     : "https://fav.me/dddd",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
    "#exception": exception.NotFoundError,
},

{
    "#url"     : "https://shimoda7.deviantart.com/art/For-the-sake-of-a-memory-10073852",
    "#comment" : "old-style URLs",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://myria-moon.deviantart.com/art/Aime-Moi-part-en-vadrouille-261986576",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://zzz.deviantart.com/art/zzz-1234567890",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://www.deviantart.com/view.php?id=14864502",
    "#comment" : "old /view/ URLs from the Wayback Machine",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "http://www.deviantart.com/view-full.php?id=100842",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://www.fxdeviantart.com/zzz/art/zzz-1234567890",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://www.fxdeviantart.com/view/1234567890",
    "#category": ("", "deviantart", "deviation"),
    "#class"   : deviantart.DeviantartDeviationExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/scraps",
    "#category": ("", "deviantart", "scraps"),
    "#class"   : deviantart.DeviantartScrapsExtractor,
    "#count"   : 12,
},

{
    "#url"     : "https://www.deviantart.com/chain-man/gallery/scraps",
    "#comment" : "deactivated account",
    "#category": ("", "deviantart", "scraps"),
    "#class"   : deviantart.DeviantartScrapsExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery/?catpath=scraps",
    "#category": ("", "deviantart", "scraps"),
    "#class"   : deviantart.DeviantartScrapsExtractor,
},

{
    "#url"     : "https://shimoda7.deviantart.com/gallery/?catpath=scraps",
    "#category": ("", "deviantart", "scraps"),
    "#class"   : deviantart.DeviantartScrapsExtractor,
},

{
    "#url"     : "https://www.deviantart.com/search?q=tree",
    "#category": ("", "deviantart", "search"),
    "#class"   : deviantart.DeviantartSearchExtractor,
},

{
    "#url"     : "https://www.deviantart.com/search/deviations?order=popular-1-week",
    "#category": ("", "deviantart", "search"),
    "#class"   : deviantart.DeviantartSearchExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery?q=memory",
    "#category": ("", "deviantart", "gallery-search"),
    "#class"   : deviantart.DeviantartGallerySearchExtractor,
    "#options"     : {"original": 0},
    "#sha1_content": "6a7c74dc823ebbd457bdd9b3c2838a6ee728091e",
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/gallery?q=memory&sort=popular",
    "#category": ("", "deviantart", "gallery-search"),
    "#class"   : deviantart.DeviantartGallerySearchExtractor,
},

{
    "#url"     : "https://www.deviantart.com/shimoda7/about#watching",
    "#category": ("", "deviantart", "following"),
    "#class"   : deviantart.DeviantartFollowingExtractor,
    "#pattern" : deviantart.DeviantartUserExtractor.pattern,
    "#range"   : "1-50",
    "#count"   : 50,
},

)
