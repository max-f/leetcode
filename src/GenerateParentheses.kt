import java.util.*

// Example: n = 3
/*[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]*/

/*
abc
acb
bac
bca
cba
cab
 */

fun main(args: Array<String>) {
    val G = GenerateParentheses()
    G.generateParenthesis(3)
}

class GenerateParentheses {
    fun generateParenthesis(n: Int): List<String> {
        val permutations: List<String> = createPermutations("()".repeat(n).toList())
        val finalResult : MutableList<String> = mutableListOf()
        for (variant in permutations) {
            val pStack: Stack<Char> = Stack()
            for (c in variant) {
                if (c == '(') {
                    pStack.push(c)
                } else if (!pStack.empty()) {
                    pStack.pop()
                }
            }
            if (pStack.empty()) {
                finalResult.add(variant)
            }
        }

        return finalResult
    }

    private fun createPermutations(l: List<Char>): List<String> {
        if (l.size <= 1) return listOf(l.joinToString())
        val permutations: MutableSet<String> = mutableSetOf()
        for (i in l.indices) {
            val currentChar: Char = l[i]
            for (sublist in createPermutations(l.subList(0, i) + (l.subList(i + 1, l.size)))) {
                permutations.add(currentChar + sublist)
            }
        }
        return permutations.toList()
    }
}