from cardmarket_api.utils.oauth_utils import generate_nonce, generate_timestamp


def test_generate_nonce():
    nonce_1 = generate_nonce()
    nonce_2 = generate_nonce()
    assert len(nonce_1) == 8
    assert nonce_1 != nonce_2

def test_generate_timestamp():
    time_stamp_1 = int(generate_timestamp())
    time_stamp_2 = int(generate_timestamp())
    assert time_stamp_2 >= time_stamp_1