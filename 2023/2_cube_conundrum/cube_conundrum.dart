import 'dart:math';

import '../utilities/file_reading.dart';

void main() async {
  final lines1 = await readLines('input1.txt');
  final possibleGamesSum = makePossibleGames(lines1);
  print(possibleGamesSum);

  final lines2 = await readLines('input2.txt');
  final minAmountOfCubesPower = findMinAmountOfCubesPower(lines2);
  print(minAmountOfCubesPower);
}

int makePossibleGames(List<String> lines) {
  int possibleGamesSum = 0;

  final games = mapGames(lines);
  for (final game in games) {
    if (game.isPossible()) {
      possibleGamesSum += game.id;
    }
  }

  return possibleGamesSum;
}

int findMinAmountOfCubesPower(List<String> lines) {
  int minAmountOfCubesPower = 0;

  final games = mapGames(lines);
  for (final game in games) {
    final reds = game.rounds.map((e) => e.redCount).cast<num>().reduce(max);
    final greens = game.rounds.map((e) => e.greenCount).cast<num>().reduce(max);
    final blues = game.rounds.map((e) => e.blueCount).cast<num>().reduce(max);
    final power = reds * greens * blues;
    minAmountOfCubesPower += power.toInt();
  }

  return minAmountOfCubesPower;
}

List<Game> mapGames(List<String> lines) {
  List<Game> games = [];

  for (final line in lines) {
    final lc = line.split(':');
    final gameString = RegExp(r'\d+').firstMatch(lc[0])?.group(0) ?? "0";

    List<GameRound> rounds = [];

    final rawRounds = lc[1].split(';');
    for (final rawRound in rawRounds) {
      final redString =
          RegExp(r'(\d+) red').firstMatch(rawRound)?.group(1) ?? "0";
      final greedString =
          RegExp(r'(\d+) green').firstMatch(rawRound)?.group(1) ?? "0";
      final blueString =
          RegExp(r'(\d+) blue').firstMatch(rawRound)?.group(1) ?? "0";

      final round = GameRound(
        redCount: int.parse(redString),
        greenCount: int.parse(greedString),
        blueCount: int.parse(blueString),
      );

      rounds.add(round);
    }

    var game = Game(int.parse(gameString));
    game.rounds = rounds;
    games.add(game);
  }

  return games;
}

class Game {
  final int id;
  List<GameRound> rounds;

  Game(this.id, {this.rounds = const []});

  bool isPossible() {
    for (final round in rounds) {
      if (round.redCount > 12) return false;
      if (round.greenCount > 13) return false;
      if (round.blueCount > 14) return false;
    }

    return true;
  }

  @override
  String toString() {
    return 'Game(id: $id, rounds: $rounds)';
  }
}

class GameRound {
  int redCount;
  int greenCount;
  int blueCount;

  GameRound({this.redCount = 0, this.greenCount = 0, this.blueCount = 0});

  @override
  String toString() {
    return 'GameRound(red: $redCount, green: $greenCount, blue: $blueCount)';
  }
}
