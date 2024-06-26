# Дмитрий Маханьков, 15 когорта, Дипломный проект, Инженер по тестированию плюс
import sender_stand_request


def get_track_number():
    track_number = sender_stand_request.post_new_order()
    return track_number.json()["track"]


def test_create_order_get_succes_response():
    track_number = get_track_number()
    response = sender_stand_request.get_get_order_info(track_number)
    assert response.status_code == 200

