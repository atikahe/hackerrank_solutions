// Finally facing my mortal enemy... Dynamic Programming
// (( found too many coding tests with this question, can't ignore ))

// Ok, but Why DP?
// Bc brute force algorithm has O(n^2) (to produce all possible substring) * O(n) (to check isPalindrome)
// = O(n^3) complexity

// Steps
// 1. Create dp of indices, i = start, j = end
// 2. Because number at the same coordinat is one letter, which is always a palindrome, pre-fill with 1 diagonally
// 3. Check two words combinations
// 4. Other combinations with len >= 3 need to satisfy as follows:
//      a. s[start] == s[end]
//      b. non-boundary substring should be a palindrome

const longestPalindrome = (word) => {
    // Initialize empty matrix
    const len = word.length
    let dp = Array.from(new Array(len), () => new Array(len).fill(0))
    
    // Initialize default vars
    let gap = 0, max = 0
    let longestPalindrome = ''

    // Loop through matrix
    while (gap < len) {
        for (let i = 0; i < len; i++) {
            let j = i + gap
            
            if (j == undefined) break

            if (gap === 0) {
                dp[i][j] = 1
            }
            else if (gap === 1 && word[i] == word[j]) {
                max = gap
                dp[i][j] =  1
            }
            else if (gap >= 2 && word[i] == word[j] && dp[i+1][j-1] === 1 ) {
                max = gap
                dp[i][j] = 1
            }
            else {
                dp[i][j] = 0
            }
        }
        gap += 1
    }

    if (max != 0) {
        for (let k = 0; k < len; k++) {
            let l = k + max
            if (dp[k][l] === 1) longestPalindrome = word.substring(k, l + 1)
        }
    }

    return longestPalindrome

}

console.log(longestPalindrome("aaaabbaa"))