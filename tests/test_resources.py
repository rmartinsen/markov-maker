from unittest.mock import Mock

import app.resources as resources


TEST_SENTENCE = {"name": "Test",
                 "sentence": "Test sentence."}
TEST_CONVERSATION = [{"name": "Test1",
                      "sentence": "Test sentence 1"},
                     {"name": "Test2",
                      "sentence": "Test sentence 2"}]

TEST_PERSON_LIST = ["test 1", "test 2"]

resources.create_sentence = Mock(return_value=TEST_SENTENCE)
resources.create_conversation = Mock(return_value=TEST_CONVERSATION)
resources.create_person_list = Mock(return_value=TEST_PERSON_LIST)


def test_get_sentence_resource():
    sentence = resources.Sentence().get()
    assert sentence == TEST_SENTENCE


def test_get_conversation_resource():
    conversation = resources.Conversation().get()
    assert conversation == TEST_CONVERSATION


def test_get_person_list_resource():
    person_list = resources.PersonList().get()
    assert person_list == TEST_PERSON_LIST
