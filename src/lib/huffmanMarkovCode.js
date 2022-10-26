import * as Math from 'mathjs';
const { eigs, multiply, column, transpose } = Math;
import {huffmanScheme} from './huffman.js'
import {getIndexEncoding, getAverageLength, getFraction} from './huffmanUlti.js'
/**
 * Question 8
 * - A function able to get equlibrium status
 * - A function per average codeword length
 */

/**
 * Return a array of probability, normalized and is matrix's equalibrium
 * also known as eigen value
 * Failed to resolve percision issue
 */
/* export function getEqulibrium(matrix) {
  let equVec = eigs(matrix).vectors;
  console.log(equVec);
  let sum = equVec.reduce((a, b) => a + b, 0);
  equVec.forEach((val, idx) => equVec[idx] /= sum);
  return equVec;
}

console.log(getEqulibrium([
  [7/5 , 3/5 , 1/2 ],
  [1/10, 3/10, 1/10],
  [1/5 , 1/10, 2/5 ],
]));
 */
export function getAverageLengthFromMarkov(matrix, equlibrumVec, radix = 2, precision=6) {
  matrix = Math.transpose(matrix);
  let sum = 0;
  for (let columns in matrix) {
    console.log(matrix[columns]);
    let len = getAverageLength(huffmanScheme(matrix[columns], radix))
    sum += len['numerator'] * equlibrumVec[columns] / len['denominator'];
  }
  // console.log(sum);
  return getFraction(sum.toFixed(6));
}


/* console.log(getAverageLengthFromMarkov([
  [7/10 , 3/5 , 1/2 ],
  [1/10, 3/10, 1/10],
  [1/5 , 1/10, 2/5 ],
], [41/64, 1/8, 15/64], 2, 6)); */
