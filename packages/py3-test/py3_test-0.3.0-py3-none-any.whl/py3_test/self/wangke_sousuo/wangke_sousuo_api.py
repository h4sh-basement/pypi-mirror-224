"""
@author: lijc210@163.com
@file: wangke_sousuo_api.py
@time: 2019/12/01
@desc:
"""

from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
