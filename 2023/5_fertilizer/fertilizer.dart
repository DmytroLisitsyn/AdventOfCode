import 'dart:math';

import '../utilities/file_reading.dart';
import '../utilities/closed_range.dart';

void main() async {
  final input1 = await readString('input1.txt');
  final result1 = round1(input1);
  print('Result 1: $result1');

  final input2 = await readString('input2.txt');
  final result2 = round2(input2);
  print('Result 2: $result2');
}

int round1(String input) {
  var almanac = Almanac.fromString(input);
  var paths = <int>[];

  for (final seed in almanac.seeds) {
    int path = seed;

    for (final map in almanac.maps) {
      path = map.mapValue(path);
    }

    paths.add(path);
  }

  var result = paths.reduce(min);
  return result;
}

int round2(String input) {
  var almanac = Almanac.fromString(input);

  var paths = <int>[];

  for (int i = 0; i < almanac.seeds.length; i += 2) {
    var seedRange = ClosedRange(
      start: almanac.seeds[i],
      end: almanac.seeds[i] + almanac.seeds[i + 1] - 1,
    );
    var mapStages = {seedRange};

    for (final map in almanac.maps) {
      var newMapStages = <ClosedRange>{};

      for (final range in mapStages) {
        newMapStages.addAll(map.mapRange(range));
      }

      mapStages = newMapStages;
    }

    if (!mapStages.isEmpty) {
      var path = mapStages.map((e) => e.start).reduce(min);
      paths.add(path);
    }
  }

  var result = paths.length > 0 ? paths.reduce(min) : 0;
  return result;
}

class Almanac {
  List<int> seeds;
  List<STDMap> maps;

  Almanac({required this.seeds, required this.maps});

  Almanac.fromString(String input)
      : seeds = [],
        maps = [] {
    var seedsString = RegExp(r'seeds: [\d ]*\n').firstMatch(input)?.group(0);
    if (seedsString != null) {
      seeds = RegExp(r'\d+')
          .allMatches(seedsString)
          .map((e) => int.parse(e.group(0) ?? '0'))
          .toList();
    }

    for (final mapMatch
        in RegExp(r'[\w-]* map:\n[\d \n]*\n').allMatches(input)) {
      var ranges = <STDRangeMap>[];
      for (final stdMatch
          in RegExp(r'(\d+) (\d+) (\d+)').allMatches(mapMatch.group(0)!)) {
        var values =
            stdMatch.group(0)?.split(' ').map((e) => int.parse(e)).toList();

        var range = STDRangeMap(
          destinationStart: values?[0] ?? 0,
          sourceStart: values?[1] ?? 0,
          length: values?[2] ?? 0,
        );
        ranges.add(range);
      }

      var map = STDMap(rangeMaps: ranges);
      maps.add(map);
    }
  }

  @override
  String toString() {
    return 'Almanac(seeds: $seeds, maps: $maps)';
  }
}

class STDMap {
  List<STDRangeMap> rangeMaps;

  STDMap({required this.rangeMaps});

  int mapValue(int value) {
    for (final range in rangeMaps) {
      var mapped = range.mapValue(value);
      if (mapped != null) {
        return mapped;
      }
    }

    return value;
  }

  List<ClosedRange> mapRange(ClosedRange range) {
    var result = <ClosedRange>[];
    var ignoredRanges = {range};

    for (final rangeMap in rangeMaps) {
      var newIgnoredRanges = <ClosedRange>{};

      for (final ignoredRange in ignoredRanges) {
        var r = rangeMap.mapRange(ignoredRange);
        if (r.mapped != null) {
          result.add(r.mapped!);
        }

        newIgnoredRanges.addAll(r.ignored);
      }

      ignoredRanges = newIgnoredRanges;
    }

    result.addAll(ignoredRanges);
    return result;
  }

  @override
  String toString() {
    return 'STDMap(rangeMaps: $rangeMaps)';
  }
}

class STDRangeMapResult {
  ClosedRange? mapped;
  List<ClosedRange> ignored = [];
}

class STDRangeMap {
  int sourceStart;
  int destinationStart;
  int length;

  STDRangeMap({
    required this.sourceStart,
    required this.destinationStart,
    required this.length,
  });

  int? mapValue(int value) {
    var mapped = value - sourceStart;
    if (mapped < 0 || mapped >= length) {
      return null;
    }

    mapped += destinationStart;
    return mapped;
  }

  STDRangeMapResult mapRange(ClosedRange range) {
    var result = STDRangeMapResult();

    var sourceRange =
        ClosedRange(start: sourceStart, end: sourceStart + length - 1);
    var intersection = range.intersection(sourceRange);
    if (intersection != null) {
      var start = intersection.start - sourceStart + destinationStart;
      var end = intersection.end - sourceStart + destinationStart;
      result.mapped = ClosedRange(start: start, end: end);
      result.ignored = range.cut(sourceRange);
    } else {
      result.ignored = [range];
    }

    return result;
  }

  List<ClosedRange> unmappableAreas(ClosedRange range) {
    var sourceRange =
        ClosedRange(start: sourceStart, end: sourceStart + length - 1);
    return range.cut(sourceRange);
  }

  @override
  String toString() {
    return 'STDRangeMap(source: $sourceStart, destination: $destinationStart, length: $length)';
  }
}
