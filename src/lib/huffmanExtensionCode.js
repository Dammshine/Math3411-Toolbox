function huffmanRecursive(probabilities, newProbabilities, extension, digits) {
  if (extension === 0) {
    let calProb = 1;
    let strRep = "";
    for (let i of digits) {
      calProb *= probabilities[i];
      strRep += 's' + (i+1).toString();
    }
    newProbabilities[strRep] = calProb;
    return;
  }

  for (let i = 0; i < probabilities.length; i++) {
    digits.push(i);
    huffmanRecursive(probabilities, newProbabilities, extension - 1, digits);
    digits.pop();
  }
}


import {huffmanScheme} from './huffman.js'
import {getIndexEncoding, getAverageLength} from './huffmanUlti.js'

/**
 * This function is for Question 7
 * Let S={s1,s2} be a source with probabilities p1=3/4,p2=1/4.
 * Find the codeword in the radix 3 Huffman code for the 3rd extension S(3) that encodes the symbol s2s2s2?
 */
export function huffmanExtension(probabilities, extension, radix) {
  // Using a map to map the new probability entries to it's encoding
  let finalDictionary = {};
  huffmanRecursive(probabilities, finalDictionary, extension, []);

  // Get array formated probabilities and probabilities
  let finalProbabilities = [];
  let finalCode = [];
  for (let [key, value] of Object.entries(finalDictionary)) {
    finalProbabilities.push(value);
    finalCode.push(key);
  }

  return huffmanScheme(finalProbabilities, radix, finalCode);
}

let scheme = huffmanExtension([0.80, 0.20], 2, 3);
console.log(getIndexEncoding(scheme, 's2s2'));