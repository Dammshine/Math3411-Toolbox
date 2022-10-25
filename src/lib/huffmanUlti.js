

/**
 * Get Average Length, as string format, => "4/9, 421/281"
 * @param {*} HuffmanScheme 
 */
export function getAverageLength(huffmanScheme) {
  // I can either perform Knuth algorithm or just use product
  let sumLength = 0;
  for (let [index, str] of Object.entries(huffmanScheme.encoding)) {
    sumLength += (str.length * huffmanScheme.probabilities[index]);
  }
  
  return getFraction(sumLength.toFixed(6));
}

export function getFraction(decimal) {
  for(var denominator = 1; (decimal * denominator) % 1 !== 0; denominator++);
  return {numerator: decimal * denominator, denominator: denominator};
}

export function getIndexEncoding(huffmanScheme, str) {
  return huffmanScheme.encoding[huffmanScheme.indexMap[str]];
}

import {huffmanScheme} from './huffman.js'

/* let scheme = huffmanScheme([0.3, 0.2, 0.15, 0.05, 0.1, 0.1, 0.075, 0.025], 2);
console.log(getAverageLength(scheme)); 
console.log(getIndexEncoding(scheme, 's2'));  */