import * as Math from 'mathjs';
const { eigs, multiply, column, transpose, fraction } = Math;

export function calKraftMillan(lens) {
  // Apply kraft-Millan
  // will use math frac to save precision
  let sum = fraction('0/1');
  for (let val of lens) {
    sum = sum.add(fraction(1, Math.floor(Math.pow(2, val)) ));
  }

  return Math.number(sum);
}

/**
 * Question 3
 */
export function findMissing(lens) {
  let finalSpace =  1 - calKraftMillan(lens);
  for (let i = 1; i < 99999; i++) {
    if (Math.pow(2, -i) < finalSpace) return i;
  }
  return -1;
}

console.log(findMissing([1,2,3,4,5,7]));
