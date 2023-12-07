import 'dart:math';

import '../utilities/file_reading.dart';

void main() async {
  final lines1 = await readLines('input1.txt');
  final result1 = round1(lines1);
  print('Result 1: $result1');

  final lines2 = await readLines('input2.txt');
  final result2 = round2(lines2);
  print('Result 2: $result2');
}

int round1(List<String> lines) {
  var result = 0;
  var cards = mapCards(lines);
  for (final card in cards) {
    final value = card.getValue();
    result += value;
  }
  return result;
}

int round2(List<String> lines) {
  var result = 0;

  var cards = mapCards(lines);
  for (final card in cards) {
    result += countCards(card.id, cards);
  }

  return result;
}

int countCards(int cardID, List<Card> cards) {
  var card = cards
      .cast<Card?>()
      .firstWhere((card) => card?.id == cardID, orElse: () => null);
  if (card == null) {
    return 0;
  }

  var result = 1;

  var copies = card.getWonCopies();
  for (final cardID in copies) {
    result += countCards(cardID, cards);
  }

  return result;
}

List<Card> mapCards(List<String> lines) {
  var cards = <Card>[];

  for (final line in lines) {
    final lc = line.split(':');
    final idString = RegExp(r'\d+').firstMatch(lc[0])?.group(0) ?? "0";
    final numbers = lc[1].split('|');

    var winning = <int>{};
    var own = <int>{};
    for (final match in RegExp(r'\d+').allMatches(numbers[0])) {
      var value = int.parse(match.group(0)!);
      winning.add(value);
    }
    for (final match in RegExp(r'\d+').allMatches(numbers[1])) {
      var value = int.parse(match.group(0)!);
      own.add(value);
    }

    var card = Card(int.parse(idString), winning: winning, own: own);
    cards.add(card);
  }

  return cards;
}

class Card {
  final int id;
  Set<int> winning;
  Set<int> own;

  Card(this.id, {required this.winning, required this.own});

  int getValue() {
    var merged = Set.from(own);
    merged.retainAll(winning);

    var value = pow(2, merged.length - 1).toInt();
    return value;
  }

  Set<int> getWonCopies() {
    var copies = <int>{};

    var merged = Set.from(own);
    merged.retainAll(winning);

    for (int i = 1; i <= merged.length; i++) {
      copies.add(id + i);
    }

    return copies;
  }

  @override
  int get hashCode => id;

  @override
  bool operator ==(other) {
    if (other is! Card) {
      return false;
    }

    return id == other.id;
  }

  @override
  String toString() {
    return 'Card(id: $id, winning: $winning, own: $own)';
  }
}
