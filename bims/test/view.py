# coding:utf-8


from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Datum:
    data_source_name: Optional[str] = None
    data_source_type: Optional[str] = None


@dataclass
class ResponseModal:
    code: int
    data: List[Datum]
    msg: str




from flask import request, render_template, Response, globals
import json
from app.main.common.alchemyEncoder import AlchemyEncoder
import datetime
from app.main.utils import utils


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@test.route('/list', methods=["GET", "POST"])
def dataList():
    if request.method == 'POST':
        page = request.form['page']
        result = {
            "data":[
	{
		"dataSourceName":"ClickHouse",
		"dataSourceType":"click_house"
	}
            ],
            "code": 0,
            "msg": "success"
        }
        return json.dumps(result, cls=AlchemyEncoder, ensure_ascii=False)
    return render_template('test/testpage.html')