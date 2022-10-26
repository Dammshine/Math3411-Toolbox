/**
 * Huffman coding part
 */
import {huffmanScheme} from './lib/huffman.js'
import {huffmanExtension} from './lib/huffmanExtensionCode.js'
import {getAverageLengthFromMarkov} from './lib/huffmanMarkovCode.js'
import {getAverageLength, getIndexEncoding, printAverageLength} from './lib/huffmanUlti.js'
import {calKraftMillan, findMissing, getMinimumRadix} from './lib/kraft-Millan.js'
import {findUniqueDecodable} from './lib/uniqueDecodable.js'

/**
 * Question 1
 * Use format
 */
let ans = findUniqueDecodable(["01", "111", "011"], ["11", "010", "0", "00"], false);
console.log(ans);

/**
 * Question 2
 * - Variation: want code word, then tehory
 * Use format
 */
/* let ans = findMissing([2,2,3,3,3,4], 1, 2);
console.log(ans); */

/**
 * Question 3
 * 
 */
/* let ans = getMinimumRadix([1, 1, 2, 3, 3, 3]);
console.log(ans); */

/**
 * Question 4
 * Get average Length restricted by it's floating point, can use calculator
 */
/* let scheme = huffmanScheme([5/11, 2/11, 1/11, 1/11, 1/11, 1/11], 3);
console.log(scheme.encoding)
console.log(getAverageLength(scheme)); */

/**
 * Question 5 decode is in c++
 * - Variation: encode do it by hand
 */

/**
 * Question 6 is theory
 */

/**
 * Question 7
 */
/* let scheme = huffmanExtension([2/3, 1/3], 3, 3);
// console.log(getIndexEncoding(scheme, "s2s2"));
printAverageLength(scheme) */
//console.log(getAverageLength(scheme)); 

/**
 * Question 8
 * - Variation: Ask to encode, theory
 */
/* let scheme = getAverageLengthFromMarkov([[1/10, 1/10, 1/2], [7/10, 3/10, 1/10], [1/5, 3/5, 2/5]], [9/34, 11/34, 7/14], 2, 6);
console.log(getAverageLength(scheme)); */

/**
 * Question 9 is in c++
 */

/**
 * Question 10 is in c++
 */