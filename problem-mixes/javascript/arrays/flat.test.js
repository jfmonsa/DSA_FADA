import { flat } from "./flat.js";
import { test, expect } from "vitest";

// Test suite for the flat function
test("flat", () => {
  expect(flat([1, 2, [3, 4], [5, [6]]], 1)).toEqual([1, 2, 3, 4, 5, [6]]);
  expect(flat([1, 2, [3, 4], [5, [6]]], 1)).toEqual([1, 2, 3, 4, 5, [6]]);
  expect(flat([1, 2, [3, 4], [5, [6]]], 2)).toEqual([1, 2, 3, 4, 5, 6]);
  expect(flat([1, 2, [3, 4], [5, [6]]], Infinity)).toEqual([1, 2, 3, 4, 5, 6]);
  expect(flat([1])).toEqual([1]);
  expect(flat([])).toEqual([]);
  expect(flat([[[[[]]]]])).toEqual([]);
  expect(flat([[[]]])).toEqual([]);
  expect(flat([[[]]], -Infinity)).toEqual([[[]]]);
  expect(flat([[[]]], -1)).toEqual([[[]]]);
  expect(flat([[[]]], -2)).toEqual([[[]]]);
  expect(flat([[[]]], -3)).toEqual([[[]]]);
  expect(flat([[[]]], -Infinity)).toEqual([[[]]]);
  expect(flat([[[]]], -1)).toEqual([[[]]]);
  expect(flat([[[]]], -2)).toEqual([[[]]]);
  expect(flat([[[]]], -3)).toEqual([[[]]]);
  expect(flat([[[]]], -Infinity)).toEqual([[[]]]);
});
