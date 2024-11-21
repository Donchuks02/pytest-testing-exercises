from cards import Card
import pytest



def start(self, card_id: int):
  """Set a card state to 'in prog'."""
  self.update_card(card_id, Card(state="in prog"))



# Let’s build some parametrized tests for the above API method:


# 1. Write out three test functions that make sure any start state results in “in prog” when start() is called:
# • test_start_from_done()
# • test_start_from_in_prog()
# • test_start_from_todo()



def test_start_from_done(cards_db):
  index = cards_db.add_card(Card("Post on twitter", state="done"))
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"


def test_start_from_in_prog(cards_db):
  index = cards_db.add_card(Card("Write to my dad", state="in prog"))
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"

def test_start_from_todo(cards_db):
  index = cards_db.add_card(Card("Clean my room", state="todo"))
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"



# 2. Write a test_start() function that uses function parametrization to test the three test cases.

@pytest.mark.parametrize(
  "start_summary, start_state",
  [
    ("Post on Twitter", "done"),
    ("Write to my dad", "in prog"),
    ("Clean my room", "todo"),
  ],
)
def test_start_function(cards_db, start_summary, start_state):
  c = Card(summary=start_summary, state=start_state)
  index = cards_db.add_card(c)
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"



# 3. Rewrite test_start() using fixture parametrization.

@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
  return request.param

def test_start_fixtures(cards_db, start_state):
  c = Card("Go to market", state=start_state)
  index = cards_db.add_card(c)
  cards_db.start(index)
  card = cards_db.get_card(index)
  assert card.state == "in prog"



# Rewrite test_start() using pytest_generate_tests.

def pytest_generate_tests(metafunc):
    if 'start_state' in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])

@pytest.mark.start_states
def test_start(cards_db, start_state):
    c = Card("Go fishing", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
