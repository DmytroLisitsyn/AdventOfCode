import 'dart:math';

class ClosedRange {
  int start;
  int end;

  int get length => start - end + 1;

  ClosedRange({required this.start, required this.end});

  ClosedRange? intersection(ClosedRange other) {
    if (start > other.end || other.start > end) {
      return null;
    } else {
      return ClosedRange(
        start: max(start, other.start),
        end: min(end, other.end),
      );
    }
  }

  List<ClosedRange> cut(ClosedRange area) {
    var pieces = <ClosedRange>[];

    if (area.start > this.start && area.end < this.end) {
      pieces.add(ClosedRange(start: this.start, end: area.start - 1));
      pieces.add(ClosedRange(start: area.end + 1, end: this.end));
    } else if (area.start <= this.start && area.end < this.end) {
      pieces.add(ClosedRange(start: area.end + 1, end: this.end));
    } else if (area.start > this.start && area.end >= this.end) {
      pieces.add(ClosedRange(start: this.start, end: area.start - 1));
    }

    return pieces;
  }

  @override
  int get hashCode => '${start}_${end}'.hashCode;

  @override
  bool operator ==(other) {
    if (other is! ClosedRange) {
      return false;
    }

    return start == other.start && end == other.end;
  }

  @override
  String toString() {
    return 'ClosedRange(start: $start, end: $end)';
  }
}
