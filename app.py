from flask import Flask, request, Response
# from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
# import numpy as np
import json

from util.sentence_embedding import get_embedding
from util.rank import enroll, rank

app = Flask(__name__)

def parse_enroll(payload): 
    # { question_id : 0, symptom: "", body_part: "" }
    question_id = payload['question_id']
    symptom = payload['symptom']
    body_part = payload['body_part']

    return question_id, symptom, body_part

def parse_rank(payload): 
    # { symptom: "" }
    return payload['symptom']

# 증상 등록
@app.route('/symptom', methods=['POST'])
def enroll_symptom():

    # 요청 바디 : 질문 아이디, 증상, 부위
    question_id, symptom, body_part = parse_enroll(request.json)

    # 증상 벡터화
    symptom_vector = get_embedding(symptom)

    # 지식 그래프에 질문id, 벡터, 부위 등록
    enroll(question_id, symptom_vector, body_part)

    # 응답 형식 적용
    result = { "result" : "success" }
    json_data = json.dumps(result)
    response = Response(json_data, content_type='application/json')

    return response

# 유사한 증상 조회
@app.route('/symptom/rank', methods=['POST'])
def rank_symptom():

    # 요청 바디 : 특정 환자 증상
    symptom = parse_rank(request.json)

    # 증상 벡터화
    symptom_vector = get_embedding(symptom)

    # 지식 그래프에서 유사 증상 관련 질문 id 리스트로 조회
    sorted_question_id_list = rank(symptom_vector)

    # 응답 형식 적용
    result = { "sorted_question_id_list" : sorted_question_id_list }
    json_data = json.dumps(result)
    response = Response(json_data, content_type='application/json')

    return response

@app.route('/symptom', methods=['PATCH'])
def update_symptom():
    return "PATCH"

@app.route('/symptom', methods=['DELETE'])
def delete_symptom():
    return "DELETE"


if __name__ == '__main__':
    app.run(port=5000, debug=True) 