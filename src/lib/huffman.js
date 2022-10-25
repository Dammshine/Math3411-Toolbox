
/**
 * Normalize the probability so array sum equals to 1
 * @param {*} probabilities 
 */
function normalizeProbabilities(probabilities) {
  let currSum = probabilities.reduce((x1, x2) => x1 + x2, 0);
  probabilities.forEach((value, idx) => probabilities[idx] = value / currSum);
  return probabilities;
}

/**
 * Add dummy variable for probability
 * @param {*} probabilities 
 * @param {*} radix 
 */
function addDummy(probabilities, radix) {
  while (probabilities.length % (radix - 1) !== 1 && radix != 2) {
    probabilities.push(0);
  }
  return probabilities;
}

/**
 * Return one object that contain all probability of selected part
 * @param {*} concatenatePart 
 */
function concatenateHuffmanCode(concatenatePart, currPrecedence) {
  let retParts = {
    "index": [],
    "prob": 0,
    "precedence": currPrecedence,
  };
  concatenatePart.forEach(obj => {
    retParts["index"].push(obj);
    retParts["prob"] += obj.prob;
  });
  return retParts;
}

function placeHighSort(lhs, rhs) {
  if (rhs.prob == lhs.prob) return lhs.precedence - rhs.precedence;
  return rhs.prob - lhs.prob;
}

function huffmanSchemeAlgoeGen(encodingTree, dictionary, radix, currArr) {
  if (typeof encodingTree === 'number') {
    dictionary[encodingTree] = currArr.slice(0, currArr.length - 1).join('');
    return;
  }

  // Otherwise break it down
  for (let i = 0; i < encodingTree.index.length; i++) {
    currArr.push(i.toString());
    huffmanSchemeAlgoeGen(encodingTree.index[i], dictionary, radix, currArr);
    currArr.pop();
  }
}

/**
 * Given a probability array, and radix, return the corresponding encoding object
 * @param {*} probabilities 
 * @param {*} radix 
 */
function huffmanSchemeAlgo(probabilities, radix) {
  let mapProabbility = [];
  for (let [index, prob] of probabilities.entries()) {
    mapProabbility.push({
      "index": [index,],
      "precedence": index,
      prob,
    });
  }
  mapProabbility.sort(placeHighSort);

  // Perform the algorithm
  // Use precedence to enforce it perform place-high strategy
  let currPrecedence = -1;
  while (mapProabbility.length > radix) {
    // Pick the last radix nums of entities and concatenate them
    let concatenatePart = mapProabbility.slice(mapProabbility.length - radix);
    mapProabbility = mapProabbility.slice(0, mapProabbility.length - radix);
    
    mapProabbility.push(concatenateHuffmanCode(concatenatePart, currPrecedence));
    mapProabbility.sort(placeHighSort);
    currPrecedence--;
  }
  
  // With map Probability, now can construct the final mapping
  let dictionary = {};
  mapProabbility = {
    "index": [...mapProabbility],
    "precedence": 0,
    "prob": 1,
  };
  let arr = [];
  huffmanSchemeAlgoeGen(mapProabbility, dictionary, radix, arr);
  return dictionary;
}



/**
 * 
 * @param {
 *  probabilities,
 *  radix
 * } 
 *  
 * @return {
 *  probabilities : Array<number>,
 *  radix : number
 *  encoding : @object {
 *    number : string,
 *  }
 * }
 */
export function huffmanScheme(probabilities, radix = 2, mappingCode = undefined) {
  // Step 1: Normalize the probabilities
  probabilities = normalizeProbabilities(probabilities);

  // Step 2: Add dummy variable for probabilities, concatenate them at the end
  probabilities = addDummy(probabilities, radix);

  // Step 3: Perform Huffman encoding algorithm
  let indexMap = {};
  if (mappingCode === undefined) {
    probabilities.forEach((value, idx) => {
      indexMap["s" + (idx + 1).toString()] = idx;
    });
  } else {
    probabilities.forEach((value, idx) => {
      indexMap[mappingCode[idx]] = idx;
    });
  }
  

  return {
    probabilities,
    radix,
    indexMap,
    encoding : huffmanSchemeAlgo(probabilities, radix),
  };
}

// ----------------------------------------------------------------
// Some local testing sanity console.log

// console.log(huffmanScheme([0.3, 0.2, 0.15, 0.05, 0.1, 0.1, 0.075, 0.025], 3).encoding);

