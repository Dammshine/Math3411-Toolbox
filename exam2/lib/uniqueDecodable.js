/**
 * 
 * @param {*} codewords a list of string represent current code words
 * @param {*} code a string representing the code check
 * @param {*} arr use to store attempts
 */
function pickOne(codewords) {
  let idx = Math.floor(Math.random() * codewords.length);
  return codewords[idx];
}

function checkUniqueDecodableHelper(codewords, code, arr) {
  // If one code can be express by the other, then it's not uniquely decodable
  // Otherwise it is

  // Base case
  if (arr.length > (code.length * 2)) return true;
 

  // Check current
  let str = "";
  for (let idx of arr) str += codewords[idx]; 
  if (str.length > code.length) return true;
  // console.log(codewords, code, str);
  for (let i = 1; i <= Math.ceil(str.length / code.length); i++) {
    if (i > 1) {
      for (let j = 0; j < codewords.length; j++) {
        if (str === code.repeat(i - 1) + codewords[j] 
        || str === codewords[j] + code.repeat(i - 1)
        || str === code.repeat(i)) {
          return false;
        }

        for (let ran = 0; ran < 10; ran++) {
          if (str === code + pickOne(codewords).repeat(i - 1)) {
            return false;
          }
        }
      }
    }
    if (str === code.repeat(i)) {
      /* console.log(arr);
      console.log(codewords, code); */
      return false;
    }
  }
  

  // Check all possible outcome
  for (let i = 0; i < codewords.length; i++) {
    arr.push(i);
    if (!checkUniqueDecodableHelper(codewords, code, arr)) return false;
    arr.pop();
  }
  // console.log("here");
  return true;
}

/**
 * 
 * @param {*} codewords a list of string represent current code words
 * @param {*} code a string representing the code check
 * @param {*} arr use to store attempts
 */
function checkUniqueDecodable(codewords, code, arr) {
  codewords = [...codewords];
  if (!checkUniqueDecodableHelper(codewords, code, [])) return false;

  for (let word of codewords) {
    let copy = [...codewords, code];
    copy = copy.filter(function(item) {
      return word !== item;
    });
    if (!checkUniqueDecodableHelper(copy, word, [])) return false;
  }
  return true;
}

export function findUniqueDecodable(codewords, options, isDecodable=true) {
  // To make it decodable
  for (let code of options) {
    // console.log("here");
    if (checkUniqueDecodable(codewords, code, []) === isDecodable) return code;
  }
  return "Not found";
}

// Sardinas-Patterson Algorithm
