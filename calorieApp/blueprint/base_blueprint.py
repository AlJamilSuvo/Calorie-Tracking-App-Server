import flask


def get_response_from_processor(processor):
    response = flask.jsonify(processor.response)
    response.status = processor.status
    response.mimetype = processor.mimetype
    return response
