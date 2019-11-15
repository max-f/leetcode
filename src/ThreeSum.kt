fun main(args: Array<String>) {
    val nums: List<Int> = listOf(1, -1, 0, 1, -2, -4)
    val t = ThreeSum()
    val result: List<List<Int>> = t.threeSum(nums)
    result.forEach { triplet -> println(triplet.joinToString(separator = ", ", prefix = "[", postfix = "]")) }
}

class ThreeSum {
    fun threeSum(numbers: List<Int>): List<List<Int>> {
        val input: List<Int> = numbers.sorted()

        val answer: MutableSet<List<Int>> = mutableSetOf()

        for (ax in input.indices) {
            for (bx in ax + 1 until input.size) {
                for (cx in bx + 1 until input.size) {
                    val sum: Int = input[ax] + input[bx] + input[cx]
                    if (sum == 0) {
                        answer.add(listOf(input[ax], input[bx], input[cx]))
                    }
                }
            }
        }
        return answer
            .map { it -> it.toList() }
    }
}
