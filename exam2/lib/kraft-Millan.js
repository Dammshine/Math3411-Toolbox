import * as Math from 'mathjs';
import { i, to } from 'mathjs';
const { eigs, multiply, column, transpose, fraction } = Math;

export function calKraftMillan(lens, radix=2) {
  // Apply kraft-Millan
  // will use math frac to save precision
  let sum = fraction('0/1');
  for (let val of lens) {
    sum = sum.add(fraction(1, Math.floor(Math.pow(radix, val)) ));
  }

  return Math.number(sum);
}

/**
 * Question 3
 */
export function findMissing(lens, sum = 1, radix=2) {
  let finalSpace =  sum - calKraftMillan(lens, radix);
  for (let i = 1; i < 99999; i++) {
    if (Math.pow(radix, -i) <= finalSpace) return i;
  }
  return -1;
}

export function getMinimumRadix(lens) {
  for (let i = 2; i < 99999; i++) {
    if (calKraftMillan(lens, i) <= 1) return i;
  }
  return -1;
}

/* 
console.log(findMissing([1,2,3,4,5,7])); */


