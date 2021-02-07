

from _projeto.elementos.adjectives import adjectives_no_article
from _projeto.elementos.adjectives2 import adjectives_with_article
from _projeto.elementos.infinitive_verbs import verbs_infinitive
from _projeto.elementos.nouns import nouns_no_article
from _projeto.elementos.nouns2 import nouns_with_article
from _projeto.elementos.nouns3 import nouns_full
from _projeto.elementos.object_pronouns import pronouns_object
from _projeto.elementos.personal_pronouns import pronouns_personal
from _projeto.elementos.possessive_adjectives import adjectives_possessive
from _projeto.elementos.possessive_pronouns import pronouns_possessive
from _projeto.elementos.time_tense_present import present_time_tense
from _projeto.elementos.time_tense_past import past_time_tense
from _projeto.elementos.to_be import to_be_present, to_be_past
from random import choice

print(
    f"""
    {choice(pronouns_personal)} {choice(to_be_present)} {choice(nouns_with_article)}
    {choice(pronouns_personal)} {choice(to_be_present)} {choice(adjectives_no_article)}
    {choice(pronouns_personal)} {choice(present_time_tense)} {choice(nouns_with_article)}
    {choice(pronouns_personal)} {choice(present_time_tense)} {choice(adjectives_no_article)}
    {choice(pronouns_personal)} {choice(present_time_tense)} {choice(verbs_infinitive)} {choice(nouns_with_article)}
    {choice(nouns_with_article)} {choice(present_time_tense)} {choice(adjectives_with_article)}
    {choice(nouns_with_article)} {choice(present_time_tense)} {choice(adjectives_no_article)}
    {choice(adjectives_possessive)} {choice(nouns_no_article)} {choice(present_time_tense)} {choice(adjectives_no_article)}
    {choice(adjectives_possessive)} {choice(nouns_no_article)} {choice(to_be_present)} {choice(adjectives_no_article)}
    {choice(adjectives_possessive)} {choice(nouns_no_article)} {choice(to_be_present)} {choice(adjectives_no_article)}
    """
)
