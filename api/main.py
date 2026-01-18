import json
import random
from datetime import datetime

# =================================================
# DANH SÁCH VIDEO
# =================================================
VIDEOS = [
    "https://files.catbox.moe/iwil8r.mp4",
    "https://files.catbox.moe/dm9504.mp4",
    "https://files.catbox.moe/qpxze5.mp4",
    "https://files.catbox.moe/wgbraa.mp4",
    "https://files.catbox.moe/3fjl5v.mp4",
    "https://files.catbox.moe/35uepq.mp4",
    "https://files.catbox.moe/85ba1y.mp4",
    "https://files.catbox.moe/fmlxfm.mp4",
    "https://files.catbox.moe/rvgqy5.mp4",
    "https://files.catbox.moe/9s133m.mp4",
    "https://files.catbox.moe/h02nig.mp4",
    "https://files.catbox.moe/5juq4f.mp4",
    "https://files.catbox.moe/4pwqeb.mp4",
    "https://files.catbox.moe/yj09em.mp4",
    "https://files.catbox.moe/xt3g7f.mp4",
    "https://files.catbox.moe/odf2ow.mp4",
    "https://files.catbox.moe/nc6xf4.mp4",
    "https://files.catbox.moe/pczll7.mp4",
    "https://files.catbox.moe/kjgds0.mp4",
    "https://files.catbox.moe/ephgwv.mp4",
    "https://files.catbox.moe/fndh30.mp4"
]

# =================================================
# HANDLER
# =================================================
def handler(request, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json; charset=utf-8"
    }

    # Random 1 video
    selected_video = random.choice(VIDEOS)

    # JSON response
    response_body = {
        "status": True,
        "data": selected_video,
        "count": len(VIDEOS),
        "update_time": datetime.now().strftime("%d/%m/%Y")
    }

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(response_body, ensure_ascii=False)
    }
