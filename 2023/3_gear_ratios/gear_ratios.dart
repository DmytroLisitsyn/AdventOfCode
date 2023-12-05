import '../utilities/utilities.dart';

void main() async {
  final lines1 = await readLines('input1.txt');
  final enginePartsSum = countEnginePartsSum(lines1);
  print(enginePartsSum);

  final lines2 = await readLines('input2.txt');
  final gearRatiosSum = countGearRatiosSum(lines2);
  print(gearRatiosSum);
}

int countEnginePartsSum(List<String> lines) {
  var enginePartsSum = 0;

  for (int i = 0; i < lines.length; i++) {
    final line = lines[i];

    for (final match in RegExp(r'\d+').allMatches(line)) {
      final value = int.parse(match.group(0) ?? '0');
      final j = match.start;
      final length = match.end - j;
      final isPartNumber = checkPartNumber(i, j, length, lines);

      if (isPartNumber) {
        enginePartsSum += value;
      }
    }
  }

  return enginePartsSum;
}

int countGearRatiosSum(List<String> lines) {
  var gearMap = Map<(int, int), List<int>>();
  for (int i = 0; i < lines.length; i++) {
    final line = lines[i];

    for (final match in RegExp(r'\d+').allMatches(line)) {
      final value = int.parse(match.group(0) ?? '0');
      final j = match.start;
      final length = match.end - j;
      final gearIndicatorPlaces = findGearIndicatorPlaces(i, j, length, lines);

      for (final gearIndicator in gearIndicatorPlaces) {
        if (gearMap[gearIndicator] == null) {
          gearMap[gearIndicator] = [value];
        } else {
          gearMap[gearIndicator]?.add(value);
        }
      }
    }
  }

  var gearRatiosSum = 0;

  for (final ratios in gearMap.values) {
    if (ratios.length == 2) {
      gearRatiosSum += ratios[0] * ratios[1];
    }
  }

  return gearRatiosSum;
}

bool checkPartNumber(int row, int column, int length, List<String> lines) {
  final startRow = row - 1 >= 0 ? row - 1 : row;
  final endRow = row + 1 < lines.length ? row + 1 : row;
  final startColumn = column - 1 >= 0 ? column - 1 : column;
  final endColumn =
      column + length < lines[row].length ? column + length : column;

  for (int i = startRow; i <= endRow; i++) {
    for (int j = startColumn; j <= endColumn; j++) {
      final symbol = lines[i][j];
      if (symbol != '.' && int.tryParse(symbol) == null) {
        return true;
      }
    }
  }

  return false;
}

List<(int, int)> findGearIndicatorPlaces(
    int row, int column, int length, List<String> lines) {
  final startRow = row - 1 >= 0 ? row - 1 : row;
  final endRow = row + 1 < lines.length ? row + 1 : row;
  final startColumn = column - 1 >= 0 ? column - 1 : column;
  final endColumn =
      column + length < lines[row].length ? column + length : column;

  List<(int, int)> gearIndicatorPlaces = [];

  for (int i = startRow; i <= endRow; i++) {
    for (int j = startColumn; j <= endColumn; j++) {
      final symbol = lines[i][j];
      if (symbol == '*') {
        gearIndicatorPlaces.add((i, j));
      }
    }
  }

  return gearIndicatorPlaces;
}
