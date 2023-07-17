from typing import Union
from fastapi import FastAPI
from pipeline.sentence_segmentation.sent_segment import sent_seg , convert_teencode
from pipeline.text_normalize import normalize,process_unikey,_normalize_each_token
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pipeline.text_normalize.process_text_to_number import covert_text_to_number,special_cases,number_dict
from pipeline.text_normalize.process_acronym_teencode import process_acronym
from pipeline.text_normalize.process_measure import  covert_measure
from pipeline.text_normalize.process_number import normalize_number,_split_2_units
from pipeline.text_normalize.normalize_api import process_tone_mark_api
from pipeline.text_normalize.process_unikey import process_unikey



app = FastAPI()



origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Body(BaseModel):
    string : str



@app.post("/api/sent_seg")
def sent_seg_controller(body: Body | None = None):



    if(len(body.string) > 500 or body is None):
        return {
            "statusCode": 400,
            "messenger": "Invalid input"
        }

    text = convert_teencode(body.string)
    res = sent_seg(text)

    return {
        "statusCode": 200,
        "result" : res
    }
@app.post("/api/text_normalize")
def text_normalize_controller(body:Body | None =None):

    if(len(body.string) > 500 or body is None):
        return {
            "statusCode": 400,
            "messenger": "Invalid input"
        }

    text = normalize(body.string.split())

    return {
        "statusCode": 200,
        "result" : " ".join(text),
    }

@app.post("/api/acronym_teencode")
def acronym_teencode_controller(body:Body | None = None):
    if(len(body.string)>500 or body is None):
        return {
            "statusCode":400,
            "message":"Invalid Input"
        }
    tokens = body.string.split()
    process_token = [process_acronym(token) for token in tokens]
    result = " ".join(process_token)
    return {
        "statusCode":200,
        "result": result,
    }

@app.post("/api/process_measure")
def process_measure_controller(body:Body |None = None):
    if (len(body.string) > 500 or body is None):
        return {
            "statusCode":400,
            "message":"Invalid Input"
        }

    result = covert_measure(body.string)
    return {
        "statusCode":200,
        "result":result,
    }
@app.post("/api/process_number")
def process_number_controller(body:Body | None = None):


    if (len(body.string)>500 or body is None):
        return {
            "statusCode":400,
            "message":"Invalid Input"
        }
    text = normalize(body.string.split())
    return {
        "statusCode":200,
        "result": " ".join(text)
    }
@app.post("/api/process_tone_mark")
def process_tone_mark_controller(body:Body | None = None):
    if(len(body.string)>500 or body is None):
        return {
            "statusCode":400,
            "message":"Invalid Input"
        }

    result = process_tone_mark_api(body.string)
    return {
        "statusCode":200,
        "result": result
    }

if __name__ == "__main__":
    print(process_unikey(
        """
            With the support from the school, the eSTI Institute, the summer internship program has gone through more than 1 month with many exciting activities in the process of developing and implementing group projects and participating in seminars to be provided with knowledge. knowledge, foundation skills, experience sharing in many fields
            Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.
        """
    ))


    # print(is_vn("more", "through", "than"))