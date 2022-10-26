import * as Math from 'mathjs';
const { eigs, multiply, column, transpose, fraction } = Math;
import {huffmanScheme} from './huffman.js'


/**
 * Get Average Length, as string format, => "4/9, 421/281"
 * @param {*} HuffmanScheme 
 */
export function getAverageLength(huffmanScheme) {
  // I can either perform Knuth algorithm or just use product
  let sumLength = fraction('0/1');
  for (let [key, value] of Object.entries(huffmanScheme.indexMap)) {
    let frac = getFraction(huffmanScheme.probabilities[value]);
    sumLength = sumLength.add(fraction(frac.numerator * huffmanScheme.encoding[value].length, frac.denominator));
    // console.log(frac);
  }

  return sumLength;
}

export function getFraction(decimal) {
  for(var denominator = 1; (decimal * denominator) % 1 !== 0; denominator++);
  return {numerator: decimal * denominator, denominator: denominator};
}

export function getIndexEncoding(huffmanScheme, str) {
  return huffmanScheme.encoding[huffmanScheme.indexMap[str]];
}

export function printAverageLength(huffmanScheme) {
  for (let [key, value] of Object.entries(huffmanScheme.indexMap)) {
    let frac = getFraction(huffmanScheme.probabilities[value]);
    console.log(key + ": "+ huffmanScheme.encoding[value] + " " + frac.numerator + "/" + frac.denominator);
  }
}

import { getAverageLengthFromMarkov } from './huffmanMarkovCode.js';

/* let scheme = huffmanScheme([2/13, 2/13, 2/13, 2/13, 2/13, 2/13, 1/13], 4);
console.log(scheme); */
/* console.log(getAverageLength(scheme));  */
/*console.log(getIndexEncoding(scheme, 's2'));  */