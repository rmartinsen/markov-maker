from app.markov_maker import create_conversation, create_sentence, \
                             MAX_NGRAMS_IN_CHAIN, MIN_NGRAMS_IN_CHAIN

test_corpus = {"test": "a b, c. d e f g h i j k l m n o p q r s t u, v w x y z a b c d e f g"}


def test_create_conversation_len():
    MIN_SENTENCES = 4
    MAX_SENTENCES = 16
    for i in range(1000):
        conversation = create_conversation(test_corpus, min_sentences=MIN_SENTENCES,
                                           max_sentences=MAX_SENTENCES)
        assert MIN_SENTENCES <= len(conversation) <= MAX_SENTENCES

        for sentence in conversation:
            text = sentence["sentence"]
            assert_sentence_is_correct_length(text)


def assert_sentence_is_correct_length(sentence):
    num_words = len(sentence.split(" "))
    assert MIN_NGRAMS_IN_CHAIN * 2 + 1 <= num_words <= MAX_NGRAMS_IN_CHAIN * 2 + 1


def test_create_sentence_has_correct_order():
    for i in range(1000):
        sentence = create_sentence(test_corpus)
        text = sentence["sentence"]
        tokens = text.lower().split(" ")
        for i in range(len(tokens) - 2):
            if tokens[i] == "z":
                assert tokens[i + 1] == "a"
            else:
                assert ord(tokens[i]) == ord(tokens[i + 1]) - 1


def test_create_sentence_no_user():
    sentence = create_sentence(test_corpus)
    assert sentence["name"] == "test"
