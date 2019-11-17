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
//    val result: List<String> = G.createPermutations(listOf('a', 'b', 'c'))
//    result.forEach { println(it) }
    G.generateParenthesis(2)
}

class GenerateParentheses {
    fun generateParenthesis(n: Int): List<String> {
        val result: List<String> = listOf(")((())")
        val finalResult : MutableList<String> = mutableListOf()
        for (variant in result) {
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


        finalResult.forEach { println(it) }

        return listOf()
    }

    fun createPermutations(l: List<Char>): List<String> {
        if (l.size <= 1) return listOf(l.joinToString())
        val permutations: MutableList<String> =  mutableListOf()
        for (i in l.indices) {
            val currentChar: Char = l[i]
            for (sublist in createPermutations(l.subList(0, i) + (l.subList(i + 1, l.size)))) {
                permutations.add(currentChar + sublist)
            }
        }
        return permutations
    }
}