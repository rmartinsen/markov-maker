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
TEST_PERSON_LIST = ["test 1", "test 2"]


index.Sentence.get = Mock(return_value=TEST_SENTENCE)
index.Conversation.get = Mock(return_value=TEST_CONVERSATION)
index.PersonList.get = Mock(return_value=TEST_PERSON_LIST)


@pytest.fixture
def client():
    test_app = index.app.test_client()
    test_app.testing = True
    return test_app


def assert_api_returns_correct_json(client, url, correct_json):
    response = client.get(url)
    assert response.status_code == 200
    assert response.content_type == "application/json"
    response_data = json.loads(response.data)
    assert response_data == correct_json


def test_sentence_api(client):
    assert_api_returns_correct_json(client, "/sentence/Test", TEST_SENTENCE)


def test_conversation_api(client):
    assert_api_returns_correct_json(client, "/convo", TEST_CONVERSATION)


def test_person_list_api(client):
    assert_api_returns_correct_json(client, "/people", TEST_PERSON_LIST)
