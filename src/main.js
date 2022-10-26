/**
 * Huffman coding part
 */
import {huffmanScheme} from './lib/huffman.js'
import {huffmanExtension} from './lib/huffmanExtensionCode.js'
import {getAverageLengthFromMarkov} from './lib/huffmanMarkovCode.js'
import {getAverageLength, getIndexEncoding} from './lib/huffmanUlti.js'
import {calKraftMillan, findMissing, getMinimumRadix} from './lib/kraft-Millan.js'
import {findUniqueDecodable} from './lib/uniqueDecodable.js'

/**
 * Question 1
 * Use format
 */
/* let ans = findUniqueDecodable(["10", "00", "0100"], ["0010", "0", "1000", "01", "011"], true);
console.log(ans); */

/**
 * Question 2
 * Use format
 */
let ans = findMissing([1, 1, 2, 3], 19/32, 4);
console.log(ans);

/**
 * Question 3
 * 
 */
/* let ans = getMinimumRadix([1, 1, 2, 3, 3, 3]);
console.log(ans); */

/**
 * Question 4
 */
/* let scheme = huffmanScheme([4/13, 4/13, 4/13, 1/13], 2);
console.log(getAverageLength(scheme)); */

/**
 * Question 5 is in c++
 */

/**
 * Question 6 is theory
 */

/**
 * Question 7
 */
/* let scheme = huffmanExtension([2/3, 1/3], 2, 3);
console.log(getIndexEncoding(scheme, "s2s2")); */

/**
 * Question 8
 * - Variation: Ask to encode, theory
 */

/**
 * Question 9 is in c++
 */

/**
 * Question 10 is in c++
 */