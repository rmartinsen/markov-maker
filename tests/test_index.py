import json
from unittest.mock import Mock

import pytest

import app.index as index


TEST_SENTENCE = {"name": "Test",
                 "sentence": "Test sentence."}
TEST_CONVERSATION = [{"name": "Test1",
                      "sentence": "Test sentence 1"},
                     {"name": "Test2",
                      "sentence": "Test sentence 2"}]

index.Sentence.get = Mock(return_value=TEST_SENTENCE)
index.Conversation.get = Mock(return_value=TEST_CONVERSATION)


@pytest.fixture
def client():
    test_app = index.app.test_client()
    test_app.testing = True
    return test_app


def test_sentence_api(client):
    response = client.get("/sentence/Test")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    response_data = json.loads(response.data)
    assert response_data == TEST_SENTENCE


def test_conversation_api(client):
    response = client.get("/convo")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    response_data = json.loads(response.data)
    assert response_data == TEST_CONVERSATION
