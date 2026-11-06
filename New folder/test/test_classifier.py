from service.classifier.rule_classifier import RuleClassifier
from service.classifier.keyword_classifier import KeywordClassifier
def test_password_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("I forgot my password")

    assert result == "account"


def test_fee_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("I have a fee problem")

    assert result == "finance"


def test_technical_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("The server is down")

    assert result == "technical"


def test_unknown_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"