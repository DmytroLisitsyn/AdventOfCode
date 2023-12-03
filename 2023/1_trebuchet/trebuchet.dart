import 'dart:convert';
import 'dart:io';

void main() async {
  final lines1 = await readLines('input1.txt');
  final calibrationSum = findCalibrationSum(lines1);
  print(calibrationSum);

  final lines2 = await readLines('input2.txt');
  final calibrationSum2 = findCalibrationSumIncludingWords(lines2);
  print(calibrationSum2);
}

int findCalibrationSum(List<String> lines) {
  int calibrationSum = 0;

  for (final line in lines) {
    final query = RegExp(r'\d');
    final ns = query.allMatches(line).map((e) => e.group(0) ?? '');
    final cvs = ns.first + ns.last;
    calibrationSum += int.tryParse(cvs) ?? 0;
  }

  return calibrationSum;
}

int findCalibrationSumIncludingWords(List<String> lines) {
  int calibrationSum = 0;

  const digits = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
  ];
  final regexString =
      ([r'\d'] + digits).reduce((value, element) => value + '|' + element);
  final query = RegExp(regexString);

  for (final line in lines) {
    final firstMatch = query.firstMatch(line)?.group(0) ?? '';

    final lastMatchIndex = line.lastIndexOf(query);
    final lastMatch =
        query.firstMatch(line.substring(lastMatchIndex))?.group(0) ?? '';

    final ns = [firstMatch, lastMatch].map((e) {
      final number = int.tryParse(e);
      if (number != null) {
        return '$number';
      } else {
        return '${digits.indexOf(e)}';
      }
    }).reduce((value, element) => value + element);

    final cvs = ns.substring(0, 1) + ns.substring(ns.length - 1);
    calibrationSum += int.parse(cvs);
  }

  return calibrationSum;
}

Future<List<String>> readLines(String filename) async {
  final input = await File(filename).readAsString();
  LineSplitter ls = new LineSplitter();
  final lines = ls.convert(input);
  return lines;
}
