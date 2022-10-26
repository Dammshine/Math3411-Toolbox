

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
  console.log(sumLength);
  return getFraction(sumLength.toFixed(8));
}

export function getFraction(decimal) {
  for(var denominator = 1; (decimal * denominator) % 1 !== 0; denominator++);
  return {numerator: decimal * denominator, denominator: denominator};
}

export function getIndexEncoding(huffmanScheme, str) {
  return huffmanScheme.encoding[huffmanScheme.indexMap[str]];
}

import {huffmanScheme} from './huffman.js'

/* let scheme = huffmanScheme([2/13, 2/13, 2/13, 2/13, 2/13, 2/13, 1/13], 4);
console.log(scheme); */
/* console.log(getAverageLength(scheme));  */
/*console.log(getIndexEncoding(scheme, 's2'));  */