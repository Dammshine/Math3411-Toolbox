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
/* let ans = findUniqueDecodable(["0", "01", "10"], ["111", "11", "00", "1"], true);
console.log(ans);
 */

/**
 * Question 2
 * - Variation: want code word, then tehory
 * Use format
 */
/* let ans = findMissing([2,3,3], 7/64, 4);
console.log(ans); */

/**
 * Question 3
 * 
 */
/* let ans = getMinimumRadix([1,2,3,4,5,6]);
console.log(ans); */

/**
 * Question 4
 * Get average Length restricted by it's floating point, can use calculator
 */
/* let scheme = huffmanScheme([0.6, 0.1, 0.3], 2);
console.log(scheme) */

//printAverageLength(scheme);
/* console.log(scheme); */
/* console.log(getAverageLength(scheme)); */
 

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
let scheme = huffmanExtension([0.5, 0.25, 0.125, 0.125], 2, 12);
console.log(getAverageLength(scheme))
/* console.log(getIndexEncoding(scheme, "s2s2")); */
/* printAverageLength(scheme); */
/* console.log(scheme); */ 
/* console.log(getAverageLength(scheme)); */

/**
 * Question 8
 * - Variation: Ask to encode, theory
 */
/* let scheme = getAverageLengthFromMarkov([[7/10, 3/10, 1/10], [1/10, 6/10, 4/10], [2/10, 1/10, 5/0]], [16/38, 13/38, 9/38], 2, 6);
printAverageLength(scheme); */

/**
 * Question 9 is in c++
 */

/**
 * Question 10 is in c++
 */