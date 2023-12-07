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
  var result = 1;

  final document = Document.fromLines(lines);
  for (final race in document.races) {
    result *= race.getSolutionsCount();
  }

  return result;
}

int round2(List<String> lines) {
  var result = 1;

  final document = Document.fromLines(lines);
  for (final race in document.races) {
    result *= race.getSolutionsCount();
  }

  return result;
}

class Document {
  List<Race> races = [];

  Document.fromLines(List<String> lines) {
    final times = RegExp(r'\d+')
        .allMatches(lines[0])
        .map((e) => int.parse(e.group(0) ?? '0'))
        .toList();
    final distances = RegExp(r'\d+')
        .allMatches(lines[1])
        .map((e) => int.parse(e.group(0) ?? '0'))
        .toList();

    var races = <Race>[];
    for (int i = 0; i < times.length; i++) {
      var race = Race();
      race.time = times[i];
      race.distance = distances[i];
      races.add(race);
    }

    this.races = races;
  }

  @override
  String toString() {
    return 'Document(races: $races)';
  }
}

class Race {
  int time = 0;
  int distance = 0;

  int getSolutionsCount() {
    var loses = 0;
    for (int t = 0; t <= time; t++) {
      final outcome = (time - t) * t;

      if (outcome > distance) {
        break;
      } else {
        loses += 1;
      }
    }

    final wins = time + 1 - loses * 2;
    return wins;
  }

  @override
  String toString() {
    return 'Race(time: $time, distance: $distance)';
  }
}
