import 'dart:convert';
import 'dart:io';

Future<List<String>> readLines(String filename) async {
  final input = await readString(filename);
  LineSplitter ls = new LineSplitter();
  final lines = ls.convert(input);
  return lines;
}

Future<String> readString(String filename) async {
  final input = await File(filename).readAsString();
  return input;
}
