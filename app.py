from flask import Flask, request, jsonify
from transformers import pipeline


app = Flask(__name__)


qa_model = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")


@app.route('/qa', methods=['POST'])
def question_answer():

    data = request.json

    question = data['question']
    context = "Technology Food Court is adjacent to the Clock Tower. Prafulla Da Canteen is situated nearby RCGSIDM. The Department of Ocean Engineering and Naval Architecture is located beside the Central Research Facility. Kalpana Chawla Space Technology Cell is next to the Department Of Metallurgical and Materials Engineering. Nescafe is the canteen that is close to VGSOM. Cryogenic Engineering Centre is situated nearby the Department Of Industrial and Systems Engineering. A T Rao Canteen is the closest canteen to Kalidas Auditorium. Netaji Auditorium is nearby the Technology Film Society Office. Kshititj Arena is adjacent to Vikramshila. Subway is the food court located near Nalanda Complex. Centre of Excellence in Artificial Intelligence is adjacent to the Nalanda Complex. The Department of Chemical Engineering is nearby the ERP Department. Department of Chemistry is beside RCGSIDM. Hijli Shaheed Bhavan is situated close to the Nehru Museum of Science and Technology. Centre of Excellence for Indian Knowledge System is adjacent to the Nehru Museum of Science and Technology. Department of Industrial and Systems Engineering is near VGSOM. School of Medical Science And Technology is nearby the Department of Architecture and Regional Planning. Raman Auditorium is close to the Department of Humanities and Social Sciences. Department of Physics is behind the Main Building. Department of Chemistry is close to B-club. NAVIC Mining Department is situated beside AGV Lab. The ECE Tea stall is at the backside of the Department of Mining Engineering. Central Library is adjacent to the Department Of Electronics And Electrical Communication Engineering. The building close to the Main Building is Central Library. Bhatnagar Auditorium is adjacent to the Department of Mathematics."

    
    answer = qa_model(question=question, context=context)["answer"]

    print("Location", answer)
  
    return jsonify({'answer': answer})


@app.route('/test', methods=['GET'])
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=5001)